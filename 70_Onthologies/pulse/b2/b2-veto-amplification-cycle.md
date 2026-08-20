---
type: Concept
title: Amplification des vetos B2 — le catalogue est vivant, pas figé
description: Le triplet 58 dit « Wonder Woman étend sa doctrine veto-dépense : corrélat direct avec la dette récurrente — chaque ligne doit porter une métrique de retour chiffrée ». Le verbe « étend » implique que les 8 vetos catalogue (cf. b2-eight-domain-vetoes-catalogue) ne sont pas un inventaire clos. Une amplification ajoute une nouvelle classe de décision au veto, pas un cas nouveau à une classe existante. Trois conditions, une procédure d'amendement D4, un anti-piège sur la dérive.
tags: [b2, veto, amplification, doctrine, extension, amendement, d4]
generated: { by: minimax-m3, at: 2026-08-19T03:25:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T03:25:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplet-wonder-woman-extension
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend la doctrine veto-dépense"
    last_modified: 2026-08-17
  - id: triplet-wonder-woman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 28 — Wonder Woman bloque toute dépense récurrente sans date de revue ni métrique de retour"
    last_modified: 2026-08-17
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: org-json
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — 8 vetos catalogue
    last_modified: 2026-08-02
  - id: b2-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — un domaine, un blocage légitime
    last_modified: 2026-08-19
  - id: omk-business-os
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — doctrine D4 append-only
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Amplification des vetos B2 — le catalogue est vivant, pas figé

## Le signal canonique

Le triplet 58 dit verbatim :

> *« Wonder Woman étend la doctrine veto-dépense : corrélat direct avec
> la dette récurrente — chaque ligne doit porter une métrique de retour
> chiffrée. »*

Le verbe **« étend »** est l'information clé. Le triplet 28 donne le
veto canonique de Wonder Woman (triplet 28) :

> *« Wonder Woman bloque toute dépense récurrente sans date de revue et
> sans métrique de retour. »*

L'amplification ajoute une exigence supplémentaire : *chaque ligne doit
porter une métrique de retour chiffrée*. C'est **plus strict** que le
veto canonique, mais c'est **dans la même catégorie** (dépense
récurrente).

`b2-eight-domain-vetoes-catalogue.md` pose le catalogue comme un
inventaire de 8 classes, avec trois propriétés (catégoriel, vérifiable,
non-négociable au niveau mésoperpétuel). Le triplet 58 montre qu'une
classe peut être **étendue** sans être réécrite. C'est la même
distinction qu'un amendement à une loi versus une nouvelle loi.

## Les deux lectures de « étend »

Le verbe est ambigu entre deux lectures également défendables :

**Lecture 1 — application à un nouveau cas** : Wonder Woman applique
sa doctrine veto-dépense à un cas qu'elle n'avait pas encore vu (par
exemple, une dépense cloud récurrente qui n'avait pas été soumise
auparavant). C'est une **continuité**, pas une amplification.

**Lecture 2 — ajout d'une nouvelle sous-classe** : Wonder Woman ajoute
*« chaque ligne doit porter une métrique de retour chiffrée »* comme
exigence supplémentaire dans la sous-classe *dépense récurrente*. C'est
une **amplification** : la doctrine devient plus stricte pour la même
catégorie de décision.

