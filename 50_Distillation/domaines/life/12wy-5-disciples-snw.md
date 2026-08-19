---
type: Concept
title: 12 Week Year 5 disciples — SNW/Curie Execution Engine
description: Les 5 disciples canon USS SNW (Curie) : Pike Vision, Una Planning, M'Benga Focus, Chapel Metrics, Ortegas Execution. Discipline 50/30/20.
tags: [12wy, snw, curie, pike, una, mbenga, chapel, ortegas, execution, 50-30-20]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: snw-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
    title: A2 Curie SNW Spec
    last_modified: 2026-05-20
  - id: snw-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/README.md
    title: 23_12WY_SNW README — Matrice 5 disciples
    last_modified: 2026-06-21
  - id: w1-quarter-intent
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/W1_Quarter_Intent_Q3_2026.md
    title: W1 Quarter Intent Q3 2026 — Vision Pike
    last_modified: 2026-06-21
  - id: w1-item2
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/W1_Item2_13e_Semaine_Rock_Decomposition.md
    title: W1 Item 2 — Rock Decomposition 13e Semaine
    last_modified: 2026-06-21
okf_version: "0.2"
---

# 12 Week Year 5 disciples — SNW/Curie Execution Engine

12WY est le framework **execution** d'A'Space OS, géré par USS SNW (Curie) via Baserow `12WY Warp Core`. Cinq disciples structurent la cadence hebdomadaire 50/30/20.

## Les 5 disciples canon

| Disciple | 12WY discipline | Hor. canon | Ikigai pilier / horizon | Item Q3 2026 owner |
|---|---|---|---|---|
| **Pike** | Vision / Quarter Intent | H10 | Klyden (H90 héritage) ↔ Bortus (H10 stratégie) | Item 2 — Définir 09/14 = 13e semaine, 09/21 = Semaine 0 |
| **Una** | Planning / Rocks | H10 | Bortus (H10 discipline) | Items 1-2 — SOB Abdaty + 13e semaine |
| **M'Benga** | Focus / Process control | H1 | Ed (H1 craft) ↔ Gordon (H1 passion) | Items 3-4 — Auto-research IA + TOKEN frugalité |
| **Chapel** | Metrics / Scorecard | H10 | Claire (H3 vocation) + D11 Fable score | Items 5-7 — YouTube PARA + Hermes + Agent OS |
| **Ortegas** | Weekly execution / Time Use | H1 | Ed (H1 craft) + Isaac (H1 logique) | Items 8-10 — Business OS + A3 structuration + Solaris/OMK/ABC |

## Doctrine 50/30/20

La règle de charge canonique SNW :

- **50 %** : exécution Rocks / Warp Core tactics.
- **30 %** : planification / Scorecard / Time Use.
- **20 %** : buffer / recovery / Beth HALT slots.

Curie compile ; A1 Morty route.

## Cycle 12WY Q3 2026 — owner mapping

| Week | Dates | Items | A3 owner principal | state stage |
|---|---|---|---|---|
| **W1** | 06/15 → 07/05 | Items 1-2 : SOB Abdaty + 13e semaine | **Una** + **Pike** | `snw_planning` |
| **W2** | 07/06 → 07/26 | Items 3-4 : Auto-research IA + TOKEN frugalité | **M'Benga** | `snw_focus` |
| **W3** | 07/27 → 08/16 | Items 5-6 : YouTube PARA + Hermes | **Chapel** | `snw_metrics` |
| **W4** | 08/17 → 09/07 | Items 7-12 : Agent OS + Business OS + A3 + Solaris/OMK/ABC + VPS DEAL | **Ortegas** + **Chapel** | `snw_execution` |
| **W13** | 09/14 | (hors Q3 — Item 2 verrouillé) | — | `13e semaine` |
| **W0 Cycle 4** | 09/21 | (transition / buffer) | — | `Semaine 0 du 4e Cycle` |

## 13e semaine = W13 = 09/14/2026

**Définition Una** : semaine intercalée entre Q3 fin (09/07) et Cycle 4 kick-off (09/21). Sert de :

- **Buffer de transition** : consolidation Q3 livrables (W4 fin 09/07 → W13 09/14 = 1 semaine buffer).
- **Pivot canon** : ratification éventuelle amendement SDD-010 (veto 90j expire 2026-08-11) avant fin Q3.
- **Life Wheel sync** : checkpoint LD01-LD08 alignement Q3 (Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou).

**Conformité SDD-010 §6.1** : *"Aucun nouveau SDD (au-delà de SDD-010) ne peut être créé pendant 90 jours, soit jusqu'au 2026-08-11."*

W13 = 09/14 tombe **après** expiration du veto 90j → première semaine autorisée pour nouveau SDD.

## Acceptance Criteria canon

- Every Rock has a Definition of Done.
- Every active tactic belongs to one active week.
- Every score claim maps to evidence.
- Any schema/API action is explicitly approved and verified.

## Sortie Curie

```yaml
ship: SNW
a2: Curie
framework: 12WY
cycle: W1-W12|W13_META
artifact_type: quarter_intent|rock|warp_core_tactic|scorecard|time_use
status: proposed|active|blocked|done
owner_ship: SNW|CERRITOS|ENTERPRISE|PROTOSTAR
expected_proof:
  - local_path_or_baserow_row_reference
next_cli_owner: codex|claude|minimax_claude|gemini
```

## D3 nuance (à noter)

`SDD-008` mappe Tendi/Rutherford différemment (cf. concept `gtd-5-stages-cerritos.md`) ; le canon local actif garde **Rutherford = Organize + Tendi = Review**. Pour SNW, le canon `A2_Curie_SNW_Spec.md` précise que si d'anciennes archives mentionnent Uhura pour des tâches d'exécution/communication adjacentes, le contrat actif garde **Ortegas** comme owner weekly execution.