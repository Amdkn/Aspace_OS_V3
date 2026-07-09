# A2→A3 SUB-AGENT BRIEF — Per-Tenant `user_task_progress` Migration (eval-2)

> Hand-off from A2 (orchestrator) to A3 (sub-agent, general-purpose, background).
> **A2 does not write SQL or run psql.** A3 owns the apply, verify, and write-back.

---

## 0. A0's intent (verbatim)

> *"Add a new 'user_task_progress' per-tenant table to abc_os on the VPS Supabase. Columns: id UUID PRIMARY KEY default gen_random_uuid(), org_id TEXT NOT NULL REFERENCES abc_os.organizations(id) ON DELETE CASCADE, member_id UUID NOT NULL REFERENCES abc_os.members(id) ON DELETE CASCADE, task_id TEXT NOT NULL REFERENCES abc_os.build_tasks(id) ON DELETE CASCADE, status TEXT NOT NULL CHECK (status IN ('pending', 'in_progress', 'done')), started_at TIMESTAMPTZ, completed_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL default now(). Per-tenant RLS: SELECT/INSERT/UPDATE/DELETE using abc_os.current_org_id() and abc_os.current_role() patterns. Apply to dev with FORCE_TARGET=1. After applying, run D1 verify and write back to the 3 memory files."*

---

## 1. Doctrine anchors (cite in any work product)

