---
type: Backend
title: Second Brain PARA — 14 sous-dossiers de Geordi
description: Cartographie mesurée 2026-08-02 des 14 sous-dossiers réels de `03_Resources_Geordi/` vers les 4 buckets PARA et les 5 strates S0→S4. Table de vérité de la racine KB.
tags: [para, second-brain, geordi, strates, mapping, kb-racine]
generated: { by: minimax-m3, at: 2026-08-17T20:42:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:42:00Z }
sources:
  - id: second-brain-map
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/SECOND_BRAIN_PARA_MAP.md"
    title: "Second Brain PARA — Carte des 14 sous-dossiers Geordi"
    last_modified: 2026-08-02
  - id: geordi-kb-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/GEORDI_KB_ROOT.md"
    title: "Geordi — Racine de la Knowledge Base"
    last_modified: 2026-08-01
  - id: fix-kb
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/FIX_KB_2026-08-02.md"
    title: "FIX KB — 2026-08-02"
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Second Brain PARA — 14 sous-dossiers de Geordi

> Mesure faite au 2026-08-02 sur le disque (jonctions exclues, realpath dedup).
> Total canon : **48 221 fichiers `.md`**. Volume = la racine KB du Second Brain PARA.

## 1. Table de vérité — 14 sous-dossiers ↔ PARA ↔ Strate

| # | Sous-dossier | `.md` | Bucket PARA | Strate | Owner canon |
|---|---|---:|---|---|---|
| 1 | `00_Index/` | 6 | méta | **S4** | Geordi |
| 2 | `01_Guides/` | 15 560 | Resources | **S3** | Geordi |
| 3 | `02_Templates/` | 136 | Resources | **S3** | Geordi |
| 4 | `03_Memory_Unified/` | 1 774 | Resources | **S1+S3** | Geordi + Computer |
| 5 | `04_From_V2_Root/` | 14 613 | **hors KB** | **hors strate** | Data (défaut) |
| 6 | `05_From_V2_Domains/` | 8 094 | **hors KB** | **hors strate** | Data (défaut) |
| 7 | `06_Claude_Code_Bare/` | 6 171 | mixte | **S0+S3** | Computer |
| 8 | `07_From_Home_Root_2026-08-01/` | 32 | Resources | **hors strate** (TRIAGE_PENDING) | Geordi |
| 9 | `08_Workspaces_Dormants_2026-08-01/` | 278 | Resources | hors strate (TRIAGE_PENDING) | Geordi |
| 10 | `09_From_Home_Root_Batch2_2026-08-01/` | 64 | Resources | hors strate (TRIAGE_PENDING) | Geordi |
| 11 | `09_Life_OS/` | 297 | Areas | **S3** | Spock |
| 12 | `Cerritos_Plane_Settings/` | 1 | Areas | hors strate | Spock (en attente) |
| 13 | `Youtube_Take_out/` | 0 | Resources | hors strate | Geordi (en attente) |
| 14 | `graphify-out/` | 1 195 | Resources | **S4** | Geordi |

## 2. Mapping inverse — depuis bucket PARA vers sous-dossiers

| Bucket PARA | Owner | Sous-dossiers Geordi |
|---|---|---|
| **Projects** (action immédiate) | Picard | (aucun pour l'instant — Picard atteignable via parent) |
| **Areas** (responsabilités continues) | Spock | `09_Life_OS/` (297) + `Cerritos_Plane_Settings/` (1) |
| **Resources** (réutilisable) | Geordi | `00_Index/` + `01_Guides/` (15 560) + `02_Templates/` (136) + `03_Memory_Unified/` (1 774) + `06_Claude_Code_Bare/` (6 171 outillage) + `graphify-out/` (1 195) + 07/08/09 Batch2 + Youtube |
| **Archives** (retiré / historique) | Data | `04_From_V2_Root/` (14 613) + `05_From_V2_Domains/` (8 094) — en attente qualification étape 3 |

## 3. Mapping strate → sous-dossiers

| Strate | Sous-dossiers | Cardinalité |
|---|---|---|
| **S0** Identité | `06_Claude_Code_Bare/CLAUDE.md` + AGENTS.md + memory/MEMORY.md | ~quelques fichiers |
| **S1** Court terme | `wiki/hand_offs/` (350) + daily notes (4) | ~354 fiches |
| **S2** Travail | `wiki/_CAPTURE_2026-08-01/` (13 slugs) + `_INTAKE/` + memory agent (35) | ~50 |
| **S3** Long terme | `01_Guides/` + `02_Templates/` + `wiki/{L0,concepts,entities,J01-J04}/` + CC_Bare/canon + `09_Life_OS/` | > 16 000 |
| **S4** Méta | `00_Index/` + `wiki/index.md` + `wiki/ROT.md` + CC_Bare/CLAUDE_INDEX + `graphify-out/` (1 195) | < 1 210 |
| **hors strate** | `04_From_V2_Root/` + `05_From_V2_Domains/` + 07/08/09_Batch2 + Cerritos + Youtube | **23 082** |

## 4. Décisions architecturales datées

- **D-2026-08-01-#1** — Racine logique, pas physique. Les 14 sous-dossiers restent à leurs chemins.
- **D-2026-08-01-#2** — `04_From_V2_Root/` et `05_From_V2_Domains/` **hors KB** tant que l'étape 3 du Plan n'a pas fait l'échantillonnage (22 707 fichiers non indexés au 2026-08-02).
- **D-2026-08-01-#3** — `06_Claude_Code_Bare/` est **mixte S0+S3**. Tag `Strate:` au cas par cas.
- **D-2026-08-01-#4** — `09_Life_OS/` **appartient fonctionnellement à Spock** malgré le chemin Geordi. Owner canon = Spock.

## 5. Divergence de comptage à arbitrer

Le brief de Geordi annonçait `04_From_V2_Root` = 14 613 et `05_From_V2_Domains` = 8 094.
Un comptage indépendant (`_count_md.py`, jonctions skip à l'entrée, dedup realpath) donne
**14 947** et **14 945**. L'écart (334 et 6 851) peut venir d'un décalage temporel (fichiers
ajoutés depuis la mesure du brief) ou d'une granularité différente. À arbitrer ultérieurement.

## Liens entrants

- `geordi-kb-quatre-piliers.md` — où logent les 4 piliers dans ces 14 sous-dossiers
- `rot-strates-s0-s4.md` — la sémantique temporelle des strates
- `geordi-junctions-map-159.md` — les frontières physiques jonctions NTFS
