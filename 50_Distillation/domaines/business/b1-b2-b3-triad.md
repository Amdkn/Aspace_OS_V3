---
type: Concept
title: Triade B1 / B2 / B3 — direction, acceptation, exécution
description: La triade canonique de gouvernance du Business OS — B1 fixe la direction, B2 accepte le DoD, B3 exécute et prouve. Aucune des trois ne peut faire le travail d'une autre.
tags: [triade, b1, b2, b3, gouvernance, doctrine]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: B1_DIRECTION_INDEX_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/00_B1_DIRECTION_INDEX.md"
    title: B1 Direction Index — CEO's Desktop
    last_modified: "2026-06-07"
  - id: B3_SWARM_CONFIG_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B3_Warp_Core_Execution/00_B3_SWARM_CONFIG.md"
    title: B3 Warp Core Execution — 8 Squads
    last_modified: "2026-06-07"
  - id: B2_DOMAIN_CONTROL_ROOM_SALES
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Sales Control Room — CEO's Desktop
    last_modified: "2026-06-07"
  - id: ADR-FWK-021
    resource: "30_Business_OS/10_Projects/ceo-desktop/CLAUDE.md (référencé)"
    title: ADR-FWK-021 — Canon Tripartite des Blueprints
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# Triade B1 / B2 / B3 — direction, acceptation, exécution

> **Une seule chose à retenir.** Le CEO's Desktop est gouverné par une triade à trois rôles non-substituables : **B1 décide la direction, B2 accepte le DoD, B3 exécute et prouve**. Aucune couche ne fait le travail d'une autre.

## Énoncé canonique

| Rôle | Responsabilité unique                  | Output                                          |
|------|----------------------------------------|-------------------------------------------------|
| B1   | Direction (north star, cadence, arbitrage) | `01_NORTH_STAR_1Y_3Y_10Y`, `02_12WY_COMMAND_CYCLES`, `03_DECISION_CHARTER`, `04_B2_HANDOFF_QUEUE` |
| B2   | Acceptation (DoD du domaine, gates, preuves) | `B2_DOMAIN_CONTROL_ROOM` par SOB (8 dossiers) |
| B3   | Exécution (tactique, preuves, Lead/Lag)  | `B3_SWARM_CONFIG` par SOB (8 dossiers)         |

**B1 = A0.** Amadeus est le seul B1 du CEO's Desktop — c'est la propriété « The CEO is the only B1 » énoncée dans `01_NORTH_STAR_1Y_3Y_10Y.md`.

## Pourquoi cette triade

- **Anti-héroïsme.** « B2 must not rewrite B1 strategy or hide blockers from B1. B2 gives goals, constraints, and proof requirements; B3 chooses tactics. B2 reviews artifacts and metrics. » (`B2_DOMAIN_CONTROL_ROOM_Sales.md`) — la doctrine nomme explicitement la dérive à éviter.
- **Preuve requise par palier.** B3 escalate B2 **uniquement** sur : missing authority, missing inputs, cross-domain conflict, DoD ambiguity. Tout autre pas est local (`00_B3_SWARM_CONFIG.md`).
- **Anti-Babysitting Rule.** B2 ne réécrit pas la stratégie B1 ; B3 n'attend pas que B2 lui dise quoi faire tactiquement.

## Handoffs

```
B1 (A0) writes direction
       ↓
B1 creates B2 request in `04_B2_HANDOFF_QUEUE.md`
       ↓
B2 converts request into DoD packet
       ↓
B2 creates B3 jobs via JTBD spec
       ↓
B3 executes only the defined jobs and returns proof
       ↓
B2 updates gates ; B1 reviews direction drift
```

## Stop conditions

- No B2 work without a B1 handoff queue item.
- No B3 work without a B2 DoD or JTBD source.
- No domain decision is final without a decision-charter entry.
- The desktop cannot bypass Beth/Morty safety — it surfaces risk, it does not hide it.

## Ce que ce n'est pas

- Pas une cascade organisationnelle de RH. B1, B2, B3 sont des **rôles d'agents** routés par `AGENT_REGISTRY_DB`, pas des personnes.
- Pas une matrice RACI. La triade est **non-substituable** ; un B1 ne peut pas devenir B2 dans la même décision.
- Pas un rituel Scrum. Il n'y a pas de sprint ; il y a une cadence 12WY (voir concept 12-Week Year).

## Conséquence opérationnelle

Toute décision qui demande d'**exécuter du B3 sans B2 DoD**, ou de **changer de direction sans decision-charter**, casse la triade et déclenche un retour à B1. Cette règle est répétée verbatim dans la charte de décision (`03_DECISION_CHARTER.md`).
