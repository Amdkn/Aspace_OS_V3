---
type: Concept
title: ZORA state lifecycle — GREEN/YELLOW/RED
description: Cycle de vie de l'état ZORA Discovery : chaque LD traverse GREEN (OK) → YELLOW (charge élevée) → RED (HARD SAFETY ou 1-turn escalation). load_signal (low/medium/high/critical) module l'intensité. beth_action conditionne le routage Morty.
tags: [zora-state, green-yellow-red, load-signal, beth-action, escalation]
generated: { by: minimax-m3, at: 2026-08-19T04:16:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:16:00Z }
sources:
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — ZORA state output
    last_modified: 2026-06-21
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — 5 états
    last_modified: 2026-05-20
okf_version: "0.2"
---

# ZORA state lifecycle — GREEN/YELLOW/RED

## Énoncé canon

Chaque LD traverse 3 états ZORA :
- **GREEN** — Evidence OK, santé/cognition/priorité cohérente. Routage Morty standard.
- **YELLOW** — Charge élevée, surveillance accrue. Morty draft seulement.
- **RED** — Dégradation détectée. **HARD SAFETY** (LD03/LD04) ou **1-turn escalation** Beth (LD05/LD06/LD08).

## load_signal (intensité)

| Valeur | Sens |
|---|---|
| `low` | LD sous bande passante safe |
| `medium` | LD dans la zone cible |
| `high` | LD saturé, surveillance accrue |
| `critical` | LD consomme plus que la bande passante safe → **escalade Discovery + Beth** (Book LD01 spec) |

## beth_action (5 valeurs)

| Valeur | Action |
|---|---|
| `none` | Pas d'action Beth |
| `review` | Revue Beth requise |
| `veto` | Veto Beth — HALT execution |
| `recovery_first` | **HARD SAFETY LD03/LD04 RED** — recovery avant routage |

## morty_route (6 ships)

`ORVILLE_IKIGAI | SNW_12WY | ENTERPRISE_PARA | CERRITOS_GTD | PROTOSTAR_DEAL | DISCOVERY_ZORA` (auto-route).

## Cycle de vie

```
GREEN ──[charge augmente]──→ YELLOW ──[charge dépasse seuil]──→ RED
   ↑                                                              ↓
   └────────────[recovery Beth + beth_action = none]──────────────�
```

Pour LD03 et LD04 spécifiquement :
- **GREEN → YELLOW** : `recovery_signal: strained` OU `cognitive_load: heavy`
- **YELLOW → RED** : seuil chiffré franchi (LD03 < 4.0, LD04 < 3.5)
- **RED → GREEN** : `beth_action = recovery_first` → recovery signal validé → retour

Pour LD05/LD06/LD08 :
- **YELLOW → RED** : isolation RED / bond fracture RED / negative-reach RED
- **1-turn escalation** = Beth escalade **immédiatement** (pas 5 min)

## Cas spéciaux

| LD | GREEN → YELLOW | YELLOW → RED | RED → GREEN |
|---|---|---|---|
| LD03 Culber | recovery_signal = strained | LD03 < 4.0 (HALT_LD03) | recovery_signal = sufficient |
| LD04 Tilly | cognitive_load = heavy | LD04 < 3.5 (HALT_LD04) | clarity_signal = clear |
| LD05 Stamets | network_signal = neutral | isolation RED | network_signal = nourishing |
| LD06 Burnham | presence_signal = thin | bond fracture RED | presence_signal = present |
| LD08 Georgiou | impact_signal = unclear | negative-reach RED | impact_signal = real |

## Verdict distillation

`canon` — fait autorité. Source canonique `A2_Discovery_ZORA_Spec.md` (output format) + `A1_Beth_Spec.md` (5 états).

## Pièges documentés

- **Piège 1** : escalader A0 sur RED sans avoir traversé Beth d'abord. **Viole veto distribué**.
- **Piège 2** : LD03/LD04 RED routé vers Morty avant recovery_first. **Viole HARD SAFETY**.
- **Piège 3** : load_signal = critical sans escalade Discovery + Beth. **Viole Book LD01 boundary**.
