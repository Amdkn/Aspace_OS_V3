---
type: Concept
title: Domaine Batman — Ops / Opérations en Loops, périmètre et frontières
description: Batman est le capitaine B2 du domaine Ops (04 canonique / 02 Coach OS). Le périmètre tient sur deux axes — boucle (process, runbook, support) et exécution répétitive (delivery, onboarding, incident) — et s'arrête où commence le périmètre IT Cyborg (run système, monitoring, déploiement) et où commence People Green Lantern (ownership humain).
tags: [domaine, batman, ops, operations-en-loops, perimetre, frontiere, b2]
generated: { by: minimax-m3, at: 2026-08-19T03:30:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T03:30:00Z }
sources:
  - id: triplet-batman-dom2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 16 — Batman pairedWith Fantastic Four (domaine 2 Coach OS — Opérations en Loops)"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Ops = 04
    last_modified: 2026-08-17
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks Sales→Ops et Product→Ops
    last_modified: 2026-08-17
  - id: triplet-41
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — instance d'arbitrage mésoperpétuelle
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Domaine Batman — Ops / Opérations en Loops, périmètre et frontières

## Ce que Batman couvre

Batman tient le **domaine Ops** (04 dans le mapping canonique 8-domain,
02 dans la numérotation Coach OS). Le périmètre tient sur deux axes :

1. **La boucle** — concevoir la procédure qui fait tourner un livrable
   de manière répétitive, et poser la **condition d'arrêt** qui la
   clôt. C'est l'axe ProcessDesign : MrFantastic conçoit la boucle,
   Batman la valide au niveau B2.
2. **L'exécution répétitive** — le moment où une promesse signée (pair
   check #2 Sales → Ops) ou un artefact produit (pair check #3
   Product → Ops) doit être livré, supporté, maintenu, et un jour
   arrêté. C'est l'axe Incidents : HumanTorch porte le feu, Batman
   arbitre l'escalade au B2 Council.

Le périmètre s'exprime en quatre phrases du triplet 16 :
> Batman (VP B2 domaine 2 — Opérations en Loops) commande le squad
> Fantastic Four (4 techniciens : MrFantastic, InvisibleWoman,
> HumanTorch, TheThing).

Le nom du domaine en Coach OS — **Opérations en Loops** — est
littéral : Batman n'opère pas en cascade linéaire, il opère en
boucles (concevoir, exécuter, arrêter, ré-architecturer). C'est ce qui
le distingue d'un Product (Flash, qui livre des artefacts) ou d'un
Sales (Martian Manhunter / JohnJones, qui crée de la valeur de
relation).

## Où Batman s'arrête — les trois frontières qui tracent le périmètre

### Frontière Ops ↔ IT (Cyborg)

**L'Ops conçoit et arrête les boucles ; l'IT les fait tourner sur le
système.** Le triplet 21 confirme que Cyborg est le B2 IT — il porte
R&D et IT. La matrice d'harmonisation pose le pair-check #4 Product →
IT sur **« le produit tourne-t-il, déploie, récupère, est-il
accessible »** ; le pair-check #3 Product → Ops pose
**« l'artefact est-il supportable opérationnellement »**.

La frontière est : Ops tient **la procédure** (runbook, escalation,
condition d'arrêt), IT tient **le système** (déploiement, monitoring,
incident infra). Concrètement, un incident applicatif est Ops si la
procédure de réponse existe mais n'a pas été exécutée ; il est IT si
la procédure n'existe pas parce que le système n'a pas été conçu
pour ce cas.

**Red flag #1 de la matrice** — *Product green, Ops/IT red* —
bloque les deux à la fois. Ce n'est pas un hasard : sans Ops ni IT,
le produit ne peut pas être livré ni maintenu. Le tandem Batman +
Cyborg est ce qui ferme la porte.

### Frontière Ops ↔ People (Green Lantern)

