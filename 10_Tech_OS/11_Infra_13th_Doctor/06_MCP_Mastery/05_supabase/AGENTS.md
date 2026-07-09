# 05_supabase — DOX leaf for Supabase MCP

> Parent: `../AGENTS.md`. Framework: `../../06_MCP_Mastery_dox/AGENTS.md`.
> Canon: leaf skill `/aspace-supabase-mastery` (master copy, 113 lines). Read that first.
> Vault: NO token (self-hosted, SSH-keyed). Auth = ssh `aspace-vps` as `amadeus`.

## Purpose

The Supabase MCP is the **database plane** of A'Space OS. It drives:
- Schema creation (one schema per product: `omk_internal`, `omk_saas`, `solaris_*`).
- RLS hardening (one policy per tenant boundary).
- PostgREST exposure (`PGRST_DB_SCHEMAS`).
- TypeScript type generation for the dashboards.
- Live queries for debugging (read-only `supabase-solaris`, RW `supabase-aspace`).

## Ownership

- A0 Amadeus — approves schema deletion, RLS policy removal, prod migrations.
- A2 Claude Code — orchestrates schema bootstrap, RLS work, type-gen.
- A3 sub-agent — runs `mcp__supabase__*` via the SSH tunnel.

## Local Contracts

### Auth

- No token. SSH alias: `aspace-vps` (`148.230.92.235`, user `amadeus`).
- Launch script (VPS): `/home/amadeus/symphony-workers/mcp-supabase-launch.sh`.
- The script uses `docker inspect` to get the current `supabase-db` IP dynamically (was
  hardcoded `172.19.0.2`, drifted to `172.19.0.3`, fixed by Antigravity on 2026-06-10).
- DB user for writes: `aspace_admin` (NoSuperuser, no access to `auth`/`storage`/`realtime`/`vault`).

### Schemas (current, verified 2026-06-10)

| Schema | Purpose | anon GRANT | RLS on tables |
|--------|---------|------------|---------------|
| `public` | PostgREST default | yes | mixed |
| `storage` | Supabase file storage | yes | yes |
| `graphql_public` | GraphQL endpoint | yes | n/a |
| `solaris_internal` | Solar-Punk staff | NO | yes |
| `solaris_saas` | Solar-Punk tenants | SELECT only | yes |
| `omk_internal` | OMK staff | NO | yes (RLS enabled 2026-06-10, 5 `staff_only_*` policies) |
| `omk_saas` | OMK tenants | SELECT only | yes (7 `*_isolation` policies) |

`PGRST_DB_SCHEMAS = public,storage,graphql_public,solaris_internal,solaris_saas,omk_internal,omk_saas`.

## Work Guidance

### W1 — ALWAYS read `/aspace-supabase-mastery` before any DB op

It encodes the 2 critical gotchas (DOCKER-USER + grants). Reading this leaf alone is not
sufficient.

### W2 — Critical gotcha #1: DOCKER-USER iptables DROP

Symptom: `connection to server at "db" ... port 5432 failed: Operation timed out` while
`supabase-db` is healthy.

Root cause: a hardening rule in chain `DOCKER-USER` that DROPs ports `5432,6543,8000,8001,8443`
for everyone except A0's IP + localhost — which also drops internal container→container traffic.

Fix (surgical, no daemon restart):
```
ssh aspace-vps "sudo iptables -I DOCKER-USER 1 -s 172.16.0.0/12 -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT"
```

**Rule:** any DROP added to DOCKER-USER for a port MUST be preceded by an ACCEPT for
`172.16.0.0/12`, else inter-container traffic dies.

### W3 — Critical gotcha #2: schema USAGE ≠ table access (42501)

`ALTER DEFAULT PRIVILEGES` only applies to **future** tables. If tables already exist,
anon/authenticated get `{"code":"42501","message":"permission denied for table X"}`
(surfaces as HTTP 401 via kong) even with schema USAGE.

Always run BOTH explicit grants AND default privileges. See the leaf skill for the
idempotent bootstrap block.

### W4 — Destructive ops (all HITL)

- `DROP SCHEMA` — HITL. Always confirm no live app uses it (grep Vercel env, grep Dokploy env).
- `DROP TABLE` — HITL. Even with RLS, this is irreversible.
- `DROP POLICY` — HITL. Confirm the policy isn't load-bearing.
- `DISABLE ROW LEVEL SECURITY` — HITL. This exposes all rows to anon.
- `DELETE FROM <table>` — HITL on prod schemas (`*_saas`, `*_internal`).
- Adding a schema to `PGRST_DB_SCHEMAS` — auto-approved (additive, no risk to existing).

### W5 — Multi-tenant query pattern

`*_saas` tables MUST have an `org_id` column. The JWT carries the `org_id` claim via a
custom access token hook. The RLS policy:
```sql
USING (org_id = (auth.jwt() ->> 'org_id')::uuid) WITH CHECK (org_id = (auth.jwt() ->> 'org_id')::uuid);
```

When querying via the MCP, always pass the JWT explicitly:
```ts
await mcp__supabase__execute_sql({
  query: 'SELECT * FROM omk_saas.documents LIMIT 10',
  // + auth header (in MCP, usually via the connected user's session)
});
```

## Verification

```bash
# Confirm DB reachable + schemas exposed:
ssh aspace-vps "cd /srv/aspace/supabase/docker; ANON=\$(grep -E '^ANON_KEY=' .env | cut -d= -f2-)
curl -s -o /dev/null -w 'saas %{http_code}\n' 'http://localhost:8000/rest/v1/organizations' -H \"apikey: \$ANON\" -H 'Accept-Profile: omk_saas'
curl -s -o /dev/null -w 'internal %{http_code}\n' 'http://localhost:8000/rest/v1/agents' -H \"apikey: \$ANON\" -H 'Accept-Profile: omk_internal'
curl -s -o /dev/null -w 'public %{http_code}\n' 'http://localhost:8000/rest/v1/' -H \"apikey: \$ANON\""
# Expect: saas=200 [], internal=401, public=200
```

## Child DOX Index

This leaf has no sub-domains yet. If "RLS policy templates" or "type-gen pipeline" become
a separate concern, split here (e.g. `05a_rls_templates/`).
