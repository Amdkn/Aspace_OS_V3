---
type: Bundle index
title: archives — Concepts distillés de 04_Archives_Data
description: Sous-bundle de la distillation. 15 concepts OKF v0.2 posés à partir du seau `04_Archives_Data/` (12 284 fichiers .md, 94 % dans `_V3_STRUCTURE_2026-08-02/`). Couvrent la doctrine d'archivage A3 Data, le versement V3 du 2026-08-02, la chaîne SDD legacy, le pipeline Graphify, et la transition de vocabulaire d'agents entre mai et août 2026.
tags: [distillation, okf, archives, v2, para, data, graphify, 2026-08-17]
generated: { by: minimax-m3, at: 2026-08-18T00:10:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-18T00:10:00Z }
sources:
  - id: bundle
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md"
    title: Index racine de la distillation 50_Distillation
    last_modified: 2026-08-17
  - id: methode
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/METHODE.md"
    title: Méthode de distillation (deux temps, règle de couverture partielle déclarée)
    last_modified: 2026-08-17
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl"
    title: Substrat d'extraction — 12 284 fichiers .md, 9,8 M mots
    last_modified: 2026-08-17
  - id: rapport
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_archives.md"
    title: Rapport de couverture de la distillation archives
    last_modified: 2026-08-18
okf_version: "0.2"
---

# archives — 15 concepts distillés du seau `04_Archives_Data`

## Doctrine d'archivage (A3 Data)

- [data-role-a3-archives-officer](data-role-a3-archives-officer.md) — Data = officier A3, mission « retired evidence searchable but not active », 5 findings YAML, 4 boundaries explicites.
- [deal-muse-data-as-conductor](deal-muse-data-as-conductor.md) — patch 2026-06-21 sur A3 : Data reste A3 (PAS 5ème A2), chef d'orchestre DEAL par imbrication DEAL ⊂ PARA, 4 jumeaux Dal/Rok-Tahk/Zero/Gwyn.
- [archive-as-source-of-truth-decision](archive-as-source-of-truth-decision.md) — décision D-2026-08-01-#1 : Geordi (03_Resources_Geordi) est la racine unique de la KB, archives = héritage réversible.

## ADR-cadres

- [adr-sober-002-anti-paperclip-doctrine](adr-sober-002-anti-paperclip-doctrine.md) — RATIFIED 2026-06-21, L0 Kernel OS, impose le move (pas la réécriture ni la suppression), manifest src→dst.
- [adr-meta-001-anti-paresse-verify-before-assert](adr-meta-001-anti-paresse-verify-before-assert.md) — ACCEPTED 2026-06-08, L1 Life OS, fondation de la série META, source du marqueur OKF `verified`.

## Versement V3 (2026-08-02)

- [archive-v3-structure-snapshot-2026-08-02](archive-v3-structure-snapshot-2026-08-02.md) — 17 665 fichiers déplacés (11 504 .md) de V3 vers `04_Archives_Data/_V3_STRUCTURE_2026-08-02/`, application de l'ADR-SOBER-002.
- [archive-published-secrets-warning](archive-published-secrets-warning.md) — au moins 11 fichiers de l'archive portent des secrets déjà publiés sur GitHub via le commit `41c19a5` ; la rotation des credentials est la seule parade.

## Legacy specs (avant 2026-05-22)

- [legacy-lifeos-app-specs-evolution](legacy-lifeos-app-specs-evolution.md) — 750 fichiers legacy, 338 440 mots, chaîne SDD V0.2 → V0.6, pivot V0.5 « Livre des Lois ».
- [sdd-sovereign-constitution-v05](sdd-sovereign-constitution-v05.md) — analyse du pivot V0.5 : 8 domaines figés, migration IndexedDB, Pont Top-Down/Bottom-Up, vocabulaire A'0 GravityClaw / A'1 Rick.

## Avant-M3 (février-mars 2026)

- [openclaw-body-legacy](openclaw-body-legacy.md) — 10 fichiers de config + AGENTS.md (20 576 octets), modèle GPT-5.2 Codex, version 2026.2.1, runtime OpenClaw (avant Claude Code).
- [agent-vocabulary-legacy-vs-current](agent-vocabulary-legacy-vs-current.md) — transition du vocabulaire d'agents entre 2026-05 et 2026-08, A'0 GravityClaw → A0 Amadeus, etc.

## Pipeline Graphify (2026-06-16)

- [graphify-out-pipeline-partial-run](graphify-out-pipeline-partial-run.md) — run 25 chunks / 8 workers / 14 ok / 11 failed, 1006 nœuds / 1666 arêtes / 17 communautés (long tail).
- [graphify-burst-chunk-duplication-pattern](graphify-burst-chunk-duplication-pattern.md) — `affine_deal_drafts.md` (60 001 mots) dupliqué dans 4 chunks, `REBUILD_PROMPT_V2.md` (15 627 mots) dans 3 chunks.

## Patterns transverses

- [shadow-active-1425-files-status](shadow-active-1425-files-status.md) — 11,6 % du seau en `status: SHADOW_ACTIVE` (1 425 fichiers), 2× plus que tous les statuts actifs réunis.
- [memory-compact-trash-snapshots](memory-compact-trash-snapshots.md) — 4 instantanés `_TRASH_2026-07-XX_mem_compact/` préservés malgré le préfixe `_TRASH_` (preuve de la doctrine « Data does not delete by default »).
- [ntfs-junctions-inventory-2026-08-01](ntfs-junctions-inventory-2026-08-01.md) — inventaire des jonctions NTFS, gardien du piège « 13,8 M de fichiers comptés là où il y en avait 14 613 ».
