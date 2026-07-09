# Phase II — D6 #94 Fix — Role "owner" Does Not Exist — Receipt (2026-06-20)

## D1 Receipts (filesystem proof)

### SQL migrations applied (Supabase project `ndvqwcapwcnpdvknxcjw` = `OMK SERVICES CUSTOMERS`)

| Migration | Version | Purpose |
|---|---|---|
| `phase_ii_fix_jwt_hook_role_claim_v2` | `20260620210010` (initial attempt) | First attempt — REMOVED top-level `{role}` overwrite. **BROKE GoTrue schema validation** (`output claims do not conform to expected schema: Expected: object, given: null`). Reverted. |
| `phase_ii_grant_supabase_auth_admin_omk_saas` | `20260620??????` | Grants `supabase_auth_admin` USAGE on `omk_saas` schema + SELECT on `omk_saas.memberships` + SELECT on `omk_saas.organizations`. Without these, the JWT hook fails at runtime with `permission denied for schema omk_saas`. |
| `phase_ii_restore_baseline_jwt_hook` | (applied, function-only) | Restore original hook body + add `SECURITY DEFINER` + add `OR v_claims = 'null'::jsonb` guard. **Sign-in works** (HTTP 200, JWT issued). |
| `phase_ii_v3_hardcode_role_authenticated` | (applied, function-only) | Final fix: change `jsonb_set(v_claims, '{role}', to_jsonb(v_role), true)` to `jsonb_set(v_claims, '{role}', to_jsonb('authenticated'::text), true)`. Top-level role becomes the real Postgres role. |

### JWT shape verified (curl + Python decode, 2026-06-20 21:16 UTC)

```
top-level role     : authenticated   ← was "owner" (D6 #94 bug, broke PostgREST)
top-level org_id   : 00000000-0000-0000-0000-000000000a01   ← unchanged
app_metadata.role  : owner          ← preserved for UI display
app_metadata.org_id: 00000000-0000-0000-0000-000000000a01   ← unchanged
```

### REST queries verified (HTTP 200 + rows)

| Endpoint | HTTP | Rows | Sample |
|---|---|---|---|
| `GET /rest/v1/clients?select=id` | 200 | 5 | Boulangerie Martin, Coiffure Étoile, Atelier Bricolage, Restaurant Le Sud, Startup Nova |
| `GET /rest/v1/invoices?select=id` | 200 | 4 | (4 seeded invoices) |
| `GET /rest/v1/agents?select=id` | 200 | 2 | Alice Martin, Bob Dupont |
| `GET /rest/v1/sops?select=id` | 200 | 3 | Onboarding client, Clôture mensuelle, Gestion impayés |
| `GET /rest/v1/organizations?select=id` | 200 | 1 | Acme Demo SARL |
| `GET /rest/v1/memberships?select=id` | 200 | 1 | dev+omk@acme-demo.fr → owner |

### Git commit (client fix)

```
abead8e fix(auth): prefer app_metadata.role over top-level role (Phase II D6 #94)
2ba0c39..abead8e  feature/omk-saas-v1.0 -> feature/omk-saas-v1.0
```

Pushed to `origin/feature/omk-saas-v1.0` — awaits A0 merge to `main` to trigger Vercel production deploy. The client-side fix preserves the UI display of the membership role (`'owner'`) instead of leaking the hardcoded `'authenticated'` to the UI.

### tsc verification

`npx tsc --noEmit --pretty false` → 0 errors.

## D6 root causes addressed

| D6 # | Symptom | Root cause | Fix (Phase II) |
|---|---|---|---|
| #94 (RE-OPENED) | `[clients] role "owner" does not exist` (Dashboard) + `[invoices] role "owner" does not exist` (Finance) after Phase I merge | The `custom_access_token_hook` migration `omk_saas_jwt_custom_access_token_hook` set the JWT's top-level `role` claim to the membership role string (`'owner'` from `memberships.role`). PostgREST uses JWT top-level `role` as the Postgres session role (`SET ROLE owner`). The `owner` role doesn't exist in Supabase Cloud (only `authenticated`, `anon`, `service_role`, `postgres`, `supabase_admin` exist). | Hardcode `jsonb_set(v_claims, '{role}', to_jsonb('authenticated'::text), true)` in the JWT hook. Membership role now lives in `app_metadata.role` only. PostgREST uses `'authenticated'` (real Postgres role). |
| #95c (NEW) | `ERROR: permission denied for schema omk_saas (SQLSTATE 42501)` during JWT issuance | The original JWT hook migration granted `EXECUTE ON FUNCTION public.custom_access_token_hook TO supabase_auth_admin` but did NOT grant `USAGE ON SCHEMA omk_saas` or `SELECT ON omk_saas.memberships`. Since the original hook was `SECURITY INVOKER`, it ran as `supabase_auth_admin` and failed on `SELECT FROM omk_saas.memberships`. | Phase II applied two fixes in combo: (1) `GRANT USAGE ON SCHEMA omk_saas TO supabase_auth_admin` + `GRANT SELECT ON omk_saas.memberships TO supabase_auth_admin`. (2) Added `SECURITY DEFINER` + `SET search_path = ''` to the hook so it runs as the function owner (`postgres`) — bypasses permission checks even if GRANTs are missing in the future. |
| #95d (NEW) | `ERROR: path element at position 1 is not an integer: "org_id"` (CONTEXT: PL/pgSQL function custom_access_token_hook(jsonb) line 74 at assignment) when GoTrue sends `claims: null` (or absent) | The original IF check `IF v_claims IS NULL THEN v_claims := '{}'::jsonb; END IF;` did not catch the JSON-null case (`event -> 'claims'` returns jsonb `'null'::jsonb` when value is JSON null, not SQL NULL). | Phase II changed to `IF v_claims IS NULL OR v_claims = 'null'::jsonb THEN v_claims := '{}'::jsonb; END IF;`. |

