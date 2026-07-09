---
source: A0_Amadeus_Canon
date: 2026-05-31
type: area_domain_principles
domain: L2_Business / Product / Jerry_Prime_LD01
tags: [#product #flash #avengers #principles #jerry_area #perpetual_doctrine]
guardian: Flash (A2)
squad: The Avengers (Captain America, Iron Man, Hulk, Thor, Black Widow, Hawkeye, Vision)
status: CANONICAL
source_resources: 01_Product (Geordi Guides — Leo Grindarss, Sachmoney, Romain Brunel, PRODUCT_CHANNELS_AUDIT)
---

# ⚡ FLASH PRODUCT PRINCIPLES — Jerry Area Perpetual Doctrine

> **Layer** : L2 Business / Jerry Area (Spock) / Domain 03 Product
> **Guardian** : Flash (A2) commanding the Avengers (A3 squad)
> **Nature** : PERPETUAL doctrine — Areas never "complete", they are maintained.
> **DRY contract** : Picard projects REFERENCE these principles; they never re-derive them.

---

## What this is

The **18 perpetual Product principles** distilled from the Product corpus
(`03_Resources_Geordi/01_Guides/01_Product` — Leo Grindarss *SaaS 200K en 2 mois*, Sachmoney
*Micro-SaaS*, Romain Brunel *14 agents IA / OpenClaw*, and `PRODUCT_CHANNELS_AUDIT`). These are the
**WHY/WHAT** of Product — the timeless laws Flash applies to take an idea to a shippable, retained
product. Project-specific HOW lives in Picard projects (Summer's Verse).

Where Growth (Superman) answers *"how do we get the right buyer to the door"*, Product (Flash)
answers *"is the thing behind the door worth keeping"*. Growth's North Star is qualified pipeline;
Product's North Star is **activation → retention** (the value actually delivered, not just sold).

---

## The 18 Flash Product Principles

### Cluster A — Vision & Discovery (Captain America / Black Widow)

**P1 — Validate before you build.** Talk to 10–20 real users before writing a line of code; pre-sell
where possible. (Leo: "hair on fire" before MVP.) A product no one confirmed wanting is a hobby.

**P2 — Jobs-to-be-Done, not feature lists.** Frame the product around the *job* the customer hires it
to do (Christensen/JTBD), not a pile of features. The job is stable; features are disposable.

**P3 — One painful problem, one product.** Solve ONE specific, urgent, recognized problem for ONE
niche (micro-SaaS logic). Breadth comes later; focus is the entry ticket.

**P4 — North Star = activation × retention.** Define a single product metric per cycle that captures
*delivered value* (activation rate, retention, NRR) — not vanity signups. (Flash-reserved.)

**P5 — Continuous discovery never stops.** Keep a standing cadence of user contact (Teresa Torres,
opportunity-solution tree). Discovery is a habit, not a launch-phase event.

### Cluster B — Build & Speed (Iron Man / Flash)

**P6 — MVP in days, not months.** Ship the smallest thing that resolves the core job. Use templates,
boilerplates, no-code/low-code (Bubble, FlutterFlow, Supabase, Stripe) to compress build time.

**P7 — Speed is the product team's edge.** Flash's signature: Build → Measure → Learn loops measured
in days. The fastest learner wins; cadence beats cleverness.

**P8 — Reuse before you write.** Prefer battle-tested boilerplates, libraries, and existing components
over net-new code. (Matches the global Research-&-Reuse rule.) Every line you don't write can't break.

**P9 — Agentic leverage scales without headcount.** Delegate repeatable product work to specialized
agents (Romain's 14-agent pattern): one agent = one role, orchestrated, supervised — not micromanaged.

**P10 — Manage technical debt deliberately.** Debt is a loan, not a sin; take it consciously and
schedule repayment. Unmanaged debt compounds until velocity dies.

### Cluster C — Data & Quality (Hulk / Hawkeye)

**P11 — Instrument from day one.** Activation, funnel, cohort, retention (DAU/MAU) wired before launch
(Mixpanel/Amplitude/PostHog). You cannot improve a loop you cannot see.

**P12 — Talk to churned users.** The reason someone *left* is worth more than ten reasons someone
stayed. Exit signal is the highest-density product feedback.

**P13 — A/B test claims, don't argue them.** Decide feature and messaging disputes with evidence, not
seniority (Hawkeye's precision). Opinions propose; data disposes.

**P14 — Definition of Done is non-negotiable.** Every increment ships against explicit acceptance
criteria + DoD (Hawkeye QA gate). "Done" without a DoD is "probably broken later".

### Cluster D — Go-to-Market & Economics (Thor / Vision / Flash)

**P15 — Product-led growth: the product is the funnel.** Build the acquisition/activation loop *into*
the product (free tier → aha moment → expansion). Distribution designed-in beats distribution bolted-on.

**P16 — Build in public to validate while you build.** Share the build, gather real feedback, grow the
launch audience *before* GA (Sachmoney). The audience is the de-risking, not just the marketing.

**P17 — Price on value; recurring + annual for cash flow.** Value-based pricing, MRR for compounding,
annual plans for runway. Start low only briefly — under-pricing too long starves the product.
(Flash-reserved economics, shared with Wonder Woman/Finance.)

**P18 — Anti-pattern: no scale before activation proof.** Never pour build effort or spend into scaling
a product whose users don't *activate and retain*. Over-engineering features before product-market fit
is the cardinal Product sin. Ship narrow, prove value, then widen.

---

## How the squad applies these

| Avenger | Cluster focus | Principles |
|---|---|---|
| Captain America | Vision & strategy | P2, P3, P4 |
| Black Widow | Research & discovery | P1, P5, P12 |
| Iron Man | Tech & build | P6, P8, P10 |
| Flash (A2) | Speed / cadence / economics | P7, P9, P17, P18 |
| Hulk | Data & analytics | P11, P13 |
| Hawkeye | QA & precision | P13, P14 |
| Thor | Go-to-market | P15, P16 |
| Vision | AI / innovation | P9 (agentic), P5 (discovery aug.) |

**Flash (B2 owner) is non-délégable on P4 (North Star definition) and P17 (pricing/unit economics).**
The squad proposes; Flash arbitrates and leaves an unchecked `[ ] Acceptance Flash` in each DoD.

---

## Product ↔ Growth boundary (so the two domains don't collide)

- **Growth (Superman)** owns *acquisition*: who shows up and why. North Star = qualified pipeline.
- **Product (Flash)** owns *value*: whether what they get is worth keeping. North Star = activation/retention.
- The handoff: Growth's validated message (JTBD-003) becomes Product's positioning input; Product's
  activation data feeds back to Growth's ICP. One datum, one owner (ADR-MESH-L2-001) — they point, not copy.

---

## Pipeline (how a Rock becomes JTBDs)

A B2 Product Rock decomposes into JTBD-001..004 the Avengers execute in a Picard project, mode-aware
(Solaris / Nexus / Orbiter). The Growth pipeline (`picard-growth-jtbd-launch`) is the proven template;
a Product equivalent is a candidate skill once a project actually instantiates Product JTBDs (see
`skills_queue.md`). Until then this doctrine is the WHAT; projects supply the HOW.

---

## DRY references

- **Projects** : each Picard project's `03_PRODUCT_PRINCIPLES_REF.md` (when instantiated) points here.
- **Sibling doctrine** : `01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md` (acquisition).
- **Runtime** : per the Symphony mesh, Product is an Avengers/ClickUp-leaning domain (WHEN/WHO execution);
  metrics live in Airtable/analytics as pointers, never copied into doctrine.

*Perpetual doctrine — maintained by Spock (Jerry Area A2) under Flash. Distilled from real Product corpus 2026-05-31.*
