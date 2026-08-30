---
type: Concept
title: Cadence sprint B2 Ops — hebdo (revue) + immédiate (portique)
description: Batman a deux temporalités : la revue hebdo canonique B2 captain (triplet 10) et le portique LAUNCH_READY événementiel. Le rapport tour 1 §T1.5.3 a noté que la cadence hebdo est trop lente pour Ops (Sales signe en continu, Flash merge en continu). Ce concept pose une cadence double : (a) revue hebdo standard B2 le vendredi, (b) portique LAUNCH_READY déclenchable intra-sprint par veto / red flag / launch demandé. Format, déclencheurs, fichiers produits.
tags: [batman, ops, cadence, sprint, hebdo, portique, launch-ready, evenementiel, revue]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: triplet-10
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 10 — chaque VP coupe le rock en 4 sprints hebdomadaires"
    last_modified: 2026-08-17
  - id: triplet-11
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 11 — 5 scrums par semaine B3, une action exécutable par jour"
    last_modified: 2026-08-17
  - id: eight-domain-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — LAUNCH_READY (transverse gate final)
    last_modified: 2026-08-17
  - id: b2-harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation — seuil déclencheur (hebdo + immédiat + post-bloquer)
    last_modified: 2026-08-19
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — cadence de revue
    last_modified: 2026-08-19
  - id: batman-launch-ready
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-launch-ready-portique-final-transverse.md"
    title: LAUNCH_READY — portique final transverse
    last_modified: 2026-08-19
  - id: batman-r1-cadrage
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-batman.md"
    title: "RAPPORT_dom-batman.md §T1.5.3 — cadence hebdo trop lente pour Ops"
    last_modified: 2026-08-19
  - id: batman-r2-cadrage
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-batman.md"
    title: "RAPPORT_dom-batman.md §T2.5.2.D — portique événementiel vs hebdo"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cadence sprint B2 Ops — hebdo (revue) + immédiate (portique)

## La double temporalité Ops

Batman opère sur **deux horloges** :

1. **L'horloge canonique B2 captain** — triplet 10 : *« chaque VP
   coupe le rock en 4 sprints hebdomadaires ; le lundi ouvre le
   sprint, le vendredi le clôt (tenu ou non, avec motif) »*. C'est
   la cadence **revue** où Batman arbitre son sprint.
2. **L'horloge événementielle portique** — LAUNCH_READY est
   posé comme *« transverse gate final »*
   (`eight-domain-avengers-wheel.md`). Un launch demandé, un veto
   posé, un red flag détecté déclenchent le portique **quand
   l'événement arrive**, pas le vendredi.

Les deux horloges ne tournent pas à la même fréquence. La cadence
hebdo rate les dérives naissantes sur la charge de livraison
(`batman-couplage-flash-product-cadence-release.md` §2 — les merges
Flash arrivent en continu). Le portique événementiel rate les
**tendances** lentes (dormance, latence d'escalade, drift de
processus).

Ce concept pose une **cadence double** : hebdo + immédiate, avec
des **frontières nettes** entre les deux pour éviter qu'elles
interfèrent.

## La cadence hebdo — vendredi revue B2

### Déclencheur

**Vendredi fin de journée ouvrée** (par défaut 17h locale, modifiable
par chaque VP en `SPRINTS.md`). Avant le weekend — Batman publie
son sprint tenu / non-tenu avant la coupure.

### Format de revue

**Inputs** :
- `SPRINTS.md` du sprint qui se clôt (4 sprints par rock).
- `MrFantastic_ProcessDesign/SCRUMS.md` (5 scrums/semaine,
  triplet 11).
- `HumanTorch_*/SCRUMS.md` (idem si le dossier est créé).
- `batman/_facts/` du sprint (cf.
  `batman-canal-remonte-b1-summers-format-concret.md`).
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` section faits Batman
  pour information.

**Output** :
- **Statut sprint** : `TENU` / `NON_TENU_AVEC_MOTIF` / `NON_TENU_SANS_MOTIF`.
- **Faits structurels/couplage** collectés dans `_facts/` → choix
  de la sortie (constat / signal / escalade).
- **Décisions sprint** (mode parallel / handoff / negotiation)
  consignées dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` si motion.
- **Mis à jour `SPRINTS.md`** : ligne d'en-tête avec statut +
  motif éventuel.

**Durée** : 30-60 minutes de revue par Batman (lecture seule,
pas d'exécution de procédure — l'exécution est B3).

### Les 3 checks obligatoires

1. **Condition d'arrêt** — au moins 1 procédure du sprint porte
   une condition d'arrêt écrite. Si 0, c'est un veto Batman
   implicite sur la procédure — Batman l'écrit dans `_facts/`
   et **ne lance pas le sprint suivant** tant que la procédure
   n'a pas de condition d'arrêt.
