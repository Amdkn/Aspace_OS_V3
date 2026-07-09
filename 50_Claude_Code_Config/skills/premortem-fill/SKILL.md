---
name: premortem-fill
description: Run a premortem analysis on a target (plugin, service, MCP, system) and ACTIVELY FILL the gaps it finds — not just write a dead handoff. Always use this skill when the user mentions "premortem", "failure modes", "D6 inventory", "what could break on X", "fill the gaps on X", "auto-fill X", "D6 root-cause on X", or asks about resilience/sustainability of any tool, plugin, or system for 1+ year operation. Especially relevant after patterns where documentation existed but fixes were never executed (the "dead handoff" anti-pattern). The skill does D1 verification across config surfaces, generates F1-F15 failure modes, classifies remediations as SAFE_AUTO (execute), SAFE_LOG_ONLY (execute+flag), A0_GO_REQUIRED (queue), or BLOCKED (flag), executes what it can safely, writes a LIVE handoff (not dead), installs a SessionStart hook so A0 cannot forget pending actions, and updates MEMORY.md. Anti-forgetting by design.
---

# Premortem-Fill — D6 inventory + auto-fill

The user has been burned by the pattern: write a beautiful premortem handoff, file it in `wiki/hand_offs/`, A0 forgets to act on it, fix never executes. **This skill exists to break that pattern** — it doesn't just write the handoff, it executes what's safe and queues what needs A0 with a SessionStart hook so A0 cannot forget.

## When to trigger

Trigger phrases (pushy — Claude under-triggers by default):
- "premortem <target>"
- "premortem-fill <target>"
- "fill the gaps on <target>"
- "auto-fill <target>"
- "what could break on <target>"
- "D6 inventory <target>"
- "D6 root-cause on <target>"
- "1an+ durability for <target>"
- "sustainability audit on <target>"
- "anti-paperclip <target>"

Also trigger when:
- User shares an MCP panel screenshot with `✗ Failed` status
- User asks "why didn't this get fixed?"
- User references a prior handoff and asks "is this still pending?"

**Do NOT trigger** for:
- Single-step tasks ("read this file")
- Code generation / refactor (use `/feature-dev` or `/refactor-clean`)
- Documentation-only requests (the skill IS documentation + execution; if user wants only docs, refuse politely and point at the live handoff location)

## Workflow (5 phases)

### Phase 1 — D1 Inventory (read-only)
Gather current state across all config surfaces. **D1 verify before assert — never claim a state without checking the file.**

| Surface | What to read |
|---|---|
| `~/.claude/settings.json` | `enabledPlugins`, `hooks`, `permissions`, `mcpServers` |
| `~/.mcp.json` | `mcpServers` (full list) |
| npm globals | `npm ls -g --depth=0` |
| PATH binaries | `which <binary>` or `Get-Command` |
| env vars | `[System.Environment]::GetEnvironmentVariable('*','User')` filtered |
| `CLAUDE.md` | grep for `<target>` references |
| `wiki/hand_offs/` | prior handoffs matching `<target>` |
| `MEMORY.md` | topic table entries for `<target>` |
| `mindsets/` | `*<target>*` Mindset/Dispatch if exists |

**Build a state map** with:
- `claimed_state`: what docs/canon say about target
- `actual_state`: what D1 verification reveals
- `gaps`: differences between claimed and actual
- `dormant`: capability exists but never activated

### Phase 2 — Failure Mode Generation (D6)
Synthesize F1-F15 from state map + prior handoffs + 5-pillar framework:

| Pillar | Failure modes |
|---|---|
| **Channel hardening** (config integrity) | F1 (broken env), F2 (config gap), F3 (binary missing) |
| **Watchdog + DLQ** (observability) | F4 (no failure detection), F5 (no DLQ), F6 (no heartbeat) |
| **Anti-paperclip** (human gate) | F7 (auto-execution chain), F8 (prompt injection), F9 (self-replication) |
| **Recovery** (rollback) | F10 (no snapshot), F11 (no rollback), F12 (orphan processes) |
| **Activation drift** (doctrine vs reality) | F13 (capability vs activation), F14 (gates pending >30d), F15 (dead handoff) |

**D1 verify each mode** by reading the actual file/command before claiming the mode exists.

**Classify by blast radius**: data loss > service killed > canon polluted > observability gap.

### Phase 3 — AUTO-FILL (the doctrine the user wants)
For each failure mode, classify remediation:

