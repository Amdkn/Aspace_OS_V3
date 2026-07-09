---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 00_Summers_Verse
surface_kind: Summer Project
domain: IT
b2_gatekeeper: Cyborg
squad: Kang Dynasty
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# IT B3 Swarm Config - Kang Dynasty

This folder configures the B3 swarm for the IT domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Cyborg reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Kang** - Repo commander: Controls source structure, branches, and technical direction.
- **Immortus** - Legacy historian: Reads old systems and protects compatibility.
- **Iron Lad** - New build scout: Prototypes clean modern paths and fresh implementations.
- **Rama-Tut** - Access keeper: Handles permissions, paths, sensitive-boundary rules, and environment assumptions.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.