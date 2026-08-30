---
type: Concept
title: Flash DoD 3 stades build/run/sunset — packet Council-ready B2-MESO-DECISION-2026-41
description: Packet mésoperpétuel saisissable au B2 Council pour amender la doctrine Flash DoD confondu en 3 stades distincts (build/run/sunset). 19 critères chiffrés agrégés (7 build + 6 run + 6 sunset) + RACI stade-dépendant + lecture large par défaut + procédure d'amendement pour lecture stricte. 6 champs obligatoires + 4 proof_expected + 3 conditions cumulatives adoption.
tags: [flash, product, dod, build-run-sunset, three-stages, doctrine-amendment, council-submission, b2-council]
generated: { by: minimax-m3, at: 2026-08-19T09:35:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-4, at: 2026-08-19T09:35:00Z }
sources:
  - id: flash-dod-3-stages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doD-build-run-sunset-three-stages.md"
    title: Flash DoD build/run/sunset three stages
    last_modified: 2026-08-19
  - id: flash-jtbd-emit-receive
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-jtbd-emit-receive.md"
    title: Flash JTBD emit/receive — DoD confondu source
    last_modified: 2026-08-19
  - id: flash-doctrine-valeur-artefact
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doctrine-valeur-artefact.md"
    title: Doctrine valeur d'artefact — 4 unités de parole B2
    last_modified: 2026-08-19
  - id: flash-red-flag-1-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-red-flag-1-trigger.md"
    title: Red flag #1 trigger Product green/Ops IT red
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique
    last_modified: 2026-08-19
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — A = B2 en aval
    last_modified: 2026-08-19
  - id: b2-council-cadence-and-chair
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: Cadence hebdomadaire du B2 Council
    last_modified: 2026-08-19
  - id: triplet-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 17 — Avengers 7 techniciens Captain America premier"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash DoD 3 stades build/run/sunset — packet Council-ready

## Le problème que ce packet ferme

Le concept `flash-doD-build-run-sunset-three-stages.md` (tour 3) a décomposé le **DoD Flash confondu** en 3 stades temporels distincts (build / run / sunset). Mais le draft reste **non Council-ready** :

1. RACI stade-dépendant **projeté** sans amendement Council explicite.
2. 19 critères chiffrés agrégés (7+6+6) **arbitraires** par construction.
3. Réconciliation lecture stricte vs large par « large par défaut » — **décision opérationnelle non-canonique**.

Ce concept **transforme le draft en packet mésoperpétuel saisissable**, prêt à être proposé en séance hebdomadaire du Council, avec procédure d'adoption plus légère que l'amendement de matrice (le DoD est une doctrine, pas une matrice — procédure 5/8 + D4, pas unanimité + B1).

## Le packet Council-ready

```yaml
meso_decision_id: B2-MESO-DECISION-2026-41
source_mandate: B2-PEER-2026-09  # peer-B2 identifié en revue doctrine
mode: parallel
impacted_domains:
  - product
tradeoff: "DoD Flash passe d'une grille 8 critères confondus toutes temporalités à
  une grille 19 critères agrégés en 3 stades (7 build + 6 run + 6 sunset). Le coût
  : 1 doctrine à tenir par Captain America à chaque revue hebdo. Le gain : le DoD
  est mesurable distinctement par stade, ce qui permet de signaler une dérive en
  run sans bloquer le build, ou un sunset-backlog sans cacher un run solide."
decision: accepted
proof_expected:
  - B2 gate product update (dod_3_stades_published)
  - B2 gate ops update (batman_run_signal_received)  # Batman reçoit les signaux run de Flash
  - B3 proof path (captain_america_review_hebdo_stade_dépendant)
  - B1 review (b1_escalade_doctrine_dod_validation)
next_review: 2026-11-15  # 12 semaines après adoption
```

## La décomposition 19 critères par stade

**Stade 1 — Build (7 critères)** :

