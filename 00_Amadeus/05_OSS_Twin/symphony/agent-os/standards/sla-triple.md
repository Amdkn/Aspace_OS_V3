---
title: SLA Triple (Temporal · Financier · Qualitatif)
---

> Per SDD-009 §2.3, every Symphony tick is constrained by a
> 3-axis SLA. **The agent MUST stop and signal if any axis is exceeded**.

## The three axes

```yaml
sla:
  max_minutes: <int>      # Axe temporel (wall-clock tick duration)
  max_cost_usd: <float>   # Axe financier (cumulative compute cost)
  max_retries: <int>      # Axe qualitatif (failed attempts before Donna DLQ)
```

## Axe temporel — `max_minutes`

- Measured from `tick_start_ts` to `tick_end_ts` (both UTC ISO-8601)
- Includes all 8 phases (WAKE→SLEEP), not just EXECUTE
- Exceeded = `Stalled` state, kill worker, log to pulse.log, attempt
  re-tick with backoff (symphony-base.spec.md §7.3)

## Axe financier — `max_cost_usd`

- Cumulative across all retries of the same issue_id
- Per-tick budget check at every turn (not just end-of-tick)
- Exceeded = `Failed` state with `error: "budget_exceeded"`, no
  re-tick (would re-burn budget). Donna DLQ hook fires.

**Reference rates** (symphony-base.spec.md §9.4) :

| Provider | Input/1M | Output/1M | Usage |
|---|---|---|---|
| Claude Sonnet 4.5 | $3.00 | $15.00 | Rick A1 critique |
| **MiniMax 2.7** | $0.30 | $1.20 | **Default A3** |
| **GLM 4.7 Flash** | $0.05 | $0.20 | **Fallback frugal** |
| GPT-4o | $2.50 | $10.00 | Évité |

## Axe qualitatif — `max_retries`

- Per-issue counter, not per-tick
- On each `Failed` / `TimedOut` / `Stalled` / `CanceledByReconciliation`:
  counter++, attempt re-tick
- Counter >= `max_retries` = Donna DLQ escalation (per
  `donna_dlq.threshold_failed_attempts` in workflow YAML)

## Budget gate (per turn)

```
after every model call:
  cumulative_cost_usd += (input_tokens × input_rate) + (output_tokens × output_rate)
  if cumulative_cost_usd > sla.max_cost_usd:
    kill worker, mark Failed, signal Donna
```

## Why 3 axes (not 1 deadline)

A single `deadline_minutes` hides cost explosions and retry storms.
The 3-axis model makes tradeoffs explicit:
- A 10-min `max_minutes` with `max_cost_usd: 0.50` says "be quick AND
  frugal" — different from "be quick, cost is no object"
- `max_retries: 3` vs `max_retries: 10` is a different policy for the
  same temporal/financial budget

## Anti-patterns

- ❌ `max_minutes: 9999` (= no constraint) — defeats the purpose
- ❌ Forgetting the cost check at per-turn granularity
- ❌ Re-trying after Donna DLQ fires (the DLQ decision is final)

## Cross-refs

- `mission-contract.md` — `sla` object
- `donna-dlq.md` — escalation after `max_retries`
- SDD-009 §2.3 (SLA Triade)
- symphony-base.spec.md §9.4 (Coût Compute)
