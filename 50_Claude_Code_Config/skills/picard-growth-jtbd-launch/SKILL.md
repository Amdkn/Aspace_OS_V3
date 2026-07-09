---
name: picard-growth-jtbd-launch
description: >-
  Scaffold a complete Guardians of the Galaxy (Growth B3 swarm) JTBD pipeline for a PROJECT PICARD
  business project, mode-calibrated to Solaris / Nexus / Orbiter. Given a Picard project folder, its
  declared AaaS mode, and an existing JTBD-001 VOC packet, this generates the rest of the squad:
  JTBD-002 ICP filter (Gamora), JTBD-003 painkiller variants (Groot + Drax kill-gate), JTBD-004
  non-paid experiment + RICE (Rocket), then syncs the B2 extraction queue statuses and appends an
  Active State Log entry to the B3 shared proof log. USE THIS SKILL whenever the user asks to "launch
  the Guardians", "roll out the Growth squad", "finish the Growth JTBDs", "instantiate 002/003/004",
  "scaffold the Growth pipeline", or similar for any Picard/Summer project — even if they don't name
  the JTBD numbers. It bakes in the doctrine constraints (HYPOTHESIS evidence, anti-pattern P1/P2,
  zero external mutation, Superman-reserved P4/P5, Legal-gate for compliance-bound projects) so the
  artifacts are consistent every time.
---

# Picard Growth JTBD Launch — Guardians Squad Scaffold

## What this does and why

The Jerry Area (Spock) holds **perpetual Growth doctrine** (18 Superman principles + the canonical
Guardians GTM packet). PROJECT PICARD projects are **finite Summer projects** with graduation gates.
DRY rule: projects **reference** Area doctrine, they never re-derive it.

This skill takes a project that already has a **JTBD-001 VOC packet** (the voice-of-customer pains +
Process Com persona, owned by Mantis) and produces the rest of the Guardians pipeline so Superman can
greenlight the first non-paid Growth loop:

- **JTBD-002 — ICP filter** (Gamora): 3 explicit *rejection* criteria, mode-calibrated.
- **JTBD-003 — painkiller variants** (Groot): 3 testable message variants tied to P8/P16, with a Drax kill-gate.
- **JTBD-004 — non-paid experiment + RICE** (Rocket): channel hypothesis, RICE frame, lead/lag + build gate, kill rule.

Then it keeps the system consistent:
- Updates the **B2 `04_*GROWTH_EXTRACTION_QUEUE.md`** (002 `READY`→`REVIEW_READY`, 003 `BLOCKED-ON-001`→`REVIEW_READY (A0-unblocked)`, adds the 004 Rocket row with artifact paths).
- Appends an **Active State Log** entry to the **B3 `03_SHARED_CONTEXT_AND_PROOF_LOG.md`**.

The point is consistency at scale: every project's squad reads the same shape, carries the same proof
contract, and never fabricates evidence or silently mutates an external system.

## The Guardians squad (who owns what)

| Member | Role | Principles | Owns |
|---|---|---|---|
| Mantis | Voice-of-customer, persona, empathy | P7/P13/P16 | JTBD-001 (prerequisite) |
| Gamora | Précision tactique, ABM, entry filter | P1/P9/P11/P3 | JTBD-002 ICP filter |
| Groot | Content / brand voice / message | P8/P14/P16/P18 | JTBD-003 painkiller variants |
| Rocket | Growth hacks, automation, experiments | P6/P7/P12/P15/P14 | JTBD-004 experiment + RICE |
| Drax | A/B brutal, kills weak variants | P5/P6/P10 | kill-gate on 003 + 004 |
| Star-Lord | Lead gen, ICP hunter, outreach | P1/P9/P13 | support across 002–004 |

**Superman (B2 owner) is non-délégable on P4 (North Star definition) and P5 (RICE arbitrage).** The
squad never scores RICE itself or sets the North Star — it produces the inputs and leaves
`score: "à calculer par Superman (P5)"` and an unchecked `[ ] Acceptance Superman` in the DoD.

## Workflow

### Step 1 — Locate the project and confirm inputs

