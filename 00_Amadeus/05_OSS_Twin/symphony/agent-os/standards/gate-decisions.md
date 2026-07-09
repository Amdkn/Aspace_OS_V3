---
title: Gate Decisions
---

> Every Symphony tick ends with **exactly one** gate decision. The
> decision is the agent's contract with A0 — no "I'll do it later".

## Three values

| Decision | Meaning | What happens next |
|---|---|---|
| **PASS** | Business gate satisfied, proof exists, no forbidden output. | Status → `Done`. Optional writeback (per `writeback-policy.md`). |
| **BLOCKED** | Missing client input, access, legal/finance decision, or external approval. | Status → `Waiting`. Donna DLQ hook fires if no progress in 24h. |
| **CONDITIONAL** | Partial proof exists, but the client/pipeline state is not ready to advance. | Status → `In Progress` with `blocker_notes`. Re-tick when state changes. |

## Strictness

- `PASS` is a **commitment**. If the agent says PASS but the proof is
  later found invalid, the agent loses greenlight trust for 7 days.
- `BLOCKED` MUST name the blocker (`access`, `input`, `legal`,
  `finance`, `approval`, `external`). Unnamed blockers = `CONDITIONAL`.
- `CONDITIONAL` MUST include a re-trigger condition ("re-poll when
  Status → X" or "wait for `context_pack_url` update").

## Gate status field (Airtable)

| Symphony decision | Airtable `Gate Status` |
|---|---|
| PASS | `PASS` |
| BLOCKED | `BLOCKED` |
| CONDITIONAL | `CONDITIONAL` (with blocker_notes in `Risk & Blocker Notes`) |

## Why 3 values (not 2)

`PASS/FAIL` is too coarse — most real-world business gates are
"yes-but-with-conditions" (e.g., proposal valid only if client signs by
Friday). `CONDITIONAL` captures that without forcing the agent to
fabricate a `PASS`.

## Anti-patterns

- ❌ Defaulting to `PASS` to make the gate look healthy
- ❌ Defaulting to `BLOCKED` to defer responsibility
- ❌ `CONDITIONAL` without re-trigger condition (= lazy `BLOCKED`)
- ❌ Two values in one tick (one tick = one decision, period)

## Cross-refs

- `mission-contract.md` — `build_gate` defines what PASS looks like
- `writeback-policy.md` — what writes each decision permits
- `donna-dlq.md` — escalation after threshold_failed_attempts
