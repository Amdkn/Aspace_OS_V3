# AAAS Sales Transverse Revenue Handoff OS

## Purpose

Sales is the transverse revenue handoff gate for 00 Agency as a Service. It converts qualified demand into bounded proposals, commitments, and handoffs without breaking Growth, Product, Ops, IT, Finance, People, or Legal constraints.

## Operating Thesis

AaaS needs Sales to convert qualified demand into scoped proposals without selling delivery the system cannot fulfill.

## Eight-Domain Sales Interface

| Domain | Sales Surface | Required Proof |
| --- | --- | --- |
| Growth | Lead source, ICP, promise | Qualified signal and message boundary |
| Sales | Diagnostic, proposal, close path | Pain, scope, next step, decision criteria |
| Product | Offer scope and exclusions | Productized deliverable and fit proof |
| Ops | Delivery readiness | SOP/owner/timeline feasibility |
| IT | CRM, intake, proposal record | Source of truth and follow-up path |
| Finance | Price, margin, payment | Approved quote and terms |
| People | Sales owner/reviewer/support | Capacity and handoff owner |
| Legal | Claims, terms, commitment | Reviewed boundary for external promise |

## Sales Control Loop

1. Receive qualified signal from Growth or direct intake.
2. Diagnose pain, fit, urgency, authority, and constraints.
3. Match the need to a Product scope and exclusions.
4. Confirm Ops feasibility, IT record path, Finance quote, People owner, and Legal boundary.
5. Produce proposal or reject/return to qualification.
6. Record decision, handoff, and proof.

## Readiness States

- `SALES_READY`: proposal packet can proceed internally.
- `NEEDS_QUALIFICATION`: return to diagnostic, ICP, or pain proof.
- `BLOCKED_COMMITMENT`: route to Product, Ops, Finance, Legal, or B1 because the commitment is unsafe.

## Project Constraint

No proposal may be sent without qualified pain, scope, price boundary, delivery feasibility, terms, and owner handoff.

## Current Decision

`SALES_READY_INTERNAL`

Sales can now run a diagnostic and produce an internal proposal packet. External send remains blocked until the Product, Ops, Finance, and Legal JTBDs produce their own proof.
