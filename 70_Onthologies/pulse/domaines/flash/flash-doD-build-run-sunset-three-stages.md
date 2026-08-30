---
type: Concept
title: Flash — DoD en trois stades : build, run, sunset
description: Le DoD du domaine Flash (Product 03) est aujourd'hui confondu entre trois stades — build, run, sunset. Ce concept le décompose explicitement avec critères d'acceptance chiffrés par stade. Permet à Flash de bloquer sur un stade spécifique sans bloquer les autres (le build peut être tenu même si le sunset est mal préparé). Réconcilie la lecture stricte (build seul) et la lecture large (build + run + sunset) du périmètre Flash.
tags: [flash, product, dod, build, run, sunset, trois-stades, acceptance-criteria, perimetre-strict, perimetre-large]
generated: { by: minimax-m3, at: 2026-08-19T08:10:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-3, at: 2026-08-19T08:10:00Z }
sources:
  - id: flash-doctrine-valeur-artefact
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doctrine-valeur-artefact.md"
    title: Doctrine valeur d'artefact — contraste Batman/Flash/Superman/Wonder Woman
    last_modified: 2026-08-19
  - id: flash-test-continuity
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doctrine-valeur-artefact-test-of-continuity.md"
    title: Test de continuité 4 dimensions (build, run, pivot, sunset)
    last_modified: 2026-08-19
  - id: flash-domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-domain-perimeter.md"
    title: Périmètre Flash — 4 frontières floues, lectures stricte vs large
    last_modified: 2026-08-19
  - id: flash-red-flag-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-red-flag-1-trigger.md"
    title: Red flag #1 — Product green Ops/IT red
    last_modified: 2026-08-19
  - id: flash-jtbd-emit-receive
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-jtbd-emit-receive.md"
    title: Flash Product — paquets JTBD émis et reçus par le squad Avengers
    last_modified: 2026-08-19
  - id: flash-pair-checks
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-checks-dependencies.md"
    title: Pair-checks Product × Ops, Product × IT, Finance × Product, Legal × Product
    last_modified: 2026-08-19
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: Cadence hebdomadaire Council — DoD révisé chaque cycle
    last_modified: 2026-08-19
  - id: b3-cycle-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-cycle-scrums-five-per-week.md"
    title: B3 cycle scrums 5 per week
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash — DoD en trois stades : build, run, sunset

## Le problème — un DoD confondu

Le DoD du domaine Product (03) est aujourd'hui **implicite et confondu**. `flash-jtbd-emit-receive.md` §« Ce que Flash (B2 sponsor) promet » cite :

> *« Bornes DoD explicites : seuils chiffrés (ex : taux de support Ops < 5 incidents/mois, NPS artefact ≥ 40, marge brute ≥ 60%) »*

Mais ces seuils mélangent trois temporalités différentes :
- **Taux de support Ops < 5 incidents/mois** → c'est un critère de **run**
- **NPS artefact ≥ 40** → c'est un critère de **build** (qualité perçue)
- **Marge brute ≥ 60%** → c'est un critère de **build** (coût)

Un DoD qui mélange les trois stades **empêche Flash de bloquer sur un stade précis**. Conséquence : le veto catalogue s'applique mal, ou s'applique trop largement.

## Les trois stades canoniques

### Stade 1 — Build (la production de l'artefact)

