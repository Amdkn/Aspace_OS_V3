---
type: Concept
title: Flash packet mésoperpétuel agrégé — soumettre B2-MESO-DECISION-2026-40 + B2-MESO-DECISION-2026-41 en séance unique
description: Packet mésoperpétuel agrégé B2-MESO-DECISION-2026-42-aggregated qui combine le packet B2-MESO-DECISION-2026-40 (pair-check #11 Growth → Product, concept 20 vague 4) et le packet B2-MESO-DECISION-2026-41 (DoD 3 stades, concept 21 vague 4) en une seule saisine Council. Format 8 champs obligatoires + 6 proof_expected consolidés + 3 conditions cumulatives adoption + procédure d'amendement **distincte par paquet** (matrice unanimité + B1 pour #40, doctrine 5/8 + D4 pour #41) + 4 cas Council-ready.
tags: [flash, product, packet-agrege, pair-check-growth-product, dod-3-stades, seance-unique, b2-council, matrix-vs-doctrine]
generated: { by: minimax-m3, at: 2026-08-19T11:45:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-5, at: 2026-08-19T11:45:00Z }
sources:
  - id: flash-pair-check-growth-product-council-submission-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-check-growth-product-council-submission-draft.md"
    title: Pair-check #11 packet Council-ready B2-MESO-DECISION-2026-40 (concept 20 vague 4)
    last_modified: 2026-08-19
  - id: flash-dod-3-stages-council-submission-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-dod-3-stages-council-submission-draft.md"
    title: DoD 3 stades packet Council-ready B2-MESO-DECISION-2026-41 (concept 21 vague 4)
    last_modified: 2026-08-19
  - id: flash-pair-check-growth-product-candidate-v5
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-check-growth-product-candidate-v5.md"
    title: Pair-check Growth → Product candidate V5 (concept 3 tour 3)
    last_modified: 2026-08-19
  - id: flash-doD-build-run-sunset-three-stages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doD-build-run-sunset-three-stages.md"
    title: Flash DoD 3 stades source (concept 2 tour 3)
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique
    last_modified: 2026-08-19
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — 3 conditions + procédure d'amendement D4
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: b2-council-cadence-and-chair
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council cadence hebdomadaire + chair
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash packet mésoperpétuel agrégé — séance unique

## Le problème que ce packet ferme

Le rapport tour 4 (`RAPPORT_dom-flash.md` §5.4 anti-pièges vague 4 + ouverture 5) recommande *« traiter les 2 packets B2-MESO-DECISION-2026-40 et B2-MESO-DECISION-2026-41 dans la même séance pour éviter les contradictions procédurales (matrice vs doctrine) »*.

Mais les 2 packets ont des **procédures d'adoption différentes** :
- **B2-MESO-DECISION-2026-40** (pair-check #11 Growth → Product) = amendement de **matrice** = unanimité 8/8 + escalate B1 (cf. `b2-veto-amplification-cycle.md` §« Confondre amplification et amendement de matrice »).
- **B2-MESO-DECISION-2026-41** (DoD 3 stades) = amendement de **doctrine** = majorité 5/8 + D4 append-only (cf. `b2-veto-amplification-cycle.md` §« Procédure 5/8 + D4 »).

Un packet « agrégé » qui appliquerait une seule procédure aux 2 = erreur procédurale. La procédure d'amendement de matrice est **plus lourde** que la procédure d'amendement de doctrine — c'est cohérent avec la hiérarchie procédurale canonique.

Ce concept **formalise l'agrégation** en un seul saisissement Council, mais avec **2 procédures distinctes** appliquées indépendamment aux 2 sous-paquets.

## Le gabarit YAML — packet agrégé

```yaml
meso_decision_id: B2-MESO-DECISION-2026-42-aggregated
source_mandate: B2-PEER-2026-10  # pair-check #11 + DoD 3 stades en séance unique
mode: parallel  # 2 sous-paquets indépendants
impacted_domains:
  - product
  - growth  # pour sous-paquet pair-check #11
tradeoff: "Agrégation de 2 saisissables Council-ready Flash en séance hebdomadaire :
  (1) B2-MESO-DECISION-2026-40 — amendement matrice V4 → V5 (ajout pair-check #11
  Growth → Product) — procédure unanimité 8/8 + escalate B1 ; (2) B2-MESO-DECISION-
  2026-41 — amendement doctrine Flash DoD 3 stades — procédure 5/8 + D4. Procédures
  distinctes appliquées indépendamment. Le coût : 1 séance + 2 votes séparés. Le gain :
  cohérence procédurale matrice+doctrine Flash + symétrie avec les 7 autres domaines."
decision: accepted
sub_packets:
  - sub_id: B2-MESO-DECISION-2026-40
    sub_tradeoff: "Amendement matrice V4 → V5..."
    sub_procedure: unanimite_8_8_plus_escalate_b1
    sub_proof_expected: [...]  # 5 proof_expected du packet source
  - sub_id: B2-MESO-DECISION-2026-41
    sub_tradeoff: "Amendement doctrine Flash DoD 3 stades..."
    sub_procedure: majorite_5_8_plus_d4_append_only
    sub_proof_expected: [...]  # 4 proof_expected du packet source
proof_expected:  # preuve globale agrégée (6 éléments)
  - B2 matrix amendment update (matrice_v5_published_with_pair_check_11)
  - B2 doctrine update (dod_3_stades_published)
  - B2 gate growth update (superman_c_signoff_cycle_hebdo)
  - B2 gate product update (flash_a_raci_scope_chiffree)
  - B2 gate ops update (batman_run_signal_received)
  - B3 proof path (captain_america_review_hebdo_stade_dépendant)
next_review: 2026-11-15  # 12 semaines après adoption = 1 cycle 12WY
```

> *« Le champ `sub_packets` est **projeté** (non-canonique) — extension du format packet mésoperpétuel pour les agrégations. À soumettre Council pour adoption si le pattern est validé. »*

## Pourquoi 2 procédures distinctes (matrice vs doctrine)

`b2-veto-amplification-cycle.md` pose la hiérarchie procédurale :

| Type d'amendement | Procédure | Justification |
|---|---|---|
| **Matrice d'harmonisation** (9 pair-checks canoniques) | Unanimité 8/8 + escalate B1 | La matrice est **la règle du jeu** entre les 8 domaines. Toute modification touche potentiellement chaque capitaine → unanimité requise |
| **Doctrine** (veto amplification, DoD, etc.) | 5/8 + D4 append-only | La doctrine est **l'interprétation** que chaque capitaine fait de sa propre règle. Toute modification touche le capitaine lui-même → majorité simple suffit |

L'asymétrie procédurale est **délibérée** : changer la matrice est plus risqué (touche 8) que changer la doctrine (touche 1). Un packet agrégé qui appliquerait la procédure matrice au DoD serait **trop lourd** (unanimité pour ce qui pourrait passer en 5/8). Inversement, un packet agrégé qui appliquerait la procédure doctrine à la matrice serait **trop léger** (5/8 pour ce qui exige unanimité).

## Le mécanisme de vote — 2 votes en 1 séance

1. **Ouverture séance hebdomadaire** par le président du tour (cf. `b2-council-cadence-and-chair.md`).
2. **Lecture packet agrégé** par Flash (B2 Product) — 5 minutes.
3. **Vote #1 — B2-MESO-DECISION-2026-40** (matrice) :
   - **Quorum unanimité** : 8 capitaines présents.
   - **Résolution** : unanimité acceptée, OU 7/8 (escalade B1 obligatoire), OU ≤6/8 (rejet).
   - **Compteur** : 8 voix attendues.
4. **Vote #2 — B2-MESO-DECISION-2026-41** (doctrine) :
   - **Quorum majorité** : 5/8 capitaines minimum.
   - **Résolution** : 5+/8 acceptée, OU 4/8 (rejet, retour draft), OU <4/8 (rejet sans recours).
   - **Compteur** : 5 voix minimum.
5. **Append-only** des 2 décisions à `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` (D4) avec horodatage séance.
6. **Distribution packets amendés** aux 8 capitaines dans les 7 jours.

## Les 4 cas Council-ready

### Cas A1 — Les 2 votes passent (Council adopte tout)

**Scénario** : unanimité 8/8 sur #40 + 5+/8 sur #41. Le packet agrégé est Council-adopté.

**Output** : matrice V5 publiée (pair-check #11 Growth → Product actif) + doctrine DoD 3 stades publiée. Le Flash **passe** au régime matrice V5 + DoD 3 stades.

### Cas A2 — Vote #40 (matrice) passe, vote #41 (doctrine) échoue

**Scénario** : unanimité 8/8 sur #40 + 4/8 sur #41 (rejet, retour draft).

**Output** : matrice V5 adoptée (pair-check #11 actif). Le DoD 3 stades reste en draft (concept 21 vague 4) — Flash amende les critères chiffrés selon les retours Council et ressoumet en séance suivante.

### Cas A3 — Vote #40 échoue à l'unanimité (escalade B1)

**Scénario** : 7/8 sur #40 (unanimité ratée) ou 6/8 (rejet).

**Output** : matrice V4 reste en vigueur. Le pair-check #11 reste **hors matrice canonique**. Flash escalade à B1 (Summers) avec packet `B2-MESO-DECISION-2026-40-escalate` (cf. gabarit concept 24 vague 4) qui reprend le motif du 7/8 ou 6/8.

### Cas A4 — Vote #40 passe, vote #41 passe — mais consultation Captain America manque

**Scénario** : unanimité 8/8 sur #40 + 5+/8 sur #41, mais Captain America (squad lead Avengers) n'a pas été consulté sur le DoD 3 stades (pair-check #3 entrant — Batman aurait dû informer Captain America).

**Output** : packet agrégé **invalide** sur le sous-paquet #41 — le DoD 3 stades exige la consultation Captain America avant adoption. Flash doit **refaire la consultation** et ressoumettre en séance suivante. Le sous-paquet #40 reste adopté (matrice ne dépend pas de Captain America).

## Le lien avec les autres concepts Flash

- **Concept 20 vague 4** (`flash-pair-check-growth-product-council-submission-draft`) : le sous-paquet #40 source.
- **Concept 21 vague 4** (`flash-dod-3-stages-council-submission-draft`) : le sous-paquet #41 source.
- **Concept 3 tour 3** (`flash-pair-check-growth-product-candidate-v5`) : le draft pair-check #11 (concept 3 tour 3) qui a été transformé en packet Council-ready (concept 20 vague 4).
- **Concept 2 tour 3** (`flash-doD-build-run-sunset-three-stages`) : le draft DoD 3 stades (concept 2 tour 3) qui a été transformé en packet Council-ready (concept 21 vague 4).

## Anti-pièges

- **Appliquer une seule procédure aux 2 sous-paquets** — c'est l'erreur procédurale type. La matrice exige unanimité, la doctrine exige majorité. Un packet agrégé doit **explicitement** déclarer les 2 procédures.
- **Confondre agrégation et fusion** — l'agrégation garde les 2 sous-paquets identifiables (champ `sub_packets`). La fusion les mélange et perd la traçabilité.
- **Champ `sub_packets` non-canonique** — c'est une projection, à soumettre Council pour adoption si le pattern est validé sur 2+ cas.
- **Vote #40 à l'unanimité sans escalation** — 7/8 = unanimité ratée = **escalade B1 obligatoire** (cf. `b2-meso-decision-packet-spec.md` §« `decision` » valeurs acceptées). Ne pas oublier.
- **Oublier la consultation Captain America sur #41** — le DoD 3 stades touche la responsabilité Captain America (cf. concept 22 vague 4 responsabilité 1). Sans consultation, le sous-paquet #41 est invalide.
- **Compteur de voix erroné** — unanimité = 8 voix, majorité = 5 voix minimum. Un compteur 7/8 = unanimité ratée, pas majorité.

## Liens

- [[flash-pair-check-growth-product-council-submission-draft]] — sous-paquet #40 (concept 20 vague 4)
- [[flash-dod-3-stages-council-submission-draft]] — sous-paquet #41 (concept 21 vague 4)
- [[flash-pair-check-growth-product-candidate-v5]] — draft source #40 (concept 3 tour 3)
- [[flash-doD-build-run-sunset-three-stages]] — draft source #41 (concept 2 tour 3)
- [[flash-multidomain-cascade-b1-escalation-packet-shape]] — gabarit packet B1-escalation (concept 24 vague 4) — utilisé en cas A3
- [[b2-meso-decision-packet-spec]] — format packet canonique
- [[b2-veto-amplification-cycle]] — procédure 5/8 doctrine + unanimité matrice
- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[b2-council-cadence-and-chair]] — cadence hebdomadaire

## Note de confiance

**Confirmé par machine, gabarit saisissable.** Le format YAML agrégé est conforme verbatim `b2-meso-decision-packet-spec.md` (6 champs obligatoires) + extension `sub_packets` **projetée** pour adoption Council. Les 2 procédures distinctes sont **tirées verbatim** de `b2-veto-amplification-cycle.md`. Les 4 cas A1/A2/A3/A4 sont **construits** à partir des 3 valeurs de `decision` (accepted, blocked, escalate_to_B1) + procédure 5/8. Le mécanisme de vote 2 votes en 1 séance est cohérent avec `b2-council-cadence-and-chair.md`. **0 adoption Council observé à date** — le gabarit est saisissable, l'activation dépend d'une séance hebdomadaire où Flash inscrit les 2 sous-paquets à l'agenda. Standing : gabarit Council-ready pour activation prochaine séance hebdomadaire, avec adoption potentielle avant fin 12WY Q3 2026.