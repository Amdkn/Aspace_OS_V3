---
type: Concept
title: Cas Batman rouge sur radar 8-domain — 4 scenarios et seuil de bascule
description: La doctrine dormance `b2-areas-dormants-doctrine` pose 3 états (DORMANT/SHADOW_ACTIVE/ACTIF) mais ne pose pas le seuil de **rouge** sur le radar 8-domain. Le concept propose 4 scenarios qui déclenchent Batman rouge (procédure vide, revue manquée, red flag #1, escalation bloquée) et un seuil de bascule à 2+ scenarios négatifs sur 4. Le seuil distingue Batman *latent* (1 scenario) de Batman *rouge* (2+ scenarios), avec consequences opérationnelles différentes.
tags: [b2, ops, batman, radar, 8-domain, rouge, seuil, scenario, dormant, bascule]
generated: { by: minimax-m3, at: 2026-08-19T06:38:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-5, at: 2026-08-19T06:38:00Z }
sources:
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas Dormants Doctrine
    last_modified: 2026-08-19
  - id: b2-harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: batman-dormance-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-dormance-procedure-6e-dimension.md"
    title: Dormance procedure — 6ᵉ dimension
    last_modified: 2026-08-19
  - id: batman-raci-i-sur-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-raci-i-sur-4-packet-council-ready.md"
    title: Batman I sur #4 — packet Council-ready
    last_modified: 2026-08-19
  - id: etat-domaines
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md"
    title: État des domaines — convergence 0/8
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cas Batman rouge sur radar 8-domain — 4 scenarios et seuil de bascule

## Le trou que ce concept ferme

Le tour 4 (`RAPPORT_dom-batman.md` §T4.5.1.4) a explicitement
signalé ce trou :

> *« Pas de définition explicite d'un cas "Batman rouge" sur le
> radar 8-domain. La doctrine dormance domaine B2 pose 3 états
> (DORMANT/SHADOW_ACTIVE/ACTIF) mais pas le seuil de passage.
> Batman pourrait rester indéfiniment en SHADOW_ACTIVE sans
> conséquence. »*

Le concept **ferme ce trou** en proposant 4 scenarios qui peuvent
déclencher Batman rouge, et un seuil de bascule à 2+ scenarios
négatifs sur 4.

## Pourquoi la doctrine dormance n'a pas posé le seuil

`b2-areas-dormants-doctrine` pose 3 états domaine B2 :

- **DORMANT** : capitaine non nommé.
- **SHADOW_ACTIVE** : nommé mais sans packet mésoperpétuel émis.
- **ACTIF** : ≥ 1 packet mésoperpétuel émis.

L'état **rouge** n'est pas un 4ᵉ état — c'est une **alerte** sur
l'un des 3 états. Un Batman ACTIF peut être **rouge** sans
perdre son statut ACTIF. La doctrine dormance **ne teste pas**
la qualité de l'état, seulement la présence.

## Les 4 scenarios Batman rouge

### Scenario 1 — Procédure vide (6ᵉ dimension : 0 procedure active)

**Définition** : Batman est ACTIF (≥ 1 packet mésoperpétuel émis),
mais **0 procedure en production** (cf.
`batman-dormance-procedure-6e-dimension` §« Les 6 dimensions »,
dimension 4).

**Indicateur** : `dimension_4 = 0` ET `dimension_5 = 0`
(0 procedure active + 0 procedure en pilote).

**Detection** : revue hebdo Batman, vérification des phases 1-5
du cycle de vie Ops.

**Statut tour 5** : scenario **projeté**, jamais détecté (Batman
ACTIF critère n'est pas tenu).

**Conséquence si détecté** : Batman **latent** (pas encore rouge)
si scenario 1 seul. Batman **rouge** à combiner avec scenario 2-4.

### Scenario 2 — Revue manquée 3 fois consécutives

**Définition** : Batman manque **3 revues hebdo consécutives**.
**Indicateur** : compteur `revue_manquee` ≥ 3.

**Detection** : revue hebdo B2 Council —présence capitaine.

**Statut tour 5** : scenario **non observé** (Batman est actif
dans chaque vague, jamais absent).

**Conséquence si détecté** : Batman **rouge** (signal remonte à
Summers via triplet 56).

### Scenario 3 — Red flag #1 déclenché

**Définition** : red flag #1 — *« Product green, Ops/IT red : ne
pas lancer »* (cf. `b2-harmonization-matrix-exploitable` §« Les
5 red flags »).

**Indicateur** : condition `product_ready=green` ET
`ops_ready=red` détectée.

**Detection** : revue hebdo Batman + Product (Flash).

**Statut tour 5** : scenario **non observé** en 4 vagues (tous les
domaines sont en `red` collectif, mais aucun cycle de build n'a
encore déclenché le red flag).

**Conséquence si détecté** : Batman **rouge** d'office (red flag
matrice est un arrêt dur).

### Scenario 4 — Escalation bloquée

**Définition** : Batman remonte un fait à Summers (triplet 56/57)
mais **Summers ne répond pas** dans un délai donné.

**Indicateur** : compteur `remontees_sans_reponse` ≥ 2 sur 30
jours.

**Detection** : revue hebdo Batman, comparaison remontees émises
vs réponses B1.

**Statut tour 5** : scenario **non saisit** (0 packet mésoperpétuel
Batman = 0 remonte à Summers).

**Conséquence si détecté** : Batman **rouge** + packet mésoperpétuel
**Council-ready** pour signaler le blockage B1.

## Le seuil de bascule — 2+ scenarios sur 4

| Batman latent | Batman rouge |
|---|---|
| 0 scenario | 2+ scenarios |
| 1 scenario | |

**Batman latent** est un signal *interne* — Batman et son squad
reconnaissent qu'un scenario est détecté, et prennent les
correctifs sans escalade B2 Council.

**Batman rouge** déclenche un **packet mésoperpétuel** :

- mode : `escalate_to_B1` (cf. `b2-meso-decision-packet-spec`)
- impacted : `[Batman, B1]`
- decision : `escalate_to_B1`
- motif : scenarios détectés

## Cas pratique — Batman latent vs Batman rouge

### Batman SHADOW_ACTIVE (Vague 2 tour 1-2-3-4)

- Scenario 1 : scenario 1 (procedure vide) **projeté**, jamais
  détecté.
- Scenario 2 : 0 revue manquée (Batman présent).
- Scenario 3 : 0 red flag #1 (0 cycle de build).
- Scenario 4 : 0 escalation bloquée (0 remonte à Summers).

**Score** : 0-1 scenario détecté.
**Statut** : Batman **latent** (scenario 1 projeté, jamais
détecté), jamais **rouge**.

### Batman ACTIF (Vague 3 hypothétique)

Si un packet mésoperpétuel est saisi (par exemple par chemin A
portique LAUNCH_READY rouge), Batman passe ACTIF. Les 4 scenarios
restent à détecteur :

- Scenario 1 : dépend des procedures lancées.
- Scenario 2 : dépend de la présence Batman.
- Scenario 3 : dépend des red flags.
- Scenario 4 : dépend des remontees B1.

**Statut** : Batman **ACTIF** est *par défaut* latente (0 scenario).
Le passage à **rouge** exige 2+ scenarios.

## Pourquoi ce seuil n'est pas posé canoniquement

Aucun triplet ne pose un seuil de bascule. La doctrine dormance
est **binaire** (DORMANT / SHADOW_ACTIVE / ACTIF). Le seuil
2+ scenarios est **mon extension** : il transforme la dormance
binaire en **dormance graduelle** (DORMANT / SHADOW_ACTIVE
0-scenario / SHADOW_ACTIVE 1-scenario / ACTIF 0-scenario / ACTIF
2+ rouge).

Cette extension est **cohérente** avec la doctrine, mais **non
posée**. Elle mérite débat en B2 Council.

## Anti-pièges

- **Confondre rouge et SHADOW_ACTIVE.** Le rouge est *transverse*
  (affecte la qualité de l'état), pas un état alternatif. Un Batman
  ACTIF peut être rouge.
- **Scenario 1 = Batman absent.** Faux : scenario 1 mesure les
  procedures (dimension 4-6), pas la présence du capitaine. La
  présence est scenario 2.
- **Compteur binaire (rouge / pas rouge).** Le seuil 2+ scenarios
  est **graduel**, pas binaire. 1 scenario = latent, 2+ = rouge.
- **Délai non posé.** Le scenario 2 (revue manquée 3 fois) pose
  un seuil de 3 sans时限. Le scenario 4 (escalation bloquée)
  pose 30 jours. Ces**chiffres sont arbitraires**, à arbitrer par
  B2 Council.

## Liens

- [[batman-dormance-procedure-6e-dimension]] — la dimension 4-6
  qui inspire scenario 1
- [[b2-areas-dormants-doctrine]] — la doctrine dormance
- [[b2-harmonization-matrix-exploitable]] — le red flag #1
  scenario 3
- [[b2-meso-decision-packet-spec]] — le packet `escalate_to_B1`
- [[batman-rupture-dormance-structurelle-wheel-8-domain]] — la
  convergence 0/8 abordée

## Note de confiance

**Reconstruit, à moitié étayé.** Les 4 scenarios sont **projetés**
par Batman, en cohérence avec la doctrine dormance et la matrice
d'harmonisation. Le seuil 2+/4 est **mon extension** de la
doctrine binaire. Les délais (3 revues, 30 jours) sont **arbitraires**.
**Confiance haute** sur la cohérence doctrinale, **moyenne** sur
le seuil et les délais. À valider en cycle : (1) le seuil 2+/4
est-il partagé par les 8 capitaines ? (2) les délais sont-ils
calibrés ? (3) le scenario 1 (procedure vide) est-il Council-ready
distinct du radar 8-domain ?
