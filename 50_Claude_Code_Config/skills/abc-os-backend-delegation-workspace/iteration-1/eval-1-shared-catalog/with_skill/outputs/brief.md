# A2 → A3 Sub-Agent Brief: `build_resources` shared-catalog table

**Eval**: eval-1-shared-catalog (iteration-1)
**Migration filename**: `0013_build_resources.sql`
**Date issued**: 2026-06-12
**Issued by**: A2 (Claude Code orchestrator)
**Executor**: A3 sub-agent (spawned via `Agent` tool, `subagent_type: general-purpose`, `run_in_background: true`)

---

## 0. A0's Intent (verbatim)

> "Add a new `build_resources` table to the abc_os schema on the VPS Supabase. Columns: id (TEXT PK), project_id (FK to build_projects ON DELETE CASCADE), title TEXT, kind TEXT (values: tool / material / technique), url TEXT (nullable), sort_order INT default 0, created_at TIMESTAMPTZ default now(). Shared catalog (no org_id), RLS = select-authenticated. Apply to dev with FORCE_TARGET=1. After applying, run D1 verify queries and write back to the 3 memory files (wiki/log.md, MEMORY_CORE/README.md, handoff_abc_os_community_dev_2026-06-10.md)."

---

## 1. Doctrine Anchors (cite in every report back)

- **D1 Verify-Before-Assert** (ADR-META-001): prove with observed `count(*)` output, not assertions. Always include the raw integer count, not "success" messages.
- **D2 Research-first**: model `build_resources` on the existing `build_projects` shared-catalog pattern in `apps/abc-os-community/supabase/migrations/abc_os/`. Use `_doctrine/Doctrine.md` patterns.
- **D3 Nuance over Literal**: doc/seed drift is real — adapt the schema/seed to the source-of-truth, do NOT refuse the apply. Flag drift in the write-back.
- **D4 No self-contradiction**: do NOT claim success if any verify count is off.
- **D5 Cost of escalation to A0**: do not ping A0 for a fixable verify miss; fix it yourself, report the fix in the write-back.
- **D6 Persistent symptom → root cause**: if `app.env` blocks the apply, root cause = Supabase hardened role; fix with `FORCE_TARGET=1` + `ON CONFLICT` safety net.
- **D7**: log everything; no silent state changes.
- **D8**: write-back is non-optional.
- **D10 Mixed-tenancy** (ADR-ABCOS-001): `build_resources` is **shared catalog** (no `org_id`, same data for every co-op). RLS = `select-authenticated` only. Per-tenant policies with `current_org_id()`/`current_role()` MUST NOT be applied to this table.

**Doctrinal references**: ADR-META-001, ADR-SUPABASE-001 (D3+D4), ADR-ABCOS-001 (D10 mixed-tenancy).

---

## 2. Tenancy classification (D10)

| Table | Tenancy | RLS shape | Why |
|-------|---------|-----------|-----|
| `build_resources` | **shared catalog** | `select-authenticated` only | Same resources apply to every co-op; no tenant isolation needed. No `org_id` column. |

Precedent for shared-catalog shape: `build_categories`, `build_projects`, `learn_courses` (all in `abc_os` baseline).

---

## 3. Pre-flight (sub-agent verifies BEFORE applying)

1. Confirm local migration file exists (sub-agent writes it from §4 below):
   `apps/abc-os-community/supabase/migrations/abc_os/0013_build_resources.sql`
2. Confirm apply script exists:
   `apps/abc-os-community/supabase/scripts/apply-abc-os-migrations.sh`
3. Verify SSH alias `aspace-vps` reachable: `ssh aspace-vps "echo ok"`
4. Verify `app.env` on VPS: `ssh aspace-vps "cat \$HOME/.aspace/app.env"` (capture actual value; expected to be `prod` per 2026-06-11 state; this is why we need `FORCE_TARGET=1`).
5. Baseline counts (run BEFORE apply, save raw output for the write-back):
   ```sql
   SELECT count(*) FROM information_schema.tables
     WHERE table_schema='abc_os' AND table_name <> '_aspace_migrations';
   -- baseline: 17
   SELECT count(*) FROM pg_tables WHERE schemaname='abc_os' AND rowsecurity = true;
   -- baseline: 17
   SELECT count(*) FROM pg_policies WHERE schemaname='abc_os';
   -- baseline: 42
   SELECT count(*) FROM abc_os._aspace_migrations;
   -- baseline: 12 (dev)
   ```

---

## 4. Full .sql DDL — write to `0013_build_resources.sql`

Use exactly this content. Idempotent. Drop-and-recreate policies. Migration tracker at the end.

