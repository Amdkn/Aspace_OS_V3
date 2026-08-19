---
type: Concept
title: Flash Product — red flag #1, Product-green Ops/IT-red, arrêt dur
description: La matrice d'harmonisation pose le red flag #1 : « Product green, Ops/IT red — ne pas lancer ». Le red flag est un arrêt dur qui bloque le lancement d'un artefact supportable mais non-maintenable. Trois cas de déclenchement concrets (support Ops insuffisant, monitoring IT manquant, runbook absent), trois cas où le red flag est abusif (Ops/IT rouges sur des critères non-pertinents, reds flags temporaires < 7 jours), et la procédure de résolution (escalade B2 Council, escalade B1 si wheel 8-domain impossible).
tags: [flash, product, red-flag, ops, it, lancement, arret-dur, b2-council, escalation]
generated: { by: minimax-m3, at: 2026-08-19T04:35:00Z }
verified:
  - { by: process:lecture-corpus-flash, at: 2026-08-19T04:35:00Z }
sources:
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — 5 red flags
    last_modified: 2026-08-17
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — les 5 red flags (l. 67-79)
    last_modified: 2026-08-19
  - id: red-flag-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Règle de résolution — 1 red flag = arrêt dur (l. 84-103)
    last_modified: 2026-08-19
  - id: batman-couplage-ops-it
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-ops-it.md"
    title: Batman — couplage Ops↔IT via Cyborg
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash Product — red flag #1

## Le canon verbatim

La matrice d'harmonisation pose 5 red flags (cf. `business-wheel-harmonization-matrix.md` §« Les 5 red flags »). Le red flag #1 est **verbatim** :

> *« Product green, Ops/IT red — ne pas lancer. Le produit ne peut pas
> être livré ou maintenu. »*

La forme exploitable (cf. `b2-harmonization-matrix-exploitable.md` §« Les 5 red flags ») ajoute la précision opérationnelle :

> *« Combinatoire simple : un red flag suffit pour bloquer, même si les
> 8 domaines sont au vert sur le radar. C'est l'inverse du radar — il
> suffit d'un en-bas pour invalider le 8-en-haut. »*

Le red flag #1 est un **arrêt dur**. Il ne déclenche pas une négociation Council — il **bloque le lancement** jusqu'à résolution.

## Pourquoi ce red flag est asymétrique

Les 5 red flags ont des asymétries :

| # | Red flag | Asymétrie |
|---|---|---|
| 1 | Product green, Ops/IT red | Bloque un launch |
| 2 | Growth green, Sales red | Demande validation avant scale |
| 3 | Sales green, Ops/People red | Risque de charge (pas arrêt dur) |
| 4 | Finance red + Growth/Product green | Demande ralentissement ou repricing |
| 5 | Legal red + public-facing work | Gèle les claims et le launch |

Le red flag #1 est le **seul arrêt dur lié à Product**. Les autres sont liés à Growth (red flag #2), Sales (red flag #3), Finance (red flag #4), Legal (red flag #5). C'est cohérent avec le rôle de Product comme **portail de lancement** : si le produit est prêt mais le run ne suit pas, le lancement explose en rétention.

## Trois cas de déclenchement légitimes

### Cas 1 — Support Ops insuffisant (Batman red)

