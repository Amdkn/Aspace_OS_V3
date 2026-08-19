---
type: Concept
title: Triptyque MORTY — 12WY ⊃ PARA ⊃ DEAL
description: Architecture exécution canonique — trois couches imbriquées où la cadence (12WY) englobe la structure (PARA) quienglobe la libération (DEAL).
tags: [triptyque, morty, 12wy, para, deal, execution, architecture]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: snw-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
    title: A2 Curie SNW Spec — Triptyque MORTY
    last_modified: 2026-05-20
  - id: snw-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/README.md
    title: 23_12WY_SNW README — Cycle Q3 2026
    last_modified: 2026-06-21
  - id: protostar-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/README.md
    title: 26_DEAL_Protostar README — DEAL ⊂ PARA ⊂ 12WY
    last_modified: 2026-06-21
okf_version: "0.2"
---

# Triptyque MORTY — 12WY ⊃ PARA ⊃ DEAL

Le triptyque MORTY est l'architecture **execution** de Life OS. Il décrit l'inclusion verticale entre les trois couches opérationnelles sous le focus d'A1 Morty.

## La poupée russe

```
12WY (Curie SNW)
  └─ PARA (Enterprise Computer) — Picard/Projects, Spock/Areas, Geordi/Resources, Data/Archives
       └─ DEAL (Holo Janeway Protostar) — Dal/Define, Rok-Tahk/Eliminate, Zero/Automate, Gwyn/Liberate
```

Conséquence canon : Curie SNW est l'horloge (métronome) qui cadence la cadence hebdomadaire 50/30/20. PARA est imbriqué DANS SNW par les 5 disciplines (Pike/Una/Chapel/M'Benga/Ortegas) qui structurent Projects/Areas/Resources/Archives. DEAL est libéré opérationnellement par Data (PARA Archives).

## Discipline 50/30/20 (load rule SNW)

Le 12WY garde le cycle actif suffisamment petit pour respecter la règle de charge 50/30/20 :

- 50 % temps : exécution Rocks / Warp Core tactics.
- 30 % temps : planification / Scorecard / Time Use.
- 20 % temps : buffer / recovery / Beth HALT slots.

## Cycle Q3 2026 (mapping A3 → semaine)

| Week | Dates | Items | A3 owner principal | state stage |
|---|---|---|---|---|
| W1 | 06/15 → 07/05 | Items 1-2 | Una + Pike | `snw_planning` |
| W2 | 07/06 → 07/26 | Items 3-4 | M'Benga | `snw_focus` |
| W3 | 07/27 → 08/16 | Items 5-6 | Chapel | `snw_metrics` |
| W4 | 08/17 → 09/07 | Items 7-12 | Ortegas + Chapel | `snw_execution` |
| W13 | 09/14 | (hors Q3) | — | `13e semaine` (Item 2) |
| W0 Cycle 4 | 09/21 | (transition) | — | Semaine 0 du 4e Cycle (Item 2) |

## Cycle conformité SDD-010 §6.1

Verbatim canon : *"Aucun nouveau SDD (au-delà de SDD-010) ne peut être créé pendant 90 jours, soit jusqu'au 2026-08-11."*

**W13 = 09/14** tombe **après** expiration du veto 90j (2026-08-11) :

- Avant 2026-08-11 : focus Q3 sur PRD/ADR/DDD/TDD uniquement.
- 2026-08-11 → 2026-09-07 : window pour ratification amendments d SDD.
- W13 = 09/14 : première semaine autorisée pour nouveau SDD.

## Acceptation MORTY

- **SNW** : Every Rock has a Definition of Done. Every active tactic belongs to one active week. Every score claim maps to evidence.
- **Cerritos** : bus horizontal qui boucle les 2 triptyques (MORTY + BETH) vers B1 Fractal.
- **Protostar** : every durable blueprint is routed to Enterprise (donc ⊂ PARA ⊂ 12WY).