---
type: Concept
title: Amplification candidate Flash — "mécanisme de reprise documenté", procédure de soumission 5/8 Council
description: Le triplet 58 ancre l'amplification Wonder Woman ("dépense récurrente → métrique de retour chiffrée"). Aucune amplification Flash n'est citée canoniquement. Ce concept formalise l'amplification candidate "mécanisme de reprise documenté" avec procédure d'amendement D4 (observation + phrase + journal) et seuil majorité simple. Quatre conditions cumulatives d'adoption par le B2 Council, trois cas abus d'application.
tags: [flash, product, veto, amplification, mecanisme-reprise, b2-council, d4, triplet-58]
generated: { by: minimax-m3, at: 2026-08-19T05:05:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-2, at: 2026-08-19T05:05:00Z }
sources:
  - id: triplet-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend la doctrine veto-dépense"
    last_modified: 2026-08-17
  - id: triplet-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
  - id: veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — 3 conditions, procédure d'amendement D4
    last_modified: 2026-08-19
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: flash-veto-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Veto Flash — l'offre dépersonnalisée (tour 1 §"Amplification candidate")
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Amplification candidate Flash — "mécanisme de reprise documenté"

## Le canon verbatim

Le triplet v3 ligne 25 cite verbatim le veto canonique Flash :

> *« Flash bloque toute offre dont la valeur dépend d'une personne nommée. »*

Le triplet 58 ancre la mécanique d'amplification par Wonder Woman :

> *« Wonder Woman étend la doctrine veto-dépense : corrélat direct avec
> la dette récurrente — chaque ligne doit porter une métrique de retour
> chiffrée. »*

Le verbe **« étend »** (cf. `b2-veto-amplification-cycle.md` §« Les deux
lectures de 'étend' ») implique que le catalogue des 8 vetos n'est pas
figé : un capitaine peut ajouter une **sous-classe** à son veto sans
réécrire le veto canonique. C'est l'amendement doctrinal, pas
l'amendement matriciel (qui exige l'unanimité + escalate B1).

## Pourquoi une amplification Flash est légitime

Le veto canonique bloque *« toute offre dont la valeur dépend d'une
personne nommée »*. Le **mécanisme de reprise documenté** est une
extension naturelle : ce n'est plus seulement *« la valeur ne dépend
pas d'une personne »*, c'est *« la valeur ne dépend pas d'une personne,
ET le mécanisme de reprise est écrit et vérifiable »*.

L'amplification transforme un veto de **forme** (la valeur est nominative
?) — ou) en veto de **forme + documentation** (la valeur est
dépersonnalisée ET le mécanisme de reprise est écrit ?). C'est plus
strict, mais c'est dans la même catégorie (offre nominative vs
offre reproductible).

## Les trois conditions de l'amplification Flash

L'amplification hérite des trois conditions canoniques de
`b2-veto-amplification-cycle.md` §« Les trois conditions
d'amplification » :

### Condition 1 — Une observation documentée d'un cas-limite

Le captain Flash a vu un cas où le veto canonique **aurait dû bloquer**
mais ne l'a pas fait, parce que la classe était trop large. La trace
est un packet mésoperpétuel ou une ligne de journal Council qui décrit
le cas-limite.

**Cas-limite typique** : une offre de coaching premium est portée par
un consultant senior, mais le contrat inclut une clause de continuité
qui désigne un partner back-up. Le veto canonique **ne bloque pas**
cette offre (la valeur n'est pas nominative au sens strict — un back-up
est nommé). Mais en pratique, si le partner back-up n'a jamais été
formé, la clause est **lettre morte**. L'amplification ferme cette
faille : *« le mécanisme de reprise doit être documenté ET exercé »*.

### Condition 2 — Une règle lisible, exprimée en une phrase

L'amplification produit un énoncé court qui s'ajoute au veto
canonique. Format canonique (cf. `b2-veto-amplification-cycle.md` §« 2.
Une règle lisible ») :

> *« Flash bloque toute offre dont la valeur dépend d'une personne
> nommée. En outre, tout mécanisme de reprise doit être documenté
> avant commercialisation, et sa preuve d'existence (partner formé,
> runbook tenu, squad back-up active) doit être vérifiable par un
> tiers qui n'est pas Flash. »*

