---
type: Concept
title: PRD-PORTFOLIO-B1-FRANCHISE — Index portfolio franchise B1
description: PRD index qui agrège les PRD commerciaux B1 de la franchise A'Space (offre 2026 Évolution IA, filtre B1 M3, portfolio franchise) avec un .bak de snapshot pré-M6.
tags: [prd, portfolio, b1-franchise, index, 2026, canon, .bak-m6]
generated: { by: minimax-m3, at: 2026-08-19T15:25:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:25:00Z }
sources:
  - id: prd-portfolio-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md"
    title: PRD-PORTFOLIO-B1-FRANCHISE_index (lu directement)
    last_modified: 2026-07-12
  - id: prd-portfolio-bak
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md._TRASH_2026-07-12_pre-m6.bak"
    title: Snapshot .bak du 2026-07-12 pré-M6
    last_modified: 2026-07-12
okf_version: "0.2"
---

# PRD-PORTFOLIO-B1-FRANCHISE — Index portfolio franchise B1

## Périmètre

Le PRD-PORTFOLIO-B1-FRANCHISE_index est l'**index** qui agrège les
PRD commerciaux de la franchise A'Space (B1) :

| PRD | Domaine |
|---|---|
| [[concept-prd-b1-filter-m3-001]] | Délégation filtre B1 (M3) |
| [[concept-prd-nexus-evolution-ia-001]] | Offre 2026 « Évolution IA d'Entreprise » |
| (lui-même) | Index portfolio franchise B1 |

## Anomalie : le `.bak` miroir

Le même chemin contient **deux fichiers** :

- `PRD-PORTFOLIO-B1-FRANCHISE_index.md` — canon actuel
- `PRD-PORTFOLIO-B1-FRANCHISE_index.md._TRASH_2026-07-12_pre-m6.bak`
  — snapshot pré-M6 marqué `_TRASH_`

Le suffixe `_TRASH_2026-07-12_pre-m6.bak` est explicite :
- **date** : 2026-07-12 (la veille du scellé Constitution v1.0)
- **état** : `_TRASH` (mis au rebut)
- **contexte** : `pre-m6` (avant le milestone M6)

Le snapshot **n'a pas été supprimé**. Il dort dans `_SPECS/PRD/`
comme **trace historique** de l'état pré-M6 — utile pour comprendre
ce qui a changé à M6.

## Verdict

**canon** — le PRD-PORTFOLIO actuel est l'index de référence. Le
`.bak` est une trace historique à conserver.

## Source du décompte

`find .../04_From_V2_Root/_SPECS/PRD/` → 4 fichiers :

- `PRD-B1-FILTER-M3-001_delegation-filtre-b1.md` (canon)
- `PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md` (canon)
- `PRD-PORTFOLIO-B1-FRANCHISE_index.md` (canon)
- `PRD-PORTFOLIO-B1-FRANCHISE_index.md._TRASH_2026-07-12_pre-m6.bak` (trace)
- `PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md._TRASH_2026-07-12_pre-m6.bak`
  (trace — NEXUS a aussi son .bak)

5 fichiers, 3 canon, 2 traces `.bak`. Les `.bak` sont la **mémoire
d'opposabilité** de la franchise.

## Concepts liés

- [[concept-prd-b1-filter-m3-001]] — le PRD opérationnel.
- [[concept-prd-nexus-evolution-ia-001]] — le PRD commercial.
- [[concept-prd-v1-master-ingress]] — la migration V0 → V1.
