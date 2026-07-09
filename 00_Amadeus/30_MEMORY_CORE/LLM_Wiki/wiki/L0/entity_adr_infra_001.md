---
name: adr-infra-001
type: ADR
namespace: INFRA
status: RATIFIED
date: 2026-05-26
level: L0
canon_path: 10_Tech_OS/12_Blueprints/02-ADR/ADR-INFRA-001_tmux-wsl-dev-pm2-vps-prod.md
amends:
  - shadow_l0_spec_md
anchors:
  - sdd-001
links:
  - entity_adr_heart_002
  - entity_adr_symph_001
  - entity_openharness
  - entity_rick
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-INFRA-001 — Tmux (WSL Dev) + PM2 (VPS Prod)

Premier ADR du namespace `INFRA`. Insight A0 post-paniques agentiques : utiliser les **process managers standards éprouvés** plutôt que des daemons custom.

## En 1 phrase
**Tmux** (Unix std, 2007) pour développement persistant dans WSL · **PM2** (Node std, 2013) pour production durable sur VPS. Aucun service important ne tourne hors de ces deux runners.

## Décisions clés (7)
1. Séparation stricte dev (Tmux/WSL) vs prod (PM2/VPS)
2. Layout Tmux canonique "aspace" (4 windows)
3. Template `ecosystem.config.js` PM2 par projet
4. 5/8 paniques SDD-001 mitigées structurellement
5. Allocation : Yaz reste Task Scheduler, services lourds sous PM2, expérimentation sous Tmux
6. Migration choisie : coexistence (pas de bascule brutale)
7. Amende SPEC.md : "no **custom** daemons" (Tmux/PM2 autorisés)

## Anti-pattern résolu
Hermes/OpenClaw/Paperclip = code custom 2 ans, fragile → effondrement. Tmux/PM2 = standards industriels battle-tested 10-20 ans, jamais de panique structurelle équivalente.

## Backlinks
- [[entity_adr_heart_002]] — couche tick anti-panique complémentaire (mode lean)
- [[entity_adr_symph_001]] — bus orchestration compatible (PM2 runner pour services Symphony lourds)
- [[entity_openharness]] — Rick A1 — peut désormais tourner sous Tmux/PM2 selon contexte

