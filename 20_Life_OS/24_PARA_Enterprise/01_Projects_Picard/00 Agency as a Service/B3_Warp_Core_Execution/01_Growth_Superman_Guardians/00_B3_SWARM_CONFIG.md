---
id: B3_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: 00_Agency_aaS
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

## Members (canon Notion AGENT_REGISTRY_DB — 6)

- **Star-Lord** (Peter Quill) - Lead Generation, Cold Outreach, ICP Hunter. Frames ICP and message hypotheses; opens field exploration.
- **Gamora** - ABM high-ticket / pipeline sentinel: cuts weak leads, validates fit, protects CRM hygiene (P9).
- **Rocket Raccoon** - Experiment engineer / growth hacks: fast channel tests, Apollo/LinkedIn scraping, automation, measurement (P6/P12/P15).
- **Groot** - Content marketing (Twitter/LinkedIn/YouTube) + **brand voice**: painkiller message, SEO/editorial, tone consistency (P8/P14/P16/P18). *Not "brand memory".*
- **Drax** - A/B testing brutal: kills weak variants without pity (P5/P6/P10).
- **Mantis** - Empathie acheteur / persona research / voice-of-customer (P7/P13/P16).

> Canon roster detail: `01_B3_AGENT_ROSTER.md` (already 6-member compliant) + `../../B2_Business_Domains/01_Growth_Superman_Guardians/B3_Squad_Guardians/00_B3_SQUAD_CANON.md`.

## Active Rock (Solaris)

```yaml
rock_id: AAAS-SOL-B2-GROWTH-2026-01
mode: Solaris (visual-first / brand-led)
north_star_metric: "Solaris-fit demos booked from brand/visual-led non-paid channels"
source_backlog: "../../B2_Business_Domains/01_Growth_Superman_Guardians/04_SOLARIS_GROWTH_EXTRACTION_QUEUE.md"
doctrine_ref: "../../B2_Business_Domains/01_Growth_Superman_Guardians/03_GROWTH_PRINCIPLES_REF.md"
```

## Operating Rule

B3 owns execution strategy. B2 (Superman) owns acceptance. B1 (Summer) owns direction. Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.