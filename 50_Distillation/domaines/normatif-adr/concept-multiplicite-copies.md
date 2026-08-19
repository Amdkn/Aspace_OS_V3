---
type: Concept
title: Multiplicité des copies — 5 copies par ADR, où est la vérité ?
description: Chaque ADR canonique existe en 5 à 13 exemplaires : source vivante (openspec ou Blueprints), chunks graphify, archive legacy, archive V3_STRUCTURE. La copie vivante fait foi.
tags: [adr, multiplicite, copies, graphify, chunks, archives]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: SAMPLE-V0.4.5
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/ADR-V0.4.5_LaboSpock.md"
    title: V0.4.5 LaboSpock — exemple de 13 copies
    last_modified: "2026-05-25"
okf_version: "0.2"
---

# Multiplicité des copies — 5 copies par ADR, où est la vérité ?

## Résumé

Chaque ADR canonique existe en **5 à 13 exemplaires** dans le dépôt V2. Cette multiplicité pose un problème simple : **quelle copie fait foi ?**

## Les cinq localisations

Pour un ADR typique du `_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/`, on trouve :

| # | Localisation | Nature | Fait foi ? |
|---|---|---|---|
| 1 | `04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/` | **Source vivante** | ✅ Oui |
| 2 | `04_From_V2_Root/05_From_V2_Domains/.../graphify-burst/chunks/chunk_001/...` | Chunk généré | ❌ Non |
| 3 | `04_From_V2_Root/05_From_V2_Domains/.../graphify-burst/chunks/chunk_011/...` | Chunk généré | ❌ Non |
| 4 | `04_From_V2_Root/05_From_V2_Domains/.../graphify-burst/chunks/chunk_015/...` | Chunk généré | ❌ Non |
| 5 | `04_From_V2_Root/05_From_V2_Domains/.../graphify-burst/chunks/chunk_017/...` | Chunk généré | ❌ Non |
| 6 | `04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/ADR/` | Legacy TOTAL_Spec | ❌ Archive |
| 7 | `04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/ADR/` | Legacy _SPECS | ❌ Archive |
| 8-12 | `04_Archives_Data/_V3_STRUCTURE_2026-08-02/...` | Mirror archive V3 | ❌ Archive |

Pour `ADR-V0.4.5_LaboSpock.md`, on observe **13 fichiers** en tout, soit 1 source + 4 chunks (uniques en fait) + 4 archives V3 + 2 legacy + 2 autres localisations.

## Pourquoi 5 copies

Le multiplicité vient de plusieurs opérations historiques :

1. **Génération graphify** : le pipeline Graphify découpe les ADR en chunks pour l'embedding. Chaque ADR peut tomber dans plusieurs chunks.
2. **Migration V3_STRUCTURE** : le 2026-08-02 a créé un snapshot V3 de l'arborescence V2, copiant tout.
3. **Legacy TOTAL_Spec + _SPECS** : avant la consolidation, le même ADR était à deux endroits.

## La copie qui fait foi

Règle énoncée dans le brief vague 2 :

> quand deux copies divergent, la copie vivante sous `05_From_V2_Domains/` fait foi — les `chunks/` sont générés, `_V3_STRUCTURE_2026-08-02/` est une archive.

En pratique, c'est :

1. **Pour les ADR L0/L1/L2** : `04_From_V2_Root/_SPECS/ADR/<couche>/` (le clone V2-Root)
2. **Pour les ADR Blueprints récents** : `05_From_V2_Domains/<couche>/12_Blueprints/02-ADR/`
3. **Pour les ADR LD01** : `05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/`

## Statut vis-à-vis de V3

**canon** sur la doctrine ; **synthese-datee** sur la pratique (la multiplicité est un legs historique que V3 doit résoudre en ne gardant qu'une copie par ADR).

## Le verdict de cette distillation

**canon** pour la doctrine de « qui fait foi ». **synthese-datee** pour la pratique du jour (V3 doit dédupliquer).

## Liens

- Voir aussi : `concept-adr-format.md` (le format)
- Voir aussi : `concept-trash-superseded.md` (la conservation)