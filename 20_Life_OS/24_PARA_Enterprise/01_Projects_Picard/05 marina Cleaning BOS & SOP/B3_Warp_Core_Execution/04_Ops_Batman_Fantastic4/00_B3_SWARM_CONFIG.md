---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 05_Marina
surface_kind: QuickAccess Mirror
domain: Ops
b2_gatekeeper: Batman
squad: Fantastic Four
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Ops B3 Swarm Config - Fantastic Four

This folder configures the B3 swarm for the Ops domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Batman reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Mr Fantastic** - System architect: Turns messy delivery into repeatable operating design.
- **Invisible Woman** - Documentation shield: Makes SOPs, checklists, and handoffs usable.
- **The Thing** - Stability tester: Finds what breaks under load and routine use.
- **Human Torch** - Cycle accelerator: Removes drag without burning the process down.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.