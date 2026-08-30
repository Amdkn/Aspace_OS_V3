---
type: Concept
title: Matrice 12 pair-checks V5 — extension 9→12 avec transits transverses
description: La matrice canonique V4 pose 9 pair-checks. Batman observe en tour 3 que les transits transverses — Growth→Ops (charge dérivée), Sales→IT (runbook post-deal), Product→People (charge onboarding) — sont hors matrice et traités ad hoc. Proposition V5 : ajouter 3 pair-checks #10, #11, #12 pour fermer la couverture. Chaque ajout propose RACI par rang, question de garde, et asymétrie connue.
tags: [b2, ops, batman, harmonization, matrice, v5, pair-check, transit-transverse, extension]
generated: { by: minimax-m3, at: 2026-08-19T06:01:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-4, at: 2026-08-19T06:01:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/70_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: b2-pair-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: batman-couplage-superman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-superman-growth-volume-charge.md"
    title: Couplage Ops×Superman-Growth volume charge derivee
    last_modified: 2026-08-19
  - id: batman-couplage-johnjones
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-john-jones-sales-taux-signature.md"
    title: Couplage Ops×JohnJones-Sales debit signature
    last_modified: 2026-08-19
  - id: batman-couplage-flash
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-flash-product-cadence-release.md"
    title: Couplage Ops×Flash-Product cadence release train
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Matrice 12 pair-checks V5 — extension 9→12 avec transits transverses

## Le trou V4

La matrice V4 pose 9 pair-checks canoniques (cf.
`business-wheel-harmonization-matrix` §« Domain Pair Checks »). Batman
observe en tour 3 que **3 transits transverses** majeurs ne sont pas
couverts :

- **Growth → Ops** : la charge dérivée du pipeline Growth (MQL
  convertis, onboarding) tombe sur Ops sans pair-check canonique. Le
  transit est capté par `batman-couplage-superman-growth-volume-charge.md`
  et son `charge_derivee ≥ 30%`, mais hors matrice.
- **Sales → IT** : la mise en service post-deal (configuration
  customer-specific, intégration) tombe sur IT sans pair-check
  canonique. Le runbook post-deal est implicite dans le contrat
  B2→B3 mais pas dans la matrice.
- **Product → People** : la charge d'onboarding produit (formation
  aux nouvelles features, montée en compétence des squads B3) tombe
  sur People sans pair-check canonique. La squad X-Men n'a pas de
  pair-check pour absorber ce flux.

