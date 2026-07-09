---
title: pulse.log Schema (Symphony 8-Phase Observability)
---

> The observability layer of a Symphony tick. 1 line per phase, 8
> lines per tick. Append-only JSONL. UTC ISO-8601 timestamps.

## File location

```
agent-os/pulse.log
```

- Per project (symphony install root)
- Append-only (never rewrite, never delete lines)
- Rotated weekly by A'Space's existing log rotation (cf. SDD-001 §6.3)

## Per-line schema

```json
{
  "ts": "2026-06-06T18:30:00.123Z",
  "tick_id": "solaris-airtable-clients-2026-06-06T18-30-00",
  "workflow_id": "solaris-airtable-clients",
  "issue_id": "recXYZ123",
  "phase": "WAKE|PROBE|DECIDE|EXECUTE|OBSERVE|LEARN|SIGNAL|SLEEP",
  "duration_ms": 145,
  "standards_injected": ["mission-contract.md", "soa-routing.md", "gate-decisions.md"],
  "decision": "...",
  "evidence_url": null,
  "cost_delta_usd": 0.002,
  "cumulative_cost_usd": 0.127,
  "aspace_layer": "L2",
  "soc_target_domain": "Growth",
  "error": null
}
```

## Field semantics

| Field | Type | Always present? | Notes |
|---|---|---|---|
| `ts` | ISO 8601 UTC | yes | Timestamp of the phase START |
| `tick_id` | string | yes | `<workflow_id>-<UTC ts minute-precision>` |
| `workflow_id` | string | yes | e.g. `solaris-airtable-clients` |
| `issue_id` | string | WAKE/SLEEP only absent (no record yet/anymore) | e.g. `recXYZ123` |
| `phase` | enum | yes | One of 8 (see below) |
| `duration_ms` | int | yes | How long the phase took |
| `standards_injected` | string[] | DECIDE/EXECUTE/OBSERVE | Which standards from index.yml were used |
| `decision` | string | PROBE/DECIDE/OBSERVE/SIGNAL | Free text, ~1 line |
| `evidence_url` | string | EXECUTE/OBSERVE/SIGNAL | Notion SOP, Airtable record, etc. |
| `cost_delta_usd` | float | EXECUTE/OBSERVE | Tokens spent this phase |
| `cumulative_cost_usd` | float | EXECUTE/OBSERVE/SIGNAL/SLEEP | Running total per tick |
| `aspace_layer` | enum L0/L1/L2 | yes | The layer this tick is for |
| `soc_target_domain` | string | DECIDE onwards | The SOA domain (Growth, Sales, …) |
| `error` | string | only on failure | Nullable. `error: null` if all good. |

## The 8 phases

| # | Phase | Purpose | Typical duration | Key output |
|---|---|---|---|---|
| 1 | **WAKE** | Tick start, read index.yml, log intent | <50ms | tick_id, layer |
| 2 | **PROBE** | Poll tracker, apply 9-criterion filter | 1-3s | eligible issue_ids |
| 3 | **DECIDE** | For each eligible, build mission contract, select standards | 100-300ms | standards_injected |
| 4 | **EXECUTE** | Run agent (Hermes/Codex/Claude Code), build proof | 30s-5min | proof_summary |
| 5 | **OBSERVE** | Validate proof, check lexique, compute cost | 100-500ms | gate_decision |
| 6 | **LEARN** | Update metrics, check Donna DLQ threshold | 10-50ms | cumulative metrics |
| 7 | **SIGNAL** | Write drafts, notify A0 (Telegram), update tracker | 50-200ms | writeback_drafts |
| 8 | **SLEEP** | Tick end, increment counter, wait for next | <10ms | tick_summary |

## Example — one full tick (8 lines)

