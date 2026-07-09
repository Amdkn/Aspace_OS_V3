---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 01-omk-business-os
surface_kind: QuickAccess Mirror
domain: Finance
b2_gatekeeper: Wonder Woman
squad: Thunderbolts
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Finance B3 Swarm Config - Thunderbolts

This folder configures the B3 swarm for the Finance domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Wonder Woman reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Red Hulk** - Budget pressure: Tests cost ceilings, burn limits, and margin pressure.
- **Taskmaster** - Accounting mirror: Tracks repeatable numbers and reconciles evidence.
- **Baron Zemo** - Strategy critic: Finds structural financial traps and bad incentives.
- **Ghost** - Leak detector: Finds hidden spend, leakage, waste, and model-usage drift.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.