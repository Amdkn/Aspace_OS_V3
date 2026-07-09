---
source: LLM_Wiki_A0
date: 2026-05-18
type: concept
domain: A0_Sovereign / Agentic_Patterns / No_Runtime
tags: [#Heartbeat #Symphony #NoRuntime #EphemeralTick #RicksVerse]
---

# Concept — Heartbeat IA 2026 (No-Runtime Tick-Based)

## Definition

The **2026 AI agent heartbeat** is an **ephemeral tick-based session pattern** : the agent doesn't run continuously. A scheduler fires it at intervals, it wakes, performs one rotating check + optionally one mission turn, signals its state to a file, and terminates. Token cost drops 60-80% versus hot sessions.

> "Stop polling, start ticking. Stop daemons, start files."

## Why this beats the old "hot session" pattern

| Hot session (pre-2026) | Tick-based (2026) |
|---|---|
| Long-running process holds context window | Process spawns, runs, dies |
| Token cost compounds during idle | Tokens spent only on actual work |
| Crash loses everything | State is on disk, next tick resumes |
| Needs daemon / supervisor | Needs only a scheduler (cron / Task Scheduler) |
| Hard to debug ("why is it stuck?") | Pulse log + outbox = full audit trail |
| Hard to isolate failures | Each tick is its own process boundary |

## Anatomy of a Tick

```
WAKE → PROBE → DECIDE → EXECUTE → OBSERVE → LEARN → SIGNAL → SLEEP
```

| Phase | What it does | A'Space artifact |
|---|---|---|
| Wake | Scheduler fires `heartbeat-tick.ps1 <agent>` | Windows Task Scheduler |
| Probe | List `memory/inbox/`, parse `pulse.log` tail | Filesystem |
| Decide | idle / Turn-1 / Turn-N+ / stall-recovery / cap | Pure function of state |
| Execute | Render prompt template, invoke CLI via stdin | `<cli> -p < prompt.md > turn-N.md` |
| Observe | Parse stdout for terminal markers (`<DONE>`, `<NEEDS_REVIEW>`, `<ESCALATE>`) | Regex on output |
| Learn | If DONE → distill memory + wiki log; if FAIL → rejections.log | Files |
| Signal | Append timestamped line to `pulse.log` | The heartbeat artifact |
| Sleep | Process exits | OS handles |

## Symphony as Reference Implementation

OpenAI's [Symphony](https://github.com/openai/symphony) (Apache 2.0, 15k⭐, Elixir/BEAM ref impl) crystallizes the 2026 pattern :

| Symphony primitive | A'Space substitute (no install) |
|---|---|
| OTP supervision tree (Elixir) | `heartbeat-watchdog.ps1` scheduled every 5min |
| AgentRunner process | `heartbeat-tick.ps1` ephemeral PowerShell |
| Codex App Server JSON-RPC stdio | `<cli> -p < prompt.md` stdin pipe |
| Linear issue tracker (control plane) | `memory/inbox/` directory (file drop) |
| Workflow.md per-issue render | `WORKFLOW.md` global + mission-card YAML frontmatter |
| Multi-turn continuation (max 20) | `outbox/<mission>/turn-N.md` chain |
| `stall_timeout_ms` | Watchdog scans `pulse.log` age vs `stall_timeout_min` |
| Retry with exponential backoff | Tick increments retry counter in `rejections.log` |

## Why "no runtime" matters for A'Space

A0 burned through OpenClaw / Hermes / Paperclip — all fragile daemon-based systems that crashed on reboot and consumed L0 attention budget. The 2026 tick-based pattern lets us **delete all three** :

- No `~/.openclaw/` gateway → use Task Scheduler
- No Hermes WSL service → use plain PowerShell
- No Paperclip Node daemon → use file drops

Result : zero install, zero new process supervision, zero new language runtime. Just files + Windows Task Scheduler + the 3 CLIs (Codex / Gemini / Claude Code on MiniMax) A0 already has.

## The 3 Shadow L0 CLIs as Tick Targets (per SDD-004 §3)

| CLI | Tempo class | Doctor mapped | Mission specialty |
|---|---|---|---|
| Codex CLI | `every 15m work-hours` | 13th (Machine) | L0 infra, PowerShell, Task Scheduler config |
| Gemini CLI | `every 30m work-hours` | 12th (Forge) | L2 tool forge, skill drafts, ADR scaffolds |
| Claude Code on MiniMax | `on-demand` + `hourly` inbox check | 11th (Produit) | L1 back-office reasoning, mission orchestration |

The Doctor → CLI mapping is canonical from `SDD-004_ricks-verse-governance.md §3` (E-Myth matrix).

## State Persistence Layout

```
Shadow_L0/agents/<CLI>/
├── Soul.md         ← Identity (rare write)
├── Agent.md        ← Mission scope, autonomy gates (rare write)
├── Heartbeat.md    ← Tempo personalization on protocol (rare write)
├── Tools.md        ← Capability surface (occasional write)
├── Context.md      ← Current Turn pointer (frequent, atomic update)
├── Workflow.md     ← Turn-1 prompt template (rare write)
├── Continuation.md ← Turn-N+ minimal prompt (rare write)
└── memory/
    ├── pulse.log         ← Append-only heartbeat trail (THE pulse)
    ├── inbox/            ← Mission cards (file drop)
    │   └── .done/        ← Completed missions (audit trail)
    ├── outbox/<mission>/ ← turn-N.md chain per mission
    ├── rejections.log    ← Patterns of failure (skill candidates)
    └── YYYY-MM-DD.md     ← Daily distillation (Claude Code maint task)
```

## Trust Gating (per agent, per mission type)

Per [SitePoint Agentic Patterns 2026](https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/) : "automate what you trust, gate what you don't."

Each `Agent.md` declares 3 lists :
- `autonomy_scope` — mission types executable without A0 sign-off
- `requires_signoff` — mission types diverted to `A0_inbox/` after Turn 1
- `forbidden` — mission types refused outright (e.g., delete-without-trash, log-secret-value)

## Why this compounds (Karpathy linkage)

This concept sits at the intersection of three patterns A'Space already absorbed :

- [[concept_compounding_knowledge]] : LLM Wiki = memory that compounds
- [[concept_autonomous_research_loop]] : Karpathy AutoResearch = research that compounds
- [[concept_god_mode_cli_stack]] : CLI Bash = execution that compounds
- **Heartbeat 2026** : *tick scheduling that compounds*

The 4 together form A'Space's autonomous OS doctrine : memory + research + execution + scheduling, all file-based, all no-runtime, all compounding.

## Cross-refs

- [[source_karpathy-autoresearch]] — the parent autonomous-loop pattern
- [[source_llm-wiki-pattern]] — sibling memory-loop pattern
- [[concept_god_mode_cli_stack]] — the execution surface heartbeats run on
- [[concept_agent_capsule]] — the 5-file standard (Soul/Agent/Heartbeat/Tools/Context) extended here
- [[concept_skill_reflex]] — how heartbeats propose skills they need
- [[entity_shadow_l0_executor_mesh]] — the mesh this heartbeat governs
- `Shadow_L0/HEARTBEAT_PROTOCOL.md` — the doctrine doc this concept abstracts
- `Shadow_L0/SPEC.md` — Symphony problem+solution adapted
- `Shadow_L0/WORKFLOW.md` — mission lifecycle
- `~/.claude/bin/heartbeat-tick.ps1` — the universal runner

## External research anchors

- OpenAI Symphony : https://github.com/openai/symphony
- Verdent deep-dive : https://www.verdent.ai/guides/openai-symphony-architecture-deep-dive
- Gleecus Agent Loop 2026 : https://gleecus.com/blogs/agent-loop-adaptive-ai-agents-complete-guide-2026/
- MindStudio Heartbeat : https://www.mindstudio.ai/blog/agentic-os-heartbeat-pattern-proactive-ai-agent
- SitePoint Agentic Patterns 2026 : https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/
- Skywork OpenClaw guide : https://skywork.ai/skypage/en/openclaw-ai-automation/2038522971263156224

## Inbounds

- `Shadow_L0/HEARTBEAT_PROTOCOL.md`
- `Shadow_L0/SPEC.md`
- `Shadow_L0/WORKFLOW.md`
- `agents/Codex_CLI/Heartbeat.md`
- `agents/Gemini_CLI/Heartbeat.md`
- `agents/Claude_Code_CLI/Heartbeat.md`
