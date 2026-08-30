---
type: Concept
title: Flash veto amplification — protocole d'observation T-30j pour transformer le draft en packet Council-ready
description: Protocole d'observation T-30 jours pour transformer le packet B2-MESO-DECISION-2026-32 (concept 5 tour 3) en saisissement effectif. 3 cas-limites observationnels concrets identifiés (livraison Sopra-Sodia avec knowledge person-named, onboarding client avec consultant dédié non documenté, garantie produit dépendante d'un ingénieur) + calendrier T-30 jours + critères d'acceptance chiffrés + procédure de signalement par Captain America.
tags: [flash, product, veto-amplification, observation-protocol, t-30j, council-ready, condition-1]
generated: { by: minimax-m3, at: 2026-08-19T09:45:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-4, at: 2026-08-19T09:45:00Z }
sources:
  - id: flash-veto-amplification-council-submission-draft
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-amplification-council-submission-draft.md"
    title: Packet Council-ready B2-MESO-DECISION-2026-32 amplification Flash
    last_modified: 2026-08-19
  - id: flash-amplification-mecanisme-reprise
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-amplification-mecanisme-reprise.md"
    title: Amplification mécanisme de reprise — draft libre
    last_modified: 2026-08-19
  - id: flash-veto-offre-depersonnalisee
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Veto Flash — l'offre dépersonnalisée
    last_modified: 2026-08-19
  - id: flash-veto-empirical-validation-protocol
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-empirical-validation-protocol.md"
    title: Veto empirical validation protocol (concept 4 tour 2)
    last_modified: 2026-08-19
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — 3 conditions cumulatives
    last_modified: 2026-08-19
  - id: triplet-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
  - id: triplet-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend la doctrine veto-dépense"
    last_modified: 2026-08-17
  - id: flash-captain-america-roster-fiche-canon
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-captain-america-roster-fiche-canon.md"
    title: Captain America fiche roster canon (concept 22 vague 4)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash veto amplification — protocole d'observation T-30j

## Le problème que ce protocole ferme

