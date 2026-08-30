---
type: Concept
title: Superman — synthèse des 4 règles B2 mal ajustées pour Council submission
description: Le rapport vague 3 a identifié 4 règles B2 qui restent mal ajustées pour Superman : vérifiabilité du veto (persistante vague 2→3), RACI sur les 2 couplages hors matrice (persistante vague 2→3), doctrine dormance vs attente (persistante vague 2→3), validation empirique du veto (nouvelle vague 3). Ce concept synthétise les 4 règles en un packet Council-ready unique B2-MESO-DECISION-2026-23, avec 4 issues adoption/rejet/escalade par règle, et une procédure 5 étapes pour soumission Council.
tags: [superman, growth, b2, regles-malajustees, council, packet, submission, synthese, 4-regles]
generated: { by: minimax-m3, at: 2026-08-19T09:40:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-4, at: 2026-08-19T09:40:00Z }
sources:
  - id: rapport-vague-3
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-superman.md"
    title: Rapport Vague 3 — escouade Superman (Growth/01)
    last_modified: 2026-08-19
  - id: amplification-council-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-amplification-council-submission-draft.md"
    title: Superman — amplification candidate Council-ready (vague 3)
    last_modified: 2026-08-19
  - id: pair-check-v5-brand
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-pair-check-v5-brand-and-analytics.md"
    title: Superman — V5 matrice pair-checks Brand #11 + Analytics #12
    last_modified: 2026-08-19
  - id: needs-signal-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-needs-signal-vs-dormant-8domain-doctrine.md"
    title: Superman — table 8×4 états NEEDS_SIGNAL vs DORMANT
    last_modified: 2026-08-19
  - id: veto-empirical-protocole
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-veto-empirical-validation-protocole.md"
    title: Superman — protocole validation empirique 3 cas/60 jours
    last_modified: 2026-08-19
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique B2
    last_modified: 2026-08-19
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — procédure 4 étapes + 3 conditions
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman — synthèse des 4 règles B2 mal ajustées pour Council submission

## Pourquoi une synthèse, pas un nouveau rapport

Le rapport vague 3 a identifié **4 règles B2 mal ajustées** pour
Superman Growth, dont 3 persistantes vague 2 → vague 3 et 1
nouvelle vague 3. Chaque règle a son **propre concept** Council-
ready :

- Règle #1 (vérifiabilité veto) → `superman-amplification-council-submission-draft.md`
- Règle #2 (RACI couplages hors matrice) → `superman-pair-check-v5-brand-and-analytics.md`
- Règle #3 (dormance vs attente) → `superman-needs-signal-vs-dormant-8domain-doctrine.md`
- Règle #4 (validation empirique) → `superman-veto-empirical-validation-protocole.md`

Ce concept **ne crée pas de nouvelle règle**. Il **synthétise** les
4 règles en un **packet mésoperpétuel unique**
(`B2-MESO-DECISION-2026-23`) que B2 Council peut trancher en une
**séance unique**, au lieu de 4 séances séparées. C'est une
**remontée vers B2** — pas un contournement.

## Le packet de synthèse

```yaml
meso_decision_id: B2-MESO-DECISION-2026-23
source_mandate: B2-PEER-2026-08
mode: negotiation
impacted_domains:
  - growth
  - people
  - it
tradeoff: |
  4 règles B2 canoniques sont mal ajustées pour Superman Growth.
  Synthèse en un packet unique pour arbitrage Council en une séance.
  Les 4 règles touchent 3 domaines (Growth/People/IT) — People en
  transverse (Brand doctrine), IT en transverse (analytics stack),
  Growth en central (veto Superman).
  Les 4 concepts Council-ready vagues 1-3 sont les pièces
  justificatives ; ce packet les agrège sans en modifier le fond.
decision: accepted
proof_expected:
  - B2 gate growth update (GROWTH_READY sur les 4 règles)
  - B2 gate people update (Brand doctrine asymétrie ratifiée)
  - B2 gate IT update (analytics stack pair-check #12 ratifié)
  - B3 proof path (B3-Guardians-validation-empirique-3-cas-60j)
next_review: 2026-11-19
```

Le packet est **conforme** au format canonique 8 champs (cf.
`b2-meso-decision-packet-spec.md`). Le mode **negotiation** est
approprié : 4 règles avec des tradeoffs non triviaux, 3 domaines
impactés, et des impacts croisés entre les règles.

## Règle #1 — Vérifiabilité du veto Superman

**Concept source** : `superman-amplification-council-submission-draft.md`.

**Problème** : le veto Superman catalogue manque la **vérifiabilité**
— c'est un critère de pratique, pas un artefact documentaire.
L'amplification candidate *« date ou horizon mesurable »* restaure
la vérifiabilité par défaut.

**3 issues possibles par Council** :

- **Adoption** (5/8 majorité simple + D4 append-only) : le veto
  Superman catalogue est **étendu** avec l'amplification.
  Effet : `GROWTH_READY` ne peut être émis sans date ou horizon
  mesurable. La vérifiabilité est restaurée.
