---
source: Shadow_L0
date: 2026-05-18
type: doctrine
status: ACTIVE
domain: Shadow_L0 / Heartbeat / No-Runtime
anchors:
  - SDD-002_a1-rick-harness.md
  - SDD-004_ricks-verse-governance.md §3 (Doctor mapping)
  - Symphony SPEC.md (https://github.com/openai/symphony)
tags: [#Heartbeat, #NoRuntime, #Symphony, #RicksVerse, #ShadowL0]
---

# HEARTBEAT_PROTOCOL — Doctrine du Pouls IA sans Runtime

> **Source de vérité unique** pour les 3 CLIs Shadow L0 (Gemini / Codex / Claude Code sur MiniMax).
> Tous les `Shadow_L0/agents/<X>/Heartbeat.md` héritent de ce document.
> Si conflit : ce protocole gagne, le capsule personnalise uniquement le tempo.

## 1. Principe Fondateur (verified research 2026)

Le Heartbeat IA 2026 n'est PAS un ping/pong continu. C'est un **tick-based ephemeral session** :

```
Schedule → Wake → Probe → Decide → Execute → Observe → Learn → Signal → Sleep
```

**Économie attendue** : 60-80% de tokens vs hot-session (source : Gleecus 2026, MindStudio).

## 2. Pourquoi sans runtime (Hermes / OpenClaw / Paperclip)

A0 a banni les daemons fragiles (cf. ADR-RICK-002 Paperclip deprecation, log 2026-05-17 Hermes retrogradation). Le pattern Symphony reste applicable mais **substitué intégralement par des primitives Windows natives** :

| Symphony fournit (Elixir/BEAM) | A'Space substitut natif | Coût install |
|---|---|---|
| OTP supervision tree | Windows Task Scheduler watchdog (1 task) | 0 (natif) |
| AgentRunner process | PowerShell `Start-Process` ephemeral | 0 |
| Codex App Server JSON-RPC stdio | `<cli> < prompt.md > outbox/turn-N.md` | 0 |
| stall_timeout_ms | `pulse.log` age check by watchdog | 0 |
| Workspace persistence | Filesystem (capsule + `outbox/`) | 0 |
| Linear control plane | LLM_Wiki + `inbox/` directories | 0 |
| Continuation guidance | `Continuation.md` template per capsule | 0 |

→ Zéro installation. Zéro daemon. Zéro nouveau langage runtime.

## 3. Architecture (file-based, no-daemon)

```
                  ┌──────────────────────────────────────────┐
                  │  Windows Task Scheduler (natif Windows)   │
                  └─────────────────┬────────────────────────┘
                                    │ tick every N min per agent
                                    ▼
                ┌──────────────────────────────────────────────┐
                │  ~/.claude/bin/heartbeat-tick.ps1 <agent>    │
                │  (ephemeral runner, 1 process per tick)      │
                └─────────────┬────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
       ┌─────────┐       ┌─────────┐       ┌──────────┐
       │ Codex   │       │ Gemini  │       │ Claude   │
       │ CLI     │       │ CLI     │       │ Code     │
       │(stdin)  │       │(stdin)  │       │(MiniMax) │
       └────┬────┘       └────┬────┘       └────┬─────┘
            │                 │                 │
            ▼                 ▼                 ▼
       pulse.log          pulse.log         pulse.log
       memory/            memory/           memory/
```

Une instance `heartbeat-tick.ps1 <agent>` :
1. Lit `Shadow_L0/agents/<agent>/Heartbeat.md` pour le tempo
2. Vérifie `memory/inbox/` pour une mission
3. Décide : idle / continuation Turn-N / new Turn-1 / stall recovery
4. Invoque le CLI approprié en stdin pipe
5. Écrit outputs dans `memory/outbox/<mission-id>/`
6. Append au `pulse.log`
7. Sort. Pas de daemon.

## 4. Le Tick Cycle (canonical)

```
WAKE     - Task Scheduler fires, heartbeat-tick.ps1 <agent> spawns
         - Read Heartbeat.md (tempo, stall_timeout_min, autonomy_scope)

PROBE    - List memory/inbox/*.md   → mission cards
         - List memory/outbox/*/ → in-progress missions (find Turn-N pointer in Context.md)
         - Read pulse.log tail     → last signal age

DECIDE   no mission + pulse < stall_timeout → emit HEARTBEAT_OK, exit 0
         mission inbox + no outbox yet      → Turn 1 (full Workflow.md render)
         mission outbox + Turn N < max      → Turn N+1 (Continuation.md render)
         mission outbox + Turn = max        → emit HEARTBEAT_CAP, escalate to A0
         pulse stale (> stall_timeout)      → emit HEARTBEAT_STALL, watchdog handles

EXECUTE  Render prompt from Workflow.md or Continuation.md template
         (variable substitution : ${MISSION_ID}, ${TURN_N}, ${LAST_OUTPUT}, ${SOUL}, etc.)
         Invoke <cli> via stdin pipe, with timeout = stall_timeout_min × 60s
         Capture stdout → memory/outbox/<mission-id>/turn-N.md
         Capture stderr → memory/outbox/<mission-id>/turn-N.err

OBSERVE  Parse stdout for terminal markers : <DONE>, <NEEDS_REVIEW>, <ESCALATE>
         Update Context.md : current Turn, last activity timestamp
         If <NEEDS_REVIEW> → move outbox dir to A0's inbox/

LEARN    If <DONE> + autonomy_scope match → distill outbox into memory/YYYY-MM-DD.md
                                          + append entry to LLM_Wiki/wiki/log.md
         If <ESCALATE> → write to memory/rejections.log with reason
         If failure pattern detected (3+ same rejection) → propose skill to skills_queue.md

SIGNAL   Append to pulse.log : timestamp | signal_type | mission | turn | result | duration_ms
         (Signal types : HEARTBEAT_OK, HEARTBEAT_EXEC, HEARTBEAT_FAIL, HEARTBEAT_STALL, HEARTBEAT_CAP)

SLEEP    Exit the process. Next tick is the next scheduled fire.
```

## 5. Rick's Verse Mapping — AI-Agnostic with Fallback Chain (per SDD-004 §3)

The 3 Shadow L0 CLIs are **interchangeable harnesses** wearing Persona hats. The **Persona** (Rick / Doctors / Companions) is the *identity*; the **CLI** is the *execution body*. **Any CLI can execute any Persona's mission card** — the choice is driven by (1) default specialty and (2) live quota availability.

### Default Specialty (preferred CLI per Doctor)

| Doctor (Persona) | Layer | Mission types | **Preferred CLI** | Why |
|---|---|---|---|---|
| 13th Doctor (Machine) | L0 env | PowerShell, Task Scheduler, file scaffolding, infra scripts | **Codex CLI** | Imperative shell + surgical edit strength |
| 12th Doctor (Forge) | L2 tools | Skills drafts, Hooks, ADR scaffolds, synthesis, comparison matrices | **Gemini CLI** | Long-context + Google One AI Pro generous quota |
| 11th Doctor (Produit) | L1 back-office | Reasoning, plan critique, spec refinement, orchestration | **Claude Code on MiniMax** | Anthropic-style reasoning, autonomy-friendly backbone |

### Quota-Aware Fallback Chain

When a CLI's quota is exhausted (Anthropic 429 / OpenAI rate-limit / MiniMax cap reached), the mission **stays the same Doctor**, only the executing CLI changes. The fallback order is calibrated on observed quota resilience :

| Doctor | 1st choice | 2nd (fallback) | 3rd (last resort) | Rationale |
|---|---|---|---|---|
| 13th (Machine / L0) | Codex CLI | **Gemini CLI** | Claude Code | Gemini is the full-spectrum fallback (long-context handles shell scripts too); Claude tertiary because L0 isn't its sweet spot |
| 12th (Forge / L2) | Gemini CLI | Claude Code | Codex CLI | Gemini Pro has the most generous quota; Claude can draft well too; Codex is workable but less idiomatic for narrative work |
| 11th (Produit / L1) | Claude Code | **Gemini CLI** | Codex CLI | When MiniMax/Anthropic capped, Gemini Pro absorbs reasoning load thanks to large context |

**Why Gemini is the universal fallback** : it has the most resilient quota envelope (Google One AI Pro) and the largest context window (1M+ tokens via Gemini Pro), so degraded efficiency outside its specialty is still acceptable. This is also documented in `30_MEMORY_CORE/README.md` (Roles Shadow L0 table : *"Gemini CLI : Full-Spectrum, Autonome et resilient aux quotas OpenAI/Anthropic"*).

### Routing Decision (in `heartbeat-tick.ps1`)

Before invoking the CLI :

```
1. Read mission card → declared preferred_cli (or default per Doctor)
2. Check that CLI's last pulse for HEARTBEAT_FAIL reason="rate-limit" within last 60min
3. If quota-fail recent → walk fallback chain to next available
4. Log routing decision in pulse.log:
     HEARTBEAT_ROUTE | mission=X | doctor=12th | preferred=Gemini_CLI | actual=Claude_Code_CLI | reason=gemini-429
5. Invoke the chosen CLI; mission Soul + Workflow are unchanged
```

### Critical invariants

- The CLI doesn't *become* the Companion. It executes the Companion's mission card. The Companion's identity (Soul) lives in the Mission Card, not in the CLI capsule.
- A0 must not develop in L0 himself (50/30/20 rule). The 3 CLIs are sub-A2 harnesses dispatched by A1 Rick to handle Doctor mission queues.
- **Failover never escalates to A0**. If all 3 CLIs are quota-exhausted, the mission stays in the inbox of the preferred CLI with a `HEARTBEAT_QUEUED` signal, and the watchdog flags it for visible reporting at next A0 session start.
- **Persona persistence** : if a mission is rendered by Gemini but the preferred-CLI was Claude, the mission card still says `on_behalf_of: 11th_Doctor.Rory`. The Doctor doesn't change. The receipt log notes the actual executor for audit (`executed_by: Gemini_CLI`).

## 6. Trust Gating (per agent, per mission type)

In each `agents/<X>/Agent.md`, define :

```yaml
autonomy_scope:
  - file-edit-trust-zone        # Edit files in C:\Users\amado, no review
  - llm-wiki-log-append         # Append to wiki log
  - skill-scaffold-draft        # Write to ~/.claude/skills/*/SKILL.md draft
  - airtable-read               # GET-only Airtable
requires_signoff:
  - airtable-write              # Any PATCH/POST/DELETE on real records
  - settings-json-edit          # Any modification of ~/.claude/settings.json
  - secrets-handling            # Anything involving an API key
  - prod-deploy                 # vercel deploy --prod, etc.
forbidden:
  - delete-without-trash        # always move to .trash/ first
  - write-outside-trust-zone    # any path outside C:\Users\amado
  - log-secret-value            # variable names only in pulse.log
```

A mission in `inbox/` whose type matches `requires_signoff` is **moved to A0's inbox** at the OBSERVE step instead of executing autonomously.

## 7. Symphony Multi-Turn Continuation

| Phase | Prompt template | What gets rendered |
|---|---|---|
| Turn 1 | `Workflow.md` | Full context : SOUL.md + Agent.md + Mission Card + current state + Tools.md |
| Turn N+ (1 < N ≤ 20) | `Continuation.md` | Minimal : "Continue. Last output : `outbox/turn-(N-1).md`. State : `Context.md`. Mission : `inbox/mission.md`." |

**Why this works without an in-memory session** :
- The CLI is invoked fresh each tick — but the **workspace state** (outbox files, Context.md pointer) persists
- Turn N+ prompt is tiny (just pointers + continuation directive) — the CLI re-reads the relevant files itself
- This is Symphony's pattern *exactly*, just file-based instead of OTP-supervised

Max turns per mission : **20** (Symphony default). If exceeded → `HEARTBEAT_CAP` + escalate.

## 8. Tempo Conventions

| Tempo class | Trigger | Use case |
|---|---|---|
| `on-demand` | Manual / A0 ad-hoc | Claude Code interactive sessions |
| `every 15m work-hours` | Task Scheduler, Mon-Fri 09-19 | Codex / Gemini light workload |
| `every 5m always` | Task Scheduler 24/7 | Watchdog only |
| `hourly` | Top of hour | Daily distillation tasks |
| `daily 06:00` | Once per day | Memory consolidation, lint, rotation |

Each capsule's `Heartbeat.md` declares one of these (or a cron-equivalent string).

## 9. Anti-Patterns Forbidden

1. **Hot session** — don't keep `claude` / `codex` / `gemini` running in interactive mode for >5 minutes between ticks. Defeats the 60-80% token saving.
2. **Compound checks in one tick** — one rotating check per wake, not all three.
3. **Reading other agents' Soul/Agent without permission** — capsule boundary is sacred.
4. **Improvising bypass flags** — always use documented wrappers (e.g., `shadow_l0_*` for Codex trust-dir).
5. **Logging secret values** — variable names only in `pulse.log` and `memory/`.
6. **Daemon temptation** — if a problem seems to need a long-running process, the answer is "more granular Task Scheduler entries", not a daemon.
7. **Re-deriving on every tick** — the wiki log is the memory. Read it. Don't redo discovery work each tick.

## 10. Cross-refs (Canon anchors)

- `_SPECS/SDD/` : the spec source of truth (NOT `~/.openclaw/workspace/agents_runtime/`)
- `10_Tech_OS/12_Blueprints/01-SDD/SDD-002_a1-rick-harness.md` : Rick harness AutoResearch principle + program.md format
- `10_Tech_OS/12_Blueprints/01-SDD/SDD-004_ricks-verse-governance.md` §3 : Doctor → Companion → mission scope
- `LLM_Wiki/wiki/concepts/concept_autonomous_research_loop.md` : Karpathy parent pattern
- `LLM_Wiki/wiki/concepts/concept_god_mode_cli_stack.md` : the CLI surface heartbeats run on
- `LLM_Wiki/wiki/concepts/concept_skill_reflex.md` : how heartbeats propose skills they need
- `LLM_Wiki/wiki/concepts/concept_heartbeat_2026.md` : pattern abstraction (created with this doctrine)

## 11. Sources externes (research verified)

- Symphony : https://github.com/openai/symphony (Apache 2.0, 15k⭐, ref impl Elixir/BEAM)
- Verdent Symphony deep-dive : https://www.verdent.ai/guides/openai-symphony-architecture-deep-dive
- PyShine Symphony breakdown : https://pyshine.com/Symphony-OpenAI-Coding-Agent-Orchestrator/
- Gleecus Agent Loop 2026 : https://gleecus.com/blogs/agent-loop-adaptive-ai-agents-complete-guide-2026/
- MindStudio Heartbeat : https://www.mindstudio.ai/blog/agentic-os-heartbeat-pattern-proactive-ai-agent
- SitePoint Agentic Patterns 2026 : https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/

## 12. Inbounds

- `Shadow_L0/agents/Codex_CLI/Heartbeat.md`
- `Shadow_L0/agents/Gemini_CLI/Heartbeat.md`
- `Shadow_L0/agents/Claude_Code_CLI/Heartbeat.md`
- `Shadow_L0/SPEC.md`
- `Shadow_L0/WORKFLOW.md`
- `~/.claude/bin/heartbeat-tick.ps1`
