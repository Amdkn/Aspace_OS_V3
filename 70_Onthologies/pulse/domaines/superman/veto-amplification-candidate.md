---
type: Concept
title: Veto Superman — amplification candidate "date ou horizon mesurable"
description: Le triplet 58 (Wonder Woman étend) montre qu'un veto peut être amplifié par ajout d'une exigence supplémentaire, à majorité simple 5/8 du B2 Council. Pour Superman, l'amplification candidate est "toute promesse publique doit indiquer une date de livraison ou un horizon mesurable". Cette amplification transforme un veto difficile à opérationnaliser (pratique de delivery) en un veto vérifiable par artefactual daté.
tags: [superman, growth, veto, amplification, doctrine, extension, council]
generated: { by: minimax-m3, at: 2026-08-19T04:04:00Z }
verified:
  - { by: process:lecture-corpus-superman, at: 2026-08-19T04:04:00Z }
sources:
  - id: veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — triplet 58 verbatim
    last_modified: 2026-08-19
  - id: triplet-v3-line-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 58 — Wonder Woman étend la doctrine veto-dépense"
    last_modified: 2026-08-17
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — propriétés (catégoriel, vérifiable, non-négociable)
    last_modified: 2026-08-19
  - id: council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence, présidence tournante, quorum 5/8
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Veto Superman — amplification candidate "date ou horizon mesurable"

## Le signal canonique — triplet 58

`b2-veto-amplification-cycle.md` cite verbatim le triplet 58 :

> *« Wonder Woman étend la doctrine veto-dépense : corrélat direct
> avec la dette récurrente — chaque ligne doit porter une métrique
> de retour chiffrée. »*

Le verbe **« étend »** est la clé. Le triplet 28 donne le veto
canonique de Wonder Woman. La diff entre les deux triplets est
**exactement l'amplification** : *chaque ligne doit porter une
métrique de retour chiffrée* est plus strict que le veto canonique
mais dans la même catégorie (dépense récurrente).

## L'amplification candidate pour Superman

`b2-veto-amplification-cycle.md` §« Trois amplifications candidates »
liste **explicitement** Superman comme projection :

| Capitaine | Veto canonique | Amplification candidate | Source implicite |
|---|---|---|---|
| Superman (Growth) | promesse publique que la delivery ne tient pas | la promesse doit indiquer une date de livraison ou un horizon mesurable | inférence depuis la doctrine `b2-council-cadence-and-chair.md` §« Pourquoi la présidence tournante » |

**Lecture explicite** :

> *Veto canonique : Superman bloque toute prise de parole publique
> qui promet un résultat que la delivery ne tient pas. En outre,
> toute promesse publique doit indiquer une date de livraison ou
> un horizon mesurable.*

Le format est exactement celui de la triple 58 :

> *« Veto canonique. En outre, {nouvelle exigence}. »*

## Pourquoi cette amplification est défendable

Trois raisons :

### 1. Elle rend le veto **vérifiable**

`b2-eight-domain-vetoes-catalogue.md` pose **3 propriétés** d'un
veto légitime : catégoriel, vérifiable, non-négociable au niveau
mésoperpétuel. Le veto Superman canonique **manque** la propriété
*vérifiable* — cf. `veto-catalogue-concrete.md` §« Pourquoi le veto
Superman est le plus difficile à opérationnaliser ».

L'amplification candidate **restaure** la vérifiabilité. Un claim
*« ROI en 30 jours »* est vérifiable (la date est 30j).
Un claim *« ROI élevé »* est invérifiable (pas de date).

### 2. Elle s'aligne avec la doctrine D4 append-only

La doctrine D4 (append-only) impose la traçabilité de toute
décision. Une promesse publique **datée** est traçable — la date
donne un point de comparaison pour vérifier si la promesse a été
tenue. Une promesse publique **non datée** est hors D4.

L'amplification candidate **rapporte** le veto Superman à D4.

### 3. Elle symétrise les 8 vetos

Les 7 autres vetos catalogue portent sur des artefacts
documentaires vérifiables (mandat écrit, condition d'arrêt, DoD,
problème reformulé, métrique chiffrée, chemin de sortie, accord
écrit). L'amplification candidate **aligne** Superman sur le même
standard.

