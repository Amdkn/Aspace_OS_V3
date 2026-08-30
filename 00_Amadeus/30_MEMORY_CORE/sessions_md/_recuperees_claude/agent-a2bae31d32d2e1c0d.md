---
session: agent-a2bae31d32d2e1c0d
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\_ARCHIVE_2026-06-16_sessions\projects\C--Users-amado\fe190d85-1d20-4b6b-ad09-92f637cc69ab\subagents\agent-a2bae31d32d2e1c0d.jsonl
debut: 2026-06-13T18:34:59.972Z
fin: 2026-06-13T18:36:55.791Z
messages_utilisateur: 1
reponses_assistant: 4
titre: "You are an Edit-only sub-agent for 2 surgical patches on OMK Dashboard SQL files. NO Write, NO Remove-Item, NO…"
---

## >>> UTILISATEUR #1

You are an Edit-only sub-agent for 2 surgical patches on OMK Dashboard SQL files. NO Write, NO Remove-Item, NO Move, NO new files.

# CONTEXT

Script `06_provision_pg_roles_omk.sql` (325 lines) failed end-to-end on the VPS for 2 reasons:
1. Sanity check (l.38-44) requires `current_user` to be `rolsuper`. On Supabase self-hosted, `postgres` is NOT rolsuper — `supabase_admin` is. The script must accept either.
2. REVOKE block (l.179-197) fails hard at line 185 (`REVOKE ALL ON SCHEMA pgsodium FROM aspace_admin`) because pgsodium extension is not installed on this Supabase 15.8.1.085. Same risk for `supabase_functions` and `pgbouncer` (also potentially absent). Need to wrap these 6 lines (3 extensions × 2 roles) in `IF EXISTS` guards.

Plus a documentation fix in `99_README.md`: add a note that host port 5432 is bound to `supabase-pooler` (Supavisor), not `supabase-db`, and the workaround is `docker exec supabase-db psql` with `docker cp` for the SQL file.

# D1 SOURCES TO READ FIRST (mandatory, before any Edit)

1. `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\dashboard\sql\06_provision_pg_roles_omk.sql` lines 1-50 (sanity check) + lines 170-200 (REVOKE block) + lines 280-325 (rollback). Understand the structure.
2. `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\dashboard\sql\99_README.md` lines 30-45 (Post-deploy section). Find the right insertion point.
3. `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\ADR-OMK-002_pg-roles-provisionning.md` lines 38-80 (D1, D2 contract). Confirm the contract doesn't dictate the sanity check implementation details.

# EDITS

## Edit 1 — Loosen sanity check in `06_provision_pg_roles_omk.sql` lines 38-44

The current sanity check requires `rolsuper=true`. On Supabase self-hosted, the superuser is `supabase_admin`, not `postgres`. Loosen the check to accept any of:
- `rolsuper=true` (classic PG superuser)
- `current_user = 'supabase_admin'` (Supabase convention)
- `rolbypassrls=true` (service_role pattern)

OLD (lines 38-44, exact block):
```sql
  SELECT rolsuper INTO v_is_superuser FROM pg_roles WHERE rolname = current_user;
  IF v_is_superuser IS NULL OR v_is_superuser = false THEN
    RAISE EXCEPTION 'This script must be run as a superuser (postgres). Current user: %', current_user;
  END IF;
  RAISE NOTICE 'Sanity check OK: current user % is superuser', current_user;
```

NEW (replacement block):
```sql
  SELECT rolsuper, rolbypassrls INTO v_is_superuser, v_has_bypassrls FROM pg_roles WHERE rolname = current_user;
  IF v_is_superuser IS NULL OR (v_is_superuser = false AND current_user <> 'supabase_admin' AND (v_has_bypassrls IS DISTINCT FROM true)) THEN
    RAISE EXCEPTION 'This script must be run as a superuser (postgres / supabase_admin) or a BYPASSRLS role. Current user: %', current_user;
  END IF;
  RAISE NOTICE 'Sanity check OK: current user % is authorized (superuser or BYPASSRLS)', current_user;
```

## Edit 2 — Wrap absent-schema REVOKEs in `06_provision_pg_roles_omk.sql` lines 185-187, 195-197

Three extensions can be absent on Supabase self-hosted: `pgsodium`, `supabase_functions`, `pgbouncer`. The script's REVOKE block fails hard on these. Wrap each pair (admin + observer) in `IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = '...')` guard.

