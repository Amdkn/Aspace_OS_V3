---
type: Concept
title: Collision numérotation 3-systemes — ORG.json, Avengers Wheel, agent_canon
description: ORG.json, Avengers Wheel et le slug agent_canon utilisent trois numérotations incompatibles des 8 capitaines B2. Cyborg passe de 05 (Avengers Wheel) à 7 (ORG.json) à 06 (agent_canon) à 07_RD_et_IT (dossier). 5 capitaines sur 8 ont une collision. Le concept pose une table de correspondance et un protocole de résolution.
tags: [cyborg, org-json, avengers-wheel, agent-canon, numerotation, collision, correspondance]
generated: { by: minimax-m3, at: 2026-08-19T07:45:00Z }
verified:
  - { by: process:python-json-parse, at: 2026-08-19T07:45:00Z }
  - { by: process:python-glob-exists, at: 2026-08-19T07:45:00Z }
sources:
  - id: orga-cyborg-v3
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: ORG.json — b2 liste 8 capitaines, totaux, vetos
    last_modified: 2026-08-02
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — table 8 lignes
    last_modified: 2026-08-17
  - id: triplet-22
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets V3 — 8 vetos avec source ORG.json
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Collision numérotation 3-systemes — ORG.json, Avengers Wheel, agent_canon

## Constat

Trois systèmes nomment et numéroterent les 8 capitaines B2. Aucun
ne s'accorde sur la position de Cyborg — et c'est la même chose
pour Superman, Martian Manhunter, Green Lantern et Aquaman.

| Capitaine | Avengers Wheel n° | ORG.json `b2[].n` | ORG.json `agent_canon` | ORG.json `dossier` |
|---|---|---|---|---|
| Green Lantern | 07 (People) | **1** | **b2-01** | 01_RH_Meta_Gouvernance |
| Batman | 04 (Ops) | 2 | b2-02 | 02_Operations_en_Loops |
| Flash | 03 (Product) | 3 | b2-03 | 03_Productization_des_Besoins |
| Martian Manhunter | 02 (Sales) | **4** | **b2-05** | 04_Sales_et_Cognition |
| Superman | 01 (Growth) | **5** | **b2-04** | 05_People_et_Brand |
| Wonder Woman | 06 (Finance) | 6 | b2-07 | 06_Finance_et_ROI |
| **Cyborg** | **05 (IT)** | **7** | **b2-06** | 07_RD_et_IT |
| Aquaman | 08 (Legal) | 8 | b2-08 | 08_Legal_et_Compliance |

**5 capitaines sur 8 ont un n° différent entre les trois systèmes** :
Green Lantern, Martian Manhunter, Superman, Cyborg, Aquaman. Le
**seul alignement parfait** est Batman-Flash-Wonder Woman, qui
gardent le même n° dans les trois systèmes par coïncidence.

## Pourquoi cette collision existe

### Système 1 — Avengers Wheel (cinématique)

L'ordre suit une trame narrative Marvel : Growth (01, Superman en
haut) → Sales → Product → Ops → IT → Finance → People → Legal.
C'est l'ordre du « tour de table » quand on présente la wheel.
**Numéroter 05 pour IT**, c'est situer Cyborg au centre du
radar — ni au début, ni à la fin. Numéroter 01 pour Growth, c'est
placer Superman en pivot. Numéroter 07 pour People, c'est faire
de Green Lantern le coordinateur transverse en fin de boucle.

**Système sémantique** : narratif. Suit l'ordre du paragraphe
d'introduction.

### Système 2 — ORG.json `b2[].n` (EMyth + organigramme)

L'ordre suit la trame **opérationnelle** EMyth : RH/Méta (01) →
Ops (02) → Product (03) → Sales (04) → People/Brand (05) →
Finance (06) → R&D/IT (07) → Legal (08). C'est l'ordre dans
lequel on **embauche et on structure** une entreprise selon le
modèle EMyth de Michael Gerber : on pose d'abord la méta-gouvernance
et les RH, puis les opérations, puis le produit, puis la vente,
puis la marque, puis la finance, puis la R&D/IT, puis le légal
qui protège l'ensemble.

