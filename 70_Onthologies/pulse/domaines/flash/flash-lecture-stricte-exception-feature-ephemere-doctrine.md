---
type: Concept
title: Flash lecture stricte exception procedure 5/8 — cas-type canonique « feature éphémère »
description: Doctrine lecture stricte exception procedure 5/8 + D4 pour amender le DoD Flash (concept 21 vague 4) **par exception**, sur des features éphémères qui ne satisfont pas la lecture large par défaut. 1 cas-type canonique « feature éphémère » (build + run < 1 sprint sans DoD long terme) + 4 critères de qualification éphémère + 3 conditions cumulatives lecture stricte + 2 abus typiques + procédure 5/8 + D4 + lien avec le DoD 3 stades.
tags: [flash, product, lecture-stricte-exception, feature-ephemere, doD-amendment, 5-8-procedure, d4, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T11:50:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-5, at: 2026-08-19T11:50:00Z }
sources:
  - id: flash-dod-3-stages-council-submission-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-dod-3-stages-council-submission-draft.md"
    title: DoD 3 stades packet Council-ready B2-MESO-DECISION-2026-41 (concept 21 vague 4)
    last_modified: 2026-08-19
  - id: flash-doD-build-run-sunset-three-stages
    resource: "C:/Users/ADO/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doD-build-run-sunset-three-stages.md"
    title: Flash DoD 3 stades (concept 2 tour 3)
    last_modified: 2026-08-19
  - id: flash-dod-3-stages-council-submission-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-dod-3-stages-council-submission-draft.md"
    title: DoD 3 stades packet — source procédure 5/8
    last_modified: 2026-08-19
  - id: flash-domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-domain-perimeter.md"
    title: Flash périmètre — 4 frontières floues (concept 1 tour 1)
    last_modified: 2026-08-19
  - id: flash-veto-offre-depersonnalisee
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Veto Flash — offre dépersonnalisée (concept 2 tour 1)
    last_modified: 2026-08-19
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — procédure 5/8 + D4
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique
    last_modified: 2026-08-19
  - id: triplet-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash lecture stricte exception procedure 5/8 — feature éphémère

## Le problème que cette doctrine ferme

Le packet `B2-MESO-DECISION-2026-41` (concept 21 vague 4) pose la **lecture large par défaut** du DoD 3 stades build/run/sunset. La lecture stricte est mentionnée comme **exception procedure 5/8** sans exemple concret. Le rapport tour 4 (`RAPPORT_dom-flash.md` §5.3 règle B2 mal ajustée 4 vague 4) signale explicitement : *« Lecture stricte exception procedure 5/8 sans exemple pratique de feature éphémère ayant déclenché la lecture stricte »*.

Cette doctrine **ferme la lacune** en proposant **1 cas-type canonique** (feature éphémère) + **4 critères de qualification** + **3 conditions cumulatives** lecture stricte + **2 abus typiques** à éviter.

## Le cas-type canonique « feature éphémère »

### Définition

Une **feature éphémère** est un artefact dont le cycle de vie complet est **inférieur à 1 sprint** (≤ 2 semaines). Caractéristiques :

- **Build** : < 1 semaine (1-3 jours).
- **Run** : < 1 semaine (5-10 jours).
- **Sunset** : daté à la livraison (la date de fin est **connue** dès la conception).

Exemples typiques :
- Bandeau promotionnel Noël (build 3 jours, run 14-21 jours, sunset pré-daté).
- Landing page campagne single-use (build 1-2 jours, run 7-10 jours, sunset pré-daté).
- Script interne temporaire (build 1 jour, run 3-5 jours, sunset pré-daté).
- Feature bêta fermée (build 5 jours, run 7-10 jours, sunset pré-daté).

### Caractéristique fondamentale

Le **run est plus court que le build**, OU le **run est explicitement daté** à la livraison. C'est l'inverse du cas normal où le run s'étend sur des mois/années.

## Les 4 critères de qualification « éphémère »

Pour qu'une feature soit qualifiée « éphémère » et admissible à la lecture stricte :