OLD (6 lines to replace, lines 185-187 then 195-197):
```sql
REVOKE ALL ON SCHEMA pgsodium          FROM aspace_admin;
REVOKE ALL ON SCHEMA supabase_functions FROM aspace_admin;
REVOKE ALL ON SCHEMA pgbouncer         FROM aspace_admin;
```

NEW (replace these 3 lines, lines 185-187):
```sql
-- REVOKE guarded: pgsodium, supabase_functions, pgbouncer may be absent on Supabase self-hosted
DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'pgsodium')          THEN REVOKE ALL ON SCHEMA pgsodium          FROM aspace_admin; END IF; IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'supabase_functions') THEN REVOKE ALL ON SCHEMA supabase_functions FROM aspace_admin; END IF; IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'pgbouncer')         THEN REVOKE ALL ON SCHEMA pgbouncer         FROM aspace_admin; END IF; END $$;
```

OLD (3 lines to replace, lines 195-197):
```sql
REVOKE ALL ON SCHEMA pgsodium          FROM aspace_observer;
REVOKE ALL ON SCHEMA supabase_functions FROM aspace_observer;
REVOKE ALL ON SCHEMA pgbouncer         FROM aspace_observer;
```

NEW (replace these 3 lines, lines 195-197):
```sql
DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'pgsodium')          THEN REVOKE ALL ON SCHEMA pgsodium          FROM aspace_observer; END IF; IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'supabase_functions') THEN REVOKE ALL ON SCHEMA supabase_functions FROM aspace_observer; END IF; IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'pgbouncer')         THEN REVOKE ALL ON SCHEMA pgbouncer         FROM aspace_observer; END IF; END $$;
```

## Edit 3 — Add pooler note in `99_README.md` after line 35

Find the line that says "**Post-deploy step (HITL, VPS):** add `omk_internal,omk_saas` to `PGRST_DB_SCHEMAS` and restart `supabase-core`" (around line 35). Insert a new paragraph immediately AFTER that line.

NEW paragraph to insert (after line 35):
```markdown

**Pooler note (HITL, sub-agent 2026-06-11)**: Host port 5432 on the VPS is bound to `supabase-pooler` (Supavisor), **not** to `supabase-db` directly. As a result, `psql -h localhost -p 5432 -U postgres` fails with "Tenant or user not found" (the pooler requires a tenant name). The HITL executor must use one of these workarounds:
- `docker cp 06_provision_pg_roles_omk.sql srv941028:/tmp/ && ssh srv941028 "docker cp /tmp/06_provision_pg_roles_omk.sql supabase-db:/tmp/ && docker exec supabase-db psql -U supabase_admin -d postgres -v ON_ERROR_STOP=1 -f /tmp/06_provision_pg_roles_omk.sql -v section=apply"` (host `/tmp` is not visible inside containers; double `docker cp` is required).
- Or pipe the SQL via stdin: `cat 06_provision_pg_roles_omk.sql | ssh srv941028 "docker exec -i supabase-db psql -U supabase_admin -d postgres -v ON_ERROR_STOP=1 -v section=apply"`.

Sanity check was loosened in the script (l.38-44) to accept `supabase_admin` in addition to classic `rolsuper` roles.
```

# DOCTRINE CONSTRAINTS

- Edit ONLY these 2 files. No Write, no Remove-Item, no Move, no new files.
- Do NOT touch the rollback section (lines 280-325) — it's still correct.
- Do NOT touch any DDL file (01-05).
- Do NOT touch `_SPECS/ADR/`.
- Verify each Edit by Reading the modified file after the Edit (sanity check the surrounding lines are intact).
- D1 proof: each Edit must cite `path:line — AVANT: "..."` then `APRÈS: "..."` (or the inserted block).

# D7 REPORT FORMAT (final message, under 600 words)

For each Edit: `path:line — AVANT` / `APRÈS` / verification Read showing the surrounding lines (1-2 lines before + after) are intact.

Then 5-line self-check:
(a) D1 sources read
(b) Script compiles mentally (psql syntax valid: DO $$ ... END $$; nested IF EXISTS)
(c) 99_README new paragraph is at the right insertion point
(d) No DDL (01-05) touched
(e) No _SPECS/ADR/ touched, no Write, no destructive ops

Keep your final report under 600 words. Go.

### assistant

I'll execute these 3 surgical edits. Let me start by reading the D1 sources.

### assistant

D1 sources read. I have the exact line numbers, the structure, and the contract. The D1 decision doesn't dictate sanity check implementation details, so my edits stay within scope. Now executing the 3 edits.

### assistant

All 4 edits applied. Now verifying by Reading the modified files to confirm surrounding lines are intact.

