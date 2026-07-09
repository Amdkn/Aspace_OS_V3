---
title: Tick Handoff (Symphony ↔ Hermes ↔ Trackers)
---

> The **4-zone boundary** of a Symphony tick. Mismatches here = the
> agent does the wrong work in the wrong place.

## The 4 zones

| Zone | Role | Can read | Can write | Triggered by |
|---|---|---|---|---|
| **Symphony** | Orchestrator, tick state machine, standards injection | All trackers (read), `agent-os/standards/index.yml` | `pulse.log` (its own), in-memory state | Task Scheduler cron, webhook, manual |
| **Tracker** (Airtable) | Source of truth, client/pipeline, finance | Itself (the DB) | Human-driven (UI); Symphony produces drafts only | Human, Airtable form, integration |
| **Hermes** (agent runtime) | Analyse, proof production, gate recommendation | Source tracker (read via Symphony), Notion SOP (read), context pack (read) | `proof_summary` to its own output buffer (Symphony then captures) | Symphony tick (EXECUTE phase) |
| **ClickUp** | Operational tasking (downstream of Airtable) | Itself | Human-driven (UI), Symphony draft only | Airtable record (recommendation), human |

## The handoff sequence

```
1. PROBE (Symphony)
   - Poll Airtable
   - Apply candidate-record-rule.md (9 criteria)
   - Skip records that fail (log not_eligible)

2. DECIDE (Symphony)
   - For each eligible record: build mission-contract.md
   - Inject relevant standards into agent prompt
   - Decide: dispatch this tick? (yes if ≤ N concurrent slots)

3. EXECUTE (Hermes, ephemeral)
   - Receive mission + standards
   - Read Airtable record (read-only)
   - Read Notion SOP via URL (read-only)
   - Read context pack via URL (read-only)
   - Produce expected_proof (4 types)
   - Emit gate_decision
   - Build writeback drafts (if any)

4. OBSERVE (Symphony)
   - Capture proof_summary from Hermes
   - Validate against forbidden-words.md
   - Validate against gate-decisions.md
   - Compute cost_delta_usd (input + output tokens × rates)

5. LEARN (Symphony)
   - Update cumulative metrics (per workflow)
   - If gate = BLOCKED and counter >= max_retries: trigger Donna DLQ

6. SIGNAL (Symphony)
   - Write pulse.log (this tick's 8 lines, JSON)
   - If gate = PASS or CONDITIONAL: write draft outputs to
     `.hermes/drafts/<record_id>.json` (A0 picks up in the morning)
   - If gate = BLOCKED: signal Donna + A0 (Telegram channel)

7. SLEEP (Symphony)
   - Increment tick counter
   - Wait for next tick (polling.interval_ms or webhook)
```

## Why 4 zones (not 3 or 2)

- **Symphony alone** = dumb scheduler (no proof)
- **Symphony + Hermes** = can produce proof, but writes are uncontrolled
- **Symphony + Hermes + Tracker (read-write)** = bi-sync nightmare
- **Symphony + Hermes + Tracker (read-only) + ClickUp (ops)** = clean
  separation, each zone has one job, A0 is the only writer

## Boundary violations to catch

- ❌ Hermes writing to Airtable directly (must go through Symphony
  draft)
- ❌ Symphony reading from ClickUp (not in scope of Airtable workflow)
- ❌ Airtable record linking to a Notion DB page that the tick also
  wants to write to (Notion is canon, read-only)
- ❌ Hermes calling another Hermes instance (no agent-to-agent comm
  outside Symphony bus)

## Cross-refs

- `mission-contract.md` — what crosses from Symphony to Hermes
- `expected-proof.md` — what crosses back from Hermes to Symphony
- `writeback-policy.md` — what crosses from Symphony to draft store
- `concept_shadow_l1_l2_heartbeat_symphony.md` (wiki) — heartbeat
  doctrine for the 8 phases
