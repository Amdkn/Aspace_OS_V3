# 06_MCP_Mastery — DOX root for the 5 production MCPs

> DOX doctrine: walk the tree from this root to the leaf before any MCP op.
> After any meaningful change, update the nearest owning `AGENTS.md` AND this index.
> Reference framework cloned at `06_MCP_Mastery_dox/AGENTS.md` (dox v1, Agent Zero).

## Purpose

This subtree is the **binding work contract** for agentic mastery of the five MCPs that drive
A'Space OS V2 production:

| # | MCP | Role | Vault location (Windows env User) |
|---|-----|------|-----------------------------------|
| 1 | hostinger | DNS, domain, VPS list | `HOSTINGER_API_TOKEN` (rotate, was exposed) |
| 2 | github | repos, PRs, issues, webhooks, releases | `GITHUB_PERSONAL_ACCESS_TOKEN` (rotate, scope = `repo, read:org, admin:repo_hook`) |
| 3 | dokploy | VPS deployments (back/services) | `DOKPLOY_API_KEY` (rotate, was exposed) |
| 4 | vercel | Frontend deployments, env vars, domains | `VERCEL_TOKEN` (clean) |
| 5 | supabase | DB schemas, RLS, PostgREST, types | `SUPABASE_ACCESS_TOKEN` (self-hosted, no token; SSH launch script) |
| 6 | graphify | Knowledge graph of the repo (code + ADRs + wikis) | reuses `ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic` (MiniMax-M3) |

These five are the only production-critical MCPs. Other MCPs in `~/.claude/mcp-configs/mcp-servers.json`
(jira, firecrawl, omega-memory, railway, cloudflare-*, exa, etc.) are utility/exploration — out of
scope for this contract.

## Ownership

| Role | Agent | Responsibility |
|------|-------|----------------|
| Sovereign (A0) | Amadeus | Sets intent, approves rotation, signs ADRs |
| Orchestrator (A2) | Claude Code | Walks this tree, dispatches to A3, updates dox after changes |
| Executor (A3) | Sub-agents | Run the leaf MCP tool calls; report back with proof |
| Skill | `/mcp-mastery` | Thin wrapper that **forces** the dox walk before any MCP op |

## Local Contracts

### C1 — Vault is the only source of truth

All API keys/tokens live in **Windows environment variables, User scope**. Never in `.md`, `.json`,
`git`, MCP server args, or in chat after a rotation.

- Read at runtime: `Get-ChildItem Env: | Where-Object { $_.Name -in @('DOKPLOY_API_KEY','HOSTINGER_API_TOKEN','GITHUB_PERSONAL_ACCESS_TOKEN','VERCEL_TOKEN') }`
- Set/rotate: `[Environment]::SetEnvironmentVariable('NAME','value','User')` then restart Claude Code.
- `.env` files (e.g. on the VPS at `/srv/aspace/supabase/docker/.env`) are also vault-tier — never paste contents.

### C2 — Rotation policy

| Trigger | Action |
|---------|--------|
| Key appeared in chat / commit / transcript | Rotate within the same session, then re-set env var |
| Quarterly (every 90 days) | Scheduled rotation, even if not exposed |
| Employee offboarding / device lost | Immediate rotation of all 5 |
| Provider-side leak alert | Immediate rotation of the affected key |

