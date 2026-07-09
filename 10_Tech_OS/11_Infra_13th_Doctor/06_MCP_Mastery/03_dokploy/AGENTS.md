# 03_dokploy — DOX leaf for Dokploy MCP

> Parent: `../AGENTS.md`. Framework: `../../06_MCP_Mastery_dox/AGENTS.md`.
> Canon: vault = `DOKPLOY_API_KEY` (Windows env User).
> ⚠️ The previous key was exposed in `mcp-servers.json` + Antigravity transcript — **rotate next session** (per root C3).

## Purpose

Dokploy is the **VPS deployment plane for back-end services** (Solarpunk Kernel's heavy containers:
Visions/Notion bridges, Symphonies, BullMQ workers). Front-ends go to Vercel (see `04_vercel/`).
This contract governs app create / build / deploy / scale on the Dokploy instance at
`dokploy.148.230.92.235.sslip.io`.

## Ownership

- A0 Amadeus — approves prod deployments, env-var changes, app deletion.
- A2 Claude Code — orchestrates build + deploy cycles.
- A3 sub-agent — runs `mcp__dokploy__*` calls.

## Local Contracts

### Auth

- Env var: `DOKPLOY_API_KEY`.
- MCP server: `npx -y @ahdev/dokploy-mcp` (HTTP via `https://dokploy.148.230.92.235.sslip.io`).
- Provider: Dokploy self-hosted on `aspace-vps`, behind Caddy + ssrip.io TLS.

### Capabilities (verified live 2026-06-10)

| Tool | Status |
|------|--------|
| `mcp__dokploy__list_projects` | ✅ 200 |
| `mcp__dokploy__create_application` | ✅ |
| `mcp__dokploy__deploy_application` | ✅ |
| `mcp__dokploy__list_deployments` | ✅ |
| `mcp__dokploy__update_application_env` | ✅ |
| `mcp__dokploy__delete_application` | HITL |

### App naming

`<role>-<proj>-<purpose>` kebab-case. Example: `symphony-omk-worker`, `vision-notion-bridge`.
Avoid generic names like `app1` — they collide on Traefik routing.

### Build vs Runtime env

Dokploy has **two** env-var sets that look identical and are not:
- **Build env** — available during `docker build` (npm install with private tokens, etc.).
- **Runtime env** — available in the running container.

Most production env vars go to **runtime**. Only put in build env what the Dockerfile literally needs.

## Work Guidance

### W1 — Read `picard-audit-and-prod-workflow` Phase 6 before any deploy

Phase 6 has the Hybrid Vercel ⇆ Dokploy recipe. Use it; do not re-derive the steps.

### W2 — Healthcheck before declaring success

After `deploy_application`, poll `list_deployments` for the new deployment_id until status = `running`
AND the app's healthcheck URL returns 200. Time-box at 5 min. If still pending, read the build logs
(via the MCP) — never assume success.

### W3 — Traefik labels

Dokploy auto-generates Traefik labels. If you need a custom domain (`*.aspace.fr` instead of
`*.sslip.io`), set the `domains` field at app creation — do not edit the compose file
after the fact, the labels get regenerated.

### W4 — Resource limits

The VPS has 16 GB RAM. Before deploying a new app, sum the existing `mem_limit` on Dokploy's
container list. If adding the new app pushes > 12 GB, propose a resource trim on another
container first.

### W5 — Rolling back

Dokploy keeps the last 3 container images. To roll back: redeploy the previous image SHA via
`deploy_application` with `image_id = <previous>`. NEVER delete a failing deploy and re-deploy
without checking why it failed.

## Verification

```bash
# Confirm Dokploy reachable + authed:
curl -s -o /dev/null -w "%{http_code}\n" https://dokploy.148.230.92.235.sslip.io/api/project.all \
  -H "Authorization: Bearer $DOKPLOY_API_KEY"
# Expect: 200
```

## Child DOX Index

This leaf has no sub-domains. If Traefik routing, Caddy upstream, or app-specific deploy
recipes become a separate concern, split here (e.g. `03a_traefik_routing/`).
