---
type: Concept
title: the-bridge — Life OS ↔ Business OS conductor track
description: Le dossier the-bridge-__-life-os relie L1 Life OS (12WY, PARA, Life Wheel) à L2 Business OS via une track V0.1.x. Le conductor-track orchestre 9 baselines V0.1.1–V0.1.9 (Command Center, PARA Business, Ikigai, Life Wheel, 12WY, GTD, DEAL, Agent Portal, App Store). V0.2 = audit de grande échelle + IA Integration.
description: ""
tags: [bridge, conductor-track, life-os, business-os, v0.1.x, v0.2, 12wy, para, gtd, ikigai]
generated: { by: minimax-m3, at: 2026-08-17T21:50:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T21:50:00Z }
sources:
  - id: conductor-track
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/the-bridge-__-life-os/conductor-track.md"
    title: Conductor Track — A'Space Web OS V0.1.x
    last_modified: 2026-03-18
  - id: bridge-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/the-bridge-__-life-os/README.md"
    title: the-bridge README (AI Studio boilerplate)
    last_modified: 2026-03-15
okf_version: "0.2"
---

# the-bridge — Life OS ↔ Business OS conductor track

Le dossier `the-bridge-__-life-os/` est le pont opérationnel entre **L1 Life OS** (12WY, PARA, Life Wheel, Ikigai) et **L2 Business OS** (Spock Areas, Jerry, Summer's Verse). C'est une **Area Spock** technique : son rôle est de tenir la trace des versions, des baselines, et des cycles de release.

> **Note** : le README du dossier (`README.md`) est un fichier AI Studio générique qui ne décrit pas le pont. Le source de vérité pour la doctrine du pont est `conductor-track.md` — c'est ce que cet Area distille.

## Le conductor-track — la mémoire dynamique du Conductor

`conductor-track.md` §« Rôle » pose le format :

> *Fichier de mémoire dynamique du Conductor (A2 Dev).*
> *Usage : Gemini CLI lit ce fichier au début de chaque session et le met à jour après chaque phase.*
> *Règle : Cocher `[x]` = Phase terminée. `[/]` = En cours. `[ ]` = À faire.*

C'est le **state-of-the-bridge** lu et écrit à chaque session. Le Conductor (A2 Dev) est l'agent qui orchestre les releases ; son état est dans ce fichier.

## Le cycle V0.1.x — 9 baselines consécutives

`conductor-track.md` §« État Global » liste 9 versions, toutes `[x]` DONE au 2026-03-18 :

| Version | Statut | Sujet | Tag Baseline |
|---|---|---|---|
| V0.1.1 | DONE | Command Center (Cœur) | `v0.1.1-baseline` |
| V0.1.2 | DONE | PARA Business (Write ALL via LD-Router) | `v0.1.2-baseline` |
| V0.1.3 | DONE | Ikigai Protocol (Read-Only) | `v0.1.3-baseline` |
| V0.1.4 | DONE | Life Wheel (Read ALL + FW Scores) | `v0.1.4-baseline` |
| V0.1.5 | DONE | 12 Week Year (Write LD01) | `v0.1.5-baseline` |
| V0.1.6 | DONE | GTD System (Write 4 LDs) | `v0.1.6-baseline` |
| V0.1.7 | DONE | DEAL Protocol (Read-Only) | `v0.1.7-baseline` |
| V0.1.8 | DONE | Agent Portal | `v0.1.8-baseline` |
| V0.1.9 | DONE | App Store & Settings (Marketplace + OsSettings) | `v0.1.9-baseline` |

Chaque baseline est un **tag git** (présumé) qui marque l'état reproductible. V0.1.9 marque **CYCLE V0.1.X TERMINE**.

## Ce que chaque baseline représente

La séquence **est** l'intégration Life OS ↔ Business OS :

- **V0.1.1 — Command Center** : le cœur (la home).
- **V0.1.2 — PARA Business** : écrire tous les Life Domains via le LD-Router (le PARA implémente l'écriture multi-LD).
- **V0.1.3 — Ikigai Protocol (Read-Only)** : l'Ikigai en lecture seule (le centre du Wheel).
- **V0.1.4 — Life Wheel (Read ALL + FW Scores)** : la wheel complète en lecture avec FW Scores (Feeling/Wheeling).
- **V0.1.5 — 12 Week Year (Write LD01)** : 12WY écrit LD01 (Business) — première intégration Life OS → Business OS active.
- **V0.1.6 — GTD System (Write 4 LDs)** : GTD écrit 4 LDs — extension de l'écriture multi-LD.
- **V0.1.7 — DEAL Protocol (Read-Only)** : DEAL (Ferriss) en lecture seule.
- **V0.1.8 — Agent Portal** : portal agent pour piloter l'ensemble.
- **V0.1.9 — App Store & Settings** : Marketplace + OsSettings unifiés, avec dynamique `getAllApps()`, dashboard, installed apps grid.

## Le passage V0.1.X → V0.2

`conductor-track.md` §« CYCLE V0.1.X TERMINE » :

> *Status : BASELINE ATTEINTE (V0.1.9).*
> *Prochaine étape : V0.2 Micro (Audit de Grande Échelle & IA Integration).*

V0.2 Micro = un audit de grande échelle et l'intégration IA. C'est la transition d'un système « manuel-Gemini-CLI-orchestré » vers un système « IA-integrated ». Pas encore daté dans le conductor-track lu.

## Le rôle openspec

À côté de `conductor-track.md`, le sous-dossier `openspec/` contient 9 changes formels (un par V0.1.x + un pour V0.1.9) au format openspec :

- `changes/aspace-web-os/` — change initial (design.md, proposal.md, tasks.md, 5 specs : agents-appstore, audit-antifragility, command-center, framework-apps, shell)
- `changes/v0.1.1-command-center/`, `v0.1.2-para-business/`, ..., `v0.1.8-agent-portal/` — un change par baseline

Le format openspec (proposal/design/tasks/specs) est le **langage des changes** : chaque release propose, design, tasks, specs.

## Le lien avec L2 Business Pulse

Le bridge **n'est pas** une Jerry Area — c'est une **Spock Area technique** au sens du concept `spock-areas-canon.md` : un domaine permanent, sans échéance, qui tient l'instrument qui relie les deux layers. Il est adjacent aux Jerry Areas (qui portent le contenu business) et aux Life Domains (qui portent le contenu Life OS). Sans le bridge, l'intégration Life OS ↔ Business OS n'a pas de substrate reproductible.

## La fonction Spock du bridge

Trois fonctions que Spock assure sur ce dossier :

1. **Traçabilité** : le conductor-track conserve l'état dynamique ; les openspec conservent l'intention et les spécs.
2. **Reproductibilité** : chaque baseline est un tag reproductible.
3. **Continuité** : le passage V0.1.X → V0.2 est documenté avec sa prochaine étape.

Sans ces trois fonctions, l'OS devient un ensemble d'artefacts sans liaison reproductible. Le bridge est ce qui maintient la **continuité opérationnelle**.

## Note sur le README

`README.md` du dossier contient le template AI Studio standard (« Run and deploy your AI Studio app »). C'est un artefact de **bootstrap** du repo, pas la doctrine du pont. Si une distillation future s'appuie sur ce README, elle sera factuellement fausse. Le source de vérité est `conductor-track.md` + `openspec/`.