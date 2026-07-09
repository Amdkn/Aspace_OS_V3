---
name: aspace-supabase-mastery
description: >
  Master the A'Space self-hosted Supabase on the Hostinger VPS (aspace-vps / 148.230.92.235):
  multi-tenant schema-per-product + RLS-per-tenant (ADR-SUPABASE-001 / ADR-OMK-001), schema
  bootstrap with CORRECT grants, PostgREST schema exposure (PGRST_DB_SCHEMAS), and the proven
  incident fixes. USE THIS SKILL whenever the user (A0) wants to: create/expose a Supabase schema
  or project, add a tenant table with RLS, debug "PostgREST Database connection timed out" /
  "permission denied for table" (42501) / 401 on a non-public schema, expose a new schema to the
  REST API, wire a dashboard/frontend to the self-hosted Supabase, or operate Supabase on the VPS
  via SSH. Trigger on "supabase schema", "expose schema", "multi-tenant", "RLS", "PGRST_DB_SCHEMAS",
  "postgrest down", "supabase MCP", "omk_internal/omk_saas/solaris_saas", "supabase grants",
  "connection timed out to db", "docker-user", or any self-hosted Supabase ops on aspace-vps.
  Bakes in the DOCKER-USER firewall gotcha and the grants-on-existing-tables gotcha that bit the CLI.
---

# A'Space Supabase Mastery (self-hosted, VPS)

> Canon: `_SPECS/ADR/ADR-SUPABASE-001` (multi-tenancy) + `_SPECS/ADR/ADR-OMK-001` (dual-product).
> Incident ref: `30_MEMORY_CORE/LLM_Wiki/wiki/sources/source_incident_supabase_docker_user_drop_2026_06_08.md`.
> Doctrine: ADR-META-001 (Verify-Before-Assert) — always prove each claim with a command.

## Topology (verified 2026-06-08)
- Host: `aspace-vps` (`148.230.92.235`, srv941028). SSH alias works: `ssh aspace-vps`.
- Runtime: **standalone docker compose** at `/srv/aspace/supabase/docker/` (NOT Dokploy, NOT Swarm).
  Source `/srv/aspace/supabase/`, A'Space layer `/srv/aspace/services/supabase/`.
- Systemd: `supabase-core.service` (oneshot → compose up), `supabase-frontend`, `supabase-apps`, `aspace-supabase-structure`.
- DB: Postgres 15.8 inside container `supabase-db`. PostgREST = `supabase-rest`. Gateway = `supabase-kong` (host :8000 / :8443).
- Network: single bridge `supabase_default`. Dokploy (Swarm) + Hermes are on OTHER networks — restarting supabase does NOT touch them.
- Caddy: routes `supabase-studio.148.230.92.235.sslip.io` (Studio, cookie-gated). The REST API HTTPS domain (`supabase.*.sslip.io`) is NOT configured by default — add a Caddy block → `kong:8000` if public REST needed.
- Secrets live in `/srv/aspace/supabase/docker/.env` (`ANON_KEY`, `SERVICE_ROLE_KEY`, `PGRST_DB_SCHEMAS`). NEVER print SERVICE_ROLE_KEY. Extract anon for tests with `ANON=$(grep -E '^ANON_KEY=' .env | cut -d= -f2-)`.

## Multi-tenancy doctrine (the nuance that matters)
- **Schema = product boundary.** One Postgres schema per product: `omk_internal`, `omk_saas`, `solaris_internal`, `solaris_saas`, ...
- **RLS = tenant boundary.** Inside a `*_saas` schema, tenants (PME clients) are ROWS isolated by `org_id` + RLS, NOT schema-per-client (does not scale). Tables `organizations` + `memberships`; `org_id` carried in the JWT via a custom access token hook.
- `*_internal` = staff data → `anon` must NOT have schema USAGE (revoke it). `*_saas` = client data → `anon` may SELECT but RLS returns `[]` without an org_id claim.

