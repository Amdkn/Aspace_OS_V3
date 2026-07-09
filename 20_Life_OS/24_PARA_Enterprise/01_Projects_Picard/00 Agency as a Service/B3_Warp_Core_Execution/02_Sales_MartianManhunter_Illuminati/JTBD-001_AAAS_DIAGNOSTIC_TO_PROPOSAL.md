---
id: AAAS_B3_SALES_001
jtbd_id: AAAS-B3-SALES-001
source_rock: AAAS_B2_SALES_ROCK_2026_01
domain: Sales
b2_owner: Martian Manhunter
b3_swarm: Illuminati
status: PASS_INTERNAL
decision_date: 2026-06-02
---

# JTBD-001 - AAAS Diagnostic To Proposal

## Job

When 00 Agency as a Service receives a qualified signal or opportunity, produce the diagnostic-to-proposal packet so Sales can decide whether to propose, reject, or return the work for more proof.

## Gate Decision

`PASS_INTERNAL`

Sales can now run a diagnostic, qualify an opportunity, produce an internal proposal packet, handle objections, and hand off the work to Product, Ops, Finance, Legal, IT, People, and Growth.

External proposal sending remains gated by Product, Ops, Finance, and Legal proof. Sales is not blocked; external commitment is gated.

## Sales Packet

```yaml
project: "00 Agency as a Service"
b2_owner: "Martian Manhunter"
b3_swarm: "Illuminati"
lead_source: "Growth-qualified signal, direct founder/operator request, or internal A'Space business need"
diagnostic_evidence: "Qualification questions, pain map, current workflow map, and desired outcome"
pain: "Founder/operator has revenue intent but no repeatable agency delivery system"
icp_or_fit: "Solo founder, small operator, local-service owner, creator/operator, or micro-agency that needs an AI-assisted operating layer"
offer_scope: "AaaS Diagnostic Sprint -> Business OS Map -> Delivery SOP -> Operating Cockpit -> Launch Handoff"
exclusions: "No custom enterprise transformation, no legal/tax advice, no unmanaged client data handling, no guaranteed revenue claim"
price_or_terms: "Pricing architecture only until Finance passes: diagnostic sprint, build sprint, managed ops retainer"
delivery_feasibility: "Internal feasible if Product defines offer, Ops defines SOP, IT defines runtime, People names owners"
legal_boundary: "No public guarantee; all claims framed as system-building and operating support, not promised outcomes"
handoff_owner: "Sales B2 owner hands to Product/Ops/Finance/Legal before external send"
proof_required: "This JTBD packet plus cross-domain gate approvals"
decision: "PASS_INTERNAL; external send gated"
```

## Qualification Questions

### Pain And Urgency

1. What business workflow is currently stuck in your head, inbox, notes, or manual follow-up?
2. What breaks when you try to sell, deliver, or delegate this work repeatedly?
3. What is the cost of keeping this workflow manual for another 30 days?
4. Which part is most painful: offer clarity, lead intake, delivery SOP, follow-up, reporting, billing, or team handoff?

### Fit And Scope

1. Is this a repeatable service or workflow, or a one-off custom project?
2. What must be visible every week for you to trust the system?
3. What tools, documents, client records, or automations already exist?
4. What should not be automated or delegated yet?

### Authority And Decision Path

1. Who owns the business decision?
2. Who owns daily execution after setup?
3. Who approves price, data access, client-facing language, and process changes?
4. What would make this a no-go?

### Success Criteria

1. What would make the diagnostic sprint obviously useful?
2. What output would let you sell or deliver with less interpretation?
3. What would prove the system is ready for the first real client/workflow?

## Diagnostic Agenda

| Segment | Time | Purpose | Output |
| --- | --- | --- | --- |
| Context | 5 min | Name business model and current bottleneck | Current-state note |
| Workflow Walkthrough | 10 min | Trace lead -> sale -> delivery -> payment -> follow-up | Workflow map |
| Pain Ranking | 10 min | Rank operational pain and revenue leakage | Pain priority |
| Boundary Check | 10 min | Identify data, legal, pricing, tooling, and people risks | Risk list |
| Fit Decision | 5 min | Decide propose, reject, or request more proof | Sales decision |
| Next Step | 5 min | Name handoff owner and evidence needed | Handoff packet |

