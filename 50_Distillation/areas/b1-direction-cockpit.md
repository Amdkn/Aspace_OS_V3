---
type: Concept
title: B1 direction cockpit — North Star, 12WY, decision charter
description: B1 possède la direction (North Star 1Y/3Y/10Y, cycles 12WY, decision charter, handoff queue, DoD/JTBD specs). Le cockpit B1 est la couche qui prend les décisions que B2 et B3 ne peuvent pas prendre sans escalader.
tags: [b1, direction, north-star, 12wy, decision-charter, handoff-queue, dod, jtbd]
generated: { by: minimax-m3, at: 2026-08-17T21:15:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T21:15:00Z }
sources:
  - id: dir-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/00_B1_DIRECTION_INDEX.md"
    title: Jerry Area Direction - LD01 Business (B1 cockpit index)
    last_modified: 2026-05-26
  - id: north-star
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
    title: North Star - J01 Jerry Prime LD01 Business
    last_modified: 2026-05-26
  - id: decision-charter
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/03_DECISION_CHARTER.md"
    title: B1 Decision Charter
    last_modified: 2026-05-31
  - id: governance
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW.md"
    title: B1 -> B2 Domain Governance Workflow
    last_modified: 2026-05-27
okf_version: "0.2"
---

# B1 direction cockpit — North Star, 12WY, decision charter

Le cockpit B1 est posé par `B1_Area_Direction/00_B1_DIRECTION_INDEX.md` et contient les six fichiers-clef d'une direction Jerry :

1. `01_NORTH_STAR_1Y_3Y_10Y.md` — direction 1 an, 3 ans, 10 ans
2. `02_12WY_COMMAND_CYCLES.md` — quatre cycles 12WY et responsabilité saisonnière
3. `03_DECISION_CHARTER.md` — droits de décision, vetos, escalation, output packet
4. `04_B2_HANDOFF_QUEUE.md` — file B1→B2 pour Rocks, gates, demandes de domaine
5. `05_B2_DEFINITION_OF_DONE_SPEC.md` — structure des packets DoD et contrat d'acceptance
6. `06_B3_JOBS_TO_BE_DONE_SPEC.md` — structure des packets JTBD B3 et contrat de preuve

L'Operating Rule est sans ambiguïté :

> *B1 owns direction and packet structure. B2 owns domain Definition of Done and gates. B3 owns execution, proof, Lead indicators, Lag indicators, and blocker reports.*

## North Star 1Y / 3Y / 10Y

`01_NORTH_STAR_1Y_3Y_10Y.md` pose trois paliers :

- **1 an** : un actif opérationnel utilisable, vendable, gouvernable — une offre claire ou un standard d'Area, un chemin de preuve opérationnel, une matrice B2 gate PASS/CONDITIONAL/BLOCKED, une trail B3 de preuves.
- **3 ans** : un système reproductible avec ownership B2 délégué, economics mesurables, documentation suffisante pour qu'un autre agent Shadow L0 continue sans ré-explication.
- **10 ans** : un actif A'Space OS compounding — licensable, teachable, auditable, portable à travers les modes Solaris/Nexus/Orbiter.

Quatre invariants directionnels sont posés :

1. B1 owns **why** and **where**.
2. B2 owns **what** must be true by domain.
3. B3 owns **how** the artifact is executed and proven.
4. Beth/Morty safety can halt expansion.
5. Product cannot graduate the business alone.

## Decision Charter — qui décide quoi

`03_DECISION_CHARTER.md` pose une matrice RACI sur 12 décision-types. Trois colonnes clés par ligne : qui owns (A/R), qui est consulted (C), qui vetoes.

Exemples saillants :

- **Intention** (ce business existe-t-il ?) : A0 Amadeus owns, jamais overridden.
- **North Star / risk appetite / 12WY cycle priority / ≤4 quarterly Rocks** : B1 owns, B1 vetoes, A0 si North Star shift.
- **Offre architecture + pricing** : B1 + Finance (Wonder Woman) co-own, Sales consulte, Finance veto sur margin.
- **IT architecture** : Cyborg (B2) owns outright — Jerry ne décide PAS IT.
- **Contract / IP / compliance** : Aquaman (B2) owns, peut veto une message publique.
- **Headcount / capsule onboarding** : Green Lantern (B2) owns, Finance consulte.

Rule of thumb : **B1 = WHY/WHERE, B2 = WHAT/gate, B3 = HOW/proof**. Un rang supérieur ne fait jamais le job d'un rang inférieur — si un B3 peut le faire, c'est un job B3.

## Les 6 vetos reconnus

1. **A0 Amadeus** — veto absolu sur Intention.
2. **B1 (Jerry/Summer)** — veto sur North Star / risk / AREA_STANDARD principle violation (ex. P6 brand damage, P4 hire sans runway 12 mois).
3. **Finance (Wonder Woman)** — veto sur deal/discount qui casse margin ou runway floor ; discount >15% requiert son sign-off.
4. **Legal (Aquaman)** — veto sur claim/contract/IP exposure qui fail compliance.
5. **B3 peer** — veto productif : quand un JTBD touche coût, legal exposure, customer promise, release quality, ou operational load, au moins un peer peut bloquer la première solution.
6. **A B2 owner** — accepte/refuse un release dans son gate.

## Les escalation thresholds

`03_DECISION_CHARTER.md` §4 liste 12 seuils. Les plus structurants :

| Signal | Seuil | Escalade |
|---|---|---|
| Rock behind | > 2 semaines | Jerry + B1 emergency session (48h) |
| MRR decline | > 5% MoM | B1 emergency (48h) |
| Runway drop | < 9 mois (alert à 6) | B1 + mitigation ; A0 si < 6 |
| Meso conflict | ≥2 B2 ne résolvent pas | B1 |
| Authority request outside mandate | any | B1 |

Chaîne canonique : B3 → (peer-unblock d'abord) → B2 owner → B1 (Jerry/Summer) → B1 gatekeepers (Rick/Morty) → A0 Amadeus. **On ne saute jamais un échelon** sauf emergency triggers explicites.

## Le B1-B2-MANDATE packet

Quand B1 mandate un B2, le packet est posé dans `04_B2_HANDOFF_QUEUE.md` au format :

```yaml
mandate_id: B1-B2-MANDATE-YYYY-NN
source_north_star: 01_NORTH_STAR_1Y_3Y_10Y.md
cycle: C1 | C2 | C3 | C4
affected_domains:
  - Growth | Sales | Product | Ops | IT | Finance | People | Legal
imbalance_type: empty_domain | overloaded_domain | blocked_gate | product_only_drift | cross_domain_conflict | missing_proof
strategic_intent: "What must become true for the business wheel to rebalance."
constraints:
  - constraint
success_signal:
  - measurable signal
b2_expected_response:
  - Rock proposal
  - DoD packet
  - meso tradeoff packet if needed
b1_decision_needed: false
```

C'est l'unité atomique de la délégation B1→B2 : intent + contraintes + success signal, **pas** un plan. B2 convertit ensuite en Rock + DoD + B3 JTBD.

## B1 intervention threshold

B1 n'intervient que si :

- ≥2 B2 ne peuvent pas résoudre un conflit meso,
- North Star / cycle priority doivent changer,
- risk appetite change,
- un domaine demande authority outside son mandate,
- la wheel 8-domain devient structurellement imbalanced.

Sinon, **B2 owns coordination, B3 owns execution**. B1 qui intervient trop souvent est un signal de B0 failure.