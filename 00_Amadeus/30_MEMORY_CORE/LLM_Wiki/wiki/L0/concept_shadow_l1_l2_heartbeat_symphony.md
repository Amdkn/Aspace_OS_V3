---
source: A0 / Codex / OpenClaw Heartbeat / OpenAI Symphony
date: 2026-05-19
type: concept
domain: Shadow_L0 / Shadow_L1 / Shadow_L2 / Heartbeat / Symphony
tags: [#Heartbeat, #Symphony, #ShadowL0, #ShadowL1, #ShadowL2, #OpenClaw, #NoRuntime]
status: DRAFT_ACTIVE
external_sources:
  - https://docs.openclaw.ai/gateway/heartbeat
  - https://openai.com/index/open-source-codex-orchestration-symphony/
---

# Shadow L1 / L2 Heartbeats Adapted To Symphony

## Executive Summary

Le heartbeat A'Space ne doit pas etre un cron qui consomme des tokens dans le vide.

Le bon modele est :

1. **OpenClaw Heartbeat** pour le contrat de comportement : petite checklist, `HEARTBEAT_OK` si rien a signaler, alertes seulement quand quelque chose merite A0.
2. **Symphony** pour le contrat d'orchestration : tick, reconciliation, candidats eligibles, dispatch, worker ephemere, retry, stall timeout, evidence.
3. **A'Space Shadow** pour le routage par couche :
   - Shadow L0 = orchestration, hygiene, audit, meta-optimisation.
   - Shadow L1 = Life OS, Baserow/Plane, scorecards, calendar, back-office personnel.
   - Shadow L2 = Business Pulse, production, growth, finance, delivery, operations.

La regle canonique : **un heartbeat ne tourne que s'il a une surface a observer ou une file a traiter**. Sinon il doit etre desactive ou repondre `HEARTBEAT_OK` sans delivery.

## Source Lessons

### OpenClaw Heartbeat

La doc OpenClaw decrit le heartbeat comme un tour planifie dans la session principale, pas comme une tache background detachee. Le comportement important pour A'Space :

- cadence configurable, `0m` pour desactiver;
- `HEARTBEAT.md` optionnel comme checklist legere;
- `lightContext` et `isolatedSession` pour reduire le cout;
- `activeHours` pour eviter les runs hors fenetre;
- `HEARTBEAT_OK` est l'accuse de reception silencieux quand rien ne merite attention;
- les blocs `tasks:` permettent de ne joindre au prompt que les checks dus.

Interpretation A'Space : le heartbeat est un **reveil de vigilance**, pas un agent qui improvise du travail.

### OpenAI Symphony

La spec Symphony decrit un orchestrateur qui, a chaque tick :

- reconcilie les runs actifs;
- valide la config;
- recupere les candidats;
- trie par priorite;
- dispatch tant qu'il reste des slots;
- gere les etats `Succeeded`, `Failed`, `TimedOut`, `Stalled`, `CanceledByReconciliation`;
- applique retry, reconciliation, stall timeout et recovery filesystem.

Interpretation A'Space : le heartbeat doit d'abord faire `PROBE -> RECONCILE -> DISPATCH?`, puis seulement invoquer un agent si une mission est eligible.

## A'Space Three-Layer Heartbeat Model

| Layer | Function | Primary Pulse | Executor | Why |
|---|---|---|---|---|
| Shadow L0 | Orchestration, audit, meta-optimisation | 60 min, disabled until organs ready | Codex CLI | Verifie LLM Wiki, hooks, tasks, capsules, drift L0/L1/L2 |
| Shadow L1 | Life OS / Back-office | 30 min, when Baserow/Plane/Calendar ready | Gemini CLI | Long context pour Life OS, Baserow, Plane, scorecards, weekly review |
| Shadow L2 | Business Pulse / production | 5 min 24/7, when production sources ready | Claude Code CLI on MiniMax | MiniMax request budget rend un pouls frequent viable pour production et ops |

Important : la cadence cible ne veut pas dire activation immediate. Tant que les systemes L1/L2 ne sont pas prets, les taches restent disabled.

## No-Empty-Heartbeat Rule

Un heartbeat est autorise seulement si au moins une condition est vraie :

1. un fichier mission existe dans `memory/inbox/`;
2. un `tasks:` block a un check du;
3. une source active a surveiller est configuree et prouvee;
4. un run precedent est `in-progress`, `stalled`, ou `needs_review`;
5. un incident/retry est en cooldown.

Sinon :

- le tick doit etre skipped;
- ou l'agent doit emettre `HEARTBEAT_OK`;
- ou la tache Windows doit rester disabled.

## Shadow L0 Heartbeat

### Mission

Shadow L0 ne produit pas de business direct. Il maintient le systeme capable de produire.

Checks typiques :

- LLM Wiki log drift : nouvelles entrees sans index/cross-ref;
- hooks Codex/Claude/Gemini : presence, parse, trust, duplication;
- skills : workflows repetes sans skill cree;
- mission queues : fichiers en attente > SLA;
- scheduler : taches disabled/enabled conformes a la phase courante;
- secret hygiene : noms de variables OK, valeurs secretes absentes;
- meta-optimisation : detecter si L1/L2 creent trop de friction.

### Cadence cible

Codex CLI : toutes les 60 minutes.

Statut actuel : **disabled** jusqu'a ce que L1/L2 aient des surfaces actives et que le L0 heartbeat d'orchestration soit valide par un run supervise.

## Shadow L1 Heartbeat

### Mission

Shadow L1 est le coeur Life OS :

- Baserow Life OS;
- Plane work-items;
- Scorecard 12WY;
- Time Use / Calendar Tracker;
- weekly review;
- fatigue/load/priorites.

Le heartbeat L1 ne doit pas "penser a ta place". Il doit remonter les anomalies :

- Rocks sans tactiques actives;
- tactiques W1-W4 sans scorecard;
- Strategic Blocks manquants;
- domaines ZORA actifs sans progression;
- Plane vide alors que Baserow contient des actions;
- dimanche review non preparee;
- surcharge cognitive : trop de tactiques ouvertes.

### Cadence cible

Gemini CLI : toutes les 30 minutes.

Pourquoi Gemini : long contexte et quota genereux, adapté aux tables Life OS, syntheses et diagnostics.

### Condition d'activation

Activer seulement apres :

- `The Scorecard (Mesure)` pret ou explicitement assume comme non pret;
- `Calendar Tracker (Time Use)` pret ou workflow manuel du dimanche documente;
- Plane workspace/projet pret ou l'absence de Plane traitee comme backlog;
- un `HEARTBEAT.md` L1 court existe avec `tasks:` dues.

## Shadow L2 Heartbeat

### Mission

Shadow L2 est le Business Pulse :

- leads et pipelines;
- production apps;
- delivery client;
- finance/margin;
- ops/legal/compliance;
- incidents.

Le heartbeat L2 peut etre frequent, mais uniquement parce qu'il surveille des surfaces qui changent :

- Airtable/ClickUp/Notion ou CLIs associes;
- Vercel/Supabase/Hostinger/Dokploy;
- logs de production;
- lead enrichment;
- cost/token burn;
- app health.

### Cadence cible

Claude Code CLI via MiniMax : toutes les 5 minutes, 24/7.

Raison : le Token Plan MiniMax rend le cout marginal acceptable, mais seulement quand L2 a des sources connectees. Sans sources, c'est du bruit.

### Condition d'activation

Activer seulement apres :

- au moins un pipeline L2 prouve par CLI/API;
- un `HEARTBEAT.md` L2 avec `tasks:` et intervals;
- une regle d'alerte claire;
- un output attendu dans LLM Wiki, Plane, ClickUp, Airtable, ou `pulse.log`;
- un fallback si MiniMax 429.

## Suggested HEARTBEAT.md Shapes

### Shadow L1 HEARTBEAT.md

```yaml
tasks:
  - name: life-os-scorecard-gap
    interval: 2h
    prompt: "Check Baserow Life OS for active Rocks without scorecard rows. Alert only if gap exists."
  - name: plane-sync-gap
    interval: 4h
    prompt: "Compare active Baserow tactics with Plane work-items. Alert only on missing operational tickets."
  - name: sunday-review-prep
    interval: 24h
    prompt: "If today is Sunday, prepare a short review checklist. Otherwise HEARTBEAT_OK."
```

### Shadow L2 HEARTBEAT.md

```yaml
tasks:
  - name: production-health
    interval: 5m
    prompt: "Check configured production health sources. Alert only on failure or missing expected signal."
  - name: lead-pipeline-drift
    interval: 30m
    prompt: "Check lead pipeline states. Alert only if raw/enriched queues exceed thresholds."
  - name: margin-shield
    interval: 6h
    prompt: "Check token/API/cost drift. Alert only if threshold crossed."
```

### Shadow L0 HEARTBEAT.md

```yaml
tasks:
  - name: wiki-log-index-drift
    interval: 1h
    prompt: "Check whether recent LLM Wiki log entries require index/concept/source updates. Alert only on drift."
  - name: skill-reflex-gap
    interval: 4h
    prompt: "Detect repeated workflows not crystallized as skills. Propose one concise skill candidate."
  - name: scheduler-conformance
    interval: 12h
    prompt: "Verify scheduled tasks match desired phase. Alert if enabled before readiness gate."
```

## Current Operational Stance

As of 2026-05-19:

- Windows tasks `ASpace-Heartbeat-*` exist but are disabled.
- This is correct because Shadow L1/L2 organs are not fully ready.
- Next step is not "run all heartbeats"; it is to build the readiness gates and `HEARTBEAT.md` task blocks.

## Readiness Gates

| Gate | L0 | L1 | L2 |
|---|---|---|---|
| Capsule exists | yes | partial | partial |
| HEARTBEAT.md exists | no | no | no |
| Source surfaces proven | local files | Baserow partial, Plane blocked | Airtable partial, prod mixed |
| tasks block defined | no | no | no |
| Scheduler enabled | disabled | disabled | disabled |
| First supervised run | pending | pending | pending |

## Next Decisions

1. Keep all scheduled tasks disabled until readiness gates exist.
2. Create `Shadow_L1/HEARTBEAT.md` and `Shadow_L2/HEARTBEAT.md` before activation.
3. Update Task Scheduler target cadence:
   - Claude Code CLI on MiniMax for L2 : 5 min, 24/7.
   - Gemini CLI for L1 : 30 min.
   - Codex CLI for L0 audit/meta : 60 min.
4. Add a `phase_enabled` flag per layer so a task can exist but skip if its organs are not ready.
5. First activation must be supervised, then switch to autonomous only after `pulse.log` proves useful non-empty behavior.

## Cross-Refs

- [[concept_heartbeat_2026]]
- [[entity_shadow_l0_executor_mesh]]
- [[concept_skill_reflex]]
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\HEARTBEAT_PROTOCOL.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\README.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L2\02_god-mode-cli-stack-20260516.md`
