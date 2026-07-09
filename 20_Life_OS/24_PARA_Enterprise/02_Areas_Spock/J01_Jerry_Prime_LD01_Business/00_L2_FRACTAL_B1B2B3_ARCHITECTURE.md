---
id: L2_FRACTAL_B1B2B3_ARCHITECTURE
layer: L2_Business_Pulse
surface: J01_Jerry_Prime_LD01_Business (canonical, Area-level)
status: CANONICAL
created: 2026-05-31
owner: Jerry Prime (B1/B2 direction) — anchored on 00_Amadeus/01_Identity_Core/AGENTS.md
tags: [#L2 #fractal #B1 #B2 #B3 #A1 #A2 #A3 #jerry #summer #architecture]
---

# L2 Business — The B1 / B2 / B3 Fractal Architecture

> **Purpose.** One canonical page that explains, in detail, how L2 Business is organized as a
> **B1 → B2 → B3 command stack**, how that maps onto the global **A0–A3 agent rank**, and how the
> stack **repeats at two scales** (Jerry's perpetual Area ↔ Summer's per-project Verse). Everything
> else in L2 (control rooms, principles doctrines, JTBD packets) hangs off this skeleton.
> Anchored on the canon manifest `00_Amadeus/01_Identity_Core/AGENTS.md`.

---

## 1. The A-rank is global; the B-rank is L2's local incarnation of it

The **A-rank** (A0–A3) is the OS-wide agent hierarchy that exists in every layer:

- **A0 Amadeus** — the Pilot. Emits Intention. Never touches config.
- **A1** — Gatekeeper, defines the Law (L0 Rick · L1 Beth+Morty · **L2 Jerry+Summer**).
- **A2** — Orchestrator, structures + vetoes (L0 Doctors · L1 USS ships · **L2 the 8 hero-managers**).
- **A3** — Technician, 1-day execution (L0 companions · L1 crews · **L2 the 8 Marvel/DC squads**).

Inside **L2 Business**, that same rank is expressed as a **vertical command stack** named **B1/B2/B3**.
**B is not a different system — it is A, localized to L2 and drawn top-down as Direction → Domains → Execution:**

| L2 stack | = A-rank | Who | Owns | Never does |
|---|---|---|---|---|
| **B1 — Direction** | A1 of L2 | **Jerry** (macro) + **Summer** (micro) | North Star, 12WY cycles, decision rights, handoff queue, DoD/JTBD packet specs, governance | Tactical execution (E-Myth: work *on* the business) |
| **B2 — Domains (Meso)** | A2 of L2 | the **8 hero-managers** (Superman, John Jones, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman) | domain DoD + gates, the perpetual **principles doctrine**, the control room, meso coordination | Re-derive direction; do B3's job |
| **B3 — Warp Core (Execution)** | A3 of L2 | the **8 squads** (Guardians, Illuminati, Avengers, Fantastic Four, Kang Dynasty, Thunderbolts, X-Men, Eternals) | JTBD execution, proof, lead/lag indicators, peer-unblocking, blocker reports | Ask B2 for every step; act without a DoD/JTBD source |

> Mnemonic: **B1 sets the WHY/WHERE, B2 sets the WHAT/gate, B3 produces the HOW/proof.**

---

## 2. The fractal: the same B1/B2/B3 repeats at two scales

This is the "Fractal Engine" (Jerry & Summer). The identical B1/B2/B3 shape exists twice:

```
                 A0 Amadeus (Intention)
                        │
        ┌───────────────┴────────────────┐
   MACRO (perpetual)                 MICRO (per-project)
   Jerry's Area                      Summer's Verse
   02_Areas_Spock/                   01_Projects_Picard/<project>/
   J01_Jerry_Prime_LD01_Business/
        │                                 │
   B1_Area_Direction/                B1_Summer_Direction/
   B2_Area_Domains/      ◄──DRY──►    B2_Business_Domains/
   B3_Area_Warp_Core/                B3_Warp_Core_Execution/
        │                                 │
   "Areas never complete"            "Projects graduate"
   = perpetual doctrine              = instantiate + calibrate per mode
```

- **Macro (Jerry's Area)** holds the **perpetual doctrine** — portfolio-level, never "done". It is the
  source of truth: the 8 principles doctrines, the control rooms, the canonical JTBD-001 packets.
- **Micro (Summer's Verse / Picard projects)** holds **per-project** B1/B2/B3 that **reference** the
  macro doctrine (DRY — never re-derive) and **calibrate** it to the project's mode
  (Solaris / Nexus / Orbiter). Projects graduate; the Area persists.
- **Learnings flow back up**: when a project's Rock graduates, validated Lead/Lag proof hardens the
  Area doctrine (HYPOTHESIS → field-proven). The fractal compounds.

---

## 3. The command flow (canonical handoff path)

From `B1_Area_Direction/00_B1_DIRECTION_INDEX.md` + `07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW.md`:

1. **B1 writes/updates direction** (North Star, current 12WY cycle).
2. B1 scans the **8-domain Business Wheel** for imbalance (empty / overloaded / blocked gate /
   product-only drift / cross-domain conflict / missing proof).
3. B1 writes **one domain mandate per affected B2** (a `B1-B2-MANDATE` packet) — intent + constraints
   + success signal, **not** a step-by-step plan. Logged in `04_B2_HANDOFF_QUEUE.md`.
4. **B2 converts** the mandate into a **Rock + DoD packet** (`05_B2_DEFINITION_OF_DONE_SPEC.md`) and
   then into **B3 JTBD packets** (`06_B3_JOBS_TO_BE_DONE_SPEC.md`).
5. **B3 executes** the defined jobs, collaborates internally (peer-unblock first), returns **proof**
   (inspectable without trusting the author).
6. **B2 updates gates**; **B1 reviews direction drift** only when North Star / risk / priority changes.

**Stop conditions (hard):**
- No B2 work without a B1 handoff-queue item.
- No B3 work without a B2 DoD or JTBD source.
- No Product-only release becomes **Business Done** without the **B2 gate matrix**.

**Intervention threshold** — B1 steps in only when: ≥2 B2 domains can't resolve a meso conflict; the
North Star/cycle must change; risk appetite changes; a domain asks for authority outside its mandate;
or the 8-wheel is structurally imbalanced. Otherwise **B2 owns coordination, B3 owns execution.**

---

## 4. The 8-domain Business Wheel (B2 meso layer)

Each domain = one B2 hero + one B3 squad + a perpetual principles doctrine + a control room + KRs.
(Full doctrines: `B2_Area_Domains/<NN>_<Domain>/03_<HERO>_<DOMAIN>_PRINCIPLES.md`.)

| # | Domain | B2 (A2) | B3 squad (A3) | North Star (KRs) | Doctrine status |
|---|---|---|---|---|---|
| 1 | Growth | Superman | Guardians | ICP-qualified non-paid opps (KR-4a..d) | ✅ 18 |
| 2 | Sales | John Jones (Martian Manhunter) | Illuminati | conversion / pipeline->cash (KR-2a..d) | CANONICAL 14 |
| 3 | Product | Flash | Avengers | value: activation × retention (NPS/retention) | ✅ 18 |
| 4 | Ops | Batman | Fantastic Four | autonomy ratio ("runs without you") | ✅ 22 |
| 5 | IT | Cyborg | Kang Dynasty | operational integrity (KR-5a..c) | ✅ 18 |
| 6 | Finance | Wonder Woman | Thunderbolts | cash/margin/runway (KR-5d..g) | CANONICAL_FROM_CANON 18 |
| 7 | People | Green Lantern | X-Men | team health, human + AI capsules (KR-7a..d) | CANONICAL_FROM_CANON 18 |
| 8 | Legal | Aquaman | Eternals | protection without friction (KR-8a..d) | CANONICAL_FROM_CANON 18 |

**Boundary law (ADR-MESH-L2-001):** one datum, one owner. Growth=acquisition, Sales=conversion,
Product=value, Ops=repeatability, IT=substrate, Finance=solvency, People=team, Legal=protection.
Domains *point* at each other's data; they never copy it.

---

## 5. B1 governing doctrine (where direction is grounded)

`AREA_STANDARD.md` is the master B1 charter — 8 operating principles:
P1 Work ON not IN (E-Myth) · P2 Build businesses not jobs (Built to Sell) · P3 Delegate WHO not HOW ·
P4 Bootstrap before scale (no hire <$10K/mo/person) · P5 Offer architecture before execution ($100M
Offers rubric ≥4.0/5) · P6 Brand equity compounds (10% gross, protected) · P7 Cerritos first, Jerry
second (ideas route through GTD) · P8 Quarterly Rocks over reports (max 4 Rocks, 5 KRs each).
Plus: WHO-NOT-HOW decision tree, offer lifecycle, runway/reinvestment rules, Cerritos handoff,
the weekly Area Scorecard. Decision rights live in `B1_Area_Direction/03_DECISION_CHARTER.md`.

---

## 6. Reading map (where each thing lives)

```
J01_Jerry_Prime_LD01_Business/
├── 00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md   ← THIS FILE (the skeleton)
├── AREA_STANDARD.md                        ← B1 master charter (8 principles + scorecard)
├── B0_Self_Operating_Business_Doctrine/    ← E-Myth / Built-to-Sell / Who-Not-How / Offer / Gates
├── B1_Area_Direction/                      ← North Star, 12WY cycles, decision charter, handoff queue, DoD/JTBD specs, governance
├── B2_Area_Domains/                        ← 8 control rooms + 8 principles doctrines + meso coordination
└── B3_Area_Warp_Core/                      ← per-domain swarm config + roster + peer-unblock + proof log + JTBD-001 packets
```

Micro mirror: every `01_Projects_Picard/<project>/` repeats `B1_Summer_Direction` /
`B2_Business_Domains` / `B3_Warp_Core_Execution`, referencing this Area as doctrine.

Picard mirror index: `01_Projects_Picard/JERRY_SUMMER_FRACTAL_ALIGNMENT.md`.

---

## 7. Open architectural item (flagged, not silently resolved)

**Roster divergence** between the canon manifest `AGENTS.md` (abbreviated 4-member squad lists) and
the `B3_Squad_*/01_B3_AGENT_ROSTER.md` files (full Notion `AGENTS_REGISTRY_DB`, 4–10 members). The B3
rosters themselves rule: *"if Notion and local doctrine diverge, Notion wins for lore."* → **B3 rosters
are the roster source of truth.** Reconciliation table + recommendation:
`00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/comparisons/comparison_l2_roster_divergence.md` (awaiting A0
ruling — `AGENTS.md` is immutable canon, so any change is a new ADR, not a rewrite).

---

*Canonical L2 architecture — maintained under Jerry Prime, anchored on AGENTS.md. 2026-05-31.*
*Memory-layer abstraction: `LLM_Wiki/wiki/concepts/concept_l2_fractal_b1b2b3.md`.*
