---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 04_Alikaly
surface_kind: QuickAccess Mirror
domain: Growth
b2_gatekeeper: Superman
squad: Guardians
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Growth B3 Swarm Config - Guardians

This folder configures the B3 swarm for the Growth domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Superman reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Star-Lord** - Narrative scout: Frames ICP and message hypotheses; opens field exploration.
- **Rocket** - Experiment engineer: Builds fast channel tests, scrapers, ads, and measurement hacks.
- **Gamora** - Pipeline sentinel: Cuts weak leads, validates fit, and protects CRM hygiene.
- **Groot** - Brand memory: Keeps tone, assets, and reusable brand primitives consistent.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.