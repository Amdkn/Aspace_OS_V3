---
type: Concept
title: Cyborg — extension des gates IT à 4 états (SYSTEM_READY / NEEDS_SYSTEM_OWNER / QUARANTINE / DORMANT) symétrique Superman 8-domain NEEDS_SIGNAL
description: Les gates IT canoniques sont 3 états (SYSTEM_READY / NEEDS_SYSTEM_OWNER / QUARANTINE, cf. eight-domain-avengers-wheel.md). Superman tour 3 (superman-needs-signal-vs-dormant-8domain-doctrine) a étendu NEEDS_SIGNAL/DORMANT aux 8 domaines. Par symétrie, ce concept pose le 4e état DORMANT pour les gates IT : une infrastructure Kang Dynasty peut être en dormance (3 conditions d'entrée) sans bloquer la wheel 8-domain. La doctrine ferme le trou canonique *« infrastructure dormante vs Shadow Active ? »* identifié au tour 2.
tags: [cyborg, gates, system-ready, needs-system-owner, quarantine, dormant, 4-etats, symetrie-superman]
generated: { by: minimax-m3, at: 2026-08-19T05:50:00Z }
verified:
  - { by: process:lecture-bcorpus-cyborg-tour-3, at: 2026-08-19T05:50:00Z }
sources:
  - id: superman-needs-signal-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-needs-signal-vs-dormant-8domain-doctrine.md"
    title: Superman tour 3 — extension 4 états READY/NEEDS_SIGNAL/BLOCKED/DORMANT aux 8 domaines
    last_modified: 2026-08-19
  - id: eight-domain-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — gates IT canoniques 3 états
    last_modified: 2026-08-17
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: Doctrine dormance B2 Areas — 3 conditions entrée + 3 déclencheurs réveil
    last_modified: 2026-08-19
  - id: cyborg-cycle-vie
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-cycle-vie-infrastructure-5-phases.md"
    title: Cyborg cycle de vie infrastructure 5 phases — dormance entre Phase 3 (Run) et Phase 5 (Reverse)
    last_modified: 2026-08-19
  - id: cyborg-dans-aaas
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-dans-aaas-3-variants.md"
    title: Cyborg dans AaaS — Family/Home 4e variant dormant Q3 2026
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — extension des gates IT à 4 états

## Le trou canon observé

Les gates IT canoniques (cf. `eight-domain-avengers-wheel.md` §« Le
mapping canonique ») sont **3 états** :

- `SYSTEM_READY` — système opérationnel.
- `NEEDS_SYSTEM_OWNER` — système需要一个 owner (équivalent People).
- `QUARANTINE` — système en quarantaine (incident ou veto actif).

Superman tour 3 (`superman-needs-signal-vs-dormant-8domain-
doctrine`) a posé l'extension 4 états pour **tous les domaines B2** :

| État | Définition |
|---|---|
| `READY` | domaine opérationnel, prêt à dispatcher |
| `NEEDS_SIGNAL` | domaine en attente d'un signal amont |
| `BLOCKED` | domaine bloqué (red flag ou veto) |
| `DORMANT` | domaine en dormance (3 conditions cumulatives) |

Par symétrie, ce concept étend les gates IT à 4 états
correspondants, avec une définition **propre à IT** :

| État IT | Définition | Équivalent Superman |
|---|---|---|
| `SYSTEM_READY` | infra opérationnelle, prête à servir | `READY` |
| `NEEDS_SYSTEM_OWNER` | infra需要一个 owner (charge Kang >80% sans backup, ou recrutement 7e agent) | `NEEDS_SIGNAL` |
| `QUARANTINE` | infra en quarantaine (incident P0, ou veto Cyborg actif) | `BLOCKED` |
| `DORMANT` | infra en dormance (usage <20% pendant ≥3 sprints consécutifs) | `DORMANT` |

## Les 3 conditions cumulatives d'entrée en DORMANT

`b2-areas-dormants-doctrine.md` pose **3 conditions cumulatives**
d'entrée en dormance pour les domaines B2 Areas. Par symétrie IT,
les 3 conditions d'entrée en DORMANT pour une infrastructure
Kang Dynasty sont :

### Condition 1 — Usage inférieur au seuil

**Usage <20% de la capacité** pendant ≥3 sprints consécutifs.

**Mesure** : Rama-Tut (Backup / Monitoring) mesure l'usage via
P18 Observability. Si l'usage reste <20% pendant 3 sprints
consécutifs, condition 1 tenue.

**Cas typique** : un service legacy non-migré, un backup
multi-AaaS non-utilisé, un environnement de staging obsolète.

### Condition 2 — Pas de dépendance aval critique

Aucune dépendance aval critique (pas de red flag #1 latent).

**Mesure** : Cyborg vérifie qu'aucune autre infrastructure ou
service ne dépend de l'infrastructure candidate à DORMANT.

**Cas typique** : un environnement de staging non-utilisé par
le pipeline CI/CD depuis ≥1 sprint, un service de pré-prod
isolé du runbook Ops.

### Condition 3 — Décision Council d'entrer en dormance

Le B2 Council (ou Cyborg + Batman conjointement, mode handoff)
tranche l'entrée en DORMANT. La décision est consignée par
packet mésoperpétuel type `B2-MESO-DECISION-YYYY-NN` avec
`mode: handoff`, `impacted_domains: [it]`, `decision: accepted`.

**Note** : pour une infrastructure **dormante par construction**
(ex : un variant AaaS non-activé), la décision Council peut
être *a posteriori* (la dormance précède la décision).

## Les 3 déclencheurs de réveil (sortie de DORMANT)

`b2-areas-dormants-doctrine.md` pose **3 déclencheurs de réveil**.
Par symétrie IT :

### Déclencheur 1 — Usage en hausse

L'usage dépasse **60% de la capacité** pendant ≥1 sprint, OU
revient au niveau nominal par décision d'architecture (ex :
migration d'un service vers cette infrastructure).

### Déclencheur 2 — Dépendance aval activée

Une autre infrastructure ou service dépend à nouveau de
l'infrastructure candidate. Le red flag #1 latent disparaît.

### Déclencheur 3 — Décision Council de réveil

Le B2 Council tranche le réveil par packet mésoperpétuel type
avec `decision: accepted`. La transition DORMANT → SYSTEM_READY
passe par la **Phase 2 (Deploy) rejouée** du cycle de vie IT
(cf. [[cyborg-cycle-vie-infrastructure-5-phases]]).

## Le cas AaaS — Family/Home 4e variant dormant

`cyborg-dans-aaas-3-variants.md` note que le **4e variant
Family/Home** est dormant Q3 2026, réveil Q4 2026 / Q1 2027 par
décision canonique. C'est un cas concret d'infrastructure
**dormante par construction** :

- Les 3 variants Solaris / Nexus / Orbiter ABC sont en `SYSTEM_READY`.
- Le variant Family/Home est en `DORMANT`.

L'extension 4 états permet de **représenter canoniquement** cette
asymétrie sans casser la wheel 8-domain. Le B2 Council n'a pas à
arbitrer chaque la Family/Home comme `NEEDS_SYSTEM_OWNER` — il
peut le marquer `DORMANT` et arbitrer le réveil quand la décision
canonique est prise.

## Le cas infrastructure Kang Dynasty dormant

Un **4e agent Kang Dynasty** pressenti (cf.
[[cyborg-kang-dynasty-effectif-canon-recompte]]) serait
naturellement dormant par construction — il n'est pas encore
recruté. Mais une **infrastructure réelle** peut aussi entrer en
DORMANT :

- **Exemple 1 — Backup staging multi-AaaS** : déployé en Phase 2
  (Deploy) Q1 2026, jamais utilisé (usage 0%). DORMANT Q2 2026
  par condition 1.
- **Exemple 2 — Sandbox Dokploy legacy** : Dokploy tué par
  ADR-OMK-004 (juin 2026), sandbox isolée, usage 0% depuis.
  DORMANT par condition 1.
- **Exemple 3 — Pipeline CI/CD Vercel Edge Runtime abandonné** :
  migration vers Node.js standard effectuée, Edge Runtime
  sandbox isolé, usage 0%. DORMANT par condition 1.

L'extension 4 états permet de **tracer** ces dormances sans
surcharger la wheel.

## La table 8×4 étendue — symétrie Superman

Superman tour 3 propose une table **8×4** (8 domaines × 4 états).
Par symétrie IT, la table IT spécifique est **4×4** (4 états
× 4 transitions) :

| État source | Événement | État cible |
|---|---|---|
| `SYSTEM_READY` | alerte P0 / incident >1h | `QUARANTINE` |
| `SYSTEM_READY` | usage <20% × 3 sprints + accord Council | `DORMANT` |
| `SYSTEM_READY` | charge Kang >80% sans 7e agent | `NEEDS_SYSTEM_OWNER` |
| `NEEDS_SYSTEM_OWNER` | recrutement 7e agent / handover owner | `SYSTEM_READY` |
| `NEEDS_SYSTEM_OWNER` | alerte P0 | `QUARANTINE` |
| `QUARANTINE` | résolution incident + revue post-mortem | `SYSTEM_READY` |
| `QUARANTINE` | abandon infra (sans alternative) | `DORMANT` |
| `DORMANT` | usage en hausse / dépendance aval / décision Council | `SYSTEM_READY` |

**Note** : il n'y a **pas de transition** DORMANT → QUARANTINE
(une infra dormante n'a pas d'incidents actifs — les alertes
sont en pause pendant la dormance).

## Le format packet mésoperpétuel — extension gate_state

`b2-meso-decision-packet-spec.md` ne porte pas l'état de gate par
domaine. C'est un **gap doctrinal** comblé par l'extension
proposée :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B2-PEER-2026-XX
mode: handoff
impacted_domains:
  - it
tradeoff: "Entrée en DORMANT du sandbox Dokploy legacy (usage 0%
  depuis pivot ADR-OMK-004)."
decision: accepted
proof_expected:
  - B2 gate IT update (system_state: DORMANT, infra: dokploy-sandbox-legacy)
next_review: 12WY-2027-Q1
gate_state_update:
  domain: it
  infra: dokploy-sandbox-legacy
  previous: SYSTEM_READY
  new: DORMANT
  trigger: condition-1 (usage <20% × 3 sprints)
```

L'extension `gate_state_update` est **optionnelle** (comme
`mediation_actor` + `l0_dependency_ref` du concept
[[cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel]]).

## Le compte IT 4×4 — symétrie Superman 8×4

Superman propose une table 8×4 (8 domaines × 4 états). Par
symétrie, la table IT 4×4 (4 états × 4 transitions) est plus
**restreinte** :

- 4 états, pas 8 (pas de granularité par squad).
- 4 transitions critiques, pas 12 (8 transitions × 1.5x).

C'est cohérent avec le périmètre IT : Cyborg gère 1 squad (Kang
Dynasty) sur 3 variants AaaS, pas 8 squads.

## Anti-pièges spécifiques DORMANT IT

- **DORMANT sans ADR.** Une infrastructure dormante sans ADR est
  une bombe à retardement. La sortie de DORMANT ne sait pas
  quoi réveiller.
- **DORMANT sans monitoring P18.** P18 Observability demande ADR +
  log. Sans monitoring pendant la dormance, l'usage réel est
  invisible — la sortie de DORMANT peut être déclenchée à tort.
- **QUARANTINE sans issue.** Une infra en QUARANTINE sans
  post-mortem ne sort jamais. C'est un red flag #1 latent.
- **NEEDS_SYSTEM_OWNER sans recrutement.** Le 4e état
  NEEDS_SYSTEM_OWNER **doit** déclencher une action People (cf.
  [[cyborg-kang-dynasty-effectif-canon-recompte]]). Sans
  recrutement ou handover, l'infra dérive vers QUARANTINE.
- **DORMANT par décision Council seule.** Condition 3 (décision
  Council) ne suffit pas — les conditions 1 (usage) et 2 (no
  dépendance aval) sont cumulatives. Une décision Council ne
  peut pas *forcer* la dormance d'une infra utilisée.
- **Confondre DORMANT IT et SHADOW_ACTIVE Aquaman.** La doctrine
  SHADOW_ACTIVE Aquaman est Coach-OS-spécifique (cf. rapport
  Aquaman tour 1). DORMANT IT est la doctrine canonique B2
  Areas. Les deux sont sémantiquement proches mais **pas
  identiques** — Aquaman SHADOW_ACTIVE ne couvre pas le cycle
  de vie IT 5 phases.

## Liens

- [[superman-needs-signal-vs-dormant-8domain-doctrine]] — modèle 8×4
- [[b2-areas-dormants-doctrine]] — doctrine dormance canonique B2 Areas
- [[cyborg-cycle-vie-infrastructure-5-phases]] — dormance entre Phase 3 et 5
- [[cyborg-dans-aaas-3-variants]] — Family/Home 4e variant dormant
- [[cyborg-kang-dynasty-effectif-canon-recompte]] — NEEDS_SYSTEM_OWNER ↔ recrutement 7e
- [[b2-meso-decision-packet-spec]] — format packet canonique

## Note de confiance

**Reconstruit, symétrique Superman.** L'extension 4 états IT est
**projetée** par symétrie Superman tour 3 (`superman-needs-signal-
vs-dormant-8domain-doctrine.md`). Les 3 conditions cumulatives et
3 déclencheurs de réveil sont **tirés verbatim** de
`b2-areas-dormants-doctrine.md`. Le 4e variant Family/Home
dormant est **cité** depuis
[[cyborg-dans-aaas-3-variants]] §« Le placement canonique Cyborg ×
AaaS ». La table 4×4 IT est **mon raisonnement** par restriction
de la table 8×4 Superman au périmètre IT. L'extension
`gate_state_update` du packet mésoperpétuel est **ma proposition**
(optionnelle, comme `mediation_actor` + `l0_dependency_ref`).

**Statut** : extension 4 états IT posée, symétrique Superman 8×4.
En attente de soumission B2 Council (mode parallel, impacted
domains: [it]). Cohérence avec [[cyborg-cycle-vie-infrastructure-
5-phases]] (dormance entre Phase 3 et 5) à valider en cycle réel.
Compatibilité D4 append-only vérifiée.