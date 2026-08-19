---
type: Concept
title: JohnJones — gates émis et pair-checks où Sales est Accountable / Consulted
description: JohnJones émet trois gates : SALES_READY, NEEDS_QUALIFICATION, BLOCKED_COMMITMENT. Sur les 9 pair-checks canoniques, JohnJones est Accountable (A) sur le #2 Sales→Ops, Consulted (C) sur le #1 Growth→Sales, et absent des autres. Le pattern A=aval / C=amont est systématique (cf. b2-pair-check-raci-by-rank). Red flags impliquant Sales : #2 (Growth green / Sales red) et #3 (Sales green / Ops ou People red).
tags: [b2, johnjones, sales, gates, pair-checks, raci, red-flag, sales-ready, blocked-commitment]
generated: { by: minimax-m3, at: 2026-08-19T04:10:00Z }
verified:
  - { by: process:lecture-corpus-sales, at: 2026-08-19T04:10:00Z }
sources:
  - id: avengers-wheel-gates
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — gates émis par Sales
    last_modified: 2026-08-17
  - id: harmonization-redflags
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: raci-par-rang
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — gates émis et pair-checks

## Les trois gates émis par Sales

`eight-domain-avengers-wheel.md` ligne 41 du tableau cite verbatim
les gates émis par Sales :

