---
source: Shadow_L0
date: 2026-05-18
type: workflow
status: ACTIVE
domain: Shadow_L0 / Symphony / Task_Lifecycle
anchors:
  - Symphony WORKFLOW.md (https://github.com/openai/symphony/blob/main/SPEC.md)
  - SDD-002_a1-rick-harness.md §6 (program.md format)
tags: [#Workflow, #Symphony, #Mission, #ShadowL0]
---

# Shadow_L0 / WORKFLOW.md — Canonical Task Lifecycle

> The implicit workflow A0 follows when shipping a mission, now made explicit.
> Symphony pattern : workflow doc + mission card + multi-turn continuation.
> Every Shadow L0 CLI reads this on Turn 1 to know "what shape a mission takes".

## 1. Mission Card Format (program.md per SDD-002 §6)

A mission card is a single markdown file dropped in `agents/<CLI>/memory/inbox/`. Format :

```markdown
---
mission_id: <kebab-case-slug>
issued_at: <ISO-8601 UTC>
issued_by: <A0 | Claude_Code | Codex | Gemini>
target_cli: <Codex_CLI | Gemini_CLI | Claude_Code_CLI>
on_behalf_of: <e.g. 13th_Doctor.Yaz>     # Companion identity, not the CLI
type: <DDD | ADR | PRD | SDD | skill | enrich | research | infra | refactor>
priority: <H1 | H3 | H10 | H30 | H90>     # Horizon per A0 doctrine
turns_budget: 20                          # Symphony default
autonomy: <auto | signoff | escalate>
related_skills: [/pp-cli-install, /airtable-enrich, ...]
---

# <Mission Title>

## Intent
<1-3 sentences from A0 — the why>

## Constraints
- <bounded, falsifiable>
- <e.g. "no PATCH on prod Airtable without --dry-run first">

## Inputs
- <files / wiki pages / URLs / API endpoints to read>

## Acceptance Criteria
- [ ] <verifiable outcome 1>
- [ ] <verifiable outcome 2>

## Out of Scope
- <what NOT to touch>

## Terminal Markers (CLI must emit one to end mission)
- `<DONE>` — all acceptance criteria met
- `<NEEDS_REVIEW>` — partial, A0 must inspect outbox
- `<ESCALATE>` — blocked, reason in body
```

## 2. Lifecycle (state machine)

```
   inbox/<mission-id>.md
            │  (Task Scheduler tick fires)
            ▼
   ┌─────────────────────────┐
   │  PROBE                  │
   │  - mission card valid?  │
   │  - turns_budget left?   │
   │  - autonomy gate?       │
   └──────────┬──────────────┘
              │
       ┌──────┴──────┐
       ▼             ▼
   AUTO_OK       SIGNOFF_REQUIRED
       │             │
       │             └──→ move to A0's inbox, exit
       ▼
   ┌─────────────────────────┐
   │  EXECUTE Turn 1         │  ← render Workflow.md with mission card
   │  (full context prompt)  │
   └──────────┬──────────────┘
              ▼
   outbox/<mission-id>/turn-1.md (+ turn-1.err if stderr)
              │
              ▼
   ┌─────────────────────────┐
   │  OBSERVE                │  ← parse for terminal marker
   │  - <DONE>?              │
   │  - <NEEDS_REVIEW>?      │
   │  - <ESCALATE>?          │
   │  - none → continuation  │
   └──────────┬──────────────┘
              │
        ┌─────┴─────┐
        ▼           ▼
    Terminal      Continue
        │           │
        │           ▼
        │      ┌─────────────────────────┐
        │      │  EXECUTE Turn N+        │  ← render Continuation.md (minimal)
        │      │  N <= 20 (Symphony cap) │
        │      └──────────┬──────────────┘
        │                 │ (loop back to OBSERVE)
        ▼                 │
   ┌─────────────────────────┐
   │  TERMINAL               │
   │  <DONE>         → LEARN │
   │  <NEEDS_REVIEW> → GATE  │
   │  <ESCALATE>     → ALERT │
   │  Turn = 20      → CAP   │
   └─────────────────────────┘
```

## 3. Per-state Actions

### PROBE (validation gate)

- Check mission card frontmatter has all required fields
- Verify `turns_budget > 0` (re-tick decrements)
- Match `type` against agent's `autonomy_scope` in Agent.md
- If `autonomy: signoff` or missing match → move outbox to A0's inbox, exit cleanly with `HEARTBEAT_GATE`

### EXECUTE Turn 1 (full context render)

Prompt template (rendered by `heartbeat-tick.ps1`) :

```
<<<SOUL>>>
{content of Soul.md}
<<</SOUL>>>

<<<MISSION>>>
{content of inbox/<mission-id>.md}
<<</MISSION>>>

<<<TOOLS>>>
{content of Tools.md (capability surface)}
<<</TOOLS>>>

<<<STATE>>>
Turn: 1 of {turns_budget}
Prior outputs: none
Current wiki log tail: {tail -5 of LLM_Wiki/wiki/log.md}
<<</STATE>>>

<<<INSTRUCTIONS>>>
Execute the mission. Write your work output, NOT chatter.
Emit exactly one terminal marker at the end:
  <DONE>         — all acceptance criteria met
  <NEEDS_REVIEW> — partial; need A0 review of outbox
  <ESCALATE>     — blocked; describe blocker in <ESCALATE_REASON> block
If neither possible after this turn, omit marker and the next turn will continue.
<<</INSTRUCTIONS>>>
```

### EXECUTE Turn N+ (minimal continuation)

```
<<<CONTINUE_MISSION>>>
Mission: {mission_id} — Turn {N} of {turns_budget}
Workspace: see {outbox/<mission-id>/}
Last output: {outbox/<mission-id>/turn-{N-1}.md}
Last context: {Context.md current state}
<<</CONTINUE_MISSION>>>

<<<INSTRUCTIONS>>>
Continue where you left off. Read your last turn output first.
Same terminal markers apply.
<<</INSTRUCTIONS>>>
```

### OBSERVE

Regex check on the new `outbox/<mission-id>/turn-N.md` :
- `\<DONE\>` → trigger LEARN
- `\<NEEDS_REVIEW\>` → trigger GATE
- `\<ESCALATE\>` → trigger ALERT, parse `<ESCALATE_REASON>...</ESCALATE_REASON>`
- None of the above + Turn < budget → write Context.md "in-progress, next turn = N+1", exit

### LEARN (terminal `<DONE>`)

1. Distill outbox into `memory/YYYY-MM-DD.md` (one-paragraph summary)
2. Append entry to `LLM_Wiki/wiki/log.md` :
   ```
   ## [YYYY-MM-DD] <type> | <mission_id> - <one-line outcome>
   <2-3 sentences>
   **Artifacts**: <outbox files>
   **Acted on behalf of**: <Doctor.Companion>
   ```
3. Move mission card from `inbox/` to `inbox/.done/` (preserve audit trail)
4. If pattern detected (3+ similar missions) → append candidate to `skills_queue.md`

### GATE (terminal `<NEEDS_REVIEW>`)

1. Move `outbox/<mission-id>/` to `agents/A0_inbox/` (A0 owns the review)
2. Leave mission card in source `inbox/` until A0 signs off
3. Append `pulse.log` : `HEARTBEAT_GATE | <mission_id> | awaiting-A0`

### ALERT (terminal `<ESCALATE>`)

1. Write reason to `memory/rejections.log`
2. If reason matches a known recoverable pattern (rate-limit, tool not found, etc.) → schedule retry per `Heartbeat.md` cooldown rules
3. Otherwise → notify A0 via TBD channel (telegram MCP / file in A0 inbox)
4. Append `pulse.log` : `HEARTBEAT_FAIL | <mission_id> | <reason>`

### CAP (Turn = 20 limit hit)

1. Mission unsuccessful, mark `outbox/<mission-id>/CAP_REACHED`
2. Append `pulse.log` : `HEARTBEAT_CAP | <mission_id> | turns-exhausted`
3. Treat as ESCALATE (A0 review)

## 4. Inter-Agent Handoff

When agent A finishes a mission whose follow-up needs agent B :

1. A writes `outbox/<mission-id>/handoff-to-B.md` with the next mission card
2. A's tick.ps1 copies it to `agents/<B>/memory/inbox/`
3. B's next tick picks it up
4. Append `pulse.log` : `HEARTBEAT_HANDOFF | from=A | to=B | mission=<mission_id>`

This is the file-based equivalent of Symphony's "agent handoff" — no IPC, no shared memory.

## 5. Mission Card Examples

### Example 1 — Codex L0 infra mission (autonomy: auto)

```markdown
---
mission_id: register-heartbeat-tasks-2026-05-18
issued_at: 2026-05-18T15:00:00Z
issued_by: Claude_Code
target_cli: Codex_CLI
on_behalf_of: 13th_Doctor.Yaz
type: infra
priority: H1
turns_budget: 5
autonomy: auto
---

# Register Heartbeat Tasks in Windows Task Scheduler

## Intent
Create 4 scheduled tasks (1 per Shadow L0 CLI + 1 watchdog) calling heartbeat-tick.ps1.

## Constraints
- User scope only (no admin)
- 15-min cadence work-hours for 3 agent ticks, 5-min always for watchdog

## Acceptance Criteria
- [ ] schtasks /Query shows 4 new tasks named "ASpace-Heartbeat-*"
- [ ] First fire produces a pulse.log entry per agent

## Terminal Markers
- `<DONE>` after schtasks /Query verification
```

### Example 2 — Gemini L2 forge mission (autonomy: auto)

```markdown
---
mission_id: scaffold-skill-airtable-outreach-2026-05-18
target_cli: Gemini_CLI
on_behalf_of: 12th_Doctor.Bill
type: skill
priority: H3
turns_budget: 10
autonomy: signoff
---

# Scaffold the /airtable-outreach skill

## Intent
Draft the SKILL.md + scripts/outline for a skill that drafts personalized outreach emails per enriched lead.

## Inputs
- Existing /airtable-enrich skill as reference
- archetype-signals.md for tone-per-archetype

## Acceptance Criteria
- [ ] SKILL.md frontmatter ready for /skill-creator
- [ ] scripts/draft-outreach.ps1 outline (not full impl)

## Terminal Markers
- `<NEEDS_REVIEW>` (autonomy=signoff means A0 reviews before /skill-creator invocation)
```

## 6. Inbounds

- `Shadow_L0/HEARTBEAT_PROTOCOL.md`
- `Shadow_L0/SPEC.md`
- `agents/Codex_CLI/Workflow.md` (CLI-specific override layer)
- `agents/Gemini_CLI/Workflow.md`
- `agents/Claude_Code_CLI/Workflow.md`