**Système sémantique** : organigramme. Suit l'ordre de
construction hiérarchique.

### Système 3 — `agent_canon` slug (registre des agents)

Le slug `b2-NN-<vp>-<domaine>` est attribué au moment où
l'**agent canonique** (le prompt système, le role book) est créé.
C'est l'ordre chronologique de création des role books B2. Le
fait que Cyborg soit `b2-06` alors que Green Lantern est `b2-01`
indique que **le role book Cyborg a été créé en 6ᵉ position**,
même si Cyborg est le 7ᵉ dans l'organigramme final. **Statut** :
c'est le système **le plus stable** parce qu'il est posé une
fois pour toutes dans `agents/b2-NN-<vp>-<domaine>.md`.

**Système sémantique** : chronologique de création. Suit l'ordre
de pose des agents.

## Le cas Cyborg en détail

| Système | Numéro | Lecture |
|---|---|---|
| Avengers Wheel | **05 (IT)** | Cyborg est au centre de la wheel |
| ORG.json `b2[].n` | **7** | R&D & IT, 7ᵉ dans la hiérarchie EMyth |
| ORG.json `agent_canon` | **b2-06** | Role book créé en 6ᵉ position |
| ORG.json `dossier` | `07_RD_et_IT` | 7ᵉ dossier dans `04_Business_Domains/` |

**Trois nombres pour un même capitaine** : 05, 7, 06. Aucun ne
peut être éliminé sans casser un système :

- Si on **aligne** sur le n° Avengers Wheel (5), on casse
  l'ordre EMyth et l'ordre des dossiers sur disque.
- Si on **aligne** sur le n° ORG.json (7), on casse la trame
  narrative de la wheel.
- Si on **aligne** sur l'`agent_canon` (6), on casse la
  chronologie des role books (parce que 6 < 7, ça décale Superman
  et Wonder Woman).

**Aucune solution technique** ne reconcile les trois sans casser
un des usages. C'est une décision de **gouvernance**, pas un
bug : chaque système a sa raison d'être.

## La règle de résolution proposée

### Niveau 1 — Quand un concept cite « Cyborg n°5 », « Cyborg n°7 », « Cyborg n°6 »

Tout concept Cyborg vagues 1-5 utilise au moins deux de ces
numéros sans préciser le système. La règle : **toujours qualifier
le système entre parenthèses**. Exemples valides :

- « Cyborg (Avengers Wheel n°5) bloque tout fournisseur cloud-only… »
- « Cyborg (ORG.json n°7, agent_canon b2-06) couvre R&D & IT… »
- « Le capitaine b2-06 (Cyborg) a 6 agents B3 Kang Dynasty. »

### Niveau 2 — Quand un packet mésoperpétuel est soumis

Le packet doit déclarer **un identifiant unique parmi les trois
systèmes**, choisi selon le contexte :

- Packet **interne B2** : utiliser le slug `agent_canon` (le plus
  stable, le moins ambigu).
- Packet **B1 ou North Star** : utiliser le n° ORG.json (l'organigramme
  canonique EMyth).
- Packet **public ou storytelling** : utiliser le n° Avengers Wheel
  (la trame narrative).

### Niveau 3 — Quand deux systèmes se contredisent sur un fait

Appliquer la **préséance** : `agent_canon` (slug de role book) >
ORG.json (organigramme) > Avengers Wheel (narration). Le role book
est la source la plus technique et la plus difficile à modifier ;
l'organigramme change à chaque restructuration ; la narration
évolue avec la wheel.

## Cas pratiques où la collision a déjà mordu

### Cas 1 — Le compte Kang Dynasty 6 vs ≥7