Picard projects live under:
`C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\<PROJECT FOLDER>\`

Project folder names contain **spaces and ampersands** (e.g. `02 ABC OS & Child Care BOS`,
`05 marina Cleaning BOS & SOP`). When using Bash, prefer `find`/`ls -d` with the full quoted
Unix-style path (`/c/Users/amado/...`) — `Glob` tends to time out on these paths. Read with the Read tool.

Confirm three things before generating:
1. **The mode** — Solaris (visual-first/brand-led), Nexus (data-first/expertise/community), or Orbiter (field-first/logistics/compliance-or-SOP). Read the project's `03_*GROWTH_PRINCIPLES_REF.md` frontmatter `mode:` field if unsure.
2. **JTBD-001 exists** — read `B3_Warp_Core_Execution/01_Growth_Superman_Guardians/JTBD-001_*_VOC_PACKET.md`. The 002/003/004 artifacts must trace to its PAIN-01..05 and persona. If it's missing, stop and say so — do not invent pains.
3. **The B2 Rock id** — read `B2_Business_Domains/01_Growth_Superman_Guardians/04_*GROWTH_EXTRACTION_QUEUE.md` for `rock_id` and the existing JTBD rows.

**JTBD ID scheme**: `<PROJECT>-<MODE>-B3-GROWTH-NNN` where mode code ∈ {SOL, NEX, ORB}. Match the prefix
already used in JTBD-001 (e.g. `MAR-ORB-B3-GROWTH-`).

### Step 2 — Read the mode calibration

Read the matching reference file. **This is what prevents verbatim copies** — each mode reframes the
North Star, the rejection criteria, the message angle, and the experiment channel differently:

- `references/mode-solaris.md` — visual-first / brand-led (StoryBrand, $100M Offers)
- `references/mode-nexus.md` — data-first / expertise / knowledge-community (Expert Secrets, Consulting Bible, E-Myth)
- `references/mode-orbiter.md` — field-first / logistics / SOP-replicable / compliance-bound (Built to Sell, Who Not How)

Also read `references/special-cases.md` for compliance-bound (Legal-gate) and THIN/DEFERRED projects.

### Step 3 — Generate the three artifacts

Write into `B3_Warp_Core_Execution/01_Growth_Superman_Guardians/` using the templates in
`references/artifact-templates.md`. Fill them from JTBD-001's actual pains/persona and the mode
calibration — do not paste another project's content. Each artifact carries:

- frontmatter: `evidence_grade: HYPOTHESIS`, `status: REVIEW_READY`, correct `jtbd_id`/`source_rock`/`guardian_lead`/`principles_ref`, and `context_pack: urn:aspace:rag:<project-slug>-growth` (the bridge id Symphony injects into a Guardian agent — see "Runtime consumer" below)
- a one-line Job statement + the HYPOTHESIS/anti-pattern P1/P2 banner
- the body (rejection criteria / variants / RICE+lead-lag) calibrated to the mode
- a Drax kill-gate (003, 004) and a productive-disagreement note where cost/promise/legal is at stake
- a handoff line and a DoD ending in `[ ] **Acceptance Superman**`

### Step 4 — Sync the B2 queue

Edit `04_*GROWTH_EXTRACTION_QUEUE.md`:
- 002: `READY` → `REVIEW_READY`, expand principles to `P1/P9/P11/P3`, add supports + artifact path.
- 003: `BLOCKED-ON-001` → `REVIEW_READY (A0-unblocked)`, principles `P8/P16/P18/P14`, add artifact path. Add `(Legal sign-off pending)` if compliance-bound.
- Add the 004 Rocket row: principles `P6/P7/P12/P15/P14`, artifact path, `REVIEW_READY (A0-unblocked)`.

The A0 directive is the authority that unblocks the dependency gate — that's why `BLOCKED-ON-001`
becomes `A0-unblocked` rather than waiting on formal JTBD-001 acceptance. Superman acceptance is still
pending (P5 reserved).

### Step 5 — Append the proof-log entry

Append an `## Active State Log` section (create it if the file is still the bare template) to
`B3_Warp_Core_Execution/01_Growth_Superman_Guardians/03_SHARED_CONTEXT_AND_PROOF_LOG.md`. Use the
YAML block in `references/artifact-templates.md` (§ proof-log entry): list all four artifact paths,
`peer_reviewed_by: Drax`, `evidence_grade: HYPOTHESIS`, the mode-specific lead/lag, and
`next_authority_needed: Superman acceptance` (plus `Legal sign-off (mandatory)` if compliance-bound).

**Metrics are pointers, never copies.** Per the tri-platform règle d'or (ADR-MESH-L2-001: Airtable =
HOW MUCH, one owner per datum), do NOT write a measured number (CPQL, pipeline value, RICE outcome) as
prose in the proof log. While the loop is `HYPOTHESIS` there is no real number yet — leave the lead/lag
as the *target* + `evidence: pending`. Once an experiment produces a real metric, the owner is the
Airtable Growth record (🦸 Leads & Audits / 💸 Sales Pipeline in base `appmWf5Xm7w9Ae0ky`); the proof
log then carries a **pointer** field: `airtable_record: rec... ` / its URL. See "Runtime consumer" below.

### Step 6 — Report

Summarize: which 3 artifacts were written, the queue diff, the proof-log entry, and the gates still
open (Superman acceptance; Legal if applicable). State explicitly that nothing external was mutated.

