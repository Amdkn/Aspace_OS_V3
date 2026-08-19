---
type: Concept
title: Capabilities A3 — Yaz / Ryan / Graham (13ème), Bill / Clara / Nardol (12ème), Amy / Rory / River (11ème)
description: Neuf agents compagnons Tech OS distribués en 3 triades. Chaque triade a une mission noyau, un MCP principal, et un ensemble d'outils interdits.
tags: [tech, agents, capabilities, division]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: d13-roles
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 § 5-7 Yaz / Ryan / Graham
    last_modified: 2026-04-27
  - id: d12-roles
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-003_tardis-protocol-orchestration.md
    title: SDD-003 § 3 Bill / Clara / Nardol
    last_modified: 2026-04-25
  - id: d11-roles
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-004_ricks-verse-governance.md
    title: SDD-004 § 8 Amy / Rory / River
    last_modified: 2026-04-26
okf_version: "0.2"
---

Neuf agents A3 distribués en **trois triades** sous leurs Doctors respectifs.

## Triade 13ème Doctor — Kernel Core (L0.3)

| Compagnon | Mission | MCP principal | Outils interdits |
|-----------|---------|---------------|------------------|
| **Yaz** (Yasmin Khan) | Surveillance, monitoring VPS, DNS, firewall | Hostinger MCP (`vps_*`, `DNS_*`) | Curl direct API ; déploiement (domaine Ryan) |
| **Ryan** (Ryan Sinclair) | Déploiement Dokploy, rollbacks canary, idempotence | Dokploy MCP (`deploy_*`, `rollback_*`) | Docker CLI brut ; modification VPS sans snapshot Yaz préalable |
| **Graham** (O'Brien) | Mémoire RAG (pgvector `kernel_memory`), WIKI append-only, snapshots | Supabase MCP (`execute_sql`, `apply_migration`) | Lecture de fichiers `.env` ; suppression logs sans archivage |

## Triade 12ème Doctor — Forge Core (L0.2)

| Compagnon | Mission | Framework |
|-----------|---------|-----------|
| **Bill** (Bill Potts) | BMAD Architect (Phase 1-5) — recherche SDK/MCP, BLUEPRINT.bmad.md | `npx bmad-method install` |
| **Clara** (Clara Oswald) | CLI Forge — Python Click dual-mode (REPL + `--json`) via 7 phases CLI-Anything | YAML schema par commande |
| **Nardol** (Nardole) | Quality Gate — AgentShield ECC (102 règles), `nardol-validate.sh`, SKILL.md frontmatter | `shell=True`, `eval()`, secrets en clair |

## Triade 11ème Doctor — Life Core (L0.1)

| Compagnon | Mission | Stack |
|-----------|---------|-------|
| **Amy** (Pond) | AG-UI / A2UI — composants React 19, Tailwind 4, design system Solarpunk | Phaser 3, WorkAdventure |
| **Rory** (Williams) | Persistance Supabase + RLS + migrations SQL + IndexedDB fallback | Supabase MCP, `run_adr003_migration()` |
| **River** (Song) | Workflows agentiques, OpenClaw + Hermes agents, App Store iFrames (Amy) | Multica, OpenClaw |

## Règle de délégation

Rick (A1) ne parle jamais **directement** à un A3. Il passe par le Doctor du domaine :
- Kernel / Infra → 13ème Doctor → Yaz / Ryan / Graham
- Forge / MCP / Skill → 12ème Doctor → Bill / Clara / Nardol
- Interface / UX / Workflow → 11ème Doctor → Amy / Rory / River

Tout contact A1 ↔ A3 direct est une **violation** (cf. SDD-003 §2, SDD-004 §7).

## Mission critique par défaut

Chacun a une mission critique + une mission restreinte (ce qu'il ne fait PAS). Yaz surveille mais ne déploie pas. Ryan déploie mais ne touche pas au VPS. Bill blueprinte mais ne code pas. Clara code en Python Click, jamais en bash. Nardol valide sans coder. Amy ne touche pas aux routes backend, Rory ne touche pas à l'UI, River n'invente pas de workflows tactiques — il orchestre les existants.

Voir aussi : [[caste-doctor-who]], [[tardis-inverse]], [[axiomes-antifragilite-k1-k4]].