---
id: SUMMER_01_CEOS_DESKTOP
layer: L2-Business-Pulse
status: PHASE_1_SKELETON
created: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
project_slug: ceo-desktop
project_kind: CEO_Command_Center
mode: Matryoshka_Dashboard
adr_anchors:
  - ADR-FWK-021
  - ADR-INFRA-002
  - ADR-INFRA-003
---

# Summer's Verse Manifest — CEO's Desktop

> The A0 CEO command center. A single pane of glass over the 8 business domains and the 8 B3 Marvel squads. Materializes the Life Wheel as an operating dashboard, not a metaphor.

## What This Project Is

CEO's Desktop is the **A0 command center** for business operations. It is not a product, not a service, not a revenue line. It is the **runtime** through which Amadeus observes, decides, and steers the 8 SOB domains (Growth, Sales, Product, Ops, IT, Finance, People, Legal) and the 8 B3 squads that execute them.

It follows the **Matryoshka principle** (ADR-INFRA-003): the Life Wheel holds the Business Wheel, the Business Wheel holds the Domain Wheels, the Domain Wheels hold the Rock Wheels. The CEO's Desktop surfaces the right layer to A0 at the right cadence.

It follows the **Repo-Home Junction Law** (ADR-INFRA-002): doctrine lives long, code lives short, junction points the way. This `_doctrine/` folder is the home; downstream `apps/<role>` homes build against it.

It follows the **Canon Tripartite des Blueprints** (ADR-FWK-021): B1 direction → B2 domain DoD → B3 jobs to be done, with explicit handoffs and proof paths.

## 1-Year Vision

CEO's Desktop **Phase 1 → 2 → 3 complete**:

- **Phase 1 (now → 2026-Q4)** — Skeleton. B1 direction locked, B2 handoff queue seeded for the 8 domains, 12WY cadence defined, decision charter ratified. No execution yet.
- **Phase 2 (2026-Q4 → 2027-Q1)** — Activation. B2 domain managers named for each of the 8 SOB. B3 squads accept first handoffs. Lead indicators wired. One full 12WY cycle proven end-to-end.
- **Phase 3 (2027-Q1 → 2027-Q2)** — Graduation. B1/B2/B3 triad operating rhythmically. Wheel balance review quarterly. Junction to Life OS (Orville/Discovery/SNW/Enterprise/Cerritos/Protostar) live.

Minimum outcomes at 1Y:

- one A0 command surface that opens in < 2 seconds and answers "where am I drifting?";
- 8 SOB domains each with a named B2 owner and a current Rock;
- 8 B3 squads each with a queued JTBD and a proof path;
- a working handoff to Life OS so A0 sees business drift and life drift in one place.

## 3-Year Vision

The CEO's Desktop is the **Life Wheel orchestrator** for Amadeus. Not a tool A0 opens, but a runtime A0 inhabits. Every quarterly review, every Rock, every domain drift triggers from here. The 12WY cadence is the heartbeat.

Minimum outcomes at 3Y:

- a 12WY rhythm with two full years of retrospective data;
- delegated B2 ownership for all 8 domains with no single-point-of-failure on A0;
- junction to Life OS stable enough that a new agent (Codex, Gemini, future Claude) can resume operating the desktop from the wiki alone;
- the 8 B3 squads operating as Marvel/DC teams with named roles, R&R, and seasonal rotation.

## 10-Year Vision

A0's **sovereign CEO runtime**. The CEO's Desktop is the canonical surface from which Amadeus steers A'Space OS V2 as a whole — Life, Business, Kernel. It is licensable as doctrine, teachable to other sovereigns, auditable by Beth & Morty, portable across the A'Space Multiverse.

Minimum outcomes at 10Y:

- archive-ready project memory (per solaris graduation gates);
- licensable doctrine pack: B1/B2/B3 templates, handoff queue schema, decision charter template, junction spec;
- A'Space Multiverse portability — CEO's Desktop runs on VPS, on-prem, or air-gapped sovereign install;
- the business wheel rotation preserved across future agents, modes, and seasons.

## ICP Variants — The 8 SOB Operating Modes

The CEO's Desktop does not have one user. It has **8 domain operators** (B2 managers) and **8 squad leads** (B3 leads) who each see the desktop through their own lens. These are the **8 SOB operating modes**:

| # | SOB Domain | B3 Squad (Marvel) | Desktop Mode | Cadence |
|---|------------|-------------------|--------------|---------|
| 1 | **Growth**   | Superman / Guardians     | Pulse — experiment velocity, ICP drift, channel mix | Weekly |
| 2 | **Sales**    | Martian Manhunter / Illuminati | Pipeline — qualified leads, conversion, handoff to Product | Weekly |
| 3 | **Product**  | Flash / Avengers         | Build — shipped Rocks, JTBD proof, scope drift | Weekly |
| 4 | **Ops**      | Batman / Fantastic Four  | Flow — SOP health, delivery reliability, cost per unit | Bi-weekly |
| 5 | **IT**       | Cyborg / Kang Dynasty    | Stack — runtime, deploy, security, MCP/CLI health | Daily |
| 6 | **Finance**  | Wonder Woman / Thunderbolts | Capital — burn, margin, runway, unit economics | Monthly |
| 7 | **People**   | Green Lantern / X-Men    | Load — owner load, training, founder-mode risk | Monthly |
| 8 | **Legal**    | Aquaman / Eternals       | Boundary — IP, terms, exposure, compliance | Quarterly |

Each mode surfaces a different facet of the same underlying data. A0 sees all 8 in one scroll; a B2 manager sees only their column plus the 4 boundaries (IT, Finance, Legal, People) that gate their work.

## What This Manifest Is Not

- Not a product spec. There is no "feature list." There is a runtime.
- Not a tool. Tools live in `apps/<role>/` per ADR-INFRA-002. Doctrine lives here.
- Not a clone of solaris. solaris is a portfolio project (Agency aaS). CEO's Desktop is a command surface for A0 over the whole portfolio. Different kind.

## Pointer

See `B1_Summer_Direction/00_B1_DIRECTION_INDEX.md` for the B1 cockpit.
