---
id: B3_SWARM_CONFIG_ABC_CHILDCARE_GROWTH
layer: L2-Business-Pulse-B3
project: abc-childcare-bos
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

# Growth B3 Swarm Config — Guardians (ABC OS + Child Care BOS — Phase 1 Stub)

This folder configures the **Growth** B3 swarm for the dual-entity
`abc-os-child-care-bos` project. Phase 1 = skeleton + topology declaration.
Roster detail and JTBD packets will be filled in subsequent phases.

> Note: this file supersedes the prior SHADOW_ACTIVE mirror (2026-05-27).
> Existing JTBD packets and member sub-folders are preserved and remain
> authoritative; only the swarm-config header is upgraded to the canonical
> B3 format (project=abc-childcare-bos, parent_jerry=Jerry Prime).

## B2 / B3 Boundary

- **B2 = Growth** (Superman, the B2 gatekeeper).
- **B3 = Guardians of the Galaxy** (6 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## ABC-Specific Anchors

- **Two ICPs, one squad** — Growth must hunt BOTH:
  - **Agriculteurs** (ABC OS side) — AI-first formation buyers, rural /
    semi-rural French, voice-channel-comfortable, ROI-driven.
  - **Childcare operators** (Child Care BOS side) — Orbiter-primary,
    relationship-driven, compliance-as-conversion-objection.
- **VAPI as acquisition surface** — cold outreach and qualification
  can ride the same VAPI voice funnel used inside the product. Growth
  owns the top-of-funnel variant of that funnel, Product owns the
  in-product variant.
- **Voice is a channel, not the offer** — do not sell "VAPI". Sell
  "agricultural formation that pays for itself" and "childcare ops that
  survive the next regulatory audit".

## Squad Topology (6 Guardians)

The 6 Guardians map to 6 distinct execution roles inside the Growth domain,
adapted to the dual ABC + Child Care reality:

| # | Agent | Execution Role (Growth) |
|---|-------|--------------------------|
| 1 | **Star-Lord** (Peter Quill) | Lead generation / ICP hunt across agriculteurs + childcare operators; cold outreach framing in FR |
| 2 | **Rocket Raccoon** | Growth engineering: VAPI funnel experiments, voice-A/B, scraping, measurement |
| 3 | **Gamora** | ABM / pipeline sentinel: cuts weak leads, validates fit (agriculteur vs operator), CRM hygiene |
| 4 | **Drax** | A/B testing brutalist: kills weak VAPI variants / weak landing variants without pity |
| 5 | **Groot** | Content + brand voice: SEO/editorial agricole, tone consistency, painkiller message |
| 6 | **Mantis** | Buyer empathy / persona research: voix-du-paysan + voix-de-la-directrice-de-crèche |

> Existing JTBD packets in this folder (JTBD-001…JTBD-005) remain canonical
> and feed the Phase 2 promotion of `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Cinematic
Universe Guardians of the Galaxy** team. Naming is a cognitive anchor,
not a literal mapping. Architecture follows the same B3 swarm patterns
as `ceo-desktop`'s sibling config and `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.
- B3 NEVER ships a growth experiment that bypasses Legal review (G8).

## Status

PHASE_1_STUB. Existing JTBDs and member sub-folders are preserved.
Reference: `../../../../ceo-desktop/_doctrine/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/`
for the sibling structure this stub was adapted from.