## Proposal Boundary

### Internal Proposal Frame

**Offer name:** Agency as a Service Diagnostic Sprint

**Core promise:** Turn a founder/operator's repeatable service workflow into a bounded operating system map that can be sold, delivered, delegated, and improved.

**Primary outputs:**

1. Business workflow map.
2. Offer and intake boundary.
3. Delivery SOP skeleton.
4. B2/B3 domain risk map.
5. Tool/runtime boundary.
6. Price/margin hypothesis handoff.
7. Legal/claims/data boundary handoff.
8. Next sprint recommendation.

### Exclusions

- No guaranteed revenue result.
- No legal, tax, compliance, or accounting advice.
- No unmanaged access to sensitive client systems.
- No custom software build unless Product and IT pass their gates.
- No external proposal send until Finance and Legal approve price/terms/claims.

## Objection Handling

| Objection | Response Boundary | Handoff |
| --- | --- | --- |
| "I need leads, not systems." | Leads without repeatable delivery create leakage; diagnostic identifies whether Sales/Growth or Ops is the first constraint. | Growth + Ops |
| "Can you automate everything?" | Automation follows mapped process and ownership. We do not automate unclear judgment. | IT + Ops |
| "Can you guarantee revenue?" | No. We can create a clearer operating system, proposal path, and delivery structure. | Legal + Finance |
| "This sounds too abstract." | Sprint outputs are concrete: workflow map, SOP skeleton, offer boundary, and next-step decision. | Product + Ops |
| "What will it cost?" | Sales can explain pricing architecture; Finance sets final price/margin/payment boundary. | Finance |
| "Who runs it after setup?" | People and Ops name owner/operator/reviewer and support path before launch. | People + Ops |

## Cross-Domain Handoff

| Domain | Handoff Question | Required Before External Send |
| --- | --- | --- |
| Growth | Is the audience/promise supported by VOC or signal? | ICP and message boundary |
| Product | What exactly is the package/demo/deliverable? | Scope, exclusions, acceptance criteria |
| Ops | Can the workflow be delivered repeatedly? | SOP, owner, timeline, exception path |
| IT | Where does intake, CRM, data, and proof live? | Source of truth and access boundary |
| Finance | What is the price, cost, margin, and payment term? | Approved price/payment model |
| People | Who owns sale, delivery, review, and support? | Owner/operator/reviewer map |
| Legal | Are claims, terms, data, and IP safe? | Claims/terms/data boundary |

## Decision Log

| Date | Decision | Reason | Next Owner |
| --- | --- | --- | --- |
| 2026-06-02 | `PASS_INTERNAL` | Sales packet, diagnostic questions, agenda, proposal boundary, objections, and handoff proof are present. | Product/Ops/Finance/Legal for external-send gates |

## PASS / BLOCKED Criteria

### Sales PASS

Sales is `PASS` when the project has:

- qualification questions;
- diagnostic agenda;
- proposal boundary;
- objections and response boundaries;
- cross-domain handoff map;
- decision log;
- explicit statement that external sending waits for other gates.

### Sales BLOCKED

Sales becomes `BLOCKED` if:

- the offer cannot name an ICP or pain;
- the proposal requires unbounded Product/Ops delivery;
- Finance cannot price it;
- Legal blocks the claims/terms;
- no owner exists for follow-up.

## Proof

This file is the produced Sales proof for `AAAS-B3-SALES-001`.

Evidence paths:

- `B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/04_AAAS_SALES_ROCK.md`
- `B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/05_AAAS_SALES_TRANSVERSE_REVENUE_HANDOFF_OS.md`
- `B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/06_AAAS_B2_B3_SALES_PROPOSAL_PROTOCOL.md`
- `B3_Warp_Core_Execution/02_Sales_MartianManhunter_Illuminati/JTBD-002_AAAS_TRANSVERSE_SALES_REVENUE_GATE.md`
