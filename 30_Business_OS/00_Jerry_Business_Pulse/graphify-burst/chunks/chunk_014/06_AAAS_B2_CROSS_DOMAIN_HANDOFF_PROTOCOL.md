---
id: AAAS_B2_CROSS_DOMAIN_HANDOFF_PROTOCOL
layer: B2_DOMAIN_SUPERVISION
project: 00 Agency as a Service
domain: Ops
status: ACTIVE
created: 2026-06-02
---

# AaaS B2 Cross-Domain Handoff Protocol

## Purpose

This protocol defines how work moves across the 8 B2 domains without losing context, ownership, or proof.

Ops owns the handoff standard. Each domain still owns its own gate.

## Handoff Packet

Every cross-domain handoff must include:

```yaml
handoff_id: "AAAS-B2-<FROM>-TO-<TO>-YYYY-NN"
from_domain: ""
to_domain: ""
project_stage: "intake|scope|delivery|launch|renewal"
decision_needed: ""
input_artifacts: []
constraints:
  promise: ""
  budget: ""
  legal: ""
  runtime: ""
  owner_load: ""
definition_of_done: ""
evidence_path: ""
deadline: ""
status: "OPEN|ACCEPTED|BLOCKED|DONE"
```

## Required Domain Handoffs

| From | To | Trigger | Packet Must Include |
|---|---|---|---|
| Growth | Sales | A channel/message produces qualified attention. | ICP, pain, source, message, lead quality signal. |
| Sales | Product | Prospect needs demo/scope. | Promised outcome, objections, buying criteria, deadline. |
| Product | Ops | Demo/scope becomes delivery. | Workflow, included/excluded features, acceptance criteria. |
| Ops | IT | Delivery depends on runtime/access/data. | Runbook need, access need, data risk, incident trigger. |
| Ops | Finance | Delivery effort affects margin. | Estimated labor, tools, rework risk, capacity constraint. |
| Ops | Legal | Delivery touches claims/data/IP/terms. | Public wording, client data, IP use, contract surface. |
| Ops | People | Delivery needs owner/operator/reviewer. | Role map, expected load, training need, escalation path. |
| People | Ops | Ownership/load changes. | Capacity update, training proof, owner readiness. |
| Finance/Legal | Sales | Price or claim boundary changes offer. | Approved price/terms/claims constraints. |

## Review Routine

1. Ops reviews open handoffs every weekly B2 Council.
2. Any `BLOCKED` handoff gets an owner and next unblock action.
3. Any cross-domain blocker older than 7 days escalates to B1.
4. Any public launch requires all required handoffs to be `DONE` or explicitly `CONDITIONAL`.

## Donna/DLQ Route

Route to Donna/DLQ when:

- A promise was made without owner or proof.
- A delivery step cannot be repeated.
- Legal/Finance constraints are unknown but public action is requested.
- A B3 agent reports fabricated or uninspectable proof.

