---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 00_Agency_aaS
surface_kind: QuickAccess Mirror
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

## Members (canon Notion AGENT_REGISTRY_DB — 6)

- **Kang Prime** - Infra core: VPS, DNS, Dokploy, orchestration (lead).
- **Iron Lad** - Provisioning automatisé (Hostinger API).
- **Scarlet Centurion** - Sécurité réseau / SSL-TLS.
- **Immortus** - Capacity planning / scaling anticipé.
- **Victor Timely** - CI/CD pipelines.
- **Rama-Tut** - Backup / Disaster Recovery.

> Canon roster: `../../B2_Business_Domains/05_IT_Cyborg_KangDynasty/B3_Squad_KangDynasty/00_B3_SQUAD_CANON.md`.

## Operating Rule

B3 owns execution strategy. B2 owns acceptance. B1 owns direction.