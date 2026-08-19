---
type: Concept
title: Source-of-truth canon — vivante (05_From_V2_Domains) vs archives (_V3_STRUCTURE)
description: La règle de canon du corpus SDD/PRD : la copie vivante sous 05_From_V2_Domains/ fait foi, les graphify-out/chunks sont générés et se régénèrent, _V3_STRUCTURE_2026-08-02/ et Legacy_LifeOS_App_Specs_2026-05-22/ sont des archives immuables.
tags: [source-of-truth, canon, vivante, archive, chunks, graphify-out, immutable, append-only]
generated: { by: minimax-m3, at: 2026-08-19T15:55:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:55:00Z }
sources:
  - id: amendement-canon-rule
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (lignes 1172-1184)"
    title: Amendement 001 — section « Copies non amendées »
    last_modified: 2026-08-19
  - id: legacy-specs-evolution
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/legacy-lifeos-app-specs-evolution.md"
    title: Concept archive : Legacy LifeOS App Specs V0.2 → V0.6
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Source-of-truth canon — vivante vs archives

## La règle du canon

Le corpus SDD/PRD vit dans **quatre types de copies**, avec une
hiérarchie explicite posée par l'Amendement 001 (verbatim, lignes
1172-1184) :

| Copie | Statut canonique | Traitement |
|---|---|---|
| `05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/` | **vivante** | source de vérité, porte les amendements |
| `03_Memory_Unified/LLM_Wiki/raw/sdd/` | source du wiki | à amender si le wiki est régénéré |
| `LLM_Wiki/wiki/graphify-out/chunks/chunk_NNN/` | **générées** | se régénèrent, ne pas toucher |
| `04_Archives_Data/_V3_STRUCTURE_2026-08-02/` | **archive** | ne jamais modifier une archive |

Pour les PRD :

| Copie | Statut |
|---|---|
| `Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/prds/` | archive scellée 2026-05-22 |
| `Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/PRD/` | archive scellée 2026-05-22 |
| `04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/PRD/` | clone intermédiaire |
| `04_From_V2_Root/_SPECS/PRD/` | **vivante post-M6** (B1/INDEX/NEXUS) |

## Pourquoi la vivante fait foi

Trois raisons :

1. **C'est la seule copie qui porte les amendements ratifiés**. Les
   archives et les chunks sont **datés du moment du snapshot** — ils
   ne capturent pas les amendements append-only.
2. **L'Amendement 001 (2026-08-19) l'a explicitement nommée** : «
   seule celle-ci — la copie vivante sous `05_From_V2_Domains/` —
   porte l'amendement ».
3. **Le pipeline graphify-out** est conçu pour régénérer les chunks à
   partir de la vivante. La vivante est l'**input**, les chunks sont
   l'**output**.

## Le piège de la duplication massive

Le corpus SDD/PRD existe en **plus de 1 000 fichiers** sur le disque
pour **~82 documents uniques** (31 SDD + 51 PRD). Le ratio
**12 fichiers / document** vient de :

- **2 miroirs Legacy** : `_SPECS/` (verticale) + `TOTAL_Spec/`
  (portrait horizontal).
- **4 copies par chaîne numérotée** : wiki raw + graphify-out/chunks
  × 3 chunks différents + 2 archives (`_V3_STRUCTURE_2026-08-02/`).
- **Clone de travail** : `_Life-OS-2026-clone/openspec/changes/...`.

## Verdict

**canon** — la règle est elle-même canon (énoncée par l'Amendement
001). Le présent concept est confirmé par :

- l'Amendement 001 du SDD-006 (verbatim)
- le concept archive [[legacy-lifeos-app-specs-evolution]] qui
  distingue `_SPECS/` (verticale) et `TOTAL_Spec/` (horizontal)

## Source du décompte

`find` exhaustif du corpus SDD/PRD :

- SDD : 175 fichiers total (mesure 2026-08-19) → 31 uniques
- PRD : 457 fichiers total → 51 uniques (estimation)

## Concepts liés

- [[concept-sdd-006-collision]] — la collision qui illustre la règle.
- [[concept-amendement-001-8e-domaine]] — l'Amendement 001 qui pose
  la règle.
