---
name: goal-loop
preamble-tier: 0
version: 1.0.0
description: |
  Autonomous goal-loop pattern. Takes an exit criterion (e.g., "D11 = 100%", "ship X", "all gaps closed"),
  dispatches sub-agents // in background, checks convergence, reports D6-honest status. Converges to:
  (a) exit criterion met, or (b) A0 manual gate hit (D7 anti-escalation), or (c) max-iterations reached.
  Sister to /multi-session (which maps tasks to sessions) and /mythos (which routes between 3 frameworks).
  Auto-invoked when user says "/goal-loop", "loop until done", "iterate to convergence", "D11 = 100%",
  or names any quantitatif exit criterion.

allowed-tools:
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Bash
  - Agent
  - TodoWrite
  - Skill

triggers:
  - goal-loop
  - /goal-loop
  - loop until done
  - iterate to convergence
  - exit criterion
  - D11 100%
  - close all gaps
  - ship X
  - autonomous loop

related:
  - multi-session (13 sessions canon mapping)
  - mythos (3 frameworks meta-router)
  - superpowers:using-superpowers (bootstrap pattern)
  - gsd-discuss-phase / gsd-plan-phase (phase loop)
  - gstack:/office-hours (CEO review for exit criteria)
  - swarm-orchestrator (N sub-agents // background)
  - super-router (gap-filling dispatch)
  - ../../ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md

doctrine_anchors:
  - ADR-META-001 (D1-D8 verify before assert)
  - ADR-SOBER-002 (anti-paperclip — converge to proof, not to ambition)
  - D9 self-choice (no escalation, no AskUserQuestion)
  - D7 cost-of-escalation (~100× original error)
  - superpowers: "If a skill applies, you don't have a choice."
  - gstack: "When in doubt, invoke. False positive cheaper than false negative."
  - gsd: "Heavy work in fresh subagent contexts. Solve context rot."

proven_run: 2026-07-09 — D11 18/100 → 75/100 → 85/100 via /goal-loop (3 sub-phases, 19 handoffs, 13 sessions touched)
---

# /goal-loop — Autonomous goal convergence pattern

## When this skill fires

ANY user message that:
- Names a quantitatif exit criterion ("D11 = 100%", "ship X feature", "all gaps closed")
- Says "loop until done", "iterate to convergence", "autonomous loop"
- Asks for a self-driving workflow that converges without manual intervention

→ /goal-loop loads, defines the exit criterion explicitly, dispatches sub-agents //, checks convergence, reports.

## Proven run (D1 verified 2026-07-09)

| Phase | Exit criterion | Sub-agents dispatched | Result | D11 delta |
|---|---|---|---|---|
| 1 | "D11 = 100%" | 0 (planning phase) | Define 5 manual gates blocking 100% | 18 → 18 |
| 2 | "D11 = 100%" | 3 (Pike + Una + Chapel) // | 3 handoffs + coordination | 18 → 75 |
| 3 | "D11 = 100%" | 8 (A3-Discovery Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou) // | 8 handoffs + aggregate | 75 → 85 |
| 4 | "D11 = 100%" | 0 (WF1 skeleton dispatch) | 5 skeleton handoffs written | 85 → 85 (manual gate remaining) |

**Convergence** : 85/100, blocked on 3 manual gates (sign-off ADRs, git push, schtasks admin). D7 anti-escalation = A0 manual action only.

## Why this exists

Without /goal-loop, A0 must manually:
1. Define the exit criterion
2. Discover what blocks it
3. Dispatch sub-agents to fill gaps
4. Re-check convergence
5. Iterate

Each iteration = A0 turns = cost 100× vs sub-agent turn (per D7). /goal-loop automates iteration **until** an A0 manual gate is hit, then reports honestly (D6).

## Preamble (run first)

```bash
# 1. Define exit criterion explicitly (D3 nuance: literal vs intent)
EXIT_CRITERION="$1"  # e.g., "D11 = 100%", "ship X feature", "all gaps closed"

# 2. D1 verify current state
echo "=== Current state D1 receipts ==="
# (varies per criterion — read relevant handoffs in wiki/hand_offs/)

# 3. Identify gaps blocking criterion
echo "=== Gaps (D6 root-cause) ==="
# (varies per criterion)

# 4. Dispatch sub-agents // to fill gaps
# Use Agent tool with subagent_type + isolation=worktree + run_in_background=true

# 5. Wait for completion notifications
# (DO NOT poll — D7 anti-escalation)

# 6. Re-check criterion convergence
echo "=== Convergence check ==="
# (varies per criterion)
```

## Loop body (executed by A0 in main session)

```
1. DEFINE exit criterion (parse from user prompt)
2. READ current state (D1 receipts: file paths, exit codes, observed state)
3. IDENTIFY gaps (D6 root-cause: what blocks the criterion)
4. DECIDE disposition:
   - IF all gaps are dispatchable (sub-agent can fill): dispatch // (max 16 concurrent per gsd/cc limit)
   - IF gap is A0 manual action (admin, sign-off, TTY): STOP, report manual gate (D7)
   - IF gap is loop-internal (next sub-agent depends on previous): chain via /multi-session
5. WAIT for completion notifications
6. RE-CHECK convergence
7. IF criterion met: DONE report
8. ELSE: iterate from step 3
9. MAX 5 iterations (then STOP, report D6 honest progress)
```

## Anti-patterns (D1-D8 enforced)

- **DO NOT** poll sub-agents (D7 cost of escalation — wait for notifications)
- **DO NOT** ask A0 questions mid-loop (D9 self-choice — A0 specified exit criterion upfront)
- **DO NOT** auto-sign-off ADRs (A0 manual action only — D7 anti-paperclip)
- **DO NOT** force git push from bash (TTY-blocked — A0 terminal only)
- **DO NOT** run schtasks without admin (admin-blocked — A0 manual only)
- **DO** report D6 honestly when manual gate hit (no false progress, no aspirational scores)
- **DO** dispatch via Agent tool with worktree isolation (CC native — solves context rot)
- **DO** write handoffs to `wiki/hand_offs/` with D4 append-only
- **DO** recompute the criterion from filesystem each iteration (no cache, no shortcut)

## Exit criterion parsing (D3 nuance)

The user's literal exit criterion may be:
- **Quantitatif** : "D11 = 100%", "ship 5 features", "all gaps closed" → direct measurement
- **Qualitatif** : "good enough", "production-ready", "no bugs" → A0 defines metric, runs loop until defined metric met
- **Implicit** : user describes desired state without naming metric → A0 extracts metric from intent

When in doubt: **ask A0 ONCE for the exit criterion**, then loop. D9 = no mid-loop questions, but a single upfront clarification is allowed.

## Convergence protocol

When /goal-loop converges (criterion met OR manual gate hit):

```
=== /goal-loop convergence report ===
Exit criterion: <literal text>
Iterations: N
Sub-agents dispatched: M (list of {subagent_type, task, duration_ms})
Handoffs written: K files in wiki/hand_offs/
Final state: <criterion score or "BLOCKED on manual gate X">

If manual gate:
- D7 ROI infinite: <command to unblock>
- D7 cost negligible: <command to unblock>

If criterion met:
- D11 / score: final
- Re-measure window: <next cron trigger>
```

## Maps to A'Space canon

| Layer | Role in /goal-loop |
|---|---|
| A0 (Jumeau Numérique) | Defines exit criterion, parses user intent, monitors convergence, reports |
| A2 superpowers | `using-superpowers` bootstrap → skill auto-invocation |
| A2 GSD | Phase loop (Discuss → Plan → Execute → Verify → Ship) for each iteration |
| A2 gstack | `gstack:/office-hours` if exit criterion is ambiguous |
| A3 freelances | Sub-agents dispatched via Agent tool |
| `wiki/hand_offs/` | Transport layer between iterations (D4 append-only) |
| `multi-session` schema | 13 sessions topology for routing |
| `super-router` | Gap-filling dispatch (snaw-w28-gaps-combler pattern) |

## Operational self-improvement

After each convergence, write to `~/.claude/skills/goal-loop/learnings.jsonl`:
```
{"date": "<ISO>", "criterion": "<text>", "iterations": N, "agents": M, "handoffs": K, "final_state": "<GREEN/BLOCKED>", "manual_gate": "<if any>", "next_time_faster": "<observation>"}
```

## Proven sub-agent types (per A'Space agents canon)

| Phase | subagent_type | Purpose |
|---|---|---|
| Discovery | `a3-discovery-{book,saru,culber,tilly,stamets,burnham,reno,georgiou}` | 1 per LDxx Life Wheel |
| Execution | `a3-snw-{pike,una,ortegas,mbenga,chapel}` | 12WY SNW captains |
| Meta-coach | `a0-amodei-murderbot-meta-coach` | A0 board observer for cross-checks |
| Veto | `a1-beth-veto` | Life preservation check (rare) |
| Sober | `a1-rick-sovereignty` | Anti-fragility check (kernel-level) |
| Code | `general-purpose` | Generic technical work |
| Quality | `code-reviewer` | Code quality review |
| Security | `security-reviewer` | Security analysis |

## D6 honest meta-observation

The /goal-loop **cannot itself bypass A0 manual gates**. That's by design (D7 anti-paperclip — autonomous loops without A0 oversight = Ultron risk). /goal-loop is the **fastest path to the manual gate**, then waits for A0. **Convergence = criterion met OR manual gate acknowledged** = both are valid wins.

The pattern replaces **A0 manually iterating** with **sub-agents iterating in background, A0 supervising**. Cost shift: A0 turns / criterion = ~1 (defines + reports) vs ~10 (manual iterate). D7 ROI infinite.