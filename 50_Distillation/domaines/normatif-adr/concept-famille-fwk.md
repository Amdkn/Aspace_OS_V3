---
type: Concept
title: Famille FWK — 12 ADR cadres framework canoniques
description: La famille FWK (FWK-011 à FWK-022) définit les sept structures-cadres canoniques (PARA, Ikigai, LifeWheel, 12WY, GTD, DEAL, AgentPortal, Settings, LD-Cooperation, Blueprints, Quick-Access).
tags: [adr, fwk, framework, structure-canon]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-FWK-011
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-FWK-011_V0.1.1_7-Phases_Structure.md"
    title: FWK 011 — 7-Phases Structure
    last_modified: "2026-05-15"
  - id: ADR-FWK-016
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-FWK-016_GTD_Structure.md"
    title: FWK 016 — GTD Structure
    last_modified: "2026-05-15"
  - id: ADR-FWK-021
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md"
    title: FWK 021 — Blueprints Canon Tripartite
    last_modified: "2026-07-26"
  - id: ADR-FWK-022
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-022_quick-access-summers-and-inbox-pattern.md"
    title: FWK 022 — Quick Access Summers + Inbox
    last_modified: "2026-07-26"
okf_version: "0.2"
---

# Famille FWK — 12 ADR cadres framework canoniques

## Résumé

La famille **FWK** (12 ADR) définit les **structures-cadres** (frameworks) canoniques d'A'Space. Elle se divise en deux sous-groupes :

- **FWK-011 à FWK-020** (10 ADR) : les cadres originels, format V0 (court, sans frontmatter). Situés dans `_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/`.
- **FWK-021 à FWK-022** (2 ADR) : les cadres récents, format Blueprint. Situés dans `05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/`.

## Les 12 cadres canoniques

| ADR | Cadre |
|---|---|
| FWK-011 | 7-Phases Structure |
| FWK-012 | PARA Structure |
| FWK-013 | Ikigai Structure |
| FWK-014 | LifeWheel Structure |
| FWK-015 | 12WY Structure |
| FWK-016 | GTD Structure |
| FWK-017 | DEAL Structure |
| FWK-018 | AgentPortal Structure |
| FWK-019 | Settings Structure |
| FWK-020 | Framework-LD Cooperation |
| FWK-021 | Blueprints Canon Tripartite (Blueprint V3) |
| FWK-022 | Quick Access Summers + Inbox Pattern |

## Le format FWK

FWK-011 à FWK-020 suivent le format V0 (phase-build, sans frontmatter strict). FWK-021 et FWK-022 sont post-restructuration V3 : ils vivent dans `12_Blueprints/02-ADR/`, format Blueprint.

## Liens entre FWK

Les 9 premiers (011-019) sont les **cadres fondateurs** du Life OS V0. FWK-020 est le méta-cadre qui les fait coopérer. FWK-021 et FWK-022 sont des **méta-cadres V3** qui absorbent les précédents dans une structure tripartite (Doctrine / Manifest / Recipes).

## Statut vis-à-vis de V3

- **FWK-011 à FWK-020** : **synthese-datee**. La justification des 7 phases est toujours vraie ; la nomenclature lisible dans la structure est caduque (FWK-021 a remplacé FWK-011 à 019 dans le canon Blueprints).
- **FWK-021** : **canon**. Le canon tripartite Blueprints (Doctrine + Manifest / Recipes) est la structure de référence V3.
- **FWK-022** : **canon**. Le pattern Quick Access + Inbox est la dernière doctrine UX validée.

## Le verdict de cette distillation

**mixte** : 9 synthese-datee + 2 canon + 1 canon. Aucune suppression.

## Liens

- Voir aussi : `concept-famille-v0.md` (le format V0 dont FWK hérite)
- Voir aussi : `concept-famille-aaas.md` (la famille AAAS pricing)