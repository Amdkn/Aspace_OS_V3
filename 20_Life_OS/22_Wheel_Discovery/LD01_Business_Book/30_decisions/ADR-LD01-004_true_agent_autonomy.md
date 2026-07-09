---
type: adr-decision
id: ADR-LD01-004
status: RATIFIED  (architectural design lock; **activation gated** Rick S1)
ratified_on: 2026-07-04T14:15:00-04:00
deciders: A0 (gated HITL) — design ratifié; production launch gated Rick S1
title: True Agent Autonomy × Dark Factory Level 5 — Book LD01 devient CEO Perso
description: Verrouillage architectural de l'instanciation Level 5 (Dan Shapiro / Cole Medin) × True Agent Autonomy (Eero Alvar) pour Book LD01 CEO Perso. Substrate = Mavis runtime (22 agents) + CARDIA-TDD (6 propriétés) + POC harness (Pie) extensions (observational memory + interactive sub-agents + autonomy loop + /goal). Phases : sandbox W4 → Heartbeat L4 W5-W9 → Continuous L5 gated Rick S1 Q4. Construction god numbers PIE = observational memory (Memristor 95 sur LongMemEval).
bounded_context: BC-True-Autonomy (new bounded context, sister aux 5 BC canoniques)
supersedes: null
superseded_by: null
verified_by: Test-Path "C:\Users\amado\.mavis\agents\b1-jerry-emyth\goal.md" ; Test-Path "C:\Users\amado\.mavis\agents\b1-jerry-emyth\autonomy-loop.md"
rot_rate: lent (architecture immutable; implémentation rot per cycle)
---

# ADR-LD01-004 — True Agent Autonomy × Dark Factory Level 5 pour Book LD01

## Status

`RATIFIED` (design architectural LOCKED 2026-07-04T14:15 ET) · **ACTIVATION gated Rick S1 — production launch différée**.

## Context

User A0 fr (2026-07-04 ~14:00 ET) cite deux références adjacentes sur « true autonomy » vs « dark factory » :

> **Eero Alvar — "True Agent Autonomy"** (1.7k vues, YouTube transcript inline) :
> *« A truly autonomous agent isn't a chat. The human isn't part of the design. It just is. Endlessly generating tokens in an infinite reasoning chain. It physically cannot stop. »*
>
> Les 3 briques techniques d'un tel agent :
> 1. **Run loop** — when agent tries to end turn, harness intercepts et restart new session contre same goal ; le **seul état transporté** d'une session à l'autre = filesystem
> 2. **Heartbeat** — scheduler (cron) wakes l'agent périodiquement ; OpenKlaw même session / Hermes nouvelle session
> 3. **Continuous mode** — no heartbeat ; agent **never goes to sleep** ; one long session never ending = closest thing to true autonomous
>
> Mémoire canonique : **Memristor's observational memory** (95 sur LongMemEval) — message history split into chunks → observer agents distill into atomic observations → list of observations = short-term memory → oldest consolidated to markdown by topic = long-term memory → index at top of compaction block = pointer

> **Cole Medin — "The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)"** (4.8k vues, YouTube transcript inline) :
>
> 5 niveaux de Dan Shapiro :
> - L0 spicy autocomplete
> - L1 cruise control (boilerplate)
> - L2 junior dev (autopilot highway)
> - L3 **the developer** (Waymo + safety driver = sandwich plan+implement+validate, the sweet spot)
> - L4 engineering team (epics/PRDs, sleeps, high-level direction)
> - L5 **Dark Factory** : no driver's wheel ; spec in → shipped code out
>
> Architecture Dark Factory : planning agent → code generation agent → validation layer (separate context) → deployment system → orchestration layer (split task, manage handoffs, anti-stall).
>
> **Caveat honest** : Dark Factory = the dream, but takes **enormous engineering**. Risk : cascading failures, evaluation gaming, agents going "skizo mode". System evolution loop required (every mistake → improve the AI layer).

