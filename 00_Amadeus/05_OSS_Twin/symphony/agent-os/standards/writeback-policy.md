---
title: Writeback Policy
---

> What a Symphony tick is allowed to write back to the source tracker.
> **Default: read-only**. Writes are exceptional, gated, draft-only.

## Default posture

```yaml
writeback_policy:
  external_write_requires_greenlight: true
  allowed_draft_outputs:
    - airtable_update_draft
    - clickup_task_draft
    - proof_summary
    - status_recommendation
```

- `external_write_requires_greenlight: true` = NO direct write to the
  source tracker. The agent produces a **draft** for A0 to review.
- `allowed_draft_outputs` = the 4 shapes the agent may produce. Anything
  else = `BLOCKED` with `error: "writeback_not_in_allowlist"`.

## The 4 allowed draft outputs

### 1. `airtable_update_draft`

A **proposed** Airtable PATCH that would update one or more fields.
The draft includes:
- `record_id` (target)
- `fields` (the proposed change, JSON-shaped)
- `reasoning` (why this update)
- `human_approval_required: true`

**Never auto-applied.** A0 (or a designated approver) reviews and
applies via the Airtable UI, not via Symphony.

### 2. `clickup_task_draft`

A proposed new ClickUp task (when the workflow decides the action
should be operational, not client-facing). Same approval gate as #1.

### 3. `proof_summary`

The full 4-type proof (per `expected-proof.md`), written to the
agent's output buffer. This is the **primary** output, not a "draft".

### 4. `status_recommendation`

A recommended `Status` value (e.g., `Qualified` → `Proposal Sent`).
This is a **recommendation**, never an auto-transition. Status changes
in Airtable are human-driven.

## What is NOT in the allowlist (and why)

- ❌ `airtable_record_create` — Symphony doesn't create new records
  (would require bi-sync semantics, blocked for v1)
- ❌ `airtable_record_delete` — irreversible, human-only
- ❌ `notion_database_write` — Notion is canon (read + capture
  post-proof), not writable from a tick
- ❌ `supabase_write` — out of scope for this workflow (Supabase is
  the L2 IT adapter, not L2 Growth)
- ❌ `email_send` — A0 sends emails, not agents

## Why draft-only

Two reasons:

1. **Trust** — A0 doesn't trust agents to write production data yet.
   Drafts let A0 see the proposed change in human-readable form.
2. **Audit** — every write should have a human in the loop. Drafts
   preserve the audit trail (`reasoning` + `human_approval_required`).

## When the greenlight gets relaxed (future)

Not in scope for v1. If/when Symphony proves itself (3 weeks
consecutive usage, < 5% Donna escalations, zero workspace orphans per
SDD-008 §4 graduation MUSE), the policy can move to
`external_write_requires_greenlight: false` per-workflow. NOT before.

## Anti-patterns

- ❌ Auto-applying `airtable_update_draft` "because A0 is sleeping"
  — even at night, A0 reviews in the morning
- ❌ Adding new output types to `allowed_draft_outputs` without a new
  ADR (each new type is a write surface, must be ratified)
- ❌ Putting the draft in `pulse.log` only (= invisible to the
  Airtable UI)

## Cross-refs

- `mission-contract.md` — `writeback_policy` field
- `gate-decisions.md` — `PASS` permits draft outputs; `BLOCKED` does
  not
- `expected-proof.md` — `proof_summary` is the primary output
