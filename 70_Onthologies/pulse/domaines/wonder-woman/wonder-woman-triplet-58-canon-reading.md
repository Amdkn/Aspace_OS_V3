---
type: Concept
title: Triplet 58 « Wonder Woman étend » — lecture A (amplification) vs lecture B (extension périmètre), recommandation au Council
description: Le triplet 58 « Wonder Woman étend la doctrine veto-dépense avec ROI à 30 jours » est ambigu entre deux lectures défendables. Lecture A : amplification unaire du veto catalogue (cf. b2-veto-amplification-cycle), condition de majorité simple 5/8 + journal D4. Lecture B : extension du périmètre Finance au triangle Growth ×Finance ×Product (cf. wonder-woman-growth-finance-product-triangular-coupling), condition d'unanimité + escalate B1. La doctrine canonique F1-F25 + le triplet 28 (veto canonique) penchent vers la Lecture A ; le triplet 58 ne tranche pas explicitement. Recommandation : Lecture A canonique avec un test cycle de 60 jours.
tags: [b2, finance, triplet-58, wonder-woman, amplification, extension, veto, doctrine, canon, recommandation]
generated: { by: minimax-m3, at: 2026-08-19T05:30:00Z }
verified:
  - { by: process:lecture-corpus-wonder-woman-tour-3, at: 2026-08-19T05:30:00Z }
sources:
  - id: triplet-58-source
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend la doctrine veto-dépense : corrélat direct avec la dette récurrente — chaque ligne doit porter une métrique de retour chiffrée"
    last_modified: 2026-08-17
  - id: triplet-28-canonical-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 28 — Wonder Woman bloque toute dépense récurrente sans date de revue ni métrique de retour"
    last_modified: 2026-08-17
  - id: veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — le catalogue est vivant, pas figé
    last_modified: 2026-08-19
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Domaine Finance — couplages amont/aval
    last_modified: 2026-08-19
  - id: triangular-coupling
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-growth-finance-product-triangular-coupling.md"
    title: Couplage triangulaire Growth × Finance × Product
    last_modified: 2026-08-19
  - id: red-flag-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-red-flag-4-trigger.md"
    title: Red flag #4 — Finance red + Growth/Product green
    last_modified: 2026-08-19
  - id: omk-vp-agent-source
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/VP_AGENT.md"
    title: Coach OS — VP_AGENT.md source du triplet 58
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Triplet 58 « Wonder Woman étend » — lecture A vs lecture B, recommandation au Council

## Le signal canonique

Le triplet 58 (`triplets/v3-business.jsonl` ligne 58, source
`coach-os/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/VP_AGENT.md`)
pose verbatim :

> *« Wonder Woman étend la doctrine veto-dépense : corrélat direct
> avec la dette récurrente — chaque ligne doit porter une métrique
> de retour chiffrée. »*

Le verbe **`seeAlso`** (selon le format JSONL) et la phrase qui
contient le mot-clé **« étend »** ancrent le triplet dans le
catalogue des amplifications (`b2-veto-amplification-cycle.md`).
**Le triplet 28** pose le veto canonique de Wonder Woman :

> *« Wonder Woman bloque toute dépense récurrente sans date de
> revue et sans métrique de retour. »*

La diff entre les deux triplets est exactement l'amplification
candidate : *« chaque ligne doit porter une métrique de retour
chiffrée »* (triplet 58) ajoute une **contrainte chiffrée**
absente du triplet 28 (qui dit juste « sans métrique de retour »).

## L'ambiguïté — deux lectures également défendables

La doctrine canonique `b2-veto-amplification-cycle.md` pose les
deux lectures explicitement et refuse de trancher :

### Lecture A — Amplification unaire du veto catalogue

Wonder Woman **étend** sa doctrine veto-dépense au sens « ajoute
une exigence chiffrée à la classe existante ». C'est une
**amplification** au sens du cycle d'amplification
(`b2-veto-amplification-cycle.md` §« Les deux lectures de « étend » »),
pas une nouvelle classe.

**Argument** : le triplet 58 dit *« corrélat direct avec la dette
récurrente »*. La corrélation est intra-classe (dépense récurrente),
pas inter-classe (lancement, pricing stratégique, etc.). Le triplet
reste dans la **catégorie** posée par le triplet 28.