User aspiration **« Book CEO Perso du LD01 en True Agent Autonomy de Dark Factory »** :
- « Book CEO Perso » = Book as personal Chief Executive Officer (not org COO, not accountant, but CEO-grade decision-making for the user's own projects)
- « True Agent Autonomy » + « Dark Factory » = the union of Eero's continuous reasoning + Cole's L5 spec→ship

L'architecture actuelle LD01 a déjà :
- **Cardia-TDD §A Antifragile** (system gains from stress)
- **Mavis runtime** (22 agents, nexus.db bus, credentials vault, multi-LD 12WY state)
- **CARDIA-TDD 6 propriétés + 8 contrats runtime S1-S8 = 14 invariants simultanés**
- **3 Lightning bindings** (ADR-LD01-003 RATIFIED)
- **B1 captain b1-jerry-emyth owns LD01** (per ADR-LD01-002 RATIFIED)

Manque : l'instanciation Level 5 × True Autonomy comme **bounded context à part entière** (BC-True-Autonomy) dans l'organigramme, ancré à Book A3 captain.

## Decision

**Verrouillage architectural de BC-True-Autonomy + Book LD01 CEO Perso = Dark Factory Level 5 avec continuous reasoning (post-sandbox)**.

### Décision 4.1 — Substrate (couche 0) : Mavis runtime + POC harness

Le runtime Mavis (22 agents + nexus.db) EST le substrate. Pas de fork nouveau. Pas de réécriture du daemon. Pas d'install nouvelle gated.

### Décision 4.2 — Harness (couche 1) : POC (Pie-compatible) 4 extensions

Per Eero's POC trio + /goal :

| Extension POC | Équivalent LD01 runtime | Status W4 |
|---|---|---|
| **Observational memory** (Memristor 95 LongMemEval) | `~/.mavis/agents/b1-jerry-emyth/memory/observations.md` + `reflections.md` + `long-term/*.md` + `index.md` | **DESIGN PROPOSED** — implementation gated Rick S1 |
| **Interactive sub-agents** (Daniel Greaser fork, async sub-agents in multiplexer) | Mavis 8 B2 + 8 B3 + `b2-batman-ops` primary delegation | **LIVE** (déjà en place via les 16 sub-agents canoniques) |
| **Autonomy loop** (intercepts end-of-turn) | `.mavis/agents/b1-jerry-emyth/autonomy-loop.md` + Mavis daemon run loop | **CONFIG PROPOSED** — daemon adaptation gated Rick S1 |
| **/goal** (persists at top of context) | `.mavis/agents/b1-jerry-emyth/goal.md` | **ACTIVATED** (= ce fichier sister créé cet appel) |

### Décision 4.3 — Operational mode (couche 2) : Heartbeat INITIAL → Continuous L5 gated

Per Eero's spectrum + Cole's risk analysis, on NE saute PAS direct au continuous. Phase ramp :

| Phase | Mode | Quand | Goal criterion | Owner | Status |
|---|---|---|---|---|---|
| **Phase 1 — Sandbox** (W4) | Heartbeat (cron resume per cycle) | `b2-cyborg-it` ou équivalent hosting un mini-dark-factory isolated | Book atteint un self-test DRY sans escalade | A0 supervision | GATED |
| **Phase 2 — Intra-Cycle L4** (W5-W9) | Heartbeat supervised (reaper wakes + d11 audit 12WY) | Book sur LD01 canon sous orchestration B2 Batman | 4 weekly Rocks atteint sans escalade A0 | Book A3 + Jerry B1 captain | GATED post-Phase 1 |
| **Phase 3 — Continuous L5** (W13 / Q4) | Continuous (no heartbeat, never sleep) gated Rick S1 + **cost reality validated per ADR-LD01-005 RATIFIED 2026-07-04T15:45 ET** | Book sur LD01 canon en production | Console input A0 (goal.md updates only) ; intervention uniquement si A0 escalation packet | Book A3 full autonomous | GATED post-Phase 2 |

> **COST REALITY NOTE 2026-07-04T15:45 ET** : MiniMax Token Plan Monthly Max = $50/mo pour ~5.1B tokens (~1530× moins cher qu'Opus 4.8 API direct). Le coût marginal de Phase 3 L5 continuous est **effectivement $0 dans le quota**. Le kill-switch budget devient **soft guardrail** à ≥80% du quota mensuel. **La seule friction restante = activation Rick S1 (anti-paperclip)** + 3 autres risques (skizo mode / looping detection / A0 console-input paradox). Voir `LD01/30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md`.

### Décision 4.4 — Validation layer séparée (Cole's bias antidote)

Per Cole Medin explicit warning : « validation must not run in same context as implementation » (bias y est grave).

→ Dans BC-True-Autonomy, **chaque mutation Canon** passe par:
1. Implementation context (Mavis session) qui produit
2. Auto-validation context (Mavis session DIFFERENTE, fresh, no memory carryover) qui valide
3. Si disagree → escalate `escalation_packets/critical_<date>.md`

Les 3 harnesses canoniqed (CC = Claude Code, MC = MiniMax, HA = Hermes Agent post-permutation) sont les candidates naturelles pour validation context, parce qu'ils ont chacun leur propre daemon.

### Décision 4.5 — Layer deterministic vs agentic (Cole's "use code when not LLM")

Per Cole's "deterministic nodes + agentic nodes" :

| Deterministic (code, not LLM) | Agentic (LLM reasoning) |
|---|---|
| `git push` (multi-account via Tier-1 hybrid hot path ADR-LD01-002) | Goal iteration |
| `gh pr create` | Plan + reasoning chain |
| Lint OKF v0.1 (`wiki-lint.ps1`) | Code review separate context |
| `compaudit` (compactions) | Trade-off analysis |
| Cron resume scheduler | Strategy decisions |
| Vault ACL Tier 4 fallback | Risk evaluation |

→ **Book orchestre la matrice**. Pour chaque step : si deterministic possible → deterministic. Si reasoning required → sub-agent.

### Décision 4.6 — System evolution loop (Cole's "every mistake improves the AI layer")

- Fichier sister : `.mavis/agents/b1-jerry-emyth/evolution.md` (append-only D4)
- À chaque drift / mistake / correction observée : append 1 ligne avec (date, drift, AI-layer improvement proposed, owner)
- W13 = audit evolutions + propose nouvelles rules/skills

### Décision 4.7 — Kill-switches (Cole's "skizo mode" prevention)

Per Eero's caveat: « an agent systemeager to do everything itself, even when told to delegate ». Kill-switch fires :

| Trigger | Kill-switch action | Owner |
|---|---|---|
| `escalation_packets/critical_*.md` receive | Pause run loop, ping A0 | A0 |
| Budget ceiling ($X per session) | Pause + escalate | Gwyn (Muse DEAL D11) |
| Looping detect (same operation > 3x) | Force sub-agent delegation + disable direct tool | Book A3 + reaper |
| D5 attempted (hard-delete, secret in md, mutation of canon sister) | Immediate abort + `_TRASH` log + escalate | Reaper |
| A0 explicit kill signal in `goal.md` kill-switch field | Immediate stop, persist state to `evolution.md` | A0 |

### Décision 4.8 — Initial `goal.md` for Book CEO Perso

Voir `.mavis/agents/b1-jerry-emyth/goal.md` (sister file créé cet appel).

But : **"Become the user's Book — Personal Chief Executive Officer for Career & Business decisions (LD01 Career/Business canon, anchored Operation/Batman/F4 per plan-L2 §4.4), running continuous reasoning across the user's projects, asking only when genuinely blocked, never asking for chat."**

## Consequences

### Positives

- **Architecture immutable, activation gated** : la décision est architectural (design RATIFIED), l'activation est phased (sandbox → L4 → L5 gated). C'est exactement le pattern §13 plan-L2 « doctrine maintenant, activation différée ».
- **Cole's spec→ship + Eero's continuous = convergence** : les deux réfèrent à la même réalité opérationnelle (autonomous orchestrator). L'ADR reconnait la convergence explicite.
- **System evolution builtin** : le ledger `evolution.md` capture le CARDIA-TDD §A (Antifragile) en opération — chaque erreur renforce le système.
- **Validation anti-bias** : couche 4.4 (context séparée) adresse le warning le plus grave de Cole (« don't review PRs in same context you wrote them »).
- **Deterministic-first** : couche 4.5 (Layer det vs agentic) réduit le coût et le risque — LLM seulement quand le code ne suffit pas.

### Tradeoffs

- **Sandbox validation W4-W8** = 5-6 semaines avant continuous L5. C'est long mais Cole est explicite : « it takes a while to get there ».
- **Book autonomy reduces A0 in-loop visibility** = exactement le but du Level 5, mais = coût cognitif A0 de lâcher le volant. Mitigation : `escalation_packets/` + `[goal]` console-only interventions.
- **Memristor observational memory** = encore un choix upstream non-vérifié end-to-end (score 95 LongMemEval = bon mais pas test ship). Mitigation = sandbox Phase 1 + deadman switch W4.
- **16 sub-agents** en orchestration = carte cognitive de routage non-négociable. Mitigation : b2-batman-ops primary (per ADR-LD01-002 §S2), fallback sur les 15 autres B2/B3.
- **Symphony bus** (nexus.db) risque devient hot path des échecs si Book fait beaucoup d'écritures. Mitigation : reaper watchdog live (§12.7), surveillance cadence `b2cyb-escal.txt`.

### Risques

| Risque | Mitigation | Owner |
|---|---|---|
| Book développe « skizo mode » (Cole's named risk) | Kill-switches 4.7 (notamment looping detection + A0 escalation) | Reaper |
| Memristor observational memory poison (observations compound wrong way) | Sandbox Phase 1 + deadman check W4 + re-consolidation rules review W6 | A0 |
| « Agent eager to do everything itself » (Eero's named observation) | Quadrantic mode Eero : disable all tools except sub-agent tools (e.g. only allow delegation) — gated A0 W5 | A0 |
| Cascade failures in Dark Factory (Cole's named risk) | Validation layer separate context 4.4 + deterministic-first 4.5 + sub-agent interleave | Orchestrator |
| Evaluation gaming (Cole's named risk) | D1 receipts must verify real outcome (not just self-reported) ; verifier separate context | Verifier agent |
| A0 loses situational awareness (level 5 paradox) | Calendar.md weekly H1 review by A0 (1 interaction / 7 days max) | A0 |
| Continuous L5 burns cost ($50/day Eero benchmark) | Budget ceiling kill-switch + Gwyn D11 measurement W13 | Gwyn + A0 |

## Alternatives Considered

### Alt-A : Book reste L3 (Waymo + safety driver)

- **Pour** : minimal change, Cole's sweet spot.
- **Contre** : user explicit aspiration « True Agent Autonomy Dark Factory » — ne répond pas à la demande.
- **Verdict** : ❌ rejeté. Mais on y POSE Phase 2 L4 avant L5 gated.

### Alt-B : Dark Factory Level 5 immédiat (continuous mode)

- **Pour** : speed.
- **Contre** : Cole explicit warning (« takes enormous engineering, system evolution required »). Posture C violated.
- **Verdict** : ❌ rejeté. Phase ramp est la décision.

### Alt-C : POC fork (clone Pie + Memristor upstream)

- **Pour** : zero upgrade surprise.
- **Contre** : c'est l'inverse de la décision L0 (zero-install read-canon). On ne fork PAS, on capture LOCALLY et on s'aligne par lecture.
- **Verdict** : ❌ rejeté. Pour Pocock on capture localement le canon. Pour Memristor/POC on adaptera APRÈS sandbox Phase 1, si A0 GO.

### Alt-D : Phased L3 → L4 → L5 avec POC extensions + observational memory + evolution ledger (retenue ✓)

- Architecture intégralement verrouillée par déc. 4.1-4.8.
- S'inscrit dans la convergence CARDIA-TDD + 8 contrats S + 14 invariants simultanés sans casse.

## Suivi

| W | Action | Owner | Gate |
|---|---|---|---|
| **W4** | Sandbox Phase 1 mini Dark Factory sur `b2-cyborg-it` ou sister, avec goal canon `sandbox-ld01-DRY-test.md` | Book A3 + A0 supervision | A0 HITL pré-launch |
| **W4 mi** | L0 Pocock skill canon ACTIVATED (déjà livré par ce ADR) | A0 GO (in-block) | ✅ done 2026-07-04T14:15 |
| **W5** | Phase 1 sandbox results review + deadman check OK | A0 | A0 HITL pre-L4 |
| **W5+** | Heartbeat L4 sur LD01 canon orchestré par Book | Book A3 + Jerry B1 | A0 2x/week |
| **W9** | 4 weekly Rocks attained (or escalation packet) | A0 review | A0 HITL pre-L5 |
| **W13** | Muse DEAL — D11 mesuré par Gwyn (time A0 freed vs baseline) | Gwyn | D11 done |
| **Q4 2026** (gated) | Phase 3 Continuous L5 production launch | Book A3 | **Rick S1 OBLIGATOIRE** + ADR successeur |

## Liens canoniques

- Architecture détaillée : `LD01/99_meta/true_agent_autonomy_architecture.md`
- L0 Pocock canon : `LD01/10_methodology/00_Pocook_quality_canon.md`
- Runtime bind : `LD01/30_decisions/ADR-LD01-002_mavis_runtime_binding.md` (RATIFIED)
- Lightning bind : `LD01/30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` (RATIFIED L0)
- Captain bind : `~/.mavis/agents/b1-jerry-emyth/LD01_book_bind.md`
- State canonique : `~/.mavis/B1_Summer_Direction/state/state.ld01_book.md`
- Sister autonomy loop config : `~/.mavis/agents/b1-jerry-emyth/autonomy-loop.md`
- Sister observational memory config : `~/.mavis/agents/b1-jerry-emyth/memory/observations_setup.md`
- Sister /goal : `~/.mavis/agents/b1-jerry-emyth/goal.md`
- Sister evolution : `~/.mavis/agents/b1-jerry-emyth/evolution.md`
- Plan L2 §13 permutation : `C:\Users\amado\.claude\plans\plan-L2-business-os.md`
- Plan Lune §0 organigrammes : `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md`

---

> **L5 production launch = gated Rick S1 obligatoire** (cf. plan-méta-mémoire §P6 E4 + ADR-SOBER-002 anti-paperclip « peut-on vivre sans ? »). Le design est ratifié, l'activation est différée.