- **ADR-META-001 (D1–D8)**: D1 Verify-Before-Assert (raw counts, never assertions), D2 Research-first (mirror `action_items` from `0002_rls_policies.sql`), D3 Nuance over Literal (adapt on drift, don't refuse), D4 No self-contradiction, D6 Root cause (Supabase hardened role → `FORCE_TARGET=1` + ON CONFLICT safety net), D10 Mixed-tenancy (per-tenant vs shared-catalog).
- **ADR-SUPABASE-001 (D3+D4)**: self-hosted multi-tenancy schemas, hardened role discipline.
- **ADR-ABCOS-001 (D10)**: mixed-tenancy precedent — 4 shared-catalog + 2 per-tenant tables already in `abc_os`.

---

## 2. Tenancy classification (D10 decision tree)

**Verdict: PER-TENANT.** The `user_task_progress` row is unique to a member inside a co-op (org-scoped). It carries `org_id` and a `member_id` FK inside the tenant. Do NOT use the shared-catalog pattern (`select-authenticated` only) — that would leak per-tenant progress across orgs.

Follow the **per-tenant pattern from `0002_rls_policies.sql`** (`action_items` table) as the structural template: 4 CRUD policies using `abc_os.current_org_id()` and `abc_os.current_role()`.

---

## 3. Pre-flight (sub-agent responsibility)

- Verify local files exist: `apps/abc-os-community/supabase/migrations/abc_os/0002_rls_policies.sql` (read for the `action_items` per-tenant pattern), `apps/abc-os-community/supabase/scripts/apply-abc-os-migrations.sh`, `apps/abc-os-community/supabase/scripts/lib/db.sh` (for `current_org_id()` / `current_role()` definitions).
- Verify SSH alias `aspace-vps` is reachable.
- Verify `app.env` on VPS (output `dev` vs `prod`); `FORCE_TARGET=1` is the override per A0 HITL precedent (2026-06-11).
- Confirm `pgcrypto` extension is enabled in `abc_os` (it should be — `gen_random_uuid()` requires it; if missing, add a `CREATE EXTENSION IF NOT EXISTS pgcrypto;` line in the new migration).
- Confirm FK targets exist: `abc_os.organizations(id)`, `abc_os.members(id)`, `abc_os.build_tasks(id)`.

---

## 4. New migration file — full DDL

**Filename**: `apps/abc-os-community/supabase/migrations/abc_os/0013_user_task_progress.sql`

**Why `0013`**: next number after the 2026-06-12 baseline (12 logged migrations). Use `0013_` prefix.

```sql
-- 0013_user_task_progress.sql
-- eval-2: per-tenant progress tracking (D10 per-tenant, mirrors action_items RLS pattern)
-- Doctrine: ADR-META-001 D1-D8, ADR-ABCOS-001 D10
-- Idempotent: safe to re-apply via apply-abc-os-migrations.sh

-- pgcrypto required for gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Table
CREATE TABLE IF NOT EXISTS abc_os.user_task_progress (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id       TEXT NOT NULL REFERENCES abc_os.organizations(id) ON DELETE CASCADE,
  member_id    UUID NOT NULL REFERENCES abc_os.members(id) ON DELETE CASCADE,
  task_id      TEXT NOT NULL REFERENCES abc_os.build_tasks(id) ON DELETE CASCADE,
  status       TEXT NOT NULL CHECK (status IN ('pending', 'in_progress', 'done')),
  started_at   TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Indexes (org_id is the hot RLS predicate; member_id + task_id for lookups)
CREATE INDEX IF NOT EXISTS idx_user_task_progress_org_id    ON abc_os.user_task_progress(org_id);
CREATE INDEX IF NOT EXISTS idx_user_task_progress_member_id ON abc_os.user_task_progress(member_id);
CREATE INDEX IF NOT EXISTS idx_user_task_progress_task_id   ON abc_os.user_task_progress(task_id);
CREATE INDEX IF NOT EXISTS idx_user_task_progress_org_task  ON abc_os.user_task_progress(org_id, task_id);

-- RLS enable (idempotent: swallow "already enabled" by guarding in the apply script if needed;
-- 2026-06-12 precedent uses DO block with EXCEPTION handler — match that)
ALTER TABLE abc_os.user_task_progress ENABLE ROW LEVEL SECURITY;

-- =========================================================================
-- Per-tenant RLS policies (4 CRUD) — mirror action_items in 0002_rls_policies.sql
-- Helpers: abc_os.current_org_id() returns the caller's org claim (set via
-- PGOPTIONS='-c app.org_id=...'); abc_os.current_role() returns the caller's
-- app role claim ('owner' | 'admin' | 'member').
-- =========================================================================

-- SELECT — any authenticated member of the org can read
DROP POLICY IF EXISTS user_task_progress_select ON abc_os.user_task_progress;
CREATE POLICY user_task_progress_select ON abc_os.user_task_progress
  FOR SELECT TO authenticated
  USING (org_id = abc_os.current_org_id());

-- INSERT — owner/admin can create; member can self-create
DROP POLICY IF EXISTS user_task_progress_insert ON abc_os.user_task_progress;
CREATE POLICY user_task_progress_insert ON abc_os.user_task_progress
  FOR INSERT TO authenticated
  WITH CHECK (
    org_id = abc_os.current_org_id()
    AND abc_os.current_role() IN ('owner', 'admin', 'member')
  );

-- UPDATE — owner/admin can update any; member can update own (member_id match)
DROP POLICY IF EXISTS user_task_progress_update ON abc_os.user_task_progress;
CREATE POLICY user_task_progress_update ON abc_os.user_task_progress
  FOR UPDATE TO authenticated
  USING (
    org_id = abc_os.current_org_id()
    AND (
      abc_os.current_role() IN ('owner', 'admin')
      OR member_id::text = current_setting('app.member_id', true)
    )
  )
  WITH CHECK (
    org_id = abc_os.current_org_id()
  );

-- DELETE — owner/admin only
DROP POLICY IF EXISTS user_task_progress_delete ON abc_os.user_task_progress;
CREATE POLICY user_task_progress_delete ON abc_os.user_task_progress
  FOR DELETE TO authenticated
  USING (
    org_id = abc_os.current_org_id()
    AND abc_os.current_role() IN ('owner', 'admin')
  );

-- Migration tracker
INSERT INTO abc_os._aspace_migrations (filename) VALUES ('0013_user_task_progress.sql')
  ON CONFLICT (filename) DO NOTHING;
```

> **Note**: `current_setting('app.member_id', true)` is the established 2026-06-12 pattern for member-self-update checks (see `action_items` UPDATE policy). If the canonical pattern in `0002_rls_policies.sql` uses a different predicate (e.g. `(SELECT auth.uid())::uuid`), match it exactly. The D3 doctrine says: **adapt to the local convention, don't invent**.

---

## 5. Apply script update — TWO edit points

**File**: `apps/abc-os-community/supabase/scripts/apply-abc-os-migrations.sh`

### 5a. Pre-flight file list (~line 53)

In the `for f in ...` pre-flight list, add `0013_user_task_progress.sql` to the array in numeric order.

### 5b. `apply_sql` block — dev branch (~line 127)

Inside `if [[ "$TARGET" == "dev" ]]; then`, add an `apply_sql` line for the new file:

```bash
apply_sql "0013_user_task_progress.sql"
```

### 5c. (Optional) `apply_sql` block — prod branch (~line 141)

**Per-tenant schema/RLS = schema-shared, safe for prod.** The DDL is idempotent and additive (no data migration). Add to the prod branch as well:

```bash
apply_sql "0013_user_task_progress.sql"
```

**Rationale**: build_hub_v2 precedent (2026-06-12) — per-tenant tables added to both dev and prod branches. Confirm with A0 HITL before prod apply; this brief targets dev only.

---

## 6. Apply command

```bash
FORCE_TARGET=1 ./scripts/apply-abc-os-migrations.sh dev
```

`FORCE_TARGET=1` is the A0-HITL-gated override (precedent 2026-06-12). The `ON CONFLICT (filename) DO NOTHING` + `CREATE TABLE IF NOT EXISTS` + `DROP POLICY IF EXISTS` patterns make re-applies safe.

**Precedent gotcha (2026-06-12)**: do NOT use `psql -v app.env=dev` (psql rejects embedded dots in var names). Use `PGOPTIONS='-c app.env=dev'` instead.

---

## 7. D1 Verify — 5 standard queries (run all, capture raw counts)

```sql
-- 1. Schema exists
SELECT count(*) AS schema_exists FROM information_schema.schemata
  WHERE schema_name = 'abc_os';
-- Expected: 1

-- 2. Table count (baseline 17 + 1 new = 18, then +1 organizations from prior batch = 19)
SELECT count(*) FROM information_schema.tables
  WHERE table_schema = 'abc_os' AND table_name != '_aspace_migrations';
-- Expected: 19

-- 3. RLS enabled (should equal table count)
SELECT count(*) FROM pg_tables
  WHERE schemaname = 'abc_os' AND rowsecurity = true;
-- Expected: 19

-- 4. Policy count (baseline 42 + 1 prior + 4 new = 47)
SELECT count(*) FROM pg_policies WHERE schemaname = 'abc_os';
-- Expected: 47

-- 5. Migrations logged (baseline 12 + 1 prior + 1 new = 14)
SELECT count(*) FROM abc_os._aspace_migrations;
-- Expected: 14
```

---

## 8. RLS effectiveness spot-checks (per-tenant correctness — D1 + D6)

These three spot-checks are the **load-bearing tests for per-tenant correctness**. A 47/19/19/14 count match is necessary but not sufficient — we must also prove the policies actually partition by `org_id`.

### 8a. anon role CANNOT SELECT
```sql
SET ROLE anon;
SET LOCAL app.org_id = 'co-op-alpha';
SELECT count(*) FROM abc_os.user_task_progress;
-- Expected: 0 rows visible (anon bypasses RLS, table is empty for anon) OR permission denied
-- (whichever the hardened role returns — both are GREEN if no leak)
RESET ROLE;
```

### 8b. authenticated role WITH current_org_id() match CAN SELECT
```sql
SET LOCAL ROLE authenticated;
SET LOCAL app.org_id = 'co-op-alpha';
-- Pre-condition: insert a row with org_id='co-op-alpha' in this org (use a seed test row or existing data)
SELECT count(*) AS visible_rows FROM abc_os.user_task_progress;
-- Expected: ≥ 1 (the matching row, when seeded)
RESET ROLE;
```

### 8c. authenticated role WITH current_org_id() MISMATCH CANNOT SELECT
```sql
SET LOCAL ROLE authenticated;
SET LOCAL app.org_id = 'co-op-bravo';  -- different org
SELECT count(*) AS visible_rows FROM abc_os.user_task_progress;
-- Expected: 0 rows (RLS blocks cross-org read)
RESET ROLE;
```

### 8d. (Bonus) UPDATE/DELETE role-gate check
```sql
SET LOCAL ROLE authenticated;
SET LOCAL app.org_id = 'co-op-alpha';
SET LOCAL app.role = 'member';   -- not owner/admin
-- Expect DELETE to affect 0 rows (RLS denies non-owner delete)
DELETE FROM abc_os.user_task_progress WHERE org_id = 'co-op-alpha';
RESET ROLE;
```

**If any spot-check fails, D6 says: the seed/apply is wrong, NOT the verify.** Re-read the .sql, mirror `action_items` exactly, amend, re-apply. Do not claim success on partial counts.

---

## 9. Expected vs actual counts (sub-agent fills these in)

| Metric | Expected | Actual | GREEN/red |
|---|---|---|---|
| Schema exists | 1 | __ | __ |
| Tables (excl. _aspace_migrations) | 19 | __ | __ |
| RLS enabled | 19 | __ | __ |
| Policies | 47 | __ | __ |
| Migrations logged | 14 | __ | __ |
| RLS spot-check 8a (anon SELECT) | 0 rows | __ | __ |
| RLS spot-check 8b (match SELECT) | ≥ 1 | __ | __ |
| RLS spot-check 8c (mismatch SELECT) | 0 rows | __ | __ |

---

## 10. Write-back contract — 3 files (never skip)

### 10a. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`
Append at top:
```markdown
## 2026-06-12 — eval-2 per-tenant `user_task_progress`

**A0 intent**: Add per-tenant `user_task_progress` table (idempotent, 4 RLS policies via `current_org_id()` + `current_role()`).

**Apply receipts** (D1 raw counts):
- tables: expected 19 / actual <fill>
- RLS enabled: expected 19 / actual <fill>
- policies: expected 47 / actual <fill>
- migrations logged: expected 14 / actual <fill>
- RLS spot-checks: 8a anon=0 rows (GREEN), 8b match≥1 (GREEN), 8c mismatch=0 rows (GREEN)

**Doctrine**: D1 ✓, D2 (mirrored action_items) ✓, D6 (FORCE_TARGET=1 override) ✓, D10 (per-tenant) ✓.

**Write-back**: README + handoff updated.
```

### 10b. `00_Amadeus/30_MEMORY_CORE/README.md`
Add a one-line bullet at the top:
```markdown
- 2026-06-12 — eval-2 per-tenant `user_task_progress` shipped (1 table, 4 RLS, +1 migration logged; tables=19, RLS=19, policies=47, migrations=14)
```

### 10c. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-12.md`
Add a "P_N Backend Status" section:
```markdown
### P_N Backend Status — 2026-06-12 (eval-2 per-tenant)

**Tables added** (1): `abc_os.user_task_progress` (id UUID PK, org_id FK, member_id FK, task_id FK, status CHECK, started_at/completed_at/created_at).

**Migrations added** (1): `0013_user_task_progress.sql` (idempotent, ON CONFLICT-safe).

**D1 verify receipts** (raw SQL output, not assertions):
```sql
-- 5 standard queries output here (paste actual psql output)
```
- tables=19 / RLS=19 / policies=47 / migrations=14 — all GREEN.

**RLS spot-checks** (D1 + D6):
- 8a anon SELECT: <paste result>
- 8b match SELECT: <paste result>
- 8c mismatch SELECT: <paste result>
- 8d member DELETE: <paste result>

**Mixed-tenancy summary** (D10): per-tenant (1 new) — org_id FK + 4 CRUD policies with `current_org_id()` and `current_role()`. Mirrors `action_items` from `0002_rls_policies.sql`.

**Prod-safety**: per-tenant schema/RLS, idempotent, additive. Prod apply gated on A0 HITL. ON CONFLICT safety net intact.

**Next safe action**: ready for prod apply (A0 HITL required) OR add `seed_user_task_progress.sql` if demo data is needed.
```

---

## 11. Drift detection protocol (D3)

If any spot-check fails OR the actual counts deviate from expected:
1. Re-read `0013_user_task_progress.sql` and `0002_rls_policies.sql` (the `action_items` reference).
2. The seed/apply is wrong, NOT the verify (D6).
3. Amend the .sql (mirror the canonical pattern exactly), re-run `FORCE_TARGET=1 ./scripts/apply-abc-os-migrations.sh dev`.
4. Flag the drift in the write-back handoff: "drift: yes — <what changed>".
5. Do NOT claim success until all 8 metrics (5 standard + 3 RLS) are GREEN.

---

## 12. Anti-patterns to avoid (2026-06-12 sub-agent failure modes)

- Writing the .sql but forgetting to update `apply-abc-os-migrations.sh` → migration never runs.
- Running the apply but skipping D1 verify → A0 can't trust the result.
- Reporting the success message without raw counts → violates D1.
- Writing back to `wiki/log.md` but not the handoff → next session loses context.
- Using `psql -v app.env=dev` (dots in var name) → psql errors. Use `PGOPTIONS='-c app.env=dev'`.
- Forgetting the `_aspace_migrations` tracker INSERT → next apply re-runs (safe but pollutes log).
- Inventing a new policy pattern instead of mirroring `action_items` → violates D2 + risks subtle RLS hole.
- Forgetting `pgcrypto` extension → `gen_random_uuid()` fails on first run.

---

## 13. Report back to A2 (final message format)

```
A0 intent: per-tenant `user_task_progress` table (eval-2)
5 verify counts (expected vs actual, all GREEN/red):
  - tables 19/<actual>  <status>
  - RLS    19/<actual>  <status>
  - policies 47/<actual> <status>
  - migrations 14/<actual> <status>
RLS spot-checks (8a/8b/8c/8d, all GREEN/red):
  - 8a anon: <status>
  - 8b match: <status>
  - 8c mismatch: <status>
  - 8d member DELETE: <status>
Drift (Y/N): <details if Y>
Write-back done: 3/3 (log.md, README.md, handoff_*.md)
Doctrine respect: D1, D2, D6, D10 — all observed.
Open follow-ups: <prod apply gate / seed request / etc.>
```

A2 will validate the receipts and report to A0. **A2 does not ask A0 what to do next.**
