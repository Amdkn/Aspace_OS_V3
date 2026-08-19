---
type: Concept
title: Famille INFRA — 8 ADR infrastructure, base de persistance opérationnelle
description: La famille INFRA (8 ADR) définit la base technique : Tmux (WSL dev) + PM2 (VPS prod), repo-home junction law, multi-tenancy Supabase, multi-couche hosting.
tags: [adr, infra, tmux, pm2, wsl, supabase, multi-tenancy]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-INFRA-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-INFRA-001_tmux-wsl-dev-pm2-vps-prod.md"
    title: INFRA 001 — Tmux (WSL) + PM2 (VPS)
    last_modified: "2026-05-26"
  - id: ADR-INFRA-002
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-INFRA-002_repo-home-junction-law.md"
    title: INFRA 002 — Repo-Home Junction Law
    last_modified: "2026-06-15"
  - id: ADR-INFRA-003
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-INFRA-003_business-os-ceo-dashboard-matryoshka.md"
    title: INFRA 003 — Business OS CEO Dashboard Matryoshka
    last_modified: "2026-07-15"
okf_version: "0.2"
---

# Famille INFRA — 8 ADR infrastructure, base de persistance opérationnelle

## Résumé

La famille **INFRA** (8 ADR) pose les fondations de persistance opérationnelle : process managers (Tmux, PM2), hébergement multi-couche, repo-home junction law, multi-tenancy Supabase, observabilité.

## Les 8 ADR

| ADR | Sujet | Statut |
|---|---|---|
| `ADR-INFRA-001` | Tmux (WSL dev) + PM2 (VPS prod) | RATIFIÉ 2026-05-26 |
| `ADR-INFRA-002` | Repo-Home Junction Law | RATIFIED |
| `ADR-INFRA-003` | Business OS CEO Dashboard Matryoshka | RATIFIED |
| `ADR-NET-001` | Hébergement Multi-Couche | RATIFIED |
| `ADR-SUPABASE-001` | Self-hosted multi-tenancy schemas | RATIFIED (superseded partiellement par OMK-004) |
| `ADR-SECNET-001` | Supabase Network Security | RATIFIED |
| `ADR-FS-001` à `FS-003` | Junction-based aliasing (3 ADR) | mixed |
| `ADR-HEART-002` | Heartbeat anti-panique | RATIFIED |

## ADR-INFRA-001 : la doctrine Tmux/PM2

L'ADR-INFRA-001 est le document de référence pour la **base de persistance opérationnelle**. Il pose la séparation stricte :

| Contexte | Plateforme | Process Manager |
|---|---|---|
| Dev local | WSL2 Ubuntu | Tmux |
| Prod | VPS Hostinger Ubuntu 24.04 | PM2 |

**Règle d'or** : aucun service qui doit survivre à une fermeture de terminal ne tourne hors Tmux (dev) ou PM2 (prod).

L'ADR-INFRA-001 amende `Shadow_L0/SPEC.md` §1 : la formule « no daemons » est précisée — interdiction = composants daemon **custom Windows-natif**, autorisation = process managers standards éprouvés Tmux (WSL) + PM2 (VPS Linux).

## ADR-INFRA-002 : Repo-Home Junction Law

Le repo `01-OMK-Business-OS` reste court, conforme à la junction law (le repo est un pointeur, pas un miroir). Cette règle structure l'organisation des sources.

## ADR-SUPABASE-001 : multi-tenancy schemas

Le multi-tenancy Supabase self-hosted (avant pivot) est codifié ici. **Partiellement supersedé** par `ADR-OMK-004` qui impose Supabase Cloud.

## Statut vis-à-vis de V3

- **ADR-INFRA-001** : **canon**. La doctrine Tmux/PM2 reste la référence V3.
- **ADR-INFRA-002** : **canon**.
- **ADR-INFRA-003** : **canon** (cadrage fractal SOA01-SOA08).
- **ADR-SUPABASE-001** : **synthese-datee** (self-host superseded mais multi-tenancy schema toujours valide).
- **ADR-FS-001 à 003** : **canon** (la doctrine junction-based).

## Le verdict de cette distillation

**mixte** : 7 canon + 1 synthese-datee. Aucun orphelin.

## Liens

- Voir aussi : `concept-famille-omk.md` (le pivot OMK → Vercel)
- Voir aussi : `concept-supersedes-partial.md` (le supersedes partiel)