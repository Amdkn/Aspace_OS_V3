---
type: Concept
title: AGENTS.md — canon absolu d'identité
description: Manifeste d'identité des agents A'Space OS. Gouverne l'identité ; la Constitution 2026-07-12 gouverne le comportement. Source de vérité pour le registre des Owners, l'organigramme canon, les ADR Fundamentals.
tags: [agents-md, identity, canon, owner, registre, hierarchy]
generated: { by: minimax-m3, at: 2026-08-17T21:08:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:08:00Z }
sources:
  - id: identity-core-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/"
    title: "01_Identity_Core — racine identité A'Space"
    last_modified: 2026-07-12
  - id: constitution
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/CONSTITUTION.md"
    title: "CONSTITUTION A'SPACE — v1.0"
    last_modified: 2026-07-12
  - id: tags-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/TAGS.md"
    title: "TAGS — registre Owner canon arbitré le 2026-08-01"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# AGENTS.md — canon absolu d'identité

> **Statut constitutionnel** : la Constitution 2026-07-12 gouverne le *comportement*.
> AGENTS.md gouverne l'*identité*. L'un ne remplace pas l'autre.

## 1. Localisation canonique

`05_From_V2_Domains/00_Amadeus/01_Identity_Core/AGENTS.md`

Sister files :
- `IDENTITY.md`
- `SOUL.md`
- `TOOLS.md`
- `USER.md`
- `Valeurs.md`
- `a0_l_canon.md`
- `a0_l_geordi_canon.md`
- `HEARTBEAT.md`
- `LEARNING.md` (changelog Constitution)
- `CONSTITUTION.md` (LOI suprême)
- `Manifeste_Souverain.md`
- `AGENTS_REGISTRY.md`

## 2. Doctrine de l'identité

### Registre Owner Star Trek (arbitré 2026-08-01)

| Owner | Domaine PARA | Fondement |
|---|---|---|
| `Computer` | Orchestration | Parent `A2_COMPUTER_ENTERPRISE_PARA` |
| `Picard` | Projects | Spec A3 : « If a Resource becomes execution-critical, route to Picard » |
| `Spock` | Areas | Élimination dans la liste `next_owner` A3 |
| `Geordi` | Resources | Spec A3 : « Geordi is the Resources officer » |
| `Data` | Archives | Spec A3 : « Geordi flags duplicated or stale references for Data review » |
| `Morty` | Focus Gatekeeper | Bus `40_SYMPHONY_BUS/state.json` : `A1:Morty > A2:Computer > A3:Geordi` |

### Registre Shelf Doctor Who (scoped aux guides)

`11thDoctor`, `12thDoctor`, `13thDoctor`, `Yaz`, `Ryan`, `Graham`, `Amy`, `Rory`, `River`, `Clara`
**uniquement** sur les guides de `01_Guides/00_KERNEL_OS/` (héritage historique).
Aucune équivalence automatique avec le registre Owner.

### Ruling A0 — Roster Canon (ADR-CANON-001, 2026-06-02)

Notion `AGENT_REGISTRY_DB` + transcriptions = **source de vérité pour le lore des rosters**.
AGENTS.md = **structure index** (corps immuable + addendum daté ADR-CANON-001).

## 3. Constitution 2026-07-12 — où loge chaque chose

L'arbre `01_Identity_Core/` héberge désormais :

- **`CONSTITUTION.md`** — LOI suprême, articles 1-8, seule rétrogradée par amendement V+
- **`AGENTS.md`** — canon identité (registre Owner, organigramme)
- **`AGENTS_REGISTRY.md`** — registre vivant (mapping Owner ↔ agent runtime)
- **`a0_l_canon.md`** — vie de A0
- **`a0_l_geordi_canon.md`** — rôle A0 dans Geordi
- **`LEARNING.md`** — changelog Constitution et amendements
- **`secrets/`** — zone protégée (non lue par les agents sauf autorisation explicite)
- **`agents/`** — capsules A0/A1/A2/A3 (132 fichiers)
- **`graphify-burst/`** — sortie Graphify

## 4. Ce qu'AGENTS.md n'est pas

- ❌ Pas le contrat de comportement (c'est la Constitution)
- ❌ Pas l'index des ressources (c'est RESOURCES_INDEX dans Geordi)
- ❌ Pas la spécification Geordi (c'est A3_Geordi_Resources_Spec.md)

## Liens entrants

- `constitution-aspace-v1.md` — la loi suprême cohabite avec AGENTS.md
- `rot-strates-s0-s4.md` — AGENTS.md loge en strate S0 (identité)
- `geordi-kb-quatre-piliers.md` — AGENTS.md est un document Dox canon long