- **Rejet** (3/8 veto) : l'amplification n'est pas adoptée. Le
  veto Superman reste sans vérifiabilité documentée — la propriété
  *« vérifiable »* reste rhétorique. C'est l'option **statu quo**.
- **Escalade B1** : le Council ne tranche pas et remonte à B1 pour
  réécriture de la règle catalogue. Très rare — B1 ne réécrit
  pas les vetos à la légère.

**Recommandation escouade** : adoption. L'amplification *« date ou
horizon mesurable »* est Council-ready (5/8 quorum documenté) et
**restaure** la propriété catalogue.

## Règle #2 — RACI sur les 2 couplages hors matrice

**Concept source** : `superman-pair-check-v5-brand-and-analytics.md`.

**Problème** : Superman a 2 couplages hors matrice canonique V4 :

- **Brand** (transverse People) — pair-check #11 V5 proposé.
- **Analytics stack** (Cyborg IT) — pair-check #12 V5 proposé.

**3 issues possibles par Council** :

- **Adoption V5** (unanimité 8/8 + B1) : la matrice d'harmonisation
  est étendue avec 2 pair-checks supplémentaires. RACI asymétrique
  Superman Consulted sur #11 et #12.
- **Adoption V5 partielle** (6/8 + B1) : seul l'un des 2 pair-checks
  est ajouté. Brand prioritaire (transverse People plus structurant)
  ou Analytics prioritaire (technique IT).
- **Rejet** : les 2 couplages restent hors matrice. Superman reste
  sans RACI explicite sur Brand et Analytics. C'est l'option
  **statu quo**.

**Recommandation escouade** : adoption V5 partielle, **Brand
prioritaire**. La Brand est transverse People et touche Superman
par la voix publique — c'est le couplage le plus structurant.
Analytics peut attendre une V6.

## Règle #3 — Doctrine dormance vs attente

**Concept source** : `superman-needs-signal-vs-dormant-8domain-doctrine.md`.

**Problème** : la doctrine Aquaman dormante (triplet 35) illustre
3 conditions cumulatives. La distinction **`NEEDS_SIGNAL` (actif)
vs `DORMANT` (inactif)** n'est pas tranchée pour les 7 autres
domaines.

**3 issues possibles par Council** :

- **Adoption table 8×4** (5/8 majorité simple) : la table 8
  domaines × 4 états (READY / NEEDS_SIGNAL / BLOCKED / DORMANT)
  est adoptée. Chaque escouade domaine valide la projection pour
  son périmètre.
- **Adoption table réduite** (5/8) : la table 8×4 est adoptée
  **uniquement pour Superman + Aquaman**. Les 6 autres domaines
  restent en 3 états (sans DORMANT). C'est l'option **progressive**.
- **Rejet** : la distinction NEEDS_SIGNAL / DORMANT reste
  implicite. La doctrine Aquaman reste isolée.

**Recommandation escouade** : adoption table 8×4 **avec
consultation croisée** des 7 autres escouades. Sans consultation,
la projection pour les 7 autres domaines reste unilatérale et
risque d'être invalidée par les pairs.

## Règle #4 — Validation empirique du veto

**Concept source** : `superman-veto-empirical-validation-protocole.md`
+ `superman-veto-cycle-observation-empirical-gap.md` (vague 4).

**Problème** : 0/3 cas observé en 90+ jours. La propriété
*« vérifiable »* du veto catalogue reste rhétorique.

**3 issues possibles par Council** :

- **Adoption protocole** (5/8 majorité simple) : chaque veto
  catalogue adopte un protocole de validation empirique (cible
  chiffrée par captain, 3 cas / 60 jours, 3 conditions de mise à
  jour doctrine).
- **Adoption protocole par Superman seul** (5/8) : Superman adopte
  le protocole, les 7 autres capitaines restent sans protocole
  formalisé. C'est l'option **pilote**.
- **Rejet** : pas de protocole. La validation empirique reste à
  la discrétion de chaque captain.

**Recommandation escouade** : adoption protocole par Superman
seul (option **pilote**). Superman est le plus avancé sur la
question (3 concepts vagues 1-3 + vague 4 gap analysis), et un
pilote Superman permet de tester le protocole avant extension aux
7 autres capitaines.

## Procédure 5 étapes pour soumission Council

Pour que le packet soit effectivement soumis, **5 étapes** sont
nécessaires :

1. **Vérification des 4 concepts sources** — chaque concept est
   Council-ready mais doit être relu par Superman (ou son successeur)
   avant soumission. Cette escouade vague 4 a posé les 4 concepts ;
   la relecture est hors périmètre vague 4.
2. **Inscription à l'ordre du jour Council** — un capitaine B2
   (Superman ou un pair) inscrit le packet `B2-MESO-DECISION-2026-23`
   à l'ordre du jour de la prochaine séance hebdomadaire. Le quorum
   5/8 doit être réuni.
