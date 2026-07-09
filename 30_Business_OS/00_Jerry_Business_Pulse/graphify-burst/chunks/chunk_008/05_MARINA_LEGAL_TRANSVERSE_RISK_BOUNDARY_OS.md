# MARINA Legal Transverse Risk Boundary OS  ## Purpose Legal is the transverse risk gate for 05 Marina Cleaning BOS & SOP. It ensures claims, data, IP, compliance, contracts, authority, liability, and approval boundaries are explicit before B2/B3 work becomes public or operational.  ## Operating Thesis Marina needs Legal to make service terms, insurance, liability, safety, client permissions, worker boundaries, and claims explicit before field delivery.  ## Eight-Domain Legal Interface | Domain | Legal Surface | Required Proof | | --- | --- | --- |
| Growth | Public claims, campaigns, privacy, endorsements | Approved claim boundary and privacy note |
| Sales | Offers, quotes, intake, terms, client commitments | Terms boundary and accepted responsibility |
| Product | IP, deliverables, exclusions, warranties | Ownership and scope/exclusion proof |
| Ops | SOPs, incidents, liability, safety, records | Liability/safety/escalation boundary |
| IT | Data handling, access, records, retention | Privacy/storage/access boundary |
| Finance | Billing, refunds, taxes, entity obligations | Payment/refund/tax responsibility boundary |
| People | Roles, contractors, consent, training, authority | Role authority and worker/agent boundary |
| Legal | Compliance, contracts, IP, defense, approvals | Legal review queue and decision log |

## Legal Control Loop
1. Identify the claim, data path, contract, IP, authority, or liability surface.
2. Name the responsible B2 owner and B3 agent.
3. Define the legal boundary: allowed, conditional, blocked, or needs external professional review.
4. Confirm related Ops, IT, Finance, People, Growth, Sales, and Product dependencies.
5. Record decision, proof, and escalation route.
6. Route uncertain or unsafe work to Donna/DLQ.
7. Emit the Legal readiness decision before launch or transfer.

## Readiness States
- LEGAL_READY: work can proceed inside the named boundary.
- NEEDS_REVIEW: return to B2/Legal queue for clarification or external review.
- BLOCKED_RISK: route to Donna/DLQ or B1 because risk/authority is unsafe.

## Project Constraint
No field job or client promise may launch without service terms, safety/liability boundary, insurance/permission check, and escalation path.

## Legal Metrics
- Open legal boundaries.
- Claims awaiting review.
- Data/IP/contract exceptions.
- Blocked-risk count.
- Decision log freshness.
- External-review dependencies.