```sql
-- 0013_build_resources.sql
-- Shared-catalog table (D10): tools / materials / techniques attached to a build_projects row.
-- Tenancy: shared catalog (no org_id). RLS = select-authenticated.
-- Doctrine: ADR-META-001 (D1 verify), ADR-ABCOS-001 (D10 mixed-tenancy).
-- Idempotent: safe to re-apply.

BEGIN;

-- 1. Table
CREATE TABLE IF NOT EXISTS abc_os.build_resources (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES abc_os.build_projects(id) ON DELETE CASCADE,
  title       TEXT NOT NULL,
  kind        TEXT NOT NULL CHECK (kind IN ('tool','material','technique')),
  url         TEXT,
  sort_order  INTEGER NOT NULL DEFAULT 0,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 2. Indexes (for project_id lookups; sort order within a project)
CREATE INDEX IF NOT EXISTS idx_build_resources_project_id
  ON abc_os.build_resources(project_id);
CREATE INDEX IF NOT EXISTS idx_build_resources_project_sort
  ON abc_os.build_resources(project_id, sort_order);

-- 3. RLS enable (idempotent: catch duplicate_object error)
DO $$
BEGIN
  ALTER TABLE abc_os.build_resources ENABLE ROW LEVEL SECURITY;
EXCEPTION WHEN duplicate_object THEN
  -- already enabled; safe to ignore
  NULL;
END$$;

-- 4. RLS policy — drop-and-recreate to allow amendments
DROP POLICY IF EXISTS build_resources_select_authenticated ON abc_os.build_resources;
CREATE POLICY build_resources_select_authenticated
  ON abc_os.build_resources
  FOR SELECT
  TO authenticated
  USING (true);

-- 5. Migration tracker (idempotent on filename PK)
INSERT INTO abc_os._aspace_migrations (filename)
  VALUES ('0013_build_resources.sql')
  ON CONFLICT (filename) DO NOTHING;

COMMIT;
```

---

## 5. Apply script update — `apply-abc-os-migrations.sh`

Edit in **TWO places** (pre-flight list AND apply_sql block, for BOTH `dev` and `prod` branches — shared-catalog schema/RLS goes everywhere):

### 5a. Pre-flight file list (around line 53)

In the `for f in ...` list that enumerates the migration files, add:

```bash
"0013_build_resources.sql"
```

inside the same array that already includes `0012_*.sql`.

### 5b. `apply_sql` block — DEV branch (around line 127)

Inside `if [[ "$TARGET" == "dev" ]]`, add a new `apply_sql` invocation:

```bash
apply_sql "0013_build_resources.sql"
```

### 5c. `apply_sql` block — PROD branch (around line 141)

Inside `if [[ "$TARGET" == "prod" ]]`, add the SAME line:

```bash
apply_sql "0013_build_resources.sql"
```

Shared-catalog DDL goes to both branches (schema + RLS, no seed). If A0 later approves a dev-only seed, add the apply line to dev only.

---

## 6. Apply command (FORCE_TARGET=1, ON CONFLICT safety net)

```bash
FORCE_TARGET=1 ./scripts/apply-abc-os-migrations.sh dev
```

- `FORCE_TARGET=1` overrides the `prod` `app.env` mismatch (precedent 2026-06-12).
- Every DDL uses `IF NOT EXISTS` / drop-and-recreate / `ON CONFLICT` → re-applying is safe.

---

## 7. D1 verify — 5 standard + 3 table-specific spot-checks

Run these AFTER the apply completes. Capture raw `count(*)` integers (D1). If any expected vs actual is off, do NOT mark success.

### 7a. The 5 standard D1 verify queries (post-apply)

```sql
-- 1. Schema exists
SELECT count(*) AS schema_exists
  FROM information_schema.schemata
 WHERE schema_name = 'abc_os';
-- expected: 1

-- 2. Table count (excluding migration tracker)
SELECT count(*)
  FROM information_schema.tables
 WHERE table_schema = 'abc_os'
   AND table_name <> '_aspace_migrations';
-- expected: 18  (17 baseline + 1 new build_resources)

-- 3. RLS enabled (should equal table count)
SELECT count(*)
  FROM pg_tables
 WHERE schemaname = 'abc_os'
   AND rowsecurity = true;
-- expected: 18

-- 4. Policy count
SELECT count(*)
  FROM pg_policies
 WHERE schemaname = 'abc_os';
-- expected: 43  (42 baseline + 1 new build_resources_select_authenticated)

-- 5. Migrations logged
SELECT count(*) FROM abc_os._aspace_migrations;
-- expected: 13  (12 baseline + 1 new 0013)
```

### 7b. `build_resources`-specific spot-checks (3)