## Hard constraints (never violate)

These are the doctrine guardrails. They exist so the artifacts are trustworthy and safe — read them
as the *reason* the skill is useful, not red tape:

- **evidence_grade: HYPOTHESIS** — these are honest desk syntheses, not field-proven. Saying so is what makes them safe to act on. Never label a desk artifact as validated.
- **Anti-pattern P1/P2** — never propose scaling a *paid* channel before the non-paid loop shows a validated lead indicator. The whole Rock is "validate the first *non-paid* loop."
- **Zero external mutation** — no scraping, sending, posting, or writing to any external system (Apollo, LinkedIn, email, CRM) without explicit A0 approval **and** credential-safe execution. If an experiment needs it, gate it: `GATED on A0 sign-off + <credential>`.
- **P4/P5 reserved for Superman** — the squad never sets the North Star metric or computes the final RICE score. Leave them for Superman.
- **Legal-gate for compliance-bound projects** — childcare, regulated services, etc.: every public message routes through Legal (Aquaman/Eternals) before diffusion. Mark `legal_gate` in frontmatter and the queue.
- **Honesty for THIN/DEFERRED Growth** — if a project's Growth surface is thin (e.g. a holding/LLC with no customer funnel), do NOT fabricate customer pains. Reframe as reputational/positioning, declare lead/lag `N/A`, route the real work to its Jerry Area domain, and leave 002/003/004 **not instantiated**. See `references/special-cases.md`.
- **DRY** — reference Area doctrine (`03_*GROWTH_PRINCIPLES_REF.md` → Jerry Area principles), never re-derive the 18 principles inside a project artifact.

## Runtime consumer — the Symphony / Airtable bridge

The JTBD artifacts this skill produces are the **WHAT** (doctrine, file-based PARA). They are designed
to be *consumed* by a runtime: the **Symphony daemon** (`00_Amadeus/05_OSS_Twin/symphony/`, Shadow A0).
Symphony's **Airtable adapter** (`L2/symphony-airtable.spec.md`) has **Growth as its primary slot**, with
the **Gardiens de la Galaxie** as the named A3 squad — i.e. exactly this squad. Knowing this keeps the
artifacts runtime-ready instead of orphaned.

How the loop is meant to close (design-time today — Symphony is hors-canon, not yet live in prod):

1. A Growth record in Airtable enters an `active_state` (`New Lead → Qualified → Proposal Sent → In Production → Won/Lost`).
2. Symphony (webhook, 5-min polling backup) picks it up and builds a **SOC payload**: `SOA Domain="Growth"`, `forbidden_lexicon`, and **`context_pack_url`** = the `context_pack` id we stamped in the artifact frontmatter (`urn:aspace:rag:<project-slug>-growth`). **This pointer is the bridge** — it's how the file-based doctrine reaches the dispatched Guardian agent, with no copy.
3. Symphony dispatches a frugal Guardian agent (OpenHarness/MiniMax) into an isolated workspace; the agent operates the record **per the doctrine** and writes back to Airtable.

The JTBD gates map onto Airtable states — keep them aligned when you write the artifacts:

| Gate (doctrine, this skill) | Airtable runtime (Symphony adapter) |
|---|---|
| JTBD-002 Gamora ICP filter (reject → Lost) | `Qualified` / `Lost` transition |
| JTBD-003 brief approved | **Build Gate** (formula "Filtre Invisible Woman", table 🦇) |
| JTBD-004 Rocket experiment | record in `In Production` |
| lead/lag + RICE outcome | record field in 🦸 / 💸 (proof log = pointer) |

**Boundaries that stay true regardless of Symphony's status** (so this is safe to bake in now):
- **Symphony reads; the agent writes.** No bi-sync, no auto-creation of records (base spec §10.3, airtable §10). Consistent with ADR-MESH-L2-001 D5 (unidirectional flows).
- **L2 sandbox = `read_only` by default, write only on Build Gate approval** (base spec §14.2) — which is exactly the Trust Gating rule below: **any Airtable write requires A0 sign-off.**
- This skill **never writes to Airtable** and **never creates an ADR for Symphony** — Symphony is explicitly hors-canon / hors-Airlock, under a 90-day SDD veto. The bridge here is a Shadow-A0 *convention* (the `context_pack` stamp + the pointer pattern), not canon. If Symphony graduates MUSE (3 weeks stable), that's when a PRD/ADR is considered — by A0, not this skill.

## Reference files

- `references/artifact-templates.md` — the JTBD-002/003/004 + proof-log templates (read before writing)
- `references/mode-solaris.md` / `mode-nexus.md` / `mode-orbiter.md` — per-mode calibration
- `references/special-cases.md` — Legal-gate (compliance) and THIN/DEFERRED handling