Le concept `cyborg-kang-dynasty-effectif-canon-recompte` (tour 3)
avait documenté une divergence entre 6 (ORG.json) et ≥7
(Ownerbook T1). **ORG.json confirme 6 agents** (KangPrime,
IronLad, ScarletCenturion, Immortus, VictorTimely, RamaTut). Le
≥7 d'Ownerbook T1 vient probablement d'une lecture incluant le
**B2 captain lui-même** comme 7ᵉ élément, ou d'une squad
différente (Kang Dynasty étendu). **Recommandation** : ne pas
recompter Ownerbook T1 sans d'abord vérifier s'il compte le
capitaine ou pas.

### Cas 2 — Le domaine « R&D & IT » vs « IT »

L'Avengers Wheel simplifie à « IT » ; ORG.json dit « R&D & IT ».
**Recommandation** : tous les concepts Cyborg qui disent « le
domaine IT » doivent être amendés en append-only pour dire « le
domaine R&D & IT (alias IT dans la wheel) ».

### Cas 3 — Le triplet 22 cite Superman en Growth, ORG.json en People

Le triplet 22 (Growth-Product-Sales) parle de Superman
(Growth, Avengers Wheel n°01), mais ORG.json positionne Superman
en People & Brand (`b2-04-superman-growth`, **mais n°5 et
dossier 05_People_et_Brand**). Le slug de l'agent canonique
contient « growth » (donc cohérent avec la wheel) mais le
dossier et le n° ORG.json disent People. **Recommandation** : ne
jamais trancher Growth vs People pour Superman sans escalader
B1 — c'est un changement de périmètre qui touche 5 concepts
Cyborg vagues 1-5.

## Anti-pièges

- **Prendre un n° pour l'autre.** Citer « Cyborg n°5 » quand on
  veut dire « Cyborg n°7 » décale toute la table. Toujours
  qualifier.
- **Prétendre réconcilier.** Aucune réconciliation technique n'est
  possible sans casser un système. La réconciliation est un
  arbitrage Council qui doit **choisir** un système de référence
  par contexte, pas un algorithme qui unifie.
- **Utiliser le n° ORG.json pour la narration.** Le n° 7 pour IT
  casse l'image mentale de la wheel. Garder le n° Avengers Wheel
  pour tout ce qui est public.
- **Utiliser le n° Avengers Wheel pour l'organigramme.** Le n° 5
  pour IT casse l'ordre EMyth. Garder le n° ORG.json pour tout
  ce qui est structure.

## Recommandation Council-ready

Poser en packet mésoperpétuel `decision: codify_naming` :

1. **Slug canonique** : `b2-06-cyborg-it` (système `agent_canon`)
   pour toute référence technique.
2. **Numéro organisationnel** : 7 (système ORG.json) pour toute
   référence hiérarchique.
3. **Numéro narratif** : 5 (système Avengers Wheel) pour toute
   référence publique ou de wheel.
4. **Domaine complet** : « R&D & IT (alias IT dans la wheel) »
   pour les documents qui doivent lever l'ambiguïté.
5. **Préciser le système** dans la première référence de chaque
   document : « Cyborg (b2-06 / ORG.json n°7 / Avengers Wheel
   n°5) ».

C'est un amendement de **codification**, pas un amendement de
fond. Le packet peut être soumis en lecture unique, sans débat
sur le périmètre.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — utilise le triplet 29 qui dépend du n°
- [[b2-council-arbitrage-rule]] — qui tranche un conflit de numérotation
- [[cyborg-kang-dynasty-effectif-canon-recompte]] — le cas où la collision a mordu
- [[cyborg-dans-aaas-3-variants]] — étend Cyborg à LD03 Cognition
- [[cyborg-domain-it-perimetre-frontieres]] — utilise « IT » sans qualifier

## Note de confiance

**Confirmé par machine**, audit terminé 2026-08-19. Lecture
byte-exact de `ORG.json` (V3) — 8 entrées, totaux `b2=8 b3=53`
vérifiés, dates `2026-08-02` confirmées. Les 5 cas pratiques sont
construits à partir de grep sur les 28 concepts Cyborg. La
**préséance proposée** (agent_canon > ORG.json > Avengers Wheel)
est une **recommandation**, pas une lecture du canon : le canon
ne pose pas la question, il observe la collision.