**Définition** : période entre l'acceptation du scope et la première mise en production de l'artefact. Pendant ce stade, Flash (Avengers) **produit**, Batman (Fantastic Four) et Cyborg (Kang Dynasty) **préparent le run** (pair-check #3 et #4 en mode handoff).

**Critères d'acceptance chiffrés** :
- ✅ Scope formalisé (chiffré en heures ou en points, DoD explicite)
- ✅ Code mergé sur main, coverage tests ≥ 80%
- ✅ Runbook documenté (date, version, owner)
- ✅ Pair-check #3 (Product → Ops) en `LAUNCH_READY` OU exception documentée
- ✅ Pair-check #4 (Product → IT) en `SYSTEM_READY` OU exception documentée
- ✅ Pair-check #6 (Finance → Product) en `FINANCE_READY` (marge prévue ≥ seuil)
- ✅ Pair-check #8 (Legal → Product) en `LEGAL_READY` (frontières IP/privacy/terms appliquées)

**Signal gate** : `PRODUCT_READY` quand les 7 critères sont ✅ (cf. `b3-veto-and-signal-vocabulary.md`).

### Stade 2 — Run (la maintenance et l'exploitation)

**Définition** : période entre la première mise en production et le début du sunset. Pendant ce stade, Batman (Fantastic Four) **maintient**, Hawkeye **surveille les métriques**, et Flash (Avengers) **corrige les défauts non-couverts par le runbook** (escalade squad lead → captain).

**Critères d'acceptance chiffrés** :
- ✅ Taux d'incidents support ≤ 5/mois (sinon : retour Flash pour correction)
- ✅ NPS post-delivery ≥ 40 sur 100 réponses mesurées
- ✅ Runbook exécuté par un tiers sans intervention de l'opérateur originel (test de continuité dimension 2 OK)
- ✅ Squad back-up identifiée et formée (rotation effective)
- ✅ Pivot reproductible (test de continuité dimension 3 OK)
- ✅ Lag indicators tenus à J+30 (rétention ≥ seuil)

**Signal gate** : `PRODUCT_RUNNING` (signal implicite, distinct de `PRODUCT_READY`). Si l'un des 6 critères tombe en rouge, Flash peut **réouvrir** le build (escalade vers CaptainAmerica + Hulk pour correction).

### Stade 3 — Sunset (la dépréciation planifiée)

**Définition** : période entre la décision de retirer l'artefact du catalogue et la dépréciation effective (fin de vie, archivage code, message client). Pendant ce stade, Flash **pilote la dépréciation**, Batman **assure la continuité pendant la transition**, Sales **communique aux clients**.

**Critères d'acceptance chiffrés** :
- ✅ Date de fin de vie posée ET communiquée aux clients ≥ 90 jours avant
- ✅ Plan de migration des clients dépendants vers une alternative (interne ou externe)
- ✅ Archivage code + documentation dans `_archive/` (runbook final, lessons learned)
- ✅ Message client standard (template Sunset) envoyé à 90j, 60j, 30j, 7j, 0j
- ✅ Monitoring sunset activé (alerte si client actif > 0 après J+0)
- ✅ Run de Batman terminé sans incident pendant la période de transition

**Signal gate** : `PRODUCT_SUNSET` (gate finale). Quand les 6 critères sont ✅, l'artefact est radié du catalogue Avengers.

## Pourquoi 3 stades et pas 4 ou 2

`flash-doctrine-valeur-artefact-test-of-continuity.md` pose un test de continuité en **4 dimensions** (build, run, pivot, sunset). Pourquoi 3 stades et pas 4 ?

**Réponse** : le test a 4 dimensions parce qu'il teste la **valeur** (qui peut pivoter). Le DoD a 3 stades parce qu'il chronologie l'**exécution** (qui fait quoi quand). Le pivot (dimension 3 du test) est une **propriété transversale** qui s'applique à tous les stades — un artefact au stade build peut pivoter, un artefact au stade run peut pivoter. Le pivot n'est pas un stade, c'est une **capacité**.

Concrètement : un artefact qui passe du stade build au stade run peut basculer (re-pivot) en stade build si ScarletWitch initie une transformation de scope. La chronologie n'est pas strictement linéaire.

## L'impact sur les pair-checks

Le DoD en 3 stades change le statut RACI sur les pair-checks :

| Pair-check | Stade build | Stade run | Stade sunset |
|---|---|---|---|
| #3 Product → Ops | C (Flash consulte Batman sur runbook) | A (Batman porte la boucle) | I (Flash informe Batman de la dépréciation) |
| #4 Product → IT | C (Flash consulte Cyborg sur déploiement) | A (Cyborg porte la résilience) | I (Flash informe Cyborg de l'archivage) |
| #6 Finance → Product | A (Flash porte la marge pendant build) | C (Wonder Woman consulte Flash sur ROI réel) | I (Wonder Woman radié l'allocation) |
| #8 Legal → Product | A (Flash applique les frontières) | C (Flash re-vérifie la conformité en run) | I (Aquaman signe la dépréciation juridique) |

**Conséquence** : un arbitrage B2 Council sur un pair-check Product doit préciser **le stade** pour déterminer qui porte le A. Le RACI par rang de `b2-pair-check-raci-by-rank.md` est **stade-aveugle** — il ne précise pas la position dans le cycle de vie. Ce concept complète le RACI en y ajoutant la dimension stade.

## La résolution de la confusion lecture stricte vs lecture large

`flash-domain-perimeter.md` §« Pourquoi ces frontières existent » pose deux lectures vivantes du périmètre Flash :
- **Lecture stricte** : build uniquement (3 critères du stade build)
- **Lecture large** : build + run + sunset (les 19 critères combinés)

Avec le DoD en 3 stades, la lecture stricte et la lecture large sont **réconciliables** :
- **Lecture stricte** : Flash porte le stade build, mais délègue explicitement run et sunset à Batman/Aquaman
- **Lecture large** : Flash porte les 3 stades, avec les pair-checks qui basculent A → I → I

**Recommandation** : la lecture large devient le défaut, et un captain qui veut la lecture stricte doit **le déclarer** dans son `00_B2_DOMAIN_CONTROL_ROOM.md`. Sinon, le défaut large s'applique.

## Les 3 anti-pièges du DoD en 3 stades

### Anti-piège 1 — Confondre run avec build-bis

Un artefact au stade run qui reçoit une nouvelle feature entre en **build-bis** (re-build), pas en run prolongé. Les critères d'acceptance sont ceux du stade build (coverage ≥ 80%, runbook réécrit, etc.), pas ceux du run.

### Anti-piège 2 — Sunset sans migration

Un sunset qui n'a pas de plan de migration des clients dépendants est **un abandon déguisé**, pas un sunset. Le critère 2 (plan de migration) est non-négociable. Un sunset qui rate ce critère est **un arbitrage B1**, pas une décision Flash.

### Anti-piège 3 — Stade run qui s'éternise

Un artefact qui reste au stade run > 36 mois sans signal de sunset est en **run-éternisé**. C'est un failure mode du test de continuité (dimension 4 KO). Flash doit signaler ce sunset-backlog à chaque revue trimestrielle.

## Pourquoi ce DoD n'est pas un processus projet

Trois différences avec un processus projet classique :

1. **Pas de dates fixes.** Les stades sont déclenchés par des **gates signals** (PRODUCT_READY, PRODUCT_RUNNING, PRODUCT_SUNSET), pas par un planning Gantt. La cadence est pilotée par les pair-checks, pas par un PMO.
2. **Pas de livrables intermédiaires obligatoires.** Seul le passage au stade suivant est mesurable. Les itérations à l'intérieur d'un stade (build, run) ne sont pas formalisées en cycle de vie externe.
3. **Le sunset n'est pas un exit.** Un sunset est un **stade** avec critères d'acceptance, pas une fin de projet. L'archive lessons learned est elle-même un livrable qui ouvre un nouveau cycle.

## Liens

- [[flash-doctrine-valeur-artefact]] — la doctrine qui sous-tend le DoD en 3 stades
- [[flash-doctrine-valeur-artefact-test-of-continuity]] — le test de continuité (4 dimensions) qui valide le DoD
- [[flash-domain-perimeter]] — les lectures stricte vs large réconciliées
- [[flash-jtbd-emit-receive]] — le DoD actuel confondu que ce concept décompose
- [[flash-red-flag-1-trigger]] — le red flag #1 qui se déclenche au stade build
- [[flash-pair-checks-dependencies]] — les 4 pair-checks dont le RACI dépend du stade
- [[b2-council-cadence-and-chair]] — la cadence hebdomadaire où le DoD est révisé
- [[b3-cycle-scrums-five-per-week]] — la cadence 5 scrums/semaine à l'intérieur du stade build

## Note de confiance

**Reconstruit, à moitié étayé.** Le triplet v3 ligne 25 (veto Flash) et `flash-jtbd-emit-receive.md` §« Ce que Flash promet » (DoD confondu) sont cités verbatim. La décomposition en 3 stades est **projetée** à partir du cycle de vie logiciel classique (build / run / sunset) et de la matrice d'harmonisation — pas une catégorie canonique du corpus. Les 7 critères build + 6 critères run + 6 critères sunset sont **reconstruits** à partir des 4 pair-checks impliquant Product, du test de continuité 4D, et de la pratique B2 → B3 documentée — chaque critère est chiffrable mais le seuil exact est **arbitraire** (≥ 80%, ≥ 40, ≥ 5/mois). La réconciliation lecture stricte vs lecture large est **mon extrapolation** — la note de confiance de `flash-domain-perimeter.md` marque déjà les 2 lectures comme « hypothèses non résolues ». La matrice RACI stade-dépendante est **projetée** à partir du RACI par rang de `b2-pair-check-raci-by-rank.md` et n'est pas étayée par un triplet canonique. Standing : draft de doctrine, à soumettre B2 Council pour validation, et à confronter au premier cycle de build observé.