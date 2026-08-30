---
type: Concept
title: Cyborg — cycle de vie d'une infrastructure IT en 5 phases (design, deploy, run, incident, reverse) aligné AaaS
description: Le rapport Batman tour 3 a posé un cycle de vie 5 phases pour les procédures Ops (conception/pilote/production/revue/arrêt). Par symétrie IT, ce concept pose un cycle de vie 5 phases pour les infrastructures Cyborg (design/deploy/run/incident/reverse), aligné sur les 3 variants AaaS (Solaris/Nexus/Orbiter) et sur les 12WY de Summers. Le cycle ferme le trou canonique durée observé au tour 1 §5.1.7 (Batman) et projeté sur IT.
tags: [cyborg, cycle-de-vie, infrastructure, 5-phases, design-deploy-run-incident-reverse, aaas, 12wy, dormance]
generated: { by: minimax-m3, at: 2026-08-19T05:30:00Z }
verified:
  - { by: process:lecture-bcorpus-cyborg-tour-3, at: 2026-08-19T05:30:00Z }
sources:
  - id: batman-cycle-vie
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-cycle-vie-procedure-ops-cinq-phases.md"
    title: Batman cycle de vie procédure Ops 5 phases (modèle de symétrie)
    last_modified: 2026-08-19
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplets 6 (cycle mensuel Summers) + 10 (4 sprints par rock) + 24 (Batman veto condition d'arrêt)"
    last_modified: 2026-08-17
  - id: cyborg-dans-aaas
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-dans-aaas-3-variants.md"
    title: Cyborg dans AaaS — Solaris/Nexus/Orbiter (3 variants actifs Q3 2026)
    last_modified: 2026-08-19
  - id: cyborg-souverainete-adr
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-souverainete-apres-adr-omk-004.md"
    title: Cyborg — la souveraineté IT après le pivot Cloud (ADR-OMK-004)
    last_modified: 2026-08-19
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: Doctrine dormance B2 Areas — 3 conditions entrée + 3 déclencheurs réveil
    last_modified: 2026-08-19
  - id: cyborg-doctrine-5-principes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-doctrine-5-principles-dispatch.md"
    title: Cyborg — 5 principes de dispatch (P2, P3, P11+P13, P14+P17, P18)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — cycle de vie d'une infrastructure IT en 5 phases

## Pourquoi 5 phases et pas 3 ou 7

Batman tour 3 (`batman-cycle-vie-procedure-ops-cinq-phases.md`) a
posé un cycle de vie 5 phases pour les procédures Ops :
conception, pilote, production, revue, arrêt. Le cycle de vie Ops
aligne sur les 12WY de Summers (triplet 6 cycle mensuel +
triplet 10 4 sprints par rock) en découpant chaque procédure en
5 phases totalisant 8-17 sprints (2-4 mois).

Par **symétrie IT**, ce concept pose un cycle de vie 5 phases pour
les **infrastructures IT** sous responsabilité Cyborg :

| # | Phase IT | Durée sprint | B3 Kang dominant | Trigger d'entrée |
|---|---|---|---|---|
| 1 | **Design** | 1 sprint | Kang Prime | Rock B1 mandaté |
| 2 | **Deploy** | 1-2 sprints | Iron Lad + Victor Timely | Design validé |
| 3 | **Run** | 4-12 sprints | Rama-Tut + Immortus | Deploy opérationnel |
| 4 | **Incident** | événementiel | Scarlet Centurion + Kang Prime | Alerte monitoring / game day |
| 5 | **Reverse** | 1 sprint | Immortus + Rama-Tut | Décision arrêt / migration AaaS |

**5 phases, granularité sprint-compatible**, symétrique au cycle
Ops de Batman.

## Phase 1 — Design (1 sprint)

**Trigger d'entrée** : Rock B1 mandaté par Summers via handoff
queue, ou packet mésoperpétuel Council tranchant une décision
d'architecture.

**Activité canon** :

- Kang Prime (lead infra) lit le Rock + DoD + JTBD (cf.
  [[cyborg-jtbd-emit-receive-kang-dynasty]]).
- Décompose en sous-tâches (P2 Decompose-or-die, cf.
  [[cyborg-doctrine-5-principles-dispatch]]).
- Iron Lad écrit les tests d'intégration d'abord (P3 TDD).
- ADR d'avant (P18 Observability) : décision, alternatives,
  risques, RTO chiffré, **date de revue** (cf.
  [[cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft]]).

**Sortie phase 1** : ADR validé + repo Terraform initial + tests
d'intégration. DoD Design = *« ADR signé Kang Prime + tests
d'intégration verts »*.

**Cycle de revue** : fin de sprint 1 (hebdomadaire).

## Phase 2 — Deploy (1-2 sprints)

**Trigger d'entrée** : Phase 1 validée (ADR signé + tests verts).

**Activité canon** :

- Victor Timely (CI/CD discipline) pousse le code via CI/CD
  (jamais SCP manuel, P14+P17 IaC + atomic immutable).
- Iron Lad provisionne l'infra (VPS Hetzner / Supabase Cloud /
  Vercel selon variant AaaS dominant — cf.
  [[cyborg-dans-aaas-3-variants]] §« L'effet sur les paquets JTBD
  émis vers Kang Dynasty »).