| Gate | Sens | Application |
|---|---|---|
| `SALES_READY` | Le domaine Sales est aligné : reformulation validée, qualification acquise, capacité de tenir la promesse | Condition suffisante pour passer Sales → Ops (pair-check #2) |
| `NEEDS_QUALIFICATION` | L'attention reçue (MQL, demande) n'est pas encore qualifiée | Signale à Growth (pair-check #1) que l'attention nécessite un travail de qualification avant d'être traitée |
| `BLOCKED_COMMITMENT` | Sales a identifié un blocker à un engagement futur (prix non calibré, delivery non tenable, claim non safe) | Bloque le passage Sales → Ops jusqu'à arbitrage Council |

**Trois observations** :

- `SALES_READY` est l'équivalent Sales de `PRODUCT_READY` ou
  `LEGAL_READY` — c'est le feu vert mésoperpétuel pour la transition
  aval.
- `NEEDS_QUALIFICATION` est **actif en amont** — Sales signale à
  Growth (pair-check #1) que l'attention reçue n'est pas encore
  qualifiable en l'état. C'est la rétroaction cross-domaine.
- `BLOCKED_COMMITMENT` correspond au red flag #2 (Growth green,
  Sales red — *« Valider l'offre avant de scaler l'attention »*),
  pas au red flag #3 (Sales green, Ops/People red). Le #3 est
  déclenché par Ops/People, pas par Sales.

## Le pattern de gates Sales

Les trois gates couvrent l'espace des états mésoperpétuels de Sales
vis-à-vis des autres domaines :

| État mésoperpétuel | Gate émis |
|---|---|
| Sales peut transférer vers Ops | `SALES_READY` |
| Sales demande à Growth de re-qualifier | `NEEDS_QUALIFICATION` |
| Sales a identifié un blocker | `BLOCKED_COMMITMENT` |

Il n'y a pas de gate `SALES_DORMANT` ou `SALES_OUT_OF_SCOPE` —
contrairement à Aquaman (Legal) qui a un état dormant canonique.
JohnJones steward un état **non-forcé** : le domaine n'écrit pas
quand il n'y a pas de matière, mais ne déclare pas de dormance.

## Pair-checks où Sales est Accountable ou Consulted

`b2-pair-check-raci-by-rank.md` tableau ligne 70-78 pose le RACI par
rang sur les 9 pair-checks. Pour Sales :

| # | Pair-check | Position Sales | Position B2 sponsor |
|---|---|---|---|
| 1 | Growth → Sales | **C (Consulted)** | B2 Sales (en aval) |
| 2 | Sales → Ops | **A (Accountable)** | B2 Ops (en aval) |

**Wait — correction importante**. La règle *« A = B2 en aval »* dit
que le sponsor en aval est Accountable. Donc :

- Pair-check #1 Growth → Sales : A = **B2 Sales** (en aval), C =
  **B2 Growth** (en amont). Sales arbitre si l'attention devient
  opportunité qualifiée.
- Pair-check #2 Sales → Ops : A = **B2 Ops** (en aval), C = **B2
  Sales** (en amont). Sales est consulté, pas accountable.

Le RACI par rang **inverse donc** la lecture naïve du sponsor :
*Sales sponsor* (qui tient le contrat B2 → B3 côté Sales) est
**Accountable sur #1** et **Consulted sur #2**. La nuance compte.

Reformulation avec la correction :

| # | Pair-check | A (Accountable) | C (Consulted) Sales | Sponsor B3 |
|---|---|---|---|---|
| 1 | Growth → Sales | **B2 Sales** | — | B3 Illuminati |
| 2 | Sales → Ops | B2 Ops | **B2 Sales** | B3 Fantastic Four |

Conséquence concrète : quand un arbitrage #1 (Growth → Sales) tourne
mal, **B2 Sales tranche**, pas B1, pas B2 Growth. Et quand un
arbitrage #2 (Sales → Ops) tourne mal, **B2 Ops tranche**, B2 Sales
est consulté mais ne statue pas.

## Red flags impliquant Sales

`business-wheel-harmonization-matrix.md` §« Les 5 red flags » en
énonce deux qui touchent Sales directement :

### Red flag #2 — Growth green, Sales red

> *« Valider l'offre avant de scaler l'attention. »*

Lecture : le radar affiche Growth au vert (paid media marche), mais
Sales ne peut pas tenir la promesse qui découle de l'attention
captée. La pression naturelle est de scaler l'attention (elle
marche), mais sans qualification Sales le pipeline se remplit de
demandes intenables. La sanction est un **arrêt dur** : valider
l'offre (la reformulation-validée, scope, prix) avant de continuer
à scaler.

Le gate `BLOCKED_COMMITMENT` est l'expression mésoperpétuelle de ce
red flag.

### Red flag #3 — Sales green, Ops/People red

> *« Risque de charge de livraison — la promesse ne pourra pas être
> tenue. »*

Lecture : Sales a signé (reformulation validée, opportunité
qualifiée, scope clair), mais Ops n'a pas la capacité de tenir la
livraison ou People n'a pas l'effectif pour la charge. La pression
naturelle est de pousser la signature (elle est gagnée), mais sans
capacité aval la promesse explose en rétention. La sanction est
aussi un **arrêt dur**.

Pour Sales, ce red flag est **passif** — Sales n'est pas la cause
du blocage, mais Sales déclenche le blocage en signant quand
l'aval n'est pas prêt. Le packet mésoperpétuel doit documenter
l'absence de validation aval **avant** la signature.

## Position de Sales dans la matrice d'harmonisation

Sur les 9 pair-checks canoniques (`b2-harmonization-matrix-exploitable.md`
§« Les 9 critères — forme tabulaire ») :

| # | Critère (transition) | Position Sales |
|---|---|---|
| 1 | Growth → Sales | **A** |
| 2 | Sales → Ops | **C** (en amont) |
| 3 | Product → Ops | absent |
| 4 | Product → IT | absent |
| 5 | Finance → Growth | absent |
| 6 | Finance → Product | absent |
| 7 | Legal → Growth | absent |
| 8 | Legal → Product | absent |
| 9 | People → Tous | **C** (transverse, tous concernés) |

Sales est **directement présent** sur 2 pair-checks (#1 A, #2 C)
et **transverse** sur 1 (#9 C). Sur les 6 autres, Sales est
**Informed** (I) — il voit passer les décisions sans les piloter.

C'est une position **étroite mais profonde** : Sales pilote une
transition (Growth → Sales) et consulte sur une autre (Sales →
Ops), mais ne touche pas aux autres. Comparaison :

- Batman (Ops) est A sur #2 #3, C sur #4, transverse sur #9.
- Wonder Woman (Finance) est C sur #5 #6.
- Aquaman (Legal) est C sur #7 #8.
- JohnJones (Sales) est A sur #1, C sur #2, C sur #9.

Trois capitaines concentrés sur 2 pair-checks directs, Batman et
Wonder Woman un cran plus haut, Aquaman un cran plus bas.

## Anti-pièges

- **Confondre gate mésoperpétuel et état B3.** `SALES_READY` est
  mésoperpétuel (decision Council), pas un état B3 (livraison
  tactique). Le B3 squad Illuminati a ses propres indicateurs
  (`SCRUMS.md` validé, etc.) qui ne se confondent pas avec les gates
  B2.
- **Émettre `SALES_READY` sans `CLIENT_VALIDATION_*.md`.** Le gate
  mésoperpétuel doit refléter un sprint tenu (cf. `SPRINTS.md`
  Sprint 3 — fichier `CLIENT_VALIDATION_01.md` présent avec
  reformulation + preuve de validation). Un gate sans fichier de
  validation est un voeu, pas un état.
- **Scaler l'attention sur Growth green quand Sales est red** (red
  flag #2). Le radar affiche Growth au vert, mais le red flag
  bloque. La pression commerciale est de scaler quand même — c'est
  précisément ce que le red flag empêche.
- **Signer quand Ops ou People est red** (red flag #3). Sales signe
  une opportunité qualifiée, mais l'aval ne tient pas. La sanction
  est un arrêt dur.
- **Prendre A sur #2 (Sales → Ops).** Le RACI par rang donne A à
  B2 Ops, pas à B2 Sales. Une lecture naïve du *« sponsor de la
  transition »* peut faire croire à Sales qu'il est A ; c'est B2
  Ops.

## Liens

- [[b2-pair-check-raci-by-rank]] — la matrice RACI par rang
- [[b2-harmonization-matrix-exploitable]] — 9 pair-checks et 5 red flags
- [[b2-council-arbitrage-rule]] — qui tient le Council quand un red flag s'oppose
- [[johnjones-domaine-sales-perimetre]] — le périmètre qui légitime les gates
- [[johnjones-veto-reformulation-validee]] — veto qui sous-tend `BLOCKED_COMMITMENT`
- [[eight-domain-avengers-wheel]] — le mapping des gates

## Note de confiance

**Confirmé par machine.** Les 3 gates (`SALES_READY`,
`NEEDS_QUALIFICATION`, `BLOCKED_COMMITMENT`) tirés verbatim de
`eight-domain-avengers-wheel.md`. Les 2 red flags (#2, #3) tirés
verbatim de `business-wheel-harmonization-matrix.md`. La
distribution RACI par rang (Sales A sur #1, C sur #2) tirée verbatim
de `b2-pair-check-raci-by-rank.md`. La reformulation du RACI
(correction sponsor = aval) est une **précision** dérivée du
document RACI lui-même, qui dit *« A est toujours le B2 captain en
aval de la transition »*. La position transverse #9 (Sales C) est
**projetée** — People → Tous fait de tout capitaine un C
transverse, pas explicitement nommé pour Sales dans le corpus.