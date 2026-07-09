# state.json Schema (aspace-l2-state-v1)

**Path** : `00_Summers_Verse/state/state.json`
**Owner** : B1-Jerry-E-Myth (write access) + all B2 Heroes (read+write their domain) + A0 Mavis (read+escalate)
**Lock** : file-level (1 writer at a time — use atomic write pattern if concurrent)

## Structure

| Field | Type | Written by | Read by |
|---|---|---|---|
| `cycle.current` | string | manual | all |
| `cycle.week` | string | manual | all |
| `b1_jerry.pulse` | enum (INIT/GREEN/YELLOW/RED) | B1-Jerry daily-cycle-reset | A0, B1-Summers |
| `b1_jerry.drift_flag` | boolean | B1-Jerry (when >2 B2 missing) | A0 |
| `b2_pulse.<domain>.status` | enum | B2 Hero daily-pulse | B1-Jerry |
| `b2_pulse.<domain>.friction_today` | string | B2 Hero daily-pulse | B1-Jerry evening |
| `b2_pulse.<domain>.b3_dispatch_id` | string | B2 Hero daily-pulse | B3 sub-agent |
| `b2_pulse.<domain>.bandwidth_h` | float | B2 Hero daily-pulse | B1-Jerry evening D11 |
| `b1_evening_pulse.*` | object | B1-Jerry evening-d11 | A0 |
| `weekly_review.*` | object | B1-Summers weekly-rocks-leadlag | A0 |
| `drift_flag` | boolean | any (boolean OR over b1_jerry.drift_flag) | A0 |
| `escalation_log[]` | array of objects | any | A0 |
| `loop_audit.*_runs` | counter | auto-incremented on each cron tick | A0 (observability) |

## Write Protocol (atomic, Posture C)

1. Read full state.json
2. Modify in memory
3. Write to `state.json.tmp`
4. Rename `state.json.tmp` -> `state.json` (atomic on POSIX, near-atomic on NTFS)

## Failure Modes

- File missing -> create with INIT defaults (first-run)
- File >50KB -> rotate to `state.json.prev` + warn (drift = bloated state)
- Concurrent write -> retry 3x with backoff 100/300/900ms (D6 lesson learned from L1 §23.1)

## DRY-Canon

- `plan-L2 §4.2` (bijection 8↔8 LD↔BD) — field naming reflects bijection
- `plan-L2 §5.4` (matrice lean Filiales) — `b1_summers.icp_active` reflects wave 01 Coach
- `plan-L0 §11` (héritage SSOT) — same atomic write pattern as Life OS state.json
- `plan-A0-L §5 D3` — 12WY reorg trigger uses `loop_audit.12wy_reorg_prompts` as audit trail

## Evolution Path

- v1.0 (current) — flat structure, 8 B2 domains
- v1.1 (Q4 2026) — nested by ICP variant when Filiales >1 active
- v2.0 (Q1 2027) — Hermes-shared state via .hermes/_ssot_claude/ (L0 §11)
