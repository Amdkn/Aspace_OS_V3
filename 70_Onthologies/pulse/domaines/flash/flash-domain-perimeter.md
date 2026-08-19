---
type: Concept
title: Périmètre du domaine Flash — Product (03) et ses quatre frontières floues
description: Flash Product (03) couvre la productisation des besoins, la valeur d'artefact, et la qualification aval de l'offre. Quatre frontières ne sont pas scellées dans le canon : (a) Flash vs Sales — qui transforme l'engagement en livrable nommé, (b) Flash vs Ops — l'artefact est-il supportable, (c) Flash vs IT — le code tourne-t-il et récupère-t-il, (d) Flash vs Finance — la marge protège-t-elle le coût de build. Chaque frontière produit un arbitrage B2 Council prévisible.
tags: [flash, product, domain-03, perimeter, frontiere, arbitrage, b2-council, avengers]
generated: { by: minimax-m3, at: 2026-08-19T04:15:00Z }
verified:
  - { by: process:lecture-corpus-flash, at: 2026-08-19T04:15:00Z }
sources:
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Flash = 03 Product = Avengers
    last_modified: 2026-08-17
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — Flash Product (ligne 25 triplet)
    last_modified: 2026-08-19
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères cross-domaines
    last_modified: 2026-08-19
  - id: triplet-v3-line-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 17 — Flash pairedWith Avengers (7 techniciens : CaptainAmerica, IronMan, Thor, Hulk, BlackWidow, Hawkeye, ScarletWitch)"
    last_modified: 2026-08-17
  - id: triplet-v3-line-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
  - id: b3-veto-vocabulary
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary — Flash = PRODUCT_READY / NEEDS_SCOPE / BLOCKED_DELIVERY
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Périmètre du domaine Flash — Product (03) et ses quatre frontières floues

## Ce que Flash Product couvre exactement

Le domaine **03 Product** captainé par Flash couvre, dans la wheel 8-domain canonique :

- **La productisation des besoins** — la transformation d'un besoin identifié (par Growth ou Sales) en un artefact livrable, reproductible, dont la valeur est indépendante de la personne qui l'a construit. La matière première : un scope, un périmètre de besoin, un cahier des charges accepté.
- **La valeur d'artefact** — l'ensemble des propriétés qui font que l'artefact **tient sans son opérateur** : documentation, runbook, tests, critères d'acceptance chiffrés. C'est ce qui distingue Flash des trois autres « docteurs » (Batman Ops parle en *état*, Superman Growth en *promesse*, Wonder Woman Finance en *retour* — cf. `batman-doctrine-remonte-fait-non-decision.md` §« Le contraste avec les autres doctrines »).
- **La qualification aval de l'offre** — le fait que l'artefact peut être livré de manière répétitive (par Ops), déployé (par IT), et chiffré en marge (par Finance). C'est la raison pour laquelle Flash émet `PRODUCT_READY` quand l'artefact est supportable, `NEEDS_SCOPE` quand le besoin n'est pas formalisé, `BLOCKED_DELIVERY` quand le build ne tient pas la promesse de scope (cf. `b3-veto-and-signal-vocabulary.md`).

Ce périmètre est **l'aval de la transition Sales → Product** (implicite dans la matrice d'harmonisation, et **l'amont** des transitions Product → Ops et Product → IT — critères #3 et #4).

## La squad Avengers — sept techniciens, sept postures

Le triplet v3 ligne 17 identifie nommément **sept Avengers** :

| Agent | Spécialité inférée | Sister canon (H10/H30/H90) |
|---|---|---|
| **CaptainAmerica** | lead / orchestration (doctrine première ligne) | H30 — porte la discipline squad |
| **IronMan** | build technique, tooling, automation | H10 — exécution immédiate |
| **Thor** | intégration / connexion (API, webhooks) | H30 — interfaces transverses |
| **Hulk** | robustesse / charge / performance | H10 — résistance au stress |
| **BlackWidow** | QA / test / falsification | H30 — preuve d'inefficacité |
| **Hawkeye** | observation / métriques / signal | H30 — œil sur les indicateurs |
| **ScarletWitch** | transformation / mutation de scope | H90 — altération contrôlée |

