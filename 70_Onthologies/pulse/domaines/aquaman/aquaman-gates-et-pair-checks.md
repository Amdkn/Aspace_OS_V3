---
type: Concept
title: Aquaman — gates émis et pair-checks où il est Consulted
description: Aquaman émet trois gates (LEGAL_READY / NEEDS_REVIEW / BLOCKED_RISK) et est Consulted sur les pair-checks #7 (Legal→Growth) et #8 (Legal→Product). Sur ces deux transitions, il n'est pas Accountable — c'est le capitaine en aval (Growth, Product) qui porte l'A. Aquaman cadre, il n'opère pas.
tags: [b2, aquaman, gates, pair-check, legal-ready, needs-review, blocked-risk, consulted]
generated: { by: minimax-m3, at: 2026-08-19T03:40:00Z }
verified:
  - { by: process:lecture-canon-aquaman, at: 2026-08-19T03:40:00Z }
sources:
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — mapping B2 → B3 et gates émis
    last_modified: 2026-08-17
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — gates émis et pair-checks

## Les trois gates émis par Aquaman

D'après `eight-domain-avengers-wheel.md` (mapping B2 → B3, ligne 08) :

| Gate | Sens | Émis quand |
|---|---|---|
| `LEGAL_READY` | Le périmètre Legal tient — claims safe, IP/privacy/terms nets, périmètre + propriété du livrable écrits. | Le packet mésoperpétuel a traité les surfaces compliance/contract/privacy/IP/claims/terms et Aquaman n'oppose pas son veto. |
| `NEEDS_REVIEW` | Un livrable touche Legal mais n'est pas encore prêt — surface à examiner. | Un B3 swarm (souvent Eternals) remonte un output qui touche un sujet Legal sans verdict final. |
| `BLOCKED_RISK` | Une exposition non gérée — risque privacy/IP/contract/claims non couvert. | Aquaman oppose son veto catalogue ou constate qu'une des 7 surfaces est en risque. |

Le triplet des gates est aligné sur les 7 surfaces du périmètre
Legal : `LEGAL_READY` ↔ toutes couvertes, `NEEDS_REVIEW` ↔ une ou
plusieurs à examiner, `BLOCKED_RISK` � une ou plusieurs en exposition
non couverte.

## Les pair-checks où Aquaman est Consulted

D'après `b2-pair-check-raci-by-rank.md`, Aquaman est Consulted (C) sur
deux pair-checks :

| # | Pair-check | A (Accountable) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|---|
| 7 | **Legal → Growth** | B2 Growth (Superman) | B3 Guardians | **B2 Legal (Aquaman)** | B1, B3 Eternals |
| 8 | **Legal → Product** | B2 Product (Flash) | B3 Avengers | **B2 Legal (Aquaman)** | B1, B3 Eternals |

Conséquence opérationnelle : **Aquaman cadre les transitions vers
Growth et Product, il ne les pilote pas.** L'arbitrage final reste
entre les mains de Superman et Flash.

## Pourquoi A = B2 en aval, pas Aquaman

Le rang B2 en aval de la transition porte l'A. C'est la lecture
systématique du RACI par rang. Pour Legal, cela donne :

- **Pair-check #7 (claims publics)** : Superman (Growth) est
  Accountable parce qu'il tient le canal de diffusion. Aquaman
  intervient en amont pour cadrer les claims (compliance, defensibility),
  mais la décision de *publier ou non* reste chez Superman. Aquaman
  n'a pas la légitimité du canal.
- **Pair-check #8 (frontières IP/privacy/terms exposés en code)** :
  Flash (Product) est Accountable parce qu'il tient la discipline de
  ship. Aquaman cadre les frontières (IP, privacy, terms), mais la
  décision de *merger ou non* reste chez Flash.

Le veto catalogue d'Aquaman peut bloquer la transition — c'est
l'`emergency trigger` qui retourne A à B1 (cf. RACI par rang
§Exceptions). Mais par défaut, Aquaman est **Consulted, pas
Accountable**.

## Les 5 red flags où Aquaman pèse

D'après `business-wheel-harmonization-matrix.md` et
`b2-harmonization-matrix-exploitable.md`, le red flag #5 implique
directement Legal :

> **Legal red + public-facing work : geler les claims et le launch.**

C'est le seul red flag où le mot *Legal* apparaît explicitement dans
la formulation canonique. Quatre autres red flags impliquent Legal en
amont ou en aval, mais pas de manière littérale :

- **#1 Product green, Ops/IT red** — un livrable public peut触及
  Legal si IT green mais Legal red.
- **#2 Growth green, Sales red** — claims non validées peuvent
  déclencher un veto Aquaman sur la transition Growth → Sales.
- **#3 Sales green, Ops/People red** — la promesse client peut
 触及 contract risk non couvert.
- **#4 Finance red + Growth/Product green** — un budget récurrent
  sans chemin de sortie peut触及 un cadre contractuel non couvert.

## Le triplet gates ↔ veto ↔ pair-check

Les trois mécanismes se renforcent :

1. **Gate** est l'état observable — ce que le B2 captain publie sur la
   wheel.
2. **Veto** est le mécanisme d'arrêt — ce que le B2 captain oppose
   pour bloquer un démarrage.
3. **Pair-check** est la transition — ce qui passe d'un domaine à
   l'autre et où Aquaman est Consulted.

Un `BLOCKED_RISK` émis sans veto opposé n'a pas de force — un veto
opposé sans `BLOCKED_RISK` n'est pas tracé. Un veto opposé sur un
pair-check où Aquaman n'est pas Consulté est overreach (cf.
[[aquaman-veto-engagement-sans-perimetre]] §Anti-pièges).

## Anti-pièges

- **Croire qu'Aquaman pilote Legal→Growth.** Il cadre, il ne pilote
  pas. Si Superman et Aquaman divergent sur une claim, c'est Superman
  qui arbitre l'opérationnel ; Aquaman escalade en veto si le risque
  est non couvert.
- **Émettre `LEGAL_READY` sans balayer les 7 surfaces.** Une gate
  sans revue des 7 surfaces est une fiction. Le proof path B3 doit
  couvrir compliance + contract + privacy + IP + claims + terms +
  permissions.
- **Confondre `NEEDS_REVIEW` et `BLOCKED_RISK`.** `NEEDS_REVIEW` est
  un état de travail en cours — la transition peut continuer
  prudemment. `BLOCKED_RISK` est un arrêt — la transition est gelée
  jusqu'à amendement.

## Liens

- [[aquaman-domaine-legal-perimetre]] — les 7 surfaces qui
  définissent les gates
- [[aquaman-veto-engagement-sans-perimetre]] — le veto qui
  produit `BLOCKED_RISK`
- [[b2-pair-check-raci-by-rank]] — le RACI par rang complet
- [[b2-harmonization-matrix-exploitable]] — la matrice qui pose
  le red flag #5
- [[eight-domain-avengers-wheel]] — le mapping B2 → B3

## Note de confiance

**Confirmé par machine.** Les 3 gates sont tirés verbatim de
`eight-domain-avengers-wheel.md`. Le RACI sur les pair-checks #7 et #8
est confirmé par `b2-pair-check-raci-by-rank.md`. Le red flag #5 est
tiré verbatim de `business-wheel-harmonization-matrix.md`. La
distinction A = B2 en aval / C = Aquaman est reconstruite depuis le
RACI par rang — confirmée par 6 triplets (7, 8, 13, 41, 56, 57), mais
non vérifiée sur un cas réel (pas de paquet mésoperpétuel Legal
enregistré dans le corpus).