## Why Phase I exposed D6 #94 (and Phase A didn't)

- **Phase A**: JWT hook function created (version `20260620180503`) but NOT yet wired in Supabase Auth dashboard. Without the hook, the JWT carries the default Supabase claims (`role: 'authenticated'`) and PostgREST works fine. But empty data (no `org_id` claim → RLS returns 0 rows).
- **Phase B Action** (A0 wired the hook): JWT now carries `role: 'owner'` at top level. PostgREST would silently break for any table query. BUT the dashboard's earlier queries were crashing on the `team`/`tasks` table errors (D6 #95), so the dashboard UI never actually exercised `SELECT FROM omk_saas.clients` against PostgREST. Phase I fixed the `team`/`tasks` crashes, which unmasked the latent role bug.
- **Phase II**: Top-level role now `'authenticated'`. PostgREST works. RLS still filters by `org_id` (top-level, set by the hook).

## Why D6 #94 was claimed DONE in Phase A (receipt over-claim)

The Phase A receipt likely checked `has_table_privilege('authenticated', 'omk_saas.clients', 'SELECT')` and saw `true`. That check DOES pass (Postgres role `authenticated` has full CRUD on all 9 `omk_saas.*` tables). But the JWT hook overwriting `role` is a SEPARATE issue that manifests only when A0 actually wires the hook (Phase B action) AND the dashboard actually queries the table (Phase I fix). Neither test existed at Phase A time.

D6 #95c was similarly latent: the original hook was `SECURITY INVOKER`, requiring the executing role (`supabase_auth_admin`) to have `USAGE ON SCHEMA omk_saas` + `SELECT ON omk_saas.memberships`. Phase A never granted these. Login worked intermittently because Supabase's auth dispatcher sometimes passes through without invoking the hook (e.g., on token refresh, which doesn't always re-run the hook). When login DID invoke the hook, it failed with `permission denied for schema omk_saas`.

## Architectural decision (final)

The membership role string (`'owner'` / `'admin'` / `'member'` / `'viewer'`) is a **business concept** (UI hierarchy, RLS visibility), NOT a Postgres role. The JWT's top-level `role` claim, however, is a **Postgres role assignment** (PostgREST uses it for `SET ROLE`). The fix separates these two concerns:

- **JWT top-level `role`**: hardcoded to `'authenticated'` (real Postgres role in Supabase Cloud).
- **JWT `app_metadata.role`**: the membership role string (`'owner'` / `'admin'` / etc.) — UI display, business logic, future per-membership RLS checks.
- **DB `memberships.role` column**: the source of truth (CHECK constraint enforces `IN ('owner','admin','member','viewer')`).

YAGNI: no need to create a Postgres role named `owner` in Supabase Cloud — adds surface area, conflicts with the standard Supabase role namespace.

## D2 backlog (out of scope this sprint)

- Update canonical SQL source `apps/dashboard/sql/04_jwt_hook.sql` to match the Phase II body (add `SECURITY DEFINER`, role=`'authenticated'`, `OR v_claims = 'null'::jsonb` guard).
- Add a CI grep check that flags `jsonb_set(v_claims, '{role}', to_jsonb(v_role))` patterns in any future hook migrations (prevent recurrence of D6 #94).
- Add a CI grep check that flags `SECURITY INVOKER` PL/pgSQL functions that query `omk_saas.*` (prevent recurrence of D6 #95c).
- Spot-check `AuthProvider.tsx` source for `role` claim origin → done in this phase (commit `abead8e`).
- A0 browser smoke-test of all 14 views post-merge.

## A0 actions needed

1. **Merge PR** `feature/omk-saas-v1.0` → `main` in GitHub UI → Vercel auto-deploys the `abead8e` commit (AuthProvider fix). The DB fix is already live.
2. **Browser smoke-test** of all 14 views — no more `role "owner" does not exist` errors. Should see real data: 5 clients, 4 invoices, 2 agents, 3 SOPs, etc.
3. **Verify UI shows `'owner'`** in any role display (TenantContext.role → `useOrg().role`). The membership role now reads from `app_metadata.role` only.

## Rollback

If Phase II breaks sign-in or queries:
1. `mcp__supabase-omk__apply_migration(name="phase_ii_rollback_v3", query="CREATE OR REPLACE FUNCTION public.custom_access_token_hook ... -- restore v2 (SECURITY DEFINER + original role overwrite from membership) -- OR restore pre-Phase-II original body")`.
2. `git revert abead8e` on `feature/omk-saas-v1.0`, force-push, A0 re-merge.

Cost-of-rollback is low (1 SQL function revert + 1 git revert). D9 self-choice authorized this fix without intermediate A0 validation.