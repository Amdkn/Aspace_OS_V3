# 12WY Area Cadence — J01 Jerry Prime / LD01 Business

## Overview

The 12WY (12-Week Year) cadence at the Jerry/Area level governs how Jerry runs strategic cycles for the LD01 Business Area ecosystem. It is NOT the same as individual Picard project 12WY cycles — Area 12WY cycles **oversee** project 12WY cycles.

**Area 12WY cadence purpose**:
- Review and update AREA_STANDARD.md
- Track Area-level lead/lag indicators
- Conduct B2 manager check-ins
- Onboard new Picard projects
- Plan next 12WY cycle

---

## Area 12WY Cycle Structure

### W1–W4: Foundation
Focus: Standards defined, B2 managers identified, first Picard projects linked.
**Area Rocks** (not project-level):
- Rock 1: AREA_STANDARD.md complete and versioned
- Rock 2: All 8 B2 domain folders structure confirmed
- Rock 3: First Picard project onboards with full B1/B2/B3 fractal
- Rock 4: Cerritos routing confirmed at >95% fidelity for Area

### W5–W8: Scaling
Focus: Portfolio depth, B2 managers active, cross-domain integration.
**Area Rocks**:
- Rock 1: Second Picard project onboards
- Rock 2: B2 managers brief and Rocks assigned
- Rock 3: Cross-domain dependencies mapped
- Rock 4: Area NPS baseline established (>50 target)

### W9–W12: Optimization
Focus: Standards refinement, next cycle planning.
**Area Rocks**:
- Rock 1: AREA_STANDARD.md quarterly review complete
- Rock 2: Area scorecard full rotation complete
- Rock 3: Next 12WY cycle Rocks defined
- Rock 4: B1 review with Rick/Morty complete

---

## Relationship to Picard Project 12WY Cycles

```
AREA 12WY (Jerry)
     │
     ├── W1-W4: Area Foundation
     │     └── Oversees: [Picard Project A W1-W4], [Picard Project B W1-W4]
     │
     ├── W5-W8: Area Scaling
     │     └── Oversees: [Picard Project A W5-W8], [Picard Project B W5-W8]
     │
     └── W9-W12: Area Optimization
           └── Oversees: [Picard Project A W9-W12], [Picard Project B W9-W12]
```

**Key principle**: Area Rocks are NOT project Rocks. Area Rocks govern the ecosystem; project Rocks govern execution.

---

## B2 Manager Check-In Cadence

Each B2 domain manager has a monthly check-in with Jerry:

| Check-In | Focus |
|----------|-------|
| **Monthly (W2, W6, W10)** | KR status, Rock progress, blockers |
| **Quarterly (W4, W8, W12)** | Rock completion, next Rock definition |
| **As-needed** | Emergency escalation, mode shift, B1 issues |

---

## 12WY Open/Close Protocol

**At 12WY Open**:
1. Review last cycle's Zone assessment (GREEN/ORANGE/RED)
2. Confirm B2 manager Rock status across all domains
3. Check Area lead/lag indicators
4. Confirm new Picard project onboarding status

**At 12WY Close**:
1. Document Area scorecard snapshot
2. Conduct B2 manager quarterly review
3. Define Area Rocks for next 12WY cycle
4. B1 review with Rick/Morty

---

---

## The Weekly Execution Engine (the heart of 12WY)

The phase folders (W01–W04 / W05–W08 / W09–W12) hold the Rocks. But the 12-Week Year **lives or dies
on the weekly cadence** — the method's whole point is that *the week, not the quarter, is the unit of
execution*. Each week:

1. **Lead vs Lag.** Score **lead measures** (controllable actions you commit to this week) — they drive
   the **lag measures** (outcomes: MRR, NPS, pipeline) you can't directly control.
2. **The Execution Score (the one number).** `% of committed weekly tactics actually completed`. The
   12WY rule: **≥85% = on track**. You are graded on *execution*, not on hitting the lag outcome — do
   the 85% and the outcomes follow. A green score under a red Rock means the Rock's tactics were wrong.
3. **The WAM (Weekly Accountability Meeting).** ~30 min, same slot weekly. Jerry + the B2 owners run
   the loop: *score last week → commit this week → name blockers*. A commit ritual, not status theatre.
   (Template: `WEEKLY_EXECUTION_TEMPLATE.md` in this folder.)

**Cadence rhythm (one surface, four tempos):**

| Tempo | Ritual | Owner |
|---|---|---|
| **Daily** | the 1 needle-moving action (Finance F13 CEO-dashboard / Codie CEO-time discipline) | each B2 / operator |
| **Weekly** | WAM: execution score + lead/lag + blockers | Jerry + B2 owners |
| **Monthly** (W2/W6/W10) | B2 KR + Rock-progress check-in | Jerry ↔ each B2 |
| **Quarterly** (W4/W8/W12 + Open/Close) | Rock completion, next-cycle Rocks, B1 review Rick/Morty | Jerry → B1 |

---

## C1–C4 command-cycle mapping (B1 gates across the 12 weeks)

The four B1 command cycles (`B1_Area_Direction/02_12WY_COMMAND_CYCLES.md`) are the **gates** that
punctuate the 3 phases:

| Command cycle | Gate | Lands in |
|---|---|---|
| **C1 Direction Lock** | North Star filled, mode selected, B2 queue seeded, Product-only risk acknowledged | 12WY **Open** (≈W1) |
| **C2 Domain Activation** | all 8 B2 domains have a named concern; Ops/IT runtime feasibility; Finance/Legal exposure; People load risk | end **Foundation** (W4) |
| **C3 Execution Proof** | B3 evidence log exists; ≥1 tactic has artifact proof; blocked items not hidden | through **Scaling** (W5–W8) |
| **C4 Graduation or Archive** | B2 gate matrix complete; B3 Lead/Lag summarized; register updated | 12WY **Close** (W12, **Optimization**) |

---

## Where the cadence runs (Baserow 12WY — Symphony L1)

The Area 12WY is the **macro** instance of the framework that the Symphony **Baserow adapter**
(USS SNW / Curie, L1) operates: `Quarter Intent` (vision per layer) · `The 12 Rocks` (each tagged
`Rock L2` for Business) · `The Warp Core` (W1–W12 weekly Top-3 with the **50/30/20** ratio: 50%
L2-Business / 30% L1-Life / 20% L0-Tech commitments). A Plane cycle = one Warp Core week.
- **Macro (here)** sets the Area Rocks + cadence; **micro** = each Picard project's own 12WY (this
  cadence *oversees* them) — same fractal as the B1/B2/B3 stack.
- The Rocks feed the 8 B2 domains: each owns ≥1 Rock per cycle, scored against its doctrine
  (`B2_Area_Domains/<NN>/03_<HERO>_<DOMAIN>_PRINCIPLES.md`, all 8 now complete) and its KRs.

---

## The 4-Rock discipline (AREA_STANDARD P8)

Max **4 Area Rocks per cycle** (more than 4 = none). Each Rock = start state + end state + 90-day
(12-week) deadline + 5 KRs. Area Rock ≠ project Rock: Area Rocks govern the ecosystem, project Rocks
govern execution. Distribute Rocks across the 8-domain wheel; never let one domain hoard all four while
another sits empty (the B1 imbalance scan, `07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW.md`).

---

*B1 owner: Jerry Prime (Area steward)*
*Source: AREA_STANDARD.md P8 (Quarterly Rocks) + 12 Week Year (Moran) + Symphony L1 Baserow adapter + B1 command cycles*
*Next review: 2026-08-21*