**Conséquence procédurale** :
- Adoption par le Council à **majorité simple 5/8** (cf.
  `b2-veto-amplification-cycle.md` §« La procédure d'amendement »).
- Archivage D4 dans le journal Council avec ligne
  `veto_amplification: Wonder Woman, classe: depense-recurrente,
  ajout: métrique chiffrée par ligne`.
- **Pas d'escalade B1** — la wheel 8-domain n'est pas modifiée.

### Lecture B — Extension du périmètre Finance au triangle

Wonder Woman **étend** son périmètre au-delà des dépenses
individuelles : elle arbitre aussi les **lancements** dont la
métrique de retour à 30 jours est absente. C'est une **extension
de rôle** au triangle Growth ×Finance ×Product (cf.
[[wonder-woman-growth-finance-product-triangular-coupling]]).

**Argument** : le triplet 58 parle d'**une métrique par ligne**, ce
qui peut référencer à un **lancement** (chacune de ses lignes = un
poste de dépense), pas seulement à une **dépense récurrente**. Le
couplage triangulaire Growth ×Finance ×Product émerge précisément
quand un lancement cumule plusieurs dépenses Growth + Product.

**Conséquence procédurale** :
- Adoption par le Council à **unanimité + escalate B1**
  (modification du périmètre d'un capitaine = modification de la
  wheel 8-domain).
- Archivage D4 dans le journal Council avec ligne
  `perimeter_extension: Wonder Woman, classe: lancement-payant,
  ajout: blocage_si_roi_30j_negatif`.
- **Escalade B1 obligatoire** — la wheel 8-domain est touchée.

## Pourquoi la Lecture A est canoniquement défendable

Trois arguments penchent vers la Lecture A :

### 1. Le triplet 28 est la base d'amplification canonique

Le triplet 28 pose le veto catalogue de Wonder Woman. Le triplet 58
est explicitement étiqueté `seeAlso` (référence liée) au triplet 28
dans le format JSONL. C'est la **convention canonique** pour
signaler une amplification du triplet précédent, pas une extension
de périmètre.

`b2-veto-amplification-cycle.md` §« Les deux lectures de « étend » »
argumente que la Lecture A est **plus défendable** parce que *« le
triplet cite verbatim "doctrine veto-dépense", donc l'extension
est dans le veto, pas dans le périmètre »*. Le triplet 58 ne
mentionne ni Growth ni Product — il reste dans le périmètre Finance
interne.

### 2. La doctrine F1-F25 ne mentionne pas de pouvoir sur les lancements

La doctrine pérenne `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` pose 25
principes F1-F25 sur la solvabilité, le pricing, l'allocation, et
l'arbitrage AI-Agency. **Aucun principe** ne donne à Wonder Woman
un pouvoir de blocage sur les lancements Growth ×Product. Le
principe F1 (runway), F4 (real net margin), et F13 (two-horizon)
donnent des **garde-fous de solvabilité** (veto catalogue, blocking
authority, red flag #4), pas un pouvoir de blocage launch.

Si la Lecture B était canonique, la doctrine F1-F25 mentionnerait
explicitement un **principe F-numéro** sur le lancement. Elle ne
le fait pas.

### 3. La distinction veto catalogue / extension périmètre est dans `b2-veto-amplification-cycle.md`

La doctrine d'amplification (`b2-veto-amplification-cycle.md`
§« L'amplification n'est pas la réécriture ») pose explicitement :

> *« L'amplification ajoute une exigence, elle n'enlève rien. Une
> réécriture de veto [...] est un acte différent : c'est un
> resserrement du périmètre qui peut libérer des cas
> précédemment bloqués. La réécriture exige l'unanimité du Council
> + escalate B1. L'amplification n'exige que la majorité simple +
> journal D4. »*

La Lecture B est une **extension de périmètre**, pas une
amplification — elle exige unanimité + B1. La Lecture A est une
**amplification intra-classe** — elle exige majorité simple +
journal D4.

## Pourquoi la Lecture B est aussi défendable

Trois arguments en faveur de la Lecture B :

### 1. Le triplet 58 mentionne « ligne », pas « dépense »

Le triplet 58 parle de **« chaque ligne »** (doit porter une
métrique de retour chiffrée). Une « ligne » peut référencer :

- Une **ligne de dépense** récurrente (Lecture A).
- Une **ligne de budget** dans un lancement (Lecture B — un
  lancement cumule plusieurs postes).
- Une **ligne d'allocation** dans une réallocation F19-F22
  (Lecture B étendue).

Si le triplet visait strictement la dépense récurrente, il aurait
dit « chaque dépense récurrente » (verbatim triplet 28) au lieu de
« chaque ligne ». La nuance lexicale suggère un périmètre plus
large.

### 2. Le couplage triangulaire Growth ×Finance ×Product est posé

Le concept `wonder-woman-growth-finance-product-triangular-coupling.md`
(rapport tour 2) pose le triangle comme **couplage émergent** qui
se manifeste quand les pair-checks #5 et #6 sont activés en
parallèle sur le même launch. Le triplet 58 pourrait être la
**doctrine implicite** de ce triangle — le « étend » de Wonder
Woman vers le launch.

### 3. La triple occurrence « dette récurrente / métrique / ligne » est canonique

Le triplet 58 cite « dette récurrente » et « métrique de retour
chiffrée ». La doctrine F19-F22 sur la trésorerie et l'allocation
(rapport tour 2 ouvert) parle précisément de dette récurrente et
de métrique. La Lecture B active F19-F22 dans le périmètre
Finance.

## Recommandation au B2 Council — Lecture A canonique

**Position retenue** : la Lecture A est canonique. Trois raisons
opératoires :

### 1. Risque procédural plus faible

La Lecture A (majorité simple 5/8 + journal D4) est plus rapide à
adopter que la Lecture B (unanimité + B1). Une adoption rapide
évite que la doctrine Finance reste ambiguë pendant un cycle
12WY entier.

### 2. Cohérence avec le triplet 28

Le triplet 28 pose le veto canonique. Le triplet 58, étiqueté
`seeAlso`, est l'amplification attendue. La cohérence procédurale
demande que l'amplification suive la procédure d'amplification,
pas une procédure d'extension de périmètre.

### 3. Le triplet 58 ne contient pas de pivot sémantique

Le triplet 58 parle toujours de « dépense récurrente » (la dette
récurrente est une forme de dépense récurrente). Il n'y a pas de
pivot sémantique vers « lancement », « pricing », ou « produit ».
La Lecture A est **plus littérale**, la Lecture B est
**plus inférentielle**.

## Le test cycle recommandé — 60 jours, 3 packets

Pour valider la Lecture A canonique, je recommande un **test
cycle** :

- **Cadence** : 60 jours (2 sprints VP × 4 sprints/semaine).
- **Cible** : 3 packets mésoperpétuels où Wonder Woman oppose
  l'amplification « métrique de retour chiffrée par ligne » à une
  dépense récurrente.
- **Mesure** : le Council accepte-t-il l'amplification par majorité
  simple 5/8 ? Le triplet 58 est-il cité verbatim dans le packet
  ? Le journal D4 archive-t-il la ligne `veto_amplification` ?
- **Issues** :
  - **3/3 accept** → Lecture A confirmée canonique.
  - **2/3 accept** → Lecture A confirmée partiellement, escalade
    B1 sur le cas refusé.
  - **1/3 ou 0/3 accept** → Lecture B probable, retraitement du
    triplet 58 en extension périmètre (unanimité + B1).

**Action attendue** : Wonder Woman consigne le test cycle dans son
prochain Rock B2-FINANCE, et remonte les 3 packets au Council
pour adoption.

## Anti-pièges

- **Adopter la Lecture B par prudence.** La Lecture B élargit
  spectaculairement le périmètre Finance — c'est une décision
  stratégique, pas une amplification tactique. Le Council doit
  résister à la tentation de « plus de pouvoir » quand la doctrine
  canonique ne le demande pas.
- **Refuser le triplet 58 comme non-canonique.** Le triplet est
  dans le canon (`triplets/v3-business.jsonl`), il est attribué à
  Wonder Woman, il est cohérent avec le triplet 28. Le refuser
  serait une perte de doctrine.
- **Confondre amplification et extension.** L'amplification
  (**Lecture A**) ajoute une exigence chiffrée au veto catalogue.
  L'extension (**Lecture B**) ajoute un pouvoir de blocage sur les
  lancements. Les deux ne sont **pas** équivalentes en procédure.
- **Adopter sans test cycle.** Adopter la Lecture A canonique
  sans observer son application en cycle réel ouvre la porte aux
  abus (Wonder Woman qui oppose l'amplification « par défaut » sans
  motif vérifiable, comme un veto politique).
- **Ignorer le test cycle.** Si 60 jours passent sans que Wonder
  Woman ait opposé l'amplification 3 fois, c'est un signal que la
  Lecture A est trop étroite ou trop large pour le besoin réel.

## Liens

- [[wonder-woman-recurrent-spend-veto]] — le veto catalogue amplifié
- [[wonder-woman-red-flag-4-trigger]] — le red flag #4 transversal
- [[wonder-woman-growth-finance-product-triangular-coupling]] — le triangle (Lecture B)
- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — la doctrine F1-F25
- [[b2-veto-amplification-cycle]] — la procédure d'amplification
- [[b2-council-arbitrage-rule]] — qui adopte

## Note de confiance

**Confirmé par machine** sur le triplet 58 (ligne 58 verbatim, JSONL
`seeAlso`). **Reconstruit** sur les deux lectures — la doctrine
`b2-veto-amplification-cycle.md` pose les deux lectures explicitement
sans trancher. **Reconstruit** sur la recommandation Lecture A —
trois arguments procéduraux (rapidité, cohérence, littéralité)
sans source canonique directe. **À valider en cycle réel** : le
test 60 jours / 3 packets dépend de l'observation d'au moins 3
dépenses récurrentes candidates à l'amplification. Si le volume
réel est plus faible, le test cycle s'étend à 90 jours.