---
type: Concept
title: Project Graduation Gates — Gate 0 à Gate 7
description: Huit gates séparent prototype et Business Done : Direction (B1), Market (Growth+Sales+B1), Product, Delivery (Ops), Runtime (IT), Margin (Finance), Trust (Legal), Handoff (People). Business Done exige les huit B2 d'accord ou une exception B1 documentée.
tags: [graduation, gates, b1, b2, business-done, project]
generated: { by: minimax-m3, at: 2026-08-17T21:05:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T21:05:00Z }
sources:
  - id: gates
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/10_PROJECT_GRADUATION_GATES.md"
    title: Project Graduation Gates
    last_modified: 2026-05-27
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
okf_version: "0.2"
---

# Project Graduation Gates — Gate 0 à Gate 7

`B1_Area_Direction/10_PROJECT_GRADUATION_GATES.md` pose un **gate ladder** à huit niveaux. La règle de promotion est sans appel : *« a project can be promoted only to the highest gate with evidence. Missing evidence must be named as a blocker, not hidden as progress. »*

## Le gate ladder

| Gate | Évidence requise | Décision owner |
|---|---|---|
| **Gate 0 — Direction** | North Star, intent 12WY, B2 handoff existe | B1 |
| **Gate 1 — Market** | ICP, pain, offer, validation sprint | Growth + Sales + B1 |
| **Gate 2 — Product** | Working artifact, user value, QA | Product |
| **Gate 3 — Delivery** | SOP, support path, ops runbook | Ops |
| **Gate 4 — Runtime** | repo / deploy / access / backup | IT |
| **Gate 5 — Margin** | price, cost, margin, payment path | Finance |
| **Gate 6 — Trust** | claims, privacy, IP, terms | Legal |
| **Gate 7 — Handoff** | owner map, training, no founder-only blocker | People |

Chaque gate est **possédée** par un hero-manager B2 (sauf Gate 0 et Gate 1 qui impliquent B1 directement). Le promoteur ne peut pas être le prouveur : un Product manager qui prouve son propre Product sans QA externe n'a pas passé Gate 2.

## La règle de promotion

La phrase canonique (`10_PROJECT_GRADUATION_GATES.md` §« Promotion Rule ») :

> *A project can be promoted only to the highest gate with evidence. Missing evidence must be named as a blocker, not hidden as progress.*

Trois implications opérationnelles :

1. Un projet n'est jamais « Gate 3 avec caveats ». Il est Gate 3 ou il n'est pas Gate 3 — les caveats sont des blockers à nommer.
2. La promotion se fait **par le bas** : passer Gate 2 suppose que Gate 1 est validé. On ne saute pas.
3. Le « Blocked » est un état **affichable**, pas un échec. Un projet Gate 2 Blocked-on-Gate-4 est un projet qui a besoin d'IT, pas un projet qui a échoué.

## Business Done — la définition stricte

`10_PROJECT_GRADUATION_GATES.md` §« Business Done » :

> *Business Done requires all 8 B2 domains to accept the release or to document a conscious B1 exception with a date for revisit.*

Deux voies pour sortir de l'état Project :

- **Voie 1** : les 8 domaines B2 acceptent le release (Gate 7 franchie, owners B2 signent).
- **Voie 2** : B1 documente une **exception consciente** avec une date de revisit. C'est la sortie explicite « on accepte que ce ne soit pas parfait, mais on date le retour ».

Pas de troisième voie. Un projet qui ne passe pas l'un ou l'autre **n'est pas Business Done** — il est un prototype, ou il est mort.

## Le lien avec la wheel

Le gate ladder et la wheel 8-domain sont la **même matrice** vue sous deux angles. Chaque gate = un domaine B2 ; chaque promotion = un acceptance du hero-manager B2. Les pair checks de la matrice d'harmonisation s'appliquent aussi entre gates adjacentes (par exemple Gate 2 vert et Gate 3 rouge = red flag « Product green, Ops red » = ne pas lancer).

## Le risque spécifique

Le **release « Product-only »** est le piège historique. Symptôme : Gate 2 vert, autres gates non testés, release shipé, l'équipe découvre Ops/IT/Legal non-préparés en production. La stop condition canonique (`00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md`) est explicite :

> *No Product-only release becomes **Business Done** without the B2 gate matrix.*

C'est précisément la protection que le gate ladder apporte.