## Les trois conditions d'amplification (cf. `b2-veto-amplification-cycle.md`)

### Condition 1 — Une observation documentée d'un cas-limite

Le captain Superman a vu un cas où la doctrine canonique **aurait
dû bloquer** mais ne l'a pas fait, parce que la classe était trop
large.

**Cas observés** (reconstruits) :

- *« Le produit booste votre ROI »* — pas de date, le ROI peut être
  mesuré à 30j, 90j, 365j. Superman bloque sur « delivery ne tient
  pas » (canonique), mais le motif est flou. Avec l'amplification,
  le motif devient *« pas de date de livraison »* — vérifiable.
- *« Intégration avec partenaire Z disponible bientôt »* — « bientôt »
  n'est pas un horizon mesurable. Superman bloque sur canonique,
  motif flou. Avec amplification, motif *« pas d'horizon mesurable »*
  — vérifiable.
- *« NPS de 100% »* — pas de fenêtre temporelle ni de cohorte.
  Cf. `veto-catalogue-concrete.md` §« Cas 5 ». Avec amplification,
  motif *« pas de date/horizon »* — vérifiable.

### Condition 2 — Une règle lisible, exprimée en une phrase

L'énoncé court (une phrase) est déjà formulé :

> *« La promesse publique doit indiquer une date de livraison ou un
> horizon mesurable. »*

Le format respecte le gabarit *« Veto canonique. En outre, ... »*.

### Condition 3 — Une décision d'archivage dans le journal Council

Le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` reçoit une ligne
`veto_amplification: superman, classe: promesse-publique, ajout:
date-ou-horizon-mesurable, depuis: <packet-id-source>`. **Append-only
D4.**

## La procédure d'amendement

`b2-veto-amplification-cycle.md` §« La procédure d'amendement » pose
4 étapes :

```
observation documentée (condition 1)
   ↓
draft d'amplification en une phrase (condition 2)
   ↓
séance hebdomadaire B2 Council : revue par les 7 autres capitaines
   ↓
   trois issues :
     - adoption (5/8 ou plus)
     - rejet (5/8 contre)
     - escalate_to_B1 (3/8 contre ou désaccord profond)
   ↓
archivage D4 dans le journal Council (condition 3)
   ↓
effet : l'amplification est citée dans tous les packets mésoperpétuels
         où la classe est en cause, à partir de la date d'effet
