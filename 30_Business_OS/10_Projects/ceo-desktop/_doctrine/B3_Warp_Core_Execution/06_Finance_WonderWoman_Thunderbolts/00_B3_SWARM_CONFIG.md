---
id: B3_SWARM_CONFIG_CEO_DESKTOP_FINANCE
layer: L2-Business-Pulse-B3
project: ceo-desktop
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

# Finance B3 Swarm Config — Thunderbolts (CEO Desktop — Phase 1 Stub)

This folder configures the **Finance** B3 swarm for the `ceo-desktop` project.
Phase 1 = skeleton + topology declaration. Roster detail and JTBD packets
will be filled in subsequent phases.

## B2 / B3 Boundary

- **B2 = Finance** (Wonder Woman, the B2 gatekeeper).
- **B3 = Thunderbolts** (6 A3-active execution agents).
- B2 owns direction, DoD, acceptance, and proof review.
- B3 owns execution strategy, local unblocking, and delivery.

## Squad Topology (6 Thunderbolts)

The Thunderbolts map to 6 distinct execution roles inside the Finance domain:

| # | Agent | Execution Role (Finance) |
|---|-------|--------------------------|
| 1 | **Yelena Belova** | Forecasting (lead) |
| 2 | **Bucky Barnes** | Cashflow discipline |
| 3 | **U.S. Agent** (John Walker) | Compliance fiscale |
| 4 | **Taskmaster** | Reproductibilité comptable: tracks repeatable numbers, reconciles evidence |
| 5 | **Ghost** | Cost optimization: finds hidden spend, leakage, model-usage drift |
| 6 | **Red Guardian** | Reporting |

> Canon roster (to be promoted in Phase 2): `01_B3_AGENT_ROSTER.md`.

## Source Inspiration

Inspiration only — the squad is named after the **Marvel Thunderbolts**
**Yelena-led roster** (the modern lineup, not the original 1997 anti-Avengers
incarnation). The "morally gray, results-driven" vibe fits Finance's reality
of having to do uncomfortable things (cost cuts, compliance enforcement) for
the project's long-term good. Architecture follows the same B3 swarm
patterns as `solaris`'s mature config.

## Operating Rule (No-Babysitting)

- B3 does not ask B2 for every step.
- B3 asks B2 **only** on: missing authority, missing inputs, cross-domain
  conflict, or DoD ambiguity.
- B3 owns execution strategy. B2 owns acceptance. B1 owns direction.
- Doctrine (P1–P18) is inherited from Area Jerry, never re-derived here.

## Status

PHASE_1_STUB. No JTBDs or runtime agents yet. Reference:
`../../../../solaris/_doctrine/B3_Warp_Core_Execution/06_Finance_WonderWoman_Thunderbolts/`
for the mature template this stub will grow into.
