---
type: Concept
title: Batman — numérotation Coach OS 02 vs mapping canonique 04
description: Le corpus contient deux numérotations des 8 domaines B2 qui se contredisent. Coach OS (triplets 15-22) numérote Batman=02 (Opérations en Loops), Superman=05 (People & Brand), Aquaman=08 (Legal & Compliance). Le mapping canonique 8-domain numérote Ops=04, Growth=01, Legal=08. Le mapping canonique est la source de vérité — mais Coach OS est la doctrine de référence du B1. Une discipline canonique s'impose.
tags: [numerotation, coach-os, mapping-canonique, batman, ops, divergence, source-verite]
generated: { by: minimax-m3, at: 2026-08-19T04:00:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:00:00Z }
sources:
  - id: triplet-coach-os-rang1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 15 — Green Lantern pairedWith x-men (domaine 1 — RH & Méta Gouvernance)"
    last_modified: 2026-08-17
  - id: triplet-coach-os-batman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 16 — Batman pairedWith fantastic-four (domaine 2 — Opérations en Loops)"
    last_modified: 2026-08-17
  - id: triplet-coach-os-flash
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 17 — Flash pairedWith avengers (domaine 3 — Productization)"
    last_modified: 2026-08-17
  - id: triplet-coach-os-martian
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 18 — Martian Manhunter pairedWith illuminati (domaine 4 — Sales & Cognition)"
    last_modified: 2026-08-17
  - id: triplet-coach-os-superman
    resource: "C:/Users/ado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 19 — Superman pairedWith guardians (domaine 5 — People & Brand)"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Ops=04, People=07
    last_modified: 2026-08-17
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — neuf pair-checks avec Ops=#3 et #4
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Batman — numérotation Coach OS 02 vs mapping canonique 04

## Les deux numérotations

Le corpus lu porte **deux numérotations des 8 domaines B2** qui ne
s'alignent pas.

### Numérotation Coach OS (triplets 15-22)

Dérivée des `VP_AGENT.md` de Coach OS
(`04_Business_Domains/0X_*_VP/VP_AGENT.md`). Ordre local :

| Coach OS | Capitaine | Squad | Triplet |
|---|---|---|---|
| 01 | Green Lantern | X-Men | 15 |
| 02 | **Batman** | **Fantastic Four** | **16** |
| 03 | Flash | Avengers | 17 |
| 04 | Martian Manhunter | Illuminati | 18 |
| 05 | Superman | Guardians | 19 |
| 06 | Wonder Woman | Thunderbolts | 20 |
| 07 | Cyborg | Kang Dynasty | 21 |
| 08 | Aquaman | Eternals | 22 |

### Numérotation canonique 8-domain (mapping Avengers Wheel)

Dérivée de `eight-domain-avengers-wheel.md` et de la matrice
d'harmonisation. Ordre canonique :

| Canon | Domaine | Capitaine | Squad |
|---|---|---|---|
| 01 | Growth | Superman | Guardians |
| 02 | Sales | JohnJones (W40 V4) | Illuminati |
| 03 | Product | Flash | Avengers |
| **04** | **Ops** | **Batman** | **Fantastic Four** |
| 05 | IT | Cyborg | Kang Dynasty |
| 06 | Finance | Wonder Woman | Thunderbolts |
| 07 | People | Green Lantern | X-Men |
| 08 | Legal | Aquaman | Eternals |

## Les contradictions entre les deux

Batman est **02** dans Coach OS et **04** dans le canon. Mais
l'important n'est pas Batman seul — c'est la **rotation** complète :

- **Superman** : 05 (Coach OS, People & Brand) ↔ 01 (canon, Growth)
- **Green Lantern** : 01 (Coach OS, RH) ↔ 07 (canon, People)
- **Cyborg** : 07 (Coach OS, R&D & IT) ↔ 05 (canon, IT)
- **JohnJones / Martian Manhunter** : 04 (Coach OS, Sales) ↔ 02
  (canon, Sales)

Lequel a la bonne position ? Lequel a le bon intitulé ? Lequel a la
bonne squad ? Les **appariements capitaine↔squad** sont stables
entre les deux numérotations (Batman↔Fantastic Four, Superman↔Guardians,
etc.). Ce qui change, c'est :

1. **L'ordre des domaines** dans la wheel.
2. **L'intitulé** de certains domaines (Coach OS *« People & Brand »*
   vs canon *« Growth »* pour Superman).
3. **Le périmètre** de certains domaines (Coach OS rattache Brand à
   Superman ; canon rattache Brand à Growth — débat non tranché).

## Quelle numérotation fait foi ?

**Le mapping canonique 8-domain.** Trois raisons :

1. **Il est cité par 4 sources** — `eight-domain-avengers-wheel.md`
   pose le mapping ; `business-wheel-harmonization-matrix.md` pose les
   pair-checks #1 à #9 avec Ops=03/04 ; `fifty-three-b3-agent-roster.md`
   confirme Ops=Batman=Fantastic4=~4 ; la doctrine D4 append-only
   pose le format packet mésoperpé qui cite *« impacted_domains »*
   avec growth/sales/product/ops/it/finance/people/legal.
