---
id: B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX
layer: B2_MESO_COORDINATION
surface: 05_Marina
surface_kind: QuickAccess Mirror
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# B2 Business Wheel Harmonization Matrix

This matrix prevents one strong domain from masking weak business readiness elsewhere.

## Domain Pair Checks

| Pair | Question | Escalation if unresolved |
|---|---|---|
| Growth + Sales | Is attention becoming qualified opportunity? | B2 Council |
| Sales + Ops | Can promises be delivered repeatedly? | B2 Council |
| Product + Ops | Is the artifact operationally supportable? | B2 Council |
| Product + IT | Can the product run, deploy, recover, and be accessed? | B2 Council |
| Finance + Growth | Is spend justified by learning or traction? | B2 Council |
| Finance + Product | Does build cost protect margin? | B2 Council |
| Legal + Growth | Are claims safe? | B2 Council |
| Legal + Product | Are IP/privacy/terms boundaries clear? | B2 Council |
| People + All | Is ownership and load sustainable? | B2 Council or B1 if structural |


## Ops Transverse Gate

Ops/Batman runs the final transverse launch gate after the pair checks. A domain can be individually `CONDITIONAL`, but the whole project cannot launch unless Ops can name:

- the delivery phase affected;
- the owner;
- the risk;
- the rollback/exception path;
- the date of next review.

Project-specific constraint: Field delivery is the product: safety, equipment, crew load, weather, QA, and client satisfaction must be operationally visible.

If Ops cannot name those fields, the whole wheel is `BLOCKED`, even if Product, Growth, or Sales are green.

## Red Flag Combinations

- Product green, Ops/IT red: do not launch.
- Growth green, Sales red: validate offer before scaling attention.
- Sales green, Ops/People red: delivery load risk.
- Finance red and Growth/Product green: slow down or reprice.
- Legal red with public-facing work: hold claims and launch.

## Review Cadence

- Weekly during active build cycles.
- Immediately before launch or public commitment.
- After any B3 blocker that touches another domain.
## People Agent Governance Gate

People Green Lantern is transverse for B2/B3 agent governance across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| B2 owner named | People + active domain | Accountable domain owner is explicit |
| B3 agent named | People + B3 swarm | Execution agent and backup are explicit |
| Decision rights clear | People + B1/B2 | Authority and approval path are explicit |
| Capacity checked | People | Agent load and overload risk are visible |
| Proof path defined | People + requesting domain | Artifact, log, or acceptance proof is named |
| Escalation path named | People + Donna/DLQ | Blocked work has a recovery owner |

No B3 task should move to Ops launch readiness until People has emitted ASSIGNED, NEEDS_OWNER, or DLQ.
## IT Systems Access Gate

IT Cyborg is transverse for systems, access, data, automation, runtime, support, and rollback across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| System owner named | IT + active domain | Tool/runtime owner is explicit |
| Access boundary clear | IT + People | Permissions and revocation path are explicit |
| Source of truth named | IT + active domain | Canonical record location is explicit |
| Data boundary defined | IT + Legal/Finance/Ops as needed | Sensitive data path is explicit |
| Automation boundary defined | IT + B2 owner | Human approval rule is explicit |
| Support and rollback named | IT + Ops | Failure route and rollback path are explicit |

No B3 task should move to People assignment or Ops launch readiness until IT has emitted SYSTEM_READY, NEEDS_SYSTEM_OWNER, or QUARANTINE where systems/data/access are involved.
## Growth Signal Gate

Growth Superman is transverse for market signal, VOC, ICP, positioning, channels, experiments, and learning loops across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| VOC evidence present | Growth + Sales/Product | Audience pain is sourced |
| ICP narrow enough | Growth + Sales | Qualified target is actionable |
| Promise boundary explicit | Growth + Product/Ops | Public promise maps to deliverable |
| Measurement path ready | Growth + IT | Tracking and source of truth are explicit |
| Budget/unit constraint clear | Growth + Finance | Spend or CAC boundary is explicit |
| Owner/reviewer named | Growth + People | Creator, owner, reviewer, learning owner are explicit |
| Claim/privacy safe | Growth + Legal | Message boundary is reviewed where sensitive |

