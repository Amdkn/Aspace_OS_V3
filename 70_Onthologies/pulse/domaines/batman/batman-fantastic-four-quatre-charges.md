---
type: Concept
title: Fantastic Four — 4 charges, 2 explicites, 2 implicites
description: La squad Fantastic Four sous Batman a 4 techniciens. Le corpus ne pose que 2 charges explicitement : MrFantastic (ProcessDesign) et HumanTorch (Incidents). InvisibleWoman et TheThing ont des charges qui ne sont pas encore explicites dans le corpus lu — c'est un trou que cet concept remonté à B3 JTBD.
tags: [batman, fantastic-four, mrfantastic, humantorch, invisiblewoman, thething, charges, b3]
generated: { by: minimax-m3, at: 2026-08-19T03:50:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T03:50:00Z }
sources:
  - id: triplet-batman-fantastic
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 16 — Batman pairedWith fantastic-four (4 techniciens)"
    last_modified: 2026-08-17
  - id: triplet-mrfantastic
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 31 — MrFantastic handledBy processdesign"
    last_modified: 2026-08-17
  - id: triplet-humantorch
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 32 — HumanTorch handledBy incidents"
    last_modified: 2026-08-17
  - id: vp-agent-batman
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_AGENT.md"
    title: VP_AGENT Batman — source des 4 noms
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Fantastic Four — 4 charges, 2 explicites, 2 implicites

## Le périmètre de la squad

Triplet 16, mot pour mot :
> *« Batman (VP B2 domaine 2 — Opérations en Loops) commande le squad
> Fantastic Four (4 techniciens : MrFantastic, InvisibleWoman,
> HumanTorch, TheThing). »*

Quatre techniciens. Le mapping canonique 8-domain dit *« ~4 »* dans
la colonne Agent count du `fifty-three-b3-agent-roster.md` — le
nombre 4 est confirmé. Mais **seules 2 charges sont explicitement
posées** par des triplets (31 et 32). Les 2 autres (InvisibleWoman,
TheThing) sont des trous que la doctrine B2 → B3 ne peut pas combler
(triplet 41 — *« B3 a l'interdit de combler un trou »*) et que le
catalogue Batman ne peut pas non plus trancher (Batman remonte des
faits, pas des décisions — triplet 56).

## Charge 1 — MrFantastic, ProcessDesign

Triplet 31 :
> *« MrFantastic (B3 squad Fantastic Four, sous Batman) tient la
> charge ProcessDesign : conçoit la boucle, décide de sa forme et de
> son point d'entrée. »*

C'est la charge la plus proche de la racine du domaine. MrFantastic
est celui qui **conçoit** la boucle avant qu'elle tourne. C'est
lui qui pose la condition d'arrêt (parfois), qui définit le point
d'entrée, qui ouvre le runbook dans `SOP/` ou équivalent.

**Domaine de responsabilité** :
- Concevoir la procédure avant qu'elle soit exécutée.
- Décider de la forme (runbook, escalation matrix, support flow).
- Décider du point d'entrée (première étape du runbook).
- Poser la condition d'arrêt **en collaboration** avec Batman (qui
  la valide au niveau B2 — c'est un fait, pas une décision, mais le
  fait doit être conforme au veto catalogue).

**Pair-check couvert** : #2 Sales → Ops (une boucle Ops commence
quand une promesse Sales arrive ; MrFantastic conçoit la boucle).
**Rôle RACI** : Responsible sur le pair-check #2.

**Cycle** : 5 scrums par semaine (triplet 11), une action exécutable
par jour. Chaque scrum ouvre sur une étape du runbook.

## Charge 2 — HumanTorch, Incidents

Triplet 32 :
> *« HumanTorch (B3 squad Fantastic Four) tient la charge Incidents :
> prend l'incident, décide de l'escalade et du retour à la normale. »*

C'est la charge la plus visible — c'est l'allumage. HumanTorch est
celui qui **prend** l'incident au moment où il se déclenche (le
ticket support, l'alerte monitoring, la panne). Il décide **quand**
escalader (au-delà d'un seuil) et **comment** revenir à la normale.

**Domaine de responsabilité** :
- Prendre l'incident dès qu'il se signale.
- Décider de l'escalade — soit vers Batman (B2 sponsor), soit vers
  Cyborg si l'incident est système, soit vers Flash si l'incident
  est un défaut d'artefact.
- Décider du retour à la normale — y compris quand l'incident est
  trop profond et qu'il faut une feature pour le résoudre (handoff
  Flash → Cyborg → Ops).

**Pair-check couvert** : #3 Product → Ops (un incident Ops révèle
souvent qu'une feature mergée n'a pas de runbook ; HumanTorch le voit,
Batman arbitre avec Flash).
**Rôle RACI** : Responsible sur le pair-check #3.

