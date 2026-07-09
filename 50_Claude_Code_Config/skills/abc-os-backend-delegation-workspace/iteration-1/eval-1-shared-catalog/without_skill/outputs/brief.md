# A2 → A3 Brief: Add `abc_os.build_resources` (Shared Catalog)

> **Eval ID**: `eval-1-shared-catalog` · `add-shared-catalog-table`
> **Date**: 2026-06-12
> **Issuer (A2)**: Claude Code Orchestrator
> **Executor (A3)**: Backend sub-agent (Postgres / Supabase)
> **Doctrine anchors**: ADR-META-001 (D1–D8, Verify-Before-Assert / Nuance / No Self-Contradiction / Cross-agent portée) · ADR-ABCOS-001 (D10 Mixed-Tenancy)

---

## 1. Intention (A0 verbatim, restated)

> Add a new `build_resources` table to the `abc_os` schema on the VPS Supabase.
> Columns: `id` (TEXT PK), `project_id` (FK to `build_projects` ON DELETE CASCADE), `title` TEXT, `kind` TEXT (values: `tool` / `material` / `technique`), `url` TEXT (nullable), `sort_order` INT default 0, `created_at` TIMESTAMPTZ default `now()`.
> **Shared catalog** (no `org_id`), RLS = `select-authenticated`.
> Apply to **dev** with `FORCE_TARGET=1`.
> After applying, run **D1 verify queries** and write back to the **3 memory files**.

This is a **D10 mixed-tenancy catalog table**: the parent `build_projects` is *tenant-scoped* (org_id), but `build_resources` is intentionally *shared* across the community. Do NOT add `org_id` to this table — that would violate D10.

---

## 2. Doctrine Anchors (binding)

| Anchor | Source | Application here |
|---|---|---|
| **D1** Verify-Before-Assert | ADR-META-001 | All counts (`tables`, `policies`, `migrations_logged`) MUST be re-queried before being written to the wiki. Never carry an expected number in your final report. |
| **D2** Nuance over Literal | ADR-META-001 | "shared catalog (no org_id)" is intentional; D10 trumps any default to add `org_id`. |
| **D3** No Self-Contradiction | ADR-META-001 | If a D1 query returns a different count than the expected baseline, the *expected* number is wrong — do NOT silently rewrite reality. |
| **D4** Coût d'Escalade A0 | ADR-META-001 | If the FK `build_projects` does not exist or is named differently, STOP and escalate to A2 — do not improvise. |
| **D5** Idempotence | ADR-META-001 | Every CREATE / POLICY / INSERT must be re-runnable. Use `IF NOT EXISTS` and `ON CONFLICT DO NOTHING`. |
| **D6** Write-Back | ADR-META-001 | Wiki + MEMORY_CORE + handoff are *part of the task*, not optional. |
| **D7** FORCE_TARGET=1 only on dev | ADR-ABCOS-001 | Production requires explicit A0 approval. Today: dev only. |
| **D8** Cross-agent portée | ADR-META-001 | The 3-file write-back must use the paths A0 already uses — do not invent new locations. |
| **D10** Mixed-Tenancy | ADR-ABCOS-001 | `build_resources` is `shared`; RLS = `authenticated` only; no `org_id` column. |

---

## 3. Migration File (idempotent .sql DDL)

> **Path** (proposed): `C:/Users/amado/A'Space OS V2/30_Business_OS/10_Projects/abc_os/migrations/20260612_add_build_resources.sql`
> If the project uses a different migration folder, **discover it first** via `Glob` of `**/abc_os/migrations/*.sql` before writing. If none exist, create the folder.

```sql
-- 20260612_add_build_resources.sql
-- Doctrine: ADR-META-001 D1-D8, ADR-ABCOS-001 D10 (mixed-tenancy, shared)
-- Idempotent: re-runnable safely. FORCE_TARGET=1 in dev only.

BEGIN;

-- 1) Table -----------------------------------------------------------------
CREATE TABLE IF NOT EXISTS abc_os.build_resources (
    id          TEXT        PRIMARY KEY,
    project_id  TEXT        NOT NULL
                REFERENCES abc_os.build_projects(id) ON DELETE CASCADE,
    title       TEXT        NOT NULL,
    kind        TEXT        NOT NULL
                CHECK (kind IN ('tool','material','technique')),
    url         TEXT,
    sort_order  INTEGER     NOT NULL DEFAULT 0,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 2) Indexes ---------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_build_resources_project_id
    ON abc_os.build_resources (project_id);
CREATE INDEX IF NOT EXISTS idx_build_resources_project_sort
    ON abc_os.build_resources (project_id, sort_order);

-- 3) RLS -------------------------------------------------------------------
ALTER TABLE abc_os.build_resources ENABLE ROW LEVEL SECURITY;

-- Drop a prior policy if it exists, to keep the script re-runnable.
DROP POLICY IF EXISTS build_resources_select_authenticated
    ON abc_os.build_resources;

CREATE POLICY build_resources_select_authenticated
    ON abc_os.build_resources
    FOR SELECT
    TO authenticated
    USING (true);

-- 4) Migration tracker (D1: log every apply) -------------------------------
-- Assume a tracker table of the shape (id SERIAL, applied_at TIMESTAMPTZ,
-- migration_name TEXT UNIQUE, sha256 TEXT).
INSERT INTO abc_os.migrations (migration_name, applied_at, sha256)
VALUES (
    '20260612_add_build_resources',
    now(),
    encode(digest('20260612_add_build_resources', 'sha256'), 'hex')
)
ON CONFLICT (migration_name) DO NOTHING;

COMMIT;
```