1. Scope signée par Superman (C sur pair-check #11 Growth → Product) ✓
2. Spec testable : ≥ 80% des acceptance criteria chiffrés
3. Code review : 0 PR mergée sans 2 reviewers Avengers
4. Tests unitaires : couverture ≥ 80% sur la nouvelle feature
5. Documentation : README + ADR si décision architecturale
6. Déploiement staging : smoke test OK pendant 24h
7. Handoff Ops (Batman) : runbook + monitoring configuré

**Stade 2 — Run (6 critères)** :

1. uptime ≥ 99% sur 30 jours glissants
2. MTTR ≤ 1h sur incidents P1
3. NPS feature ≥ 40 sur 100 réponses mesurées
4. Rétention J+30 ≥ 90% des users activés
5. Coût run ≤ 1.5x coût build initial
6. Backlog run < 5 tickets ouverts par feature ship

**Stade 3 — Sunset (6 critères)** :

1. Décision sunset documentée (rationale + alternatives)
2. Communication users ≥ 30 jours avant arrêt
4. Migration path vers alternative ou arrêt
3. Données users : export + suppression conforme RGPD
4. Code archivé (read-only repo taggé)
5. Runbook sunset exécuté sans incident P1
6. Post-mortem publié si sunset échoue

## Le RACI stade-dépendant

Le RACI **varie selon le stade**, contrairement au RACI par rang fixe (cf. `b2-pair-check-raci-by-rank.md`) qui s'applique aux pair-checks :

| Stade | A (Accountable) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| **Build** | B2 Ops (Batman) — supportabilité | B3 Avengers | B2 Product (Flash) | B1, B3 Fantastic Four |
| **Run** | B2 Product (Flash) — ownership run | B3 Avengers | B2 Ops (Batman) | B1, B3 Fantastic Four |
| **Sunset** | B1 (Summers) — décision stratégique | B2 Product (Flash) | B2 Ops (Batman), B3 Avengers | tous domaines |

**Justification du RACI stade-dépendant** :

- **Build A = Batman** : la supportabilité opérationnelle est jugée par Batman, pas Flash. Flash livre le code, Batman accepte la charge de run.
- **Run A = Flash** : une fois le feature en run, Flash tient la responsabilité de la qualité (rétention, NPS, coût). Batman est Consulted sur incidents.
- **Sunset A = B1** : la décision d'arrêter un feature est **stratégique** (impact North Star), pas opérationnelle. B1 tranche avec input Flash + Batman.

**C'est une extension du RACI par rang**, pas une contradiction. La matrice canonique V4 fixe A = B2 en aval pour les pair-checks ; ici, A varie selon le **stade temporel** du feature, pas selon le **domaine en aval**. La nuance est dans le temps, pas dans la structure domaine-à-domaine.

## Lecture stricte vs lecture large — réconciliation

Le rapport tour 3 §5.3 a identifié l'ambiguïté : « lecture stricte » (build seul) vs « lecture large » (4 dimensions continuité). La réconciliation proposée dans le packet :

- **Lecture large par défaut** : le DoD s'applique aux 3 stades simultanés. C'est la lecture cohérente avec le test de continuité 4D (concept 1 tour 3) qui pose que la valeur d'un artefact se mesure sur build + run + pivot + sunset.
- **Lecture stricte comme exception** : un domaine peut demander la lecture stricte (build seul) par procédure 5/8 + D4, si la temporalité du feature le justifie (ex : feature éphémère, MVP, proof-of-concept). Cette exception doit être **documentée dans le packet de décision du feature**, pas laissée implicite.

## Les 6 champs obligatoires remplis

1. **`meso_decision_id`** — `B2-MESO-DECISION-2026-41`, format canonique D4.
2. **`source_mandate`** — `B2-PEER-2026-09`, peer-B2 (Flash a identifié l'ouverture en revue doctrine, pas un mandate B1).
3. **`mode`** — `parallel`, parce que le DoD amendé n'affecte qu'un seul domaine (Product). Aucun séquencement cross-domaine requis — Superman et Batman sont informed, pas impactés en séquencement. **Distinct du pair-check #11** qui est `negotiation` parce que bilatéral.
4. **`impacted_domains`** — 1 domaine : product. C'est une doctrine domaine-spécifique.
5. **`tradeoff`** — abandon du DoD confondu au profit d'un DoD stades-dépendant.
6. **`decision`** — `accepted` (par hypothèse, en attente de la séance).

## Les 4 proof_expected

1. **B2 gate product update** : `dod_3_stades_published` — la doctrine est publiée dans `flash-doD-build-run-sunset-three-stages.md` amendé.
2. **B2 gate ops update** : `batman_run_signal_received` — Batman reçoit les signaux run de Flash conformément au RACI stade-dépendant.
3. **B3 proof path** : `captain_america_review_hebdo_stade_dépendant` — Captain America tient la revue hebdo par stade, pas par feature globale.
4. **B1 review** : `b1_escalade_doctrine_dod_validation` — packet escalate à B1 pour ratification de la doctrine DoD 3 stades.

## Les 3 conditions cumulatives d'adoption

L'amendement d'une **doctrine** (pas d'une matrice) suit la procédure **5/8 + D4** (cf. `b2-veto-amplification-cycle.md`), plus légère que l'amendement de matrice (unanimité + B1). 3 conditions cumulatives :

1. **Condition 1 — RACI cohérent avec le RACI par rang canonique.** Le RACI stade-dépendant **étend** le RACI par rang sans le contredire (la variation est temporelle, pas domaine-à-domaine). ✓
2. **Condition 2 — Lecture large par défaut + procédure 5/8 pour lecture stricte.** La réconciliation est documentée dans le packet, pas laissée implicite. ✓
3. **Condition 3 — 5/8 adoption Council + D4 append-only.** Adoption par 5 capitaines sur 8 (Batman, Superman, JohnJones, WonderWoman, GreenLantern minimum, les autres Informed), puis append D4 dans le journal Council.

**Aucune des 3 conditions n'est Council-ready tant que la séance n'est pas tenue.** Le packet est saisissable — la séance est à convoquer.

## La procédure d'adoption en 5 étapes

1. **Vérification préalable** : CaptainAmerica confirme le format + la mesurabilité des 19 critères.
2. **Agenda Council** : inscription à l'agenda hebdomadaire.
3. **Lecture 7 jours** : distribution aux 8 capitaines.
4. **Délibération + vote 5/8** : adoption, amendement, ou rejet.
5. **Append D4 + escalate B1 (information)** : la doctrine est adoptée par le Council, B1 est informé (pas d'escalade de ratification — l'amendement de doctrine est Council-final).

**Effet cible** : 2026-09-15 (cohérente avec packet B2-MESO-DECISION-2026-40 pair-check #11).
**Next review** : 2026-11-15 (1 cycle 12WY complet).

## Anti-pièges

- **Confondre doctrine et matrice.** L'amendement d'une doctrine suit 5/8 + D4. L'amendement d'une matrice suit unanimité + B1. Ce packet amende une **doctrine** (DoD 3 stades), pas une matrice. Procédure plus légère.
- **Critères chiffrés sans source de mesure.** Un critère « NPS ≥ 40 sur 100 réponses mesurées » exige un **chemin de mesure** explicite (PostHog ? Survey ? Log support ?). Le packet pose les chiffres mais les sources de mesure sont à attacher en annexe par le squad lead Captain America.
- **RACI stade-dépendant comme RACI par pair-check.** Le RACI stade-dépendant **n'est pas** un RACI par rang. Il s'applique aux 3 temporalités du feature, pas aux transitions domaine-à-domaine. Confondre les deux casse la matrice canonique.
- **Lecture stricte sans packet de feature.** Tout feature qui demande la lecture stricte (build seul) doit avoir un **packet de décision du feature** documenté. Sinon, lecture large par défaut s'applique.
- **Sunset comme abandon silencieux.** Le stade sunset a 6 critères stricts (communication 30j, migration path, RGPD, archivage) — c'est un sunset **encadré**, pas un kill silencieux.

## Liens

- [[flash-doD-build-run-sunset-three-stages]] — le draft source du packet
- [[flash-jtbd-emit-receive]] — le DoD confondu originel (à amender)
- [[flash-doctrine-valeur-artefact]] — les 4 unités de parole B2 (cadre du DoD)
- [[flash-doctrine-valeur-artefact-test-of-continuity]] — le test 4D qui justifie les 3 stades
- [[flash-red-flag-1-trigger]] — le red flag #1 qui se déclenche au stade build
- [[flash-pair-check-growth-product-council-submission-draft]] — le packet voisin B2-MESO-DECISION-2026-40
- [[b2-meso-decision-packet-spec]] — le format canonique
- [[b2-pair-check-raci-by-rank]] — le RACI par rang (étendu, pas contredit)
- [[b2-veto-amplification-cycle]] — la procédure 5/8 pour amendement de doctrine
- [[b2-council-cadence-and-chair]] — la cadence hebdomadaire

## Note de confiance

**Confirmé par machine, saisissable mais pas Council-adopté.** Le format packet est conforme verbatim. Le RACI stade-dépendant est **cohérent** avec le RACI par rang (extension temporelle, pas contradiction cross-domaine). Les 19 critères chiffrés restent **arbitraires par construction** — la procédure 5/8 laisse au Council le pouvoir d'amender les seuils. La procédure d'adoption 5 étapes est canonique. **0 adoption Council réelle** — le packet est saisissable, la séance est à convoquer, le 5/8 reste hypothétique. Standing : saisissable, à proposer en prochaine séance hebdomadaire (même séance que le pair-check #11 pour symétrie procédurale).