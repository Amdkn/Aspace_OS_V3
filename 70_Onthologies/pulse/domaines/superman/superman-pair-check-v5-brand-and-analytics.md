---
type: Concept
title: V5 matrice d'harmonisation — deux pair-checks supplémentaires #11 Brand (People↔Growth) et #12 Analytics (Growth↔IT)
description: La matrice d'harmonisation V4 (9 pair-checks canoniques) ignore deux couplages révélés par la lecture critique : Superman↔People Brand transverse et Superman↔IT analytics stack. La V5 propose deux pair-checks supplémentaires #11 People→Growth (Brand doctrine) et #12 IT→Growth (analytics stack). RACI Superman A sur #11 (Brand aval — il exécute), Cyborg A sur #12 (IT aval — il déploie). Procédure d'amendement unanimité + B1.
tags: [superman, growth, harmonization, v5, pair-check, brand, analytics, amendment]
generated: { by: minimax-m3, at: 2026-08-19T06:45:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-3, at: 2026-08-19T06:45:00Z }
sources:
  - id: harmonization-v4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation V4 — 9 critères + 5 red flags
    last_modified: 2026-08-19
  - id: domain-perimeter-tour1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/domain-perimeter.md"
    title: Périmètre Superman tour 1 — 3 frontières floues (Brand #2, IT #3)
    last_modified: 2026-08-19
  - id: pair-checks-dependencies-tour1
    resource: "C:/Users/ado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/pair-checks-dependencies.md"
    title: Superman couplages cross-domaines — 3 pair-checks canoniques + 2 hors matrice
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — A = B2 en aval, R = B3
    last_modified: 2026-08-19
  - id: v4-vs-v1-arbitration
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-v4-vs-v1-arbitration-rule.md"
    title: V4 vs Coach OS V1 — règle d'arbitrage de la divergence triplet 19
    last_modified: 2026-08-19
okf_version: "0.2"
---

# V5 matrice d'harmonisation — deux pair-checks supplémentaires

## Le constat — la matrice V4 ignore deux couplages réels

`b2-harmonization-matrix-exploitable.md` pose **9 critères
cross-domaines** V4. Le tour 1 Superman (`domain-perimeter.md`
+ `pair-checks-dependencies.md`) a documenté **3 pair-checks
canoniques** qui touchent Superman (#1 Growth→Sales, #5
Finance→Growth, #7 Legal→Growth) et **2 couplages hors matrice**
qui existent en pratique mais ne sont pas testés :

1. **Couplage Superman ↔ People (Brand transverse)** — la
   doctrine Brand reste People (Green Lantern, V4 canonique)
   mais Superman exécute via StarLord_Story et Groot_Content.
   Cf. `domain-perimeter.md` §« Frontière #2 ».
2. **Couplage Superman ↔ IT (analytics stack)** — l'analytics
   stack (Mixpanel, Amplitude, PostHog) est Cyborg (déploiement)
   mais Superman consomme (lecture, configuration événements).
   Cf. `domain-perimeter.md` §« Frontière #3 ».

Le triplet 19 (Coach OS V1) cite *« Superman = People & Brand »*
— héritage V1 non-superseded. Cette **cohabitation
lecture-V4/lecture-V1** n'est pas tranchée par la matrice V4.

**Conséquence** : les arbitrages Council qui touchent Brand ou
Analytics n'ont pas de pair-check matrice pour tester le
transfert. Ils passent en mode `negotiation` systématique, ce
qui alourdit le Council.

## La V5 matrice — proposition de 2 pair-checks supplémentaires

### Pair-check #11 — People (Brand doctrine) → Growth (Brand execution)

| Champ | Valeur |
|---|---|
| **Source en amont** | Brand (doctrine transverse, People) |
| **Source en aval** | Growth (exécution Brand via StarLord/Groot) |
| **Question de garde** | La doctrine Brand reste-t-elle People quand Growth l'exécute ? |
| **RACI** | A = B2 People (Green Lantern), R = B3 Guardians (StarLord/Groot), C = B2 Growth (Superman), I = B1, B3 X-Men |
| **Red flag associé** | Aucun canon — proposition : *« Brand growth vert avec People brand rouge : arbitrer le périmètre Brand avant toute campagne publique »* |

**Asymétrie volontaire par rapport au RACI canonique** :
Superman est **Consulted** ici, pas Accountable. C'est
l'inverse du pattern *« A = B2 en aval »* — pour Brand,
**People reste Accountable** même si Growth exécute. La
justification : le Brand est une doctrine transverse
(canonicité, ton, registre narratif) que seul People tient.
Superman **exécute**, mais n'**arbitre pas**.

### Pair-check #12 — IT (analytics deployment) → Growth (analytics consumption)

| Champ | Valeur |
|---|---|
| **Source en amont** | Analytics stack (Cyborg IT, déploiement + monitoring) |
| **Source en aval** | Growth (Superman, configuration événements + lecture données) |
| **Question de garde** | L'analytics stack reste-t-il sous souveraineté IT quand Growth le consomme ? |
| **RACI** | A = B2 IT (Cyborg), R = B3 Kang Dynasty (Nebula_Analytics ou analogue), C = B2 Growth (Superman), I = B1, B3 Guardians |
| **Red flag associé** | Proposition : *« IT analytics vert avec Growth consumption rouge : limiter la lecture Growth aux dashboards publiés »* |

**Asymétrie volontaire** : Superman est **Consulted**, pas
Accountable, sur le stack lui-même. Cyborg reste A parce que
la souveraineté infra (déploiement, monitoring, souveraineté
données) est Cyborg. Superman **consomme** l'analytics mais
ne le **possède** pas.

## Pourquoi passer de 9 à 12 pair-checks, et pas rester à 9

Trois raisons :

### 1. Les couplages Brand/Analytics existent en pratique

`pair-checks-dependencies.md` §« Les couplages non canoniques
que la matrice ne montre pas » les décrit explicitement. Une
matrice qui ignore un couplage réel produit des arbitrages
Council systématiquement en mode `negotiation` parce que
aucun test prede le transfert. Ajouter 2 pair-checks **réduit**
la charge Council.

### 2. Le RACI canonique a une exception naturelle

Le tableau RACI canonique pose *« A = B2 en aval de la
transition »* (cf. `b2-pair-check-raci-by-rank.md` §« Pourquoi
A = B2 en aval, pas B1 »). Les pair-checks #11 et #12 sont
des exceptions **justifiées** : A reste People pour #11 (la
doctrine Brand) et IT pour #12 (la souveraineté analytics).
Documenter les exceptions dans la matrice **réduit** le
besoin de les re-justifier à chaque arbitrage.

### 3. La V5 reste dans le format canonique

Ajouter 2 lignes au tableau des 9 critères existants ne casse
pas la structure. Le format *« source amont → source aval →
question de garde »* reste canonique. Le RACI par rang
(référence `b2-pair-check-raci-by-rank.md`) s'applique
tel quel.

## La procédure d'amendement V4 → V5

Le format canonique matrice V4 → V5 n'est pas documenté. Par
lecture critique de `b2-council-arbitrage-rule.md` §« Quand le
Council escalade à B1 », la procédure inférée est :

```
draft V5 (pair-checks #11 et #12)
   ↓
séance hebdomadaire B2 Council
   ↓
   unanimité 8/8 requise (réécriture matrice, pas amplification)
   ↓
   + validation B1 (la matrice est un outil de cycle)
   ↓
effet : V5 substituée à V4, red flags #6 et #7 ajoutés
         au catalogue canonique
```

**Trois barrières**, pas une seule :

1. **Unanimité 8/8** au Council — un captain peut bloquer
   (ex : Cyborg refuse #12 parce que ça absorbe Nebula_Analytics
   trop vite).
2. **Validation B1** — B1 doit accepter la modification de la
   matrice, parce que la matrice conditionne les arbitrages
   cycle.
3. **Append-only D4** — V4 reste dans son état. V5 est un
   **nouveau fichier** (`v5-harmonization-matrix.md`), pas
   une édition de V4.

**C'est plus strict qu'une amplification de veto** (qui
demande 5/8 simple). Une matrice est **un outil de cycle**,
pas une doctrine — sa modification est plus sensible.

## Le cas asymétrique — Superman A resterait-il légitime ?

Une objection possible : *« si Superman est A sur Finance →
Growth (#5) et Legal → Growth (#7), pourquoi n'est-il pas A
sur People → Growth (#11) et IT → Growth (#12) ? »*

Réponse : parce que **Brand et Analytics sont des doctrines
transverses**, pas des outputs croissance. La règle A = B2
en aval s'applique aux **outputs** (Finance produit une
dépense récurrente → Superman la consomme). Brand et
Analytics sont des **inputs doctrinaux** que Superman consomme
sans les produire.

C'est une **distinction subtile** que la V5 doit rendre
explicite. Si la V5 pose Superman A sur #11 et #12, elle
brise la cohérence — Superman devient A sur 4 pair-checks
entrants, ce qui est asymétrique par rapport aux autres
capitaines.

## Le timing de soumission V5

Trois moments où la V5 peut être soumise :

### Timing A — Quand un arbitrage Brand/Analytics touche Superman

Le Council peut saisir l'occasion d'un arbitrage Brand
spécifique pour proposer la V5. Risque : mélanger arbitrage
spécifique et modification matrice.

### Timing B — Quand 1+ capitaine le demande en séance

Si un capitaine (typiquement Green Lantern ou Cyborg)
demande la V5, le président de séance inscrit à l'ordre du
jour. Risque : créer un précédent où la matrice est
ré-écrite à la demande.

### Timing C — Cycle de revue matrice

`b2-harmonization-matrix-exploitable.md` §« Cadence de revue »
pose trois contexts de ré-évaluation : hebdomadaire pendant
build actif, immédiatement avant launch, après B3 blocker
cross-domaine. **Pas** de cycle de revue matrice dédié.

Le timing recommandé : **proposer la V5 lors d'un arbitrage
Brand/Analytics réel** (timing A). Si un tel arbitrage ne
survient pas dans les 6 mois,forcer le timing C par une
séance dédiée.

## Les trois contre-arguments possibles

### « La matrice canonique V4 suffit — les arbitrages Brand/Analytics passent en negotiation »

Réponse : la negotiation fonctionne mais charge le Council.
La V5 **réduit** la charge en rendant les arbitrages
systématiques `parallel` ou `handoff` au lieu de
`negotiation`.

### « People et IT peuvent absorber Brand/Analytics dans leur propre scope »

Réponse : Superman **exécute** déjà Brand via StarLord/Groot
et Analytics via dashboards. La V5 ne **crée** pas la
dépendance, elle la **teste**. Sans V5, les arbitrages
Council traitent la dépendance **au cas par cas**, sans
matrice commune.

### « 9 pair-checks, c'est déjà beaucoup »

Réponse : le format tabulaire est conçu pour scaler (le
catalogue 8 vetos a le même principe — 8 lignes, ajoutables).
Ajouter 2 lignes ne casse pas la lisibilité.

## Anti-pièges

- **V5 imposée sans unanimité 8/8.** Refusée — c'est une
  réécriture matrice, pas une amplification. Un captain
  hostile peut bloquer en séance.
- **V5 sans validation B1.** Refusée — B1 doit accepter la
  modification de matrice comme outil de cycle.
- **V5 qui réécrit V4 (édition in-place).** Refusée par D4.
  V5 est un **nouveau fichier**, V4 reste dans son état.
- **V5 qui pose Superman A sur #11 et #12.** Refusée par
  symétrie avec RACI canonique. A reste People sur #11, IT
  sur #12. Superman Consulted.
- **V5 saisie par Superman seul.** Refusée par procédure
  (8/8 + B1). Superman propose, mais ne tranche pas.

## Liens

- [[b2-harmonization-matrix-exploitable]] — la matrice V4
- [[domain-perimeter]] — les 3 frontières Brand/IT/People
- [[pair-checks-dependencies]] — les 2 couplages non canoniques
- [[b2-pair-check-raci-by-rank]] — le RACI par rang canonique
- [[b2-council-arbitrage-rule]] — quand escalader B1
- [[superman-v4-vs-v1-arbitration-rule]] — le triplet 19 et
  la marque Brand transverse

## Note de confiance

**Reconstruit, à moitié étayé.** Les 3 pair-checks V4 qui
touchent Superman sont tirés verbatim de la matrice canonique
+ RACI par rang. Les 2 couplages non canoniques (Brand,
Analytics) sont projetés depuis `pair-checks-dependencies.md`
+ le triplet 19 (Coach OS V1). La procédure d'amendement
unanimité 8/8 + B1 est **reconstruite** par lecture critique
de `b2-council-arbitrage-rule.md` — le format matrice V4 →
V5 n'est pas documenté ailleurs dans le corpus. Le cas
asymétrique Superman A reste légitime est **projeté** par
distinction outputs/inputs doctrinaux. Les 3 contre-arguments
sont **reconstruits** par lecture critique des anti-pièges
génériques matrice. Le timing A recommandé est **projeté**
par lecture des contextes de ré-évaluation canoniques.
