---
source: LLM_Wiki_A0
date: 2026-05-31
type: comparison
domain: L2_Business / Agent_Hierarchy / Canon_Reconciliation
status: RULED
ruled: 2026-06-02
ruling: "Notion AGENT_REGISTRY_DB + transcriptions = canon prime for roster lore. AGENTS.md = structure index. Finance→Bucky-led Thunderbolts; Sales→Black Bolt-led Illuminati. See ADR-CANON-001."
tags: [#comparison #roster #divergence #AGENTS_md #B3_squad #notion_registry #canon #ruled]
---

# Comparison: L2 squad roster divergence — `AGENTS.md` vs B3 squad canon

> **Why this exists.** Two canon surfaces describe the 8 L2 B3 squads and they **disagree**:
> the manifest `00_Amadeus/01_Identity_Core/AGENTS.md` lists **abbreviated 4-member** squads, while
> each `B2_Area_Domains/<NN>/B3_Squad_<X>/00_B3_SQUAD_CANON.md` + `B3_Area_Warp_Core/<NN>/01_B3_AGENT_ROSTER.md`
> transcribes the **full Notion `AGENTS_REGISTRY_DB`** (4–10 members). The B3 rosters themselves rule:
> *"if Notion and local doctrine diverge, Notion wins for lore; local doctrine wins for paths."*
> ⚠️ `AGENTS.md` is immutable canon — this doc **recommends**, A0 **rules** (any change = new ADR).

## Divergence table

| Domain / Squad | `AGENTS.md` manifest (abbrev.) | B3 roster = Notion canon (full) | Verdict |
|---|---|---|---|
| Growth / Guardians | Star-Lord, Rocket, Gamora, Groot (4) | + **Drax, Mantis** (6) | manifest = subset |
| Sales / Illuminati | Illuminati I–V (5, **generic role names**) | **Black Bolt, Iron Man, Mr Fantastic, Namor, Professor X, Doctor Strange** (6, named) | **naming divergence** — canon names win |
| Product / Avengers | Cap, Iron Man, Thor, Black Widow (4) | + **Hulk, Hawkeye, Scarlet Witch** (7) | manifest = subset |
| Ops / Fantastic Four | Mr Fantastic, Inv. Woman, The Thing, Human Torch (4) | same (4) | ✅ aligned |
| IT / Kang Dynasty | Kang, Immortus, Iron Lad, Rama-Tut (4) | **Kang Prime**, Iron Lad, **Scarlet Centurion**, Immortus, **Victor Timely**, Rama-Tut (6) | subset + "Kang"→"Kang Prime" |
| Finance / Thunderbolts | **Red Hulk, Taskmaster, Zemo, Ghost** (4) | **Bucky Barnes, Yelena Belova, Red Guardian, Ghost, Taskmaster, U.S. Agent** (6) | **REAL divergence** — only Ghost+Taskmaster overlap |
| People / X-Men | Prof X, Cyclops, Jean, Beast (4) | + **Wolverine, Storm, Nightcrawler, Rogue** (8) | manifest = subset |
| Legal / Eternals | Ikaris, Ajak, Phastos, Thena (4) | + **Sersi, Kingo, Sprite, Druig, Gilgamesh, Makkari** (10) | manifest = subset |

## Pattern

- 6 of 8 squads: `AGENTS.md` is a **4-member abbreviation** of a larger Notion roster (Ops happens to
  be 4, so it aligns). Not a contradiction — an index vs the full registry.
- **2 of 8 are genuine divergences**: **Sales** (generic `Illuminati I–V` vs named characters) and
  **Finance** (Red Hulk/Zemo manifest vs Bucky/Yelena/Red Guardian/U.S. Agent canon — the
  *Thunderbolts* team composition differs). These can't both be right.

## ✅ RULING (A0, 2026-06-02) — recorded in ADR-CANON-001

A0 ruled: **the canon stays Notion and its transcription**, and the divergences are corrected
definitively (not merely documented). Outcome:

1. **Notion `AGENT_REGISTRY_DB` + its faithful transcriptions = source of truth for roster lore.**
2. **AGENTS.md = structure index** (immutable body preserved); a dated **Reconciliation Addendum**
   (ADR-CANON-001) was appended restating the 8 full canonical rosters.
3. **2 genuine divergences resolved in Notion's favour:** Finance → **Bucky-led Thunderbolts**
   (Bucky · Yelena · Red Guardian · Ghost · Taskmaster · U.S. Agent; Red Hulk/Zemo retired);
   Sales → **Black Bolt-led Illuminati** (named members; generic Illuminati I–V retired).
4. Verification 2026-06-02: **no working doctrine surface carried the old names** — only AGENTS.md
   did, now reconciled. Follow-up (non-blocking): rename/align the `agents/L2_A3_*.md` capsule files.

→ Formal record: `_SPECS/ADR/ADR-CANON-001_roster-source-of-truth.md`.

---

## Recommendation (superseded by RULING above — kept for history)

1. **Source of truth = the B3 rosters / Notion `AGENTS_REGISTRY_DB`** (already the rule in-file). The
   8 doctrines + JTBD packets built 2026-05-31 use these full rosters.
2. **`AGENTS.md` stays immutable**; treat its squad lists as an **abbreviated index**. If A0 wants
   alignment, spawn a **new ADR** (e.g. `ADR-CANON-00X_roster-source-of-truth`) declaring Notion
   prime + adding a one-line pointer in AGENTS.md to the B3 rosters — never a silent rewrite.
3. **Resolve the 2 real divergences explicitly**: confirm Finance/Thunderbolts membership
   (Bucky-led canon vs Red-Hulk manifest) and Sales/Illuminati naming (named vs generic) — A0's call,
   then reflect the ruling in the new ADR.

## Full canon rosters (Notion — used by the 2026-05-31 doctrines)

- Growth/Guardians (6): Star-Lord · Gamora · Rocket · Groot · Drax · Mantis
- Sales/Illuminati (6): Black Bolt · Iron Man · Mr Fantastic · Namor · Professor X · Doctor Strange
- Product/Avengers (7): Captain America · Iron Man · Thor · Hulk · Black Widow · Hawkeye · Scarlet Witch
- Ops/Fantastic Four (4): Mr Fantastic · Invisible Woman · Human Torch · The Thing
- IT/Kang Dynasty (6): Kang Prime · Iron Lad · Scarlet Centurion · Immortus · Victor Timely · Rama-Tut
- Finance/Thunderbolts (6): Bucky Barnes · Yelena Belova · Red Guardian · Ghost · Taskmaster · U.S. Agent
- People/X-Men (8): Professor X · Cyclops · Jean Grey · Wolverine · Storm · Beast · Nightcrawler · Rogue
- Legal/Eternals (10): Ikaris · Sersi · Ajak · Kingo · Phastos · Sprite · Druig · Thena · Gilgamesh · Makkari

> Note: Iron Man, Mr Fantestic, Professor X appear in **two** squads (Sales Illuminati borrows the
> "secret council" archetypes). That's intentional cross-casting in the Notion lore, not an error.

---

## Inbounds
- [[concept_l2_fractal_b1b2b3]] — the B1/B2/B3 stack these squads (B3) sit in
- `01_Identity_Core/AGENTS.md` — the manifest being reconciled