1. **Sunset pré-daté** dans la spec initiale (la date de fin est écrite avant la première ligne de code).
2. **Durée totale** (build + run) ≤ 1 sprint standard (≤ 2 semaines pour Captain America, soit 10 jours ouvrés).
3. **Pas de dépendance person-named** (sinon c'est un cas Flash veto, pas un cas lecture stricte exception).
4. **Pas de garantie client long terme** (sinon c'est un cas Aquaman veto sur le périmètre, pas un cas lecture stricte exception).

> *« Les 4 critères sont **cumulatifs** — un seul manque = la feature n'est pas éphémère, le DoD 3 stades standard s'applique. »*

## Les 3 conditions cumulatives lecture stricte

Pour amender le DoD 3 stades **par lecture stricte** sur une feature éphémère (passage du DoD large au DoD strict), il faut **3 conditions cumulatives** :

1. **Condition 1 — qualification éphémère vérifiée** : les 4 critères ci-dessus sont tous validés par Captain America (squad lead Avengers) dans `scrums.md` section « blockers ».
2. **Condition 2 — adoption packet mésoperpétuel lecture stricte** : un packet `B2-MESO-DECISION-YYYY-NN` est produit avec `decision: accepted` ET mention `lecture_stricte_exception: true` ET référence à la feature éphémère (id, pas nom).
3. **Condition 3 — adoption majorité 5/8 + D4 append-only** : la lecture stricte est un **amendement de doctrine** (DoD), pas un amendement de matrice. La procédure est donc **5/8 + D4** (cf. `b2-veto-amplification-cycle.md` §« Procédure 5/8 + D4 »).

> *« Les 3 conditions sont **cumulatives** et **vérifiables**. Sans l'une, la lecture stricte ne s'applique pas — la lecture large par défaut reste en vigueur. »*

## Les 2 abus typiques à éviter

### Abus 1 — Qualifier une feature long-terme en « éphémère » pour échapper au DoD

**Symptôme** : une feature avec run > 1 mois est qualifiée « éphémère » parCaptain America pour éviter le DoD 19 critères (7 build + 6 run + 6 sunset).

**Détection** : le critère 2 (durée totale ≤ 1 sprint) est violé. Batman (B2 Ops) détecte par le run > 1 sprint mesuré.

**Remède** : Batman refuse la qualification « éphémère » et **remonte le fait** à Flash (cf. triplets 56/57). Flash re-qualifie en DoD standard.

### Abus 2 — Lecture stricte par défaut sur toutes les features

**Symptôme** : Flash invoque la lecture stricte systématiquement, sans qualification « éphémère », pour alléger le DoD Flash.

**Détection** : la condition 1 (qualification éphémère) est violée par construction (toutes les features passent en lecture stricte). Aquaman (B2 Legal) détecte par l'absence de garantie client long terme systématique.

**Remède** : Aquaman oppose son veto (triplet 30) sur les garanties client et **escalade** au Council. Le Council invalide la lecture stricte par défaut et rappelle la lecture large par défaut.

## Le packet mésoperpétuel type lecture stricte exception

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN  # année-NN
source_mandate: B2-PEER-YYYY-NN  # peer-B2 (Captain America → Flash)
mode: parallel
impacted_domains:
  - product
tradeoff: "Lecture stricte exception sur feature éphémère <feature_id>. Sunset
  pré-daté <YYYY-MM-DD>. Durée totale <X> jours (< 1 sprint). 4 critères qualification
  éphémère validés par Captain America. DoD 19 critères amendé à <N> critères stricts
  éphémères (build_only / run_only / sunset_only)."
decision: accepted
lecture_stricte_exception: true  # champ ajouté pour traçabilité
feature_id: <id>
feature_sunset_date: <YYYY-MM-DD>
feature_duree_totale_jours: <X>
criteria_qualification_ephemere:
  - sunset_pre_date: true
  - duree_totale_sprint_inf_1: true
  - pas_dependance_person_named: true
  - pas_garantie_client_long_terme: true
proof_expected:
  - B2 gate product update (dod_lecture_stricte_amended)
  - B3 proof path (captain_america_validation_scrums_blockers)
  - B1 review (b1_escalade_doctrine_dod_validation)
next_review: <feature_sunset_date + 30j>  # 30j après sunset pour ré-évaluation
```

> *« Le champ `lecture_stricte_exception` est **projeté** (non-canonique) — extension du format packet mésoperpétuel pour les lectures strictes par exception. À soumettre Council pour adoption. »*

## Le lien avec les autres concepts Flash

- **Concept 21 vague 4** (`flash-dod-3-stages-council-submission-draft`) : le packet source qui pose la lecture large par défaut et mentionne la lecture stricte par exception. Ce concept 30 **déploie l'exception**.
- **Concept 2 tour 3** (`flash-doD-build-run-sunset-three-stages`) : le DoD 3 stades source avec 19 critères agrégés (7+6+6). La lecture stricte **réduit** ce DoD à un sous-ensemble éphémère.
- **Concept 1 tour 1** (`flash-domain-perimeter`) : les 4 frontières floues du périmètre Flash — la lecture stricte est une lecture **restreinte** du périmètre DoD, pas une lecture stricte du périmètre domaine.
- **Concept 2 tour 1** (`flash-veto-offre-depersonnalisee`) : le veto Flash qui **ne s'applique pas** aux features éphémères (critère 3 lecture stricte = pas de dépendance person-named). Le veto est orthogonal à la lecture stricte.

## Anti-pièges

- **Lecture stricte sans qualification éphémère** — sans les 4 critères validés, la lecture stricte est abusive. Captain America doit vérifier les 4 critères dans `scrums.md`.
- **Lecture stricte sans packet mésoperpétuel** — la lecture stricte est un **amendement de doctrine**, pas une décision opérationnelle Captain America. Sans packet, l'amendement n'est pas Council-tracé.
- **Lecture stricte sans majorité 5/8** — la lecture stricte reste en draft si elle n'est pas adoptée en Council. Sans adoption, Captain America ne peut pas l'appliquer.
- **Feature éphémère sans sunset pré-daté** — le sunset pré-daté est le **critère cardinal** de l'éphémère. Sans sunset pré-daté, ce n'est pas éphémère, c'est un run classique qui dégénère.
- **Confondre éphémère et sunset-backlog** — un sunset-backlog (concept 1 tour 3 § failure modes) est une feature **non** sunsetée dont le sunset a été oublié. Une feature éphémère a un sunset **pré-daté dès la conception**.

## Liens

- [[flash-dod-3-stages-council-submission-draft]] — packet source lecture large par défaut (concept 21 vague 4)
- [[flash-doD-build-run-sunset-three-stages]] — DoD 3 stades source (concept 2 tour 3)
- [[flash-domain-perimeter]] — périmètre Flash (concept 1 tour 1)
- [[flash-veto-offre-depersonnalisee]] — veto Flash (concept 2 tour 1)
- [[flash-doctrine-valeur-artefact-test-of-continuity]] — test 4D (concept 1 tour 3)
- [[b2-veto-amplification-cycle]] — procédure 5/8 + D4 doctrine
- [[b2-meso-decision-packet-spec]] — format packet canonique
- [[triplets-v3-ligne-25]] — Flash veto offre-depersonnalisee

## Note de confiance

**Confirmé par machine, doctrine saisissable.** Le cas-type « feature éphémère » est **construit** à partir de pratiques courantes (bandeau promotionnel, landing page campagne) + canonique OMK (script interne temporaire, feature bêta fermée). Les 4 critères de qualification sont **projetés** depuis le triplet 25 (pas de dépendance person-named — orthogonal au veto) + triplet 30 Aquaman (pas de garantie client long terme). Les 3 conditions cumulatives lecture stricte sont **cohérentes** avec `b2-veto-amplification-cycle.md` §« Procédure 5/8 + D4 » (amendement doctrine). Le champ `lecture_stricte_exception` est **projeté** (non-canonique) — extension du format packet mésoperpétuel. Les 2 abus typiques sont **construits** à partir des pair-checks canoniques (Batman Ops détecte abus 1 sur critère 2, Aquaman Legal détecte abus 2 sur critère 4). **0 cas pratique observé à date** — la doctrine est saisissable, l'activation dépend d'une feature éphémère effectivement qualifiée et d'un packet mésoperpétuel produit. Standing : doctrine Council-ready pour activation à la première feature éphémère détectée en cycle.