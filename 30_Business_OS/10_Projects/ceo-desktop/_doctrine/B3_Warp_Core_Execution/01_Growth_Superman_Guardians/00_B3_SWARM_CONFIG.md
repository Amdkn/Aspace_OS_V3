---
id: B3_SWARM_CONFIG_CEO_DESKTOP_GROWTH
layer: L2-Business-Pulse-B3
project: ceo-desktop
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: Growth
b2_gatekeeper: Superman
squad: Guardians_of_the_Galaxy
topology_size: 6
source_inspiration: Marvel Cinematic Universe (Guardians of the Galaxy)
---

# Growth B3 Swarm Config — Guardians (CEO Desktop — Phase 1 Stub)

This folder configures the **Growth** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = Growth** (Superman, the B2 gatekeeper).
- **B3 = Guardians of the Galaxy** (6 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (6 Guardians)

The 6 Guardians map to 6 distinct execution roles inside the Growth domain:

| # | Agent | Execution Role (Growth) |
|---|-------|--------------------------|
| 1 | **Star-Lord** (Peter Quill) | Lead generation / ICP hunt / cold outreach framing |
| 2 | **Rocket Raccoon** | Growth engineering: experiments, automation, scraping, measurement |
| 3 | **Gamora** | ABM / pipeline sentinel: cuts weak leads, validates fit, CRM hygiene |
| 4 | **Drax** | A/B testing brutalist: kills weak variants without pity |
| 5 | **Groot** | Content + brand voice: SEO/editorial, tone consistency, painkiller message |
| 6 | **Mantis** | Buyer empathy / persona research / voice-of-customer |

> Canon roster (to be promoted in Phase 2): `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Cinematic Universe**
**Guardians of the Galaxy** team. Naming is a cognitive anchor, not a literal
mapping. Architecture follows the same B3 swarm patterns as `solaris`'s
mature config: local graph, supervisor boundary at B2, meso-swarm at L2.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/`
for the mature template this stub will grow into.
