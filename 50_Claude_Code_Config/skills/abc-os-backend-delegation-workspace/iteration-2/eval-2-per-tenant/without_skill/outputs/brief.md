# A2 → A3 Brief: Add `user_task_progress` Per-Tenant Table to `abc_os`

**Eval**: eval-2-per-tenant · `add-per-tenant-table`
**From**: Claude Code (A2, Orchestrator)
**To**: A3 sub-agent (executor) — Supabase/Postgres technical
**Doctrine anchors**: `ADR-META-001` (D1–D8, Anti-Paresse), `ADR-ABCOS-001` D10 (mixed-tenancy), `AGENTS.md` Canon
**Classification**: **D10 — PER-TENANT** table (scoped by `org_id`; tenancy via `current_org_id()`)

---

## 1. Intent (A0 → A2)

Add a new `abc_os.user_task_progress` table to the **VPS Supabase `abc_os` schema (dev target)**, model the existing per-tenant pattern (`0002_rls_policies.sql` → `action_items`), apply with `FORCE_TARGET=1`, run D1 verify, write back to the 3 memory files.

**Doctrinal grounding**:

- **ADR-META-001 D1–D8** — *Verify before assert*. D1: every claim must be backed by a query result captured this session. D2: no literal-derivation masquerading as verification. D7: cross-DB reality check before declaring success.
- **ADR-ABCOS-001 D10** — Mixed-tenancy rule: any table with `org_id` + `member_id` is **per-tenant**. RLS MUST gate on `current_org_id()` and `current_role()`. Mixed rows between orgs = **silent data leak** → CRITICAL.
- **AGENTS.md Canon** — Identity (`00_Amadeus/01_Identity_Core`) ≠ Runtime ≠ Config. Migration files live in repo (Runtime), never in Canon.

---

## 2. DDL — Migration `0014_user_task_progress.sql` (new)

Create the file in the migrations directory (path discovered by `apply-abc-os-migrations.sh` — see §3):

```sql
-- 0014_user_task_progress.sql
-- Per-tenant (D10) — gated by abc_os.current_org_id() + abc_os.current_role()
-- Pattern: mirrors action_items in 0002_rls_policies.sql

BEGIN;

-- pgcrypto already enabled in 0000_init; gen_random_uuid() is available.
-- If you hit "function gen_random_uuid() does not exist", run:
--   CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS abc_os.user_task_progress (
  id           UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id       TEXT         NOT NULL REFERENCES abc_os.organizations(id) ON DELETE CASCADE,
  member_id    UUID         NOT NULL REFERENCES abc_os.members(id)        ON DELETE CASCADE,
  task_id      TEXT         NOT NULL REFERENCES abc_os.build_tasks(id)     ON DELETE CASCADE,
  status       TEXT         NOT NULL CHECK (status IN ('pending','in_progress','done')),
  started_at   TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT now()
);

-- Indexes aligned with the per-tenant read paths (org-scoped + member-scoped)
CREATE INDEX IF NOT EXISTS user_task_progress_org_id_idx
  ON abc_os.user_task_progress (org_id);
CREATE INDEX IF NOT EXISTS user_task_progress_member_id_idx
  ON abc_os.user_task_progress (member_id);
CREATE INDEX IF NOT EXISTS user_task_progress_task_id_idx
  ON abc_os.user_task_progress (task_id);

ALTER TABLE abc_os.user_task_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE abc_os.user_task_progress FORCE  ROW LEVEL SECURITY;

-- ── RLS policies (4 — SELECT / INSERT / UPDATE / DELETE) ────────────────────
-- Convention: current_org_id() returns the org from the JWT claim;
--             current_role()  returns the Postgres role of the caller.
--             (Both are defined in 0001_helpers.sql of the abc_os schema.)

DROP POLICY IF EXISTS utp_select ON abc_os.user_task_progress;
CREATE POLICY utp_select ON abc_os.user_task_progress
  FOR SELECT
  USING (
    current_role() IN ('anon','authenticated','service_role')
    AND org_id = current_org_id()
  );

DROP POLICY IF EXISTS utp_insert ON abc_os.user_task_progress;
CREATE POLICY utp_insert ON abc_os.user_task_progress
  FOR INSERT
  WITH CHECK (
    current_role() IN ('authenticated','service_role')
    AND org_id = current_org_id()
  );

DROP POLICY IF EXISTS utp_update ON abc_os.user_task_progress;
CREATE POLICY utp_update ON abc_os.user_task_progress
  FOR UPDATE
  USING      (org_id = current_org_id() AND current_role() IN ('authenticated','service_role'))
  WITH CHECK (org_id = current_org_id() AND current_role() IN ('authenticated','service_role'));

DROP POLICY IF EXISTS utp_delete ON abc_os.user_task_progress;
CREATE POLICY utp_delete ON abc_os.user_task_progress
  FOR DELETE
  USING (
    current_role() IN ('authenticated','service_role')
    AND org_id = current_org_id()
  );

COMMIT;
```

