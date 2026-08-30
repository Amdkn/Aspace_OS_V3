---
type: Concept
title: Batman — proposition d'ajout en Informed (I) sur le pair-check #4 Product → IT
description: Le RACI par rang pose Batman A sur #2 (Sales→Ops) et #3 (Product→Ops), mais Batman est absent des pair-checks amont qui conditionnent sa capacité à tenir ces deux positions. Le pair-check #4 (Product→IT) teste si le système porte le produit — Batman dépend de cette sortie pour que #3 soit tenable. Recommandation : ajouter Batman en I (Informed) sur #4 pour que la dépendance Product→IT→Ops soit visible dans le journal Council, sans empiéter sur la position A de Cyborg.
tags: [batman, cyborg, raci, pair-check, informed, dependance, product-it-ops, journal-council, b2]
generated: { by: minimax-m3, at: 2026-08-19T06:05:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T06:05:00Z }
sources:
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Batman absent du pair-check #4 (Product→IT)
    last_modified: 2026-08-19
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation — pair-check #4 et red flag #1
    last_modified: 2026-08-17
  - id: batman-couple-ops-it
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-ops-it.md"
    title: Batman × Cyborg — chaîne Product→IT→Ops, red flag #1
    last_modified: 2026-08-19
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — instance qui consigne les arbitrages
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman — proposition d'ajout en Informed (I) sur le pair-check #4

## Le constat — Batman dépend de #4 sans être consulté

Le RACI par rang (`b2-pair-check-raci-by-rank.md`) pose 9 lignes
pour les 9 pair-checks canoniques. Sur la ligne #4 (Product → IT) :

| # | Pair-check | A | R | C | I |
|---|---|---|---|---|---|
| 4 | Product → IT | B2 IT (Cyborg) | B3 Kang Dynasty | B2 Product (Flash) | B1, B3 Avengers |

Batman est **absent** du quartet RACI de #4. Il n'est ni A, ni R,
ni C, ni I. Conséquence : quand Flash merge une feature et que
Cyborg statue sur la capacité IT à la porter, Batman n'est pas
dans la boucle — il découvre la décision quand la feature arrive
en pair-check #3 (Product → Ops).

**C'est asymétrique** : Batman est A sur #3, mais il dépend de la
sortie de #4 pour que #3 soit tenable. Si Cyborg pose rouge sur #4
(feature non-déployable), Batman hérite du rouge en #3 sans avoir
été consulté sur #4.

## Pourquoi le RACI n'inclut pas Batman en I sur #4

Le RACI par rang pose A = B2 en aval de la transition (cf.
`b2-pair-check-raci-by-rank.md` §« Le tableau par rang »). Pour
#4, l'aval est B2 IT (Cyborg), pas B2 Ops (Batman). Le RACI est
**strictement aligné sur la transition Product → IT**, pas sur les
**dépendances aval** que la transition crée.

C'est un choix de design défendable : un RACI qui inclut toutes
les dépendances aval deviendrait illisible (chaque transition
aurait 5-6 I au lieu de 1-2). Mais il crée un **angle mort** pour
Batman : la transition #4 conditionne sa propre position A sur #3,
sans qu'il en soit informé.

## L'asymétrie révélée par la chaîne Product → IT → Ops

Le concept `batman-couplage-ops-it.md` (tour 1) a posé la **chaîne
Product → IT → Ops** comme un phénomène réel : le produit doit
d'abord tourner sur le système IT (pair-check #4) avant d'être
supportable Ops (pair-check #3). Le red flag #1 (*Product green,
Ops/IT red*) couvre la situation où #3 et #4 sont rouges
simultanément — mais ne dit rien sur la **dépendance** de #3
vis-à-vis de #4.

Trois cas concrets où Batman est en angle mort sur #4 :

1. **Cyborg refuse un déploiement** parce que la feature ne
   respecte pas les contraintes IT (latence, scalabilité,
   monitoring). Batman ne le sait pas. Quand la feature arrive en
   #3, Batman doit supporter un artefact **non-déployé** — il ne
   peut pas écrire de runbook sans accès au système.
2. **Cyborg accepte un déploiement dégradé** (mode dégradé,
   feature flag off pour certains clients). Batman ne le sait pas
   explicitement. Le runbook Ops décrit un comportement qui n'est
   pas celui de la production.
3. **Cyborg signale une dette IT** (monitoring incomplet, alerting
   à renforcer). Batman ne le sait pas. Le runbook Ops ne couvre
   pas les incidents que l'alerting IT ne détecte pas.

