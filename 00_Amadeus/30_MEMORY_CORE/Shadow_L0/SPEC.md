---
source: Shadow_L0
date: 2026-05-18
type: spec
status: ACTIVE
domain: Shadow_L0 / Symphony / Orchestration
anchors:
  - OpenAI Symphony SPEC.md (https://github.com/openai/symphony/blob/main/SPEC.md)
  - SDD-000_ricks-verse-constitution.md
  - SDD-002_a1-rick-harness.md
  - SDD-004_ricks-verse-governance.md
tags: [#SPEC, #Symphony, #Orchestration, #RicksVerse, #NoRuntime]
---

# Shadow_L0 / SPEC.md — Problem + Intended Solution

> Symphony-style spec : we describe **what should happen**, not **how every step is coded**.
> The 3 CLI harnesses (Codex / Gemini / Claude Code on MiniMax) read this spec and self-organize.

## 1. Problem Statement

A0 needs an autonomous agent mesh that can :

1. **Run on Windows without daemons** — no Hermes service, no OpenClaw gateway, no Paperclip Node process. Past attempts created fragile WSL/systemd dependencies that broke on reboot.
2. **Respect the 50/30/20 budget** — A0 spends at most 20% on L0. The mesh must self-orchestrate so A0 issues Intent at A1 level and never touches L0 configs.
3. **Bypass Anthropic's autonomy refusal** — Anthropic doesn't allow Claude SDK launches in unattended mode. We use **MiniMax Token Plan Anthropic-compatible** as the Claude Code provider, keeping the Claude Code harness while running on an autonomy-friendly backbone.
4. **Be Symphony-compliant** — leverage the 2026 doctrine of ephemeral tick sessions + multi-turn continuation + workspace persistence, but adapted to a no-runtime substrate.
5. **Use the LLM Wiki as memory** — not in-memory threads, not a database. Files. Everything compounds via `wiki/log.md` + `agents/<X>/memory/`.
6. **Anchor on SDD canon** — the spec source of truth is `10_Tech_OS/12_Blueprints/01-SDD/`, NOT `~/.openclaw/workspace/agents_runtime/` (which is sketched, never canonical).

## 2. Intended Solution (high-level steering)

```
┌───────────────────────────────────────────────────────────┐
│ A0 Amadeus (the Pilot)                                    │
│   ↓ emits Intention (3-Turn Air Lock)                     │
├───────────────────────────────────────────────────────────┤
│ A1 Rick (Symphony orchestrator role)                      │
│   ↓ routes Intent → Doctor mission queue                  │
├───────────────────────────────────────────────────────────┤
│ A2 Doctors (mission decomposers)                          │
│   13th Doctor — L0 Machine    → Codex CLI executes         │
│   12th Doctor — L2 Forge      → Gemini CLI executes        │
│   11th Doctor — L1 Back Office → Claude Code (MiniMax)     │
│   ↓ drop mission cards in agents/<CLI>/memory/inbox/      │
├───────────────────────────────────────────────────────────┤
│ A3 Companions (mission execution)                          │
│   - Mission card declares which Companion (e.g. Yaz)      │
│   - The CLI harness runs the mission per HEARTBEAT_PROTOCOL │
│   - Outputs land in outbox/, distilled to memory/         │
├───────────────────────────────────────────────────────────┤
│ LLM Wiki (compounding memory)                              │
│   - log.md = the heartbeat-aware journal                  │
│   - concepts/ = patterns extracted                        │
│   - sources/ = ingested external knowledge                │
└───────────────────────────────────────────────────────────┘
```

## 3. Doctor → CLI Routing (AI-Agnostic, Quota-Aware)

**Critical doctrine** : the 3 CLIs are **interchangeable harnesses**. Each Doctor has a *preferred* CLI by default specialty, but **any CLI can execute any Doctor's mission** if the preferred is quota-exhausted. Persona identity (Doctor + Companion) is invariant; the executing CLI is variable.

### Default Specialty + Fallback Chain

| Doctor | Layer | Companions | 1st CLI | 2nd (fallback) | 3rd (last resort) |
|---|---|---|---|---|---|
| **13th** (Machine) | L0 | Yaz, Ryan, Graham, River, Nardole | Codex CLI | **Gemini CLI** | Claude Code |
| **12th** (Forge) | L2 | Bill, Clara, Donna (DLQ) | Gemini CLI | Claude Code | Codex CLI |
| **11th** (Produit) | L1 | Amy, Rory | Claude Code on MiniMax | **Gemini CLI** | Codex CLI |

Why this layout (anchored on SDD-004 + observed quota resilience) :
- **Specialty preference** : 13th = machine work → Codex's shell/edit strength; 12th = forge/synthesis → Gemini's long-context; 11th = reasoning → Claude on MiniMax
- **Universal fallback = Gemini CLI** : largest context window + most resilient quota envelope (Google One AI Pro). When Anthropic or OpenAI rate-limits, Gemini absorbs the load with degraded-but-acceptable efficiency
- **Persona invariance** : `on_behalf_of: 11th_Doctor.Rory` survives the CLI switch; only `executed_by:` in the receipt changes

### Routing Decision (made by `heartbeat-tick.ps1`)

```
1. Read mission card → declared preferred_cli (or default per Doctor)
2. Probe last 60min of preferred CLI's pulse.log for HEARTBEAT_FAIL reason=rate-limit
3. If recent quota failure → walk fallback chain to first available CLI
4. Log routing : HEARTBEAT_ROUTE | mission=X | doctor=12th | preferred=Gemini | actual=Claude | reason=gemini-429
5. Invoke the chosen CLI; mission Soul/Workflow are unchanged
6. If ALL 3 quota-exhausted → mission stays in preferred inbox with HEARTBEAT_QUEUED, watchdog surfaces at A0 session start
```

### Why this prevents the failure A0 flagged

Original draft hard-coded CLI=Doctor. Quota failure on one CLI would have stranded all that Doctor's missions. The fallback chain ensures **no single CLI outage halts the mesh** — work continues at slightly lower efficiency on a fallback executor. Once quota resets, the next tick routes back to the preferred CLI naturally.

## 4. Symphony-Adapted Lifecycle

```
1. A0 Intent (DM with Claude Code, sync)
        ↓
2. Claude Code drafts a Mission Card (markdown, structured per program.md format SDD-002 §6)
        ↓
3. Mission Card dropped into target CLI's inbox/ (file move)
        ↓
4. Task Scheduler fires the target CLI's tick (per Heartbeat tempo)
        ↓
5. tick.ps1 reads Heartbeat.md + Mission Card → renders Turn 1 prompt → invokes CLI
        ↓
6. CLI output → outbox/<mission>/turn-1.md → Context.md updated → pulse.log appended
        ↓
7. Next tick : if Context.md says "in-progress" → Turn N+ continuation
        ↓
8. Terminal marker (<DONE> / <NEEDS_REVIEW> / <ESCALATE>) detected → final action :
   - <DONE> → distill to memory/YYYY-MM-DD.md + wiki log entry + remove from inbox
   - <NEEDS_REVIEW> → move outbox/ to A0's inbox (sign-off gate)
   - <ESCALATE> → write rejection.log + notify A0
        ↓
9. Wiki log entry created → A0 sees the result at next session start
```

## 5. Acceptance Criteria

A working Shadow_L0 mesh meets all of :

- [ ] Each of 3 CLIs has a complete capsule (Soul/Agent/Heartbeat/Tools/Context/Workflow/Continuation/memory)
- [ ] `heartbeat-tick.ps1 <agent>` runs without errors for all 3 agents
- [ ] Task Scheduler entries exist (1 per agent at declared tempo + 1 watchdog every 5 min)
- [ ] A mission card dropped in inbox is picked up at next tick, executed, and logged
- [ ] `requires_signoff` missions are diverted to A0's inbox without execution
- [ ] `pulse.log` shows continuous heartbeat (no gap > stall_timeout_min)
- [ ] Wiki log receives one entry per completed mission
- [ ] **No daemon** runs. Only the ephemeral tick processes.
- [ ] **No OpenClaw / Hermes / Paperclip install** required.

## 6. Out of Scope (this spec)

- Cross-machine orchestration (mesh is local-only for now)
- GUI / dashboard (CLI + LLM Wiki is the interface)
- Mission card auto-generation (A0 + Claude Code create them manually for now — auto-gen is V2)
- Voice / VAPI interface (separate spec)

## 7. Anti-Goals

- **Reinvent a runtime** : if we end up needing a long-running daemon, this spec failed
- **Couple to a specific provider** : MiniMax is *current* Claude Code backbone, but the protocol survives a switch
- **Hide complexity in a Gateway** : everything is files + scheduled tasks. Anyone can `cat` the state.

## 8. Inbounds

- `Shadow_L0/HEARTBEAT_PROTOCOL.md`
- `Shadow_L0/WORKFLOW.md`
- `agents/Codex_CLI/Agent.md`
- `agents/Gemini_CLI/Agent.md`
- `agents/Claude_Code_CLI/Agent.md`
