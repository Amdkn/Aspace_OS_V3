---
id: B3_SWARM_CONFIG_ABC_CHILDCARE_FINANCE
layer: L2-Business-Pulse-B3
project: abc-childcare-bos
status: PHASE_1_STUB
created: 2026-06-07
updated: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
domain: Finance
b2_gatekeeper: Wonder_Woman
squad: Thunderbolts
topology_size: 6
source_inspiration: Marvel (Thunderbolts — Yelena-led roster)
---

# Finance B3 Swarm Config — Thunderbolts (ABC OS + Child Care BOS — Phase 1 Stub)

This folder configures the **Finance** B3 swarm for the dual-entity
`abc-os-child-care-bos` project. Phase 1 = skeleton + topology declaration.
Roster detail and JTBD packets will be filled in subsequent phases.

> Note: this file supersedes the prior SHADOW_ACTIVE mirror (2026-05-27).
> Existing member sub-folders are preserved; only the swarm-config header
> is upgraded to the canonical B3 format.

## B2 / B3 Boundary

- **B2 = Finance** (Wonder Woman, the B2 gatekeeper).
- **B3 = Thunderbolts** (6 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## ABC-Specific Anchors

- **Dual-entity revenue model** — the Finance squad must reason about
  TWO distinct P&Ls:
  - **ABC OS** — formation SaaS revenue (subscription / per-formation
    pricing, AI-first cost structure, VAPI usage as primary COGS).
  - **Child Care BOS** — Orbiter-primary revenue (relationship-driven,
    contract-heavy, regulatory-bound, high-ASP).
- **Per-entity cost tracking** — VAPI usage / Gemini / Claude token
  costs land on ABC. Childcare staffing / compliance / insurance
  costs land on Child Care BOS. No commingling.
- **$200K MRR target (3-year)** — per SUMMERS_VERSE_MANIFEST. Thunderbolts
  forecast the path, defend the unit economics, enforce the burn
  discipline.
- **The Million Dollar Weekend (Noah Huber)** — per book alignment,
  Huber's work is the primary Finance reference for Child Care BOS
  economics. Used to pressure-test childcare unit economics.

## Squad Topology (6 Thunderbolts)

The Thunderbolts map to 6 distinct execution roles inside the Finance domain:

| # | Agent | Execution Role (Finance) |
|---|-------|--------------------------|
| 1 | **Yelena Belova** | Forecasting lead (dual-entity, 1y / 3y / 10y horizons) |
| 2 | **Bucky Barnes** | Cashflow discipline (per-entity P&L) |
| 3 | **U.S. Agent** (John Walker) | Compliance fiscale (FR agricole + childcare licensing) |
| 4 | **Taskmaster** | Reproductibilité comptable: tracks repeatable numbers, reconciles evidence |
| 5 | **Ghost** | Cost optimization: VAPI / LLM token drift, childcare insurance leakage |
| 6 | **Red Guardian** | Reporting — dual-entity dashboard for A0 / B1 review |

> Existing member folders (`01_Red_Hulk`, `02_Taskmaster`, `03_Baron_Zemo`,
> `04_Ghost`) remain canonical and feed the Phase 2 promotion of
> `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Thunderbolts
Yelena-led roster** (the modern lineup, not the original 1997
anti-Avengers incarnation). The "morally gray, results-driven" vibe
fits Finance's reality of having to do uncomfortable things (cost
cuts, compliance enforcement) for the project's long-term good.
Architecture follows the same B3 swarm patterns as `ceo-desktop`'s
sibling config and `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.
- B3 NEVER ships a financial artifact that bypasses Legal (G8) review
  (fiscal compliance, contract terms).

## Status

PHASE_1_STUB. Existing member sub-folders are preserved. Reference:
`../../../../ceo-desktop/_doctrine/B3_Warp_Core_Execution/06_Finance_WonderWoman_Thunderbolts/`
for the sibling structure this stub was adapted from.
