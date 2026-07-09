---
id: B3_WARP_CORE_LEAD_LAG_LOG_TEMPLATE
layer: L2_Business_Pulse
status: SHADOW_ACTIVE
created: 2026-05-21
---

# B3 Warp Core Execution - Lead/Lag Log Template

B3 executes tactics and records proof. B3 does not own the Rock.

## Execution Log

```yaml
date: YYYY-MM-DD
summer_project: ""
domain: Growth|Sales|Product|Ops|IT|Finance|People|Legal
rock_id: ""
tactic_id: ""
b3_squad: ""
lead_measure_done: true|false
lag_measure_delta: ""
artifact_path: "C:\\..."
blocker: ""
next_action: ""
```

## Lead vs Lag

| Type | Meaning |
|---|---|
| Lead | Action under control this week |
| Lag | Result observed after action |

## Completion Rule

A tactic is not complete until an artifact path, measurable result, or blocker note exists.
