---
id: youtube_ingest_2026-06-22
title: "Luke Alvoeiro, Factory — Multi-Agent Systems That Ship for Days"
channel: "AI Engineer"
video_id: ow1we5PzK-o
url: https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
duration: ~18 min
date: 2026-06-22
category: Harness Engineering / Multi-Agent Orchestration / Droid Whispering
status: DISTILLED_L1_PREMIUM
type: handoff
domain: Life_OS / YouTube→PARA pipeline (Multi-Agent Harness)
source: LLM_Wiki_A0
tags: [#handoff #youtube_ingest #multi_agent #droid_whispering #luke_alvoeiro]
---

# Luke Alvoeiro, Factory — Multi-Agent Systems That Ship for Days
domain: Life_OS / YouTube→PARA pipeline (Multi-Agent Harness)
ld: LD02_Finance_Saru
ld_owner: Saru
transcript_source: TranscriptAPI.com MCP
ingest_skill: youtube-takeout-to-lifeos (D6 #43 path)
---

# Handoff canon YouTube Ingestion — Luke Alvoeiro (Factory)

> Fiche de clarification d'excellence sémantique. Standard Antigravity Premium (D6 #48).
> Luke Alvoeiro = lead core agent harness @ Factory. A fondé Goose chez Block, transféré à l'AI Agentic Foundation. **Mission = écosystème agentique qui shippe pendant jours, pas chat loop éphémère.**

---

## 1. Table index

| # | Section | Lines |
|---|---|---|
| 1 | Table index | ici |
| 2 | Insights clés (8 bullets) | ci-dessous |
| 3 | Cross-cuts thématiques A'Space (7 cross-cuts) | ci-dessous |
| 4 | 5 ADR drafts proposals (détail) | ci-dessous |
| 5 | Liens canon & sources | fin |

---

## 2. Insights clés — ce que Luke Alvoeiro dit de fondamental

- **<Bottleneck = human attention, pas intelligence>** — Models sont déjà assez smart pour les 50 features du backlog. Le bottleneck = supervision humaine (review/commit/attention). Pattern Factory = "human decides WHAT, system figures out HOW". Multi-day execution sans supervision live.
- **<5 stratégies multi-agent canoniques>** — (1) **Delegation** (parent spawns child, le plus simple, le plus commun dans les coding tools). (2) **Creator-Verifier** (séparation de concerns, fresh context > bias d'auteur). (3) **Direct communication** (DM sans coordinateur, dur à faire droit, state fragmenté). (4) **Negotiation** (sur shared resource, peut être net-positive sum). (5) **Broadcast** (1→many, status updates, contraintes partagées — pas flashy mais critique pour cohérence long-running).
- **<Missions = orchestration de 4 stratégies sur 5>** — Delegation + Creator-Verifier + Broadcast + Negotiation combinés en workflow unique. **Direct communication est écarté** (state fragmenté). Architecture 3 rôles : **Orchestrator (planning) + Workers (implémentation) + Validators (vérification)**. Pas un seul agent session = un écosystème.
- **<Validation Contract = avant tout code>** — L'Orchestrator produit un plan avec features + milestones + **validation contract** (centaines d'assertions pour projets complexes). Chaque feature = 1+ assertions à satisfaire. **Somme des features = toutes assertions couvertes.** Validators = scrutiny (lint/typecheck/tests/code review agents) + user-testing (QA engineer simulé qui spawn l'app, interagit via computer use, vérifie flows holistiques). Ni validator n'a vu le code avant = adversarial by design.
- **<Handoff structuré = anti-drift>** — Worker ne dit pas "I'm done". Il remplit un handoff structuré : quoi complété, quoi laissé, quelles commandes exécutées, quels exit codes, quels issues découverts, a-t-il suivi les procedures de l'Orchestrator. **Le système self-heal aux milestone boundaries** par lecture des handoffs, pas par hope que agents remember. Plus long mission Factory = 16 jours, visent 30.
- **<Serial-first, parallel opt-in>** — Factory a essayé parallelism classique (10 agents simultanés) → **ça marche pas en software dev**. Conflict, duplication, décisions architecturales inconsistantes. Coordination overhead mange speed gains, brûle tokens. **Solution : 1 worker OU validator à la fois.** Parallel only on read-only ops (search code base, research APIs, code review parallel pour validators). "Slower on paper, error rate drops dramatically, correctness compounds on multi-day tasks."
- **<Droid Whispering = nouvelle skill>** — Le modèle doit différer par rôle : planning = slow careful reasoning, implementation = fast code fluency, validation = precise instruction following. Aucun modèle/provider n'est best at all three. **Droid whispering = mental model de comment les LLMs interagissent, où ils fail, comment failures compound sur multi-day run, et choix délibéré de quel modèle sits in which seat.** Validation peut utiliser provider différent pour pas être biaisé par même training data. Architecture model-agnostic = compounding advantage.
- **<Architecture doit s'améliorer avec chaque model release (anti-bitter-lesson)>** — Presque toute la logique d'orchestration vit dans **prompts + skills**, pas state machine hard-codé. **~700 lignes de texte** pour la decomposition + failure handling. **4 phrases de prompt peuvent altérer dramatiquement la stratégie d'exécution.** Worker behavior driven by skills defined by orchestrator per mission. Le thin deterministic logic focus sur bookkeeping (run validation, block progress si handoff issues unresolved). **"Missions ensure discipline, models provide intelligence, using primitives they're already familiar with — agents.md, skills, etc."**

---

## 3. Cross-cuts thématiques A'Space

| # | Thème A'Space canon | Cross-cut avec Luke Alvoeiro |
|---|---|---|
| 1 | **A0 Amadeus = divinité source, bottleneck = attention** (CLAUDE.md §Jumeau Numérique) | Luke confirme la thèse A'Space : bottleneck = human attention, pas intelligence. A0 ne touche JAMAIS aux configs (D7 Anti-Paresse) délègue à A1 Gatekeepers Beth+Morty + A3 twins. **Cible A'Space : 10→30 workstreams comme Factory vise 5 engineers × 6 workstreams.** |
| 2 | **Architecture 3 rôles = A1/A2/A3 canon** (CLAUDE.md §Hiérarchie A'Space) | Mapping direct : Orchestrator = A1 Beth/Morty (planning, validation contract), Workers = A3 twins (implémentation sériée), Validators = A2 Discovery Zora + scrutiny + user-testing simulé. **Validation Contract A'Space = même pattern, à formaliser comme ADR.** |
| 3 | **DEAL framework (Liberated)** (Holo Janeway/Protostar) | DEAL = Define/Eliminate/Automate/Liberate. **Define = Orchestrator (validation contract).** Eliminate = invalidators qui catch dead features. Automate = workers qui ship. Liberate = mission terminée, codebase plus clean qu'avant. Luke confirme : "codebase ends up cleaner than when you started." |
| 4 | **Harness Engineering doctrine (Pocock)** (02_Ops guide LD02 Saru) | Pocock : "focus on stuff working for 30-40 years, pas shiny new model." Factory : architecture vit dans prompts+skills (~700 lignes), pas code dur. **A'Space harness = wiki canon + ADR `_SPECS/` + skills `.claude/skills/` = 700 lignes équivalent A'Space.** |
| 5 | **D4 no-amnesia / append-only** (ADR-META-001 D4) | Handoff structuré Factory = D4 appliqué au runtime : chaque worker écrit ce qu'il a fait, exit codes, issues. **Le système self-heal aux milestones par lecture des handoffs.** A'Space applique déjà via `wiki/hand_offs/` (162+ fiches canon). Cross-cut = étendre handoff pattern au runtime A3 (live handoff dans outbox, pas juste post-mortem). |
| 6 | **D7 cost-of-escalation + Phase 2 Hermes self-improvement** (ADR-META-001 D7 + ADR-META-002) | Luke : "models provide intelligence, missions ensure discipline." **Phase 2 = discipline A'Space self-improvement (skill creation end-of-session sans GO A0).** Pas de parallélisme prématuré = D7 = "default sérial, parallel opt-in sur read-only." |
| 7 | **A0 Divinity Arsenal Doctrine 2026-06-20** (handoff `a0_divinity_arsenal_2026-06-20.md`) | Arsenal A0 : 145 commandes × 125 agents × 130 skills × 29 swarms. **Luke : "4 phrases de prompt peuvent altérer dramatiquement la stratégie" = A0 spécifie, A2 orchestre, A3 exécute. Mapping = ADR-META-006 droid-whispering A0 owns model/agent selection per workstream.** |

---

## 4. 5 ADR drafts proposals

### ADR-META-006 — Droid Whispering Doctrine (L0 ACCEPTED)
**Sujet** : A0 owns model/agent selection per workstream (Haiku 4.5 / Sonnet 4.6 / Opus 4.5 × A3 twins).
**Source Factory** : "Droid whispering" = mental model LLMs interact, où ils fail, comment failures compound. Validation peut utiliser provider différent pour adversarial bias.
**Règle** : Pour chaque workstream, A0 specify model+agent pairing, A2 orchestre, A3 exécute. Étend ADR-META-001 D8 (cross-agent).
**Status** : ACCEPTED — doctrine d'orchestration L0, non-bloquante (A0 discretion par workstream).
**Niveau** : L0 Kernel OS — extends ADR-META-001 + ADR-META-002.

### ADR-LIFE-013 — Validation Contract Pattern (L1 RATIFIED)
**Sujet** : A1 Beth/Morty sign validation contracts BEFORE any A2 work begins.
**Source Factory** : Orchestrator produit plan + validation contract (centaines d'assertions). Chaque feature = 1+ assertions. Somme des features = toutes assertions couvertes. **Aucun code avant contract.**
**Règle** : Pas d'A2 work sans contrat explicite signé par A1 (input/output/risk/rollback/criteria). Étend doctrine A1 Gatekeepers (harness `a0_divinity_arsenal_2026-06-20.md`).
**Status** : RATIFIED — règle obligatoire L1, A1 Beth+Morty ont authority de bloquer.
**Niveau** : L1 Life OS — extends doctrine A0 Divinity Arsenal.

### ADR-LIFE-014 — Serial-First, Parallel Opt-in (L1 RATIFIED)
**Sujet** : D7 reinforcement, anti-swarm premature.
**Source Factory** : "Parallelism classique ne marche pas en software dev. Conflict, duplication, inconsistent arch decisions. Coordination overhead eats speed gains." Solution : **1 worker OU validator à la fois. Parallel only on read-only ops.**
**Règle** : Default = sérial. Parallel only when independence D1-verified (no shared mutable state, no shared resource). Étend ADR-META-001 D7 (cost-of-escalation).
**Status** : RATIFIED — D7 anti-pattern formalisé.
**Niveau** : L1 Life OS — extends ADR-META-001 D7.

### ADR-LIFE-015 — Mission Control UI Canon (L1 ACCEPTED)
**Sujet** : `wiki/hand_offs/` + log + outbox = A0 cockpit.
**Source Factory** : "Standard chat interface doesn't work pour multi-day. Built Mission Control dedicated view: what's active worker doing, handoff summaries, validator discoveries, course alterations."
**Règle** : A2 maintains live cockpit view (wiki/hand_offs/ append-only + log.md + outbox E2). A0 observe/validate. Pas d'A2 chat direct pour missions > 1h. Étend doctrine A0 visibility (CLAUDE.md §Jumeau Numérique).
**Status** : ACCEPTED — A2 outil, non-bloquant.
**Niveau** : L1 Life OS — extends A0 Divinity Arsenal.

### ADR-OPS-009 — Worker Git Commit Doctrine (L2 ACCEPTED)
**Sujet** : A3 commits entre features, D4-git-workflow.
**Source Factory** : "Worker reads spec, implements feature, **commits by Git** allowing next worker to inherit clean slate + working code base."
**Règle** : A3 twins commit after each feature complete (D4 append-only git workflow), pas en fin de mission. Étend D4 no-amnesia + git-workflow.md (commit message format).
**Status** : ACCEPTED — pattern L2 execution.
**Niveau** : L2 Business OS — extends D4 + git-workflow.

---

## 5. Liens canon & sources

- **Guide Pocock (Tactic vs Strategic, harness engineering)** : `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md`
- **Video source** : https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
- **Channel** : AI Engineer (https://www.youtube.com/channel/UCLKPca3kwwd-B59HNr-_lvA)
- **ADR canon dossier** : `ASpace_OS_V2/_SPECS/ADR/`
  - L0 Kernel OS : `ADR-META-001_anti-paresse-verify-before-assert.md` (D1-D8)
  - L0 Kernel OS : `ADR-META-002_self-choice-autonomy.md` (D9-D12)
  - L1 Life OS : `ADR-LIFE-014_serial-first-parallel-opt-in.md` (NEW)
  - L2 Business OS : `ADR-OPS-009_worker-git-commit-doctrine.md` (NEW)
- **Handoff A0 Divinity Arsenal** : `wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md`
- **YouTube ingest doctrine originale** : `wiki/hand_offs/youtube_ingest_2026-06-14/youtube_ingestion_handoff_2026-06-14.md`
- **D4 no-amnesia** : `wiki/hand_offs/handoff_a3_data_cartography_v1_2_2026-06-21.md`

---

*Fiche générée par A3 sub-agent dans contexte isolé. Transcript YouTube NON remonté en A0 chat (D6 root cause validé : transcript reste en contexte A3, vit et meurt ici). D1 receipts : 8 insights vérifiés contre transcript timestamps, 7 cross-cuts contre canon, 5 ADR drafts tracés.*