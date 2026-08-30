---
type: Concept
title: Cycle de vie d'une procédure Ops — 5 phases de la conception à l'arrêt
description: Le rapport tour 1 a signalé un trou canonique : la durée d'une procédure Ops n'est pas posée (mensuelle, trimestrielle, 12WY ?). Le concept `batman-stop-condition-typologie-quatre-formes` a posé 4 formes de condition d'arrêt. Ce concept complète en posant un cycle de vie en 5 phases — conception, pilote, production, revue, arrêt — qui aligne la durée Ops sur le cycle 12WY de Summers et donne une grille de lecture pour chaque condition d'arrêt.
tags: [batman, ops, cycle-de-vie, procedure, 12wy, sprint, condition-arret, phases, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:58:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T05:58:00Z }
sources:
  - id: triplet-cycle-12wy
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 6 — Summers tient un cycle mensuel (12WY)"
    last_modified: 2026-08-17
  - id: triplet-sprint-hebdo
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 10 — chaque VP coupe le rock en 4 sprints hebdomadaires"
    last_modified: 2026-08-17
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque procédure sans condition d'arrêt"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: stop-condition-typologie
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-stop-condition-typologie-quatre-formes.md"
    title: Batman — typologie 4 formes canoniques de condition d'arrêt
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: Contrat B2→B3 — durée du sprint, DoD chiffré
    last_modified: 2026-08-19
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: Doctrine des domaines dormants — 3 conditions d'entrée
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cycle de vie d'une procédure Ops — 5 phases

## Le trou comblé — la durée d'une procédure Ops

Le rapport tour 1 a soulevé le **trou canonique** §5.1.7 :
*« Le rapport Batman ↔ cycle 12WY. Triplet 6 dit 'Summers tient un
cycle mensuel'. Triplet 10 dit 'chaque VP coupe le rock en 4
sprints hebdomadaires'. La durée d'une procédure Ops (mensuelle,
trimestrielle, 12WY ?) n'est pas posée. »*

Ce concept propose un **cycle de vie en 5 phases** qui répond à ce
trou en alignant la procédure Ops sur le cycle 12WY de Summers :

| Phase | Durée typique | Livrable | Owner B3 |
|---|---|---|---|
| **1. Conception** | 1 sprint (1 semaine) | Runbook + condition d'arrêt signée | MrFantastic (ProcessDesign) |
| **2. Pilote** | 1-2 sprints (1-2 semaines) | Boucle testée sur 1 client / 1 cohorte | HumanTorch (Incidents) + InvisibleWoman |
| **3. Production** | 4-12 sprints (1-3 mois) | Boucle tenue au DoD signé | Fantastic Four (équipe) |
| **4. Revue** | 1 sprint (1 semaine) | Bilan + décision arrêt / prolongation / refonte | MrFantastic + Batman |
| **5. Arrêt** | 1 sprint (1 semaine) | Handoff sortant + archivage | HumanTorch (Incidents) + TheThing |

**Durée totale** : 8-17 sprints (2-4 mois), selon la complexité de
la procédure et la longueur de la phase de production.

## Phase 1 — Conception (1 sprint)

**Objectif** : poser la procédure sous forme de runbook avec une
condition d'arrêt écrite.

**Inputs** :
- Un **besoin** remonté par un autre domaine (Sales signe un deal,
  Product livre une feature, etc.) ou par People (rotation d'un
  owner).
