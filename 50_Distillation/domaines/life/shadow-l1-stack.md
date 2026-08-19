---
type: Concept
title: Shadow L1 Stack — mapping framework → outil distant
description: Mapping canonique des 6 frameworks Life OS vers leurs outils Shadow L1 (Baserow, Obsidian, Plane, Affine). Plane.so pour GTD, Baserow pour 12WY+ZORA, Affine Edgeless pour DEAL.
tags: [shadow-l1, baserow, obsidian, plane, affine, stack, shadow-tools]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: gatekeepers-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/README.md
    title: 00_Gatekeepers_Beth_Morty README — Shadow L1 Tool Map
    last_modified: 2026-05-20
  - id: life-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/README.md
    title: 20_Life_OS README — Shadow L1 Tool Map
    last_modified: 2026-05-20
  - id: orville-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/21_Ikigai_Orville/A2_Orville_Spec.md
    title: A2 Orville Spec — Shadow tool Obsidian/filesystem notes
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Shadow L1 Stack — mapping framework → outil distant

Le **Shadow L1 Stack** est la table canonique qui mappe chaque framework Life OS vers son outil distant. Les A2 ships ne **poss**edent** pas l'état canonique : ils le **consomment** via leur outil Shadow L1.

## Table canonique

| Framework | A2 / Ship | Shadow tool |
|---|---|---|
| Ikigai | USS Orville | Obsidian / notes |
| Life Wheel / ZORA | USS Discovery | Baserow `LD00 ZORA` |
| 12WY | USS SNW / Curie | Baserow `12WY Warp Core`, Scorecard, Time Use |
| PARA | USS Enterprise / Picard | Obsidian |
| GTD | USS Cerritos | Plane.so |
| DEAL | USS Protostar / Holo Janeway | Affine Edgeless |

## Lecture par A1

Beth lit en parallèle 7 surfaces :

| Surface | Path / tool | Pourquoi Beth la lit |
|---|---|---|
| Canon SDD | `10_Tech_OS/12_Blueprints/01-SDD/SDD-005_life-os-l1-integration.md` | Architecture cible Life OS |
| Shadow L1 SDD | `10_Tech_OS/12_Blueprints/01-SDD/SDD-008_shadow-L1-life-os.md` | Baserow / Plane / Obsidian / Affine lab |
| Meta scope | `10_Tech_OS/12_Blueprints/01-SDD/SDD-010_meta-cloture-scope-13eme-semaine.md` | 13th week, 50/30/20, Beth Veto |
| LLM Wiki | `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/` | Mémoire durable et preuves |
| Baserow | `LD00 ZORA`, `12WY Warp Core`, Scorecard, Time Use | ZORA, 12WY, charge domaine |
| Obsidian | `20_Life_OS/24_PARA_Enterprise/` | PARA source of truth |
| Plane | GTD workspace / Life OS project | Capture et daily work-items |
| Affine | DEAL workspace | Blueprints libération et automation |

## Context7 Boundary par outil

Pour chaque outil Shadow L1, Baserow / Plane / Affine **API, schema, rollup, MCP, Symphony adapter, CLI** = `NEEDS_CONTEXT7` avant mutation. Les lectures locales, diagnoses statiques, ou écriture de handoff ne nécessitent pas Context7.

| Outil | Context7 requis pour |
|---|---|
| Baserow | API, schema, rollup, MCP, Symphony adapter, CLI |
| Obsidian | Junction filesystem, plugin sync (peu fréquent) |
| Plane | API, project schema, MCP, webhook, provider config |
| Affine | API, Edgeless, MCP, plugin, provider config |

## Règle de propriété canonique

> *"No A1 action is valid unless it can answer: 1. Which domain or framework is affected? 2. Which A2 ship owns the decision? 3. Which A3 crew member owns the next action? 4. Which evidence path proves the request? 5. Did Beth clear the execution?"*
> — `00_Gatekeepers_Beth_Morty/README.md`

## Anti-patterns détectés

- **Créer un état parallel quand l'outil Shadow L1 le possède déjà** → Morty blocks.
- **Traiter LLM Wiki comme action tracker** → LLM Wiki = mémoire durable, pas live task state.
- **Mutation directe sans dry-run** → Morty bloque.

## Couplage Symphony Bus

`00_Amadeus/05_OSS_Twin/symphony/` = adaptateur cross-tool canon. Chaque mutation outillée passe par Symphony quand un adaptateur existe. Pattern machine à états sémantique (state.json), **pas d'UI visuelle n8n**.