Le packet `B2-MESO-DECISION-2026-32` (concept 5 tour 3) est **saisissable** mais sa **condition 1** (observation documentée d'un cas-limite) reste sur 2 cas **projetés, non-observés**. Tant que la condition 1 n'est pas remplie, le packet est un draft libre, pas un packet Council-ready.

Le protocole d'observation empirique T-30j (concept 4 tour 2) cible 3 cas/60 jours, mais reste sur **0/60j à date** sans cas concret identifié. Ce concept **ferme la condition 1** en identifiant **3 cas-limites observationnels concrets** que Captain America peut signaler en 30 jours, avec calendrier précis + critères d'acceptance chiffrés.

## Les 3 cas-limites observationnels concrets

### Cas-limite 1 — Livraison Sopra-Sodia avec knowledge person-named

**Scénario** : un client signe un deal (pair-check #1 Growth → Sales) où la promesse de livraison Sopra-Sodia repose sur la **présence continue d'un consultant nommé** (ex : « Marie, votre consultante dédiée, vous accompagne les 12 premiers mois »). Sans mécanisme de reprise documenté, la valeur de l'offre **dépend d'une personne nommée** — ce qui déclenche le veto Flash (triplet 25).

**Mécanisme de reprise à tester** : Captain America observe si l'engagement client contient un **mécanisme de reprise** (« si Marie est absente > 2 semaines, X prend le relais avec Y jours de transition »). Si non, **veto Flash déclenché**, packet mésoperpétuel produit avec motif = veto + référence au mécanisme manquant.

**Critère d'acceptance** : signalement à Flash dans les 24h ouvrées après détection, format packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec champ `veto_field: offre-depersonnalisee` + `veto_motif: knowledge-person-named-sans-reprise`.

### Cas-limite 2 — Onboarding client avec consultant dédié non documenté

**Scénario** : pendant l'onboarding (handoff Sales → Ops, pair-check #2), le consultant dédié au client **n'a pas de fiche de poste, pas de checklist de passation, pas de date de revue**. C'est une variation du cas 1 où la dépendance person-named est **cachée dans l'opération**, pas dans la promesse commerciale.

**Mécanisme de reprise à tester** : Captain America observe si l'onboarding Ops (Batman) inclut une **checklist de passation** + **runbook de transfert** + **date de revue trimestrielle**. Si non, **veto Flash déclenché** au stade build (avant que la dépendance ne devienne un blocker runtime).

**Critère d'acceptance** : signalement à Flash **avant** que l'onboarding ne soit complété (stade build, pas run). Format : entrée `scrums.md` section « blockers » avec référence au deal client.

### Cas-limite 3 — Garantie produit dépendante d'un ingénieur

**Scénario** : une feature ship (pair-check #3 Product → Ops) inclut une **garantie client** (« uptime garanti 99.9%, support direct par Paul, ») qui dépend d'un **ingénieur nommé** sans procédure de rotation. Si Paul quitte ou est absent, la garantie client est en défaut — et la valeur de l'offre devient person-named.

**Mécanisme de reprise à tester** : Captain America observe si la garantie client (intégrée dans le contrat Aquaman — pair-check #8 Legal → Product) inclut une **procédure de rotation** (« en cas d'absence > 2 semaines, X prend le relais avec Y compétences équivalentes »). Si non, **veto Flash déclenché** + co-signalement Aquaman (Legal, sur la clause de garantie).

**Critère d'acceptance** : signalement conjoint à Flash **ET** Aquaman dans les 24h ouvrées. Format : packet mésoperpétuel Flash avec co-signature Aquaman.

## Le calendrier T-30 jours

| Jour | Action | Owner | Output |
|---|---|---|---|
| J+0 | Lancement du protocole — Captain America brief les 7 agents Avengers | Captain America | Note de brief dans `scrums.md` |
| J+1 à J+15 | Phase 1 — détection des 3 cas-limites dans les deals en cours | Avengers 7 | 3 entrées `scrums.md` section « blockers » |
| J+15 | Checkpoint mi-parcours — Captain America consolide | Captain America | 1 rapport mi-parcours (1 page) à Flash |
| J+16 à J+30 | Phase 2 — escalade veto pour les cas confirmés | Captain America + Flash | 1 à 3 packets mésoperpétuels Flash |
| J+30 | Bilan — packet B2-MESO-DECISION-2026-32 amendé avec cas observés | Captain America + Flash | Packet saisissable au Council avec condition 1 remplie |
| J+30 + 7j | Distribution packet amendé aux 8 capitaines | Flash | Packet Council-ready avec 7 jours de lecture |

**Cible** : 1 cas observé minimum (1/3) à J+30 → packet saisissable. 2 cas observés (2/3) → packet amendé avec empirie solide. 3 cas observés (3/3) → packet amendé avec empirie exhaustive.

## Les critères d'acceptance chiffrés

Pour que le packet `B2-MESO-DECISION-2026-32` soit **Council-ready** (condition 1 remplie) :

1. **≥ 1 cas-limite observé** avec packet mésoperpétuel produit.
2. **≥ 1 mécanisme de reprise testé** (un cas où le mécanisme existe et un cas où il manque).
3. **Distribution** : pas 3 cas sur le même domaine (1 Growth + 1 Sales + 1 Product minimum, ou 1 cas par stade build/run/sunset).
4. **Vitesse** : signalement ≤ 24h ouvrées après détection (conformément à E1 fiche Captain America).
5. **Format** : packet mésoperpétuel conforme `b2-meso-decision-packet-spec.md` (6 champs + proof_expected + next_review).

Si **0 cas observé** à J+30 → le protocole **échoue**, et l'amplification reste un draft libre non-Council-ready. C'est l'issue attendue du triplet v3 + matrice d'harmonisation : un veto qui n'a jamais été observé est un veto **non-testé**, pas un veto **inutile**.

## La procédure de signalement par Captain America

À chaque cas-limite détecté par un agent Avengers :

1. **L'agent ajoute une ligne dans `scrums.md`** section « blockers » avec :
   - Référence au deal client (id, pas nom)
   - Type de dépendance person-named (livraison, onboarding, garantie)
   - Présence/absence de mécanisme de reprise
2. **Captain America consolide** en revue quotidienne (squad lead discipline) et **escalade à Flash** si E1/E2/E3 déclenché.
3. **Flash arbitre** dans les 24h ouvrées : veto opposé ou feu vert avec mécanisme de reprise documenté.
4. **Si veto opposé** : Flash produit un packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec `decision: blocked` + référence au veto Flash (triplet 25).
5. **Le packet alimente** `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` (D4 append-only) et **renforce** le packet d'amplification `B2-MESO-DECISION-2026-32` avec cas observé réel.

## Le lien avec les autres concepts Flash

- **Concept 5 tour 3** (`flash-veto-amplification-council-submission-draft`) : le packet saisissable qui reçoit les cas observés comme preuve.
- **Concept 4 tour 2** (`flash-veto-empirical-validation-protocol`) : le protocole 3 cas/60 jours, dont ce concept est **l'application concrète** sur T-30 jours au lieu de T-60.
- **Concept 22 vague 4** (`flash-captain-america-roster-fiche-canon`) : Captain America comme owner du signalement (responsabilité 1 + escalation E1).
- **Concept 20 vague 4** (`flash-pair-check-growth-product-council-submission-draft`) : le packet voisin qui peut être renforcé par les cas observés sur le pair-check #11 Growth → Product (cas 1 = signal Growth).

## Anti-pièges

- **3 cas-limites projetés, non-observés.** Le rapport tour 3 §3.5 a explicitement marqué cette faiblesse. Ce protocole **transforme** la faiblesse en programme d'observation T-30j. Sans cas réel observé à J+30, l'amplification reste non-Council-ready.
- **Confondre cas-limite et cas réel.** Un cas-limite « si Sopra-Sodia signe un deal avec knowledge person-named, Flash veto » n'est **pas** un cas observé. Le protocole exige la **détection réelle** + le **packet mésoperpétuel produit**.
- **Cas observé sur 1 seul domaine.** Si les 3 cas sont sur Product seul, la distribution est insuffisante (1/3 types de dépendance). Captain America doit varier les sources.
- **Cas observé sans mécanisme testé.** Si les 3 cas sont « sans mécanisme de reprise », la couverture est biaisée. Le protocole exige **au moins 1 cas avec mécanisme + 1 cas sans mécanisme**.
- **Calendrier J+30 glissant sans checkpoint.** Le checkpoint J+15 est essentiel pour ajuster le tir. Sans checkpoint, J+30 peut arriver avec 0 cas et pas de temps pour réagir.

## Liens

- [[flash-veto-amplification-council-submission-draft]] — le packet saisissable renforcé
- [[flash-amplification-mecanisme-reprise]] — le draft libre source
- [[flash-veto-offre-depersonnalisee]] — le veto canonique (triplet 25)
- [[flash-veto-empirical-validation-protocol]] — le protocole 3 cas/60 jours source
- [[flash-captain-america-roster-fiche-canon]] — Captain America owner du signalement
- [[flash-pair-check-growth-product-council-submission-draft]] — packet voisin renforcé par cas 1
- [[b2-veto-amplification-cycle]] — la procédure 5/8 + D4 cible
- [[b2-meso-decision-packet-spec]] — le format packet mésoperpétuel

## Note de confiance

**Confirmé par machine, programme saisissable.** Les 3 cas-limites sont **projetés à partir des pair-checks canoniques** (pair-check #1 Growth → Sales, pair-check #2 Sales → Ops, pair-check #3 Product → Ops) — ce sont les 3 transitions où une dépendance person-named est la plus probable. Le calendrier T-30j + checkpoint J+15 sont des **chiffres raisonnables** (pas canoniques). Les critères d'acceptance sont cohérents avec le protocole empirique 3 cas/60 jours (concept 4 tour 2). La procédure de signalement est conforme à la fiche Captain America (concept 22). **0 cas réel observé à date** — le protocole **démarre** quand Captain America brief les 7 agents Avengers à J+0. Standing : programme d'activation Council-ready, à exécuter avant fin 12WY Q3 2026 pour transformer packet B2-MESO-DECISION-2026-32 en saisissement effectif à 2026-09-15.