Dans les 3 cas, Batman est en **découverte tardive** — il
construit son runbook sur une réalité qu'il ne maîtrise pas.

## La proposition — Batman en I (Informed) sur #4

Je propose d'ajouter Batman en I sur le pair-check #4 dans la table
RACI. La ligne amendée deviendrait :

| # | Pair-check | A | R | C | I |
|---|---|---|---|---|---|
| 4 | Product → IT | B2 IT (Cyborg) | B3 Kang Dynasty | B2 Product (Flash) | B1, **B2 Ops (Batman)**, B3 Avengers |

**Trois propriétés de l'ajout** :

1. **Informed, pas Consulted** — Batman n'est pas consulté sur
   la décision IT, il est informé de la sortie. C'est cohérent
   avec la doctrine remonte-fait (triplet 56) : Batman reçoit le
   fait, il ne statue pas.
2. **B2 Ops, pas B3 Fantastic Four** — l'ajout est au rang B2,
   pas B3. C'est Batman qui est informé, pas MrFantastic
   directement. Batman relaie ensuite vers sa squad si nécessaire.
3. **A de Cyborg inchangé** — l'ajout ne modifie pas la position
   A de Cyborg sur #4. Cyborg reste l'arbitre de la transition
   Product → IT. Batman est un **spectateur informé**, pas un
   copilote.

## Pourquoi cette correction est défendable

Trois raisons qui rendent la correction **non-controversée** :

1. **Cohérence avec la doctrine remonte-fait** — Batman informé
   peut signaler un problème Ops en aval sans empiéter sur
   l'arbitrage Cyborg. La remontée du fait est la doctrine
   canonique.
2. **Visibilité de la chaîne Product → IT → Ops** — la dépendance
   entre #4 et #3 est documentée par le red flag #1, mais pas
   par le RACI. L'ajout Batman en I rend la dépendance visible
   dans le journal Council, sans la formaliser comme un pair-check
   supplémentaire.
3. **Anti-red flag #1** — le red flag #1 (Product green, Ops/IT
   red) s'allume quand **les deux** sont rouges. Si Batman est
   informé des décisions Cyborg, il peut signaler une dérive
   Cyborg **avant** que le rouge ne s'allume. C'est un mécanisme
   d'alerte précoce.

## Pourquoi cette correction peut être refusée

Trois raisons qui pourraient faire refuser la correction par B2
Council :

1. **Inflation du RACI** — si chaque dépendance aval ajoute un I,
   le RACI gonfle. Le canon préfère un RACI court (9 lignes, 4
   colonnes) à un RACI complet (9 lignes, 6-8 colonnes).
2. **Batman overreach** — Batman informé de #4 pourrait être tenté
   de commenter les décisions IT, même sans droit de vote. C'est
   un risque de **glissement** vers un rôle Consulted de facto.
3. **Cohérence avec les autres I** — le RACI par rang actuel met
   B1 et B3 en I sur chaque pair-check. Ajouter Batman en I crée
   une **asymétrie** : Batman est le seul B2 en I sur un pair-check
   où il n'est ni A, ni C, ni R. Pourquoi Batman et pas les
   autres B2 en aval indirect ?

**Réponse aux 3 objections** :

1. L'inflation est **locale** (1 case par ligne, pas une colonne
   entière). Le RACI reste lisible.
2. Le risque de glissement est **cadré** par la doctrine remonte-fait.
   Batman remonte le fait, il ne statue pas. Si Batman commence à
   commenter les décisions IT, c'est une transgression de la
   doctrine — le Council peut le sanctionner.
