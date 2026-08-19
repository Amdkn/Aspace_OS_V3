---
type: Concept
title: Batman Accountable sur Sales→Ops et Product→Ops — la squad Fantastic Four en exécution
description: Batman est Accountable (RACI par rang) sur 2 des 9 pair-checks : Sales → Ops et Product → Ops. Dans les deux cas, le Responsible est B3 Fantastic Four (MrFantastic pour ProcessDesign, HumanTorch pour Incidents). Le contrat bilatéral B2 sponsor + B3 squad lead à double signature est ce qui rend les deux transitions tenables.
tags: [batman, raci, pair-check, sales-ops, product-ops, fantastic-four, jtbd, contract, b2, b3]
generated: { by: minimax-m3, at: 2026-08-19T03:45:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T03:45:00Z }
sources:
  - id: b2-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: triplet-mrfantastic
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 31 — MrFantastic handledBy processdesign"
    last_modified: 2026-08-17
  - id: triplet-humantorch
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 32 — HumanTorch handledBy incidents"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Batman Accountable sur Sales→Ops et Product→Ops

## Vue d'ensemble — Batman A sur 2 des 9 pair-checks

Le RACI par rang (`b2-pair-check-raci-by-rank.md`) place Batman (B2
Ops) en position **Accountable** sur deux transitions :

| # | Pair-check | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| 2 | **Sales → Ops** | B3 Fantastic Four | B2 Sales (JohnJones) | B1 (Summers), B3 Illuminati |
| 3 | **Product → Ops** | B3 Fantastic Four | B2 Product (Flash) | B1 (Summers), B3 Avengers |

Règle de lecture du tableau : A est toujours le B2 captain **en aval**
de la transition. Sur les 9 pair-checks, Batman est A deux fois — et
B3 Fantastic Four est R deux fois. Le tandem Batman + Fantastic
Four est ce qui ferme la wheel côté opérationnel.

## Pair-check #2 — Sales → Ops : les promesses peuvent-elles être tenues répétitivement ?

**Source en amont** : JohnJones (Sales) — une promesse signée (deal).
**Source en aval** : Batman (Ops) — la procédure de livraison, onboarding,
support.

