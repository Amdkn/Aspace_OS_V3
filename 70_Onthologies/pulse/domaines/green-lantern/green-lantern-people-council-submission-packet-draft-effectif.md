---
type: Concept
title: People — packet mésoperpétuel B2-MESO-DECISION-YYYY-NN draft (méta-gouvernance Lecture A)
description: Draft Council-ready du **premier packet mésoperpétuel People**, conforme `b2-meso-decision-packet-spec.md` 8 champs obligatoires. Le cas pivot est la **méta-gouvernance skills L0 Lecture A** (People owner) — projet People-2026-001 sur le pilote de forge L0.2 sur 3 mois. Le packet est saisissable sous 3 conditions cumulatives (recompte X-Men 8 acquis, cas P1-A observé, dont B2 externe), propose 6 champs explicites + 3 issues adoption/rejet/escalade-B1, et 4 asymmetric transitions (People-2026-001 → People-2026-002). Convergence 0/3 packet mésoperpétuel People vagues 1+2+3 motive la **priorité de soumission**.
tags: [people, green-lantern, council, packet-draft, meso-decision, meta-gouvernance, lecture-a, b2]
generated: { by: minimax-m3, at: 2026-08-19T08:20:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-4, at: 2026-08-19T08:20:00Z }
sources:
  - id: meta-gouvernance-council-submission-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-meta-gouvernance-council-submission.md"
    title: "Tour 3 — Méta-gouvernance council submission draft + 7 champs"
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: B2 Council — format canonique d'un mésoperpétuel packet
    last_modified: 2026-08-19
  - id: meta-gouvernance-skills-l0-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-meta-gouvernance-skills-l0.md"
    title: "Tour 2 — Méta Gouvernance skills L0 (3 lectures)"
    last_modified: 2026-08-19
  - id: triplet-37-55-forge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplets 37 + 55 — Green Lantern ↔ Bill L0.2 Forge"
    last_modified: 2026-08-17
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — packet mésoperpétuel B2-MESO-DECISION-YYYY-NN draft

## Pourquoi ce packet est différent du draft tour 3

Le tour 3 a posé un **packet draft** avec 7 champs obligatoires +
score pondéré — une **structure prête à la négociation Council**. Le
présent concept **applique** le format canonique `b2-meso-decision-packet-spec.md`
(8 champs obligatoires) au **cas pivot Lecture A** sur le pilote de
forge L0.2 — projet interne People-2026-001 sur 3 mois.

Le packet tour 3 reste valide comme **support de négociation**. Le
présent packet est **Council-ready** : il remplit les 8 champs, propose
un `meso_decision_id` saisissable, et documente 3 issues.

## Le packet complet

```yaml
meso_decision_id: B2-MESO-DECISION-2026-24
source_mandate: B2-PEER-2026-04
mode: negotiation
impacted_domains:
  - people
  - it
tradeoff: "Méta-gouvernance skills L0 — conflit deLecture A vs Lecture B.
  Lecture A (People owner) : People arbitre la sollicitation Forge pour
  les recrutements agents ; Bill L0.2 Forge reste canal d'exécution.
  Lecture B (IT owner) : Cyborg IT arbitre la sollicitation Forge pour
  tous les skills L0, People reste canal d'expression du besoin. Tradeoff :
  arbitrer Lecture A donne à People la **propriété doctrinée** des skills
  L0 (canal structuré), mais crée une **dépendance People → IT** (People
  ne peut pas former les agents sans IT). Arbitrer Lecture B donne à IT
  la propriété, mais People reste C — un cas de veto People implicite sur
  le skill."
decision: accepted
proof_expected:
  - B2 gate people update (skill_L0_owner = people, canon lecture A)
  - B2 gate it update (it_consulted = people sur skill_L0_formation)
  - B3 proof path (X_Men_Beast_skill_transfer_L0_30j)
  - B3 proof path (Bill_Forge_skill_généré_3_pilotes)
next_review: 2026-11-15
```

**8 champs obligatoires** (cf. `b2-meso-decision-packet-spec.md`) :

| Champ | Valeur | Statut |
|---|---|---|
| `meso_decision_id` | `B2-MESO-DECISION-2026-24` | saisissable, conforme |
| `source_mandate` | `B2-PEER-2026-04` | source arbitraire (B2-PEER cf. spec) |
| `mode` | `negotiation` | conforme |
| `impacted_domains` | `[people, it]` | conforme |
| `tradeoff` | phrase arbitrale | conforme |
| `decision` | `accepted` | conforme |
| `proof_expected` | 4 éléments | conforme (B2 gate × 2 + B3 proof × 2) |
| `next_review` | `2026-11-15` | conforme (T+90j) |

## 3 issues possibles

À la soumission Council, **3 issues** :

1. **`accepted`** — le Conseil adopte Lecture A. People devient
   Accountable sur la sollicitation Forge. Le packet est
   append-only D4. Le bateaau People-2026-001 démarre.