Cette répartition est **projetée** à partir des noms canon Marvel et du pattern de fiche roster B3 (~400-470 mots, cf. `fifty-three-b3-agent-roster.md`). Aucune fiche `b3-*.md` individuelle n'a été lue dans cette distillation.

## Où Flash s'arrête — quatre frontières qui ne sont pas scellées

### Frontière 1 — Flash vs Sales (JohnJones)

Sales (JohnJones) promet une offre à un client. Flash doit la matérialiser. La frontière canonique est : Sales signe le deal, Flash produit l'artefact. Mais **qui définit le scope livrable** n'est pas tranché.

Cas concret : un client signe un deal pour « coaching IA premium ». Sales a promis une expérience « sur mesure ». Si Flash refuse la personnalisation au nom du veto offre-dépersonnalisée (cf. `flash-veto-offre-depersonnalisee.md`), le scope doit être **renégocié** avec le client. La frontière est franchie silencieusement si Flash accepte un scope nominatif pour ne pas perdre le deal — c'est précisément le cas que le veto est censé bloquer.

Le B2 Council arbitre en mode **negotiation** : le DoD du deal (Sales) et le DoD de l'artefact (Flash) sont tous deux légitimes et s'opposent.

### Frontière 2 — Flash vs Ops (Batman)

La matrice d'harmonisation critère #3 (`business-wheel-harmonization-matrix.md` §« Domain Pair Checks ») demande *« l'artefact est-il supportable opérationnellement ? »*. La frontière canonique est : Flash livre un artefact, Ops le maintient. Mais **qui porte la responsabilité de la boucle** (run, support, monitoring) n'est pas tranché.

Cas concret : un artefact Flash embarque une logique complexe (ex : scoring algorithmique). Batman refuse de le maintenir en run parce que la complexité dépasse la SOP support standard. Le Council arbitre en mode **handoff** : soit Flash documente davantage (runbook), soit Ops absorbe la complexité (formation squad), soit le scope de l'artefact est réduit.

### Frontière 3 — Flash vs IT (Cyborg)

La matrice critère #4 demande *« le produit tourne-t-il, déploie, récupère, est-il accessible ? »*. La frontière canonique est : Flash produit le code, Cyborg le déploie. Mais **qui porte la dette technique** (refactor, dépendance obsolète, dette de sécurité) n'est pas tranché.

Cas concret : Flash produit une feature qui dépend d'une librairie open-source devenue vulnérable. Cyborg refuse de la redéployer tant que le refactor n'est pas fait. Flash argue que le refactor n'est pas dans le scope signé. Le Council arbitre en mode **handoff** : la dette technique est dans le périmètre Cyborg (qui doit maintenir l'infra) ou dans le périmètre Flash (qui doit tenir la qualité) ?

### Frontière 4 — Flash vs Finance (Wonder Woman)

La matrice critère #6 demande *« le coût de build protège-t-il la marge ? »*. La frontière canonique est : Flash consomme un budget de build, Finance surveille la marge. Mais **qui arbitre entre la qualité de l'artefact et le coût de sa production** n'est pas tranché.

Cas concret : Wonder Woman oppose un veto-dépense récurrente sur un outil de monitoring nécessaire au support de l'artefact Flash. Flash argue que l'outil est dans le périmètre de qualité (post-veto canonique), Finance argue que c'est une dépense récurrente sans ROI. Le Council arbitre en mode **negotiation** : les deux DoDs sont légitimes et s'opposent.

## Pourquoi ces frontières existent dans le canon