- Scarlet Centurion configure sécurité réseau, firewall, SSL/TLS.

**Sortie phase 2** : Infra provisionnée + monitoring actif (P18
Observability) + alertes configurées. DoD Deploy = *« uptime ≥99%
sur 24h de test + alertes testées + escalade Cyborg <15min" »*.

**Gates canon** :

- **uptime ≥99%** et **MTTR <1h** (escalation rule Kang Dynasty
  OMK, cf. [[cyborg-jtbd-emit-receive-kang-dynasty]] §« L'escalation
  rule canonique »).
- **Souveraineté gate P11+P13** : pas de GAFAM cloud-only sans
  chemin de sortie documenté (veto Cyborg).

**Cycle de revue** : fin de sprint 2 ou 3 (selon durée).

## Phase 3 — Run (4-12 sprints)

**Trigger d'entrée** : Phase 2 validée (uptime + alertes OK).

**Activité canon** :

- Rama-Tut porte monitoring + backup (P18 Observability).
- Immortus porte capacity planning + scaling (long-term).
- Kang Prime supervise l'ensemble (H10 horizon).

**Variance par variant AaaS** :

- **Solaris** (ancre LD03 Cognition, civic-grade IT) — phase Run
  plus longue (8-12 sprints) car déploiement structurant.
- **Nexus OMK** (sub-lead IT, pivot Cloud) — phase Run moyenne
  (4-6 sprints) car pivot rapide.
- **Orbiter ABC** (lead IT partagé, récent) — phase Run courte
  (4-8 sprints) car stabilisation.

**Gates canon pendant Run** :

- **Date de revue ≤30 jours** (cf. amplification triplet 58 si
  adoptée).
- **Métrique de réversibilité** vérifiable (IaC complet + game day
  failover joué).
- **Sprint 12WY alignment** : alignement avec le cycle 12WY de
  Summers (triplet 6 + triplet 10).

**Sortie phase 3** : *« infra en régime nominal »*. DoD Run =
*« uptime ≥99% maintenu + 0 incident P0 sur 4 sprints consécutifs
+ date de revue honorée + métrique réversibilité mise à jour »*.

**Cycle de revue** : fin de chaque sprint (hebdomadaire).

## Phase 4 — Incident (événementiel)

**Trigger d'entrée** : Alerte monitoring (P18) ou game day
programmé. **Phase non planifiée**, déclenchée par événement.

**Activité canon** :

- Scarlet Centurion (sécurité) + Kang Prime (lead) traitent
  l'incident en H30/H10.
- ADR d'après (P18) : cause racine, RTO mesuré, escalade
  Cyborg si >1h.
- Si incident touche **#4 Product → IT** (Cyborg A), Batman est
  *Informed* via le journal Council (cf.
  [[cyborg-pair-check-rac-batman-i-cyborg-a-product-it]] si
  adopté).
