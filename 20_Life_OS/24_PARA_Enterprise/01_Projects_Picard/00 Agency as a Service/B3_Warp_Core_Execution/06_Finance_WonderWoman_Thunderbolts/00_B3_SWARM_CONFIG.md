---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 00_Agency_aaS
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

## Members (canon Notion AGENT_REGISTRY_DB — 6)

- **Bucky Barnes** - Cashflow discipline (lead).
- **Yelena Belova** - Forecasting.
- **Red Guardian** - Reporting.
- **Ghost** - Cost optimization: finds hidden spend, leakage, model-usage drift.
- **Taskmaster** - Reproductibilité comptable: tracks repeatable numbers, reconciles evidence.
- **U.S. Agent** - Compliance fiscale.

> Canon roster: `../../B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md`.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.