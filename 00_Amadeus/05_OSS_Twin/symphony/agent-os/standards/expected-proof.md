---
title: Expected Proof
---

> A Symphony tick is **not done** until the `expected_proof` list is
> fully delivered. No proof, no PASS.

## The 4 canonical proof types

```yaml
expected_proof:
  - client_or_pipeline_summary        # (1) What is this client/record about?
  - recommendation_or_deliverable     # (2) What should A0 do with it?
  - risk_and_blocker_notes            # (3) What could go wrong?
  - gate_decision                     # (4) PASS / BLOCKED / CONDITIONAL
```

## Per-type shape

### (1) `client_or_pipeline_summary`

- 2-5 sentences
- Identifies: client/company name, what they want, where they are in
  the pipeline, the relevant context pack URL
- No buzzwords, no marketing fluff — see `forbidden-words.md`

### (2) `recommendation_or_deliverable`

- Concrete next action: "send proposal X" / "schedule call at time Y"
  / "block until client provides Z" / "produce deliverable D"
- Includes a **draft** if applicable (proposal text, email body, SOP
  outline) — drafts are `allowed_draft_outputs`
- Always names the human-in-the-loop (A0) for final approval

### (3) `risk_and_blocker_notes`

- 1-3 bullets
- Categories: `access` (no permission), `input` (waiting on client),
  `legal` (RGPD/compliance), `finance` (budget), `approval` (needs
  signoff), `external` (third-party blocker)
- If empty, the agent must explicitly say "no risks identified" (not
  just omit the field)

### (4) `gate_decision`

- One of PASS / BLOCKED / CONDITIONAL (see `gate-decisions.md`)
- Includes the reasoning: why this gate, not another
- CONDITIONAL MUST include re-trigger condition

## Where the proof goes

- **In the tick's `EXECUTE → OBSERVE → SIGNAL` phases** — the agent
  builds the proof as it works
- **Final write** — proof + decision + writeback in the SIGNAL phase
- **Airtable update** — only if `writeback_policy` allows (requires
  greenlight for most writes)
- **pulse.log** — final line of the tick includes the decision

## Why this exact 4

- (1) Without summary, the gate is in a vacuum
- (2) Without recommendation, the gate is a status report (useless)
- (3) Without risk, A0 flies blind on what could fail
- (4) Without decision, nothing to schedule / dispatch / close

The 4 together = "A0 can read this in 90 seconds and know whether to
act, wait, or intervene".

## Anti-patterns

- ❌ Skipping (3) when there are no risks — empty = "no risks
  identified", not absent
- ❌ Bundling all 4 in one paragraph (each must be parseable separately
  for downstream automation)
- ❌ Putting the proof in the comment of a code block (humans won't see
  it; automation can't parse it)
- ❌ A "proof" that's just the source record's Description field
  copy-pasted (= no work done by the agent)

## Cross-refs

- `mission-contract.md` — `expected_proof` field
- `gate-decisions.md` — proof type (4)
- `writeback-policy.md` — proof as `allowed_draft_outputs`
- `forbidden-words.md` — proof must pass lexique scan