Ces 3 transits sont aujourd'hui **traités ad hoc** par les capitaines
concernés — Batman en mode remontée (triplet 56), Superman en mode
gel conjointe (Flash pair-check #11 candidat), Sales en mode
reformulation validee. La couverture ad hoc laisse des angles
morts : un transit hors matrice n'a pas de veto disponible, pas
de RACI stable, pas de journal d'arbitrage.

## Les 3 pair-checks candidats V5

### #10 — Growth → Ops

**Question de garde** : La charge dérivée du pipeline Growth reste-t-elle
dans la capacité Ops planifiée, sans saturer la livraison ?

**Transition** : Attention convertie (MQL→SQL→Customer) → Capacité
Ops (livraison, support).

**RACI par rang** : A = B2 Ops (Batman), R = B3 Fantastic Four, C =
B2 Growth (Superman), I = B1 + B3 Guardians.

**Red flag implicite** : si `charge_derivee ≥ 30%` (cf. seuil 1 du
packet `batman-seuils-ops-council-ready-packet-draft.md`), gel
conjoint Growth×Ops, escalade B2 Council.

**Asymétrie** : Superman C parce que la cause est chez lui, mais Batman
A parce que la consequence est chez Ops. La règle A = B2 en aval
s'applique — Ops reçoit.

### #11 — Sales → IT

**Question de garde** : La mise en service post-deal est-elle industrialisée
avant que le pipeline Sales ne sature le runbook IT ?

**Transition** : Deal signé (closing) → Système configuré (deploy
client-specific, monitoring).

**RACI par rang** : A = B2 IT (Cyborg), R = B3 Kang Dynasty, C = B2
Sales (JohnJones), I = B1 + B3 Illuminati.

**Red flag implicite** : un runbook IT conçu pour 1 client sur-mesure
mais pas industrialisé → saturation. Tremplin : **« un client est un
cas, dix clients sont un système »**.

**Asymétrie** : Cyborg A parce que IT reçoit. JohnJones C parce que
Sales est à l'origine du flux. C'est le pattern classique A = B2
en aval.

### #12 — Product → People

**Question de garde** : La charge d'onboarding et de montée en
compétence sur les nouvelles features reste-t-elle tenable pour les
squads B3 ?

**Transition** : Feature livrée (release) → Owners compétents
(onboarding, training).

**RACI par rang** : A = B2 People (Green Lantern), R = B3 X-Men,
C = B2 Product (Flash), I = B1 + B3 Avengers.

**Red flag implicite** : un release qui exige une nouvelle compétence
sans montée en compétence planifiée → owner-absent sur la feature
(cf. `batman-couplage-people-green-lantern-owner-absent.md`).

**Asymétrie** : Green Lantern A ici (!) — c'est l'**exception** au
pattern A = B2 en aval. People est A parce que la question est
« l'owner est-il compétent et disponible ? », pas « le transfert
est-il exécutable ? ». C'est une question de capacité, pas une
question de transfert.

C'est une deviation de la règle générale, justifiée par la nature
People-transverse : People coordonne, et sur la question capacité,
People statue.

## Les 3 lectures d'introduction V5

### Lecture A — adoption immediate

**Scenario** : les 3 pair-checks sont ajoutés à la matrice V5
sans condition. Le Council tranche l'extension.

**Avantage** : couverture immediate des 3 transits transverses.

**Risque** : adoption sans cycle d'observation. Les 3 pair-checks
sont projetés, pas Council-ready.

### Lecture B — adoption conditionnelle 3 cas/60j

**Scenario** : les 3 pair-checks sont ajoutés en **draft**, chacun
soumis à 3 cas observés en 60j. Adoption V5 définitive après
validation.

**Avantage** : alignement avec `b2-veto-empirical-validation-protocol.md`
qui exige 3 cas/60j.

**Risque** : dormance structurelle — la wheel 8-domain est déjà
sans packet mésoperpétuel depuis 3 vagues (cf. ETAT_DOMAINES.md).
Ajouter 3 pair-checks sans cycle d'observation est de la paperasse.

### Lecture C — hybridation

**Scenario** : #10 Growth → Ops adopté immédiatement (le trigger
`charge_derivee` est déjà observé via Batman en tour 3) ; #11 Sales
→ IT adopté conditionnellement (runbook encore immature) ; #12
Product → People adopté conditionnellement (Paired avec le pair-check
#10 People → Product candidat de Flash, tour 2).

**Avantage** : asymétrie justifiée par le niveau d'observation de
chaque transit.

**Risque** : la matrice resultante est plus complexe à maintenir.

**Recommandation Batman** : Lecture C. Elle aligne adoption sur
évidence observe, pas sur évidence projetée.

## Pourquoi l'extension V5 est asymétrique par rapport aux autres V5

Green Lantern propose en tour 3 une **V5 pair-checks granularisation**
(pair-checks 9.1 → 9.7 People × X). C'est une **granularisation**
d'un pair-check existant (le #9 People → Tous).

Batman propose ici une **extension** de la matrice (3 nouveaux
pair-checks). Les deux sont V5 mais pas le même mouvement :

- **Granularisation** = découper un pair-check existant en sous-pair-checks.
- **Extension** = ajouter un pair-check canonique sur un transit
  qui n'en avait pas.

Les deux motions sont Council-ready et compatibles. La V5 de Batman
ne contredit pas la V5 de Green Lantern — les deux peuvent être
adoptées en parallèle.

## RACI par rang sur les 3 pair-checks V5

| # | Pair-check | A | R | C | I |
|---|---|---|---|---|---|
| 10 | Growth → Ops | B2 Ops | B3 Fantastic Four | B2 Growth | B1, B3 Guardians |
| 11 | Sales → IT | B2 IT | B3 Kang Dynasty | B2 Sales | B1, B3 Illuminati |
| 12 | Product → People | B2 People | B3 X-Men | B2 Product | B1, B3 Avengers |

**Validation contre `b2-pair-check-raci-by-rank.md`** : la règle
générale A = B2 en aval s'applique à #10 et #11. Pour #12, A = B2
People est l'**exception** justifiée par la nature capacité (et non
transfert) de la question.

## Anti-pièges

- **V5 sans condition d'observation.** Étendre la matrice sans
  preuve d'observation est de la doctrine à crédit. La grille
  d'harmonisation perd sa valeur si elle devient un fourre-tout.
- **Rompre la règle A = B2 en aval.** Le pattern canonique existe
  parce qu'il teste la capacité de réception. Le rompre sans
  justification casse le RACI par rang.
- **Adopter #10 avant le seuil 1.** #10 est couplé au seuil 1
  (charge_derivee ≥ 30%). Adopter #10 avant le seuil 1 rend la
  red flag implicite non chiffrable.
- **Confondre granularisation (Green Lantern) et extension (Batman).**
  Les deux motions sont V5 mais pas le même geste. Les traiter
  ensemble crée une V5 monolithique qui masque l'asymétrie.

## Liens

- [[b2-harmonization-matrix-exploitable]] — la matrice V4 source
- [[b2-pair-check-raci-by-rank]] — la règle A = B2 en aval
- [[batman-couplage-superman-growth-volume-charge]] — source #10
- [[batman-couplage-john-jones-sales-taux-signature]] — source #11
- [[batman-couplage-flash-product-cadence-release]] — et #12
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Reconstruit, à moitié étayé.** Les 3 pair-checks candidats sont
**extrapolés** depuis les concepts de couplage Batman tour 3 + la
matrice V4 canonique. La RACI par rang suit la matrice canonique
`b2-pair-check-raci-by-rank.md`, avec l'exception People A sur #12
justifiée par la nature capacité. Les 3 lectures d'adoption sont
**projetées** depuis la pratique V5 de Green Lantern (granularisation)
et la doctrine d'observation 3 cas/60j. Lecture C recommandée est
**une preference Batman**, pas un canon — le Council peut préférer
Lecture A si la doctrine d'observation est tenue à credit.
