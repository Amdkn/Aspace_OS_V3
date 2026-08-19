---
type: Concept
title: Veto Batman — procédure sans condition d'arrêt écrite
description: Le veto catalogue de Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite. Le veto est catégoriel (porte sur une classe, pas sur un cas), vérifiable (le motif est dans le packet) et non-négociable au niveau mésoperpétuel. Il se déclenche dans 4 cas concrets et serait abusif dans 3 autres.
tags: [veto, batman, ops, condition-arret, runbook, procedure, catalogue, b2]
generated: { by: minimax-m3, at: 2026-08-19T03:35:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T03:35:00Z }
sources:
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman hasVetoOver procedure-sans-condition-arret"
    last_modified: 2026-08-17
  - id: triplet-batman-veto-remonte
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait, avec son motif"
    last_modified: 2026-08-17
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — propriétés catégoriel/vérifiable/non-négociable
    last_modified: 2026-08-19
  - id: triplet-batman-remonte-fait
    resource: "C:/Users/ado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Veto Batman — procédure sans condition d'arrêt écrite

## Le motif canonique, mot pour mot

Triplet 24, source `coach-os/ORG.json` :
> *« Batman bloque toute procédure qui n'a pas de condition d'arrêt
> écrite. »*

Triplet 57, source `04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_SOUL.md` :
> *« Le veto de Batman ne se négocie pas dans le sprint : il remonte
> à Summers comme un fait, avec son motif. »*

Deux phrases. La première dit **ce qui est bloqué** ; la seconde dit
**comment le veto se gère** quand un autre capitaine veut passer
outre.

## Les trois propriétés du veto (catalogue)

Tout veto B2 légitime a trois propriétés (`b2-eight-domain-vetoes-catalogue.md`
§« Les trois propriétés d'un veto légitime ») :

### 1. Catégoriel

Le veto porte sur une **classe** de procédures, pas sur une procédure
individuelle. *« Je bloque ce runbook »* n'est pas un veto catalogue.
*« Je bloque toute procédure qui n'a pas de condition d'arrêt écrite »*
en est un.

Conséquence pour Batman : il ne peut pas utiliser son veto pour
bloquer un runbook qu'il n'aime pas. Il peut seulement invoquer la
règle générale — *« ce runbook n'a pas de condition d'arrêt »*.

### 2. Vérifiable

Le motif doit être **vérifiable par un tiers qui n'est pas le
capitaine**. Pour Batman, le test est binaire : ouvrir la procédure,
chercher la section *« condition d'arrêt »* (ou équivalent), la
trouver absente ou non chiffrée. Si la procédure dit *« arrêter
quand le client n'en veut plus »*, le veto tient — le motif est
*« pas de condition chiffrée »*. Si la procédure dit *« arrêter
quand le NPS descend sous 30 sur 2 trimestres consécutifs »*, le
veto tombe — la condition est là.

### 3. Non-négociable au niveau mésoperpétuel

Un capitaine B2 ne peut pas passer outre le veto d'un autre
capitaine B2. La seule issue est B1 (escalade). Pour Batman, le
triplet 57 explicite : *« le veto ne se négocie pas dans le sprint »* —
ni Flash (Product), ni Superman (Growth), ni JohnJones (Sales) ne
peuvent dire *« OK on lance quand même, c'est une exception »*.
S'ils veulent forcer, ils escaladent à Summers pour réécriture de
la règle catalogue — ce qui est explicitement *« très rare »* dans
le catalogue.

## Les 4 cas concrets où le veto se déclenche

Cas tirés de la doctrine B2 + transposés au périmètre Ops :

1. **Runbook sans section « arrêt ».** Un runbook qui décrit comment
   démarrer, exécuter, escalader, mais qui ne dit pas comment **arrêter**
   proprement. Le veto tient. C'est le cas nominal.
2. **Process de support sans SLO de fin.** Un process de support qui
   tourne en boucle sur chaque ticket sans seuil chiffré de
   désengagement (*« on arrête quand le client a 3 tickets résolus »*).
   Le veto tient.
3. **Boucle d'onboarding sans condition de handover.** Une procédure
   d'onboarding client qui n'indique pas le moment où Coach OS
   transfère la responsabilité au client (handoff). Le veto tient —
   un onboarding qui ne se termine jamais est une Ops qui ne s'arrête
   pas.
4. **Process de revue sans périodicité d'arrêt.** Une revue
   hebdomadaire ou mensuelle qui ne précise pas quand elle s'arrête
   (à la fin du projet ? quand le DoD est rempli ? jamais ?). Le
   veto tient.

## Les 3 cas où le veto serait ABUSIF

Le veto catalogue est légitime quand il est **catégoriel**, pas
quand il sert un agenda personnel. Trois cas où Batman abuse s'il
invoque :

1. **Procédure avec condition d'arrêt mais que Batman juge
   insuffisante.** Le veto catalogue teste la **présence** de la
   condition, pas sa **qualité**. *« Le runbook dit "arrêter quand
   le client n'en veut plus" — c'est trop vague »* est une critique
   de design, pas un veto. Batman escalade en revue, il ne bloque
   pas sur la base d'un jugement esthétique.
2. **Procédure d'un autre capitaine qui touche à l'Ops.** Un process
   Finance (Wonder Woman) ou People (Green Lantern) qui n'a pas de
   condition d'arrêt relève de leur veto respectif (dépense récurrente
   sans revue / recrutement sans critère de sortie), pas du veto
   Batman. Batman signale, il ne bloque pas un process dont il n'est
   pas propriétaire.