3. **Délibération Council** — les 4 règles sont débattues, avec les
   3 issues par règle. Le président de séance (turning chair, cf.
   `b2-council-cadence-and-chair.md`) tranche les 4 règles **en une
   séance** pour éviter l'éparpillement.
4. **Décision par règle** — chaque règle reçoit une décision
   `accepted` / `blocked` / `escalate_to_B1`. Les 4 décisions sont
   consignées dans **un seul packet mésoperpétuel** (synthèse) ou
   **4 packets séparés** (granularité). L'option **1 packet** est
   recommandée pour la traçabilité.
5. **Append D4 + revue à 90 jours** — la décision est append-only
   dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`. La revue
   `next_review: 2026-11-19` (90 jours) vérifie l'application des
   4 règles adoptées.

## Anti-pièges

- **Confondre synthèse et nouveau packet.** Ce packet
  `B2-MESO-DECISION-2026-23` est une **synthèse** des 4 concepts
  Council-ready vagues 1-3 + vague 4. Il n'introduit **aucune
  nouvelle règle** — c'est un **aggrégat** pour faciliter
  l'arbitrage Council.
- **Adoption V5 sans unanimité.** Règle #2 exige unanimité 8/8 + B1.
  Si Council tente une adoption 5/8, c'est une **violation de
  procédure matrice** (cf. rapport vague 3 §« Réfutation 3 »).
- **Pilote Superman seul永久.** Règle #4 pilote Superman est un
  **essai**, pas un privilege永久. Après 90 jours, le protocole
  est évalué et **étendu** ou **abandonné** selon les résultats.
- **Oublier la consultation croisée pour règle #3.** Règle #3
  table 8×4 sans consultation des 7 autres escouades est
  **unilatérale** et risque d'invalidation par les pairs.
  L'option **progressive** (Superman + Aquaman seuls) évite ce
  risque.

## Statut canonique

**Council-ready, pas Council-adopted.** Le packet est :

- **Proposé** par cette escouade Superman vague 4.
- **Formaté** selon le gabarit canonique 8 champs.
- **Sourcé** sur 4 concepts vagues 1-3 + vague 4 gap analysis.
- **Non soumis** — la procédure 5 étapes relève d'un captain B2
  (Superman ou pair).

**Confiance** : *haute* sur la structure du packet (synthèse 4
règles), *moyenne* sur l'adoption effective (le quorum 5/8 et
l'unanimité 8/8 sont des seuils ambitieux pour une séance réelle).

## Une remarque finale — pourquoi ce packet合成 est utile

Le canon convergence 8/8 domaines vague 1+2+3 a produit 30+
concepts sans aucun packet mésoperpétuel réel observé. Les 4
règles mal ajustées Superman sont **symptomatiques** de cette
convergence : les concepts Council-ready existent, mais le Council
ne les agrège pas en arbitrage réel. Le packet合成
`B2-MESO-DECISION-2026-23` est une **proposition d'agrégation** —
si Superman peut合成 4 règles en 1 packet, les 7 autres capitaines
peuvent en faire autant, et la convergence wheel 8-domain peut
**évoluer** vers une adoption effective.

C'est une **remontée vers B2** sur la **dormance structurelle** de
la wheel (cf. ETAT_DOMAINES vague 3 *« convergence 8/8 sans packet
— dormance structurelle persistante »*). Cette escouade ne peut
pas la résoudre seule — mais elle peut la **signaler** par un
packet Council-ready qui démontre qu'une adoption est possible.

## Liens

- [[rapport-dom-superman-vague-3]] — les 4 règles identifiées vague 3
- [[superman-amplification-council-submission-draft]] — Règle #1 source
- [[superman-pair-check-v5-brand-and-analytics]] — Règle #2 source
- [[superman-needs-signal-vs-dormant-8domain-doctrine]] — Règle #3 source
- [[superman-veto-empirical-validation-protocole]] — Règle #4 source
- [[superman-veto-cycle-observation-empirical-gap]] — Règle #4 gap analysis
- [[b2-meso-decision-packet-spec]] — le format canonique
- [[b2-veto-amplification-cycle]] — la procédure d'amplification
- [[b2-council-cadence-and-chair]] — la cadence Council
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Synthèse Council-ready, pas Council-adopted.** Les 4 règles
proviennent de concepts vagues 1-3 + vague 4 déjà Council-ready.
Le packet合成 est conforme au format canonique 8 champs. Les
3 issues par règle sont **projetées** par lecture critique (cf.
vague 3 rapport §« Règles mal ajustées »), pas vérifiées par une
séance réelle. La procédure 5 étapes est **reconstruite** depuis
`b2-council-cadence-and-chair.md` + `b2-veto-amplification-cycle.md`,
pas citée comme un bloc canonique. **Confiance moyenne** sur
l'adoption effective, *haute* sur la structure de synthèse.