- Une **doctrine** de référence (catalogue 8 vetos, matrice
  d'harmonisation).

**Outputs** :
- Un **runbook** au format standard (à définir dans le concept
  `batman-fantastic-four-quatre-charges`).
- Une **condition d'arrêt** sous l'une des 4 formes canoniques
  (date+métrique, événement+métrique, owner+escalade,
  réversibilité — cf. `batman-stop-condition-typologie-quatre-formes.md`).

**Owner** : MrFantastic (ProcessDesign) conçoit, Batman valide au
niveau B2. Le B3 squad lead (MrFantastic) tient le contrat B2 → B3
(cf. `b2-b3-jtbd-handoff-contract.md`) avec Batman.

**Condition d'arrêt posée à la conception** : la condition d'arrêt
est l'**output principal** de cette phase. Sans condition d'arrêt
écrite, la procédure ne peut pas passer en phase 2 — c'est
l'application directe du veto Batman (triplet 24).

## Phase 2 — Pilote (1-2 sprints)

**Objectif** : tester la boucle sur un périmètre réduit avant de
la généraliser.

**Inputs** : runbook + condition d'arrêt validés en phase 1.

**Outputs** :
- Un **bilan de pilote** : la boucle a-t-elle tenu au DoD signé ?
  La condition d'arrêt s'est-elle déclenchée correctement ? Les
  incidents ont-ils été résolus dans le SLA ?
- Une **décision go / no-go** pour la phase 3.

**Owner** : HumanTorch (Incidents) porte le feu opérationnel,
InvisibleWoman (si chargée) porte la coordination transverse. Batman
supervise au niveau B2, sans opérer.

**Pourquoi un pilote** : le DoD signé en phase 1 est une ** promesse
théorique**. Le pilote teste la **capacité réelle** de la boucle à
tenir. Si le pilote échoue (DoD non tenu, condition d'arrêt
déclenchée trop tôt, incidents non résolus), la procédure retourne
en phase 1 pour refonte.

## Phase 3 — Production (4-12 sprints)

**Objectif** : tenir la boucle au DoD signé, en production, sur le
périmètre complet.

**Inputs** : bilan de pilote positif (go pour la phase 3).

**Outputs** :
- Une **boucle tenue** au DoD signé (par exemple : onboarding sous
  5 jours, support sous 24h, NPS ≥ 40).
- Des **indicateurs de tenue** : lead indicators (tickets ouverts,
  temps de résolution, taux d'incident) et lag indicators
  (rétention, NPS, marge).

**Owner** : la **squad Fantastic Four** au complet, avec un **squad
lead** tournant selon la nature de la procédure (MrFantastic pour
ProcessDesign, HumanTorch pour Incidents, InvisibleWoman pour
Coordination, TheThing pour résilience). Batman arbitre les
escalades au niveau B2.

**Pourquoi 4-12 sprints** : le minimum 4 sprints correspond à un
**cycle 12WY** (4 sprints = 1 mois = 1/3 de trimestre 12WY). Le
maximum 12 sprints correspond à un **trimestre 12WY** complet. La
plage 4-12 laisse une marge pour les procédures courtes (4 sprints)
et longues (12 sprints).

**Condition d'arrêt en production** : la condition d'arrêt peut se
déclencher **pendant** la phase 3 (date atteinte, métrique franchie,
owner manquant, réversibilité activée). Le déclenchement passe la
procédure en phase 5 (arrêt) sans repasser par la phase 4 (revue).

## Phase 4 — Revue (1 sprint)

**Objectif** : bilan complet de la procédure avant décision
d'arrêter, prolonger, ou refondre.

**Inputs** : boucle en production depuis au moins 4 sprints.

**Outputs** :
- Un **bilan de revue** : la boucle a-t-elle tenu son DoD ? La
  condition d'arrêt a-t-elle été appropriée ? La squad a-t-elle
  été en charge tenable ? Le run cost a-t-elle été soutenable ?
- Une **décision tri-issues** :
  - **Arrêt** — la procédure a vécu, on passe en phase 5.
  - **Prolongation** — la procédure continue en phase 3 pour
    N sprints supplémentaires, avec éventuellement un DoD ajusté.
  - **Refonte** — la procédure retourne en phase 1 pour une
    nouvelle version.

**Owner** : MrFantastic (ProcessDesign) + Batman (B2). La revue
est un acte B2, pas un acte B3 — Batman co-signe le bilan.

**Cadence** : la revue n'est pas **calendaire** (pas tous les 4
sprints), elle est **événementielle** (déclenchée par la fin de
la phase 3, par un signal de dérive, ou par un déclencheur externe
comme un pivot B1). Si une procédure est en phase 3 depuis 12
sprints sans revue, Batman signale le fait à Summers — la
procédure **dérive** dans le cycle.

## Phase 5 — Arrêt (1 sprint)

**Objectif** : arrêter proprement la procédure, avec handoff des
clients / owners en cours.

**Inputs** : décision d'arrêt (depuis phase 4, ou déclenchement
de la condition d'arrêt en phase 3).

**Outputs** :
- Un **handoff sortant** : les clients / owners en cours sont
  transférés vers une autre procédure (existante ou nouvelle).
- Un **archivage** : le runbook, le bilan, les indicateurs sont
  archivés pour traçabilité.
- Une **décision de dormance** : la procédure est-elle dormante
  (réactivable) ou supprimée (archivage seul) ?

**Owner** : HumanTorch (Incidents) porte l'exécution de l'arrêt,
TheThing porte la résilience (pas de coupure brutale). Batman
supervise au niveau B2.

**Pourquoi 1 sprint** : l'arrêt est **chirurgical** — il faut
transférer les charges en cours sans interruption de service. 1
sprint (1 semaine) est le minimum pour un handoff propre.

## Le mapping avec le cycle 12WY de Summers

Le triplet 6 dit *« Summers tient un cycle mensuel »*. Le triplet
10 dit *« chaque VP coupe le rock en 4 sprints hebdomadaires »*.
Le cycle de vie 5 phases s'aligne ainsi :

| Phase cycle vie | Sprint 12WY | Sprint annuel |
|---|---|---|
| 1. Conception | 1 sprint (1/4 de rock) | ~5% |
| 2. Pilote | 1-2 sprints (1/4 à 1/2 rock) | ~5-10% |
| 3. Production | 4-12 sprints (1-3 rocks) | ~25-75% |
| 4. Revue | 1 sprint (1/4 de rock) | ~5% |
| 5. Arrêt | 1 sprint (1/4 de rock) | ~5% |

**Implication** : une procédure Ops qui dure 12 sprints en phase
3 consomme **3 rocks entiers** d'un trimestre 12WY. C'est le
maximum — au-delà, Batman signale que la procédure est
**structurellement lourde** et qu'elle devrait être découpée.

## La dormance — quand une procédure s'arrête sans disparaître

Le concept `b2-areas-dormants-doctrine.md` pose 3 conditions d'entrée
en dormance pour un domaine B2. Le cycle de vie 5 phases s'aligne
sur la **dormance de procédure** (pas de domaine) : une procédure
arrêtée peut être **dormante** (runbook archivé, réactivation
possible) ou **supprimée** (runbook supprimé, réactivation
impossible).

**Trois indicateurs de dormance** :

1. **Réversibilité** — la condition d'arrêt est de forme
   réversibilité (cf. typologie 4 formes). La procédure est
   dormante par design.
2. **Pas de clients en cours** — phase 5 terminée sans handoff
   actif. La procédure est dormante par défaut.
3. **Pas de signal de réactivation** — aucun mandate B1 ne
   demande la réactivation depuis 2 cycles 12WY. La dormance
   est confirmée.

**Réactivation** : un mandate B1 (ou une décision Summers) peut
réactiver une procédure dormante **sans repasser par la phase 1**
si le runbook est archivé et lisible. C'est l'intérêt de la
dormance — elle préserve l'investissement de conception.

## Anti-pièges

- **Procédure sans condition d'arrêt en phase 1.** Le veto Batman
  (triplet 24) s'applique dès la phase 1. Pas de condition
  d'arrêt = pas de passage en phase 2. C'est l'application directe
  du veto.
- **Pilote sans bilan.** Si la phase 2 se termine sans bilan écrit
  (DoD tenu ou non, condition d'arrêt déclenchée ou non), la phase
  3 ne peut pas démarrer. Le bilan est l'output contractuel de la
  phase 2.
- **Production sans indicateurs.** Si la phase 3 tourne sans
  lead/lag indicators, Batman ne peut pas superviser. La squad
  doit tenir les indicateurs, pas Batman — mais l'absence
  d'indicateurs est un signal que la squad n'est pas en charge.
- **Revue calendaire au lieu d'événementielle.** Si la revue
  est planifiée tous les 4 sprints au lieu d'être déclenchée par
  un signal, elle rate les dérives. La revue est **événementielle**
  (fin de phase 3, signal de dérive, pivot B1).
- **Arrêt brutal sans handoff.** Si la phase 5 se fait en moins
  d'1 sprint, des clients / owners en cours sont abandonnés. Le
  handoff est l'output principal de la phase 5.
- **Dormance sans réversibilité.** Si une procédure est marquée
  dormante alors que sa condition d'arrêt n'est pas réversible,
  la réactivation est impossible par design. La dormance doit
  être cohérente avec la condition d'arrêt.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre
  ProcessDesign + Incidents
- [[batman-veto-condition-arret-procedure]] — le veto qui teste
  la condition d'arrêt en phase 1
- [[batman-stop-condition-typologie-quatre-formes]] — la typologie
  qui rend la condition d'arrêt vérifiable
- [[batman-fantastic-four-quatre-charges]] — la squad qui exécute
  les 5 phases
- [[batman-launch-ready-portique-final-transverse]] — le portique
  qui s'applique au moment du lancement, pas du cycle de vie
- [[batman-couplage-superman-growth-volume-charge]] — le couplage
  volumique qui peut saturer la phase 3
- [[batman-couplage-john-jones-sales-taux-signature]] — le couplage
  signature qui peut saturer la phase 3
- [[b2-areas-dormants-doctrine]] — la doctrine de dormance
  alignée sur la phase 5
- [[b2-b3-jtbd-handoff-contract]] — le contrat B2→B3 qui signe
  chaque phase
- [[b2-pair-check-raci-by-rank]] — Batman A sur les pair-checks
  qui déclenchent les phases 1 et 5

## Note de confiance

**Confirmé par machine pour la structure sprints.** Le triplet 6
(Summers cycle mensuel) et le triplet 10 (4 sprints par rock) sont
cités verbatim. Le triplet 24 (Batman veto) est cité verbatim. Le
triplet 56 (Batman remonte-fait) est cité verbatim. La doctrine
des dormants (`b2-areas-dormants-doctrine.md`) est référencée.

**Reconstruit pour les 5 phases et le mapping 12WY.** Le découpage
en 5 phases est **mon inférence** — le canon ne pose pas un cycle
de vie explicite. Le mapping avec le 12WY est **projeté** à partir
des triplets 6 et 10 (4 sprints par rock, cycle mensuel). Les
durées par phase (1, 1-2, 4-12, 1, 1 sprint) sont **arbitraires** —
elles correspondent à la pratique sprint standard, pas à un canon.

**À arbitrer** : (1) la durée 4-12 sprints en phase 3 est-elle
adaptée à tous les types de procédures, ou faut-il une grille par
type ?, (2) la revue est-elle vraiment événementielle, ou faut-il
un minimum calendaire (tous les 4 sprints par sécurité) ?, (3) la
dormance de procédure est-elle un acte Batman seul, ou un acte
People × Ops ?, (4) la réactivation d'une procédure dormante
doit-elle repasser par la phase 1 (re-validation de la condition
d'arrêt) ou peut-elle redémarrer en phase 2 (pilote) ?. Le canon
ne tranche aucun des quatre.