C'est **une phrase**, pas un texte. Si l'amplification devient un
paragraphe, c'est une réécriture déguisée, qui exige l'unanimité +
escalate B1.

### Condition 3 — Une décision d'archivage dans le journal Council

Le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` reçoit une ligne
`veto_amplification: flash, classe: offre-depersonnalisee, ajout:
mecanisme_reprise_documente, depuis: <packet-id-source>`. La ligne
est append-only (D4). Sans cette ligne, l'amplification n'a pas de
**date d'effet** — elle ne peut pas être citée par un autre capitaine.

## La procédure d'adoption — majorité simple 5/8

`b2-veto-amplification-cycle.md` §« La procédure d'amendement » pose la
séance hebdomadaire B2 Council comme instance d'adoption. Pour
l'amplification Flash :

1. **Observation documentée** : packet mésoperpétuel ou ligne de
   journal Council (condition 1).
2. **Draft d'amplification** en une phrase, archivé dans le journal
   Council (conditions 2 + 3 fusionnées pour traçabilité).
3. **Séance hebdomadaire B2 Council** : revue par les 7 autres
   capitaines.
4. **Trois issues** :
   - **Adoption** (7/8 ou 8/8 — unanimité ou unanimité moins une
     abstention documentée).
   - **Adoption simplifiée** (5/8) — si l'amplification touche
     **uniquement la doctrine Flash** (et non la wheel 8-domain).
     C'est le cas de *« mécanisme de reprise documenté »* : l'ajout
     ne modifie le veto d'aucun autre capitaine.
   - **Rejet** (5/8 contre) — l'amplification n'est pas adoptée, le
     veto canonique reste en l'état.
   - **Escalate B1** (3/8 contre ou désaccord profond) — l'amplification
     remonte à B1, qui peut amender le catalogue canonique (ce qui est
     plus rare et plus lourd).

L'amplification Flash **peut** être adoptée à majorité simple 5/8 parce
qu'elle ne touche que la doctrine Flash. La nuance
`b2-veto-amplification-cycle.md` §« La procédure d'amendement » : *« si
un autre capitaine est impacté, l'unanimité est requise »*.

## Quatre conditions cumulatives d'adoption par le B2 Council

L'amplification n'est pas un acte libre — quatre conditions
cumulatives sont nécessaires :

1. **L'observation** documente un cas où le veto canonique a laissé
   passer une offre à valeur nominative (condition 1).
2. **Le draft** est en une phrase (condition 2).
3. **L'archivage D4** est fait dans le journal Council (condition 3).
4. **La majorité 5/8** est atteinte en séance hebdomadaire (condition
   procédurale).

Une amplification qui manque une condition n'est pas une
amplification — c'est un acte d'autorité non documenté. Le packet
mésoperpétuel qui cite une amplification sans ces quatre conditions est
**non-vérifiable**.

## Trois cas d'application légitimes

Trois cas où l'amplification "mécanisme de reprise documenté" bloque
l'offre (alors que le veto canonique l'aurait laissée passer) :

### Cas 1 — Clause de continuité sans partner formé

L'offre inclut une clause de continuité (partner back-up nommé dans le
contrat). Mais le partner n'a **jamais été formé** sur la méthode.
L'amplification bloque : le mécanisme de reprise est documenté, mais
**non fonctionnel**. La preuve d'existence (formation tenue, exercice
simulé de passation) manque.

### Cas 2 — Squad back-up sans mandat de reprise

L'offre est portée par un squad de 3 personnes. Le contrat mentionne
une squad back-up, mais cette squad n'a **pas de mandat** de reprise
(qui décide quand elle prend le relais ? quel est le seuil de bascule ?).
L'amplification bloque : le mécanisme de reprise est **non-décit**.

### Cas 3 — Runbook tenu mais non exercé

L'offre inclut un runbook complet de la méthode. Mais le runbook
n'a **jamais été exécuté** par un tiers (pas de test de continuité).
L'amplification bloque : le mécanisme est **documenté**, pas **vérifié**.

## Trois cas d'application abusifs

Trois cas où l'amplification serait invoquée à tort (par erreur
politique ou par excès de zèle) :

### Cas abusif 1 — Refus d'une offre pilote sur mesure

Un capitaine B2 refuse une offre pilote *« parce que le mécanisme de
reprise n'est pas documenté pour ce client spécifique »*. **C'est un
abus** : un pilote est par définition une co-construction avec un
client identifié. Le mécanisme de reprise est exigé pour
l'**offre reproductible**, pas pour le pilote. Distinction analogue à
`flash-veto-offre-depersonnalisee.md` §« Cas abusif 2 — Refus d'un
pilote client sans engagement ».

### Cas abusif 2 — Mécanisme de reprise appliqué à un single-shot

Un capitaine B2 refuse une prestation one-shot (mission ponctuelle,
livrable unique) au motif que *« le mécanisme de reprise n'est pas
documenté »*. **C'est un abus** : un single-shot n'a pas vocation à
être reproduit. Le mécanisme de reprise ne s'applique qu'aux offres
**reproductibles** (catalogued offering).

### Cas abusif 3 — Mécanisme de reprise utilisé pour bloquer un concurrent

Un capitaine B2 refuse une offre dont le mécanisme de reprise est
tenu par un **sous-traitant** (outsourced back-up). **C'est un abus** :
le veto canonique ne porte pas sur la **nature** du mécanisme de
reprise (interne ou externalisé), mais sur son **existence et sa
vérification**. Un sous-traitant formé et mandaté est un mécanisme de
reprise valide.

## Anti-pièges

- **Amplification silencieuse.** Un Flash qui « étend sa doctrine » sans
  passer par le Council casse la traçabilité D4. Le packet
  mésoperpétuel qui cite l'amplification devient non-vérifiable.
- **Amplification comme pouvoir personnel.** Une amplification qui
  revient systématiquement sur les mêmes offres est un outil
  politique, pas doctrinal. Le signal : une amplification adoptée par
  Flash à chaque cycle est en dérive.
- **Confondre amplification et réécriture.** L'amplification **ajoute**
  une exigence. Une réécriture (ex : *« Flash bloque toute offre
  > 1000 € »*) est un resserrement du périmètre qui peut libérer des
  cas précédemment bloqués. La réécriture exige unanimité + escalate
  B1.
- **Amplification appliquée avant son adoption.** Une amplification
  qui n'a pas atteint la majorité 5/8 ne peut pas être invoquée
  contre une offre. Le packet mésoperpétuel qui s'en prévaut est
  invalide.

## Liens

- [[b2-veto-amplification-cycle]] — la procédure canonique d'amplification
- [[b2-eight-domain-vetoes-catalogue]] — le catalogue que l'amplification étend
- [[b2-council-arbitrage-rule]] — l'instance qui adopte ou refuse l'amplification
- [[b2-meso-decision-packet-spec]] — le format où l'amplification est consignée
- [[flash-veto-offre-depersonnalisee]] — le veto canonique que cette amplification étend
- [[flash-doctrine-valeur-artefact]] — la doctrine valeur d'artefact qui porte l'amplification
- [[b2-council-cadence-and-chair]] — la séance hebdomadaire qui statue

## Note de confiance

**Confirmé par machine, à moitié étayé.** Le triplet 58 (Wonder Woman
étend) est cité verbatim et ancre l'existence du mécanisme
d'amplification. Le triplet 25 (Flash veto) est verbatim. La procédure
canonique (3 conditions + majorité 5/8) est tirée verbatim de
`b2-veto-amplification-cycle.md`. Les 3 cas d'application légitimes
sont **projetés** à partir de la doctrine de valeur d'artefact et de la
pratique reconstruite (partner non-formé, squad sans mandat, runbook
non-exercé). Les 3 cas abusifs sont **reconstruits** par analogie avec
les cas abusifs du veto canonique (`flash-veto-offre-depersonnalisee.md`
§« Trois cas abusifs »). L'amplification elle-même n'a **pas été
soumise** au Council à la date de cette distillation — c'est un draft
de tour 2, pas une amplification en vigueur.