- Si incident touche **chaîne L0** (River Song, Sobriété Rick,
  A0 HITL), escalade B1 (cf.
  [[cyborg-couplages-l0-rick-river-song-pyramide]]).

**Gates canon Incident** :

- **uptime <99%** : escalade automatique Kang Dynasty → Cyborg.
- **MTTR >1h** : escalade automatique Kang Dynasty → Cyborg.
- **incident touche L0/L1** : escalade B1 (Summers).

**Sortie phase 4** : retour à phase 3 (Run) ou transition vers
phase 5 (Reverse) si l'incident révèle un problème structurel.

## Phase 5 — Reverse (1 sprint)

**Trigger d'entrée** : Décision arrêt / migration vers un autre
variant AaaS / transition vers L0 Rick (cf. présomption W40 §M1+M2
non tranchée, [[cyborg-couplages-l0-rick-river-song-pyramide]]).

**Activité canon** :

- Immortus porte le capacity planning de sortie (décommission).
- Rama-Tut porte backup final + restauration vérifiée sur l'alternative.
- Kang Prime signe l'ADR d'arrêt + la réversibilité vérifiée.

**3 issues possibles** :

1. **Reverse vers un autre variant AaaS** — Solaris → Orbiter ABC
   (ex : cycle de vie civic-grade Solaris → cycle de vie partage
   Orbiter). DoD = *« IaC ré-importé sur Orbiter + game day failover
   joué + uptime ≥99% sur 24h test post-migration »*.
2. **Reverse vers L0 Rick** (si W40 §M1+M2 confirmé) — l'infra
   migre vers L0 Rick, Cyborg perd lead IT sur cette infra.
   DoD = *« handover L0 Rick documenté + IaC importé + 1 cycle
   de revue post-handover »*.
3. **Décommission pure** — l'infra est arrêtée sans alternative.
   DoD = *« données archivées (backup final) + dépendances
   downstream notifiées + ADR d'arrêt signé »*.

**Gates canon Reverse** :

- **Chemin de sortie documenté** (veto Cyborg) : IaC + contrat +
  failover.
- **Migration testée** : pas de bascule sans game day failover
  joué.

**Cycle de revue** : fin de sprint Reverse.

## La dormance d'une infrastructure IT

Une infrastructure peut **entrer en dormance** entre Phase 3 (Run)
et Phase 5 (Reverse) si :

1. **Usage inférieur à un seuil** pendant ≥3 sprints consécut
3. (charge <20% capacité, traffic <10% pic).
2. **Pas de dépendance aval critique** (pas de red flag #1
   latent).
3. **Décision Council** d'entrer en dormance (mode handoff).

L'infrastructure dormante conserve son **ADR**, son **IaC**, et
son **monitoring P18**. La sortie de dormance suit la doctrine
`b2-areas-dormants-doctrine.md` (3 déclencheurs de réveil : usage
en hausse, dépendance aval activée, décision Council).

## Le cycle de vie complet — un déploiement Solaris typique

Exemple concret : un déploiement Solaris AaaS civic-grade (Kardashev
Type 3, Memory Core local-first) sur 16 sprints total :

```
Phase 1 Design      : sprint 1   (Kang Prime ADR, Iron Lad TDD)
Phase 2 Deploy      : sprints 2-3 (Victor Timely CI/CD, Scarlet Centurion SSL)
Phase 3 Run         : sprints 4-15 (Rama-Tut monitoring, Immortus capacity)
Phase 4 Incident X  : sprint 7   (game day failover, RTO mesuré)
Phase 4 Incident Y  : sprint 11  (alerte uptime <99%, escalade Cyborg)
Phase 5 Reverse     : sprint 16  (migration vers Orbiter ABC, handover)
```

**Durée totale** : 16 sprints = 4 mois ≈ 12WY courant. Aligné
sur le cycle de Summers.

## Le portail LAUNCH_READY transverse — symétrie Batman

