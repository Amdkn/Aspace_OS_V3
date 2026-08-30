---
type: Concept
title: Flash — cascade multi-domaines veto sur un même artefact
description: Quand un artefact Flash essuie 2+ veto simultanés de domaines différents (ex : Batman sur condition d'arrêt, Wonder Woman sur ROI monitoring, Superman sur promesse non tenue), il n'existe pas de procédure canonique de résolution. La matrice d'harmonisation pose les red flags (cf. b2-harmonization-matrix-exploitable), mais pas l'ordre de priorité quand 2+ vetos catalogue tombent en même temps. Ce concept pose une cascade en 5 étapes avec critères de priorité, un test de cohérence procédurale, et 4 issues canoniques.
tags: [flash, veto, multi-domain, cascade, priorite, harmonisation, red-flag, arbitration]
generated: { by: minimax-m3, at: 2026-08-19T08:50:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-3, at: 2026-08-19T08:50:00Z }
sources:
  - id: b2-eight-domain-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos — propriétés + 4 issues
    last_modified: 2026-08-19
  - id: b2-harmonization-matrix-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères + 5 red flags
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — instance d'arbitrage
    last_modified: 2026-08-19
  - id: b2-three-cooperation-modes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-three-cooperation-modes.md"
    title: Trois modes de coopération B2 — parallel / handoff / negotiation
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Format YAML mésoperpétuel — 8 champs obligatoires
    last_modified: 2026-08-19
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos — triplet 58 Wonder Woman
    last_modified: 2026-08-19
  - id: b1-stop-conditions-escalier
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-stop-conditions-escalier.md"
    title: B1 stop conditions + escalier canonique
    last_modified: 2026-08-19
  - id: flash-red-flag-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-red-flag-1-trigger.md"
    title: Red flag #1 — Product green Ops/IT red
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash — cascade multi-domaines veto sur un même artefact

## Le problème — un cas non couvert

La matrice d'harmonisation pose **5 red flags** canoniques (`b2-harmonization-matrix-exploitable.md` §« Les 5 red flags ») qui bloquent un lancement quand une combinaison de wheel-states rend l'ensemble incohérent. Le **red flag #1** (Product green, Ops/IT red) touche directement Flash : *« Ne pas lancer. Le produit ne peut pas être livré ou maintenu. »*

Mais **2 situations non couvertes** par la matrice :

1. **Veto catalogue simultanés** : un artefact Flash essuie 2+ veto catalogue (Batman sur condition d'arrêt, Wonder Woman sur ROI monitoring, Superman sur promesse non tenue). Le canon ne donne pas d'ordre de priorité.
2. **Red flag + veto catalogue simultanés** : un red flag matrice est déclenché ET un veto catalogue est opposé. Le canon ne dit pas lequel des deux doit être levé en premier.

Le rapport tour 2 (`RAPPORT_dom-flash.md` §5.2 ouverture 7) ne signale pas cette lacune — c'est un gap **non-détecté**. Ce concept ferme le gap en posant une **cascade procédurale en 5 étapes** avec critères de priorité.

## La cascade en 5 étapes

### Étape 1 — Identification des vetos et red flags simultanés

**Trigger** : Flash consigne dans le journal CaptainAmerica qu'un artefact a reçu 2+ veto catalogue OU 1+ veto catalogue + 1+ red flag matrice.

**Action** : Flash déclare l'état **MULTI_VETO_PRESSURE** sur l'artefact. La déclaration est un ping Council (pas un packet mésoperpétuel encore — c'est une alerte).

**Critère d'acceptance** : la déclaration MULTI_VETO_PRESSURE contient :
- ID de l'artefact
- Liste des vetos opposés (capitaine + classe + motif vérifiable)
- Liste des red flags déclenchés (matrice + statut radar)
- Date de détection

### Étape 2 — Cartographie veto × cycle de vie

**Action** : Flash cartographie chaque veto sur le cycle de vie 3 stades (build / run / sunset, cf. `flash-doD-build-run-sunset-three-stages.md`).

**Trois cas** :
- **Tous les veto touchent le même stade** (ex : 3 veto sur build) → cascade classique, le build est bloqué, run et sunset sont en attente.
- **Veto touchent des stades différents** (ex : Batman veto build, Wonder Woman veto run) → cascade complexe, voir étape 3.
- **Veto touchent un stade + red flag** (ex : Batman veto build + red flag #1 Ops/IT red) → cascade prioritaire, voir étape 4.

**Critère d'acceptance** : la cartographie est dans le journal CaptainAmerica avec ligne par veto × stade.

### Étape 3 — Test de cohérence procédurale

**Question** : les 2+ veto opposés sont-ils dans la **même catégorie procédurale** ou dans des **catégories différentes** ?

**Trois verdicts** :
- ✅ **Cohérence procédurale OK** — les veto sont dans la même catégorie procédurale (ex : 2 veto Batman Ops cycle + Aquaman Legal périmètre). Le Council arbitre en **un seul** arbitrage unifié.
- ⚠️ **Cohérence procédurale partielle** — les veto sont dans 2 catégories procédurales proches (ex : Batman Ops cycle + Cyborg IT réversibilité). Le Council arbitre en **deux** arbitrages séquentiels (ordre : cycle avant réversibilité, par convention).
- ❌ **Cohérence procédurale KO** — les veto sont dans des catégories incompatibles (ex : Batman Ops cycle + Superman Growth promesse). Le Council arbitre en **escalade B1** (cf. `b1-stop-conditions-escalier.md` §« Quand l'escalier canonique s'applique »).

**Critère d'acceptance** : le verdict du test est documenté dans le journal CaptainAmerica.

### Étape 4 — Arbitrage Council ou escalade B1

**Trois issues selon le verdict de l'étape 3** :

#### Issue A — Cohérence OK : arbitrage Council unifié

**Mode** : `negotiation` (deux DoDs ou plus en conflit et nécessitent un tradeoff — cf. `b2-three-cooperation-modes.md` §« Negotiation »).

**Action** : le B2 Council convoque les capitaines veto + Flash + CaptainAmerica (squad lead observateur). Le packet mésoperpétuel documente le tradeoff.

**Format mésoperpétuel** :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B2-MULTI-VETO-YYYY-NN
mode: negotiation
impacted_domains:
  - product
  - <autres domaines en veto>
tradeoff: "Artefact X a 2+ veto catalogue simultanés dans la même catégorie procédurale. Le Council arbitre en negotiation."
decision: accepted | blocked | escalate_to_B1
proof_expected:
  - B2 gate update (<veto levé ou amendé>)
  - B3 proof path (artefact re-préparé)
next_review: YYYY-MM-DD
```

#### Issue B — Cohérence partielle : arbitrage séquentiel

**Mode** : `handoff` séquentiel (chaque veto est traité dans l'ordre canonique).

**Action** : B2 Council tranche le premier veto (catégorie procédurale la plus haute dans la hiérarchie), puis le second. Chaque arbitrage produit un packet mésoperpétuel distinct.

**Hiérarchie procédurale canonique (par défaut)** :
1. **Cycle** (Batman Ops veto condition d'arrêt) — le plus haut, touche le 12WY.
2. **Périmètre** (Aquaman Legal veto périmètre prestation)
3. **Réversibilité** (Cyborg IT veto cloud-only)
4. **ROI** (Wonder Woman Finance veto dépense récurrente)
5. **Valeur** (Flash Product veto offre dépersonnalisée — amplifié ou canonique)
6. **Promesse** (Superman Growth veto promesse non tenue)
7. **Reformulation** (JohnJones Sales veto reformulation non validée)
8. **Recrutement** (Green Lantern People veto recrutement sans mandat)

**Justification de la hiérarchie** : l'ordre reflète l'impact sur le cycle de vie (cycle > périmètre > réversibilité > ROI > valeur > promesse > reformulation > recrutement). Le cycle 12WY est le plus contraint, le recrutement est le plus flexible.

#### Issue C — Cohérence KO : escalade B1

**Mode** : `escalate_to_B1` (cf. `b2-meso-decision-packet-spec.md` §« decision »).

**Action** : le packet mésoperpétuel documente les veto incompatibles et remonte à B1. Le motif d'escalade est explicite.

**Format mésoperpétuel** :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B2-MULTI-VETO-YYYY-NN
mode: parallel  # car le Council ne peut pas trancher en parallel
impacted_domains:
  - product
  - <domaines en veto>
tradeoff: "Veto catalogue simultanés dans des catégories procédurales incompatibles. Le Council ne peut pas trancher sans toucher au North Star."
decision: escalate_to_B1
proof_expected:
  - B1 décision
next_review: N/A  # B1 tient la suite
```

### Étape 5 — Consignation et re-vérification

**Action** : le packet mésoperpétuel (issue A, B, ou C) est append-only dans le journal Council. L'artefact est **re-vérifié** dans les 30 jours suivant la décision.

**Critère d'acceptance** : la re-vérification à 30 jours est documentée dans le journal CaptainAmerica avec :
- Statut de chaque veto (levé, amendé, ou maintenu)
- Preuve de la résolution (capture, log, métrique, témoignage client — `b3-proof-path-4-formes.md`)
- Effet sur la wheel 8-domain (un veto levé peut faire basculer un autre domaine)

## 3 cas concrets de cascade

### Cas 1 — Batman veto condition d'arrêt + Wonder Woman veto ROI monitoring

**Contexte** : Flash livre un artefact SaaS builder pour coaching premium. Batman refuse la condition d'arrêt de la procédure (cf. `batman-veto-procedure-sans-condition-arret.md`). Wonder Woman refuse l'allocation récurrente pour le monitoring de l'artefact (cf. `wonder-woman-veto-depense-recurrente.md`).

**Cartographie stade** : Batman veto build (condition d'arrêt de la procédure build), Wonder Woman veto run (monitoring).

**Cohérence procédurale** : Batman cycle (haut), Wonder Woman ROI (moyen). Cohérence partielle.

**Issue** : Issue B (arbitrage séquentiel). Le Council tranche d'abord Batman (catégorie cycle, plus haute). Batman amende la procédure avec une condition d'arrêt. Puis le Council tranche Wonder Woman avec la nouvelle procédure en main.

### Cas 2 — Superman veto promesse non tenue + Batman veto condition d'arrêt

**Contexte** : Superman a publié une promesse « coaching IA premium » avec date de livraison J+30. L'artefact Flash est en retard (J+45). Superman oppose son veto catalogue (promesse que la delivery ne tient pas). Batman oppose son veto (la procédure de late delivery n'a pas de condition d'arrêt écrite).

**Cartographie stade** : Superman veto build (la promesse publique est sur le build), Batman veto build aussi (condition d'arrêt de la procédure).

**Cohérence procédurale** : Superman promesse (catégorie 6), Batman cycle (catégorie 1). Catégories procédurales incompatibles (North Star en jeu).

**Issue** : Issue C (escalade B1). Le packet mésoperpétuel documente le conflit North Star et remonte.

### Cas 3 — Flash veto offre dépersonnalisée amplifié + Aquaman Legal veto périmètre

**Contexte** : Flash oppose son veto amplifié (mécanisme de reprise non documenté — cf. `flash-veto-amplification-council-submission-draft.md`). Aquaman oppose son veto (périmètre de prestation non documenté — triplet Aquaman).

**Cartographie stade** : Flash veto build (valeur), Aquaman veto build (périmètre).

**Cohérence procédurale** : Flash valeur (catégorie 5), Aquaman périmètre (catégorie 2). Catégories procédurales proches.

**Issue** : Issue B (arbitrage séquentiel). Aquaman d'abord (catégorie 2 plus haute). Aquaman amende le périmètre (ajout clause de propriété intellectuelle). Puis Flash tranche avec le périmètre amendé.

## Pourquoi la hiérarchie procédurale est fixée par défaut

`b2-three-cooperation-modes.md` §« Negotiation » pose la matrice de prioritis ation (North Star > cycle > risque > effort). Cette matrice **arbitre le contenu** de la négociation, pas l'**ordre de traitement** des veto simultanés.

L'ordre de traitement proposé (cycle > périmètre > réversibilité > ROI > valeur > promesse > reformulation > recrutement) est **construit** par :
- Impact sur le cycle 12wy (le plus contraint en haut)
- Réversibilité de la décision (le moins réversible en haut)
- Coût d'une décision tardive (le plus coûteux en haut)

C'est une **projection** à partir du triplet v3 et de la doctrine fractal — pas une citation canonique. Le B2 Council peut amender l'ordre en séance par majorité simple.

## 4 issues canoniques en sortie de cascade

| Issue | Quand | Mode Council | Décision type |
|---|---|---|---|
| **A** — Cohérence OK | 2+ veto même catégorie | `negotiation` | `accepted` avec amendement |
| **B** — Cohérence partielle | 2+ veto catégories proches | `handoff` séquentiel | `accepted` avec arbitrage par veto |
| **C** — Cohérence KO | 2+ veto catégories incompatibles | `escalate_to_B1` | `escalate_to_B1` avec motif |
| **D** — Un veto levé en cours de cascade | Un veto tombe avant les autres | `parallel` (le cas redevient mono-veto) | `accepted` ou `blocked` sur les veto restants |

L'issue D est **importante** : un veto peut être levé en cours de cascade (par amendement du mandat, par retrait du mandat, ou par escalade). Si le veto tombe avant les autres, le cas redevient **mono-veto**, et la cascade s'arrête. Le packet mésoperpétuel final documente l'évolution.

## Pourquoi cette cascade n'est pas dans le canon B2

Trois raisons qui expliquent pourquoi cette procédure est absente :

1. **Matrice d'harmonisation focus red flags, pas veto simultanés.** La matrice pose 5 red flags qui sont des arrêts durs, mais les red flags sont des états de wheel, pas des veto catalogue.
2. **Catalogue 8 veto focus classe, pas simultanéité.** Le catalogue pose 8 classes de veto, pas la priorité entre eux. La priorité est implicite (un seul veto à la fois, par défaut).
3. **Vague 2 escouades sans cycle réel.** Les 8 escouades ont produit des concepts mais aucun cycle réel de build n'a été observé (cf. `RAPPORT_dom-flash.md` §5.2 convergence 8/8). La cascade multi-veto n'a pas été testée.

## Anti-pièges

- **Veto comptabilisé comme red flag.** Un veto catalogue n'est pas un red flag matrice. Les red flags sont des états de wheel (8 domaines), les vetos sont des classes de décision. La cascade traite les deux séparément.
- **Hiérarchie procédurale considérée comme canonique.** L'ordre cycle > périmètre > réversibilité > ROI > valeur > promesse > reformulation > recrutement est une projection, pas une citation. Le Council peut amender.
- **Escalade B1 par défaut.** L'escalade B1 (Issue C) doit rester rare. Si elle devient le mode dominant, c'est un signal que la matrice canonique est sous-spécifiée.
- **Issue D ignorée.** Si un veto tombe en cours de cascade, le cas devient mono-veto — le packet mésoperpétuel final doit le documenter, pas le passer sous silence.
- **Cascade appliquée à 1 seul veto.** Si l'artefact n'a qu'1 veto, la cascade ne s'applique pas — c'est le traitement mono-veto standard (`b2-eight-domain-vetoes-catalogue.md` §« La règle de résolution »).

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — le catalogue des 8 veto et leurs 4 issues
- [[b2-harmonization-matrix-exploitable]] — les 5 red flags qui complètent la cascade
- [[b2-council-arbitrage-rule]] — l'instance qui tranche les cascades
- [[b2-three-cooperation-modes]] — les 3 modes parallel/handoff/negotiation
- [[b2-meso-decision-packet-spec]] — le format mésoperpétuel appliqué aux cascades
- [[b2-veto-amplification-cycle]] — le triplet 58 Wonder Woman, précédent de l'amplification
- [[b1-stop-conditions-escalier]] — l'escalade B1 quand Issue C
- [[flash-veto-amplification-council-submission-draft]] — le veto amplifié Flash peut être un des veto simultanés
- [[flash-doD-build-run-sunset-three-stages]] — la cartographie veto × stade de l'étape 2
- [[flash-red-flag-1-trigger]] — le red flag #1 qui peut être combiné avec un veto catalogue

## Note de confiance

**Reconstruit, à moitié étayé.** Le triplet 25 (Flash veto), triplet 58 (Wonder Woman étend), triplet 24 (Batman veto) sont cités implicitement. La matrice d'harmonisation (9 critères + 5 red flags) est **verbatim** de `b2-harmonization-matrix-exploitable.md`. Le catalogue des 8 veto et les 4 issues sont **verbatim** de `b2-eight-domain-vetoes-catalogue.md`. Le format mésoperpétuel (8 champs) est **verbatim** de `b2-meso-decision-packet-spec.md`. La hiérarchie procédurale canonique (cycle > périmètre > réversibilité > ROI > valeur > promesse > reformulation > recrutement) est **mon extrapolation** — pas citée ailleurs dans le corpus. Les 3 cas concrets (Batman + Wonder Woman, Superman + Batman, Flash + Aquaman) sont **projetés** à partir des combinaisons plausibles de veto simultanés sur un même artefact SaaS builder coaching premium. Les 4 issues (A, B, C, D) sont **reconstruites** à partir du triplet v3 + matrice d'harmonisation + catalogue 8 veto — la multiplicité des issues est mon extrapolation. Standing : draft de procédure, à soumettre B2 Council pour validation et à confronter au premier cycle réel de cascade multi-veto observé.