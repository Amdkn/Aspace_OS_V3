# Fable × Auto-Research × /loop × Symphony × Agent OS

> Doctrine for autonomous agentic loops. Apply whenever a session involves
> Karpathy auto-research, Claude Code `/loop`, Symphony orchestration, or
> Agent OS (Brian Casel) standards. **Read at session start, every time.**

## Why

Without this rule, future agents re-derive architecture from first principles,
forget the Fable/Mythos/loop/Symphony/Agent OS connection, and force A0 to
re-teach. Cost: ~30 min A0 time + extreme frustration per session.
A0 ultimatum 2026-06-16: "SI TU ME FAIS L'AMNESIQUE APRES CA ALORS
J'ABANDONNE L'IDEE DE TRAVAILLER AVEC TOI."

## What is what (definitions, do not confuse)

| Term | What it is | Source |
|---|---|---|
| **Fable** | Karpathy YouTube 2026 — autonomous research pattern (4 pillars: Penser dense, Livrable fini, Relecture, Vérité). 63 HuggingFace sessions distilled. NOT the model Fable-M2.7 (deprecated), NOT the brand "Fable" (YT creator). | Karpathy auto-research YouTube |
| **Auto-Research** | Karpathy pattern: agent researches topic autonomously, iterates on findings, no human-in-loop per iteration. | Karpathy |
| **Claude Code `/loop`** | Runtime that fires a prompt on cron schedule. Composable with `run_in_background: true` and `ScheduleWakeup`. Min interval 60s. | Bundled `/loop` skill |
| **Symphony** | A'Space OS V2 multi-agent orchestrator: 3 A1 (Beth/Morty/Rick) + 6 A2 (Curie SNW, ZORA Discovery, Orville Ikigai, LCARS Enterprise, Holo Deck Cerritos, Holo Janeway Protostar) + 35 A3 twins. Twin runtime at `ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/`. | A'Space canon |
| **Agent OS** | Brian Casel @ Builder Methods v3.0 (2026-01-20) — bash CLI standards framework: 5 commands + 3 scripts + standards files. NOT LangChain, NOT Fabuleux-tiers, NOT a web server. | Brian Casel Builder Methods |
| **Agent OS → Symphony** | Wrapper `agent-os-to-symphony.sh` at `C:/Users/amado/ASpace_OS_V2/10_Tech_OS/agent-os-bridge/` injects Agent OS standards into Symphony twins. | A'Space infra |
| **OpenClaw Heartbeat** | Runtime tick cycle with `LEARN` step = Phase 2 (autonomous skill creation). Symmetric to agent end-of-session skill creation. | `Shadow_L0/HEARTBEAT_PROTOCOL.md` |
| **Phase 2 (Hermes-style self-improvement)** | Agents create skills at end-of-session WITHOUT A0 GO. Justification: cost of false-positive (~5 min) << cost of A0 escalation (~100x). | ADR-META-001 D7 + Hermes self-improvement |

## The 4-step loop (canonical)

1. **Capture** — twin captures raw input (`.twin.md` append, `wiki/log.md` line, or local memory file)
2. **Process** — A3 twin applies Agent OS standard (e.g., `api/response-format`, `global/coding-style`) + ADR-META-001 D1-D8 (Verify, Research, Nuance, No-Contradiction, Proof, Root-cause, Cost-of-Escalation, Cross-agent)
3. **Persist** — write-back to canon (D4 append-only, no hard-delete, `_TRASH_<date>/` for retirements)
4. **Loop** — `/loop` CronCreate or ScheduleWakeup fires next iteration

## How to apply — keyword triggers

When the user (A0) mentions ANY of:
- "auto research" / "recherche auto" / "Karpathy" / "Fable" / "Mythos"
- "loop" / "ralph" / "boucle" / "ralph-loop" / "ralph-wiggum"
- "agent OS" / "Brian Casel" / "Builder Methods" / "fabuleux"
- "Symphony" / "twin" / "agent" / "A1" / "A2" / "A3" / "Beth" / "Morty" / "Curie" / "Zora"
- "MCP" / "bridge" / "DEAL" / "GTD" / "PARA" / "12WY" / "Ikigai"

