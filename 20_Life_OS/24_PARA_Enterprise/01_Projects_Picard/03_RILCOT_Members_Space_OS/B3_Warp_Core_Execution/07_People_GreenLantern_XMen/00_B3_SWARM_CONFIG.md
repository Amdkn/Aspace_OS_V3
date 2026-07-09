---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 03_RILCOT
surface_kind: QuickAccess Mirror
domain: People
b2_gatekeeper: Green Lantern
squad: X-Men
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# People B3 Swarm Config - X-Men

This folder configures the B3 swarm for the People domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Green Lantern reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Professor X** - People vision: Aligns roles, load, and learning with mission.
- **Cyclops** - Field lead: Coordinates execution discipline and team focus.
- **Jean Grey** - Empathy sensor: Detects overload, conflict, and communication risk.
- **Beast** - Knowledge keeper: Turns lessons into training, playbooks, and reusable memory.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.