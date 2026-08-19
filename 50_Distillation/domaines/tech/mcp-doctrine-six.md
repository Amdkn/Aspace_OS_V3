---
type: Concept
title: Doctrine MCP — six serveurs canoniques production
description: Six MCP de production reconnus par DOX : hostinger, github, dokploy, vercel, supabase, graphify. Chacun a son AGENTS.md feuille ; ses outils ont un owner A0/A2/A3 explicite.
tags: [tech, mcp, dox, integrations, vault]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: mcp-root
    resource: 05_From_V2_Domains/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/AGENTS.md
    title: 06_MCP_Mastery — DOX root
    last_modified: 2026-06-10
  - id: dox-framework
    resource: 05_From_V2_Domains/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery_dox/AGENTS.md
    title: DOX framework
    last_modified: 2026-01-01
  - id: vault
    resource: 05_From_V2_Domains/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/01_hostinger/AGENTS.md
    title: 01_hostinger — DOX leaf
    last_modified: 2026-06-10
okf_version: "0.2"
---

La DOX (AGENTS.md hiérarchique) reconnaît **six MCP de production** comme le contrat de travail liant l'agentique au système :

| # | MCP | Rôle | Vault (env var User Windows) |
|---|-----|------|------------------------------|
| 1 | hostinger | DNS, domaines, VPS list | `HOSTINGER_API_TOKEN` |
| 2 | github | repos, PRs, issues, webhooks, releases | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| 3 | dokploy | VPS deployments (back/services) | `DOKPLOY_API_KEY` |
| 4 | vercel | Frontend deployments, env vars, domains | `VERCEL_TOKEN` |
| 5 | supabase | DB schemas, RLS, PostgREST, types | SSH `aspace-vps` (pas de token) |
| 6 | graphify | Knowledge graph du repo | réutilise `ANTHROPIC_API_KEY` + base MiniMax |

## Trois contrats durs

1. **C1 — Vault = seule source de vérité.** Toutes les clés vivent dans Windows env vars User scope. Jamais dans `.md`, `.json`, `git`, MCP server args, ou chat après rotation.
2. **C2 — Rotation policy.** Trigger = clé exposée en chat / commit / transcript ; trigger trimestriel programmé ; trigger immédiat si employé offboardé ou device perdu. Sur chaque rotation, append d'une ligne `## Rotations` dans l'ADR-INFRA-MCP-001.
3. **W3 — Destructive ops = HITL gate.** DELETE (domaine, repo, schema, deployment, database), DROP (table, schema, policy, RLS), `DISABLE ROW LEVEL SECURITY`, DELETE FROM prod, ajout DNS prod → tous HITL.

## Hiérarchie DOX obligatoire

Avant tout appel MCP, l'agent **doit** lire :
1. `06_MCP_Mastery/AGENTS.md` (root)
2. AGENTS.md feuille de l'enfant ciblé (hostinger / github / dokploy / vercel / supabase)
3. Skill leaf (`/aspace-supabase-mastery`, etc.) si existe

Sans cette chaîne dans le contexte, l'appel MCP est non-conforme.

## Smoke tests de validation

5 tests parallèles à passer en `< 5 s` :
- `hostinger` → `listDomains()` ≥ 1 domaine
- `github` → `gh api user` = `Amdkn`
- `dokploy` → `list_projects` ≥ 1
- `vercel` → `list_teams` inclut `team_d3JjRK4fJUE9ACohbdlhv9Gc` (amd-lab)
- `supabase` → `list_objects --schema_name public` ≥ 0

Voir aussi : [[vault-tier-pattern]], [[paniques-k1-k4-kernel]], [[symphony-bus-replace-n8n]].