```jsonl
{"ts":"2026-06-06T18:30:00.000Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","phase":"WAKE","duration_ms":12,"aspace_layer":"L2","decision":"index.yml loaded, 10 standards available"}
{"ts":"2026-06-06T18:30:00.012Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","phase":"PROBE","duration_ms":1234,"aspace_layer":"L2","decision":"polled 42 records, 3 eligible, 39 not_eligible","error":null}
{"ts":"2026-06-06T18:30:01.246Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","issue_id":"recXYZ123","phase":"DECIDE","duration_ms":87,"aspace_layer":"L2","soc_target_domain":"Growth","standards_injected":["mission-contract.md","soa-routing.md","gate-decisions.md","forbidden-words.md","sla-triple.md","expected-proof.md","writeback-policy.md"],"decision":"dispatch to orchestrator (Superman) + researcher + strategist","error":null}
{"ts":"2026-06-06T18:30:01.333Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","issue_id":"recXYZ123","phase":"EXECUTE","duration_ms":4521,"aspace_layer":"L2","soc_target_domain":"Growth","standards_injected":["mission-contract.md","gate-decisions.md","expected-proof.md"],"evidence_url":"https://airtable.com/...","cost_delta_usd":0.012,"cumulative_cost_usd":0.012,"decision":"proof built (4/4 types)","error":null}
{"ts":"2026-06-06T18:30:05.854Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","issue_id":"recXYZ123","phase":"OBSERVE","duration_ms":203,"aspace_layer":"L2","soc_target_domain":"Growth","standards_injected":["forbidden-words.md","gate-decisions.md"],"cost_delta_usd":0.003,"cumulative_cost_usd":0.015,"decision":"lexique clean, gate=PASS","error":null}
{"ts":"2026-06-06T18:30:06.057Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","issue_id":"recXYZ123","phase":"LEARN","duration_ms":15,"aspace_layer":"L2","soc_target_domain":"Growth","cumulative_cost_usd":0.015,"decision":"cumulative metrics updated, no Donna escalation (1/3 retries)","error":null}
{"ts":"2026-06-06T18:30:06.072Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","issue_id":"recXYZ123","phase":"SIGNAL","duration_ms":78,"aspace_layer":"L2","soc_target_domain":"Growth","cumulative_cost_usd":0.015,"evidence_url":"https://airtable.com/...","decision":"drafts written: 1x airtable_update_draft, 1x proof_summary","error":null}
{"ts":"2026-06-06T18:30:06.150Z","tick_id":"solaris-airtable-clients-2026-06-06T18-30-00","workflow_id":"solaris-airtable-clients","phase":"SLEEP","duration_ms":3,"aspace_layer":"L2","cumulative_cost_usd":0.015,"decision":"tick complete, total_duration_ms=6150","error":null}
```

## Why this exact schema

- **Per-line JSON** = one phase = one line, easy to grep, easy to load in
  any tool
- **`duration_ms` per phase** = reveals bottlenecks (which phase eats
  the budget)
- **`standards_injected` per phase** = reveals which standards actually
  fired (validate the injection logic)
- **`cost_delta_usd` + `cumulative_cost_usd`** = budget guardrails
  visible in real time
- **`aspace_layer` always present** = easy filtering by L0/L1/L2
- **`error: null` always present** = tooling can grep `"error": "..."`
  to find failures

## Anti-patterns

- ❌ Free-form text logs (no structure) — unparseable
- ❌ One giant JSON for the whole tick — loses the per-phase signal
- ❌ Non-UTC timestamps (or local time without TZ) — desync across
  capsules
- ❌ Pulse.log in `/tmp/` or other ephemeral path — lost on restart
- ❌ Rewriting lines in place (e.g. updating `cumulative_cost_usd`
  on each phase) — kills the audit trail

## Tooling (future)

- `symphony-tail` — pretty-print last N ticks (think `tail -f` +
  color by phase)
- `symphony-cost` — aggregate cost per workflow / per day
- `symphony-bottleneck` — histogram of `duration_ms` per phase
- `symphony-errors` — grep `error != null` lines

## Cross-refs

- `tick-handoff.md` — what each phase does in 4-zone boundary
- `sla-triple.md` — cost_per_turn check at EXECUTE/OBSERVE
- ADR-SYMPH-001 §D3 (the 8 phases)
- symphony-base.spec.md §12 (logging doctrine)
