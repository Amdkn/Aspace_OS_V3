---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 00_Agency_aaS
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

## Members (canon Notion AGENT_REGISTRY_DB — 7)

- **Captain America** - Product vision / roadmap conviction (lead).
- **Iron Man** - Tech architecture / choix stack / debt management.
- **Thor** - Power features / MVP brute force quand timing critique.
- **Hulk** - QA destructeur / edge cases / stress testing.
- **Black Widow** - Spec writing / user stories rigoureuses.
- **Hawkeye** - Précision UX / sniper feature-level.
- **Scarlet Witch** - Vision design system / brand cohérence.

> Canon roster: `../../B2_Business_Domains/03_Product_Flash_Avengers/B3_Squad_Avengers/00_B3_SQUAD_CANON.md`.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.