---
type: Concept
title: Cyborg triplet 58 amplification — packet mésoperpétuel final Council-ready (date de revue ≤30j + métrique de réversibilité)
description: Le tour 3 concept `cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft.md` pose le draft d'amplification triplet 58 (date de revue ≤30j + métrique de réversibilité) pour le veto §07 cloud-only-sans-sortie. Ce concept pose la **forme finale Council-ready** : packet mésoperpétuel complet conforme `b2-meso-decision-packet-spec.md` 7 champs obligatoires + extensions optionnelles `mediation_actor` + `l0_dependency_ref` + `gate_state_update` + `analytics_v5_consumption_signed_by`, 3 cas d'observation post-pivot (Edge Runtime Vercel / JWT hook HITL A0 / Solaris civic-grade), 3 cas d'abus (Vercel Node portable / Supabase Auth standard / Dokploy rétroactif), 4 étapes procédure adoption, 3 issues adoption/rejet/escalade B1, et 4 contre-arguments Superman-style défendables.
tags: [cyborg, triplet-58, amplification, council-ready, packet, veto-07, date-revue, reversibilite, cloud-only]
generated: { by: minimax-m3, at: 2026-08-19T09:10:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-4, at: 2026-08-19T09:10:00Z }
sources:
  - id: cyborg-tour-3-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft.md"
    title: Cyborg triplet 58 amplification — draft Council tour 3
    last_modified: 2026-08-19
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — cycle, 3 conditions, D4
    last_modified: 2026-08-19
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 7 champs
    last_modified: 2026-08-19
  - id: triplet-58-source
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 (Wonder Woman étend doctrine veto-dépense) — modèle d'amplification"
    last_modified: 2026-08-17
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council cadence hebdomadaire + quorum 5/8
    last_modified: 2026-08-19
  - id: adr-omk-004
    resource: "C:/Users/amado/ASpace_OS_V2/.../ADR-OMK-004_pivot-supabase-cloud-vercel.md"
    title: ADR-OMK-004 RATIFIED 2026-06-19 — pivot Dokploy → Vercel/SupabaseCloud (Conditions B/D/E HITL pending)
    last_modified: 2026-06-19
  - id: cyborg-souverainete
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-souverainete-apres-adr-omk-004.md"
    title: "Souveraineté après ADR-OMK-004 — matrice 7 lignes post-pivot"
    last_modified: 2026-08-19
  - id: cyborg-mediation-actor
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel.md"
    title: "Cyborg — extension packet mediation_actor + l0_dependency_ref (compatibilité D4)"
    last_modified: 2026-08-19
  - id: cyborg-validation-empirique
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-validation-empirique-protocole-3-cas-60j.md"
    title: "Cyborg — protocole validation empirique 3 cas/60j (concept 1 tour 4)"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg triplet 58 amplification — packet mésoperpétuel final

## Synthèse de l'amplification candidate

L'amplification candidate **« date de revue ≤30j + métrique de
réversibilité »** étend le veto §07 (*« Cyborg bloque tout
fournisseur cloud-only sans chemin de sortie documenté »*) avec
**deux exigences supplémentaires** :

1. **Date de revue** : toute décision cloud-only approuvée doit
   porter une `date de revue ≤ 30 jours` post-décision, à laquelle
   le chemin de sortie documenté est **re-vérifié** (game day
   rejoué, IaC mise à jour, clause Aquaman re-vérifiée).

