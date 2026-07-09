---
id: ADR-CANON-001
title: Roster Source of Truth — Notion AGENT_REGISTRY_DB prime over AGENTS.md squad lists
status: ACCEPTED
date: 2026-06-02
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2)
domain: L2_Business / Agent_Hierarchy / Canon_Reconciliation
supersedes_scope: AGENTS.md §"Macro Squads" roster membership (lore only — NOT structure)
tags: [#ADR #canon #roster #notion #AGENTS_md #B3_squad #divergence]
---

# ADR-CANON-001 — Roster Source of Truth

## Status

**ACCEPTED** — A0 ruling, 2026-06-02. Notion is canon prime for L2 B3 squad roster lore.

## Context

Two canon surfaces describe the eight L2 B3 squads and they **disagreed**:

- **`00_Amadeus/01_Identity_Core/AGENTS.md`** — the immutable manifest — lists **abbreviated
  4-member** squads (and, for Sales, *generic* role names `Illuminati I–V`).
- **The B3 transcriptions** (`B2_*_Domains/<NN>/B3_Squad_<X>/00_B3_SQUAD_CANON.md` +
  `B3_*_Warp_Core/<NN>/01_B3_AGENT_ROSTER.md`) faithfully transcribe the **Notion
  `AGENT_REGISTRY_DB`** (4–10 named members per squad).

The divergence was catalogued in
`LLM_Wiki/wiki/comparisons/comparison_l2_roster_divergence.md` (2026-05-31, then
`AWAITING_A0_RULING`). It found:

- **6 of 8 squads**: `AGENTS.md` is a 4-member **subset/abbreviation** of a larger Notion roster
  (Ops happens to be 4, so it aligns). An index, not a contradiction.
- **2 of 8 are genuine contradictions** that cannot both be right:
  - **Finance / Thunderbolts** — `AGENTS.md`: Red Hulk, Taskmaster, Zemo, Ghost.
    Notion: **Bucky Barnes, Yelena Belova, Red Guardian, Ghost, Taskmaster, U.S. Agent**
    (different team composition — only Ghost + Taskmaster overlap).
  - **Sales / Illuminati** — `AGENTS.md`: generic `Illuminati I–V`.
    Notion: **Black Bolt, Iron Man, Mr Fantastic, Namor, Professor X, Doctor Strange** (named).

All eight 2026-05-31 B2 doctrines + B3 JTBD packets were already built on the **full Notion
rosters**. Verification 2026-06-02 confirmed **no working doctrine surface carries the old
divergent names** — the only surface still divergent is `AGENTS.md` itself.

## Decision

1. **Source of truth for L2 B3 squad roster *lore* (membership + names) = Notion
   `AGENT_REGISTRY_DB` and its faithful local transcriptions** (the `00_B3_SQUAD_CANON.md` /
   `01_B3_AGENT_ROSTER.md` files). Where Notion and any other surface diverge on *who is in a
   squad* or *what they are called*, **Notion wins**.

2. **`AGENTS.md` remains canonical for structure** — the A0–A3 hierarchy, sector→manager→squad
   mapping, SOA codes, and file-path wiring. Its abbreviated squad lists are to be read as an
   **index**, not the authoritative membership.

3. **The two genuine divergences are resolved in Notion's favour, definitively:**
   - Finance/Thunderbolts canonical roster = **Bucky Barnes · Yelena Belova · Red Guardian ·
     Ghost · Taskmaster · U.S. Agent** (Bucky-led). The Red Hulk / Zemo composition is **retired.**
   - Sales/Illuminati canonical roster = **Black Bolt · Iron Man · Mr Fantastic · Namor ·
     Professor X · Doctor Strange** (Black Bolt-led). The generic `Illuminati I–V` labels are
     **retired.**

4. **`AGENTS.md` is corrected by an additive, dated Reconciliation Addendum** that references this
   ADR and restates the eight full canonical rosters — **not** a silent rewrite of its body (the
   original lines stay for history; the addendum supersedes them for roster lore). This honours the
   immutability convention (never rewrite canon; record supersession explicitly).

5. **Notion stays the upstream authority.** The transcriptions are downstream copies; if Notion
   `AGENT_REGISTRY_DB` changes, the transcriptions + this ADR's roster list must be re-synced. One
   datum, one owner (ADR-MESH-L2-001 spirit): the owner is Notion.

## The eight canonical rosters (Notion `AGENT_REGISTRY_DB`)

| Sector (B2 manager) | Squad | Lead | Members |
|---|---|---|---|
| Growth (Superman) | Guardians of the Galaxy (6) | Star-Lord | Star-Lord · Gamora · Rocket · Groot · Drax · Mantis |
| Sales (John Jones / Martian Manhunter) | Illuminati (6) | Black Bolt | Black Bolt · Iron Man · Mr Fantastic · Namor · Professor X · Doctor Strange |
| Product (Flash) | The Avengers (7) | Captain America | Captain America · Iron Man · Thor · Hulk · Black Widow · Hawkeye · Scarlet Witch |
| Ops (Batman) | Fantastic Four (4) | Mr Fantastic | Mr Fantastic · Invisible Woman · Human Torch · The Thing |
| IT (Cyborg) | Kang Dynasty (6) | Kang Prime | Kang Prime · Iron Lad · Scarlet Centurion · Immortus · Victor Timely · Rama-Tut |
| Finance (Wonder Woman) | Thunderbolts (6) | Bucky Barnes | Bucky Barnes · Yelena Belova · Red Guardian · Ghost · Taskmaster · U.S. Agent |
| People (Green Lantern) | X-Men (8) | Professor X | Professor X · Cyclops · Jean Grey · Wolverine · Storm · Beast · Nightcrawler · Rogue |
| Legal (Aquaman) | Eternals (10) | Ikaris | Ikaris · Sersi · Ajak · Kingo · Phastos · Sprite · Druig · Thena · Gilgamesh · Makkari |

> **Intentional cross-casting:** Iron Man, Mr Fantastic and Professor X each appear in **two**
> squads — the Sales/Illuminati "secret council" borrows archetypes from Product/Ops/People. This
> is canon lore in Notion, not an error.

## Consequences

- ✅ One unambiguous roster across the OS; the 2026-05-31 doctrines + JTBD packets are now formally
  blessed (they already used these rosters).
- ✅ `AGENTS.md` immutability preserved (additive addendum, history intact).
- ✅ Future agent-capsule files (`agents/L2_A3_*.md`) should be created/renamed against this roster
  (e.g. Finance squad capsules = Bucky/Yelena/Red Guardian/U.S. Agent, not Red Hulk/Zemo). This is a
  **follow-up housekeeping task**, not blocking.
- ⚠️ Notion remains the editable upstream; drift requires re-sync of transcriptions + this table.

## Related

- `LLM_Wiki/wiki/comparisons/comparison_l2_roster_divergence.md` (now `RULED`)
- `00_Amadeus/01_Identity_Core/AGENTS.md` (Reconciliation Addendum appended 2026-06-02)
- `LLM_Wiki/wiki/concepts/concept_l2_fractal_b1b2b3.md` (the B1/B2/B3 stack these squads sit in)
- ADR-MESH-L2-001 (one datum, one owner — applied here: roster owner = Notion)
