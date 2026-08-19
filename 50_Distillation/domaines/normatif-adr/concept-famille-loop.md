---
type: Concept
title: Famille LOOP — 5 ADR cadences et boucles (canon loop, queues, heartbeat, calendar)
description: La famille LOOP (5 ADR) pose les cadences et boucles : canon loop verification-first, queues over loops HITL rightward, orient-layer signals wagers, heartbeat respiration cascade, calendar by design.
tags: [adr, loop, cadence, heartbeat, calendar, queues]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-LOOP-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-LOOP-001_canon-loop-verification-first.md"
    title: LOOP 001 — Canon Loop Verification-First
    last_modified: "2026-07-15"
  - id: ADR-LOOP-002
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-LOOP-002_queues-over-loops-hitl-rightward.md"
    title: LOOP 002 — Queues over Loops HITL Rightward
    last_modified: "2026-07-15"
  - id: ADR-LOOP-CADENCE-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-LOOP-CADENCE-004_heartbeat-respiration-cascade_RATIFIED.md"
    title: LOOP-CADENCE 004 — Heartbeat Respiration Cascade RATIFIED
    last_modified: "2026-07-15"
okf_version: "0.2"
---

# Famille LOOP — 5 ADR cadences et boucles (canon loop, queues, heartbeat, calendar)

## Résumé

La famille **LOOP** (5 ADR) pose les **cadences** et **boucles** du système. Elle alterne entre deux préfixes : `ADR-LOOP-NNN` (boucles) et `ADR-LOOP-CADENCE-NNN` (cadences temporelles).

## Les 5 ADR LOOP

| ADR | Sujet |
|---|---|
| `ADR-LOOP-001` | Canon Loop Verification-First |
| `ADR-LOOP-002` | Queues over Loops HITL Rightward |
| `ADR-LOOP-003` | Orient-Layer Signals Wagers |
| `ADR-LOOP-CADENCE-004` | Heartbeat Respiration Cascade (RATIFIED) |
| `ADR-LOOP-CADENCE-005` | Calendar by Design (RATIFIED) |

## ADR-LOOP-001 : Canon Loop Verification-First

La **boucle canonique** : verify → assert. Toute boucle d'agent qui affirme sans vérifier est non-canonique. C'est l'application de `ADR-META-001` (anti-paresse verify-before-assert) au domaine des boucles.

## ADR-LOOP-002 : Queues over Loops HITL Rightward

Doctrine : préférer les **queues** (files d'attente HITL) aux boucles serrées. Le HITL (Human-In-The-Loop) doit se trouver **le plus à droite possible** dans la chaîne — c'est-à-dire le plus tard possible, après que l'agent a fait son maximum de travail automatisé.

## ADR-LOOP-CADENCE-004 : Heartbeat Respiration Cascade

Le **heartbeat** est la cadence de respiration du système. Il se déclenche à intervalle régulier et vérifie l'état des agents. RATIFIED 2026-07-15.

## ADR-LOOP-CADENCE-005 : Calendar by Design

Le calendrier est un objet de design, pas une donnée brute. Le système maintient un calendrier canonique qui structure les rituels et les deadlines.

Une version `.bak` existe dans `_TRASH_2026-07-13_pre-w24-m3/` — un instantané pré-mutation qui a été sauvegardé avant une refonte.

## Statut vis-à-vis de V3

**canon** sur les 5 ADR. Aucune dépréciation.

## Le verdict de cette distillation

**canon**. La famille LOOP est le rythme du système. Elle ne se estille pas.

## Liens

- Voir aussi : `concept-famille-warmode.md` (les postures WARMODE)
- Voir aussi : `concept-trash-superseded.md` (le `.bak` de LOOP-CADENCE-005)