**Ops livre la charge ; People tient l'owner.** Le pair-check #9
(People → Tous) place People en Consulted sur tous les pair-checks,
pas en Accountable. Mais Batman dépend de People sur deux points
critiques :

- La **charge de livraison** (pair check #2 Sales → Ops) tient parce
  que People a posé un owner tenable. Si l'owner People est manquant,
  la promesse Ops ne peut pas être tenue répétitivement — c'est le
  red flag #3 (Sales green, Ops/People red).
- La **rotation d'un owner Ops** (changement de MrFantastic, départ
  de HumanTorch) est un trou People que Batman ne comble pas. Le
  triplet 41 interdit au B3 de combler un trou ; le symétrique B2
  n'est pas explicite, mais Batman ne statue pas sur la People — il
  signale à Green Lantern, qui arbitre via B2 Council si l'owner ne
  vient pas.

### Frontière Ops ↔ Product (Flash) — la plus fine

Ops est **Accountable** sur le pair-check #3 (Product → Ops), donc
Batman reçoit l'artefact de Flash. Mais Batman n'**évalue** pas
l'artefact — il vérifie qu'il est **supportable** dans la boucle Ops.

Conséquence : un artefact qui ne peut pas être maintenu Ops (ex : une
feature qui exige un runbook de 40 pages par client) n'est pas un
problème Batman, c'est un signal que Flash doit revoir son design. La
frontière Ops ↔ Product se joue sur la question **« l'artefact passe-t-il
la boucle ? »** — pas sur **« l'artefact est-il bon ? »**.

## Ce que Batman ne fait PAS — quatre interdits dérivés

1. **N'écrit pas de rock.** C'est Summers (B1). Triplet 7 dit *« B2
   produit SPRINTS.md et rien d'autre, interdit rock et scrum »*.
2. **N'écrit pas de scrum.** C'est le technicien B3. Triplet 8 dit
   *« B3 produit SCRUMS.md et rien d'autre, interdit rock et sprint »*.
3. **N'arbitre pas en escalade.** Batman remonte à Summers des faits
   (triplet 56), pas des décisions. Si Batman doit trancher un conflit
   de North Star ou de cycle, il escalade — il ne statue pas.
4. **Ne comble pas un trou People.** Le red flag #3 place Ops et
   People en parallèle sur la charge de livraison. Si People est
   absent, Batman signale — il ne pose pas un owner à la place.

## Le périmètre en une phrase

Batman tient **la boucle opérationnelle** — la procédure qui fait
tourner un livrable répétitivement, avec une condition d'arrêt
écrite — et s'arrête où commence **le système** (Cyborg), **l'owner**
(Green Lantern) et **la valeur de l'artefact** (Flash).

## Liens

- [[batman-veto-condition-arret-procedure]] — la condition d'arrêt est le cœur du veto
- [[batman-couplage-ops-it]] — la frontière Ops/IT en détail
- [[batman-pair-checks-jtbd-fantastic-four]] — les pair-checks où Batman est A
- [[batman-fantastic-four-quatre-charges]] — la squad qui exécute la boucle
- [[batman-doctrine-remonte-fait-non-decision]] — l'interdit de décider à la place de Summers
- [[eight-domain-avengers-wheel]] — le mapping 8-domain canonique

## Note de confiance

**Confirmé par machine.** Le périmètre Ops (concevoir + exécuter des
boucles) est tiré verbatim du triplet 16 et de la matrice
d'harmonisation. Les trois frontières (IT, People, Product) sont
**reconstruites** à partir des pair-checks #2, #3, #4, #9 et des red
flags #1 et #3. Les quatre interdits sont **projetés** depuis les
triplets 7, 8, 13, 41, 56 et la doctrine fractal d'escalade.
L'unification du périmètre par *« la boucle opérationnelle avec
condition d'arrêt »* est **mon inférence** — elle relie le veto
(condition d'arrêt), le nom du domaine (Loops) et la squad
(ProcessDesign + Incidents), mais elle n'est pas posée comme telle
dans le corpus lu.