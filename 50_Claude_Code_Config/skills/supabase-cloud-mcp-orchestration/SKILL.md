---
name: supabase-cloud-mcp-orchestration
description: Orchestrate Supabase Cloud (supabase.com) operations via the official `@supabase/mcp-server-supabase` MCP (v0.8.2+). Use this skill when the user says "create a Supabase project", "list my projects", "run a migration on cloud", "check project health", "rotate anon key", or any Supabase Cloud API operation. TRIGGERS on "supabase cloud", "supabase.com", "cloud project", "PAT supabase", "mcp supabase", "list orgs", "list projects". Auth = `SUPABASE_ACCESS_TOKEN` (Personal Access Token from https://supabase.com/dashboard/account/tokens), set via Test Key Pragma. The Cloud MCP is **different** from `aspace-supabase-mastery` (which is for the self-hosted VPS Supabase — schema/RLS/grants on aspace-vps). Cloud MCP exposes project management + PostgREST; self-hosted uses psql/SSH/grants.
---

# /supabase-cloud-mcp-orchestration — Supabase Cloud via official MCP

## Why Cloud MCP not self-hosted for new work
- Architecture pivot (2026-06-16, see `handoff_business_os_resumption_2026-06-16.md`): **new projects** = Supabase Cloud. Self-hosted Supabase on aspace-vps is in **sunset mode** (kept alive for `solaris_saas`, `omk_saas`, `abc_os` until cutover).
- The official MCP supports Cloud only. It uses the Management API + PostgREST API.
- For self-hosted Supabase operations (grants, RLS, schema bootstrap, DOCKER-USER iptables fix), use `aspace-supabase-mastery` instead — different tools, different doctrine.

## MCP wiring (verified 2026-06-16)
- Server: `@supabase/mcp-server-supabase@0.8.2` (npm, Apache-2.0, official Supabase team)
- Wired in `.mcp.json` as `"supabase"` (replaces the legacy `supabase-aspace` + `supabase-solaris`, archived 2026-06-16 → `_TRASH_2026-06-16_mcp_supabase_legacy/`)
- Auth: `SUPABASE_ACCESS_TOKEN` env var User scope (rotate per Test Key Pragma)
- Transport: stdio via `npx -y @supabase/mcp-server-supabase@latest`

## Preconditions (verify first)

| Check | Command | Pass criterion |
|---|---|---|
| MCP server alive | `claude mcp list` (in a Claude Code session) | `supabase: ... - ✓ connected` |
| Token valid | Call `mcp__supabase__list_organizations` | returns ≥ 1 org (A0's `amd-lab` Personal) |
| Right org context | Inspect returned orgs list | `personal` org = amdkn7's solo projects; `team` org = amd-lab |

> If `list_organizations` returns 401, the token is wrong/expired. Rotate via Test Key Pragma.

## Tool catalogue (the 20+ tools exposed)

### Project management
- `list_organizations` — all orgs the token can see
- `list_projects` — projects in a given org (filter by region, status)
- `get_project` — single project details (id, name, region, status, db_version, plan)
- `create_project` — bootstrap a new project (pick region, plan, db_pass, name)
- `pause_project` / `restore_project` — toggle project state (free tier only)
- `delete_project` — DESTRUCTIVE, requires HITL double-convocation (mirrors `supabase-aspace` execute_sql)
- `get_project_url` / `get_anon_key` / `get_service_key` — secrets (service_key requires HITL)

### Database (PostgREST-bound queries via Management API)
- `list_tables` — tables in a schema (default `public`)
- `execute_sql` — read-only SQL via the project's PostgREST endpoint (use the project's pooler, NOT direct)
- `apply_migration` — apply a `.sql` migration file to the project (idempotent, versioned)
- `list_migrations` — read migration history
- `generate_typescript_types` — produce TS types matching the current schema

### Branching (preview environments)
- `create_branch` — git-style branch of a project (separate DB, separate URLs)
- `list_branches` / `delete_branch` / `merge_branch` / `reset_branch` / `rebase_branch` — branch ops
- `list_branch_diffs` — schema diff between branches

### Observability
- `get_advisors` — security + performance linter (run after migrations)
- `get_logs` — recent logs (filter by service: api/db/auth/storage/realtime)
- `get_project_stats` — project health (CPU, RAM, connections)

### Auth (limited)
- `list_auth_users` / `get_auth_user` / `update_auth_user` / `delete_auth_user`
- `list_auth_admin` — admin-level ops (HITL required)

## Common workflows

### Bootstrap a new SaaS project

1. `list_organizations` → pick `personal` or `team`
2. `create_project({ name: "<project-name>", region: "eu-west-1", plan: "free", db_pass: "<random>" })` → returns `projectRef`
3. `get_project_url({ projectRef })` → returns `https://<ref>.supabase.co`
4. `get_anon_key({ projectRef })` → save to `.env.local` (NEXT_PUBLIC_SUPABASE_URL / NEXT_PUBLIC_SUPABASE_ANON_KEY)
5. Apply migrations: `apply_migration({ projectRef, name: "001_init", sql: "<contents of migrations/001_init.sql>" })`
6. Wire frontend: standard `createClient(url, anon, { db: { schema: 'public' } })` in supabase-js

### Verify a project is healthy

```
1. get_project_stats({ projectRef })  # expect CPU < 60%, RAM < 70%
2. get_advisors({ projectRef, type: "security" })  # expect 0 critical
3. get_logs({ projectRef, service: "db" })  # tail last 50, scan for FATAL
4. list_migrations({ projectRef })  # all should be `applied`
```

### Run a one-off SQL query (read-only)

```
execute_sql({ projectRef, sql: "SELECT count(*) FROM users" })
# → returns rows array, NEVER the connection string or DDL
```

## Gotchas (D6 paid for)

| Symptom | Root cause | Fix |
|---|---|---|
| `create_project` returns 402 Payment Required | Free-tier project count > 2 in this org | Pause an old project, or upgrade org to Pro plan |
| `get_service_key` returns 403 | Token scope is `anon` not `service_role` | Regenerate PAT with `service_role` scope (HITL — A0) |
| `execute_sql` returns "permission denied for table X" | RLS is on but no policy, OR JWT has no `org_id` claim | Add a permissive policy OR ensure the JWT context is correct (use a real anon key for client queries) |
| `apply_migration` fails halfway | Migration is NOT atomic in a single transaction | Wrap in `BEGIN; ... COMMIT;` and use `IF NOT EXISTS` everywhere; check `list_migrations` to see what landed |
| `list_branches` shows orphan branches | Branch was never merged; costs $0.013/branch/day after 7 days | Delete with `delete_branch` or merge with `merge_branch` |

## Auth & token rotation

- `SUPABASE_ACCESS_TOKEN` = Personal Access Token (PAT) from https://supabase.com/dashboard/account/tokens
- PAT scopes: `all` (full org), or granular (per-project read/write)
- To rotate: A0 generates new PAT → pastes in chat → agent sets env var User scope → A0 revokes old
- **NEVER** inline the PAT in `.mcp.json` (notion-style) — use env var (Test Key Pragma doctrine)

## What this skill does NOT do

- ❌ Direct psql to Cloud (use `execute_sql` MCP tool, or `supabase db connect` CLI with the project's pooler URL)
- ❌ Self-hosted Supabase ops (use `aspace-supabase-mastery` instead)
- ❌ Manage Supabase Edge Functions (use `supabase functions deploy` CLI)
- ❌ Manage Storage buckets via raw SQL (use the dashboard or `supabase storage` CLI)
- ❌ Multi-region replication (Cloud plan-dependent, ask A0)

## Related

- Skill `aspace-supabase-mastery` — self-hosted Supabase on aspace-vps (legacy/sunset)
- ADR-SUPABASE-001 — multi-tenancy doctrine (schema = product, RLS = tenant)
- `_SPECS/ADR/ADR-SUPABASE-001_*` — canonical contracts
- `wiki/hand_offs/handoff_business_os_resumption_2026-06-16.md` — architecture pivot context