Le pair-check Product → Ops (#3) détecte que Batman refuse de maintenir l'artefact. Le motif est documenté dans le packet mésoperpétuel (cf. `flash-pair-checks-dependencies.md` §« Pair-check #3 »).

**Exemple** : Flash livre un artefact avec une logique de scoring algorithmique. Batman refuse de le maintenir en run parce que la complexité dépasse la SOP support standard. **Red flag #1 déclenché**.

**Action** : le lancement est suspendu jusqu'à résolution du pair-check (Flash enrichit le runbook, Batman absorbe la complexité, ou scope réduit).

### Cas 2 — Monitoring IT manquant (Cyborg red)

Le pair-check Product → IT (#4) détecte que Cyborg refuse de déployer l'artefact. Le motif est documenté dans le packet mésoperpétuel (cf. `flash-pair-checks-dependencies.md` §« Pair-check #4 »).

**Exemple** : Flash produit une feature qui dépend d'une librairie open-source vulnérable. Cyborg refuse de la redéployer tant que le refactor n'est pas fait. **Red flag #1 déclenché**.

**Action** : le lancement est suspendu jusqu'à résolution du pair-check (Flash refactore, Flash retire la feature, ou Cyborg absorbe le risque).

### Cas 3 — Runbook absent

L'artefact est supportable théoriquement, mais aucun runbook n'a été produit. Sans runbook, Batman et Cyborg ne peuvent pas maintenir ni déployer. C'est un cas dérivé des cas 1 et 2, mais avec une cause spécifique : **absence de documentation**.

**Exemple** : Flash livre un artefact dont seul CaptainAmerica comprend la logique interne. Sans documentation, la squad Fantastic Four ne peut pas supporter. **Red flag #1 déclenché**.

**Action** : Flash consigne le DoD *« runbook produit avant launch »* dans le packet mésoperpétuel, et le launch est suspendu jusqu'à production du runbook.

## Trois cas où le red flag est abusif

### Cas abusif 1 — Ops/IT rouges sur des critères non-pertinents

Batman ou Cyborg oppose un refus sur un critère **non-pertinent pour l'artefact**. Par exemple : Batman refuse un artefact parce que la squad Fantastic Four n'a pas la **certification ISO 27001** (utile pour des données bancaires, non-pertinent pour un artefact de coaching).

**Distinction canonique** : le red flag #1 porte sur la **capacité opérationnelle** (savoir maintenir), pas sur la **certification** (savoir attester). Si Batman oppose un refus non-pertinent, le B2 Council doit passer outre le refus et statuer sur le fond.

### Cas abusif 2 — Reds flags temporaires < 7 jours

Batman ou Cyborg oppose un refus **temporaire** (incident en cours, manque de slot Paperclip — cf. `b2-failsafe-paperclip-recovery.md` §« Le cas Spécial — plafond Paperclip »). Le refus sera levé dans la semaine.

**Distinction canonique** : le red flag #1 porte sur un **état structurel** (la squad ne sait pas maintenir), pas sur un **état transitoire** (la squad ne peut pas maintenir cette semaine). Si le refus est transitoire, le lancement peut être **reporté**, pas **annulé**.

### Cas abusif 3 — Refus sans motif documenté

Batman ou Cyborg oppose un refus sans **motif vérifiable** (cf. `b2-eight-domain-vetoes-catalogue.md` §« Propriété 2 — Vérifiable »). Le motif doit être écrit dans le packet mésoperpétuel.

**Distinction canonique** : un refus sans motif est un **veto invalide**. Le B2 Council passe outre (propriété 4 du veto catalogue).

## La procédure de résolution — quand le red flag #1 se déclenche

### Étape 1 — Détection

Le red flag #1 est détecté par l'un des 4 mécanismes :
- **Pair-check #3** (Product → Ops) qui échoue
- **Pair-check #4** (Product → IT) qui échoue
- **Scan red flag hebdomadaire** pendant le cycle de build actif (cf. `b2-harmonization-matrix-exploitable.md` §« Le seuil déclencheur »)
- **Signal Batman/Cyborg** qui notifie l'impossibilité de lancer

### Étape 2 — Documentation

Le packet mésoperpétuel est créé avec :
```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B2-PEER-YYYY-NN  # pair-check échoué
mode: handoff | negotiation
impacted_domains:
  - product
  - ops
  - it
tradeoff: <le conflit entre valeur d'artefact et capacité opérationnelle>
decision: blocked  # arrêt dur
proof_expected:
  - runbook produit (si cas 3)
  - pair-check #3 ou #4 ré-évalué (si cas 1 ou 2)
next_review: <date de résolution prévue>
```

### Étape 3 — Communication aux porteurs

Les porteurs B1, B2 Sales, B3 Avengers sont notifiés. Le **lancement est suspendu** — pas un report, une suspension. Aucune nouvelle acquisition client n'est lancée tant que le red flag tient.

### Étape 4 — Issue

Quatre issues possibles :

1. **Pair-check résolu** (Flash amende l'artefact, Batman absorbe la complexité, ou scope réduit) → red flag levé, lancement autorisé
2. **Escalade B2 Council** (négociation entre Batman et Flash) → packet mésoperpétuel avec `mode: negotiation`, decision possible `accepted` avec conditions
3. **Escalade B1** (B2 Council ne peut pas préserver la wheel 8-domain — cf. `b2-council-arbitrage-rule.md` §« Quand le Council escalade à B1 ») → `decision: escalate_to_B1`
4. **Lancement annulé** (B1 confirme que le red flag tient et le lancement n'est pas viable) → l'artefact est **recyclé** en MVP interne, pas commercialisé

## Le couplage Ops ↔ IT (Batman ↔ Cyborg)

Le red flag #1 a une propriété particulière : il implique **deux domaines en aval** (Ops ET IT). Les autres red flags impliquent un seul domaine en conflit.

**Conséquence opérationnelle** : un arbitrage sur le red flag #1 doit traiter **deux pair-checks en parallèle** (#3 Product → Ops et #4 Product → IT). Batman et Cyborg peuvent être en désaccord — Flash est en amont (C) sur les deux pair-checks, mais **le Council arbitre en bloc**.

Le triplet Batman-Cyborg (cf. `batman-couplage-ops-it.md`) pose la chaîne implicite `Product → IT → Ops` : IT déploie, Ops maintient. Si Cyborg refuse de déployer, Batman ne peut pas maintenir. Si Batman refuse de maintenir, Cyborg refuse de déployer (parce que le déploiement sert à maintenir). **Les deux refus sont couplés**.

Le B2 Council peut choisir de **débloquer l'un avant l'autre** (IT d'abord, Ops ensuite), mais le red flag tient tant que les deux ne sont pas au vert.

## Pourquoi ce red flag est non-négociable

Le red flag #1 est **non-négociable au niveau mésoperpétuel** : aucun capitaine B2 ne peut passer outre sans escalader B1. C'est la même règle que les vetos catalogue (cf. `b2-eight-domain-vetoes-catalogue.md` §« Propriété 3 »).

Trois raisons :

1. **L'enzyme de rétention.** Un produit lancé sans support Ops/IT voit sa rétention chuter. La rétention perdue ne se récupère pas (cf. pratique documentée — non citée).
2. **Le coût de retour.** Reprendre un produit lancé sans support coûte 5-10× plus cher que suspendre le lancement (correction post-mortem vs pré-mortem).
3. **L'effet sur les autres domaines.** Un produit qui explose en rétention impacte **tout** : Sales (réclamations), Growth (bad buzz), Finance (coût de support), Legal (risque de litige). Le red flag #1 est un **protecteur systémique**.

## Anti-pièges

- **Red flag détecté mais non documenté.** Un refus Batman/Cyborg qui n'est pas consigné dans un packet mésoperpétuel n'a pas de force de red flag. Le B2 Council doit exiger la documentation avant de bloquer le lancement.
- **Lancement lancé malgré le red flag.** Un captain B2 ou B3 qui lance le produit sans attendre la levée du red flag engage sa responsabilité disciplinaire. Le packet mésoperpétuel post-launch doit documenter l'exception.
- **Red flag confondu avec un veto.** Le red flag est un **arrêt technique** (le lancement n'est pas viable). Le veto est un **blocage catégoriel** (l'offre ne doit pas exister). Les deux peuvent coexister (un produit peut être veto par Flash ET red flag #1 par Batman), mais ils sont **distincts**.
- **Red flag #1 utilisé comme levier commercial.** Batman ou Cyborg qui oppose un refus pour des raisons non-pertinentes (cf. cas abusif 1) utilise le red flag comme outil politique. Le B2 Council doit distinguer le refus légitime du levier commercial.

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 critères + 5 red flags
- [[b2-council-arbitrage-rule]] — qui tient le Council et arbitre les red flags
- [[b2-meso-decision-packet-spec]] — le format des packets de blocage
- [[flash-pair-checks-dependencies]] — les pair-checks #3 et #4 qui déclenchent le red flag
- [[flash-domain-perimeter]] — les frontières Ops et IT
- [[batman-couplage-ops-it]] — le couplage Ops ↔ IT qui rend le red flag non-trivial
- [[eight-domain-avengers-wheel]] — le mapping Flash/Avengers

## Note de confiance

**Confirmé par machine, à moitié étayé.** Le red flag #1 (verbatim) et sa règle d'arrêt dur sont tirés de la matrice d'harmonisation canonique. Les 3 cas de déclenchement légitimes sont **projetés** à partir de la matrice + la pratique observée (support Ops, monitoring IT, runbook absent) — pas explicitement documentés comme cas canoniques. Les 3 cas abusifs sont **reconstruits** à partir de la doctrine Batman (remonter les faits, pas les décisions — triplets 56-57) et de la propriété *vérifiable* du veto catalogue. La procédure de résolution en 4 étapes est **empruntée** au format mésoperpétuel canonique (cf. `b2-meso-decision-packet-spec.md`). Le couplage Ops ↔ IT est **projeté** à partir de `batman-couplage-ops-it.md` — pas une chaîne explicitement posée ailleurs dans le corpus.
