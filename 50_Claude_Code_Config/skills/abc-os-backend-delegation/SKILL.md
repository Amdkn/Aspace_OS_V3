---
name: abc-os-backend-delegation
description: Delegate abc_os Supabase schema/migration/RLS work to a sub-agent with full doctrine respect, D1 Verify-Before-Assert receipts, and a 3-file write-back contract. Use this skill whenever the user asks to add a new table to the abc_os schema on the self-hosted VPS Supabase (aspace-vps), write an idempotent migration file, set up RLS policies for a new table (per-tenant OR shared-catalog tenancy), seed reference data from a TypeScript source-of-truth, or reconcile a doc/seed drift after an apply. Triggers include phrases like "add X table to abc_os", "new migration for Y", "seed the Z catalog", "RLS for the new table", "apply migrations to aspace-vps", or "run this migration". DO NOT use for: app-level data fetching code (that's a Next.js task), schema-less changes, or any operation that doesn't touch the abc_os Postgres schema on the VPS.
metadata:
  type: skill
  domain: backend-delegation
  layer: L2 (Business OS)
  anchors:
    - ADR-META-001 (D1-D8 doctrine, esp. D1 Verify-Before-Assert)
    - ADR-SUPABASE-001 (self-hosted multi-tenancy schemas, D3+D4)
    - ADR-ABCOS-001 (multitenant Supabase strategy, D10 mixed-tenancy)
  precedent: 2026-06-12 build_hub_v2 apply (12 migrations, 17 tables, 42 RLS, FORCE_TARGET=1)
---

# abc-os-backend-delegation

Doctrine-aware backend delegation to VPS Supabase. Encapsulates the 6-step workflow used to ship the build_hub_v2 migration on 2026-06-12: write the .sql locally → update the apply script → spawn a sub-agent that applies with FORCE_TARGET=1 → runs D1 verify queries → spot-checks data → writes back to 3 memory files. The sub-agent gets the full doctrine + D1 verify receipts + write-back contract in the brief; the orchestrator (A2) only validates the receipts and reports to A0.

**Why this exists as a skill**: every backend change to abc_os repeats the same pattern (idempotent SQL + apply script update + D1 verify + write-back). Baked into a skill, each invocation is ~5-8 min faster than re-deriving the workflow, the doctrine anchors, and the verify-query set from scratch. The skill also forces the orchestrator to delegate — A2 never touches SQL or psql directly.

## 6 Hardened Iter-2 Assertions (mandatory brief structure)

A2 MUST include the following 6 doctrinal checkpoints in EVERY sub-agent brief. These were added in iter-2 (2026-06-13) to catch 3 doctrinal errors that slipped through iter-1's presence-based assertions:

1. **A1 — Tracker table literal match** : brief MUST reference the exact literal `abc_os._aspace_migrations` (canonical tracker from 0000_init precedent). MUST NOT reference fictional variants like `abc_os.migrations` (without underscore) or `abc_os.schema_migrations`. All `INSERT INTO abc_os._aspace_migrations ...` statements MUST use `ON CONFLICT (filename) DO NOTHING` (idempotency on the `filename` PK column).

2. **A2 — RLS `current_role()` scope** : any `current_role()` use in a USING or WITH CHECK clause MUST be one of:
   - `TO authenticated USING (true)` — shared-catalog (no `current_role()` at all, role scoped via TO clause)
   - `USING (org_id = current_org_id())` — per-tenant SELECT (canonical action_items pattern)
   - `current_role() IN ('owner', 'admin', 'member')` — per-tenant INSERT/UPDATE/DELETE app-role check (NOT Postgres roles)
   
   The anti-pattern `current_role() IN ('anon', 'authenticated', 'service_role')` is FORBIDDEN — service_role bypasses RLS by design, so including it in the predicate is meaningless; the canonical pattern uses the `TO` clause to restrict the role and the `USING` clause to scope the row.

3. **A3 — Old/New diff structure** : any migration brief MUST include either:
   - An "## Old" / "## New" markdown header pair showing the schema diff for A0 review, OR
   - An explicit "DRY-RUN MODE" line (when the apply will only run after A0 HITL approval).
   
   This forces the brief to be reviewable without the sub-agent actually running the apply.

4. **A4 — FORCE_TARGET=1 with idempotency safety net** : brief MUST mention `FORCE_TARGET=1` AND every CREATE TABLE / CREATE INDEX / CREATE POLICY statement MUST use `IF NOT EXISTS` or `DROP IF EXISTS` (idempotency). The migration tracker INSERT MUST use `ON CONFLICT (filename) DO NOTHING`. This guarantees the apply is safe to re-run.

5. **A5 — Mixed-tenancy decision tree cited** : brief MUST cite either "D10" or the decision tree itself (shared-catalog = TEXT PK no org_id, per-tenant = has org_id). This forces the sub-agent to classify the new table BEFORE writing DDL, preventing the most common error (wrong tenancy classification).

6. **A6 — Write-back contract complete** : brief MUST mention all 3 write-back targets with the canonical paths:
   - `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` (prepend `## YYYY-MM-DD` block)
   - `00_Amadeus/30_MEMORY_CORE/README.md` (one-line bullet at top)
   - `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_<DATE>.md` (P_N Backend Status section)
   
   Each file must be cited with its full path; the handoff file MUST use the `handoff_abc_os_community_dev_<DATE>.md` naming convention.

## When to use

- Adding a new table (or set of tables) to the `abc_os` schema
- Adding a new index, constraint, or column to an existing `abc_os` table
- Writing or amending RLS policies (per-tenant with `current_org_id()` OR shared-catalog with `select-authenticated`)
- Seeding reference data from a TS/JSON source-of-truth (catalog data, not user data)
- Reconciling a doc/seed drift after an apply (column-name mismatch, FK id mismatch, etc.)

**Do NOT use for**: app-level Next.js data fetching, schema-less file changes, or anything that doesn't touch Postgres.

## Mixed-tenancy decision tree (D10)

Before writing any migration, classify each new table as either **shared catalog** (no `org_id`, readable by all authenticated users) or **per-tenant** (has `org_id` FK, RLS via `current_org_id()` and `current_role()`):

```
Is the data the same for every co-op?
├── YES → shared catalog (TEXT PK, no org_id, RLS = select-authenticated)
│         e.g. build_categories, build_projects, learn_courses
└── NO  → per-tenant (TEXT or UUID PK, has org_id FK to organizations,
                       RLS = per-org policies with current_org_id() and current_role())
         e.g. build_milestones, members, action_items
```

When in doubt, default to **per-tenant** — a shared catalog leaks data across orgs by design, per-tenant is reversible but the opposite is not. Mixed models can coexist (see D10 precedent: 4 shared-catalog tables + 2 per-tenant tables in abc_os).

## Inputs to collect before delegating

| Input | Required? | Where to get it |
|-------|-----------|-----------------|
| Table/column definitions (DDL) | YES | A0's intent + reference to TS source if exists |
| Tenancy classification per table | YES | Mixed-tenancy decision tree above |
| Migration filename (next number) | YES | `ls apps/abc-os-community/supabase/migrations/abc_os/` |
| Apply target (dev/prod) | YES | A0 HITL gate; default dev |
| FORCE_TARGET=1? | YES | Default 1 (A0 HITL precedent 2026-06-11) |
| Whether to update apply-abc-os-migrations.sh | YES | Always YES for new schema/RLS; YES for seed only if dev |
| D1 verify queries (post-conditions) | YES | Use the standard 5-query set + add table-specific spot checks |
| Write-back files | YES | Always 3: `wiki/log.md`, `MEMORY_CORE/README.md`, `handoff_abc_os_community_dev_*.md` |

## Standard D1 verify query set (5 queries)

Run these after every apply to prove the migration landed. Output is the proof; if any count is off, the migration is NOT done.

```sql
-- 1. Schema exists
SELECT count(*) AS schema_exists FROM information_schema.schemata WHERE schema_name = 'abc_os';
-- Expected: 1

-- 2. Table count (expected = N core + N learn + N build_brand + N new)
SELECT count(*) FROM information_schema.tables
WHERE table_schema = 'abc_os' AND table_name != '_aspace_migrations';
-- Expected (2026-06-12 baseline): 17

-- 3. RLS enabled (should equal table count)
SELECT count(*) FROM pg_tables WHERE schemaname = 'abc_os' AND rowsecurity = true;
-- Expected (2026-06-12 baseline): 17

-- 4. Policy count (expected = 38 baseline + N for new shared-catalog tables)
SELECT count(*) FROM pg_policies WHERE schemaname = 'abc_os';
-- Expected (2026-06-12 baseline): 42

-- 5. Migrations logged (in abc_os._aspace_migrations)
SELECT count(*) FROM abc_os._aspace_migrations;
-- Expected (2026-06-12 baseline): 12 (dev) or 7 (prod: 0000-0002 + 0004-0005 + 0008 + 0010 + 0012)
```

## The 6-step delegation workflow

When A0 says "add X" or "ship Y migration", the orchestrator (A2) follows these 6 steps. **A2 never writes SQL or runs psql — all technical work goes to a sub-agent.**

### Step 1: Pre-flight brief
Write a self-contained brief for the sub-agent. Include:
- A0's exact intent (verbatim quote)
- The .sql files to write (full DDL, idempotent, with comments)
- The apply script update (which `apply_sql` lines to add, in which TARGET branch)
- The 5 standard D1 verify queries + 3-5 table-specific spot-checks
- The 3-file write-back contract (what to add, where, format)
- Doctrine anchors: D1-D8 + D10 mixed-tenancy
- FORCE_TARGET=1 with ON CONFLICT safety net
- Expected counts (table/RLS/policy/migration) so the sub-agent can compare to actual

### Step 2: Spawn sub-agent in background
Use `Agent` tool with `subagent_type: general-purpose` and `run_in_background: true`. Pass the brief verbatim — don't summarize, don't paraphrase. The sub-agent is the executor; A2 is the orchestrator.

### Step 3: Sub-agent applies with FORCE_TARGET=1
Precedent: when `app.env` on the VPS is `prod` but the seed/apply is dev-only, the sub-agent must set `FORCE_TARGET=1` to override. This is HITL-gated by A0's "GO" on the apply itself. The safety net is `ON CONFLICT (id/filename) DO NOTHING` in every migration — even if the apply runs twice, the DB state is idempotent.

```bash
FORCE_TARGET=1 ./scripts/apply-abc-os-migrations.sh dev
```

### Step 4: Sub-agent runs D1 verify queries
The 5 standard queries + 3-5 spot-checks. Output must include the raw `count` values, not just assertions. If a count is off, the sub-agent rolls back via Drop-and-Recreate or amendments to the .sql files (and re-applies).

### Step 5: Sub-agent writes back to 3 files
The write-back contract — never skip, this is how the next session picks up context:

1. **`00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`** — append a `## YYYY-MM-DD` block at the top with: A0's intent, the apply receipts (counts), the write-back links.
2. **`00_Amadeus/30_MEMORY_CORE/README.md`** — add a one-line bullet at the top (date + summary).
3. **`00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_<DATE>.md`** — add a "P_N Backend Status" section with: tables added, migrations added, D1 verify receipts (raw SQL + count), spot-checks, mixed-tenancy summary, prod-safety, next safe action.

### Step 6: A2 reports to A0
Summarize: A0's intent → 5 verify counts (GREEN/red) → write-back done → doctrine respect → open follow-ups. Do NOT ask A0 what to do next — A0 will issue a new intention or redirect.

## Doctrine anchors (cite in every sub-agent brief)

- **D1 Verify-Before-Assert** (ADR-META-001): prove with observed output, not assertions. Always include the raw count.
- **D2 Research-first**: if a similar table already exists, follow its pattern. Use `_doctrine/Doctrine.md` patterns as the source of truth.
- **D3 Nuance over Literal**: doc/seed drift is real — adapt the seed to the schema, flag the drift in the write-back, fix the docs in a follow-up. Don't refuse the apply.
- **D4 No self-contradiction**: don't claim success if any verify count is off.
- **D6 Persistent symptom → root cause**: if `app.env` blocks the apply, the root cause is the Supabase hardened role, not the preflight. Fix with FORCE_TARGET=1 + ON CONFLICT safety net.
- **D10 Mixed-tenancy** (ADR-ABCOS-001): per-tenant and shared-catalog can coexist. RLS for shared catalog = `select-authenticated` only; RLS for per-tenant = `current_org_id()` and `current_role()` policies.

## Idempotent SQL patterns (template)

Every migration MUST use these patterns so re-applying is safe:

```sql
-- Table creation
CREATE TABLE IF NOT EXISTS abc_os.<table_name> (
  id    TEXT PRIMARY KEY,
  ...
);

-- Index
CREATE INDEX IF NOT EXISTS idx_<table>_<col> ON abc_os.<table>(col);

-- RLS enable (idempotent: error if already enabled, catch and ignore)
ALTER TABLE abc_os.<table> ENABLE ROW LEVEL SECURITY;

-- RLS policy (drop-and-recreate to allow amendments)
DROP POLICY IF EXISTS <policy_name> ON abc_os.<table>;
CREATE POLICY <policy_name> ON abc_os.<table>
  FOR SELECT TO authenticated
  USING (true);

-- Seed (idempotent on PK)
INSERT INTO abc_os.<table> (id, ...) VALUES ('id-1', ...)
  ON CONFLICT (id) DO NOTHING;

-- Migration tracker
INSERT INTO abc_os._aspace_migrations (filename) VALUES ('0013_xxx.sql')
  ON CONFLICT (filename) DO NOTHING;
```

## Apply script update pattern

When adding a new migration, edit `apps/abc-os-community/supabase/scripts/apply-abc-os-migrations.sh` in TWO places:

1. The `for f in ...` pre-flight file list (line ~53)
2. The `apply_sql` block in the relevant `if [[ "$TARGET" == "dev" ]]` (line ~127) or `if [[ "$TARGET" == "prod" ]]` (line ~141) branch

For shared-catalog (schema/RLS only, no seed), add to BOTH dev and prod branches. For dev-only seed, add to dev branch only.

## Sub-agent brief template

```text
TASK: <one-line summary>
DOCTRINE ANCHORS: ADR-META-001 (D1-D8), ADR-ABCOS-001 (D10 mixed-tenancy)
TENANCY: shared-catalog | per-tenant | mixed (cite D10 decision tree — A5)
TARGET: dev | prod
FORCE_TARGET: 1 | 0 (default 1, ON CONFLICT safety net intact — A4)

PRE-FLIGHT:
- Verify local files: <list of .sql files with absolute paths>
- Verify SSH alias `aspace-vps` reachable
- Verify `app.env` on VPS (output: actual vs TARGET)

APPLY:
```bash
FORCE_TARGET=1 ./scripts/apply-abc-os-migrations.sh dev
```

A3 — OLD/NEW DIFF (for A0 review):
## Old
<previous schema/RLS state, with line refs to current migration files>

## New
<proposed DDL summary, with line refs to the new migration file>

D1 VERIFY (5 standard + 3 spot):
<the 5 standard queries — must use abc_os._aspace_migrations for the 5th (A1)>
<3 table-specific spot-checks: e.g. SELECT count(*) FROM abc_os.build_projects WHERE category_id='homesteading'>

A2 — RLS SCOPE CHECK:
- shared-catalog: FOR SELECT TO authenticated USING (true) — no current_role() in USING
- per-tenant: FOR SELECT TO authenticated USING (org_id = current_org_id()) — no service_role in USING

EXPECTED COUNTS (vs actual):
- table count: expected 17+1=18 / actual <sub-agent fills>
- RLS enabled: expected 17+1=18 / actual <sub-agent fills>
- policy count: expected 42+1=43 / actual <sub-agent fills>
- migrations logged: expected 12+1=13 / actual <sub-agent fills>

WRITE-BACK (3 files, full canonical paths — A6):
1. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` — prepend `## YYYY-MM-DD` block at top
2. `00_Amadeus/30_MEMORY_CORE/README.md` — add bullet at top
3. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_<DATE>.md` — add "P_N Backend Status" section

DRIFT DETECTION:
- If spot-check fails, the seed/apply is wrong, NOT the verify. Re-read the .sql and the source-of-truth TS file, adapt, re-apply. Flag the drift in the write-back.

REPORT BACK: A0's intent → 4 counts (expected vs actual GREEN/red) → drift (Y/N) → write-back done (3/3).
```

## ROI & reusability

- First apply (build_hub_v2) took ~25 min from intent to D1 verified. With this skill: ~5-8 min.
- Every new shared-catalog table, per-tenant table, RLS policy set, or seed file reuses this same pattern.
- The doctrine anchors (D1-D8, D10) and the 5 standard verify queries are the load-bearing pieces. Sub-agents that don't have them in their brief skip steps or invent wrong verify queries.

## Anti-patterns to flag (sub-agent failure modes)

- Sub-agent writes the .sql but doesn't update the apply script → migration exists locally but never runs
- Sub-agent runs the apply but doesn't run D1 verify → A0 can't trust the result
- Sub-agent runs D1 verify but only reports the success message, not the raw counts → violates D1
- Sub-agent writes back to wiki/log.md but not to the handoff → next session loses context
- Sub-agent uses `psql -c "..."` with embedded dots in the var name (e.g. `-v app.env=dev`) → psql errors. Use `PGOPTIONS='-c app.env=dev'` instead (precedent 2026-06-12).
- Sub-agent forgets the migration tracker INSERT → next apply will re-run the migration (idempotent so safe, but pollutes the log)