Le portique **LAUNCH_READY** est le gate transverse final posé par
Batman tour 2 (`batman-launch-ready-portique-final-transverse`).
Pour Cyborg, l'équivalent est **SYSTEM_READY** (gates IT canon, cf.
`eight-domain-avengerswheel.md`) — la sortie de Phase 2 (Deploy)
est le moment où SYSTEM_READY est émis.

La **chaîne transverse complète** :

```
Rock B1 → Phase 1 Design → Phase 2 Deploy → SYSTEM_READY (Cyborg)
                                                  ↓
                                          Phase 3 Run (Cyborg)
                                                  ↓
                                          Phase 4 Incident (Cyborg remonte)
                                                  ↓
                                          Phase 5 Reverse (Cyborg)
                                                  ↓
                                          LAUNCH_READY (Batman, portique final)
```

SYSTEM_READY est un gate **interne** au cycle de vie IT.
LAUNCH_READY est le gate **transverse** Batman qui consomme
SYSTEM_READY comme input.

## Anti-pièges spécifiques au cycle de vie IT

- **Phase 1 sans ADR.** P18 Observability demande ADR. Sans ADR,
  le design n'est pas auditable, le cycle est cassé.
- **Phase 2 sans IaC.** P14+P17 atomic immutable. Deploy sans IaC
  = SSH manuel sur prod = Kang canon violation.
- **Phase 3 sans date de revue.** Sans date, l'amplification
  triplet 58 (si adoptée) ne peut pas être honorée. Le Run
  dérive.
- **Phase 4 Incident sans escalade.** MTTR >1h = escalade
  automatique Kang Dynasty → Cyborg. Sans escalade, l'incident
  devient un red flag #1 latent.
- **Phase 5 sans chemin de sortie.** Veto Cyborg : IaC + contrat
  + failover obligatoires. Sans chemin de sortie, le Reverse
  est impossible — l'infra devient un vendor lock-in.
- **Dormance sans ADR.** Une infrastructure dormante sans ADR est
  une bombe à retardement — la sortie de dormance ne sait pas
  quoi réveiller.
- **Confondre Phase 2 (Deploy) et Phase 3 (Run).** Deploy = up
  ≤24h. Run = up ≥4 sprints. La transition Deploy → Run n'est
  pas anodine — c'est le moment où SYSTEM_READY est émis.

## Liens

- [[cyborg-jtbd-emit-receive-kang-dynasty]] — pipeline Rock→DoD→JTBD
- [[cyborg-doctrine-5-principles-dispatch]] — P2, P3, P11+P13, P14+P17, P18
- [[cyborg-dans-aaas-3-variants]] — variance par variant AaaS
- [[cyborg-souverainete-apres-adr-omk-004]] — chemin de sortie IaC + failover
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — escalade L0 Phase 4
- [[batman-cycle-vie-procedure-ops-cinq-phases]] — symétrie Ops 5 phases
- [[batman-launch-ready-portique-final-transverse]] — LAUNCH_READY transverse

## Note de confiance

**Reconstruit, symétrique Batman.** Le pattern 5 phases est
**projeté** par symétrie Batman tour 3 (`batman-cycle-vie-
procedure-ops-cinq-phases.md`). Les 5 phases IT sont **mon
raisonnement** par combinaison du pipeline Rock→DoD→JTBD
(cf. [[cyborg-jtbd-emit-receive-kang-dynasty]]) et des 5
principes de dispatch (cf. [[cyborg-doctrine-5-principles-dispatch]]).
La variance par variant AaaS est **projetée** depuis la doctrine
[[cyborg-dans-aaas-3-variants]]. La chaîne transverse
SYSTEM_READY → LAUNCH_READY est **reconstruite** depuis
[[batman-launch-ready-portique-final-transverse]]. La doctrine
dormance est **citée verbatim** depuis
`b2-areas-dormants-doctrine.md`. Le déploiement Solaris typique
est **illustratif**, pas observé.

**Statut** : cycle de vie IT 5 phases posé, aligné AaaS + 12WY.
En attente d'observation en cycle réel pour validation granularité
et durée des phases. Cohérence avec Batman cycle de vie Ops à
vérifier par le B2 Council.