---
name: l1-weekly-snapshot
description: >
  Weekly snapshot of 12-Week Year (USS SNW) execution status. USE THIS SKILL
  whenever the user (A0) wants to: close the week with a 12WY retro, see what
  got done vs what was committed, identify the 1-2 goals to attack next week,
  generate the Friday SNW brief, or commit the next 12WY cycle. Bakes in MCP
  interactive preference (Notion MCP for 12WY database queries), the 12WY
  doctrine (cycles of 12 weeks, weekly scorecard, 1-3 weekly tactics per goal),
  Beth/SNW mapping, A0 sovereignty (no auto-mutation of the 12WY database —
  read-only by default, write only with explicit A0 GO), D1 proof (paste the
  Notion query output), the 4-file writeback contract, and the 1-page format
  (no more, no less — A0 scans, not reads). L1 = Life OS / USS SNW.
when_to_use: |
  - User says "Friday SNW", "12WY retro", "weekly snapshot", "12-week close"
  - A0 is closing a 12WY week (typically Friday afternoon)
  - A0 wants to commit the next week's 1-3 tactics per goal
  - A0 is starting a new 12WY cycle (every 12 weeks — special 3-page version)
inputs: |
  1. Week number (1-12) and cycle start date
  2. Implicit: A0 wants a 1-page snapshot, not a multi-page report
  3. Optional: A0's pre-typed "I want to commit X" (write to Notion if provided)
outputs: |
  1. 1-page markdown snapshot (≤80 lines) at `wiki/reports/l1_snw_<cycle>_w<week>.md`
  2. Append 1 line to `wiki/log.md`
  3. If A0 committed new tactics, write to Notion 12WY database (HUMAN-READABLE diff first)
---

# /l1-weekly-snapshot — Friday 12WY retro + next-week commit

> **Doctrine** : 12-Week Year (Brian P. Moran) = execute in 12-week cycles.
> Each week = 1 scorecard. Each goal = 1-3 weekly tactics. Discipline =
> weekly review, no skipping.
>
> **Canon refs** : `concept_shadow_l1_l2_heartbeat_symphony.md` ·
> 12WY official `12weekyear.com` · Notion `AGENT_REGISTRY_DB` (Sovereign sync).

## When to trigger

| Signal | Action |
|---|---|
| A0 says "Friday SNW", "12WY retro", "weekly close" | Run the standard weekly flow |
| A0 says "I scored X this week on goal Y" | Fold into the snapshot if mid-week |
| A0 says "12-week cycle ending" | Run the **cycle close** variant (3 pages, not 1) |
| A0 says "I want to start a new cycle" | Hand off to `picard-audit-and-prod-workflow` style (PRD, then break into 12 weeks) |

## MCP interactive — Notion queries (read-only by default)

```text
# Pull the current 12WY cycle
mcp__notion__API-post-search query="12WY cycle <YYYY>"
# Or, if a data_source_id is known:
mcp__notion__API-query-data-source data_source_id=<id> filter={...}

# Pull this week's tactics
mcp__notion__API-query-data-source data_source_id=<tactics_db>
  filter={"property": "Week", "number": {"equals": <week>}}
  filter={"property": "Cycle", "relation": {"contains": <cycle_id>}}
```

**Anti-pattern** : do NOT use `query-data-source` with `data_source_url=collection://...`
syntax (per the Sovereign notational rules — use `API-query-data-source` with
`data_source_id`, or `API-post-search` with the title).

## Read-only by default — write contract

| Operation | Default | Override |
|---|---|---|
| Read cycle / goal / tactic | yes | n/a |
| Read scorecard | yes | n/a |
| Write new tactic | **NO** (HITL) | A0 must pre-type the tactic in chat |
| Update tactic status (done/partial/blocked) | **NO** (HITL) | A0 must pre-type the status |
| Archive a goal | **NO** (HITL) | A0 must explicitly say "archive" |

