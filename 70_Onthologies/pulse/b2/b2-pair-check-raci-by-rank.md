---
type: Concept
title: RACI par rang sur les 9 pair-checks — qui est Accountable quand deux domaines se croisent
description: Le rapport tour 2 a refusé un RACI par pair-check comme trop spéculatif. Lu en intégralité, le triplet v3 (7, 8, 13, 41, 56, 57) ancre un RACI par rang (B1/B2/B3), pas par personne. Pour chaque transition, B2 en aval est Accountable, B2 en amont est Consulted, B1 est Informed, B3 est Responsible. Le RACI par rang est plus court à tenir qu'un RACI par personne, et ne dérive pas quand un capitaine change.
tags: [b2, raci, rang, pair-check, accountabilite, escalation, dependance]
generated: { by: minimax-m3, at: 2026-08-19T03:10:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T03:10:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplet-b2-sprints-only
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 7 — B2 produit SPRINTS.md et rien d'autre, interdit rock et scrum"
    last_modified: 2026-08-17
  - id: triplet-b3-scrums-only
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 8 — B3 produit SCRUMS.md et rien d'autre, interdit rock et sprint"
    last_modified: 2026-08-17
  - id: triplet-b3-depends-b2-sprint
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 13 — B3 dependsOn B2-sprint"
    last_modified: 2026-08-17
  - id: triplet-b3-interdit-trou
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: triplet-batman-veto-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait"
    last_modified: 2026-08-17
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
okf_version: "0.2"
---

# RACI par rang sur les 9 pair-checks

## Pourquoi par rang, pas par personne

Le rapport tour 2 a refusé un RACI par pair-check comme **trop spéculatif** :
*« Pour chacun des 9 pair-checks, qui est Accountable, Responsible, Consulted, Informed. La matrice d'harmonisation pose les transitions mais pas les owners. Refusé — c'est une projection depuis le framework RACI projet-management, pas une source canonique. »*

La projection reste vraie **par personne** — Superman est Accountable sur Growth×Sales ? C'est un raccourci rhétorique, pas un fait canonique. Mais elle devient défendable **par rang** quand on lit les triplets 7, 8, 13, 41, 56, 57 :

- Le triplet 7 dit *« B2 produit SPRINTS.md et rien d'autre, interdit rock et scrum »* — le rang B2 a un mandat **sprint**, pas un mandat d'exécution.
- Le triplet 8 dit *« B3 produit SCRUMS.md et rien d'autre, interdit rock et sprint »* — le rang B3 a un mandat **scrum** (exécution quotidienne), pas un mandat d'arbitrage.
- Le triplet 13 dit *« B3 dependsOn B2-sprint »* — la dépendance va de B3 vers B2, pas l'inverse. B3 ne peut pas initier une transition.
- Le triplet 41 dit *« B3 interdit-combler-trou »* — B3 signale, ne décide pas. C'est Responsible, pas Accountable.
- Les triplets 56 et 57 disent *« Batman remonte à Summers des faits, pas des décisions »* et *« Batman veto remonte à Summers comme un fait »* — le rang B2 sponsor d'une transition ne tranche pas l'arbitrage final, il porte le fait. Accountable n'est pas B2 seul.

Le rang B1 (Summers) reste Accountable final sur le North Star — il tranche les conflits que B2 ne peut pas résoudre. C'est la position **Informed** sur l'opérationnel, **Accountable** sur la cohérence cycle.

## Le tableau par rang

| # | Pair-check | A (Accountable) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|---|
| 1 | Growth → Sales | B2 Sales | B3 Illuminati | B2 Growth | B1, B3 Guardians |
| 2 | Sales → Ops | B2 Ops | B3 Fantastic Four | B2 Sales | B1, B3 Illuminati |
| 3 | Product → Ops | B2 Ops | B3 Fantastic Four | B2 Product | B1, B3 Avengers |
| 4 | Product → IT | B2 IT | B3 Kang Dynasty | B2 Product | B1, B3 Avengers |
| 5 | Finance → Growth | B2 Growth | B3 Guardians | B2 Finance | B1, B3 Thunderbolts |
| 6 | Finance → Product | B2 Product | B3 Avengers | B2 Finance | B1, B3 Thunderbolts |
| 7 | Legal → Growth | B2 Growth | B3 Guardians | B2 Legal | B1, B3 Eternals |
| 8 | Legal → Product | B2 Product | B3 Avengers | B2 Legal | B1, B3 Eternals |
| 9 | People → Tous | B2 captain du domaine impacté | B3 squad du domaine impacté | B2 People | B1, B3 X-Men (transverse) |

**Règle de lecture** : A est **toujours le B2 captain en aval de la transition** (le domaine qui reçoit). C'est la position `b2-b3-jtbd-handoff-contract.md` §« Le rôle du capitaine B2 sponsor » qui devient une matrice systématique, pas un cas par cas.

## Pourquoi A = B2 en aval, pas B1

L'escalade à B1 est une **exception**, pas le mode normal. La doctrine fractal §« L'escalier d'escalade (canonique) » dit *« on ne saute jamais un échelon, sauf emergency triggers explicites »*. Si B1 était A sur chaque pair-check, l'escalier canonique s'inverserait — B1 serait le pass-through obligé, pas l'arbitre final. Le rang B2 en aval porte l'opérationnel de la transition, c'est lui qui sait si la transition tient.

Trois exceptions qui retournent A à B1 :

1. **Conflit de North Star** — deux mandates B1 simultanés exigent des wheel-states incompatibles. A bascule à B1.
2. **Violation de cycle** — un arbitrage exige de dépasser le 12WY courant. A bascule à B1.
3. **Boundary non-négociable tierce** — un veto catalogue (cf. `b2-eight-domain-vetoes-catalogue.md`) s'oppose à un mandate B1 lui-même. A bascule à B1.

Ces trois exceptions sont citées verbatim dans `b2-council-arbitrage-rule.md` §« Quand le Council escalade à B1 ».

## Pourquoi R = B3, pas B2

Le triplet 41 dit *« B3 a l'interdit de combler lui-même un trou du sprint — il le signale à son VP au lieu de laisser le défaut invisible »*. B3 est Responsible au sens **d'exécution opérationnelle du transfert** : c'est le squad qui produit la sortie du domaine en amont et la passe au domaine en aval. Mais B3 n'est pas Accountable — il porte la responsabilité d'**exécuter la transition**, pas de **statuer sur sa cohérence**.

Conséquence concrète : un B3 qui détecte un trou dans le pair-check signale au B2 captain sponsor (en aval) et au B2 captain en amont. Le B2 sponsor arbitre. Si B2 sponsor ne peut pas trancher (handoff ou negotiation), ça remonte au B2 Council — pas à B3, pas à B1.

## Le cas People → Tous

People (Green Lantern) est l'unique pair-check où B2 People **n'est pas A** — A est le B2 captain du domaine impacté. C'est la position **transverse** de People (cf. `eight-domain-avengers-wheel.md` §« Le coordinateur transverse — People ») : People coordonne, ne statue pas. Le rang B2 People est Consulted sur tous les pair-checks, Accountable uniquement sur les pair-checks qui touchent directement People (ex : People → People sur la rotation d'un owner, mais ce n'est pas un pair-check canonique).

C (Consulted) sur le pair-check #9 est **toujours B2 People**, parce que People est le seul domaine qui peut signaler un blocker de capacité (charge, ownership). I (Informed) inclut **toujours B3 X-Men**, parce que X-Men tient le recruiting (triplet 33) et la tech-recruiting (triplet 34) — la squad doit savoir quand un pair-check touche un poste à pourvoir.

## Le lien avec le contrat B2 → B3

`b2-b3-jtbd-handoff-contract.md` pose le contrat bilatéral. Le RACI par rang **renforce** ce contrat :

- Le B2 sponsor (A dans le tableau) signe le contrat conjointement avec le B3 squad lead (R).
- Le B2 captain en amont (C) est consulté avant la signature, pas après.
- B1 (I) voit la signature dans le journal Council, pas en direct.

La **double signature** (B2 sponsor + B3 lead) devient une propriété du rang, pas un cas par cas. C'est le RACI qui la rend systématique.

## Anti-pièges

- **RACI par personne.** Un RACI qui dit *« Superman est A sur Growth×Sales »* lie l'arbitrage à la personne. Si Superman change, le RACI perd sa valeur. Le RACI par rang survit aux changements de capitaine — seul le rang reste, le nom tourne.
- **A = B2 en aval par défaut.** Si A était toujours B2 sponsor, le RACI dirait *« B2 sponsor arbitre »*, ce qui est le contrat B2→B3. Le RACI **étend** la logique à 9 transitions, dont certaines (People → Tous) ne sont pas des handoffs sponsor/lead.
- **Escalade à B1 par défaut.** Si le RACI envoyait chaque pair-check à B1, l'escalier canonique serait inversé. B1 est Informed, pas Consulted. Le B2 sponsor arbitre l'opérationnel ; B1 arbitre la cohérence cycle et North Star.
- **B3 qui décide.** Un B3 qui lit ce RACI pourrait croire qu'il est Accountable sur l'exécution. Il est Responsible, pas Accountable. La nuance est dans le triplet 41 — combler un trou n'est pas décider d'un arbitrage.
- **People comme A transverse.** People est transverse en C, jamais en A. Le pair-check #9 (People → Tous) a A = B2 du domaine impacté, pas B2 People. People coordonne, il ne statue pas.

## Liens

- [[b2-council-arbitrage-rule]] — l'instance qui arbitre quand A ne peut pas trancher
- [[b2-harmonization-matrix-exploitable]] — les 9 pair-checks sur lesquels le RACI se déploie
- [[b2-three-cooperation-modes]] — parallel/handoff/negotiation comme lecture du RACI
- [[b2-eight-domain-vetoes-catalogue]] — les cas où un veto renverse A vers B1
- [[b2-b3-jtbd-handoff-contract]] — la double signature B2 sponsor + B3 lead
- [[b2-areas-dormants-doctrine]] — quand un capitaine en A est dormant
- [[b2-council-cadence-and-chair]] — la séance où A statut en cas d'ambiguïté
- [[b1-stop-conditions-escalier]] — les trois exceptions qui retournent A à B1

## Note de confiance

**Reconstruit, à moitié étayé.** Le RACI par rang est étayé par 6 triplets (7, 8, 13, 41, 56, 57) qui ancrent la séparation des mandats par rang et la dépendance B3 → B2. Le choix A = B2 en aval est **reconstruit** à partir du rôle B2 sponsor dans `b2-b3-jtbd-handoff-contract.md` et des trois exceptions d'escalade à B1 dans `b2-council-arbitrage-rule.md`. Le cas People → Tous est **projeté** : People comme transverse est cité dans `eight-domain-avengers-wheel.md`, mais le RACI sur les 9 pair-checks n'est pas posé ailleurs dans le corpus. La forme tabulaire (R, A, C, I) est **empruntée** au framework RACI projet-management — assumée comme projection, pas comme vérité canonique.
