---
name: cloud-bootstrap
description: Bootstrap a Supabase Cloud project with the OMK canonical schema (omk_saas.* + RLS + JWT hook + seed). Idempotent, re-runnable. Use when creating a new Supabase Cloud project, applying omk_saas to a fresh project, or auditing an existing one.
triggers:
  - "bootstrap supabase project"
  - "apply omk_saas schema"
  - "create cloud supabase for OMK"
  - "multi-tenant supabase setup"
  - "tenant isolation bootstrap"
  - "drift in supabase schema"
roi_minutes: 30
doctrine: |
  Matt Pocock — "Skills are a multiplier for AI... if I'm able to oversee a codebase and think
  about how things should be built and just tell AI how to do it, then AI just has so much richer
  context to work with." This skill encodes the strategic OMK tenant-isolation doctrine so
  that bootstrapping a new Cloud project is one command, not 6 manual migrations.
---

# Cloud Bootstrap — Supabase OMK SaaS Schema

## What this skill does

Takes a Supabase Cloud project_id and applies the canonical multi-tenant schema:

1. **Schema** — creates `omk_saas` schema + 9 tables (organizations, memberships, clients, documents, agents, invoices, sops, legal_docs, sales_leads)
2. **RLS** — enables + forces RLS on every table, installs tenant_isolation policies
3. **JWT hook** — creates `public.custom_access_token_hook` function (must be wired in Auth dashboard manually — D6 #64)
4. **PG roles** — provisions `aspace_admin` + `aspace_observer` with REVOKE defense-in-depth
5. **Seed** — optional dev seed: 1 org (acme-demo) + 1 user + 1 membership + sample data

**Idempotent** — re-running is safe (every DDL uses `IF NOT EXISTS` or `DROP IF EXISTS`).

## When to use

- Creating a new Supabase Cloud project for an OMK customer or OMK internal team
- Auditing an existing project that drifted from canonical schema
- Onboarding a new dev who needs a working dev environment
- Smoke-testing the schema after a Cloud infrastructure change

## When NOT to use

- Production data migration (this skill only creates schema, not data)
- Schema evolution (use `supabase/migrations/` directory + `apply_migration` for new columns)
- Non-OMK schemas (use direct SQL for non-canonical work)

## Prerequisites

- `mcp__supabase-omk__*` (or `mcp__supabase__*` for non-OMK) tools available
- Supabase project created + service_role key accessible (auto-injected for Edge Functions)
- A0 to manually wire the JWT hook in Auth dashboard (D6 #64, ~2 min)

## Workflow

### Step 1: Verify the target project

```typescript
mcp__supabase-omk__get_project({ id: "<project_id>" })
// Verify: status === "ACTIVE_HEALTHY", region = us-west-2 (or whatever)
```

### Step 2: Apply the 6 canonical migrations (in order)

The canonical schema is split across 6 SQL files in `C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/dashboard/sql/`:

| # | File | Purpose | Order matters? |
|---|------|---------|----------------|
| 1 | `02_omk_saas_schema.sql` | Schema + 7 core tables | YES — must be first |
| 2 | `03_rls_policies.sql` | RLS + 30 policies | YES — after 02 |
| 3 | `06_provision_pg_roles_omk.sql` | aspace_admin + aspace_observer | YES — after 03 (so GRANTs work) |
| 4 | `04_jwt_hook.sql` | custom_access_token_hook | YES — after 03 (so policy checks pass) |
| 5 | `05_seed_dev.sql` | 1 org + 5 clients + docs/agents/invoices/sops | NO — only for dev/staging |
| 6 | (Phase D addendum) | 2 tables: legal_docs + sales_leads + RLS | YES — after 04 |

**Important**: `apply_migration` does NOT accept `BEGIN` / `COMMIT` blocks. The seed file (05) has been adapted to omit them. If you copy other SQL files directly, strip psql meta-commands (`\set`, `\echo`, `\if`) — they will fail with cryptic errors.

### Step 3: Apply via `mcp__supabase-omk__apply_migration`

```typescript
mcp__supabase-omk__apply_migration({
  project_id: "<project_id>",
  name: "omk_saas_schema_canon",  // snake_case, no spaces
  query: "<read file 02, paste contents>",
})
// Repeat for files 03, 06, 04, 05, 06_addendum
```

### Step 4: Verify

```sql
-- Run via mcp__supabase-omk__execute_sql
SELECT 'tables' AS check, count(*) AS value
FROM pg_tables WHERE schemaname = 'omk_saas'
UNION ALL SELECT 'rls_policies', count(*) FROM pg_policies WHERE schemaname = 'omk_saas'
UNION ALL SELECT 'roles', count(*) FROM pg_roles WHERE rolname IN ('aspace_admin', 'aspace_observer')
UNION ALL SELECT 'jwt_hook', 1 FROM pg_proc WHERE proname = 'custom_access_token_hook';
-- Expected: tables=9, rls_policies=40+, roles=2, jwt_hook=1
```

### Step 5: A0 ACTION — wire the JWT hook (D6 #64)

Cannot be done via API. A0 must:
1. Open https://supabase.com/dashboard/project/<ref>/auth/hooks
2. Enable "Custom Access Token" → function `public.custom_access_token_hook`
3. Save

This is the ONLY manual step. Without it, every SaaS query returns 0 rows silently.

### Step 6: A0 ACTION — expose omk_saas schema in PostgREST (D6 #68)

Cannot be done via API. A0 must:
1. Open https://supabase.com/dashboard/project/<ref>/settings/api
2. Under "Exposed schemas", add `omk_saas` (alongside `public`)
3. Save (~30s PostgREST restart)

Without this, the REST API returns 404 for any `omk_saas.*` table.

## Outputs

- 1 schema (`omk_saas`)
- 9 tables (7 core + 2 added in Phase D)
- ~40 RLS policies (CRUD × 7 + CRUD × 2 + org/memberships special)
- 2 PG roles (`aspace_admin`, `aspace_observer`)
- 1 JWT hook function
- 1 dev org with sample data (if step 5 ran)

## Verification end-to-end

```bash
# 1. Direct DB probe
PGPASSWORD="<service_role_pw>" psql -h db.<ref>.supabase.co -U postgres -d postgres -c \
  "SELECT count(*) FROM omk_saas.clients; SELECT count(*) FROM omk_saas.organizations;"

# 2. JWT injection test (after A0 wires hook)
# Sign in as dev+omk@acme-demo.fr, decode JWT at https://jwt.io
# Expected: app_metadata.org_id = 00000000-0000-0000-0000-000000000a01

# 3. REST API test (after A0 exposes schema)
curl -X GET 'https://<ref>.supabase.co/rest/v1/clients?select=id,name,email&limit=5' \
  -H "apikey: <anon_key>" \
  -H "Authorization: Bearer <jwt_from_step_2>"
# Expected: 5 rows (Boulangerie Martin, Coiffure Étoile, etc.)
```

## D6 lessons shipped (encoded in this skill)

- **D6 #64**: JWT hook wiring is dashboard-only (no API path)
- **D6 #68**: PGRST_DB_SCHEMAS is dashboard-only
- **D6 #77**: Deno Edge Functions have separate tsc context (exclude from dashboard tsconfig)
- **D6 #79**: refreshSession() required to re-issue JWT after org creation
- **D6 #80**: Rollback on partial failure in Edge Functions (orphaned orgs prevention)

## Anti-pattern guards

- **D4 no-hard-delete**: drift tables archived in `_archive_drift_<date>` schema, not DROPped without trace
- **D7 cost-of-escalation**: A0 only needs 2 manual UI clicks (2-3 min total), not a 30-min HITL session
- **Skill Creator Reflex**: this skill is the strategic encoding of the doctrine — not a one-off shell command

## Related skills

- `aspace-supabase-mastery` — broader Supabase patterns (RLS, JWT, storage)
- `abc-os-backend-delegation` — backend workflow for abc-os community
- `abc-os-write-back-protocol` — write-back to canon after schema changes

## Related ADRs

- ADR-OMK-001 — dual-product dashboard (AMENDED 2026-06-19 to single SaaS)
- ADR-OMK-002 — PG roles provisionning
- ADR-OMK-004 — pivot Supabase Cloud + Vercel
- ADR-OMK-005 — tenant isolation guard (this skill implements it server-side)