| Class | Trigger | Action |
|---|---|---|
| **SAFE_AUTO** | No A0 decision needed, no canon touch, no settings.json edit | **Execute immediately**, log to handoff |
| **SAFE_LOG_ONLY** | Touches canon/docs but no semantics change | **Execute**, flag for A0 review |
| **A0_GO_REQUIRED** | settings.json / hooks / cron / secret rotation / canon immuable | **Queue**, do NOT execute, surface in `wiki/hand_offs/<target>_premortem_pending_actions.md` |
| **BLOCKED** | Cannot remediate (out of scope, needs A0 human input, infra change) | **Flag, do NOT execute** |

### Phase 4 — Anti-forgetting mechanism
1. **Install SessionStart hook** (`sessionstart-premortem-pending-detector.ps1`) if not already installed:
   - At session start, reads `wiki/hand_offs/*_premortem_pending_actions.md` files
   - Outputs `⚠️ [premortem-fill] <target> has <N> pending A0 actions: <file>:<line> : <action>` to stdout
   - A0 cannot start session without seeing pending actions
2. **Add hook entry to `~/.claude/settings.json`** under `hooks.SessionStart` (idempotent — skip if already present)

### Phase 5 — LIVE handoff + canon update
- **Write `wiki/hand_offs/<target>_premortem_live.md`** (auto-refreshed on each run) with:
  - Current state (auto-verified)
  - F1-F15 with auto-remediated status
  - Pending A0 actions list (live)
  - Activation gates count
  - Cron activity log
  - Sister canon links (Mindset/Dispatch)
- **Write `wiki/hand_offs/<target>_premortem_pending_actions.md`** with the A0_GO_REQUIRED queue
- **Update `MEMORY.md`** topic table (D4 append-only, 1-line pointer)
- **Cross-link** to existing `mindsets/<target>_Mindset.md` and `mindsets/<target>_Dispatch.md` if they exist; create them if missing

## Output format (each run)

```
[premortem-fill] Target: <name>
[premortem-fill] D1 state: <X config files, Y canon files, Z env vars>
[premortem-fill] Failure modes: F1-F15 generated, D1 verified
[premortem-fill] Auto-fill (SAFE_AUTO): <count> actions executed
  - F3: created `<file>` with <content>
  - F7: added line to MEMORY.md
[premortem-fill] Pending A0_GO (NOT executed): <count> actions
  - F2: settings.json edit false → true (line N) — needs A0 GO
  - F5: cron watchdog 23h ET activation — needs A0 GO
[premortem-fill] Live handoff: wiki/hand_offs/<target>_premortem_live.md
[premortem-fill] Pending actions: wiki/hand_offs/<target>_premortem_pending_actions.md
[premortem-fill] SessionStart hook: <status>
[premortem-fill] MEMORY.md: <status>
[premortem-fill] Next run: re-invoke `/premortem-fill <target>` to refresh
```

## Anti-patterns the skill REFUSES

- ❌ Just writing a handoff without executing SAFE_AUTO actions
- ❌ Executing A0_GO_REQUIRED actions without explicit GO
- ❌ Re-theorizing failure modes without D1 verify
- ❌ Creating the skill that needs A0 to remember to invoke it (SessionStart hook does the reminding)
- ❌ Bypassing the 4-file Mindmap canonical files (each target needs Mindset + Dispatch + premortem_live + premortem_pending_actions)
- ❌ Touching `AGENTS.md` / `CLAUDE.md` / `_SPECS/ADR/` without explicit A0 GO (canon immuable)

## Sister skills

- `canon-batch-spawn` — parallel canon batch creation
- `l0-deploy-verify` — infra verification
- `mcp-mastery` — MCP config debugging
- `abc-os-write-back-protocol` — canon append-only

## Constraints

- Per CLAUDE.md Skill Creator Reflex: don't wait for A0 approval — create in autonomy (Phase 2)
- Per ADR-META-001 D7: A0 escalation cost ~100x, default to action
- Per Anti-Paperclip (ADR-SOBER-002 §D3 #5): SAFE_AUTO actions MUST NOT span agent-spawn cascade, must NOT remove human gate, must NOT self-replicate

## Files

- `SKILL.md` (this file)
- `premortem_fill.py` (executable)
- `scripts/sessionstart-premortem-pending-detector.ps1` (anti-forgetting hook)