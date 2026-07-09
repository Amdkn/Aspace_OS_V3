# Doctrine output template

The canonical structure for `03_<HERO>_<DOMAIN>_PRINCIPLES.md`. Match the voice of
the existing siblings (`03_SUPERMAN_GROWTH_PRINCIPLES.md`, `03_FLASH_PRODUCT_PRINCIPLES.md`,
`03_BATMAN_OPS_PRINCIPLES.md`) — read one before writing.

## Frontmatter (keep these keys)

```yaml
---
source: A0_Amadeus_Canon
date: <YYYY-MM-DD>
type: area_domain_principles
domain: L2_Business / <Domain> / Jerry_Prime_LD01
tags: [#<domain> #<hero> #<squad> #principles #jerry_area #perpetual_doctrine ...]
guardian: <Hero> (A2)
squad: The <Squad> (<real members from B3 squad canon>)
status: CANONICAL | DRAFT_V1_DÉBUT | DRAFT_PENDING_CORPUS
source_corpus: <NN>_<Domain> (Geordi Guides — <named channels/authors>)
distillation: v1 | v2 (<n principes> ; <backlog note>)
---
```

## Body sections (in this order)

```markdown
# <emoji> <HERO> <DOMAIN> PRINCIPLES — Jerry Area Perpetual Doctrine[ (v1 — DÉBUT)]

> **Layer** : L2 Business / Jerry Area (Spock) / Domain <NN> <Domain>
> **Guardian** : <Hero> (A2) commanding the <Squad> (A3 squad)
> **Nature** : PERPETUAL doctrine — Areas never "complete", they are maintained.
> **DRY contract** : Picard projects REFERENCE these principles; they never re-derive them.

---

## What this is[ — and its honest status]
<1 para: what was distilled, from which corpus. 1 para: this domain's question vs its
neighbours, and the North Star (quote the real KR). If début/pending, say so plainly here.>

---

## The <N> <Hero> <Domain> Principles[ (v1)]

### Cluster <X> — <name> — <squad member(s)>
**P1 — <bold claim>.** <why it matters, 1-3 sentences>
  - optional tags: AARRR/lifecycle stage · squad lead · KR served
**P2 — …**
…
(use the corpus's own framework as the cluster spine when it has one — e.g. DEAL for Ops)

---

## How the squad applies these
<table: squad member → focus → principle numbers. Members are CANON from the B3 squad
file — do not invent. Mark provisional roles as provisional.>

**<Hero> (B2 owner) is non-délégable on <1-2 reserved decisions>.** The squad proposes;
<Hero> arbitrates, leaving an unchecked `[ ] Acceptance <Hero>` in each DoD.

---

## <Domain> ↔ <neighbours> boundary
<how this domain differs so domains don't collide. One datum, one owner
(ADR-MESH-L2-001) — domains point, never copy.>

---

## Anti-patterns (<domain> sins <Hero> forbids)
<numbered list, each citing which principle(s) it violates; include the universal
"fabricating a proof of execution → Donna/DLQ" one.>

---

## Mesh anchoring (where these become operational)
<Notion SOP DB / ClickUp / Airtable / Symphony / Supabase — how the principles show up
in the L2 tooling mesh. Pointers, not copies.>

---

## Extension plan / backlog   (if not yet complete)
<table of next sources → likely future principles; bump distillation to vN next time.>

---

## DRY references
- Sibling doctrine: <links to the other 03_*_PRINCIPLES.md>
- Domain identity / KRs: 00_B2_DOMAIN_CONTROL_ROOM.md + README.md
- Squad canon: B3_Squad_<Squad>/00_B3_SQUAD_CANON.md
- Projects reference via 03_<DOMAIN>_PRINCIPLES_REF.md (when instantiated)

## Sources distilled
<bullet list mapping each resource file → the principles it produced. This is the
proof trail; keep it honest and specific.>

*Perpetual doctrine — maintained by Spock (Jerry Area A2) under <Hero>. Distilled from
<real corpus / N sources>, <date>.[ Extensible.]*
```

## Companion README (short)

```markdown
# <emoji> <Domain> Domain — <Hero> & The <Squad>
> Jerry Area (Spock) · L2 Business · Domain <NN> <Domain>

## Files
- `03_<HERO>_<DOMAIN>_PRINCIPLES.md` — the <N> perpetual principles (WHY/WHAT). **Start here.** Status: <status>.

## Squad
<Hero> (A2) commands the <Squad> (A3): <members + one-word roles>.

## North Star
<the domain North Star in one line>.

## DRY
<one-line boundary vs neighbours>. One datum, one owner (ADR-MESH-L2-001).

*Perpetual doctrine — maintained by Spock under <Hero>. Distilled from <corpus>.*
```

## Filled mini-example (Ops, abbreviated — see the real file for full)

```markdown
**P1 — Tacit → Explicit (SOPs are the foundation).** Convert tribal knowledge in the
founder's head into documented, versioned SOPs. Knowledge that lives only in a person
is a single point of failure.
...
| Mr. Fantastic | Systems architecture, SOPs, process mapping | P1, P2, P3, P5, P12, P13 |
| Invisible Woman | **Build Gate / QA / exception handling** (grounded: "Filtre Invisible Woman") | P6, P8, P16 |
```
