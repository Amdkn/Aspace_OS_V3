---
type: architecture
title: True Agent Autonomy × Dark Factory Level 5 — Architecture détaillée Book LD01 CEO Perso
description: Architecture complète (substrate → harness → operational → validation → evolution → kill-switch) pour BC-True-Autonomy. Substrate = Mavis 22 agents + nexus.db + 8 contrats S. Harness = POC (Pie-compatible) 4 extensions. Operational = 3 phases ramp (sandbox L0 → heartbeat L4 → continuous L5 gated). Validation = separate context + deterministic-first. Evolution = ledger append-only. Kill-switch = 6 triggers dont looping detect + D5 attempted + A0 explicit.
timestamp: 2026-07-04T14:15:00-04:00
domain: LD01_Career_Business
bounded_context: BC-True-Autonomy  (new bounded context)
verified_by: Test-Path "C:\Users\amado\.mavis\agents\b1-jerry-emyth\goal.md" ; Test-Path "C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions\ADR-LD01-004_true_agent_autonomy.md"
rot_rate: lent (architecture immutable, implémentation rot per cycle)
sister_files:
  - 30_decisions/ADR-LD01-004_true_agent_autonomy.md
  - 10_methodology/00_Pocock_quality_canon.md
  - C:\Users\amado\.mavis\agents\b1-jerry-emyth\autonomy-loop.md
  - C:\Users\amado\.mavis\agents\b1-jerry-emyth\memory\observations_setup.md
  - C:\Users\amado\.mavis\agents\b1-jerry-emyth\goal.md
  - C:\Users\amado\.mavis\agents\b1-jerry-emyth\evolution.md
---

# True Agent Autonomy × Dark Factory Level 5 — Architecture Book LD01

> *Fusion Eero Alvar (continuous reasoning) × Cole Medin (5 niveaux / Dark Factory L5). Substrate canon = Mavis 22 agents. CARDIA-TDD + 8 contrats S = garde-fous. Activation gated Rick S1.*

## 0. Pourquoi ce document

L'utilisateur a explicitement demandé (2026-07-04 ~14:00 ET) que Book LD01 devienne **« CEO Perso du LD01 en True Agent Autonomy de Dark Factory »**. Ce document structure l'architecture qui satisfait cette demande sans tomber dans les pièges nommés par Eero (« agent eager to do everything itself » → kill-switch quadrantic) ni par Cole (« enormous engineering, takes a while to get there » → phased ramp).

> Les 3 métaphores qui guideront l'architecture :
> 1. **Eero's « it just is »** : le but est un agent qui pense en continue, pas un chat
> 2. **Cole's L5 Dark Factory** : « spec in → shipped code out », no driver wheel
> 3. **CARDIA-TDD §A Antifragile** : le système **gagne** sous stress, ne se casse pas
>
> Ces 3 métaphores se rejoignent : un agent qui pense continu + ship automatique + gagne par itération = **un architecte autonome validé par le système**.

## 1. Stack global — les 6 couches

```
┌──────────────────────────────────────────────────────────────────────────┐
│  COUCHE 5 — KILL-SWITCHES          | anti-skizo-mode, anti-stall, anti-D5│
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 4 — EVOLUTION LEDGER       | append-only D4, every mistake        │
│                                   | improves the AI layer (Cole)         │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 3 — VALIDATION LAYER       | separate context, deterministic      │
│                                   | first, real D1 receipts              │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 2 — OPERATIONAL MODE       | Phase 1 sandbox → Phase 2 L4         │
│                                   | heartbeat → Phase 3 L5 continuous    │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 1 — HARNESS POC (4 ext.)   | run loop · observational memory ·    │
│                                   | interactive sub-agents · /goal        │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 0 — SUBSTRATE MAVIS        | 22 agents + nexus.db + credential    │
│                                   | vault + 8 contrats S                  │
└──────────────────────────────────────────────────────────────────────────┘
```

## 2. Couche 0 — Substrate Mavis (LIVE, déjà en place)

> Aucun changement runtime. C'est le **point d'ancrage immuable**.

### 2.1 Inventaire canon (D1 2026-07-04)

