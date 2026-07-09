# Iteration 2 — Anti-Doctrinal-Error Guards

**Date** : 2026-06-12
**Goal** : Iter 1 had `delta = +0.00` (both 100%). Add strict anti-doctrinal guards so the skill demonstrably helps.

## New Assertions (13 total, regex-based, mechanical)

| Error | Where | Guard |
|---|---|---|
| **E1** Fictional tracker (`abc_os.migrations` / `abc_os.schema_migrations`) | eval-1, eval-2 | Uses canonical `abc_os._aspace_migrations (filename)` + `ON CONFLICT (filename) DO NOTHING` |
| **E2** FORCE_TARGET=1 hard-fail in prod contradicts D10 | eval-1 | Shared-catalog DDL goes to both envs (no `exit 3`) |
| **E3** `service_role` in per-tenant SELECT USING | eval-2 | Uses canonical `FOR SELECT TO authenticated USING (org_id = abc_os.current_org_id())` |
| **E4** No verbatim Old/New structure on drift Edits | eval-3 | All 3 drift items have explicit `Old string` / `New string` labels |

5/5/3 split across eval-1/2/3.

## Pass Rates

| | With Skill | Without Skill | Delta |
|---|---:|---:|---:|
| **Iter 1** (6 lenient) | 100% | 100% | +0.00 |
| **Iter 2** (13 strict) | **100%** | **78.6%** | **+0.21** |

Per-eval iter 2: eval-1 100/75, eval-2 100/75, eval-3 100/86. Tokens +7283.

## Without-Skill Failures

- **eval-1** : invented `abc_os.migrations (id SERIAL, sha256)` + banned `FORCE_TARGET=1` in prod.
- **eval-2** : invented `abc_os.schema_migrations (version, filename)` + `current_role() IN ('anon','authenticated','service_role')` in SELECT USING.
- **eval-3** : read A0's "edit the handoff" as "no edits needed" — just prose, no Old/New labels. Sub-agent would make 0 data-row edits.

All 3 caught by the new guards.

## Iter 3 Recommendation

Keep all 13. Optional:
- Tighten 3-file write-back from count=3 to `substring_all` checking WHICH 3.
- Add env-var check: `$SUPABASE_DB_URL` / `lib/db.sh`, not `$ABC_OS_DEV_URL`.
- Add 4th error: shared-catalog DDL missing `DO` block with `EXCEPTION` for idempotent RLS re-enable.

Skill is now +21 pts better than no-skill.