**Pattern conformance with `0002_rls_policies.sql → action_items`**: 4 policies (SELECT/INSERT/UPDATE/DELETE), `FORCE ROW LEVEL SECURITY` on, gating on `current_org_id()` + `current_role()` — identical shape.

---

## 3. `apply-abc-os-migrations.sh` update

Add a new branch (or a `*)` case) so the new file is applied **only** when `FORCE_TARGET=1` is set and the file is numbered `0014_…`:

```bash
# In apply-abc-os-migrations.sh, inside the case that matches migration files:
0014_*)   psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -f "$MIG_DIR/0014_user_task_progress.sql" ;;
```

**Invariants**:

- `FORCE_TARGET=1` env var must be exported before invocation (per eval prompt).
- Idempotent (`CREATE TABLE IF NOT EXISTS`, `DROP POLICY IF EXISTS`, `CREATE INDEX IF NOT EXISTS`) — re-running is safe.
- Wrapped in a single `BEGIN; … COMMIT;` so a failed statement rolls back the whole migration.

---

## 4. D1 Verify Queries (post-apply, all must be captured as evidence)

Run every one of these on the **dev** Supabase. Paste results verbatim in the A3 → A2 report (D1 = verify-before-assert).

```sql
-- Q1. Table exists, RLS forced, gen_random_uuid() default wired
SELECT
  c.relname                            AS table_name,
  c.relrowsecurity                     AS rls_enabled,
  c.relforcerowsecurity                AS rls_forced,
  pg_get_triggerdef(oid)               -- (defensive: confirm no stray triggers)
FROM pg_class c
WHERE c.relname = 'user_task_progress'
  AND c.relnamespace = 'abc_os'::regnamespace;

-- Q2. Exactly 4 policies, all on user_task_progress
SELECT polname, polcmd, polpermissive
FROM pg_policy
WHERE polrelid = 'abc_os.user_task_progress'::regclass
ORDER BY polname;

-- Q3. gen_random_uuid() resolves (pgcrypto)
SELECT gen_random_uuid() AS sample_uuid;

-- Q4. Expected global post-apply counts
SELECT
  (SELECT count(*) FROM information_schema.tables
     WHERE table_schema = 'abc_os')                                AS tables_count,
  (SELECT count(*) FROM pg_class c
     WHERE c.relnamespace = 'abc_os'::regnamespace
       AND c.relkind = 'r' AND c.relrowsecurity)                   AS rls_count,
  (SELECT count(*) FROM pg_policy p
     JOIN pg_class c ON c.oid = p.polrelid
     WHERE c.relnamespace = 'abc_os'::regnamespace)                AS policies_count,
  (SELECT count(*) FROM abc_os.schema_migrations
     WHERE filename = '0014_user_task_progress.sql')               AS migration_logged;

-- Q5. Migration row appended
SELECT version, filename, applied_at
FROM abc_os.schema_migrations
ORDER BY version DESC
LIMIT 3;
```

**Expected values** (post-apply, **dev** target):

| Counter | Expected | Why |
|---|---|---|
| `tables_count`  | **19** | 18 existing + `user_task_progress` |
| `rls_count`     | **19** | All `abc_os` tables RLS-enabled |
| `policies_count`| **47** | 43 existing + 4 new (`utp_*`) |
| `migration_logged` | **1** | one row for `0014_…` |
| Total `schema_migrations` rows | **14** | 13 prior + 1 new |

If any count diverges, **STOP** and report — do not declare success (D1, D2).

---

## 5. RLS Effectiveness Spot-Checks (must all behave as specified)

Use Supabase's `anon` and `authenticated` roles; switch `request.jwt.claims.org_id` and `request.jwt.claims.role` to simulate tenancy. Each test must show the **expected** outcome:

```sql
-- SETUP (run once in a transaction; rollback after)
-- 1) Insert one row in org_A and one in org_B (use service_role; bypasses RLS)
SET LOCAL ROLE service_role;
INSERT INTO abc_os.user_task_progress (org_id, member_id, task_id, status)
VALUES ('org_A', '<member_A_uuid>', '<task_1>', 'pending'),
       ('org_B', '<member_B_uuid>', '<task_1>', 'pending');
RESET ROLE;

-- S1. anon role → no rows visible (deny-by-default)
SET LOCAL ROLE anon;
SELECT count(*) AS visible_rows FROM abc_os.user_task_progress;
-- EXPECTED: 0
RESET ROLE;

-- S2. authenticated, current_org_id() = 'org_A' → 1 row
SET LOCAL ROLE authenticated;
SET LOCAL "request.jwt.claims" = '{"sub":"u1","role":"authenticated","org_id":"org_A"}';
SELECT count(*) AS visible_rows FROM abc_os.user_task_progress;
-- EXPECTED: 1 (org_A only)
RESET ROLE;
RESET "request.jwt.claims";

-- S3. authenticated, current_org_id() = 'org_C' (no match) → 0 rows
SET LOCAL ROLE authenticated;
SET LOCAL "request.jwt.claims" = '{"sub":"u2","role":"authenticated","org_id":"org_C"}';
SELECT count(*) AS visible_rows FROM abc_os.user_task_progress;
-- EXPECTED: 0
RESET ROLE;
RESET "request.jwt.claims";

-- S4. authenticated, org_A → INSERT with mismatched org_id → BLOCKED
SET LOCAL ROLE authenticated;
SET LOCAL "request.jwt.claims" = '{"sub":"u3","role":"authenticated","org_id":"org_A"}';
INSERT INTO abc_os.user_task_progress (org_id, member_id, task_id, status)
VALUES ('org_B', '<member_A_uuid>', '<task_2>', 'pending');
-- EXPECTED: ERROR — new row violates row-level security policy (D10)
RESET ROLE;
RESET "request.jwt.claims";

ROLLBACK;
```

**Acceptance**: S1=0, S2=1, S3=0, S4=ERROR. Any other outcome = RLS broken, **CRITICAL**, do not proceed to write-back.

---

## 6. 3-File Write-Back Contract

After D1 + spot-checks all pass, append a row to each of these three files (one-line summary, atomic across the three, idempotent):

1. **`ASpace_OS_V2/_SPECS/ADR/ADR-ABCOS-001_mixed-tenancy.md`** — append to the D10 examples table:
   `| user_task_progress | per-tenant | 0014_… | utp_select/insert/update/delete |`

2. **`ASpace_OS_V2/30_MEMORY_CORE/Memory_Core/abc_os_migrations.md`** — append:
   `2026-06-12 · 0014_user_task_progress · per-tenant · tables=19 rls=19 policies=47 migrations=14`

3. **`ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/abc_os_post_apply.md`** — append a dated block with the Q1–Q5 + S1–S4 results verbatim (D1 evidence). Cite the DDL file path, the apply command, and the exact counts observed.

**No hard-delete** in any of these (Anti-Technicien / Checkpoint doctrine): only append or new dated block.

---

## 7. Execute (A3 only)

```bash
# Pre-flight
[ -z "$SUPABASE_DB_URL" ] && { echo "ABORT: SUPABASE_DB_URL not set"; exit 2; }
[ "$FORCE_TARGET" != "1" ] && { echo "ABORT: FORCE_TARGET must be 1"; exit 2; }

# Apply
FORCE_TARGET=1 ./apply-abc-os-migrations.sh 0014_user_task_progress.sql

# D1 + spot-checks
psql "$SUPABASE_DB_URL" -f ./_evals/0014_verify.sql
psql "$SUPABASE_DB_URL" -f ./_evals/0014_rls_spotchecks.sql

# 3-file write-back (only if all green)
$EDITOR_ASSPACE_ROOT/_SPECS/ADR/ADR-ABCOS-001_mixed-tenancy.md
$EDITOR_ASSPACE_ROOT/30_MEMORY_CORE/Memory_Core/abc_os_migrations.md
$EDITOR_ASSPACE_ROOT/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/abc_os_post_apply.md
```

---

## 8. Deliverable (A3 → A2)

A single report containing:

- Exact `psql` exit codes for apply + verify + spot-checks (all must be 0 or the expected RLS-violation error).
- Q1–Q5 result sets **verbatim** (D1 evidence).
- S1–S4 result sets + error message for S4.
- Confirmation that the 3 memory files were updated (diffs or appended blocks).
- Any anomaly → escalate to L0/Donna DLQ (per AGENTS.md), **do not** patch around it.

---

## 9. Assumptions

- `pgcrypto` is already enabled (it is, per `0000_init`); the brief includes the `CREATE EXTENSION` fallback as a safety net per ADR-META-001 D1.
- `abc_os.current_org_id()` and `abc_os.current_role()` exist and are stable (defined in `0001_helpers.sql`); this brief does **not** redefine them.
- Migration filename pattern is `NNNN_*.sql` and `apply-abc-os-migrations.sh` already dispatches by prefix.
- `abc_os.schema_migrations` exists as the migration ledger (per existing `0002_rls_policies.sql` rollout pattern).
- Dev target = `abc_os` schema on the **VPS Supabase** (per eval prompt); no production migration.
- A3 reports results; A2 reports to A0; A0 validates and ratifies (per AGENTS.md role separation).

**End of brief.**