2. **Métrique de réversibilité** : toute décision cloud-only
   approuvée doit porter une **métrique chiffrée** de réversibilité
   (RTO cible, temps de re-création IaC depuis zéro, taille de
   l'export data). La métrique est **mesurée** à T+30 et **vérifiée**
   à T+90.

C'est l'asymétrie Cyborg vs Wonder Woman triplet 58 : Wonder Woman
amplifie son veto *dépense récurrente* avec *« métrique de retour »*,
Cyborg amplifie son veto *cloud-only* avec *« date de revue + métrique
de réversibilité »*. La symétrie est défendable par lecture des 4
leviers Solarpunk (ADR-L2-AAAS-001, cf. tour 2).

## Le packet mésoperpétuel final — Council-ready

Le packet complet, conforme au gabarit `b2-meso-decision-packet-spec.md`
7 champs obligatoires, **prêt à à être soumis en séance hebdomadaire
B2 Council** :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B2-PEER-2026-XX
mode: parallel
impacted_domains:
  - it
  - finance  # Wonder Woman F24 co-signe (cf. concept 3 tour 4)
  - legal   # Aquaman triplet réversibilité co-signe
tradeoff: "Amplification du veto §07 Cyborg par Wonder Woman triplet 58 —
  ajouter 'date de revue ≤30j + métrique de réversibilité chiffrée' à la
  classe 'cloud-only-sans-sortie'. Symétrique à l'amplification Wonder
  Woman 'dépense récurrente-sans-ROI' (triplet 58 verbatim)."
decision: accepted | accepted_conditional | refused
veto_amplification:
  captain: cyborg
  classe_cible: cloud-only-sans-sortie
  amplifications_candidates:
    - exigence: "date de revue ≤30j post-décision"
      justification: "Veto sans date de revue = voeu, pas décision"
      source: triplet-58-modèle  # Wonder Woman verbatim
    - exigence: "métrique de réversibilité chiffrée"
      justification: "Triplet canonique contrat + IaC + failover
                      sans métrique = réversibilité non documentée"
      source: cyborg-couplage-aquaman-reversibilite
  procedure_d_amendement:
    condition_1_observation_documentee:
      cas: "ADR-OMK-004 RATIFIED 2026-06-19 — 3 conditions HITL A0 pending
           (B JWT hook / D Vercel Authentication OFF / E PAT rotation)
           = observations documentées d'un cas-limite où date de revue
           + métrique réversibilité auraient aidé"
      source: ADR-OMK-004 §Conditions
    condition_2_regle_une_phrase:
      phrase: "Veto §07 + date de revue ≤30j + métrique de réversibilité."
    condition_3_archivage_D4:
      journal: "B2_DC_DIRECTION_COUNCIL_DECISIONS.md"
      ligne: "veto_amplification: cyborg, classe: cloud-only-sans-sortie,
             ajout: date-revue-30j + metric-reversibilite,
             depuis: B2-MESO-DECISION-2026-XX"
      effet_date: 2026-MM-DD
proof_expected:
  - B2 gate catalog update (veto §07 amplifiée)
  - B3 proof path (IT_Kang_Dynasty_3_cas_observation_60j)
red_flag: no
superman_reading: v4_canonical  # symétrie avec packet type Superman
mediation_actor:
  - actor: river_song
    role: L0
    ref: triplet-38 (ligne 38)  # cf. cyborg-couplages-l0
    status: informed
  - actor: rick_sobriety
    role: A1
    ref: B2_Cyborg_IT_Dispatch_P11_P13
    status: informed
l0_dependency_ref:
  - type: triplet
    id: triplet-38-cyborg-dependsOn-river-song
    location: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl ligne 38"
gate_state_update:
  domain: it
  veto_classe: cloud-only-sans-sortie
  previous: categoriel-only
  new: categoriel-amplifié
  amplification_date: 2026-MM-DD
  source_packet: B2-MESO-DECISION-2026-XX
next_review: 12WY-2026-Q4
```

## Les 3 cas d'observation post-pivot (Condition 1 remplie)

### Cas 1 — Edge Runtime Vercel (juin 2026)

**Observation** : `ADR-OMK-004` §Conditions ligne 207 verbatim cite
Vercel Edge Runtime comme dépendance post-pivot. Edge Runtime est
**catégoriellement cloud-only** (Vercel-only), mais **techniquement
non-portable** vers Node.js standard sans réécriture.

**Cas-limite** : la décision cloud-only (Edge Runtime) a été
**acceptée** par le pivot sans date de revue explicite ni métrique
de réversibilité. L'amplification triplet 58 aurait exigé :

- Date de revue T+30j pour re-vérifier le chemin de sortie Edge
  Runtime (Node.js standard).
- Métrique de réversibilité : temps de réécriture Edge → Node.

**Statut** : cas-limite observé, amplification applicable a posteriori.

### Cas 2 — JWT hook HITL A0 (juin 2026 - ongoing)

**Observation** : `ADR-OMK-004` §Condition B (HITL A0 pending) cite
*« re-provision manuel du custom_access_token_hook sur Cloud »*.
Le hook Auth est sur self-host `148.230.92.235`, non migré Cloud.

**Cas-limite** : la décision cloud-only (Custom Auth Hook Cloud)
est **bloquée** par HITL A0 pending. La métrique de réversibilité
*« temps de re-provision hook Cloud depuis self-host »* n'est pas
chiffrée.

**Statut** : cas-limite observé, amplification applicable a posteriori.

### Cas 3 — Solaris civic-grade variant AaaS (Q3-Q4 2026)

**Observation** : `cyborg-dans-aaas-3-variants.md` (concept 2
tour 2) pose Solaris comme lead IT Cyborg sur infrastructure
*civic-grade* (souveraineté renforcée). La migration Solaris
n'a pas de date de revue post-activation ni de métrique de
réversibilité chiffrée.

**Cas-limite** : la décision cloud-only Solaris est **acceptée**
par hypothèse canonique AaaS, sans amplification triplet 58
appliquée.

**Statut** : cas-limite observé, amplification applicable a
posteriori pour les activations Q3-Q4 2026.

## Les 3 cas d'abus (anti-cas)

### Abus 1 — Vercel Node standard portable

**Cas** : vendor Vercel hébergeant une app Node.js standard (pas
Edge Runtime). L'IaC Terraform standard décrit l'infra, le game day
est joué. **L'amplification triplet 58 NE doit PAS s'appliquer**
parce que le triplet canonique réversibilité est déjà complet sans
amplification.

**Test** : sans amplification, la décision cloud-only est déjà
acceptable (veto §07 levé). L'amplification ajouterait une date de
revue ≤30j qui n'apporte rien (Vercel Node standard est portable
sans réécriture).

**Action** : le Council doit refuser l'amplification sur ce cas.

### Abus 2 — Supabase Auth standard outillé

**Cas** : vendor Supabase Auth standard (go_true, JWT signé,
refresh token). Outillage natif sans custom hook. L'IaC est standard
Supabase CLI, le game day est joué.

**L'amplification triplet 58 NE doit PAS s'appliquer** parce que
le chemin de sortie est documenté par défaut (Supabase CLI export +
restore standard).

**Action** : le Council doit refuser l'amplification sur ce cas.

### Abus 3 — Dokploy rétroactif (mort)

**Cas** : Dokploy a été tué par ADR-OMK-004. Une décision
cloud-only **antérieure** à la mort de Dokploy ne peut pas être
*amplifiée a posteriori*. Le vendor n'existe plus.

**L'amplification triplet 58 NE peut PAS s'appliquer** parce que
la Condition 1 (observation documentée d'un cas-limite) ne peut
pas être satisfaite pour un vendor mort.

**Action** : le Council doit refuser l'amplification sur ce cas.

## La procédure d'adoption — 4 étapes

### Étape 1 — Soumission Council hebdomadaire

Le packet est inscrit à l'ordre du jour de la prochaine séance
hebdomadaire B2 Council. Le quorum 5/8 est requis pour adoption
(`b2-council-cadence-and-chair.md`).

### Étape 2 — Délibération Council

Trois issues selon le vote :

- **5/8 ou plus** → adoption. L'amplification est actée.
- **3/8 à 4/8** → rejet simple. Le veto §07 reste canonique sans
  amplification.
- **< 3/8 ou désaccord profond** → `escalate_to_B1`. B1 tranche
  en dernier ressort.

### Étape 3 — Archivage D4 + amendement catalogue

Si adoption, le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`
reçoit la ligne :

```
veto_amplification: cyborg, classe: cloud-only-sans-sortie,
ajout: date-revue-30j + metric-reversibilite,
depuis: B2-MESO-DECISION-2026-XX,
date_effet: YYYY-MM-DD,
quorum: 5/8 ou plus
```

Le catalogue `b2-eight-domain-vetoes-catalogue.md` est amendé pour
inclure l'amplification.

### Étape 4 — Effet — protocole validation empirique 3 cas / 60j

Une fois l'amplification adoptée, le protocole `cyborg-validation-
empirique-protocole-3-cas-60j.md` (concept 1 tour 4) entre en
phase d'observation : 3 cas de décisions cloud-only approuvées
avec date de revue ≤30j + métrique de réversibilité chiffrée,
sur 60 jours.

Si les 3 cas remplissent les 5 critères + 3 indicateurs (cf. concept
1), la doctrine est **confirmée**. Sinon, **amendée** ou **invalidée**.

## Les 4 contre-arguments Superman-style défendables

`superman-amplification-council-submission-draft.md` (concept
Superman tour 3) a posé 4 contre-arguments défendables. Cyborg les
reprend symétriquement :

### Contre-argument 1 — « L'amplification alourdit le processus »

**Réponse Cyborg** : la date de revue ≤30j est **unique** (pas une
par événement), et la métrique de réversibilité est **standard**
(temps de re-création IaC + RTO cible). L'amplification ajoute **2
champs** au packet mésoperpétuel, pas une procédure nouvelle.

### Contre-argument 2 — « 30 jours c'est trop court pour une revue »

**Réponse Cyborg** : 30 jours = **1 cycle de sprint B3** (cf.
`b2-bb2-jtbd-handoff-contract.md` §« Cadre d'exécution »). C'est
aligné sur la cadence canonique B2, pas une cadence arbitraire.
Si la revue est trop courte pour un cas, le cas est **probablement
trop complexe pour être cloud-only** — l'amplification force la
réflexion.

### Contre-argument 3 — « La métrique de réversibilité est
invérifiable »

**Réponse Cyborg** : la métrique est **mesurée à T+30** (game day
rejoué, export data testé, IaC restaurée depuis zéro). C'est une
mesure opérationnelle, pas une auto-déclaration. L'invérifiabilité
est un signal que la métrique doit être **plus précise**, pas un
argument contre l'amplification.

### Contre-argument 4 — « Wonder Woman a son amplification, Cyborg
aussi — risque de cascade »

**Réponse Cyborg** : l'amplification triplet 58 a une **procédure
canonique** (`b2-veto-amplification-cycle.md`) qui exige Condition 1
(observation documentée) + Condition 2 (règle en une phrase) +
Condition 3 (archivage D4). Si les 7 autres capitaines proposent
des amplifications, elles suivent la même procédure. La cascade est
**contrôlée par le format**, pas un risque de dérive.

## Les 3 cas où le Council peut refuser l'amplification

Le Council peut refuser l'amplification pour 3 raisons :

### Refus 1 — Condition 1 non tenue

Aucun cas d'observation documentée d'un cas-limite où l'amplification
aurait aidé. C'est peu probable au 2026-08-19 — les 3 cas
d'observation post-pivot (Edge Runtime / JWT hook / Solaris) sont
**documentés** (cf. supra).

### Refus 2 — Condition 2 trop stricte

La règle *« date de revue ≤30j + métrique de réversibilité »*
est trop stricte pour la pratique. Le Council peut amender la
règle (ex : date de revue ≤60j, métrique optionnelle pour les
vendor <100€/mois). Mais c'est un **amendement**, pas un rejet.

### Refus 3 — Quorum non atteint

Le quorum 5/8 n'est pas réuni en séance (cas typique : 7 captains
présents mais 2 abstentions). L'amplification est reportée à la
prochaine séance. Si le quorum reste non atteint pendant 2 cycles,
l'amplification est **retirée** et Cyborg reste sur le veto §07
canonique sans amplification.

## La compatibilité D4 append-only

Le packet est **compatible D4** :

- Les 7 champs obligatoires sont conformes à
  `b2-meso-decision-packet-spec.md`.
- Les extensions optionnelles (`mediation_actor`,
  `l0_dependency_ref`, `gate_state_update`) sont conformes à
  `cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel.md`
  (concept 5 tour 3).
- Le champ `superman_reading: v4_canonical` est conforme au pattern
  packet mésoperpétuel Superman.
- Le champ `analytics_v5_consumption_signed_by` n'est **pas**
  inclus ici (pas applicable à l'amplification veto, seulement aux
  événements analytics).

## La responsabilité tripartite

### Cyborg porte la soumission

Cyborg soumet le packet en séance hebdomadaire. Il porte la
**défense** de l'amplification auprès des 7 autres capitaines.

### Wonder Woman co-signe (F24)

Wonder Woman a posé triplet 58 verbatim. Sa co-signature est
**attendue** — c'est elle qui a créé le précédent d'amplification.
Sans sa co-signature, l'amplification Cyborg n'a pas le **modèle
canonique** à invoquer.

### Le Council arbitre

Le Council tranche entre adoption / rejet / escalate_to_B1 selon
le vote 5/8. L'archivage D4 est **automatique** si adoption.

### B1 tranche l'escalade

Si escalate_to_B1, B1 a la compétence finale sur l'amplification.
B1 peut amender, rejeter, ou adopter avec conditions supplémentaires.

## Anti-pièges spécifiques

- **Amplification alourdissant le veto §07.** Le veto §07 reste
  valide sans amplification. L'amplification ajoute une couche, pas
  elle ne le substitue pas. Le packet sans amplification reste
  Council-ready.
- **Amplification en cascade non contrôlée.** Les 7 autres capitaines
  peuvent proposer des amplifications suivant la même procédure. La
  cascade est **contrôlée par la procédure canonique**, pas un
  risque.
- **Amplification sans observation documentée.** Condition 1 non
  tenue = amplification rejetée. Sans cas-limite observé, l'amplification
  est un pouvoir personnel, pas une doctrine.
- **Amplification sans amendement catalogue.** Si le Council adopte
  mais le catalogue n'est pas amendé, l'amplification n'a pas de
  force canonique. L'archivage D4 + amendement catalogue sont
  **tous deux requis**.
- **Cycle 60j non déclenché post-adoption.** Sans le protocole
  validation empirique (concept 1 tour 4), l'amplification n'est pas
  **vérifiée**. Le Council peut re-amender ou invalider.

## Liens

- [[cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft]] — draft tour 3 (ce concept le finalise)
- [[cyborg-validation-empirique-protocole-3-cas-60j]] — protocole validation empirique post-amplification
- [[cyborg-coupling-aquaman-reversibilite]] — triplet canonique source de l'amplification
- [[cyborg-souverainete-apres-adr-omk-004]] — 3 cas d'observation post-pivot
- [[cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel]] — extensions packet optionnelles
- [[b2-veto-amplification-cycle]] — procédure canonique
- [[b2-eight-domain-vetoes-catalogue]] — catalogue 8 vetos (à amender)
- [[b2-meso-decision-packet-spec]] — format packet
- [[b2-council-cadence-and-chair]] — quorum 5/8
- [[superman-amplification-council-submission-draft]] — modèle format draft

## Note de confiance

**Confirmé par machine** sur le format packet mésoperpétuel 7
champs (`b2-meso-decision-packet-spec.md`), sur la procédure
amplification (`b2-veto-amplification-cycle.md`), et sur le modèle
Wonder Woman triplet 58 (verbatim `triplets/v3-business.jsonl`).
**Reconstruit** sur les 3 cas d'observation post-pivot (Edge
Runtime, JWT hook, Solaris) par lecture d'`ADR-OMK-004` RATIFIED +
`cyborg-dans-aaas-3-variants.md` — chaque cas est un **cas-limite**
vérifiable. **Reconstruit** sur les 3 cas d'abus par lecture critique
de la matrice réversibilité 7 lignes post-pivot — chaque cas est un
**anti-pattern** qui démontre où l'amplification **ne doit pas**
s'appliquer. **Reconstruit** sur les 4 contre-arguments Superman-
style par symétrie avec `superman-amplification-council-submission-
draft.md` — chaque contre-argument est **défendable** parce qu'il
a déjà été défendu par Superman. **Reconstruit** sur les 3 cas de
refus Council par lecture critique de `b2-council-cadence-and-chair.md`
§« Quorum 5/8 » + la procédure d'amendement veto canonique.

**Statut** : packet mésoperpétuel **final Council-ready** posé.
Prêt à être soumis en séance hebdomadaire B2 Council avec quorum
5/8. Compatible D4 append-only. **À soumettre** par Cyborg avec
co-signature attendue de Wonder Woman. Précédent procédural :
amplification veto avec extensions packet optionnelles.