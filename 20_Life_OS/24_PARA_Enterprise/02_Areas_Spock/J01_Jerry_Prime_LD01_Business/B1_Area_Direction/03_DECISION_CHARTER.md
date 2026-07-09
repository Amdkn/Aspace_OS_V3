---
id: B1_DECISION_CHARTER
layer: B1_DIRECTION
surface: J01_Jerry_Prime_LD01_Business
status: CANONICAL
created: 2026-05-31
updated: 2026-05-31
---

# B1 Decision Charter — Who decides what, who can veto, when to escalate

> The B1 cockpit (`00_B1_DIRECTION_INDEX.md`) needs explicit decision rights so B2 managers and B3
> swarms act without inferring authority. This charter answers three questions for every L2 decision:
> **who owns it, who can veto it, and when it escalates.** Anchored on `AREA_STANDARD.md` (the 8
> operating principles) and `AGENTS.md` (the escalation chain Jerry → B1 Rick/Morty → A0).

---

## 1. Decision rights by rank (RACI-style)

| Decision type | Owns (A/R) | Consulted (C) | Vetoes | Escalates to |
|---|---|---|---|---|
| **Intention / what business exists at all** | A0 Amadeus | — | A0 | — |
| North Star (1Y/3Y/10Y), risk appetite | **B1** (Jerry macro / Summer micro) | B2 wheel | B1 (Beth-conscience via Morty) | A0 |
| 12WY cycle priority, the ≤4 quarterly Rocks | **B1** | B2 owners | B1 | A0 if North Star shifts |
| Offer architecture, pricing strategy (ASP) | **B1** + **Finance B2 (Wonder Woman)** | Sales B2 | Finance (margin) | B1 |
| Domain mandate (what a B2 must make true) | **B1** | affected B2 | B1 | — |
| Domain Rock + DoD + gates | **B2 owner** (the hero) | peer B2 (meso) | B2 owner | B1 |
| Execution tactics, tools, order of work | **B3 squad** | squad peers | B3 lead | B2 owner |
| Cross-domain meso conflict | the 2+ **B2s** (DC coordination) | — | — | B1 if unresolved |
| IT architecture | **Cyborg (B2)** — Jerry does NOT decide | B1 (alignment to runway) | Cyborg | B1 |
| Cash-flow execution, reconciliation | **Wonder Woman (B2)** | B1 | Wonder Woman | B1 |
| Any public claim / contract / IP (regulated) | **Aquaman (B2)** — compliance gate | B1, originating B2 | **Aquaman (can veto a public message)** | B1 / A0 |
| Headcount / capsule onboarding | **Green Lantern (B2)** | Finance (runway) | Green Lantern + Finance | B1 |

**Rule of thumb:** B1 sets WHY/WHERE, B2 sets WHAT/gate, B3 sets HOW/proof. A higher rank never does
a lower rank's job (E-Myth P1) — if a B3 can do it, it IS a B3 task.

---

## 2. The non-délégable B2 decisions (reserved per domain)

Each B2 owner keeps an unchecked `[ ] Acceptance <Hero>` in every domain DoD. These are the calls a
B2 may **not** delegate to the B3 swarm:

| Domain | Reserved to the B2 owner |
|---|---|
| Growth (Superman) | North Star metric (P4) + RICE prioritization (P5) |
| Sales (John Jones) | Pricing strategy (ASP discipline) + deal qualification |
| Product (Flash) | North Star definition (P4) + pricing/unit economics (P17) |
| Ops (Batman) | Autonomy North Star (P4) + go/no-go on automation investment |
| IT (Cyborg) | IT architecture (outright — Jerry does not decide) |
| Finance (Wonder Woman) | Pricing + reinvestment allocation; discount >15% sign-off |
| People (Green Lantern) | Headcount timing (12-mo runway rule) + retention intervention |
| Legal (Aquaman) | Contract escalation (B1 vs B2) + IP-protection priority |

---

## 3. Veto rights (who can stop work)