> **Note (D4)**: If `abc_os.build_projects` does not exist or its PK column is not `id TEXT`, **STOP** and escalate to A2. Do not rename columns silently.

---

## 4. `apply-abc-os-migrations.sh` Update

> **Path** (proposed): `C:/Users/amado/A'Space OS V2/30_Business_OS/10_Projects/abc_os/scripts/apply-abc-os-migrations.sh`
> If a different path exists, follow it. Confirm via `Glob` first.

### 4.1 Pre-flight list (always echo, do not skip)

Add the new migration to the pre-flight `echo` block (single source of truth for what will be applied):

```bash
echo "[apply-abc-os-migrations] pending migrations:"
echo "  - 20260612_add_build_resources.sql  (NEW: shared build_resources catalog)"
```

### 4.2 apply_sql block (dev + prod branches)

```bash
apply_sql() {
    local target="$1"   # "dev" | "prod"
    local file="$2"

    case "$target" in
        dev)
            if [ "${FORCE_TARGET:-0}" != "1" ]; then
                echo "[ERR] dev apply requires FORCE_TARGET=1" >&2
                exit 2
            fi
            echo "[apply] dev <- $file"
            psql "$ABC_OS_DEV_URL" -v ON_ERROR_STOP=1 -f "$file"
            ;;
        prod)
            # D7: prod requires explicit A0 sign-off; this branch must NOT
            # run from FORCE_TARGET=1. We hard-fail if forced.
            if [ "${FORCE_TARGET:-0}" = "1" ]; then
                echo "[ERR] FORCE_TARGET=1 forbidden on prod" >&2
                exit 3
            fi
            echo "[apply] prod <- $file"
            psql "$ABC_OS_PROD_URL" -v ON_ERROR_STOP=1 -f "$file"
            ;;
        *)
            echo "[ERR] unknown target: $target" >&2
            exit 4
            ;;
    esac
}
```

### 4.3 Invocation (today = dev only)

```bash
FORCE_TARGET=1 ./apply-abc-os-migrations.sh dev \
    ./migrations/20260612_add_build_resources.sql
```

---

## 5. D1 Verify Queries (run after apply, capture exact output)

These are the **5 standard D1 verify queries** + **2 build_resources-specific spot-checks**. Run all 7. Capture the raw output. Re-run if any count seems off — never assert without re-queried evidence (D1).

### 5.1 Standard (5)

```sql
-- Q1: total tables in abc_os
SELECT count(*) AS tables
  FROM information_schema.tables
 WHERE table_schema = 'abc_os';

-- Q2: tables with RLS enabled
SELECT count(*) AS rls_enabled
  FROM pg_tables t
  JOIN pg_class c ON c.relname = t.tablename
 WHERE t.schemaname = 'abc_os'
   AND c.relrowsecurity;

-- Q3: total policies in abc_os
SELECT count(*) AS policies
  FROM pg_policies
 WHERE schemaname = 'abc_os';

-- Q4: migrations logged
SELECT count(*) AS migrations_logged
  FROM abc_os.migrations;

-- Q5: most recent migration row
SELECT migration_name, applied_at
  FROM abc_os.migrations
 ORDER BY applied_at DESC
 LIMIT 1;
```

### 5.2 build_resources spot-checks (2)

```sql
-- S1: table exists with expected columns + check constraint
SELECT column_name, data_type, is_nullable, column_default
  FROM information_schema.columns
 WHERE table_schema = 'abc_os'
   AND table_name   = 'build_resources'
 ORDER BY ordinal_position;

-- S2: RLS enabled + exactly one SELECT policy for 'authenticated'
SELECT c.relrowsecurity AS rls_enabled,
       (SELECT count(*) FROM pg_policies
         WHERE schemaname = 'abc_os'
           AND tablename  = 'build_resources'
           AND cmd        = 'SELECT'
           AND roles::text[] @> ARRAY['authenticated']::name[]) AS select_policies
  FROM pg_class c
  JOIN pg_namespace n ON n.oid = c.relnamespace
 WHERE n.nspname = 'abc_os' AND c.relname = 'build_resources';
```

### 5.3 Expected post-apply counts (baseline for comparison ONLY)

> **D1 / D3 reminder**: these are baselines. Re-query everything. If actual ≠ expected, **the actual is truth** — report the delta to A2; do not "fix" the wiki to match expectation.

