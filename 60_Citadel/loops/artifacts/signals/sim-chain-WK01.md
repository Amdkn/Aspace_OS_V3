---
type: signal
status: open
tag: sim-chain
sources: [cron/wf3_sim_runner.py]
seen: 1
wk: 1
chain_verdict: CHAIN_SOUTENABLE
run_id: 2026-07-08T14:42:07-04:00-63f137
---
# sim-chain-WK01 — chain verdict MiroFish (W29)

Composition (3 sims, AND) :
- WF0 (state machine) = **GREEN** — receipt: 15_airlock.json
- WF1 (schedule) = **OK** (8t, 8.00/wk) — receipt: worklog.md
- WF2/L2 (queue) = **SOUTENABLE** (8) "— receipt: sim-cadence-x4.md (W28 L2 stress probe)

**Chain verdict : CHAIN_SOUTENABLE**
Reasons : aucune

## Timeline
- [2026-07-08T14:42:07-04:00] [wf3-chain] rid=2026-07-08T14:42:07-04:00-63f137 verdict=CHAIN_SOUTENABLE · wf0=GREEN · wf1=OK(8t/8.00/wk) · wf2=SOUTENABLE(8) · reasons=OK
- [2026-07-08T14:42:55-04:00] [wf3-chain] rid=2026-07-08T14:42:55-04:00-1bca95 verdict=CHAIN_SOUTENABLE · wf0=GREEN · wf1=OK(8t/8.00/wk) · wf2=SOUTENABLE(8) · reasons=OK
- [2026-07-08T14:46:51-04:00] [wf3-chain] rid=2026-07-08T14:46:51-04:00-e8e2f6 verdict=CHAIN_UNKNOWN · wf0=UNKNOWN · wf1=OK(8t/8.00/wk) · wf2=SOUTENABLE(9) · reasons=OK
- [2026-07-08T14:50:01-04:00] [wf3-chain] rid=2026-07-08T14:50:01-04:00-d01352 verdict=CHAIN_SOUTENABLE · wf0=GREEN · wf1=OK(8t/8.00/wk) · wf2=SOUTENABLE(9) · reasons=OK