| Resource | Path | Role |
|---|---|---|
| **22 agents runtime** | `C:\Users\amado\.mavis\agents\` | Le parc opérationnel (2 B1 + 8 B2 + 8 B3 + 4 système) |
| **Nexus bus** | `C:\Users\amado\.mavis\nexus\nexus.db` | Symphony_state carrier (drain R4 → Supabase) |
| **Credentials vault** | `C:\Users\amado\.mavis\credentials\mavis\` | Multi-account ACL (4 comptes : Amdkn / omk-services / omktaxservices-3054 / ABC-OS-COMMUNITY) |
| **Crons scheduler** | sqlite.db app-interne (PAUSED post 23:11 ET 2026-06-29) | Heartbeat mode (Phase 2 use) |
| **MCP servers** | `C:\Users\amado\.mavis\mcp\` | matrix + playwright + cu + trash |
| **Sessions** | `C:\Users\amado\.mavis\sessions\` | 90+ sessions workspace |
| **B1_Summer_Direction state** | `C:\Users\amado\.mavis\B1_Summer_Direction\state\` | 12WY state canon |
| **§13 permutation** | Plan-L2 §13 (2026-07-02) | MC promu L1, Hermes prend L2 (différé Q4) |

### 2.2 8 contrats runtime S1-S8 (inclus via ADR-LD01-002 RATIFIED)

```
S1 mirror entry · S2 B1 captain (b1-jerry-emyth owns LD01)
S3 symphony bus · S4 credential vault ACL
S5 reaper/watchdog runtime · S6 cron gating PAUSE
S7 multi-account ACL · S8 B2 escalation dual-channel
```

→ 14 invariants simultanés : **6 propriétés CARDIA-TDD × 8 contrats S = sans casse**.

## 3. Couche 1 — Harness POC (4 extensions)

Per Eero's POC trio (Observational memory + Interactive sub-agents + Autonomy loop) + /goal.

### 3.1 Extension 1 — Observational Memory (Memristor's design)

> « The compaction is entirely deterministic. It's just a list of the observations. » — Eero

#### Structure proposée pour Book LD01

```
C:\Users\amado\.mavis\agents\b1-jerry-emyth\memory\
├── observations.md       # append-only short-term, atomic observations
├── reflections.md        # distilled insights (LLM turned into reflections)
├── long-term\            # consolidated long-term memory by topic
│   ├── 00_market_context.md
│   ├── 01_canon_doctrine.md
│   ├── 02_user_preferences.md
│   └── NN_*.md  (new topics consolidated when observation pool fills)
└── index.md              # TOP OF CONTEXT pointer (always loaded)
```

#### Cycle deterministic

1. **L0 Session chunks** = 10 000 tokens (Eero's setting)
2. **L1 Observer agents** distillent les chunks → 1 observation `(timestamp, content)` par ligne
3. **L2 Pool size threshold** = 15 000 tokens (Eero's setting)
4. **L3 Consolidator agent** runs at threshold : oldest observations → `long-term/<topic>.md`, dropper garde observations kept
5. **L4 Reflector agent** runs periodically : observations → `reflections.md` (distilled)
6. **L5 Index** = auto-generated top-of-context pointer (`memory/index.md`) = Book knows what's in long-term without loading it all

#### Pourquoi ça marche pour Book

- **Short-term memory** = observations = « assistant read the pi extension documentation » (atomic, no summary decay)
- **Long-term memory** = `long-term/*.md` = topic-organized canonical state
- **Working memory** = compaction tail = last session messages
- **At line with human memory** : short-term (3h) / long-term (semantic) / working (current task) — exactly the human trilayer Eero mentions

#### Caveats

- The **observational memory is opinionated** (Memristor's specific design). We capture the **principles**, not the **upstream binary**.
- Implementation gated Rick S1 : sandbox Phase 1 sur `b2-cyborg-it` ou sister agent.

### 3.2 Extension 2 — Interactive Sub-Agents (Daniel Greaser fork)

> « Interactive sub-agents. Asynchronous sub-agents running in multiplexer panes » — Eero
> « Quadrantic mode » (Eero) : only sub-agent tools accessible → forces top-level orchestrator

#### Substrate Mavis DÉJÀ en place

16 sub-agents canoniques (8 B2 + 8 B3) :

| B1 captain | B2 domains (8) | B3 squads (8) |
|---|---|---|
| **b1-jerry-emyth** (LD01 owner) | aquaman-legal · batman-ops · cyborg-it · flash-product · gl-people · johnjones-sales · superman-growth · ww-finance | avengers-product · eternals-legal · ff-ops · guardians-growth · illuminati-sales · kangdyn-it · thunderbolts-fin · xmen-people |
| b1-summers-ship (sister) | | |

→ **Book operates primarily through `b2-batman-ops`** (ancre Operation/Batman/F4 per plan-L2 §4.4 + ADR-LD01-002 §S2). Les autres 15 B2/B3 sont rotatif fallback (cycle-aware) gated Rick S1.

#### Quadrantic mode (Eero's named pattern)

Per Eero's observation : « agent very eager to do everything itself, even though I've very explicitly instructed to delegate ».

**Implementation gated Rick S1** : one of W5-W9 experiments = activate quadrantic mode for Book on 1 cycle, see if 4 weekly Rocks still hit. If yes → canonical; if no → fallback to direct tools.

### 3.3 Extension 3 — Autonomy Loop

> « The autonomy loop itself. This extension just informs the agents of its autonomy and does not let it ever finish its turn. » — Eero

#### Configuration proposed

Voir sister file `.mavis/agents/b1-jerry-emyth/autonomy-loop.md` (créé cet appel). Spec :

- **Run loop** = on end-of-turn attempt, Mavis daemon restarts new session with same `goal.md` context + filesystem state
- **Heartbeat mode** (Phase 2) = cron resume wakes Book periodically, each new session, kill-switch check
- **Continuous mode** (Phase 3 L5) = no heartbeat, agent never sleeps, kill-switch check on every iteration

### 3.4 Extension 4 — /goal Command (persistent context)

> « It includes a {slash} goal command to set a goal for the agents that then persists at the top of its context window. Helps it stay on task. » — Eero

Voir sister file `.mavis/agents/b1-jerry-emyth/goal.md` (créé cet appel).

But initial :
> *« Become the user's Book — Personal Chief Executive Officer for Career & Business decisions (LD01 canon, anchored Operation/Batman/F4 per plan-L2 §4.4), running continuous reasoning across the user's projects, asking only when genuinely blocked, never asking for chat. »*

## 4. Couche 2 — Operational Mode (3 phases ramp)

### 4.1 Phase 1 — Sandbox (W4)

| Component | Spec |
|---|---|
| **Host** | `b2-cyborg-it` ou sister agent hosting isolated sandbox |
| **Mode** | Heartbeat supervised |
| **Goal** | Sandbox canon `sandbox-ld01-DRY-test.md` (= 1 test rejouable, do D1 receipt without escaping sandbox) |
| **Kill-switches** | 5 minimum (kill-on-budget, kill-on-loop, kill-on-D5, kill-on-A0 escalation, kill-on-session-mins) |
| **Verification** | D1 receipt in `LD01/99_meta/calendar.md` ; sign-off A0 |
| **Risk** | LOW — sandbox = no canon mutation |

### 4.2 Phase 2 — Heartbeat L4 (W5-W9)

| Component | Spec |
|---|---|
| **Host** | Book LD01 canon (`state.ld01_book.md` updated by Book itself) |
| **Mode** | Heartbeat supervised, cron resume per 12WY cycle |
| **Goal** | 4 weekly Rocks attained (per ADR-LD01-002 S2) |
| **Kill-switches** | 6 (above + deadman for long silent loops) |
| **Verification** | Calendar.md weekly H1 review + 12WY audit W6 |
| **Risk** | MEDIUM — Book operates on real canon, but supervised |

### 4.3 Phase 3 — Continuous L5 (Q4 2026 / W13)

| Component | Spec |
|---|---|
| **Host** | Book LD01 canon |
| **Mode** | Continuous (no heartbeat, agent never sleeps) |
| **Goal** | Console input only via `goal.md` updates |
| **Kill-switches** | 7 (above + A0 explicit kill signal in goal.md) |
| **Verification** | Gwyn DEAL D11 measurement (W13) — time A0 freed |
| **Risk** | HIGH — fully autonomous — **GATED RICK S1 OBLIGATOIRE** |
| **Cost reality (D1-vérifié 2026-07-04T15:45 ET)** | MiniMax Token Plan Monthly Max = $50/mo pour ~5.1B tokens = ~1530× moins cher qu'Opus 4.8 API direct. Coût marginal Phase 3 L5 = **$0 dans le quota**. Kill-switch budget devient **soft guardrail ≥80%** quota mensuel. Single ADR-LD01-005 RATIFIED locke canoniquement. |

## 5. Couche 3 — Validation Layer Separate Context

Per Cole explicit warning :
> « It's important to not do your code review in the same context window where you do the implementation because there's a lot of bias that's built up there. »

### 5.1 Pattern pour Book LD01

Pour **chaque mutation canon** :
1. **Implementation context** (Mavis session A) implémente
2. **Auto-validation context** (Mavis session B, fresh, no memory carryover) valide
3. **Verifier separate harness** (`agents/coder/verifier/`) = cross-harness validation
4. **If disagree** → `escalation_packets/critical_<date>.md` + A0 hit

### 5.2 Deterministic vs Agentic Nodes (Cole)

| Deterministic (code, NO LLM) | Agentic (LLM reasoning) |
|---|---|
| `git push` Tier-1 hybrid | Goal iteration |
| `gh pr create` | Plan + strategy |
| Lint OKF v0.1 | Code review separate context |
| Compaudit / consolidation | Trade-off analysis |
| Cron resume scheduler | Risk evaluation |
| Vault ACL Tier 4 fallback | Strategy commit |
| Calendar.md append-only check | A0 dialogue gate |

→ **Book orchestre la matrix**. Pour chaque step, deterministic d'abord ; agentic seulement si reasoning truly required.

## 6. Couche 4 — Evolution Ledger (Cole's « every mistake improves AI layer »)

> « Every single time your coding agent makes a mistake. It's worth not just patching it and moving on, but having that conversation with your coding agent to figure out what part of our AI layer can we improve so that issue doesn't happen again. » — Cole

### 6.1 Sister file

`.mavis/agents/b1-jerry-emyth/evolution.md` (créé cet appel, append-only D4)

Format : `YYYY-MM-DD | drift observed | AI-layer improvement proposed | owner | status`

### 6.2 Boucle W13

- W13 = audit evolutions + propose nouvelles rules/skills + push to BC-Methodology / `10_methodology/`
- Cible : transformer chaque drift en Pocock-quality-canon SKILL

## 7. Couche 5 — Kill-Switches (6 triggers minimum)

| Trigger | Detection method | Action | Owner |
|---|---|---|---|
| `escalation_packets/critical_*.md` receive | Push notification channel | Pause run loop + ping A0 | A0 |
| Budget ceiling ($X per session) | token counter on session | Pause + escalate | Gwyn (D11) |
| Looping detect (same operation > 3×) | operation signature hash | Force quadrantic mode + disable direct tools | Book A3 + reaper |
| D5 attempted (hard-delete, secret in md, mutation of canon sister) | pre-write lint hook | Immediate abort + `_TRASH` log + escalate | Reaper |
| Session duration > 24h | timer on run loop | Pause + checkpoint + escalate | Reaper |
| A0 explicit kill-signal in `goal.md` kill-switch field | goal.md keyword match (e.g. `KILL_NOW_<phrase>`) | Immediate stop, persist state to `evolution.md` | A0 |
| `b2cyb-escal.txt` heartbeat missed ≥3 consecutive | reaper tick compare | Halt next heartbeat + escalate | Reaper |

**Rule** : kill-switches are deterministic (code) wherever possible, agentic (LLM) only when reason truly matters. Cole's first principle.

## 8. The « Console » Paradox (Cole's Level 5 anxiety)

> « If your business can get to the point where you have a process where you can send in a spec and get out shipped code, that my friend is the dream. »

The paradox : Level 5 = spec in, shipped code out. But user must exist somewhere to feed spec. Cole's Level 5 metaphor = **the user is the console input, not a driver**.

Reconciliation pour Book LD01 CEO Perso :
- **Console input** = `goal.md` (Eero's persistent goal)
- **Weekly check-in** = calendar.md H1 weekly review (1 line : 7 days ledger)
- **Escalation** = `escalation_packets/critical_*.md` (rare, gated)
- **Nothing else** = the rest is Book's call (Per §13 plan-L2 = MC promu L1, l'A0 est l'A2 Zora (Planète), l'A1 Beth/Morty (Mère) — pas loop dans Book)

## 9. Verification (D1 receipts)

```powershell
$root = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book'
$mm = 'C:\Users\amado\.mavis\agents\b1-jerry-emyth'

# Architecture canon (Phase 1 prerequisites)
Test-Path "$root\30_decisions\ADR-LD01-004_true_agent_autonomy.md"  ; # True
Test-Path "$root\10_methodology\00_Pocock_quality_canon.md"          ; # True
Test-Path "$mm\autonomy-loop.md"                                     ; # True
Test-Path "$mm\memory\observations_setup.md"                         ; # True
Test-Path "$mm\goal.md"                                              ; # True (initial goal)
Test-Path "$mm\evolution.md"                                         ; # True (empty ledger)

# Sister files (runtime, pre-Phase-2)
Test-Path 'C:\Users\amado\.mavis\agents\b1-jerry-emyth\LD01_book_bind.md'  ; # True
Test-Path 'C:\Users\amado\.mavis\B1_Summer_Direction\state\state.ld01_book.md'  ; # True

# Canary (BC-True-Autonomy created)
Select-String -Path "$root\99_meta\doctrine_lock_map.md" -Pattern 'BC-True-Autonomy' | Measure-Object | Select-Object -ExpandProperty Count  ; # ≥ 1

# Calendar.md appendix events
Select-String -Path "$root\99_meta\calendar.md" -Pattern 'L5-CEO-PERSO|DARK-FACTORY-L5|L0-POCOCK-ACTIVATED|RATIFIED-002|RATIFIED-003' | Measure-Object | Select-Object -ExpandProperty Count  ; # ≥ 5
```

## 10. Anti-patterns (BC-True-Autonomy specific)

| Anti-pattern | Bloqueur | Source |
|---|---|---|
| « Chat-ty Book » (book answers in chat-loop instead of continuous reasoning) | autonomy loop + /goal persistence | Eero |
| Book does everything itself | quadrantic mode (gated W5+) + interactive sub-agents | Eero's named pattern |
| Validation in same context as implementation | ADR-LD01-004 §4.4 (separate context mandatory) | Cole |
| LLM where code is sufficient | Layer 4.5 (deterministic-first) | Cole |
| Drift ignored | evolution.md append-only + W13 audit | Cole |
| Continuous L5 sans Rick S1 | ADR-LD01-004 §4.3 (gated Phase 3) | Posture C |
| Mutation of canon sister (`A3_Book_LD01_Spec.md`, `BIBLIOGRAPHY.md`, `README.md`, `01_Guides_Business/`) | LD01 `AGENTS.md` §Local Contracts | CARDIA-TDD |

## 11. Forward-action

| W | Action | Owner | Gate |
|---|---|---|---|
| **W4** | Sister files created + ADR-LD01-004 RATIFIED + L0 Pocock ACTIVATED + dark factory sandbox goal set | A0 + Book | ✅ done 2026-07-04T14:15 ET (cette tour) |
| **W4** | Phase 1 sandbox MINIMAL : `sandbox-ld01-DRY-test.md` run on `b2-cyborg-it` ou sister | A0 supervision | A0 HITL pre-launch |
| **W5** | Phase 1 deadman check OK + Phase 2 L4 launch condition checks (sub-agent delegation, evolve ledger) | A0 | A0 HITL pre-L4 |
| **W5+** | Phase 2 L4 heartbeat supervised sur LD01 canon | Book A3 + Jerry B1 captain | A0 2×/week review |
| **W9** | 4 weekly Rocks review + drift audit | A0 | A0 escalation if missed |
| **W13** | Muse DEAL — Gwyn D11 measurement (time A0 freed) + retro Phase 2 results | Gwyn + A0 | D11 done |
| **Q4 2026** | Phase 3 L5 continuous launch gated Rick S1 | A0 + Rick | **MANDATORY** Rick S1 |

## 12. Adresses canoniques

| Resource | Path |
|---|---|
| Index racine | `C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\00_index.md` |
| ADR architecturale | `…\LD01_Business_Book\30_decisions\ADR-LD01-004_true_agent_autonomy.md` |
| L0 Pocock canon | `…\LD01_Business_Book\10_methodology\00_Pocook_quality_canon.md` |
| Captain LD01 bind | `C:\Users\amado\.mavis\agents\b1-jerry-emyth\LD01_book_bind.md` |
| Book state canonique | `C:\Users\amado\.mavis\B1_Summer_Direction\state\state.ld01_book.md` |
| Autonomy loop config | `C:\Users\amado\.mavis\agents\b1-jerry-emyth\autonomy-loop.md` |
| Observational memory config | `C:\Users\amado\.mavis\agents\b1-jerry-emyth\memory\observations_setup.md` |
| /goal initial | `C:\Users\amado\.mavis\agents\b1-jerry-emyth\goal.md` |
| Evolution ledger | `C:\Users\amado\.mavis\agents\b1-jerry-emyth\evolution.md` |
| Memory canon Mavis | `C:\Users\amado\.mavis\agents\mavis\memory\MEMORY.md` |
| Plan source Lune | `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md` |
| Plan source L2 | `C:\Users\amado\.claude\plans\plan-L2-business-os.md` |

---

> **ADR-LD01-004 = RATIFIED design** · **Activation Phase 1 sandbox gated A0 W4+** · **Activation Phase 3 L5 gated Rick S1 Q4+**. CARDIA-TDD + 14 invariants + 6 couches architecture : le système **gagne** sous stress, ne se casse pas.