3. **Procédure déjà arrêtée.** Une procédure marquée *« arrêtée le
   2026-XX-XX, motif : fin de produit »* n'a pas besoin de condition
   d'arrêt — elle a une **date d'arrêt**. Le veto tombe
   automatiquement.

## Anti-pièges

- **Veto utilisé comme pouvoir personnel.** Le veto Batman est un
  garde-fou opérationnel, pas un outil de blocage politique. Le
  signal : un veto Batman qui revient systématiquement sur les mêmes
  procédures est probablement un veto politique, pas un veto
  catalogue.
- **Veto opposé sans motif écrit.** Le triplet 57 exige *« avec son
  motif »*. Un veto non documenté dans le packet mésoperpétuel est
  invalide — et le Council peut passer outre.
- **Veto qui ne remonte pas à Summers.** Le triplet 56 distingue
  Batman qui *« remonte des faits »* de Batman qui *« prend des
  décisions »*. Si Batman oppose un veto sans escalader le fait à
  Summers, il a statué — et la doctrine canonique dit que ce n'est
  pas son rôle.
- **Confondre condition d'arrêt et date de fin.** Une procédure avec
  date de fin (ex : revue du 12WY-2026-Q3) a une condition d'arrêt
  — elle s'arrête au 2026-09-30. Le veto teste la présence d'un
  déclencheur chiffré, pas la présence d'une date calendaire.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre où s'applique le veto
- [[batman-doctrine-remonte-fait-non-decision]] — pourquoi le veto remonte à Summers
- [[b2-eight-domain-vetoes-catalogue]] — les 8 vetos et leurs trois propriétés
- [[b2-council-arbitrage-rule]] — l'instance qui consigne le veto dans le packet
- [[b2-meso-decision-packet-spec]] — le format qui porte le motif vérifiable

## Note de confiance

**Confirmé par machine.** Le motif du veto (triplets 24 et 57) et les
trois propriétés (catalogue) sont tirés verbatim. Les 4 cas de
déclenchement sont **reconstruits** à partir du périmètre Ops
(ProcessDesign, runbook, support, onboarding, revue) et du nom du
domaine (Opérations en Loops). Les 3 cas d'abus sont **projetés** à
partir de l'anti-piège *« veto utilisé comme outil politique »* du
catalogue et de la doctrine de séparation des vetos entre capitaines.
La distinction *condition d'arrêt vs date de fin* est **mon
inférence** — elle n'est pas explicite dans le corpus, mais elle
tombe des trois propriétés (catégoriel + vérifiable).