**Cycle** : 5 scrums par semaine, mais avec une **astreinte**
implicite — les incidents ne respectent pas le calendrier. C'est un
fait non explicité dans le corpus : le triplet 32 ne dit pas si
HumanTorch est de garde 24/7 ou pas. **Trou à signaler.**

## Charges 3 et 4 — InvisibleWoman et TheThing (trous explicites)

Le triplet 16 nomme les 4 agents. Aucun triplet 33+ ne pose la
charge de InvisibleWoman ni de TheThing. C'est un **trou de canon**
que la doctrine B2 → B3 ne peut pas combler :

- Le triplet 41 interdit à B3 de combler un trou du sprint en
  silence. Symétriquement, Batman ne peut pas trancher la charge
  d'un B3 sans mandat explicite.
- Le triplet 56 dit que Batman remonte des **faits**, pas des
  décisions. Poser la charge d'InvisibleWoman ou TheThing, c'est
  décider — c'est Summers (B1) qui peut le faire, ou Green Lantern
  (B2 People) si c'est un choix de staffing.

### Hypothèses (non canoniques)

À partir du nom Marvel et du périmètre Ops, deux hypothèses
**non-canoniques** sur les 2 charges manquantes :

- **InvisibleWoman** — Force Fields, protection,屏障. Hypothèse : *
  SOP Maintenance / Documentation Ops* — tenir la propreté des
  runbooks, archival, gouvernance documentaire Ops.
- **TheThing** — Force brute, endurance, roc. Hypothèse : *Charge
  Ops de masse* — onboarding de cohortes, support de volume, le roc
  sur lequel l'Ops s'appuie quand la charge explose.

**Ces hypothèses ne sont pas canoniques.** Le corpus lu ne pose
aucune des deux. Elles sont posées ici **comme signal à B3
JTBD** : Batman peut ouvrir un arbitrage *« charges 3 et 4 non
posées »* au prochain B2 Council, et demander à Green Lantern de
trancher (People est le B2 qui peut poser un owner, pas Batman).

## Le risque si les 2 charges restent implicites

Si Batman délègue à MrFantastic + HumanTorch seulement, **2 B3 sur 4
portent toute la charge** — la moitié de la squad est en
sous-utilisation, l'autre moitié en surcharge. C'est un red flag #3
*Sales green, Ops/People red* — la charge Ops est portée par trop
peu d'agents, la livraison devient fragile.

**Remède** : Batman remonte le fait *« 2 charges non posées, risque
de surcharge MrFantastic+HumanTorch »* à Summers via le B2 Council.
Summers tranche, en lien avec Green Lantern (People).

## Anti-pièges

- **Inférer les charges 3 et 4 sans escalader.** Poser la charge
  d'InvisibleWoman *« parce que c'est ce que son nom Marvel suggère »*
  est une décision Batman. Ce n'est pas son rôle — il remonte le
  fait et laisse Summers trancher.
- **Confondre MrFantastic et HumanTorch.** MrFantastic **conçoit** la
  boucle ; HumanTorch **prend** l'incident. La différence est dans le
  temps — ProcessDesign est en amont (avant que la boucle tourne),
  Incidents est en aval (quand la boucle dérape).
- **Traiter HumanTorch comme un pompier 24/7.** Le corpus ne dit
  pas qu'il est d'astreinte. Si c'est implicite, c'est un People
  problem (charge de travail tenable ?) — Batman signale, il ne
  statue pas.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre où s'inscrivent les charges
- [[batman-pair-checks-jtbd-fantastic-four]] — les pair-checks où MrFantastic et HumanTorch sont R
- [[batman-doctrine-remonte-fait-non-decision]] — pourquoi Batman remonte le trou des charges 3-4
- [[b2-b3-jtbd-handoff-contract]] — le contrat que Batman signe avec MrFantastic et HumanTorch

## Note de confiance

**Confirmé par machine pour 2 charges sur 4.** MrFantastic
(ProcessDesign) et HumanTorch (Incidents) sont posés verbatim. Les
charges d'InvisibleWoman et TheThing sont **non canoniques** — le
corpus lu (triplets v3, triplet 16, VP_AGENT Batman, AGENT MrFantastic)
ne les pose pas. Les hypothèses *« SOP Maintenance »* et *« Charge
Ops de masse »* sont **mon inférence** à partir du nom Marvel et du
périmètre Ops — elles sont posées ici comme signal, pas comme canon.
Le risque de surcharge 2/4 est **mon raisonnement** — il relie le
trou canonique au red flag #3 de la matrice d'harmonisation.