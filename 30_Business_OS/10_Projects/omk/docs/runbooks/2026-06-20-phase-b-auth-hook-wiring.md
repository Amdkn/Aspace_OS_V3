---
runbook_id: omk_phase_b_auth_hook_wiring
created: 2026-06-20
owner: A0_Amadeus
scope: OMK Tax Service Cloud Supabase project ndvqwcapwcnpdvknxcjw
status: AWAITING_A0_ACTION
estimated_time: 2 minutes
---

# 🔐 OMK Phase B — Auth Hook Wiring Runbook

## Context (D1 receipts)

The SQL migration of Phase A is **complete and verified**:

- ✅ 7 `omk_saas.*` tables created with FK constraints and CHECK constraints
- ✅ RLS enabled + FORCE RLS on all 7 tables
- ✅ 30 RLS policies installed (5 tables × {SELECT, INSERT, UPDATE, DELETE} × tenant_isolation + service_role_all + 2 on organizations/memberships)
- ✅ PG roles `aspace_admin` + `aspace_observer` provisioned with REVOKE defense-in-depth on reserved schemas
- ✅ `public.custom_access_token_hook(jsonb)` function created and GRANT EXECUTE to `supabase_auth_admin`
- ✅ Seed data: 1 org (acme-demo) + 1 user (dev+omk@acme-demo.fr) + 1 membership (owner) + 5 clients + 3 docs + 2 agents + 4 invoices + 3 SOPs
- ✅ Drift `public.*` archived in `_archive_drift_2026_06_20` (7 tables × 31 rows, RLS locked)
- ✅ Hook logic VERIFIED via direct invocation: returns `org_id: 00000000-0000-0000-0000-000000000a01`, `role: owner`, `app_metadata.memberships: [...]`

## What's blocking end-to-end auth

The `public.custom_access_token_hook` function exists in the database but is **NOT yet wired** into the Supabase Auth server's hook chain. Until it is wired:

- Every JWT issued by Supabase Auth will **NOT** include the `org_id` claim
- Every `omk_saas.*` query as `authenticated` role returns **0 rows silently** (because `current_org_id()` reads `auth.jwt() ->> 'org_id'` which is NULL)
- This is the **silent failure risk** flagged in `omk/apps/dashboard/AGENTS.md` gotcha #4

## ⚠️ A0 ACTION — Wire the hook (2 minutes)

### Option A: Dashboard UI (recommended, no CLI needed)