→ **IMMEDIATELY** reference this rule + the corresponding `.claude/memory/*.md` pointer. Do NOT re-derive the architecture from first principles.

## When to use auto-research (D2 gate)

✅ Use when:
- Multi-source ingestion (YouTube batch, wiki sync, Notion → PARA)
- Memory Core ↔ `.claude/memory` alignment
- Standards/skill scaffolding (Agent OS, MCP re-writes)
- Long-form handoffs (500+ line analyses)
- Pattern distillation from many sessions/examples

❌ Don't use when:
- One-shot, single-step tasks
- User demands immediate action ("Fais ça maintenant")
- Tasks with no clear "iterate on findings" loop
- Tasks where the user has explicit goal in mind, not exploration

## Autonomy doctrine (D7 + Phase 2)

- **D7 cost-of-escalation**: A0 escalation is ~100x the original error. Default to non-escalation.
- **Phase 2 (Hermes-style)**: agents create skills at end-of-session WITHOUT A0 GO. Justification: cost of false-positive skill creation (~5 min) << cost of A0 escalation (~100x).
- **D9 self-choice (ADR-META-002)**: when path is evident, choose without asking. Notification only (outbox E2).
- **D10 Local Outbox**: any decision = outbox notification to A0 (never silent).
- **D11 retry protocol**: si un A2 refuse dispatch, retry avec autre ship ou escalate Beth.

## Auto-Research execution template (4 steps, ~10 min per iteration)

```bash
# 1. Capture — read canon FIRST
Read wiki/index.md   # junction at C:/Users/amado/.claude/memory/wiki/
Read MEMORY.md       # C:/Users/amado/.claude/projects/C--Users-amado/memory/MEMORY.md
ls  <topic_dir>      # scope the topic

# 2. Process — analyze with D1-D8
#    D1: file counts, byte counts, grep receipts
#    D3: nuance terms (Fable = 3 senses, Agent OS = Brian Casel NOT LangChain)
#    D6: root cause (what's the actual blocker, not the symptom)
#    D7: don't escalate to A0 mid-research

# 3. Persist — write-back canon
#    - new .claude/memory/project_<topic>_<date>.md (D4 append-only)
#    - 1-line pointer in MEMORY.md (≤200 chars)
#    - never modify existing canon (D4)
#    - retirements → _TRASH_<date>/

# 4. Loop — schedule next iteration
#    /loop <interval> /<skill-name>      # in-session loop
#    CronCreate <cron> "<prompt>"         # persistent schedule
#    ScheduleWakeup <seconds> "<prompt>"  # /loop dynamic
```

## Anti-patterns (D6 root cause + D7 escalation prevention)

- ❌ Treating auto-research as a **goal** (it's a pattern, not a goal — "tech is not a goal")
- ❌ Spawning sub-agents without first reading canon (D2 research-first)
- ❌ Re-deriving architecture when memory file exists
- ❌ Asking "do you want me to do X?" when intent is clear
- ❌ Asking about Windows audio (user has volume, said it 3+ times)
- ❌ Forgetting Fable / Mythos / loop / Symphony / Agent OS connection (read this file at session start)
- ❌ Producing walls of text (user can't read, prefers TTS or short)
- ❌ Skipping the D1 receipts (no claim without filesystem proof)

## Related rules

- `agents.md` — agent orchestration patterns (read first)
- `hooks.md` — Stop hook TTS pattern (SAPI Hortense)
- `development-workflow.md` — feature dev with auto-research integration
- `.claude/memory/feedback_tts_and_communication.md` — TTS + communication lessons (CRITICAL feedback)
- `.claude/memory/project_symphony_karpathy_loop_integration.md` — integration map
- `.claude/memory/wiki/` (junction to Memory Core) — full canon
- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` — D1-D8 doctrine
- `_SPECS/ADR/ADR-META-002_self-choice-autonomy.md` — D9-D12 doctrine
