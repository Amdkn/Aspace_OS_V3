---
type: Concept
title: AMEND pattern — append-only sur les ADR canoniques
description: Les amendements ADR (AMEND-001, AMEND-002…) sont append-only : un ADR amendé reste canonique, le AMEND ne réécrit pas le corps mais ajoute une décision datée.
tags: [adr, amend, append-only, pattern]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-AAAS-PRICING-001-AMEND-002
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_AMEND-002_spacex-rarety_PROPOSED_2026-07-12.md"
    title: AMEND 002 SpaceX Rarety (PROPOSED non ratifié)
    last_modified: "2026-07-12"
  - id: ADR-AAAS-PRICING-001-AMEND-003
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_AMEND-003_enterprise-os-tier5_RATIFIED_2026-07-15.md"
    title: AMEND 003 Tier 5 Enterprise OS (RATIFIED)
    last_modified: "2026-07-15"
  - id: ADR-RH-META-GOUVERNANCE-001-v3
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v3_RATIFIED_2026-07-26.md"
    title: RH Meta Gouvernance canonical v3 (RATIFIED)
    last_modified: "2026-07-26"
  - id: ADR-GSTACK-IMBRICATION-001-v2
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/META_Organization/ADR-GSTACK-IMBRICATION-001-v2_RATIFIED_2026-07-26.md"
    title: GStack Imbrication v2 RATIFIED
    last_modified: "2026-07-26"
okf_version: "0.2"
---

# AMEND pattern — append-only sur les ADR canoniques

## Résumé

Le **pattern AMEND** est la doctrine de modification des ADR canoniques : on **n'efface jamais** une décision ratifiée, on la complète par un ADR-`<ID>-AMEND-<NNN>` qui ajoute une décision datée.

## Pourquoi append-only

Le canon A'Space défend une règle simple : **le fait qu'une décision ait changé est lui-même une information**. Effacer la décision originelle pour la remplacer par la nouvelle perdrait la trace du mouvement.

Ce principe est posé explicitement dans plusieurs ADR :

- `ADR-L2-TRIPTYQUE-V3-001` : `supersedes: NONE (D4 additif : V2 reste archive vivante + applicable pour rétro-compat ; forward canon = V3)`
- `ADR-L2-TRIPTYQUE-V4-001` : `supersedes: NONE (D4 additif : V3 stays archive vivante for rétro-compat; forward canon = V4)`
- `ADR-L2-PAPERCLIPAI-004` : `supersedes: NONE (D4 append-only)`
- `ADR-L2-KARDASHEV-TYPE-FRACTAL-001` : `supersedes: NONE (D4 additif — clarification layer over existing canon)`

## Trois chaînes AMEND documentées

### Chaîne 1 — AAAS Pricing

| Étape | Fichier | Statut | Date |
|---|---|---|---|
| Original | `ADR-AAAS-PRICING-001_aaas-pricing-canon.md` | RATIFIED | 2026-06-24 |
| AMEND-001 | (impossible à confirmer) | ? | ? |
| AMEND-002 | `..._AMEND-002_spacex-rarety_PROPOSED_2026-07-12.md` | PROPOSED non ratifié | 2026-07-12 |
| AMEND-003 | `..._AMEND-003_enterprise-os-tier5_RATIFIED_2026-07-15.md` | RATIFIED | 2026-07-15 |

L'AMEND-003 ajoute le Tier 5 (Coach-Deployer, $1500/mo engine + 4 daughter packages) au canon pricing 5-tiers.

### Chaîne 2 — RH Meta Gouvernance

| Étape | Fichier | Statut | Date |
|---|---|---|---|
| Canonical v1 | (drafts `_DRAFTS_PPR_LANE`) | PROPOSED | 2026-07-25 |
| Canonical v2 | `..._canonical-v2_PROPOSED_2026-07-25.md` | PROPOSED non ratifié | 2026-07-25 |
| Canonical v3 | `..._canonical-v3_RATIFIED_2026-07-26.md` | RATIFIED | 2026-07-26 |

### Chaîne 3 — GStack Imbrication

| Étape | Fichier | Statut | Date |
|---|---|---|---|
| Original | `..._gstack-superpowers-gsd-wargame_RATIFIED_2026-07-26.md` | RATIFIED | 2026-07-26 |
| v2 | `..._gstack-superpowers-gsd-wargame-v2_RATIFIED_2026-07-26.md` | RATIFIED | 2026-07-26 |

Le suffixe `-v2` est une variante du pattern — la deuxième version est ratifiée le même jour.

## Le pattern D4

Le label **D4 append-only** revient dans presque tous les AMEND. C'est la doctrine formalisée :

> Une décision ratifiée reste canonique. Toute évolution ouvre un AMEND daté qui complète, jamais n'efface.

## Le verdict de cette distillation

**canon**. Le pattern AMEND est appliqué systématiquement dans les chaînes documentées ci-dessus. Aucun AMEND n'a été trouvé qui contrevienne à la règle append-only.

## Liens

- Voir aussi : `concept-adr-format.md` (statuts ADR)
- Voir aussi : `concept-trash-superseded.md` (conservation des versions superseded)