## CRITICAL GOTCHA #1 — "Database connection timed out" is usually iptables, not Docker
PostgREST logs `connection to server at "db" ... port 5432 failed: Operation timed out` while `supabase-db` is healthy.
Root cause seen 2026-06-08: a hardening rule in chain **`DOCKER-USER`** that DROPs ports `5432,6543,8000,8001,8443` for everyone except A0's IP + localhost — which ALSO drops internal container→container traffic.
Diagnostic matrix (run these, don't theorize — D6):
```
ssh aspace-vps "sudo iptables -S DOCKER-USER"          # look for a DROP on 5432/6543/8000...
ssh aspace-vps "docker exec supabase-db pg_isready"    # db itself OK?
# host->db works (OUTPUT chain) but container->container fails (FORWARD/DOCKER-USER) = this bug
```
**Fix (surgical, reversible, no daemon restart):**
```
ssh aspace-vps "sudo iptables -I DOCKER-USER 1 -s 172.16.0.0/12 -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT"
# persist (iptables-persistent is enabled):
ssh aspace-vps "sudo cp /etc/iptables/rules.v4 /etc/iptables/rules.v4.bak.$(date +%Y%m%d) ; \
  sudo sed -i '/-A DOCKER-USER -s 174/i -A DOCKER-USER -s 172.16.0.0/12 -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT' /etc/iptables/rules.v4 ; \
  sudo sh -c 'iptables-restore --test < /etc/iptables/rules.v4' && echo VALID"
```
Rule: any DROP added to DOCKER-USER for a port MUST be preceded by an ACCEPT for `172.16.0.0/12`, else inter-container traffic dies.

## CRITICAL GOTCHA #2 — schema USAGE ≠ table access (42501)
`ALTER DEFAULT PRIVILEGES` only applies to FUTURE tables. If tables already exist, anon/authenticated get
`{"code":"42501","message":"permission denied for table X"}` (surfaces as HTTP 401 via kong) even with schema USAGE.
**Bootstrap a schema correctly (idempotent):**
```sql
CREATE SCHEMA IF NOT EXISTS <schema>;
GRANT USAGE ON SCHEMA <schema> TO authenticated, service_role;   -- anon ONLY for *_saas, never *_internal
-- existing tables:
GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA <schema> TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA <schema> TO service_role;
GRANT USAGE,SELECT ON ALL SEQUENCES IN SCHEMA <schema> TO authenticated, service_role;
-- *_saas only: GRANT SELECT ON ALL TABLES IN SCHEMA <schema> TO anon;  + GRANT USAGE ON SCHEMA <schema> TO anon;
-- future tables:
ALTER DEFAULT PRIVILEGES IN SCHEMA <schema> GRANT SELECT,INSERT,UPDATE,DELETE ON TABLES TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA <schema> GRANT ALL ON TABLES TO service_role;
-- enable RLS + policy per table:
ALTER TABLE <schema>.<t> ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON <schema>.<t>
  USING (org_id = (auth.jwt() ->> 'org_id')::uuid) WITH CHECK (org_id = (auth.jwt() ->> 'org_id')::uuid);
```
Run grants via explicit `psql -c "..."` statements — NOT a heredoc through `ssh "... <<SQL"` (the heredoc gets mangled and silently runs nothing; verify with `has_table_privilege`).

## Expose a schema to the REST API
PostgREST reads `PGRST_DB_SCHEMAS` from `.env` at startup. Adding a schema is additive (won't break `public`).
```
ssh aspace-vps "cd /srv/aspace/supabase/docker && cp .env .env.bak.$(date +%Y%m%d) && \
  sed -i 's/^PGRST_DB_SCHEMAS=.*/PGRST_DB_SCHEMAS=public,storage,graphql_public,<schema1>,<schema2>/' .env && \
  docker compose up -d rest"
ssh aspace-vps "docker logs supabase-rest --tail 4"   # expect 'Successfully connected' + 'Schema cache loaded N Relations'
```
Clients query a non-default schema with header `Accept-Profile: <schema>` (read) / `Content-Profile` (write),
or `createClient(url, anon, { db: { schema: '<schema>' } })` in supabase-js.

## Verify end-to-end (always finish with proof — D5)
```
ssh aspace-vps "cd /srv/aspace/supabase/docker; ANON=\$(grep -E '^ANON_KEY=' .env | cut -d= -f2-)
curl -s -o /dev/null -w 'saas %{http_code}\n' 'http://localhost:8000/rest/v1/organizations' -H \"apikey: \$ANON\" -H 'Accept-Profile: <schema>_saas'   # expect 200 []
curl -s -o /dev/null -w 'internal %{http_code}\n' 'http://localhost:8000/rest/v1/staff_users' -H \"apikey: \$ANON\" -H 'Accept-Profile: <schema>_internal' # expect 401 (anon denied)
curl -s -o /dev/null -w 'public %{http_code}\n' 'http://localhost:8000/rest/v1/' -H \"apikey: \$ANON\"  # expect 200 (non-regression)"
```
200 `[]` on saas = exposed + RLS gating rows (correct). 401 on internal = anon properly excluded. 200 on public = no regression.

## Clean restart (blast radius = supabase only)
```
ssh aspace-vps "cd /srv/aspace/supabase/docker && docker compose down && docker compose up -d"
# then re-apply the DOCKER-USER ACCEPT if it was ever lost, wait 40s, check: docker ps | grep supabase
```

## MCP wiring (per ADR-SUPABASE-001 D2)
- `supabase-solaris` (READ): SSH wrapper `/home/amadeus/symphony-workers/mcp-supabase-launch.sh` (postgres-mcp, analyze/list/explain).
- `supabase-aspace` (WRITE, to build): create_project_schema / apply_migration / execute_sql RW / generate_typescript_types, role `aspace_admin` (NoSuperuser, no access to auth/storage/realtime/vault).

## Guardrails
- Never print SERVICE_ROLE_KEY. Anon key is public (client-side) but still don't paste it into .md/.json/git.
- VPS / prod mutations require the bypass channel (Antigravity extension or CLI `--dangerously-skip-permissions`); Claude Code Desktop's "Ignorer les permissions" works for SSH but not all flows.
- Always back up `.env` / `rules.v4` before edits. Always verify with a real query, never assert success blind.