Le triplet 58 penche vers la **lecture 2** : *« corrélat direct avec la
dette récurrente »* suggère que Wonder Woman a observé un cas
(dépense récurrente qui n'a pas de métrique de retour chiffrée) et a
étendu sa doctrine pour fermer la faille. La lecture 1 ne demande pas
de nouvel énoncé — le veto canonique suffit.

## Les trois conditions d'amplification

L'amplification n'est pas un acte libre du capitaine. Elle exige trois
conditions cumulatives. Une amplification qui manque une condition
n'est pas une amplification — c'est un **acte d'autorité** non
documenté.

### 1. Une observation documentée d'un cas-limite

Le capitaine a vu un cas où la doctrine canonique **aurait dû
bloquer** mais ne l'a pas fait, parce que la classe était trop
large. La trace est un **packet mésoperpétuel** ou une **ligne de
journal Council** qui décrit le cas-limite. Sans cette trace, le
capitaine ne peut pas justifier l'amplification — il ne fait
qu'exercer un pouvoir personnel.

### 2. Une règle lisible, exprimée en une phrase

L'amplification produit un énoncé court qui s'ajoute au veto
canonique. Format : *« {Veto canonique}. En outre, {nouvelle
exigence}. »* L'amplification qui produit un texte de plus d'une
phrase est une réécriture déguisée — elle doit repasser par le
processus de modification du catalogue (escalade B1, D4).

### 3. Une décision d'archivage dans le journal Council

Le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` reçoit une ligne
`veto_amplification: <capitaine>, classe: <catégorie>, ajout:
<exigence>, depuis: <packet-id-source>`. La ligne est append-only
(D4). Sans cette ligne, l'amplification n'a pas de **date
d'effet** — elle ne peut pas être citée par un autre capitaine.

## La procédure d'amendement

```
observation documentée (condition 1)
   ↓
draft d'amplification en une phrase (condition 2)
   ↓
séance hebdomadaire B2 Council : revue par les 7 autres capitaines
   ↓
   trois issues :
     - adoption (7/8 ou 8/8)
     - rejet (5/8 contre)
     - escalate_to_B1 (3/8 contre ou désaccord profond)
   ↓
archivage D4 dans le journal Council (condition 3)
   ↓
effet : l'amplification est citée dans tous les packets mésoperpétuels
         où la classe est en cause, à partir de la date d'effet
```

L'amplification n'est **pas** un acte unilatéral du capitaine — elle
passe par le Council, comme tout amendement de doctrine. La nuance :
une amplification qui touche **uniquement la doctrine d'un capitaine**
(et non la wheel 8-domain) peut être adoptée à la majorité simple du
Council (5/8), pas necessarily à l'unanimité. Si un autre capitaine
est impacté, l'unanimité est requise.

## Trois amplifications candidates (projetées)

Les 8 vetos catalogue ont chacun des cas-limites connus. Trois
amplifications projetées à partir de la pratique observée :

| Capitaine | Veto canonique | Amplification candidate | Source implicite |
|---|---|---|---|
| Wonder Woman (Finance) | dépense récurrente sans date de revue | chaque ligne doit porter une métrique de retour chiffrée | triplet 58 — explicite |
| Aquaman (Legal) | prestation sans accord écrit sur le périmètre | la propriété intellectuelle du livrable doit être déclarée avant le démarrage | pratique documentée (Master_Agreements) |
| Superman (Growth) | promesse publique que la delivery ne tient pas | la promesse doit indiquer une date de livraison ou un horizon mesurable | inférence depuis la doctrine `b2-council-cadence-and-chair.md` §« Pourquoi la présidence tournante » |

Les trois sont **projetées** — seule Wonder Woman a une amplification
explicite dans le triplet 58. Les deux autres sont des candidats que
le Council pourrait adopter en séance.

## L'amplification n'est pas la réécriture

L'amplification **ajoute** une exigence, elle n'enlève rien. Une
réécriture de veto (par exemple, *« Wonder Woman bloque toute dépense
récurrente »* → *« Wonder Woman bloque toute dépense > 1000 € »*) est
un acte différent : c'est un **resserrement du périmètre** qui peut
libérer des cas précédemment bloqués. La réécriture exige
l'unanimité du Council + escalate B1 (parce qu'elle touche la wheel
8-domain). L'amplification n'exige que la majorité simple + journal
D4.

## Anti-pièges

- **Amplification silencieuse.** Un capitaine qui « étend sa doctrine
  » sans passer par le Council casse la traçabilité D4. Le packet
  mésoperpétuel qui cite l'amplification devient non-vérifiable.
- **Amplification comme pouvoir personnel.** Une amplification qui
  revient systématiquement sur les mêmes domaines est un outil
  politique, pas doctrinal. Le signal : un capitaine qui dépose plus
  d'amplifications qu'il n'y a de séances est en dérive.
- **Amplification qui contredit le veto canonique.** Si l'amplification
  produit un énoncé qui contredit le veto canonique, c'est une
  réécriture déguisée. Le Council doit refuser ou exiger
  l'escalade B1.
- **Amplification qui n'est pas cumulative.** Une amplification qui
  s'applique à un cas unique (« pour ce recrutement, j'ajoute
  l'exigence X ») n'est pas une amplification — c'est un cas
  d'application de la matrice d'harmonisation. La doctrine catalogue
  n'est pas concernée.
- **Confondre amplification et amendement de matrice.** L'amplification
  touche un veto, l'amendement de matrice touche une pair-check ou un
  red flag. Les deux passent par le Council, mais avec des majorités
  différentes (matrice = unanimité + B1, amplification = majorité
  simple).

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — le catalogue que l'amplification étend
- [[b2-council-arbitrage-rule]] — l'instance qui adopte ou refuse l'amplification
- [[b2-meso-decision-packet-spec]] — le format où l'amplification est consignée
- [[b2-council-cadence-and-chair]] — la séance hebdomadaire qui statue
- [[b2-three-cooperation-modes]] — la lecture parallel/handoff/negotiation d'une amplification
- [[b2-pair-check-raci-by-rank]] — l'amplification qui touche un pair-check (rare)
- [[b2-areas-dormants-doctrine]] — quand l'amplification concerne un capitaine dormant
- [[omk-business-os]] — la doctrine D4 append-only qui s'applique

## Note de confiance

**Confirmé par machine, à moitié.** Le triplet 58 est cité verbatim et
ancre l'existence d'une amplification. Le triplet 28 donne le veto
canonique de Wonder Woman, et la diff entre les deux triplets est
exactement l'amplification. La procédure d'amendement (3 conditions,
séance hebdomadaire, majorité 5/8) est **reconstruite** à partir de
la cadence canonique du Council (`b2-council-cadence-and-chair.md`) et
de la doctrine D4 append-only. Les trois amplifications candidates
(Aut aquaman, Superman) sont **projetées** à partir de la pratique
documentée et ne sont pas étayées par des triplets canoniques. La
distinction amplification/réécriture est **empruntée** au framework
juridique (loi vs amendement) — assumée comme projection.
