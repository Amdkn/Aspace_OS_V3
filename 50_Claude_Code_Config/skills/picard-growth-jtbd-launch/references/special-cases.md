# Special cases

## A. Compliance-bound projects (Legal-gate)

Trigger: regulated domain — childcare, health, finance, anything where a public claim can create
legal/regulatory exposure (e.g. ABC Child Care). The Rock's `definition_of_done` and queue will
mention Legal review.

What changes:
- Add `legal_gate: true` to JTBD-003 and JTBD-004 frontmatter.
- In JTBD-003 §3 (Drax kill-gate): add "killed if the promise contradicts regulation or can't be honored by Ops."
- No variant may claim anything that contradicts regulation. Frame on **trust + proof**, not superlatives.
- In the B2 queue, mark 003/004 `REVIEW_READY (A0-unblocked, Legal sign-off pending)` and add **Legal-gated** to the Output cell.
- In the proof-log entry: title gets ", Legal sign-off pending"; `next_authority_needed` includes "Legal sign-off (mandatory)"; `blocks_unblocks` notes "COMPLIANCE GATE — Legal (Aquaman/Eternals) sign-off required on any public message before diffusion".
- Add a note to the B2 queue's PARA note: "Contrainte transverse : handoff Legal (Aquaman/Eternals) sur tout message public."

The handoff is to the **Legal domain (Aquaman / Eternals squad)** — not Growth's call to waive.

## B. THIN / DEFERRED Growth surfaces

Trigger: the project has **no real customer funnel** — e.g. a holding company / LLC formation, an
internal-only entity, a positioning vehicle (e.g. Alikaly Bana Holding → LLC). Forcing a customer
VOC here would mean **fabricating pains**, which violates the proof contract.

What to do instead — **do NOT instantiate JTBD-002/003/004**:
- In `03_*GROWTH_PRINCIPLES_REF.md`, mark the Growth surface **THIN** and set `cross_jerry_routing:` to the relevant Jerry Area domain (e.g. J03).
- In `04_*GROWTH_EXTRACTION_QUEUE.md`, set the Rock `status: DEFERRED` and keep only **one thin JTBD-001** reframed as reputational/positioning — NOT customer pains. Declare Lead/Lag `N/A`.
- The thin JTBD-001 reframes "Growth" as positioning/deal-flow/reputation (e.g. POS-01/02/03 for counterparties), and **routes the real work to Jerry (J0x) / Legal**.
- Leave 002/003/004 explicitly **not instantiated** with a one-line reason. Only instantiate them later if an A0 reactivation trigger fires (the entity starts a real customer funnel).

The honesty here is the value: a DEFERRED-but-truthful queue is worth more than four fabricated artifacts.

## C. Duplicate / mirror folders

Some projects have both a spaced-name folder and a slug mirror (e.g. `01 OMK Business OS` and
`01-omk-business-os`, or `00 Agency as a Service` and `00_Summers_Verse`). Write to the **canonical**
folder the existing JTBD-001 and B2 queue already live in. If unsure, read the frontmatter `project:`
id of the JTBD-001 you're extending and match it. Don't duplicate artifacts across both mirrors.
