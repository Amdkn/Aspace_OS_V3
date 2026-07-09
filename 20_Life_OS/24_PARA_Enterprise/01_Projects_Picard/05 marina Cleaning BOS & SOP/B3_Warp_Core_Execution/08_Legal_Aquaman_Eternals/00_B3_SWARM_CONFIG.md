---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 05_Marina
surface_kind: QuickAccess Mirror
domain: Legal
b2_gatekeeper: Aquaman
squad: Eternals
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# Legal B3 Swarm Config - Eternals

This folder configures the B3 swarm for the Legal domain. The swarm executes B2 JTBD packets autonomously, collaborates internally, and escalates only when the contract cannot be satisfied.

## Design Pattern

- **Local graph** inside the squad: every member can help unblock another member.
- **Supervisor boundary** at B2: Aquaman reviews goals, DoD, gates, and proof.
- **Meso swarm** across B2 VPs: domain blockers can be negotiated with peer B2s before escalating to B1.
- **No babysitting**: B3 does not ask B2 for every step; B3 asks only for missing authority, missing inputs, cross-domain conflict, or DoD ambiguity.

## Source Inspiration

Inspiration only: Agency Swarm communication_flows/roles; OpenAI Swarm handoffs/context variables; Swarms hierarchical-parallel-collaborative modes; Kimi Agent Swarm parallel work and productive disagreement; Agent Swarm lead-worker delegation/persistent memory.

## Members

- **Ikaris** - Claims force: Checks assertive claims, guarantees, and exposure.
- **Ajak** - Compliance judge: Maps policy, privacy, and regulatory boundaries.
- **Phastos** - IP builder: Protects assets, licenses, templates, and inventions.
- **Thena** - Defense counsel: Prepares fallback positions, disclaimers, and dispute posture.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.