---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 03_RILCOT
surface_kind: QuickAccess Mirror
domain: Product
b2_gatekeeper: Flash
squad: Avengers
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Product B3 Swarm Config - Avengers

This folder configures the B3 swarm for the Product domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Flash reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Captain America** - Quality anchor: Defines user-facing acceptance and prevents sloppy shipping.
- **Iron Man** - Builder: Turns the JTBD into working product artifacts.
- **Thor** - Release force: Pushes deliverables across the finish line and stress-tests impact.
- **Black Widow** - Research and edge cases: Finds hidden constraints, competitors, and failure modes.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.