If A0 says "commit X, Y, Z as next week", surface the diff first:
```
=== PROPOSED WRITE TO NOTION 12WY DB ===
Tactics to create (3):
- Goal: "Ship P1.4 Vercel" / Tactic: "Run L0 deploy-verify on preview URL" / Week: 12
- Goal: "Write 12WY retro" / Tactic: "Draft 1-page snapshot by Fri 17:00" / Week: 12
- Goal: "L2 mesh protocol" / Tactic: "Ratify ADR-L2-MESH-001" / Week: 11

Type GO to write, MODIFY to edit, VETO to abort.
```

Only after A0 says GO does the skill call `API-post-page` or `API-patch-page`.

## The 1-page snapshot format

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l1_snw_<cycle>_w<week>.md`

```markdown
---
report_type: l1_snw_snapshot
cycle: <cycle_name>
week: <1-12>
date: YYYY-MM-DD
agent: <session id>
---

# SNW Snapshot — Cycle <name> · Week <N>/12 · <YYYY-MM-DD>

## This week's scorecard

| Goal | Planned | Done | Status |
|---|---|---|---|
| <goal 1> | <X tactics> | <Y done> | GREEN/YELLOW/RED |
| <goal 2> | ... | ... | ... |
| <goal 3> | ... | ... | ... |

**Overall**: <X>% execution. <1-line read on the week>

## What worked

- <1 bullet per green tactic, with link to proof>

## What blocked

- <1 bullet per yellow/red, with proposed unblock>

## Next week's commitment (1-3 tactics per goal)

### <Goal 1>

- [ ] <tactic 1>
- [ ] <tactic 2>

### <Goal 2>

- [ ] <tactic 1>

## Cycle progress

- Weeks completed: N/12
- Cycle ends: <date>
- Cycle-level goal status: <1 line>
```

**Hard cap** : ≤80 lines. A0 scans in 60 seconds. If longer, the format is
wrong, not the content.

## Cycle close (every 12 weeks)

When `week == 12`, replace the standard format with a 3-page close:
- **Page 1** : the standard 1-page snapshot (above)
- **Page 2** : cycle scorecard (goal by goal, weeks G/Y/R, key learnings)
- **Page 3** : next cycle proposal (3-5 new goals, drafted from the close)
  — flagged as **DRAFT, A0 to ratify before next cycle starts**

Path: `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/reports/l1_snw_cycle_<name>_close.md`

## Constraints

| Constraint | Enforcement |
|---|---|
| ≤80 lines per snapshot | A0 scan time is the hard limit |
| No auto-write to Notion | HITL gate; surface diff, wait for GO |
| D1 proof | Every "done" item has a link/observation backing it |
| Cite the actual Notion page/ID | No paraphrasing — quote the row's `Name` property verbatim |
| No fabrications of past scorecards | If a week's data is missing, write "no data" and link the gap |
| Append-only log | `wiki/log.md` gets 1 line, old entries untouched |

## Anti-patterns (do NOT)

| Anti-pattern | Why | Fix |
|---|---|---|
| Auto-write tactics to Notion without GO | HITL violation | Surface diff, wait |
| Generate a 5-page report A0 won't read | Token waste, format abuse | Cap at 80 lines |
| Mix cycle-close content into a weekly snapshot | Confused audience | Variant format per week number |
| Skip the "what blocked" section | Learn nothing, repeat blockers | Always include Y/RED items |
| Write "100% done" without proof | D1 violation — assertion | Paste the Notion row status |
| Reset scorecard to 0 at week boundary | Lose the cumulative view | Cycle progress section keeps it |

## See also

- `12weekyear.com` — official methodology
- `/l1-research-pulse` — the external research (12WY blog, etc.)
- `picard-audit-and-prod-workflow` — when a new 12WY cycle needs a PRD
- `wiki/reports/l1_snw_*.md` — accumulated weekly snapshots
- Notion `AGENT_REGISTRY_DB` — Sovereign sync (12WY database lives here)
