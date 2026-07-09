# JTBD-002 AAAS Transverse Sales Revenue Gate

## Job

When 00 Agency as a Service prepares any proposal, quote, commitment, sales script, close motion, or revenue handoff, Sales must verify qualification and cross-domain readiness.

## Output

A dated Sales readiness decision:

- `SALES_READY`
- `NEEDS_QUALIFICATION`
- `BLOCKED_COMMITMENT`

## Readiness Checks

| Check | Question | Current Proof |
| --- | --- | --- |
| Diagnostic | What pain/fit evidence exists? | Diagnostic questions and qualification script in `JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` |
| Authority | Who can decide? | Qualification section asks for economic buyer, operator, and approval path |
| Scope | What is included/excluded? | Proposal boundary names diagnostic sprint, system map, operating cockpit, and exclusions |
| Price | What is quoted and approved? | Pricing architecture only; final dollars wait for Finance JTBD |
| Delivery | Can Product/Ops deliver? | Internal handoff required before external send |
| Legal | Are claims/terms safe? | Claims and terms are bounded; external send waits Legal JTBD |
| Handoff | Who owns next step? | B2 Sales owner and cross-domain handoff table named |

## Guardrail

No proposal may be sent externally without qualified pain, scope, price boundary, delivery feasibility, terms, and owner handoff.

## Decision

`SALES_READY_INTERNAL`

The Sales gate passes for internal diagnostic and proposal production. External proposal send remains gated by Product, Ops, Finance, and Legal proof.

## Proof

- `JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md`
- `04_AAAS_SALES_ROCK.md`
- `05_AAAS_SALES_TRANSVERSE_REVENUE_HANDOFF_OS.md`
- `06_AAAS_B2_B3_SALES_PROPOSAL_PROTOCOL.md`