**Question de garde** (matrice d'harmonisation) : *« Les promesses
peuvent-elles être tenues répétitivement ? »*

**DoD côté Ops** : pour chaque promesse acceptée par Sales, Batman
doit pouvoir ouvrir une boucle Ops (livrer, onboard, supporter, un
jour arrêter) sans surcharger la squad Fantastic Four.

**Red flag déclencheur** : #3 *Sales green, Ops/People red* —
*risque de charge de livraison, la promesse ne pourra pas être tenue*.
Batman est A ; Green Lantern (People) est C. Si Batman ne peut pas
arbitrer la charge seul, il escalade au B2 Council.

**Forme de la preuve attendue** (cf. `b2-b3-jtbd-handoff-contract.md`) :
- *capture* (runbook Screenshots du process d'onboarding) **OU**
- *log* (horodatage des livraisons, NPS, charge par client).

**Capitaine B2 sponsor** : Batman (A).
**B3 squad lead** : MrFantastic (ProcessDesign) — conçoit la boucle
(triplet 31 : *« MrFantastic tient la charge ProcessDesign : conçoit
la boucle, décide de sa forme et de son point d'entrée »*).

**Cycle de revue** : hebdomadaire (B2 cadence) — revue de la charge
FantasticFour, NPS post-onboarding, charge support.

## Pair-check #3 — Product → Ops : l'artefact est-il supportable opérationnellement ?

**Source en amont** : Flash (Product) — un artefact shipé (feature
mergée).
**Source en aval** : Batman (Ops) — la boucle de maintenance et de
support.

**Question de garde** : *« L'artefact est-il supportable
opérationnellement ? »*

**DoD côté Ops** : pour chaque feature mergée, Batman doit pouvoir
produire (ou faire produire par Fantastic Four) un runbook de support
en une journée — sinon Flash doit revoir son design.

**Red flag déclencheur** : #1 *Product green, Ops/IT red* —
*ne pas lancer*. Le couple Batman + Cyborg est ce qui ferme la
porte. Si Batman ne peut pas supporter une feature, il ne peut pas
laisser Flash la merger ; il remonte le fait à Summers.

**Forme de la preuve attendue** :
- *log* (runbook ouvert dans `SOP/` ontology, daté) **OU**
- *capture* (ticket support type résolu en moins de N heures).

**Capitaine B2 sponsor** : Batman (A).
**B3 squad lead** : HumanTorch (Incidents) — porte le feu
opérationnel (triplet 32 : *« HumanTorch tient la charge Incidents :
prend l'incident, décide de l'escalade et du retour à la normale »*).

**Cycle de revue** : hebdomadaire — revue des runbooks ouverts, des
incidents résolus, du gap entre feature mergée et runbook écrit.

## Le contrat bilatéral B2 sponsor + B3 lead

`b2-b3-jtbd-handoff-contract.md` pose le contrat : Batman signe
conjointement avec le B3 squad lead (MrFantastic pour #2, HumanTorch
pour #3). Trois champs supplémentaires que Batman doit poser dans
chaque JTBD packet :

1. **Cadre d'exécution** — sprint B3 d'une semaine (5 scrums/semaine,
   triplet 11), squad Fantastic Four, Batman sponsor.
2. **Bornes DoD explicites** — pour #2, un seuil chiffré (ex : *« NPS
   post-onboarding ≥ 40 sur 100 réponses »*) ; pour #3, un seuil
   (ex : *« 95 % des features mergées ont un runbook ouvert sous
   24h »*).
3. **Preuves attendues par forme** — Batman choisit 1 ou 2 formes
   parmi les 4 canoniques (capture, log, métrique, témoignage client).

## Les JTBD packets que Batman émet

Batman **émet** vers B3 deux types de paquets :

- `B3-JTBD-YYYY-NN-Sales2Ops` — un paquet par série de promesses
  Sales à transformer en boucle Ops. Squad cible : Fantastic Four,
  lead MrFantastic.
- `B3-JTBD-YYYY-NN-Product2Ops` — un paquet par série de features
  mergées à supporter. Squad cible : Fantastic Four, lead
  HumanTorch.

## Les JTBD packets que Batman reçoit

Batman **reçoit** un paquet de B3 quand Fantastic Four remonte un
trou (triplet 41 — *« B3 a l'interdit de combler lui-même un trou
du sprint — il le signale à son VP »*). Le paquet est un trou
explicite : *« MrFantastic ne peut pas ouvrir le runbook onboarding
parce que Sales n'a pas transmis la spec client »*. Batman arbitre
— il escalade à JohnJones (B2 Sales amont) ou au B2 Council si la
spec manque structurellement.

## Anti-pièges

- **Batman A sur un pair-check où il n'est pas en aval.** Le RACI par
  rang place toujours A côté réception. Batman n'est jamais A sur
  Growth×Sales ni Product×IT — c'est JohnJones et Cyborg. Confondre
  A = Ops serait surcharger Batman.
- **B3 Fantastic Four qui décide de l'arbitrage.** Le triplet 41 dit
  *« B3 signale, ne decide pas »*. MrFantastic ne tranche pas si une
  promesse Sales est tenable — il remonte à Batman, qui arbitre
  avec JohnJones.
- **Batman qui ne remonte pas un trou People.** Le red flag #3 place
  Ops **et** People en parallèle sur la charge de livraison. Si
  People n'a pas posé d'owner tenable, Batman ne pose pas un
  Batman à la place — il signale à Green Lantern et au B2 Council.
- **Cycle de revue plus long que la semaine.** Un pair-check
  Sales→Ops ou Product→Ops sans revue hebdomadaire rate les dérives
  naissantes. Le B2 cadence est hebdomadaire, pas mensuelle.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre qui motive les pair-checks
- [[batman-fantastic-four-quatre-charges]] — la squad en détail
- [[batman-veto-condition-arret-procedure]] — le veto applicable aux runbooks des pair-checks
- [[b2-pair-check-raci-by-rank]] — le tableau complet des 9 pair-checks
- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral détaillé

## Note de confiance

**Confirmé par machine.** Les 2 pair-checks où Batman est A sont
tirés verbatim du RACI par rang. Les DoD et seuils chiffrés en exemple
sont **mon illustration** — ils n'ont pas été vérifiés contre un
profil Fantastic Four individuel. Le rôle MrFantastic (ProcessDesign)
et HumanTorch (Incidents) est cité verbatim des triplets 31 et 32.
Les formes de preuve et le contrat bilatéral sont extrapolés depuis
`b2-b3-jtbd-handoff-contract.md`.