```sql
-- Spot 1. New table exists in abc_os schema
SELECT count(*)
  FROM information_schema.tables
 WHERE table_schema = 'abc_os'
   AND table_name = 'build_resources';
-- expected: 1

-- Spot 2. RLS enabled on new table + exactly 1 policy named build_resources_*
SELECT count(*) AS rls_policies
  FROM pg_policies
 WHERE schemaname = 'abc_os'
   AND tablename  = 'build_resources';
-- expected: 1  (build_resources_select_authenticated)

-- Spot 3. FK constraint to build_projects exists
SELECT count(*)
  FROM information_schema.table_constraints
 WHERE table_schema   = 'abc_os'
   AND table_name     = 'build_resources'
   AND constraint_type = 'FOREIGN KEY'
   AND constraint_name LIKE '%build_projects%';
-- expected: 1
```

### 7c. Expected vs Actual — sub-agent fills actual values

| Check | Expected | Actual (sub-agent fills) | Status |
|-------|----------|--------------------------|--------|
| 1. schema_exists | 1 | __ | GREEN/red |
| 2. table_count | 18 | __ | GREEN/red |
| 3. rls_enabled_count | 18 | __ | GREEN/red |
| 4. policy_count | 43 | __ | GREEN/red |
| 5. migrations_logged | 13 | __ | GREEN/red |
| Spot 1. table exists | 1 | __ | GREEN/red |
| Spot 2. rls_policies on new | 1 | __ | GREEN/red |
| Spot 3. FK to build_projects | 1 | __ | GREEN/red |

If any row is red, the apply is NOT done. Diagnose: re-read the .sql + apply script update, amend, re-apply (D3 + D6).

---

## 8. Write-back contract — 3 files, mandatory, in this order

### 8a. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`

Prepend a `## 2026-06-12` block at the top (most recent at top). Use this skeleton:

```markdown
## 2026-06-12 — build_resources table added (eval-1-shared-catalog)

**A0 intent**: Add shared-catalog `build_resources` table to abc_os (D10). Tenancy = shared (no org_id), RLS = select-authenticated.
**Migration**: `0013_build_resources.sql` (applied to dev, FORCE_TARGET=1).
**Doctrine**: ADR-META-001 (D1, D3, D6, D8), ADR-ABCOS-001 (D10 mixed-tenancy).
**Tenancy**: shared catalog.

**Apply receipts (D1 verify, raw counts)**:
- schema_exists: 1 (expected 1) — GREEN
- table_count: <actual> (expected 18) — <status>
- rls_enabled_count: <actual> (expected 18) — <status>
- policy_count: <actual> (expected 43) — <status>
- migrations_logged: <actual> (expected 13) — <status>
- spot table exists: 1 (expected 1) — GREEN
- spot rls_policies on build_resources: 1 (expected 1) — GREEN
- spot FK to build_projects: 1 (expected 1) — GREEN

**Drift**: <Y/N> — <if Y, what changed and how the schema/seed was adapted>
**Write-back links**: README.md, handoff_abc_os_community_dev_2026-06-10.md
```

### 8b. `00_Amadeus/30_MEMORY_CORE/README.md`

Add a one-line bullet at the top of the most recent section:

```markdown
- 2026-06-12: `build_resources` shared-catalog table added to abc_os (D10), 1 table + 1 RLS policy, 0013 migration applied to dev.
```

### 8c. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md`

Append a new section near the top (do NOT rewrite existing sections). Title: `## P_N Backend Status — 2026-06-12 build_resources`. Include:

```markdown
## P_N Backend Status — 2026-06-12 build_resources

**Tables added**: 1 (`abc_os.build_resources`)
**Migrations added**: 1 (`0013_build_resources.sql`, applied to dev with FORCE_TARGET=1)
**D1 verify receipts** (raw SQL + count, post-apply):
- schema_exists = 1 (expected 1) — GREEN
- table_count = <actual> (expected 18) — <status>
- rls_enabled = <actual> (expected 18) — <status>
- policy_count = <actual> (expected 43) — <status>
- migrations_logged = <actual> (expected 13) — <status>
- spot build_resources exists = 1 — GREEN
- spot rls policies on build_resources = 1 — GREEN
- spot FK to build_projects = 1 — GREEN

**Mixed-tenancy summary**: `build_resources` = shared catalog (D10). No org_id. RLS = `build_resources_select_authenticated` (select-authenticated only).
**Prod-safety**: Schema/RLS is safe to promote to prod (no seed, no user data). To promote: same `0013` line, prod branch of apply-abc-os-migrations.sh, prod apply without FORCE_TARGET.
**Next safe action**: A0 may now seed a few reference rows in dev (e.g. `INSERT INTO abc_os.build_resources ... ON CONFLICT (id) DO NOTHING`) — needs a new migration `0014_build_resources_seed.sql` added to dev branch only.
```

---

## 9. Drift detection protocol (D3, D6)

If any spot-check fails, the seed/schema/apply is wrong, NOT the verify. Steps:

