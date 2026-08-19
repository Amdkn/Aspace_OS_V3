---
type: Concept
title: B2 Handoff Queue & Decision Charter — la traçabilité B1 → B3
description: Deux artefacts qui matérialisent la triade B1/B2/B3 : la file de handoffs B1→B2 (8 lignes SOB en PENDING) et la decision charter (un schema YAML pour chaque décision de direction).
tags: [b1-b2-b3, handoff, decision-charter, traçabilité, beth, boundary-gates]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: B1_B2_HANDOFF_QUEUE_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/04_B2_HANDOFF_QUEUE.md"
    title: B2 Handoff Queue — CEO's Desktop
    last_modified: "2026-06-07"
  - id: B1_DECISION_CHARTER_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/03_DECISION_CHARTER.md"
    title: Decision Charter — CEO's Desktop
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# B2 Handoff Queue & Decision Charter — la traçabilité B1 → B3

> **Une seule chose à retenir.** La **B2 Handoff Queue** est le papier B1 → B2 (8 lignes SOB en PENDING par défaut). La **Decision Charter** est le schema YAML de toute décision de direction. Sans eux, la triade B1/B2/B3 est invisible — et invisible = invérifiable.

## B2 Handoff Queue — la file canonique

### Énoncé

> B1 (A0) writes here before B2 work begins. B2 does not invent direction; B2 translates direction into domain Rocks, gates, and tactic specs for the 8 SOB. (`04_B2_HANDOFF_QUEUE.md`)

### Les 8 lignes (toutes PENDING en Phase 1)

| Status | B2 Domain | Direction Item                                       | Why Now                                                         |
|--------|-----------|------------------------------------------------------|------------------------------------------------------------------|
| PENDING | Growth    | Name the ICP variant + first experiment velocity     | The desktop must surface Growth pulse first — leading indicator   |
| PENDING | Sales     | Define qualification + handoff to Product             | Without qualification, Growth pulse is noise                     |
| PENDING | Product   | Bound the desktop's own scope as a Product            | The desktop is not a product, but it has a Product column         |
| PENDING | Ops       | Define delivery/SOP gate for the desktop's weekly review | The weekly review must run without A0 hero-moding             |
| PENDING | IT        | Confirm runtime/access/deploy assumptions             | The desktop must open in < 2s; runtime must be sovereign          |
| PENDING | Finance   | Estimate cost-to-run for the desktop                  | Avoid hidden recurring burn on the command center                |
| PENDING | People    | Name owner/load for each of the 8 B3 squad leads      | Prevent founder-mode overload on A0                              |
| PENDING | Legal     | Review IP/terms/data boundary for the desktop         | The desktop holds business data — boundary must be explicit       |

### Règle de transition

> A row leaves **PENDING** only when the B2 domain has accepted it and produced either PASS, CONDITIONAL, or BLOCKED with an evidence path. (`04_B2_HANDOFF_QUEUE.md`)

Phase 1 close-out exige au moins 1 ligne avec un B2 manager nommé + au moins 1 ligne avec un statut Beth/Morty safety.

## Decision Charter — le schema YAML

### Énoncé

Le `03_DECISION_CHARTER.md` définit le packet schema canon pour toute décision :

```yaml
decision_id: ""
date: "2026-06-07"
scope: "ceo-desktop"
question: ""
options:
  - ""
recommendation: ""
risk_if_wrong: ""
reversibility: "high|medium|low"
boundary_gates:
  it: "GREEN|ORANGE|HALT|NA"
  finance: "GREEN|ORANGE|HALT|NA"
  legal: "GREEN|ORANGE|HALT|NA"
  people: "GREEN|ORANGE|HALT|NA"
beth_morty_status: "GREEN|ORANGE|HALT"
b2_owner: "Growth|Sales|Product|Ops|IT|Finance|People|Legal"
b3_artifact_required: true
proof_path: ""
next_review: ""
```

### Décision rights (B1 peut / B1 ne peut pas)

**B1 (A0) peut décider :**
- la direction 1Y/3Y/10Y du CEO's Desktop ;
- quel SOB reçoit le prochain handoff ;
- si un domaine passe PENDING → ACCEPTED → BLOCKED dans la handoff queue ;
- si le desktop reste shadow-active, s'active, ou se met en pause ;
- si une décision a besoin de Beth, Morty, Jerry, Picard, ou d'un 4-boundary gate.

**B1 (A0) ne peut pas :**
- exécuter du B3 directement ;
- bypass les B2 DoD gates ;
- marquer un SOB domain comme Business Done depuis Product Done seul ;
- muter provider/API/MCP/CLI config sans évidence explicite et signoff ;
- cacher un risque IT, Finance, Legal, ou People non résolu.

### Escalation

- **HALT** si Beth/Morty safety est rouge, ou si un des 4 boundary gates est HALT.
- **Escalate to Jerry** quand la décision affecte un Area standard ou l'équilibre du Life Wheel.
- **Escalate to Picard** quand la décision change un statut projet (shadow → active → paused → archived).
- **Escalate to A0 (self)** quand la décision touche l'identité, le budget, l'exposition légale, ou la direction 1Y/3Y/10Y elle-même.

## Pourquoi ces deux artefacts

- **Traçabilité = auditabilité.** Toute décision de direction est révisable, contestable, transmissible.
- **Anti-héroïsme.** B1 ne peut pas décider seul sans packet schema. Le packet force à nommer le scope, les options, le risque, la réversibilité, les boundary gates.
- **Beth/Morty status.** Chaque décision porte un statut de sécurité — HALT bloque la ratification.

## Conséquence opérationnelle

Une décision qui modifie la direction sans packet schema complet **n'est pas une décision** ; c'est un mouvement de cap. Le mouvement de cap sans packet déclenche un retour vers B1 pour cadrage.
