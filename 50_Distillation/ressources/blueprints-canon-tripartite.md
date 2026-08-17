---
type: Concept
title: Canon Tripartite des Blueprints (ADR-FWK-021)
description: Doctrine d'isomorphie L0/L1/L2 pour les Blueprints : trois canons (10_Tech_OS\12_Blueprints\, 20_Life_OS\28_Blueprints\, 30_Business_OS\09_Blueprints\). Chaque canon contient 01-SDD/02-ADR/03-PRD/04-DDD. _SPECS\ devient zone d'inbox, plus de canon.
tags: [blueprints, canon, l0-l1-l2, isomorphie, adr-fwk-021, sdd, adr, prd, ddd]
generated: { by: minimax-m3, at: 2026-08-17T21:05:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:05:00Z }
sources:
  - id: adr-fwk-021-entity
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/entities/entity_adr_fwk_021.md"
    title: "ADR-FWK-021 — Canon Tripartite des Blueprints"
    last_modified: 2026-05-22
  - id: adr-fs-001-entity
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/entities/entity_adr_fs_001.md"
    title: "ADR-FS-001 — Junction-Based Aliasing"
    last_modified: 2026-05-22
  - id: concept-sdd
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_sdd.md"
    title: "Concept: SDD (System Design Documents)"
    last_modified: 2026-05-11
okf_version: "0.2"
---

# Canon Tripartite des Blueprints (ADR-FWK-021)

> Doctrine établissant **trois canons Blueprints isomorphes** : un par couche.
> Ratifiée 2026-05-22 par A0.
> Corollaire opérationnel d'`ADR-FS-001` (junction-based aliasing).

## 1. Les trois canons

| Couche | Chemin canon | Rôle Owner |
|---|---|---|
| **L0** | `10_Tech_OS\12_Blueprints\` | Rick (L0 Sovereignty) |
| **L1** | `20_Life_OS\28_Blueprints\` | Beth/Morty (L1 Life) |
| **L2** | `30_Business_OS\09_Blueprints\` | Jerry/Summer (L2 Business) |

Chaque canon contient les **4 mêmes sous-dossiers isomorphes** :

```
<canon>/
├── 01-SDD/     — System Design Documents
├── 02-ADR/     — Architecture Decision Records
├── 03-PRD/     — Product Requirements Documents
└── 04-DDD/     — Domain-Driven Design artifacts
```

## 2. Convention immuable

```
<TYPE>-<NAMESPACE>-<NNN>_<kebab-case>.md
```

Exemple : `ADR-FS-001_junction-based-aliasing.md`, `SDD-000_constitution-ricks-verse.md`.

## 3. Déclassement de `_SPECS\`

`_SPECS\` était le canon historique. **Désormais zone d'inbox (brouillons), plus de canon**.
Tout contenu canon migre vers la triplette L0/L1/L2.

## 4. Isomorphie pratique

Si un ADR-FS-001 (filesystem, L0) traite d'un répertoire L1 ou L2 :

- Le contenu vit dans `02-ADR/` du **canon L0** (le namespace gagne).
- Un cross-pointer documente l'impact aux autres couches.

Si un SDD traite du design d'une app L2 :
- Le contenu vit dans `01-SDD/` du **canon L2** (`30_Business_OS\09_Blueprints\01-SDD\`).
- Le `01-SDD/` du canon L0 héberge seulement les designs infra (kernel, agents).

## 5. Statut Constitution v1.0

L'article 5 de la Constitution A'SPACE (2026-07-12) rétrograde les ADR en **mémoire
consultative**. L'ADR-FWK-021 lui-même survit comme **bonne pratique d'architecture** :
« canon isomorphe L0/L1/L2 avec sous-dossiers 01-SDD/02-ADR/03-PRD/04-DDD » — réflexe
d'ingénierie, pas blocage.

## 6. Liens avec la doctrine NTFS junction

- ADR-FS-001 expose les Blueprints via NTFS junctions sectorielles.
- ADR-FWK-021 garantit que chaque couche a son propre canon et ne fuit pas dans une autre.
- Ensemble : **architecture canonique + exposition filesystem = souveraineté maintenable.**

## Liens entrants

- `adr-immutability-ricks-law.md` — l'amont (les ADR eux-mêmes)
- `sdd-system-design-documents.md` — la couche design
- `ntfs-junction-aliasing.md` — la matérialisation filesystem