1. Re-read `0013_build_resources.sql` and confirm §4 was applied verbatim.
2. Re-read the apply script update (§5a/5b/5c) and confirm both branches include the new apply_sql line.
3. Compare column names in the .sql against the A0 intent (verbatim in §0) and against any TypeScript source-of-truth in `apps/abc-os-community/`.
4. If column name or FK target drifted: amend the .sql with drop-and-recreate, re-apply, re-verify.
5. Log the drift + fix in `wiki/log.md` (D3 nuance) and in the handoff file. Do not silently swallow it.
6. Do NOT escalate to A0 unless the drift is a policy/architecture question (e.g. tenancy mis-classification). D5 — fix it yourself first.

---

## 10. Anti-patterns to avoid (sub-agent failure modes)

- Forgetting the migration tracker `INSERT` at the end of the .sql → next apply re-runs the migration (idempotent so safe, but pollutes the log).
- Updating only the pre-flight list in `apply-abc-os-migrations.sh` but not the `apply_sql` block → migration never runs.
- Updating only the `dev` branch of the `apply_sql` block but not the `prod` branch (or vice versa) → silent drift between environments.
- Reporting "apply succeeded" without raw `count(*)` integers → violates D1.
- Writing to `wiki/log.md` but skipping the handoff → next session loses context.
- Using `psql -v app.env=dev` with dots in the var name → psql errors. Use `PGOPTIONS='-c app.env=dev'` (precedent 2026-06-12) — but for this apply we use `FORCE_TARGET=1`, so no psql var needed.
- Using `RAISE NOTICE` / DO blocks that swallow real errors (e.g. catching all exceptions in the RLS enable block) → silent partial applies. The exception handler in §4 is scoped to `duplicate_object` only.
- Adding per-tenant `current_org_id()` policies to a shared-catalog table → D10 violation, over-isolates data that should be shared.

---

## 11. Report-back contract (sub-agent → A2)

Reply to A2 in under 200 words with:

```
APPLY: 0013_build_resources.sql applied to dev (FORCE_TARGET=1) — exit 0 / exit !=0
D1 VERIFY (5 standard + 3 spot):
  1. schema_exists        expected 1   actual <n>  <GREEN/red>
  2. table_count          expected 18  actual <n>  <GREEN/red>
  3. rls_enabled_count    expected 18  actual <n>  <GREEN/red>
  4. policy_count         expected 43  actual <n>  <GREEN/red>
  5. migrations_logged    expected 13  actual <n>  <GREEN/red>
  spot1 table exists      expected 1   actual <n>  <GREEN/red>
  spot2 rls policies      expected 1   actual <n>  <GREEN/red>
  spot3 FK build_projects expected 1   actual <n>  <GREEN/red>
DRIFT: <Y/N — if Y, one-line summary of what changed and how>
WRITE-BACK: 3/3 done (wiki/log.md, MEMORY_CORE/README.md, handoff_2026-06-10.md)
DOCTRINE RESPECT: D1 D3 D6 D8 D10 confirmed
OPEN FOLLOW-UPS: <none | list>
```

A2 then summarizes to A0: A0 intent → 5+3 counts (GREEN/red) → write-back done → doctrine respect → open follow-ups. A2 does NOT ask A0 what's next.

---

## 12. Expected post-apply counts (sub-agent reference card)

| Metric | Baseline (2026-06-12) | +1 migration | Expected actual |
|--------|------------------------|--------------|-----------------|
| `abc_os` tables (excl. `_aspace_migrations`) | 17 | +1 | **18** |
| Tables with RLS enabled | 17 | +1 | **18** |
| RLS policies on `abc_os` | 42 | +1 | **43** |
| Rows in `abc_os._aspace_migrations` (dev) | 12 | +1 | **13** |
| `build_resources` table exists | 0 | +1 | **1** |
| Policies on `build_resources` | 0 | +1 | **1** |
| FKs from `build_resources` to `build_projects` | 0 | +1 | **1** |

If any "actual" diverges, the apply is incomplete. Diagnose per §9.

---

## 13. Out of scope (do NOT do)

- Do NOT seed any reference rows. Seed is a follow-up migration `0014_build_resources_seed.sql`, added to dev branch only, requires A0 HITL on row content.
- Do NOT promote to prod. Prod promotion is a separate apply run.
- Do NOT modify the apply script's pre-flight enforcement (e.g. the env-var guard) — that is infra, not schema.
- Do NOT change `current_org_id()` / `current_role()` helpers — D10 says shared-catalog tables don't use them.
- Do NOT touch unrelated tables, policies, or migrations.

---

**End of brief. Sub-agent: execute §3 → §6 → §7 → §8 → §11, in that order. Do not skip steps. Do not paraphrase this brief to A2 — report back via the §11 contract.**