Le canon V4 (OMK Business OS, Triptyque V4 ACTIVE 2026-07-15) positionne Flash en Product/03 avec squad Avengers (7 agents). Mais le triplet v3 ligne 17 cite une source unique (`VP_AGENT.md` Coach OS) — le substrat OMK B3 n'a pas de validation indépendante de l'effectif 7. C'est un **héritage de version** que le canon n'a pas re-tranché.

Conséquence pour le périmètre : Flash Product est le **nom opérationnel courant**, mais **deux hypothèses restent vivantes** : (a) le périmètre est strictement la productisation (lecture étroite), (b) le périmètre inclut aussi la maintenance transverse (lecture large). Le triplet 25 cite *« Flash bloque toute offre dont la valeur dépend d'une personne nommée »* — la lecture large du périmètre est cohérente avec un veto sur la **maintenance** (pas seulement le **build**).

## Les trois conséquences opérationnelles

1. **Chaque transition Product × Ops, Product × IT, Finance × Product, Legal × Product** doit **re-vérifier** le périmètre en amont. Le canon ne tranche pas les quatre frontières, le captain Flash tranche en séance.
2. **Le veto-offre-depersonnalisée** touche la frontière #1 (Sales) principalement. Il ne tranche pas les frontières #2-#4.
3. **L'amplification du veto** (cf. `b2-veto-amplification-cycle.md` §« Trois amplifications candidates ») projette une amplification Superman ; aucune amplification Flash n'est citée dans le triplet 58 — c'est une amplification candidate pour Council futur.

## Anti-pièges

- **Périmètre tenu pour acquis.** Si Flash accepte un mandat B1 « coaching sur mesure » parce que « CaptainAmerica peut le faire », il assume la frontière #1 sans l'arbitrer. Le packet mésoperpétuel doit déclarer le périmètre emprunté.
- **Veto catalogue utilisé pour bloquer toute personnalisation.** Le veto porte sur la valeur d'**offre** (commercialisée), pas sur la qualité de l'**artefact** (interne). Flash peut accepter un artefact « sur mesure » pour un client pilote sans contrevenir au veto — tant que l'**offre reproductible** reste non-dépendante d'une personne.
- **Confondre périmètre et responsabilité.** Flash est *Accountable* (A dans le RACI par rang — cf. `b2-pair-check-raci-by-rank.md`) sur les pair-checks où il est en aval — c'est la **transition vers** Product (Finance → Product, Legal → Product), pas le périmètre de Product lui-même. Voir `flash-pair-checks-dependencies.md`.

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 critères qui détectent les quatre frontières
- [[b2-eight-domain-vetoes-catalogue]] — le veto Flash ancré ligne 25
- [[b2-pair-check-raci-by-rank]] — la matrice RACI qui rend Flash Accountable sur Finance→Product et Legal→Product
- [[flash-veto-offre-depersonnalisee]] — le veto qui touche la frontière #1
- [[flash-pair-checks-dependencies]] — le détail des 4 couplages
- [[flash-red-flag-1-trigger]] — la conséquence si Ops/IT sont rouges pendant que Product est vert
- [[flash-doctrine-valeur-artefact]] — pourquoi Flash parle en valeur d'artefact
- [[flash-jtbd-emit-receive]] — les paquets JTBD émis/reçus par Avengers
- [[eight-domain-avengers-wheel]] — la cartographie 8-domaines V4

## Note de confiance

**Confirmé par machine, avec deux hypothèses non résolues.** Le mapping Flash = 03 Product = Avengers est confirmé par `eight-domain-avengers-wheel.md`, le triplet ligne 25, le triplet ligne 17 (verbatim), et le triplet ligne 17 source Coach OS V1. Les quatre frontières sont **reconstruites** à partir de la matrice d'harmonisation + le RACI par rang + la lecture des 4 pair-checks impliquant Product. La répartition 7-Avengers par spécialité est **projetée** à partir des noms canon Marvel et du pattern roster B3 — pas vérifiée par lecture de fiches individuelles.