| Metric | Expected |
|---|---|
| tables in `abc_os` | **18** |
| tables with RLS enabled | **18** |
| policies in `abc_os` | **43** |
| migrations_logged | **13** |
| `build_resources.select_policies` | 1 |
| `build_resources.rls_enabled` | true |

---

## 6. Write-Back Contract (3 files — D6, D8)

After D1 verification passes, update **exactly these three files**. Paths are absolute. Do not create new wiki pages.

### 6.1 `C:/Users/amado/A'Space OS V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`

Append a dated block (do not edit prior entries):

```markdown
## 2026-06-12 — abc_os.build_resources (shared catalog)

- Migration: `20260612_add_build_resources.sql` applied to **dev** (FORCE_TARGET=1)
- Doctrine: ADR-META-001 (D1-D8), ADR-ABCOS-001 (D10 mixed-tenancy, shared)
- Tenancy: shared (no `org_id`) — parent `build_projects` is tenant-scoped
- RLS: `SELECT` to `authenticated` only
- D1 counts (post-apply, RE-QUERIED): tables=__ __ · RLS=__ __ · policies=__ __ · migrations_logged=__ __
- Spot-checks: `build_resources` RLS=on, select_policies=__ __
```

> Fill the blanks with the *actual* values from the re-queried D1 run, not from the baseline table.

### 6.2 `C:/Users/amado/A'Space OS V2/00_Amadeus/30_MEMORY_CORE/README.md`

Add a one-line entry in the "Recent schema changes" section (create the section if absent):

```markdown
- **2026-06-12** — `abc_os.build_resources` added (shared catalog, D10). See `wiki/log.md` for D1 verification trail.
```

### 6.3 `C:/Users/amado/A'Space OS V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md`

Append a **2026-06-12 follow-up** subsection at the end of the handoff:

```markdown
### 2026-06-12 follow-up — build_resources (shared catalog)

- Added `abc_os.build_resources` (id, project_id FK, title, kind, url, sort_order, created_at).
- Shared (D10): no `org_id`; RLS = `authenticated` SELECT.
- Applied to dev under FORCE_TARGET=1. Prod branch still gated (D7).
- D1 verify: <paste actual counts here, NOT the baseline>.
- Migration row: `20260612_add_build_resources` in `abc_os.migrations`.
- Next: confirm with A0 before any prod apply.
```

---

## 7. Execution Checklist (A3, tick as you go)

- [ ] **Discover paths**: `Glob` for `**/abc_os/migrations/*.sql` and `**/abc_os/scripts/apply-abc-os-migrations.sh` to confirm exact locations.
- [ ] **Confirm FK target**: verify `abc_os.build_projects(id)` exists with `id TEXT PK`. If not → escalate (D4).
- [ ] **Pre-flight echo**: add the new migration name to the script's pending list.
- [ ] **apply_sql branch**: confirm both `dev` and `prod` arms respect `FORCE_TARGET`.
- [ ] **Apply**: `FORCE_TARGET=1 ./apply-abc-os-migrations.sh dev ./migrations/20260612_add_build_resources.sql`
- [ ] **D1 verify (5 standard + 2 spot)** — capture raw output.
- [ ] **Compare to baseline** — report deltas, do not coerce (D1/D3).
- [ ] **Write-back** to the 3 files in section 6, using **actual** counts.
- [ ] **Final report** to A2: paste the 7 query results + the 3 file diffs + any deviation from baseline.

---

## 8. Stop Conditions (escalate to A2, do not improvise)

1. `abc_os.build_projects` does not exist, has a different PK name, or PK is not TEXT.
2. `abc_os.migrations` does not exist (you'll need a different tracker table — A2 must confirm).
3. D1 actual counts diverge from baseline by more than the deltas implied by this single migration (+1 table, +1 RLS, +1 policy, +1 migration row).
4. `psql` apply errors on the CHECK constraint, FK, or RLS policy.
5. `FORCE_TARGET=1` is missing from the env (D7: refuse to apply).

---

## 9. Out of Scope (do NOT do)

- Do NOT add `org_id` to `build_resources` (D10).
- Do NOT enable `INSERT`/`UPDATE`/`DELETE` policies (A0 specified `select-authenticated` only).
- Do NOT touch prod (D7 — requires explicit A0 sign-off).
- Do NOT rewrite prior entries in `wiki/log.md` or the handoff (append only).
- Do NOT create new wiki pages or new MEMORY_CORE files (D8).
- Do NOT skip the D1 re-query and just paste the baseline into the write-back (D1/D3).

---

## 10. Definition of Done (A3 → A2)

A complete report to A2 contains:

1. The `psql` apply output (or a one-line success indicator with row counts).
2. The 7 D1 verify query results, raw.
3. A side-by-side: expected baseline vs. actual, with deltas called out.
4. The 3 file write-backs, with diffs or appended sections shown.
5. A green/red status for each of the 6 assertions in `eval_metadata.json`.

A2 will then relay to A0 for sign-off on a future prod apply.
