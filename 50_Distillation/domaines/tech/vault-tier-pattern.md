---
type: Concept
title: Vault-tier pattern — secrets en env vars Windows, jamais versionnés
description: Tous les tokens MCP et clés API vivent dans les variables d'environnement Windows User scope, jamais dans le code, les `.md`, `.json` ou `git`. Source unique de vérité.
tags: [tech, securite, vault, secrets, mcp]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: mcp-c1
    resource: 05_From_V2_Domains/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/AGENTS.md
    title: 06_MCP_Mastery § C1 Vault is the only source of truth
    last_modified: 2026-06-10
  - id: secnet
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-SECNET-001_supabase-network-security.md
    title: ADR-SECNET-001 Plan de rotation secrets
    last_modified: 2026-05-28
  - id: kernel-env
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 § 4.2 Fichier .env Kernel
    last_modified: 2026-04-27
okf_version: "0.2"
---

Le pattern **vault-tier** impose que toutes les clés API et tokens MCP vivent dans les variables d'environnement Windows User scope (PowerShell `[Environment]::SetEnvironmentVariable('NAME','value','User')`), **jamais** dans le code versionné.

## Cycle de vie d'une clé

1. **Création** dans l'UI du provider (hpanel.hostinger.com, github.com/settings/tokens, etc.).
2. **Set** dans Windows env vars User scope, sans coller la valeur dans une sortie agent.
3. **Test-key-in-chat pragma** : A0 colle la clé, l'agent la pose dans l'env var.
4. **Smoke test non-destructif** : `gh api user` (GitHub), `GET /v1/user` (Hostinger), etc.
5. **Revoke de l'ancienne clé** côté provider.
6. **Append** d'une ligne `## Rotations` dans `ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md`.

## Triggers de rotation

| Trigger | Action |
|---------|--------|
| Clé apparue en chat / commit / transcript | Rotation immédiate, dans la même session |
| Trimestrielle (90 jours) | Rotation programmée même non-exposée |
| Offboarding employé / device perdu | Rotation immédiate des 5 clés |
| Alerte leak côté provider | Rotation immédiate de la clé impactée |

## Anti-patterns

- `.env` commité dans un repo → `gitignore` obligatoire dès l'init.
- Clé révélée en `print()` de log → masquage `***REDACTED***` + préfixe court.
- Lecture directe d'un `.env` par un A3 → bloquée par hook `PreTool` Nardol.
- `GET ${HOSTINGER_API_TOKEN}` dans un script sans guard `check_env_vars` → K3 (Secret Leak 401) garanti.

## Fichier `.env` côté VPS

Sur le VPS (`/srv/aspace/supabase/docker/.env`, `~/symphony-workers/*/.env`), les `.env` sont aussi vault-tier : **chmod 600**, jamais commit, jamais collés. Le seul dépôt autorisé est vault Word/Cryptomator (Phase 4 de ADR-SECNET-001).

Voir aussi : [[mcp-doctrine-six]], [[symphony-bus-replace-n8n]], [[sovereignty-tier-pyramid]].