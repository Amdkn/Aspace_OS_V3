# 04_vercel — DOX leaf for Vercel MCP

> Parent: `../AGENTS.md`. Framework: `../../06_MCP_Mastery_dox/AGENTS.md`.
> Canon: vault = `VERCEL_TOKEN` (Windows env User).

## Purpose

Vercel is the **frontend deployment plane** for A'Space OS. Every Next.js app — `omk-dashboard`,
`omk-landing`, `abc-os-community`, and any future landing — deploys here. The 3 omk apps
already live in the `amd-lab` team (see C2 below).

## Ownership

- A0 Amadeus — approves prod env-var changes, domain assignments, project deletion.
- A2 Claude Code — orchestrates env-var / domain / deploy operations.
- A3 sub-agent — runs `mcp__vercel__*` calls.

## Local Contracts

### Auth

- Env var: `VERCEL_TOKEN`.
- MCP server: HTTP at `https://mcp.vercel.com` (MCP-server side carries auth).
- Provider: `vercel.com` (account `Amdkn`, team `amd-lab`).

### C2 — Team + Project map (verified 2026-06-10)

| App | Project ID | Team | Domain |
|-----|------------|------|--------|
| `abc-os-community` | `prj_HSw4IBR2omI5qegmEinOksr6xzo0` | `team_d3JjRK4fJUE9ACohbdlhv9Gc` (amd-lab) | tbd |
| `omk-dashboard` | `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` | `team_d3JjRK4fJUE9ACohbdlhv9Gc` | tbd |
| `omk-landing` | `prj_o0ugJWfm19310ioQiMCngcBEOhfB` | `team_d3JjRK4fJUE9ACohbdlhv9Gc` | tbd |

> Domain assignment is the next open ticket — wire `omk.aspace.fr` (or similar) once DNS
> record is set via `01_hostinger/`.

### Env-var scopes

Vercel has 3 env scopes: `development`, `preview`, `production`. The **same** var name can hold
3 different values. For A'Space:
- `VITE_SUPABASE_URL` / `VITE_SUPABASE_ANON_KEY` — must be set in **all 3** scopes for the
  dashboard to work locally, in preview deploys, and in prod.
- `VERCEL_TOKEN` itself — NOT an env var; it's the auth credential.
- Never set `SERVICE_ROLE_KEY` in any Vercel env (use the VPS-side `aspace_admin` role for
  write ops; the dashboard reads with anon + RLS).

## Work Guidance

### W1 — Read `vercel-deploy-from-github` skill first

This skill encodes the GitHub → Vercel auto-deploy setup, the env-var wiring, and the
common gotchas. Do not re-derive.

### W2 — Env-var updates

```ts
// Set the same var across all 3 environments:
await Promise.all([
  mcp__vercel__update_env_variable({ projectId, key, value, target: 'development' }),
  mcp__vercel__update_env_variable({ projectId, key, value, target: 'preview' }),
  mcp__vercel__update_env_variable({ projectId, key, value, target: 'production' }),
]);
```

Always re-verify with `list_env_variables` after a write — Vercel sometimes silently drops
the `target` array on PATCH.

### W3 — Deploy via MCP or via push

Two paths:
- **Git push** (default) — Vercel auto-deploys on push to the connected branch. Confirm the
  GitHub-Vercel connection via `mcp__vercel__get_deployment` and check the `source = git`.
- **MCP direct** — `mcp__vercel__create_deployment` with explicit `gitSource`. Use this for
  hot-fixes or when the GH webhook is broken.

### W4 — Destructive ops

- `delete_project` — HITL gate. Vercel does NOT keep backups of project config (env vars,
  domains, build settings). Screenshot the current config first via `get_project`.
- Domain removal — HITL gate. Affects DNS resolution globally.
- Production env-var changes — HITL gate (development/preview are auto-approved).

## Verification

```bash
# Confirm token + reachability:
mcp__vercel__list_teams
# Expect: 200, includes "amd-lab" (team_d3JjRK4fJUE9ACohbdlhv9Gc)

# Confirm the 3 projects are visible:
mcp__vercel__list_projects
# Expect: abc-os-community, omk-dashboard, omk-landing
```

## Child DOX Index

This leaf has no sub-domains. If a separate contract emerges for "domains + DNS" vs
"builds + env vars", split here.