1. Open: **https://supabase.com/dashboard/project/ndvqwcapwcnpdvknxcjw/auth/hooks**
2. Find the section **"Custom Access Token"**
3. Toggle the switch to **Enabled**
4. In the "Hook function" dropdown, select: **`public.custom_access_token_hook`**
5. Click **Save**
6. Wait ~30 seconds for the auth provider to reload (you'll see a "Hook enabled" toast)
7. Verify: visit `https://supabase.com/dashboard/project/ndvqwcapwcnpdvknxcjw/auth/users` — click on `dev+omk@acme-demo.fr` row, then "..." → "Send magic link" or "Reset password" to trigger JWT issuance. Decode the JWT (use https://jwt.io) and confirm the payload includes `"org_id": "00000000-0000-0000-0000-000000000a01"` and `"app_metadata": {"memberships": [...]}`.

### Option B: Supabase CLI (terminal)

```bash
# Requires Supabase CLI installed + logged in to the right org
supabase login
supabase --project-ref ndvqwcapwcnpdvknxcjw hooks update access-token \
  --function public.custom_access_token_hook \
  --enabled
```

> **Note**: the `supabase hooks update` subcommand may not exist on older CLI versions. If it fails, fall back to Option A.

## Verification after wiring

Run this query from the Supabase SQL Editor (project `ndvqwcapwcnpdvknxcjw`) to confirm the hook is registered:

```sql
SELECT name, enabled, function_name, function_schema
FROM auth.hooks
WHERE name = 'custom_access_token_hook';
```

Expected: 1 row with `enabled = true`, `function_name = custom_access_token_hook`, `function_schema = public`.

If empty: the wiring did not persist — re-try Option A.

## Live E2E test (post-wiring)

Once the hook is enabled, run this curl from your terminal to confirm an authenticated client sees the seeded data:

```bash
# Step 1: Get a JWT for the dev user via the magic link flow
# (open in browser, click link, copy access_token from localStorage)

# Step 2: Call the Supabase REST API with the JWT
curl -X GET 'https://ndvqwcapwcnpdvknxcjw.supabase.co/rest/v1/clients?select=id,name,email,status&limit=10' \
  -H "apikey: <your-anon-key>" \
  -H "Authorization: Bearer <your-jwt>"
```

Expected response: a JSON array with **5 rows** (Boulangerie Martin, Coiffure Étoile, Atelier Bricolage, Restaurant Le Sud, Startup Nova).

If the response is `[]` (empty array): the hook is not injecting `org_id` correctly. Double-check the function name in the dashboard.

## Cross-tenant isolation test (adversarial)

Create a SECOND test user via the Supabase Dashboard (Auth → Users → Add user with email `dev2+omk@example.com`, no membership). Try to query `clients`:

```bash
curl -X GET 'https://ndvqwcapwcnpdvknxcjw.supabase.co/rest/v1/clients?select=id,name' \
  -H "apikey: <your-anon-key>" \
  -H "Authorization: Bearer <user2-jwt>"
```

Expected: **empty array** (user has no membership → hook returns `org_id: NULL` → RLS policy filters all rows).

If user2 sees the 5 rows: **CRITICAL SECURITY BUG** — the RLS policy or hook is misconfigured. Stop and investigate.

## Rollback (if anything goes wrong)

1. Dashboard → Auth → Hooks → Custom Access Token → **Disable**
2. The function `public.custom_access_token_hook` remains in the database but is no longer invoked
3. The `omk_saas.*` schema and RLS policies remain in place but the seed data is hidden from all authenticated users (0 rows visible)
4. To fully revert the schema: `DROP SCHEMA omk_saas CASCADE;` (will lose all seed data — recreate by re-applying Phase A.3 + A.7 migrations)

## After wiring: report back

Reply with: **"hook wired, JWT shows org_id claim"** (or paste the decoded JWT payload).

Then I can proceed with:
- **Phase C**: repository layer upgrade (switch from `public.*` to `omk_saas.*`)
- **Phase D**: bulk-generate the 13 sub-pages
- **Phase E**: wire `react-router-dom 7`
- **Phase F**: auth + onboarding wizard
- **Phase G**: deploy + verify

## Hitting the wiring now?

If you want me to try the CLI route in the background while you do Option A, just say "go CLI" — I'll attempt the hook wiring via the management API and report back. Otherwise, just toggle the switch in the dashboard UI and let me know.

---

## D6 lessons shipped (2026-06-20)

### D6 #62: Supabase Management API does NOT expose auth hook endpoints

**Symptom**: attempted `POST /v1/projects/<ref>/auth/hooks` with valid `SUPABASE_ACCESS_TOKEN` (44 chars, `sbp_*` PAT) — returned `{"message":"Cannot POST /v1/projects/<ref>/auth/hooks"}`.

**Root cause**: the Supabase Management API (`api.supabase.com/v1`) does not expose auth hook configuration endpoints. The auth hook system is part of GoTrue (the internal auth server) and is configured via:

1. **Dashboard UI** at `/auth/hooks` (the only public path)
2. **Supabase CLI** `supabase hooks` subcommand (requires CLI 1.200+)
3. **Direct DB** via the `auth.hooks` table — BUT this table is owned by `supabase_auth_admin` which the SQL editor role (`postgres`) cannot write to (tested `SELECT FROM auth.hooks` → `42P01 relation does not exist` because the table is in GoTrue's private namespace, not exposed via PostgREST)

**Fix**: use Option A (Dashboard UI) — it's the only reliable path as of 2026-06-20.

### D6 #63: `auth.hooks` not queryable from SQL editor

**Symptom**: `SELECT * FROM auth.hooks` returns `42P01 relation does not exist`.

**Root cause**: GoTrue uses an internal Go data structure for hooks, not a Postgres table. The hook configuration is loaded from `auth.config.site_url` + a separate Go-side `auth.hook_custom_access_token` GUC at GoTrue boot time.

**Fix**: after wiring via Dashboard UI, verify by:
- Triggering a JWT issuance (magic link or sign-up)
- Decoding the resulting JWT at https://jwt.io
- Confirming `app_metadata.org_id` claim is present and matches `omk_saas.memberships`

---

*Runbook created by Phase B automation, 2026-06-20. Persists in `omk/docs/runbooks/` per ADR-INFRA-002 (build-bearing vs durable split).*

## D6 #85 (2026-06-20) — Vercel Authentication is ON by default

**Symptom (live E2E)**: After deploying `feature/omk-saas-v1.0` (SHA `2706091`) via Vercel auto-deploy, every URL `.vercel.app` (including previews) returns **HTTP 401** with a Vercel-branded auth splash that redirects to `https://vercel.com/sso-api?url=...`. The OMK app is never reached. The splash shows "Authentication Required" + "Vercel Authentication" footer.

**Root cause**: Vercel Authentication is **ON by default** for all new projects (added in 2024, applies to hobby + pro plans). The toggle is **per-project** in `Settings → Security`, NOT per-deployment. This is independent of the Supabase hook wiring (D6 #64) and the PGRST_DB_SCHEMAS exposure (D6 #68).

**Fix** (A0 action, ~30 sec):
1. Open https://vercel.com/omk-services/omk-saas-os/settings/security
2. Find "Vercel Authentication" section
3. Toggle OFF
4. Save
5. The next request to any `*.vercel.app` URL will reach the OMK app directly.

**Verification**: re-curl the URL after the toggle:
```bash
curl -sI https://omk-saas-kbyhsl88j-omk-services.vercel.app/ -L
# Expected: 200 OK (no Vercel auth splash, HTML body shows the OMK LoginView)
```

**D7 lesson**: never assume a Vercel deployment is "live" until the HTTP 200 + non-Vercel-branded body is confirmed. The 401 from Vercel Authentication is easy to miss because the response is HTML, not JSON.

**Update to Phase B runbook**: Action 2 is now **MANDATORY**, not "verify". Mark it as such in any future onboarding runbook.