- **A0 Amadeus** — absolute veto on Intention (what we pursue at all). Never overridden.
- **B1 (Jerry/Summer; Beth's conscience expressed through the B1 layer)** — veto on anything that
  violates the North Star, risk appetite, or an `AREA_STANDARD` operating principle (e.g. revenue
  that damages brand equity = P6 veto; a hire without 12-mo runway = P4 veto).
- **Finance (Wonder Woman)** — veto on any deal/discount that breaks the margin floor or runway
  threshold (discount >15% requires her sign-off).
- **Legal (Aquaman)** — veto on any public claim, contract, or IP exposure that fails compliance
  (the `legal_gate` — Growth/Sales cannot waive it).
- **A B3 peer** — *productive-disagreement* veto: when a JTBD affects cost, legal exposure, customer
  promise, release quality, or operational load, at least one peer may block the first solution. The
  disagreement must end in: accepted revision, rejected-with-reason, or B2 escalation.

---

## 4. Escalation thresholds (when a decision climbs)

From `AREA_STANDARD.md` monthly-review triggers + domain canons:

| Signal | Threshold | Escalates to |
|---|---|---|
| Any Rock behind | > 2 weeks | Jerry + B1 emergency session (48h) |
| MRR decline | > 5% MoM | B1 emergency session (48h) |
| Runway drop | < 9 months (alert at 6) | B1 + mitigation plan; A0 if <6 |
| B2 domain at risk | > 2 consecutive weeks | Jerry + B2 remediation |
| NPS drop | > 10 points | B1 + root-cause |
| Close rate | < 25% | Sales audit + corrective action |
| Growth CPQL | > 150€ for 14 days | Jerry (Superman escalation) |
| IT uptime / MTTR | uptime <99% mo · MTTR >1h | Cyborg → Jerry |
| Finance | runway <6mo · Solaris margin <25% | Wonder Woman → Jerry |
| People | >3 agents `Standby` · HIGH ethics finding | Green Lantern → Jerry |
| Legal | HIGH RGPD finding · client-data breach | Aquaman → Jerry → A0 |
| Meso conflict | ≥2 B2 domains can't resolve | B1 |
| Authority request outside mandate | any | B1 |

**Canonical chain:** B3 → (peer-unblock first) → B2 owner → B1 (Jerry/Summer) → B1 gatekeepers
(Rick/Morty) → A0 Amadeus. Never skip a rung except for the explicit emergency triggers above.

---

## 5. Output packet — the B1 decision record

Every B1 decision that changes direction is logged as a short packet (so drift is auditable):

```yaml
decision_id: B1-DECISION-YYYY-NN
date: YYYY-MM-DD
type: north_star | cycle_priority | offer_pricing | domain_mandate | veto | escalation_ruling
trigger: "what surfaced this decision (signal + threshold)"
options_considered:
  - option + 1-line tradeoff
decision: "the call made"
owner: A0 | B1 Jerry | B1 Summer | B2 <hero> | Finance | Legal
vetoes_applied: [none | who + why]
affected_domains: [Growth | Sales | Product | Ops | IT | Finance | People | Legal]
cascades_to:
  - "B1-B2-MANDATE-… in 04_B2_HANDOFF_QUEUE.md (if it spawns domain work)"
reversible: true | false
review_date: "when to revisit (or 'standing')"
```

A0 decisions are recorded the same way with `owner: A0` and `reversible: false` unless stated.

---

## 6. Stop conditions (inherited from the Direction Index)

- No B2 work without a B1 handoff-queue item.
- No B3 work without a B2 DoD or JTBD source.
- No Product-only release becomes **Business Done** without the B2 gate matrix.
- No decision that crosses a §4 threshold proceeds without the escalation it requires.

---

*B1 Decision Charter — owned by Jerry Prime, governed by Beth's conscience, ratified by A0.*
*Anchored on `AREA_STANDARD.md` + `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md`. 2026-05-31.*