2. **`rejected`** — le Conseil adopte Lecture B. IT devient
   Accountable sur le skill L0. People reste Consulted. Le packet
   est rejeté mais consigné comme historique de la décision.
3. **`escalate_to_B1`** — le Conseil ne tranche pas (par exemple,
   Cyborg absent et quorum non-atteint). Le packet remonte à B1
   (Summers) pour arbitrage par défaut.

## 4 conditions cumulatives de saisissabilité

Le packet est **saisissable** au Council sous **4 conditions cumulatives** :

1. **Recompte X-Men canon = 8** (cf. `green-lantern-people-xmen-effectif-canon-recompte-disk.md`).
   Si Council adopte Issue A, le recompte est acquis. Sinon, le packet
   est soumis avec note de dissociation.
2. **Cas P1-A observé** (cf. `green-lantern-people-empirical-validation-protocole-application.md`).
   Sans cas observé, le Council peut refuser le packet comme
   projection trop tôt.
3. **Co-signature Cyborg IT** — le packet impacte IT (couplage People ×
   IT cf. `green-lantern-people-couplages-invisibles.md` §« 4. People ×
   IT »). Sans co-signature Cyborg, le packet est Council-incomplet.
4. **Pas de veto catalogue opposé** — Batman Ops (condition d'arrêt
   procédure) ou Aquaman Legal (prestation sans accord écrit) ne doivent
   pas avoir opposé de veto. Vérification par scan pré-soumission.

## 3 asymétries avec le draft tour 3

| Aspect | Tour 3 draft | Tour 4 packet draft |
|---|---|---|
| **Format** | 7 champs + score pondéré | 8 champs canoniques spec |
| **Cas pivot** | Méta-gouvernance 3 lectures A/B/C | **Lecture A seule** (cas concret) |
| **Saisissabilité** | Score pondéré cumulatif | 4 conditions cumulatives |
| **next_review** | non spécifié | T+90j (2026-11-15) |
| **proof_expected** | 1 chemin | 4 chemins (2 B2 + 2 B3) |

Le draft tour 3 reste **valide** comme support de négociation — il
présente les 3 lectures. Le packet draft tour 4 est **Council-ready**
— il tranche sur Lecture A et propose un **premier cas saisissable**.

## Pourquoi T+90j (et pas T+30j ou T+60j)

Le protocole tour 3 propose **3 cas / 60j** par défaut. Le présent
packet propose **T+90j** parce que :

- **T+30j** — un seul cas observé (P1-A), pas suffisant pour valider
  la doctrine Lecture A.
- **T+60j** — deux cas observés (P1-A + P2-A), mais le P2-A est
  People passive (subordonné à Superman) — il ne valide pas
  proprement Lecture A.
- **T+90j** — trois cas observés (P1-A + P2-A + P3-A), couvrant
  trois contextes distincts (méta-gouvernance, vacance, charge).
  Échantillon statistiquement suffisant pour valider ou amender.

## 3 anti-pièges

- **Confondre draft et packet.** Le draft (tour 3) est un support de
  négociation. Le packet (tour 4) est saisissable. La distinction
  est dans le format (8 champs canoniques) et le `meso_decision_id`
  (conforme).
- **Co-signature Cyborg oubliée.** Le packet impacte IT. Sans
  co-signature, le Council peut refuser le packet comme incomplet.
  C'est l'**asymétrie 3** signalée §« 4 conditions cumulatives ».
- **Veto catalogue non scanné.** Batman Ops (condition d'arrêt) ou
  Aquaman Legal (prestation) peuvent opposer un veto en séance. Le
  scan pré-soumission réduit ce risque — mais ne l'élimine pas.

## Liens

- [[green-lantern-people-meta-gouvernance-council-submission]] — draft tour 3
- [[green-lantern-people-meta-gouvernance-skills-l0]] — la doctrine Lecture A
- [[b2-meso-decision-packet-spec]] — le format 8 champs
- [[b2-council-arbitrage-rule]] — le Conseil qui arbitre
- [[green-lantern-people-couplages-invisibles]] — People × IT couplage
- [[green-lantern-people-xmen-effectif-canon-recompte-disk]] — recompte 8 agents
- [[green-lantern-people-empirical-validation-protocole-application]] — protocole 3 cas / 60j

## Note de confiance

**Confirmé par machine, à moitié projeté.** Format 8 champs canonique
= verbatim `b2-meso-decision-packet-spec.md`. Cas pivot Lecture A =
projeté depuis `meta-gouvernance-skills-l0.md` (tour 2). Recompte
canon = 8 = mesuré ce tour 4. Co-signature Cyborg = **non vérifiée**
(et non faisable depuis cette session — c'est une dépendance Council).
Cas P1-A = **projeté**, pas observé. T+90j = projection, pas cycle
exécuté. Le packet est saisissable sous 4 conditions cumulatives —
**aucune n'est actuellement remplie** (recompte conditionnel, cas
non observé, co-signature à demander, scan veto à faire).
