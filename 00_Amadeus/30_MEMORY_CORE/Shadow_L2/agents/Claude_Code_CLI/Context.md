---
source: Shadow_L2
date: 2026-05-19
type: agent-context
agent: Claude_Code_CLI
layer: L2
---

# Context.md — Claude Code L2 Runtime Pointer

```yaml
current_mission: null
current_turn: 0
rotation_index: 0      # for 3 rotating checks (Heartbeat §4)
last_tick_ts: null
last_tick_signal: null
last_alert_anomaly: null
last_alert_ts: null
backoff_active: false
backoff_until: null
```

> Mis à jour par `heartbeat-tick-l2.ps1` à chaque OBSERVE phase.
> Reset manuel autorisé si corruption.
