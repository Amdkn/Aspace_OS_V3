---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 00_Agency_aaS
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

## Members (canon Notion AGENT_REGISTRY_DB — 10)

- **Ikaris** - Lead / vision juridique long-terme.
- **Sersi** - Adaptabilité juridictionnelle (FR / EU / US).
- **Ajak** - Résolution amiable.
- **Kingo** - Public-facing / CGV.
- **Phastos** - Templates de contrats.
- **Sprite** - IP protection.
- **Druig** - Négociation de clauses.
- **Thena** - Litigation / archives.
- **Gilgamesh** - Enforce des clauses.
- **Makkari** - Vélocité signature (DocuSign < 24h).

> Canon roster: `../../B2_Business_Domains/08_Legal_Aquaman_Eternals/B3_Squad_Eternals/00_B3_SQUAD_CANON.md`.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.