```

**Quorum** : 5 capitaines sur 8 (cf.
`b2-council-cadence-and-chair.md`). Si quorum non atteint, séance
reportée au mardi. Si veto catalogue actif, séance convoquée le
jour même (quorum minimum 3).

**Président de séance** : président tournant par impacted captain.
Pour l'amplification Superman, Superman préside (puisque c'est sa
doctrine). Mais les 7 autres capitaines ont voix — l'adoption
nécessite **5/8 minimum**.

## Amplification vs réécriture — la nuance critique

`b2-veto-amplification-cycle.md` §« L'amplification n'est pas la
réécriture » pose la distinction :

- **Amplification** : ajoute une exigence, n'enlève rien. Veto
  canonique + nouvelle exigence → classe plus stricte.
- **Réécriture** : modifie le périmètre du veto. *« Veto
  Wonder Woman bloque toute dépense récurrente »* → *« Veto
  Wonder Woman bloque toute dépense > 1000 € »*. **C'est un
  resserrement qui peut libérer des cas précédemment bloqués.**

L'amplification candidate Superman est une **amplification**, pas
une réécriture :

- Veto canonique : promesse non tenue → bloque les promesses sans
  DoD.
- Amplification : + date ou horizon mesurable → bloque aussi les
  promesses sans date.

**Rien n'est libéré** — la classe est plus stricte. **Majorité
simple 5/8 suffit**, pas unanimité + B1.

## Les contre-arguments possibles — ce qu'un captain hostile dirait

`b2-veto-amplification-cycle.md` §« Anti-pièges » pose les
contre-arguments. Pour l'amplification Superman :

### « C'est une exigence cosmétique »

Un captain hostile (Flash, JohnJones) peut dire *« la date n'est
pas une exigence de delivery, c'est cosmétique »*. Réponse : la
date **est** une exigence de delivery, parce qu'elle permet la
vérification a posteriori. Sans date, le delivery est non-vérifiable
— c'est la définition même de l'absence de D4.

### « Wonder Woman a déjà une métrique, Superman duplique »

Wonder Woman (Finance) exige une métrique de retour chiffrée
(triplet 58). Superman exigerait une date ou horizon. Les deux
sont **distinctes** : Wonder Woman porte sur la dépense, Superman
porte sur la promesse publique. Une dépense récurrente paid media
a une métrique de retour (MQL qualifies, ROI). Une promesse
publique a une date ou horizon (date de livraison, date de
mesure). **Pas de duplication**.

### « Cela alourdit la charge B3 (Groot, Mantis) »

Groot_Content et Mantis_VoC doivent ajouter une date à chaque
livrable. C'est une ligne de plus dans le JTBD packet. La charge
est marginale (5-10 minutes par livrable) et le gain de
vérifiabilité est asymétrique (un claim daté est 10x plus
vérifiable qu'un claim non daté).

### « Le canon V4 ne pose pas l'amplification, c'est une projection »

Exact. `b2-veto-amplification-cycle.md` marque
explicitement l'amplification Superman comme **projetée**. Le
canon n'ancre pas cette amplification par un triplet dédié
(comme le triplet 58 pour Wonder Woman). **C'est un candidat**,
pas une amplification adoptée.

## L'adoption en Council — projection

Si Superman propose l'amplification en séance hebdomadaire :

1. **Lecture de l'observation documentée** (3 cas observés).
2. **Lecture du draft** (1 phrase, format canonique).
3. **Débat** : 7 capitaines consultés.
4. **Vote** : 5/8 minimum pour adoption.

**Scénario probable** : adoption 6/8 ou 7/8. Les capitaines les
plus susceptibles de voter contre sont **JohnJones** (Sales — la
promesse est aussi son périmètre) et **Flash** (Product — la
promesse touche aussi la feature ship).

## Anti-pièges

- **Amplification silencieuse.** Si Superman adopte l'amplification
  sans passer par le Council, c'est une violation D4. Le Council
  doit refuser ou exiger l'escalade B1.
- **Amplification comme pouvoir personnel.** Si Superman dépose
  l'amplification **et** est le seul à l'invoquer dans les packets
  suivants, c'est un outil politique, pas doctrinal.
- **Amplification qui contredit le veto canonique.** Si la
  formulation produit un énoncé qui contredit *« la delivery ne
  tient pas »*, c'est une réécriture déguisée. Le Council doit
  refuser.
- **Amplification qui n'est pas cumulative.** Une amplification
  *« pour ce claim particulier, j'ajoute la date »* n'est pas
  une amplification — c'est un cas d'application. La doctrine
  catalogue n'est pas concernée.

## Liens

- [[b2-veto-amplification-cycle]] — la doctrine d'amplification
- [[b2-eight-domain-vetoes-catalogue]] — le catalogue 8 vetos
- [[b2-council-cadence-and-chair]] — la mécanique de séance
- [[veto-catalogue-concrete]] — les cas où le veto tient
- [[domain-perimeter]] — frontières que l'amplification touche
- [[pair-checks-dependencies]] — pair-checks où l'amplification
  s'applique

## Note de confiance

**Projets, à moitié étayé.** L'amplification candidate est listée
explicitement par `b2-veto-amplification-cycle.md` §« Trois
amplifications candidates » comme projection. La triple 58
canonique de Wonder Woman ancre la **procédure**, mais pas
l'amplification Superman (qui n'a pas de triplet dédié). Les 3
cas observés (condition 1) sont **reconstruits** par lecture
critique du veto canonique et de la pratique documentée. Les 4
contre-arguments sont **projetés** à partir des anti-pièges de
`b2-veto-amplification-cycle.md` §« Anti-pièges » et de la
doctrine des autres vetos.
