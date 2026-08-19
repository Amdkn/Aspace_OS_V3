---
type: Concept
title: Repo-Home Junction Law — la doctrine vit longtemps, le code vit court
description: La loi ADR-INFRA-002 — chaque projet Picard porte une junction `_doctrine/` en lecture seule vers la source canonique. Le code change, la doctrine reste.
tags: [adr-infra-002, junction, doctrine, repo-home, d6, d4]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: MANIFEST_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/MANIFEST.md"
    title: Manifest — ceo-desktop
    last_modified: "2026-07-13"
  - id: MANIFEST_SOLARIS
    resource: "30_Business_OS/10_Projects/solaris/MANIFEST.md"
    title: Manifest — solaris
    last_modified: "2026-07-13"
  - id: MANIFEST_OMK
    resource: "30_Business_OS/10_Projects/omk/MANIFEST.md"
    title: Manifest — omk (PARENT)
    last_modified: "2026-07-13"
  - id: README_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/README.md"
    title: README — CEO's Desktop
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# Repo-Home Junction Law — la doctrine vit longtemps, le code vit court

> **Une seule chose à retenir.** Chaque projet Picard porte un dossier `_doctrine/` qui est une **junction** vers la source canonique — pas une copie. La doctrine vit longtemps ; le code, l'implémentation et les particularités projet vivent court.

## Énoncé canonique

> ADR-INFRA-002 (Repo-Home Junction Law): doctrine lives long, code lives short, junction points the way. (`README_CEO_DESKTOP.md`, `MANIFEST_CEO_DESKTOP.md`)

## La règle en pratique

Chaque `30_Business_OS/10_Projects/<project>/` porte, en symlink ou en dossier-miroir :

- **`_doctrine/`** — lecture seule, source canonique (`20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/<project>/` pour les Picard-Projects, ou `20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_*/<project>/` pour les Spock-Areas).
- **`CLAUDE.md`** — addenda projet-scopés, **ne duplique pas** `~/.claude/CLAUDE.md`.
- **`MANIFEST.md`** — canon d'identité projet, frontmatter complet, status, Rocks, graduation criteria.
- **`apps/`** — surface build-bearing, **optionnelle en Phase 1**.

## Pourquoi cette loi

- **D4 append-only + D6 no-self-contradiction guard.** Les MANIFEST canon se propagent par junction, pas par duplication. Tout override local doit explicitement dire « je dérive de, parce que ».
- **Réversibilité.** Un projet peut pivoter ou être archivé sans toucher à la doctrine. Le code change, la doctrine reste lisible.
- **Lisibilité humaine.** Un agent qui ouvre un projet voit immédiatement : (1) le canon, (2) la particularité projet, (3) le code. Pas 23 niveaux de copies.

## Trois exemples lus dans le corpus

| Projet         | `_doctrine/` pointe vers                                                            | Source MANIFEST              |
|----------------|--------------------------------------------------------------------------------------|------------------------------|
| `ceo-desktop`  | `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/00 Agency as a Service` (sister canon) | `MANIFEST.md:17`             |
| `solaris`      | `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/00 Agency as a Service`            | `MANIFEST_SOLARIS:17-19`     |
| `omk`          | `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/`                | `MANIFEST_OMK:22`            |

## Anti-patterns

- **Dupliquer la doctrine dans le projet.** Le MANIFEST canon se réfère par chemin, jamais par recopie.
- **Toucher la cible de la junction depuis le projet.** La source canonique ne se modifie **que** depuis son propre dossier.
- **Oublier la junction en Phase 1 puis la créer tardivement.** Le `area_junction_placeholder.md` est explicitement le marqueur de Phase 1 deferred pour `ceo-desktop` ; il sera remplacé par la symlink Phase 2.

## Conséquence opérationnelle

Un projet qui n'a pas de junction `_doctrine/` n'a pas de source de vérité. Sa MANIFEST ne peut pas être ratifiée ; ses Rocks ne peuvent pas être acceptés ; sa Phase 2 ne peut pas démarrer.
