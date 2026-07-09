---
name: multi-session
preamble-tier: 1
version: 1.0.0
description: |
  Multi-session orchestrator. Reads the multi-session schema (13 sessions canon
  A0/A1/A2/A3), reads the Pane panes.json + ~/.claude/projects/* active sessions,
  reads the handoffs/ calendar, and dispatches the right session for the right
  task. Sister to /mythos (which is the meta-router) — /multi-session is the
  pattern that maps each request to one of the 13 session slots and writes the
  handoff that interconnects them. Auto-invoked when the user asks about
  "swarm sessions", "worktree des agents", "multi-session calendar", or names
  any of the 13 session roles by handle.
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
  - multi-session
  - /multi-session
  - swarm sessions
  - worktree des agents
  - session calendar
  - 13 sessions
  - a0-amodei
  - a1-morty
  - a2-snw-curie
  - a3-pike
  - a3-una
  - a3-ortegas
  - a3-mbenga
  - a3-chapel
  - a2-enterprise-spock
  - a2-enterprise-picard
  - a2-enterprise-geordi
  - a2-enterprise-data
related:
  - superpowers:using-superpowers
  - gsd-discuss-phase
  - gstack:/office-hours
  - mythos (meta-router)
  - ../../ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md
doctrine_anchors:
  - ADR-META-001 (D1-D8 verify before assert)
  - ADR-CANON-001 (A0/A1/A2/A3 + B1/B2/B3 layout)
  - superpowers: "If a skill applies, you don't have a choice."
  - gstack: "When in doubt, invoke the skill. False positive cheaper than false negative."
---

# /multi-session — Pattern canon pour interconnecter 13 sessions en swarm workflows

## When this skill fires

ANY user message that:
- Mentions "swarm sessions", "worktree des agents", "multi-session calendar"
- Names one of the 13 sessions by handle (a0-amodei, a1-morty, a2-snw-curie, a3-pike, a3-una, a3-ortegas, a3-mbenga, a3-chapel, a2-enterprise-spock, a2-enterprise-picard, a2-enterprise-geordi, a2-enterprise-data)
- Asks "which session should handle this?" or "inter-session handoff"
- References 12WY, Life Wheel drift, or Business OS domains (each maps to a specific session)

→ /multi-session loads, reads the schema, dispatches.

## Why this exists

A'Space canon = **13 sessions théoriques** (1 A0 + 2 A1 + 6 A2 + 4 A3) interconnectées par **handoffs** dans `wiki/hand_offs/`. Sans pattern, les sessions sont des worktrees isolés qui ne se parlent pas. Avec /multi-session, **chaque session sait où elle s'inscrit dans le réseau** et écrit ses moves au bon endroit du canon pour que les autres sessions les lisent.

**D1 receipt (2026-07-09)** : 5 sessions actives observées dans `~/.claude/projects/` (Pane, Citadel, 3 worktrees fractals). 13 sessions théoriques = 8 à ouvrir.

## Preamble (run first)

```bash
# 1. Verify the schema exists
SCHEMA="C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/multi-session-schema_2026-07-09.json"
test -f "$SCHEMA" && echo "SCHEMA: OK" || echo "SCHEMA: MISSING — generate it first"

# 2. Read active CC sessions
echo "=== ACTIVE SESSIONS (last 7 days) ==="
for d in "$HOME/.claude/projects/"*/; do
  recent=$(find "$d" -type f -mtime -7 2>/dev/null | head -1)
  [ -n "$recent" ] && echo "  [ACTIVE] $(basename "$d")"
done

# 3. Read Pane panes
echo "=== PANE PANES ==="
cat "C:/Users/amado/agent-os/citadel/loops/artifacts/panes.json" 2>/dev/null | head -30