Rotation protocol (A0-driven, agent-assisted):
1. Generate new key in provider UI/API.
2. Test-key-in-chat pragma (A'Space OS V2 doctrine): paste the new key here, agent sets it.
3. Agent runs a non-destructive smoke test (e.g. `GET /v1/user` for Hostinger, `gh api user` for GitHub).
4. On green, revoke the old key in the provider.
5. Update `last_rotated` in this file's C3 table.
6. Append a `## Rotations` line to `_SPECS/ADR/ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md`.

### C3 — Current vault state (verified live)

| MCP | Env var | Source provider | Last verified | Status |
|-----|---------|-----------------|---------------|--------|
| hostinger | `HOSTINGER_API_TOKEN` | hpanel.hostinger.com | 2026-06-10 | ⚠️ was exposed in `mcp-servers.json:187` — rotate next session |
| github | `GITHUB_PERSONAL_ACCESS_TOKEN` | github.com/settings/tokens | 2026-06-10 | ✅ clean |
| dokploy | `DOKPLOY_API_KEY` | dokploy panel | 2026-06-10 | ⚠️ was exposed in `mcp-servers.json:179` and Antigravity transcript — rotate next session |
| vercel | `VERCEL_TOKEN` | vercel.com/account/tokens | 2026-06-10 | ✅ clean |
| supabase | n/a (self-hosted) | ssh `aspace-vps` + `/home/amadeus/symphony-workers/mcp-supabase-launch.sh` | 2026-06-10 | ✅ tunnel stable, IP `172.19.0.3` (was `172.19.0.2`, fixed dynamically) |
| graphify | n/a (reuses `ANTHROPIC_API_KEY`) | `graphify` CLI (PyPI `graphifyy`) + MCP server | 2026-06-10 | ✅ installed via `uv tool install`, MiniMax-M3 endpoint live |

## Work Guidance

### W1 — Before any MCP op, walk the tree

1. Read this root `AGENTS.md`.
2. Identify which of the 5 children owns the target (hostinger/github/dokploy/vercel/supabase).
3. Read that child's `AGENTS.md` end-to-end.
4. Read the leaf skill if one exists (`/aspace-supabase-mastery`, `/vercel-deploy-from-github`, etc.).
5. **Then** call the MCP tool. Never before.

### W2 — Before any edit, check for a relevant leaf skill first

| Intent | Read first |
|--------|-----------|
| Add/change DNS record | `01_hostinger/AGENTS.md` |
| Create repo / open PR / add webhook | `02_github/AGENTS.md` |
| Deploy app to VPS / scale service | `03_dokploy/AGENTS.md` |
| Deploy frontend / set env / add domain | `04_vercel/AGENTS.md` |
| Create schema / RLS / PostgREST / types | `05_supabase/AGENTS.md` + `/aspace-supabase-mastery` |

### W3 — Destructive ops require HITL gate

The following ALWAYS require Amadeus's explicit go-ahead, even in "auto-pilot" mode:
- `DELETE` of a domain, repo, project, schema, deployment, or database.
- Any `DROP` (table, schema, policy, RLS).
- Production env-var changes (Vercel prod env, Dokploy prod env).
- Rotation of any of the 5 vault keys.
- Webhook or DNS record changes that affect production traffic.

Non-destructive reads, drafts, dev/preview envs, dry-runs — auto-approved when the leaf `AGENTS.md`
is in context.

### W4 — After any meaningful change, update the dox chain

- Local contract / endpoint change → update the child `AGENTS.md` and the relevant C-row here.
- New destructive op discovered → append to the child's Work Guidance.
- Vault state change (rotation) → update C3 + append to ADR-INFRA-MCP-001 `## Rotations`.
- New leaf skill created → add to W2 table here.

## Verification

Live smoke tests (run all 5 in parallel to confirm "autonomous" status):

| MCP | Smoke test | Expected |
|-----|------------|----------|
| hostinger | `hostinger-mcp` → listDomains() | 200, ≥ 1 domain (aspace.fr, etc.) |
| github | `gh api user` (uses env PAT) | 200, login = `Amdkn` (or current) |
| dokploy | `mcp__dokploy__list_projects` | 200, ≥ 1 project |
| vercel | `mcp__vercel__list_teams` | 200, includes `team_d3JjRK4fJUE9ACohbdlhv9Gc` (amd-lab) |
| supabase | `mcp__supabase__list_objects --schema_name public` | 200, ≥ 0 objects |

If any smoke test fails: STOP, do not retry blindly. Re-read the child's `AGENTS.md` Work Guidance.
Per ADR-META-001 D6 — "Persistent symptom → exact command": record the failing command + exact
error in the leaf doc before guessing a fix.

## Child DOX Index

| # | Folder | Owns | Critical gotchas |
|---|--------|------|------------------|
| 1 | `01_hostinger/` | DNS, domains, VPS | Token exposure path; rate limit 5 req/s |
| 2 | `02_github/` | repos, PRs, webhooks, releases | PAT scopes; webhook signing secret |
| 3 | `03_dokploy/` | apps, deployments, Traefik | App name uniqueness; build context; env vs runtime env |
| 4 | `04_vercel/` | projects, env vars, domains | `amd-lab` team_id; project_id mapping; env-var scope (dev/preview/prod) |
| 5 | `05_supabase/` | schemas, RLS, PostgREST, types | DOCKER-USER iptables DROP; ALTER DEFAULT PRIVILEGES vs explicit GRANT; dynamic DB IP |
| 6 | `06_graphify/` | knowledge graph of the repo (cross-cutting) | Python 3.13 cap for Leiden; LLM backend config; `graphify-out/` is gitignored; first build on ASpace_OS_V2 = 5–15 min for ~13k canon files |

When any child grows sub-domains, add a `Child DOX Index` to that child and reference it from
here.