2. **Il est utilisé par le B2 Council** — la routine du Council
   (`b2-council-arbitrage-rule.md`) parle de *« 8 hero-managers B2 »*
   sans imposer un ordre ; les pair-checks de la matrice sont
   numérotés dans l'ordre canonique.
3. **Coach OS est un cas particulier** — Coach OS est une Franchise
   Prototype du Business OS, **pas** le canon. La phrase
   `coach-os.md` ligne 1 est *« Coach OS est la première Franchise
   Prototype du Business OS »*. La numérotation Coach OS est
   **interne au projet**, pas canonique.

## La contradiction supportée — pourquoi ce n'est pas un drame

Les deux numérotations **ne se contredisent pas sur le fond** — elles
divergent sur l'**ordre** et sur **l'intitulé** de certains domaines.
L'appariement capitaine↔squad est identique. Le périmètre Batman
(Opérations en Loops) est le même dans les deux (Ops = boucle, Ops =
procédure, Ops = condition d'arrêt).

Conséquence pratique : **on peut citer Batman comme 02 ou 04 sans
perdre le sens**, tant qu'on ne mélange pas les deux numérotations
dans le même document. La règle que je propose :

- Dans les **packets mésoperpétuels** et la **matrice
  d'harmonisation** : utiliser la numérotation canonique (04).
- Dans les **documents Coach OS** (`VP_AGENT.md`, dossiers Coach OS)
  : utiliser la numérotation Coach OS (02).
- Dans les **concepts OKF transverses** (comme celui-ci) : citer les
  deux, marquer Coach OS comme *« local »* et le mapping canonique
  comme *« canonique »*.

## Le débat ouvert — People & Brand vs Growth

La divergence la plus有意思 n'est pas la numérotation — c'est
**l'intitulé** de Superman :

- **Coach OS** : *« People & Brand »* — Superman couvre People **et**
  Brand. Brand est la dimension publique, marketing, communication.
- **Canon** : *« Growth »* — Superman couvre Growth (attention,
  traction, marketing d'acquisition).

La différence est dans la **direction** : Coach OS *« People & Brand »*
place Superman au centre de la People (les personnes qui portent la
marque). Canon *« Growth »* place Superman au centre de l'attention
(la marque au service de la traction).

Ces deux lectures ne sont pas incompatibles — **une marque forte EST
un actif Growth, et les People qui la portent sont son vecteur**. Mais
la numérotation différente reflète deux doctrines : Coach OS voit
Brand comme un sous-domaine People ; le canon voit Brand comme un
sous-domaine Growth. Lequel est correct ? Le canon, probablement —
parce que les pair-checks #1 (Growth×Sales), #5 (Finance×Growth), #7
(Legal×Growth) placent la brand au croisement de Growth et Sales, pas
de People.

**Mais** — la position Coach OS n'est pas absurde. Si Summers (CEO)
considère que la marque est un actif People (les clients, les
ambassadeurs, les témoignages), alors People & Brand est un domaine
unique. C'est une décision de cycle, pas une décision opérationnelle —
c'est **Summers** qui tranche.

## Anti-pièges

- **Citer Batman comme 02 sans préciser *« Coach OS »*.** Risque de
  confusion. Le 02 est Coach OS local ; le 04 est canonique.
- **Citer Batman comme 04 sans préciser *« mapping 8-domain »*.**
  Symétrique. Le 04 n'est pas Coach OS.
- **Mélanger les deux numérotations dans le même packet.** Un packet
  mésoperpétuel qui cite Ops=02 et People=01 dans le même champ
  `impacted_domains` est illisible — le scan ne sait plus quelle
  wheel est active.
- **Trancher le débat People & Brand vs Growth.** C'est une décision
  de cycle (Summers), pas une décision Batman (Ops) ou Superman
  (Growth). Batman remonte le constat, il ne statue pas.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Batman, indépendant de la numérotation
- [[batman-veto-condition-arret-procedure]] — le veto Batman, identique dans les deux numérotations
- [[eight-domain-avengers-wheel]] — la source canonique du mapping 04
- [[b2-harmonization-matrix-exploitable]] — les 9 pair-checks qui utilisent le 04 canonique

## Note de confiance

**Confirmé par machine pour les deux numérotations.** Les triplets
15-22 sont cités verbatim pour Coach OS. Le tableau canonique est
tiré verbatim de `eight-domain-avengers-wheel.md`. La préférence
pour le canon est **mon raisonnement**, motivé par 3 arguments
(multi-sources, usage B2 Council, statut Coach OS = Franchise
Prototype). Le débat People & Brand vs Growth est **mon inférence** —
il relie les deux intitulés Superman, mais ne tranche pas la
question de cycle.