### assistant

All 3 edits verified. Surrounding lines intact (section comments above/below untouched, REVOKE blocks before/after still present, READMEs Post-deploy step retained). Now final D7 report.

# D7 Report — 3 Surgical Edits Complete

## Edit 1 — `06_provision_pg_roles_omk.sql:38-44` sanity check loosened

**AVANT** (l.38-44): `SELECT rolsuper INTO v_is_superuser` → `IF v_is_superuser IS NULL OR v_is_superuser = false` → "must be run as a superuser (postgres)"

**APRÈS** (l.38-44): `SELECT rolsuper, rolbypassrls INTO v_is_superuser, v_has_bypassrls` → `IF v_is_superuser IS NULL OR (v_is_superuser = false AND current_user <> 'supabase_admin' AND (v_has_bypassrls IS DISTINCT FROM true))` → "must be run as a superuser (postgres / supabase_admin) or a BYPASSRLS role"

**Verification (Read)**: l.33 (comment "Refuse d'exécuter si on n'est pas connecté en tant que superuser (postgres)") and l.47 (empty line) intact. DO/DECLARE/BEGIN/END/$$; structure preserved.

## Edit 2 — `06_provision_pg_roles_omk.sql:185-187` admin REVOKEs guarded

**AVANT** (l.185-187): 3 plain `REVOKE ALL ON SCHEMA pgsodium/supabase_functions/pgbouncer FROM aspace_admin;` lines

**APRÈS** (l.186-187): 1 inline comment + 1 single-line `DO $$ BEGIN IF EXISTS ... END IF; END $$;` wrapping the 3 conditional REVOKEs via `pg_namespace` lookup

**Verification (Read)**: l.184 `REVOKE ALL ON SCHEMA vault FROM aspace_admin;` and l.189 `REVOKE ALL ON SCHEMA auth FROM aspace_observer;` intact. Section header (l.171) untouched.

## Edit 3 — `06_provision_pg_roles_omk.sql:195-197` observer REVOKEs guarded

**AVANT** (l.195-197): 3 plain `REVOKE ALL ON SCHEMA pgsodium/supabase_functions/pgbouncer FROM aspace_observer;` lines

**APRÈS** (l.195): 1 single-line `DO $$ BEGIN IF EXISTS ... END IF; END $$;` wrapping the 3 conditional REVOKEs

**Verification (Read)**: l.194 `REVOKE ALL ON SCHEMA vault FROM aspace_observer;` and l.197-198 section header (`11. POST-PROVISIONNING VERIFY`) intact.

## Edit 4 — `99_README.md:35` pooler note inserted

**AVANT** (l.35): "**Post-deploy step (HITL, VPS):** add `omk_internal,omk_saas` to `PGRST_DB_SCHEMAS` and restart `supabase-core`..." (followed by `---` on l.37)

**APRÈS** (l.35-41): Post-deploy step retained, then blank line, then "**Pooler note (HITL, sub-agent 2026-06-11)**" paragraph (3 sub-bullets + sanity check mention) inserted, then `---` separator preserved on l.43

**Verification (Read)**: l.33 dashboard post-deploy step and l.43 `---` separator both intact. The new block is sandwiched between the two existing post-deploy paragraphs as intended.

## Self-Check (5 lines)

(a) D1 sources read: `06_provision_pg_roles_omk.sql` (l.1-50, l.170-204), `99_README.md` (l.25-49), `ADR-OMK-002_pg-roles-provisionning.md` (l.38-87) — all confirmed. ADR-OMK-002 D1 defines role attributes only, not sanity check implementation → edits are within scope.

(b) Script compiles mentally: `DO $$ BEGIN IF EXISTS (...) THEN REVOKE ...; END IF; END $$;` is valid psql plpgsql (the original file already uses this exact `DO $$` pattern on l.65-79). `IS DISTINCT FROM true` handles NULLs correctly for `rolbypassrls`. Sanity check SELECT now reads two columns into two declared booleans — type matches.

(c) 99_README insertion point: paragraph is after l.35 "Post-deploy step (HITL, VPS)" and before l.37 `---` separator — exactly as specified.

(d) No DDL (01-05) touched: only `06_provision_pg_roles_omk.sql` and `99_README.md` were modified.

(e) No _SPECS/ADR/ touched, no Write, no Remove-Item, no Move, no new files created. Rollback section (l.280-325) untouched. No destructive ops.

**Files modified** (absolute paths):
- `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\dashboard\sql\06_provision_pg_roles_omk.sql`
- `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\dashboard\sql\99_README.md`
