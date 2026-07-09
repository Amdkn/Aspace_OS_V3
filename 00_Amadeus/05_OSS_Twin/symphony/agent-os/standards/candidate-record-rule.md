---
title: Candidate Record Rule (Airtable Filter)
---

> A Symphony tick may only dispatch a record that passes ALL of the
> following 9 criteria. One miss = record skipped, logged as
> `not_eligible` in pulse.log.

## The 9 criteria

| # | Airtable field | Requirement | Why |
|---|---|---|---|
| 1 | `Status` | `New Lead`, `Qualified`, `Proposal Sent`, or `In Production` | Terminal states are out of scope |
| 2 | `SOA Domain` | `Growth`, `Sales`, or `Finance` (L2-Airtable scope) | Other domains route to other workflows |
| 3 | `Name` / `Title` | Non-empty | Human-readable handle for A0 |
| 4 | `Description` / `Brief` | Non-empty OR a SOP linked | Agent needs context |
| 5 | `Build Gate` | Non-empty | Defines what PASS looks like |
| 6 | `Context Pack URL` OR `Notion SOP URL` | At least one | Executable context |
| 7 | `SLA Max Time` | Present, integer minutes | Axe temporel |
| 8 | `SLA Max Cost` | Present (or `0`) | Axe financier |
| 9 | `SLA Max Retries` | Present, integer | Axe qualitatif |

## Reject behavior

- Single failure: record **skipped**, not failed
- Logged in pulse.log as `phase: PROBE, decision: not_eligible,
  reason: <which criterion failed>`
- Skipped records get re-checked on next tick (state may have changed)
- **No Donna escalation** for skipped records (it's not a failure, it's
  a filter)

## Why this list

The 9 criteria = the minimum information for an agent to make a
**gate decision** (PASS/BLOCKED/CONDITIONAL). Missing any one = the
agent would have to guess, and guessing at the gate is a BLOCKED
scenario by definition.

## Where the check lives

- **PROBE phase** of every tick
- Per-tracker (Airtable, ClickUp, Notion all have their own 9-criteria
  variant, mapped from the canonical Symphony state machine)
- `before_dispatch` hook in WORKFLOW.md front matter

## Anti-patterns

- ❌ Loosening the criteria to "ship faster" — every loosened
  criterion = 1 future tick that will BLOCK on it
- ❌ Adding the criteria in the agent prompt instead of the PROBE phase
  (the agent might forget to check)
- ❌ Silently passing a record that fails 1 criterion — silent failures
  destroy A0's trust in the bus

## Cross-refs

- `mission-contract.md` — fields 7-9 (SLA triple) come from criteria 7-9
- `soa-routing.md` — criterion 2 (SOA Domain) feeds the routing table
- `gate-decisions.md` — what happens when the record IS eligible