2. **Charge B3** — MrFantastic et HumanTorch (et InvisibleWoman /
   TheThing si les charges sont posées) ont un nombre d'actions
   quotidien **tenable** (≤ 5 scrums/semaine par agent). Si un
   agent dépasse, Batman remonte en fait couplage (People).
3. **Portique LAUNCH_READY** — un launch demandé dans le sprint
   doit être en statut `READY` (vert) ou `BLOCKED` (rouge avec
   motif). Pas de statut `IN_PROGRESS` qui traîne.

## La cadence immédiate — portique LAUNCH_READY événementiel

### Déclencheurs (4 cas)

Le portique est déclenché par l'un des 4 événements suivants
(tirés du rapport §T5.5.2.Q et du concept
`batman-launch-ready-portique-final-transverse.md`) :

1. **Veto Batman posé** — Batman oppose un veto (procédure sans
   condition d'arrêt). Le portique passe `BLOCKED` sur la procédure
   vetoée, et Batman publie le motif dans `_facts/` (fait binaire).
2. **Red flag matrice détecté** — Batman détecte un red flag #1
   (Product green, Ops/IT red) ou #3 (Sales green, Ops/People red).
   Le portique passe `BLOCKED` transverse, Batman publie le fait
   couplage (cf. `batman-couplage-flash-product-cadence-release.md`).
3. **Launch demandé par B1 ou Council** — Summers mandate un
   launch, ou le Council arbitre un go. Le portique passe
   `READY` transverse, Batman consigne dans `_facts/`.
4. **Escalade bloquée** — Batman escalade Summers et Summers ne
   répond pas en 5 jours ouvrés (cf. canal Batman §Sortie 3). Le
   portique passe `BLOCKED` sur l'arbitrage en attente, Batman
   consigne le silence (fait structurel).

### Format de portique

**Inputs** : événement déclencheur + son contexte (qui, quoi,
quand, où, pourquoi).

**Output** : ligne dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`
section *« portique LAUNCH_READY Batman — événements »* :

```yaml
portique_id: BATMAN-PORTIQUE-YYYY-NN
date_declenchement: YYYY-MM-DDTHH:MM:SSZ
type_declencheur: veto|red_flag|launch_demande|escalation_bloquee
source_declencheur: <path/evenement>
statut: "READY"|"BLOCKED"
motif: "<si BLOCKED, le motif>"
domaines_impacted: [<liste>]
date_cloture_attendue: YYYY-MM-DD
```

**Durée de traitement Batman** : ≤ 4h ouvrées entre déclencheur
et publication. Pas de revue vendredi uniquement — l'événement
est **immédiat**.

### Les 4 issues possibles

1. **READY vert** — Batman publie `READY`, le Council entérine
   en lecture seule (pas de motion).
2. **BLOCKED rouge avec motion** — Batman publie `BLOCKED` ET
   saisit une motion `B2-MESO-DECISION-YYYY-NN` qui demande
   l'arbitrage.
3. **BLOCKED rouge sans motion** — Batman publie `BLOCKED` sans
   motion — c'est un **signal** au Council, qui décide
   d'arbitrer ou pas.
4. **READY conditionnel** — Batman publie `READY` avec une
   condition explicite (par exemple *« prêt si Flash ferme le
   ticket #NN avant 17h »*). Le conditionnel expire à la date
   indiquée, et le portique bascule en `BLOCKED` si la condition
   n'est pas remplie.

## La frontière entre les deux cadences

Trois règles pour qu'elles n'interfèrent pas :

1. **La revue hebdo ne crée pas de portique.** Si Batman détecte
   un événement portique pendant la revue du vendredi, il
   **diffère** le traitement au lundi matin — pas de mélange
   des deux cadences. Le vendredi est **lecture seule**, pas
   **événementielle**.
2. **Le portique ne crée pas de revue hebdo.** Un portique peut
   signaler un problème structurel, mais la **tendance** (par
   exemple 3 portiques `BLOCKED` en 2 semaines) ne se voit
   qu'en revue hebdo. Le portique n'agrège pas, il **signale**.
3. **Le format est distinct.** Revue hebdo → `SPRINTS.md`
   (statut tenu / non-tenu). Portique → `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`
   (READY / BLOCKED avec motion ou signal). Pas de cross-write.

## Le rôle des B3 squad leads (MrFantastic, HumanTorch)

Les 4 charges B3 sont **tenues au quotidien** par les B3 squad
leads :

- **MrFantastic (ProcessDesign)** — tient le scrums quotidien,
  signale à Batman les triggers `charge_derivee` (Superman Growth
  via Sales) en intra-sprint, pas en attente du vendredi.
- **HumanTorch (Incidents)** — prend l'incident, escalade Batman
  en intra-sprint si l'incident dépasse son seuil d (par défaut
  > 4h ou impact > 5 utilisateurs).
- **InvisibleWoman** (charge à poser par Green Lantern, cf.
  procédure de ré-ouverture) — tiendra probablement la **charge
  Documentation/Communication** transverse.
- **TheThing** (charge à poser par Green Lantern) — tiendra
  probablement la **charge Stabilité/Reversibility** transverse.

Les B3 squad leads **ne déclenchent pas** le portique — ils
**remontent** à Batman, qui décide si le portique est
déclenché. Le portique reste un geste **Batman** (B2 captain),
pas B3.

## Anti-pièges

- **Revue hebdo le vendredi qui dure 4 heures.** Batman passe
  trop de temps en revue, pas assez en escalation. **Garde-fou** :
  si la revue dépasse 90 minutes, Batman **diffère** au lundi —
  pas de revue marathon.
- **Portique sur événement non-significatif.** Batman déclenche
  le portique sur un veto de portée limitée qui ne touche pas le
  cycle — c'est du bruit. **Garde-fou** : le portique ne se
  déclenche que sur les 4 événements listés (veto / red flag /
  launch demandé / escalation bloquée).
- **Mix des deux cadences.** Batman publie un portique en pleine
  revue vendredi ou statue sur un sprint en plein portique —
  l'événement est **perdu** dans le bruit. **Garde-fou** : règle
  1 et règle 2 ci-dessus (frontières nettes).
- **Sprint qui s'ouvre sans condition d'arrêt.** Batman ouvre un
  sprint qui contient une procédure sans condition d'arrêt — c'est
  un veto implicite. **Garde-fou** : check 1 obligatoire en revue
  vendredi.
- **Portique `READY` non-conditionné.** Batman publie `READY`
  sans vérifier les 7 autres domaines — c'est une violation du
  portique **transverse**. **Garde-fou** : check 3 obligatoire —
  les 7 autres domaines doivent être en `READY` ou `BLOCKED`
  explicite, pas en `IN_PROGRESS` dormant.
- **Charge B3 sous-estimée.** Batman ne vérifie pas que MrFantastic
  a ≤ 5 scrums/semaine — la cadence sprint B3 est oubliée.
  **Garde-fou** : check 2 obligatoire en revue vendredi.

## Liens

- [[batman-launch-ready-portique-final-transverse]] — le portique
  en détail (4 cas de refus, 3 étages d'escalade)
- [[batman-canal-remonte-b1-summers-format-concret]] — le format
  `_facts/` où Batman consigne les portiques
- [[batman-couplage-flash-product-cadence-release]] — le trigger
  `charge_derivee` que MrFantastic remonte en intra-sprint
- [[b2-harmonization-matrix-exploitable]] — le seuil déclencheur
  (hebdo + immédiat + post-bloquer) qui justifie la cadence
  double
- [[batman-rupture-dormance-structurelle-wheel-8-domain]] — la
  convergence 0-packet qui rend la cadence double inopérante

## Note de confiance

**Reconstruit, à moitié étayé.** Le triplet 10 (4 sprints hebdo,
lundi ouvre, vendredi clôt) est cité verbatim. Le triplet 11 (5
scrums/semaine B3) est cité verbatim. La position *« LAUNCH_READY
= transverse gate final »* est citée verbatim depuis
`eight-domain-avengers-wheel.md`. Les 3 checks hebdo (condition
d'arrêt / charge B3 / portique) sont **projetés** à partir de
l'anti-piège *« veto implicite sur procédure sans condition »*,
du red flag #3 (Sales green, Ops/People red), et du concept
LAUNCH_READY tour 2. Les 4 déclencheurs de portique sont
**reconstruits** à partir des concepts Batman tour 2-5
(veto / red flag / launch / escalade bloquée). Les 4 issues
possibles (`READY` / `BLOCKED` motion / `BLOCKED` signal /
`READY` conditionnel) sont **projetées** à partir du format
mésoperpétuel et de la pratique Council. Les 3 règles de
frontière sont **mon inférence** — le canon pose la cadence
hebdo (triplet 10) et la matrice d'harmonisation pose le seuil
déclencheur (hebdo + immédiat + post-bloquer), mais le canon ne
pose pas explicitement l'interdit de mélange. Le rôle B3 squad
leads (4 charges) est **reconstruit** à partir des triplets
31-32 et de la procédure de ré-ouverture 2 charges implicites
(cf. concept tour 6). La durée 4h ouvrées et 90 minutes sont
**arbitraires** — alignées sur la pratique sprint standard, pas
posées canoniquement.