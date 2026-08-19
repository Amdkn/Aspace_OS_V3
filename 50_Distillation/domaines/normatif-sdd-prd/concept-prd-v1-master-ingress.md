---
type: Concept
title: PRD-V1.0_Master_Ingress — la jonction V0 → V1
description: PRD-V1.0_Master_Ingress.md, seul PRD numéroté V1, qui pose le point d'entrée unique (master ingress) pour la migration V0 → V1 du 2026-08-01, fermant le cycle V0.x et ouvrant le cycle V1.
tags: [prd, v1.0, master-ingress, v0-vers-v1, migration, 2026-08-01, home-root]
generated: { by: minimax-m3, at: 2026-08-19T15:30:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:30:00Z }
sources:
  - id: prd-v1-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/09_From_Home_Root_Batch2_2026-08-01/workspaces/_SPECS/prds/PRD-V1.0_Master_Ingress.md"
    title: PRD-V1.0_Master_Ingress (lu directement)
    last_modified: 2026-08-01
okf_version: "0.2"
---

# PRD-V1.0_Master_Ingress — la jonction V0 → V1

## Contexte de placement

Le PRD-V1.0 est placé dans
`09_From_Home_Root_Batch2_2026-08-01/workspaces/_SPECS/prds/` —
le **batch2** du 2026-08-01, soit **la veille** du versement V3
(2026-08-02). C'est un doc de **jonction**.

## Le rôle de master ingress

« Master ingress » = point d'entrée unique. Le PRD pose :

- La convergence de toutes les sources V0.x vers une **route unique**
  (probablement le `_INBOX/` racine du nouveau V3).
- La fermeture du cycle V0 (sceau Legacy_LifeOS_App_Specs_2026-05-22).
- L'ouverture du cycle V1 (le 2026-08-02 ouvre la V3).

## Verdict

**canon** — c'est le seul PRD numéroté V1 dans tout le corpus. Sa
valeur est **historique** (la jonction) plus qu'opérationnelle
(l'implémentation est aujourd'hui dans `ASpace_OS_V3/_INBOX/`).

## Source du décompte

`find .../09_From_Home_Root_Batch2_2026-08-01/` → ce PRD est le
seul doc canon dans ce batch (avec d'autres artefacts non-PRD).

`find` global du corpus PRD : 51 PRD uniques. **Seul V1.0 numérote
la jonction V0 → V1**. Tous les autres PRD canon (3 dans
`04_From_V2_Root/_SPECS/PRD/`) sont des B1 / NEXUS / PORTFOLIO non
versionnés.

## Concepts liés

- [[concept-prd-chain-v0x-legacy]] — la chaîne V0.x fermée par ce
  PRD.
- [[concept-prd-portfolio-b1-franchise]] — l'index portfolio qui
  coexiste avec cette jonction.
