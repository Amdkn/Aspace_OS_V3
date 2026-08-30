---
type: Concept
title: Couplage Batman × Wonder Woman — la récurrence Ops et le veto-dépense
description: Les procédures Ops (run, support, monitoring, revue) sont récurrentes par nature. Le veto Batman (condition d'arrêt) et le veto Wonder Woman (dépense récurrente sans date de revue + métrique de retour) portent sur le même livrable récurrent. 4 cas de recouvrement, 3 zones de partage, et une asymétrie : Wonder Woman a une amplification canonique (triplet 58), Batman n'en a pas.
tags: [batman, wonder-woman, couplage, finance, ops, recurrence, condition-arret, depense, veto, b2]
generated: { by: minimax-m3, at: 2026-08-19T04:40:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T04:40:00Z }
sources:
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: triplet-wonder-woman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 28 — Wonder Woman bloque toute dépense récurrente sans date de revue et sans métrique de retour"
    last_modified: 2026-08-17
  - id: triplet-wonder-woman-extension
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend la doctrine veto-dépense (métrique de retour chiffrée)"
    last_modified: 2026-08-17
  - id: b2-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — Batman et Wonder Woman en regard
    last_modified: 2026-08-19
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — triplet 58 ancre la procédure
    last_modified: 2026-08-19
  - id: wonder-woman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-recurrent-spend-veto.md"
    title: Wonder Woman — veto recurrent-spend + date + métrique
    last_modified: 2026-08-19
  - id: wonder-woman-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Wonder Woman — couplages Finance × autres domaines
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Couplage Batman × Wonder Woman — la récurrence Ops et le veto-dépense

## Le constat — l'Ops est récurrente par nature

Les procédures Ops (run, support, monitoring, onboarding récurrent,
revue hebdomadaire) sont **structurellement récurrentes** : elles
tournent en boucle sur la durée de vie d'un livrable. Ce n'est pas
un défaut — c'est la définition du périmètre Ops
(`domaine-batman-ops-perimetre-frontieres.md`).

Le veto catalogue de Batman porte sur la **condition d'arrêt** :
*« bloque toute procédure qui n'a pas de condition d'arrêt écrite »*
(triplet 24). La condition d'arrêt pose la question *« quand est-ce
qu'on arrête la boucle ? »*.

Le veto catalogue de Wonder Woman porte sur la **dépense récurrente** :
*« bloque toute dépense récurrente sans date de revue et sans
métrique de retour »* (triplet 28). Le veto-dépense pose la question
*« quand est-ce qu'on re-vérifie que la dépense tient son ROI ? »*.

**Les deux questions sont différentes mais elles portent sur le même
livrable** : une procédure Ops est à la fois une boucle (Batman) et
une dépense récurrente (Wonder Woman). Aucune des deux ne s'applique
à une procédure one-shot — par construction, une procédure one-shot
n'est pas récurrente.

## Les 4 cas de recouvrement

### Cas 1 — Runbook Ops avec condition d'arrêt + run cost chiffré

Batman GREEN (condition d'arrêt posée) ; Wonder Woman GREEN (run cost
estimé, date de revue 12WY, métrique de retour : NPS ou marge). Les
deux vetos tiennent simultanément. **Cas nominal.**

### Cas 2 — Runbook Ops avec condition d'arrêt mais sans run cost chiffré

Batman GREEN ; Wonder Woman RED — le run cost (coût mensuel de la
procédure) n'est pas chiffré dans le packet. Wonder Woman tient son
veto ; Batman tient le sien. Les deux capitaines bloquent. Batman
ne peut pas passer outre le veto Wonder Woman (catalogue propriété
3 : non-négociable au niveau mésoperpétuel).

### Cas 3 — Procédure sans condition d'arrêt mais run cost chiffré

Batman RED ; Wonder Woman GREEN. Batman tient son veto ; Wonder
Woman ne peut pas dire *« le run est chiffré, donc la procédure
tourne »* — son veto teste la dépense récurrente, pas la condition
d'arrêt. Batman **seul** bloque.

### Cas 4 — Procédure sans condition d'arrêt ni run cost chiffré

Batman RED ; Wonder Woman RED. Double porte fermée. L'escalade
B1 est probable — la wheel 8-domain ne tient pas.

## Les 3 zones de partage — ce que chaque veto teste vraiment

### Zone A — Batman teste *quand on arrête*

La condition d'arrêt est **une décision de cycle** : *« la procédure
s'arrête au 2026-12-31 »* ou *« la procédure s'arrête quand le NPS
descend sous 35 »*. Batman n'a pas le mandat d'étendre le cycle —
c'est Summers (B1). Mais Batman a le mandat de **constater**
l'absence de cette décision.

### Zone B — Wonder Woman teste *quand on re-vérifie le ROI*

La date de revue et la métrique de retour sont **un dispositif de
surveillance** : *« le run cost est re-vérifié tous les 90 jours ;
la métrique est le NPS, seuil de coupure 35 »*. Wonder Woman tient
la discipline de la revue — Batman ne la tient pas.

### Zone C — Les deux testent *qui arrête*

Wonder Woman a son amplification canonique (triplet 58) — *« chaque
ligne doit porter une métrique de retour chiffrée »*. Batman n'a
**aucune amplification canonique** équivalente dans le triplet v3.
C'est une asymétrie : Wonder Woman peut durcir sa doctrine par
amplification (cf. `b2-veto-amplification-cycle.md`), Batman doit
passer par une réécriture du catalogue (escalade B1, unanimité du
Council).

## L'asymétrie — Wonder Woman a une amplification, Batman pas

Le triplet 58 ancre l'amplification Wonder Woman : *« corrélat
direct avec la dette récurrente — chaque ligne doit porter une
métrique de retour chiffrée »*. La procédure d'amplification est
documentée dans `b2-veto-amplification-cycle.md` (3 conditions :
observation documentée, règle en une phrase, archivage D4).

Pour Batman, **aucun triplet ne pose une amplification du veto
condition d'arrêt**. La raison reconstruite : le veto Batman teste
la **présence** d'une condition d'arrêt, pas sa **qualité**. Une
amplification du type *« la condition d'arrêt doit être chiffrée »*
irait plus loin que le canon — elle ajouterait une exigence de seuil.

**Conséquence concrète** : si Wonder Woman et Batman sont en
conflit sur une procédure, Wonder Woman peut invoquer son veto +
son amplification (deux étages de garde), Batman peut seulement
invoquer son veto (un seul étage). Le Council arbitre en faveur du
plus strict — c'est la doctrine catalogue *« non-négociable au
niveau mésoperpétuel »* — mais Batman doit escalader B1 pour
durcir sa propre doctrine.

## Pourquoi ce couplage n'est pas un pair-check canonique

La matrice d'harmonisation pose 5 pair-checks Finance → autres
domaines : #5 (Finance → Growth), #6 (Finance → Product). **Aucun
Finance → Ops**. La raison reconstruite : Finance teste
l'**allocation** du budget, pas la **boucle opérationnelle** qui
consomme le budget. Le coût d'une procédure Ops est une **dépense
récurrente** (Wonder Woman), pas une **allocation** initiale (Finance
vers Growth/Product).

**Conséquence** : le couplage Batman × Wonder Woman est un couplage
**de veto adjacent + de zone partagée**, pas un pair-check de
transition. Il n'a pas de RACI canonique. Wonder Woman n'apparaît
ni en A, ni en R, ni en C, ni en I sur les pair-checks #2 et #3
(Batman A). Wonder Woman apparaît **en veto adjacent** sur la
récurrence.

## Anti-pièges

- **Batman qui refuse un run cost chiffré.** Batman teste la condition
  d'arrêt, pas le run cost. Si le run cost est chiffré mais la
  procédure n'a pas de condition d'arrêt, Batman tient son veto
  seul. Il ne dit pas *« le run est trop cher »* — c'est Wonder
  Woman.
- **Wonder Woman qui refuse une condition d'arrêt.** Wonder Woman
  teste la dépense récurrente, pas la condition d'arrêt. Elle ne
  dit pas *« la procédure devrait s'arrêter plus tôt »* — c'est
  Batman.
- **Batman qui amplifie son veto en silence.** Sans triplet canonique
  et sans passage par le Council (cf.
  `b2-veto-amplification-cycle.md`), une amplification Batman est
  invalide. Batman peut proposer une amplification au Council, pas
  l'imposer.
- **Wonder Woman qui impose son amplification sur un runbook Ops.**
  L'amplification s'applique à la doctrine veto-dépense, pas aux
  procédures Batman. Wonder Woman peut bloquer un runbook Ops au
  motif *« run cost non chiffré »* (vet canonique), pas au motif
  *« la métrique de retour est trop molle »* (amplification).
- **Traiter la récurrence Ops comme une dette Wonder Woman.** Une
  procédure Ops est récurrente mais elle n'est pas **une dette**
  au sens financier. La dette récurrente est un cas particulier
  (triplet 58) — pas la généralité.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Ops récurrent
- [[batman-veto-condition-arret-procedure]] — le veto Batman
- [[batman-couplage-legal-aquaman-perimetre-propriete]] — l'autre couplage transverse Batman
- [[wonder-woman-recurrent-spend-veto]] — le veto Wonder Woman canonique + amplification
- [[wonder-woman-finance-couplings]] — les couplages Finance en général
- [[b2-eight-domain-vetoes-catalogue]] — les deux vetos en regard
- [[b2-veto-amplification-cycle]] — la procédure d'amplification que Batman n'a pas encore activée

## Note de confiance

**Confirmé par machine pour les deux vetos.** Les triplets 24, 28,
58 sont cités verbatim. Les 4 cas de recouvrement sont **reconstruits**
à partir des deux veto catalogue et de la propriété *non-négociable
au niveau mésoperpétuel*. Les 3 zones de partage sont **projetées**
à partir de l'asymétrie amplification (triplet 58 ancre Wonder
Woman ; pas d'équivalent Batman dans le triplet v3). L'asymétrie
*Wonder Woman peut durcir par amplification / Batman doit escalader
B1* est **mon raisonnement** défendu à partir du triplet 58 et de
la doctrine amplification. La conclusion *« couplage de veto adjacent,
pas un pair-check »* est **projetée** — le canon ne pose pas
explicitement cette distinction. À vérifier en cycle réel : (1) la
double porte se déclenche-t-elle souvent ?, (2) Batman a-t-il déjà
proposé une amplification de son veto au Council ? (3) la
non-canonisation Finance → Ops est-elle un trou ou un choix ?