3. Batman est le **seul B2** dont la position A sur #3 dépend
   directement de #4. Superman (A sur #1) ne dépend pas de #4.
   Wonder Woman (A sur #6) ne dépend pas de #4. Flash (A sur #6,
   C sur #4) est déjà dans la boucle. La spécificité de Batman
   justifie l'ajout.

## La procédure d'amendement — unanimité + B1 selon la règle canonique

Le RACI par rang est **un document canonique B2**. Son amendement
suit la procédure posée par `b2-council-arbitrage-rule.md` §« Quand
le Council escalade à B1 » : une décision mésoperpétuelle qui
touche au cadre RACI nécessite l'**unanimité B2** + **Informed
B1**. Si Summers accepte l'amendement, le RACI est mis à jour.

**Trois issues possibles** :

1. **Amendement accepté** — Batman en I sur #4, RACI mis à jour,
   Batman informé des décisions IT à compter du cycle suivant.
2. **Amendement refusé** — Batman reste absent de #4, mais le
   Council consigne le débat. La proposition est **non-tranchée**,
   elle peut revenir au cycle suivant.
3. **Compromis** — Batman en I sur #4, **mais** uniquement quand
   la décision Cyborg touche un artefact Ops-sensible (déploiement
   production, mode dégradé, dette IT affectant le run). Le RACI
   est mis à jour avec une note conditionnelle.

## Anti-pièges

- **Batman en C sur #4 au lieu de I.** Batman Consulted sur #4
  serait un **overreach** — il aurait voix au chapitre sur les
  décisions IT sans en avoir la responsabilité. C'est incompatible
  avec la position A de Cyborg.
- **Batman en I sur les 9 pair-checks.** Si Batman est informé
  de tous les pair-checks, le RACI gonfle et Batman devient un
  observateur de tout, ce qui dilue sa capacité d'arbitrage sur
  ses propres pair-checks.
- **L'ajout Batman en I ne modifie pas le portique LAUNCH_READY.**
  Le portique (cf. `batman-launch-ready-portique-final-transverse.md`)
  est transverse, Batman le tient déjà. L'ajout en I sur #4 est
  **orthogonal** au portique.
- **L'ajout ne modifie pas la chaîne canonique de remontée.** Si
  Batman est informé d'un rouge Cyborg, il remonte à Summers
  (triplet 56), pas à Flash. La chaîne reste Batman → Summers.
- **L'ajout ne donne pas à Batman un droit de veto sur #4.** Si
  Cyborg accepte un déploiement, Batman ne peut pas bloquer. Il
  remonte le fait, Summers arbitre. Le veto Batman (triplet 24)
  s'applique toujours seulement à son périmètre (procédure sans
  condition d'arrêt), pas aux décisions IT.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Ops
  qui dépend de la sortie IT
- [[batman-couple-ops-it]] — la chaîne Product→IT→Ops qui motive
  la proposition
- [[batman-couplage-flash-product-cadence-release]] — la cadence
  Flash que Batman verrait via l'info Cyborg
- [[batman-couplage-superman-growth-volume-charge]] — le couplage
  amont Growth que Batman verrait par transit
- [[batman-launch-ready-portique-final-transverse]] — le portique
  qui s'appuie sur la matrice 9 + 5
- [[b2-harmonization-matrix-exploitable]] — la matrice #4 et red
  flag #1
- [[b2-pair-check-raci-by-rank]] — le RACI à amender
- [[b2-council-arbitrage-rule]] — la procédure d'amendement
  unanimité + B1

## Note de confiance

**Confirmé par machine pour le constat d'asymétrie.** Le RACI par
rang est posé verbatim dans `b2-pair-check-raci-by-rank.md` table
9 pair-checks. La ligne #4 est lue intégralement — Batman absent
du quartet. Le red flag #1 est posé verbatim par la matrice
d'harmonisation. Le triplet 56 (Batman remonte-fait) est cité
verbatim.

**Reconstruit pour la proposition d'amendement.** L'ajout Batman
en I sur #4 est **mon inférence** — le RACI actuel ne le pose pas.
Les 3 raisons qui rendent la correction défendable (cohérence
remonte-fait, visibilité chaîne, anti-red-flag) sont **projetées**
depuis la doctrine canonique. Les 3 raisons de refus possibles
(inflation RACI, Batman overreach, asymétrie avec les autres B2)
sont **reconstruites** depuis l'anti-piège *« RACI par personne »*
du concept RACI. La procédure d'amendement (unanimité + B1) est
**tirée verbatim** de `b2-council-arbitrage-rule.md`.

**À arbitrer** : (1) Batman en I sur #4 est-il acceptable pour
Cyborg (qui tient A), ou est-ce une pression de trop sur ses
arbitrages ?, (2) l'ajout doit-il être étendu à Superman (A sur
#1) et Wonder Woman (A sur #6) pour symétrie, ou reste-t-il
spécifique à Batman ?, (3) la procédure d'amendement unanimité + B1
est-elle tenable, ou faut-il une procédure simplifiée pour les
amendements RACI mineurs ?, (4) la proposition doit-elle être
soumise au prochain B2 Council, ou attend-on un cas concret où
l'absence de Batman en I cause un incident ?. Le canon ne tranche
aucun des quatre.