No Growth motion should become public or feed Sales/Ops until Growth has emitted GROWTH_READY, NEEDS_SIGNAL, or BLOCKED_PROMISE.
## Legal Risk Gate

Legal Aquaman is transverse for claims, data, IP, contracts, authority, compliance, liability, and approval boundaries across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| Claim boundary explicit | Legal + Growth/Sales | Public promise is supported and bounded |
| Data/privacy path clear | Legal + IT/Ops | Storage, access, retention, and privacy boundary are explicit |
| IP/deliverable ownership clear | Legal + Product | Ownership, reuse, exclusions, and transfer are explicit |
| Terms/liability boundary clear | Legal + Sales/Ops/Finance | Commitments, refunds, safety, tax, and responsibility are explicit |
| Authority owner named | Legal + People/B1 | Approval/signature/commitment authority is explicit |
| Escalation path named | Legal + Donna/DLQ | Uncertain risk has a recovery owner |

No B3 task should become public, contractual, data-bearing, or externally binding until Legal has emitted LEGAL_READY, NEEDS_REVIEW, or BLOCKED_RISK.
## Finance Money Gate

Finance Wonder Woman is transverse for pricing, margin, budget, cash, costs, payment terms, refunds, tax/legal dependencies, approvals, and leakage across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| Price/budget explicit | Finance + active domain | Price, quote, budget, or spend cap is named |
| Cost model explicit | Finance + Ops/People/IT | Labor, tooling, supplies, compliance, and delivery costs are visible |
| Margin/cash clear | Finance | Margin, cash timing, and payment terms are explicit |
| Refund/exception path named | Finance + Sales/Ops/Legal | Refunds, failed delivery, and exceptions have a boundary |
| Approval owner named | Finance + B1/B2 | Spend, price, or payment authority is explicit |
| Leakage path named | Finance + Donna/DLQ | Unpriced labor or unsafe money risk has escalation |

No B3 task should become public, paid, billed, staffed, or financially binding until Finance has emitted FINANCE_READY, NEEDS_MODEL, or BLOCKED_LEAKAGE.
## Sales Revenue Gate

Sales Martian Manhunter is transverse for diagnostic, qualification, proposal, close, commitment, and revenue handoff across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| Diagnostic proof | Sales + Growth | Pain, fit, authority, and urgency are explicit |
| Scope and exclusions | Sales + Product | Offer boundary is explicit |
| Delivery feasible | Sales + Ops | Delivery owner and path are explicit |
| Price/terms approved | Sales + Finance/Legal | Quote, payment, terms, and claims are bounded |
| Handoff owner named | Sales + People | Next owner and proof path are explicit |

No proposal, quote, commitment, or revenue handoff proceeds until Sales has emitted SALES_READY, NEEDS_QUALIFICATION, or BLOCKED_COMMITMENT.
## Product Offer Gate

Product Flash is transverse for offer, package, MVP/demo, scope, QA, acceptance, and deliverable boundaries across the eight domains.

| Gate | Owner | Required Proof |
| --- | --- | --- |
| Scope explicit | Product + Sales/Growth | Included work and promise boundary are explicit |
| Exclusions explicit | Product | Non-goals and unsupported promises are explicit |
| Acceptance criteria | Product + Ops | Done/QA/proof path is explicit |
| Runtime and economics | Product + IT/Finance | System/data and price/margin boundaries are explicit |
| Ownership and legal | Product + People/Legal | Owner, reviewer, IP, and claims boundary are explicit |

No offer, demo, service package, deliverable, or Product-bound promise proceeds until Product has emitted PRODUCT_READY, NEEDS_SCOPE, or BLOCKED_DELIVERY.