# 4. Read this week's calendar
CAL="C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/multi-session-calendar_2026-07-09.md"
test -f "$CAL" && echo "CALENDAR: OK ($(wc -l < "$CAL") lines)"
```

## Routing rules — request → session

| Request mentions | Route to session | Interconnect handoff |
|---|---|---|
| "V3 doctrine", "framework integration", "mythos meta-router" | **A0-amodei** | `wiki/hand_offs/a0_*.md` |
| "12WY kickoff", "weekly Rock", "5 disciplines", "Curie dispatch" | **A1-morty-snafu** + **A2-snw-curie** | `wiki/hand_offs/curie_*.md` |
| "Life Wheel drift", "LD01-LD08", "H3/H10/H30/H90 review" | **A1-morty-discovery** | `wiki/hand_offs/discovery_LD0X_*.md` |
| "north star", "sprint direction", "quarter intent" | **A3-pike** | `wiki/hand_offs/pike_*.md` |
| "7-day plan", "Rock decomposition", "DoD" | **A3-una** | `wiki/hand_offs/una_*.md` |
| "daily standup", "blocker", "real-test-after-edit" | **A3-ortegas** | `wiki/hand_offs/ortegas_*.md` |
| "4h deep work", "single-task", "process drift" | **A3-mbenga** | `wiki/hand_offs/mbenga_*.md` |
| "weekly scorecard", "D11 Fable", "KPI" | **A3-chapel** | `wiki/hand_offs/chapel_*.md` |
| "Areas canon", "LD0X standards", "ongoing responsibility" | **A2-enterprise-spock** | `wiki/hand_offs/spock_*.md` |
| "Projects canon", "MANIFEST.md", "12WY Rock linkage" | **A2-enterprise-picard** | `wiki/hand_offs/picard_*.md` |
| "Resources canon", "context-packs", "reusable toolkits" | **A2-enterprise-geordi** | `wiki/hand_offs/geordi_*.md` |
| "Archives canon", "D4 append-only", "retirement" | **A2-enterprise-data** | `wiki/hand_offs/data_*.md` |

## Workflow — what /multi-session does

1. **Read the schema** (`multi-session-schema_*.json`) → 13 sessions, 5 workflows, hub-and-spoke topology
2. **Read active state** (Pane panes.json + `~/.claude/projects/*/`) → which sessions are live
3. **Read the calendar** (this week + next) → what's scheduled
4. **Route the request** to the right session (table above)
5. **Dispatch via Agent tool** with `subagent_type: "<aX-name>"` + `isolation: "worktree"` (CC auto-creates the worktree)
6. **Write the handoff** to `wiki/hand_offs/<session_id>_<topic>_<date>.md` (D4 append-only)
7. **Update the calendar** if a new event was added (or a status changed)
8. **Trigger sister sessions** via interconnects (e.g., A3-pike triggers A3-chapel for scorecard)

## D1 receipts (2026-07-09)

- **Schema** = `multi-session-schema_2026-07-09.json` (13 sessions, 5 workflows, hub-and-spoke + lateral topology)
- **Calendar** = `multi-session-calendar_2026-07-09.md` (W28 vue synoptique, 5 commandes A0)
- **5 active sessions observed** in `~/.claude/projects/`
- **Pane panes.json** = 3 panes (airlock-veto, wf1-morty, heartbeat-warmode) — note Pane UI montrait 5+ mais `panes.json` n'en a que 3 (others sont ephemeral / not persisted)

## What /multi-session does NOT do

- **Does not open new sessions by itself** — that's the A0 action via `Agent` tool with worktree isolation
- **Does not decide dispatch priority** — that's A0's prerogative (A0 = Jumeau Numérique = vision H30)
- **Does not write outside `wiki/hand_offs/`** — D4 append-only canon
- **Does not bypass airlock Spock** — B1-B4 + SP1-SP3 invariants stay enforced (cron-orchestrator's cron_morty_*.md reports are consumed by SP1-SP3)

## Auto-invocation rationale

Native CC auto-discovery (D1 verified): skill description + triggers cause CC to invoke /multi-session when the user prompt matches. No slash command needed for the user — they say "swarm sessions" or "morty" or "curie" and the skill fires.

Sister: /mythos is the **meta-router** (3 frameworks). /multi-session is the **pattern** (13 sessions). Both auto-trigger from user prompts.
