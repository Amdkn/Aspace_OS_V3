---
id: B1_B2_DEFINITION_OF_DONE_SPEC_05_MARINA
layer: L2_Business_Pulse
kind: SummerProject
status: SHADOW_ACTIVE
date: 2026-05-26
---

# B2 Definition Of Done Spec - 05_Marina

B1 defines the format of done. B2 owns the domain-specific Definition of Done.

## B2 DoD Packet

`yaml
dod_id: ""
date: "2026-05-26"
scope: "05_Marina"
b2_domain: "Growth|Sales|Product|Ops|IT|Finance|People|Legal"
rock_or_gate: ""
owner_b2: ""
status: "DRAFT|READY_FOR_B3|CONDITIONAL|BLOCKED|DONE"
definition_of_done: ""
acceptance_criteria:
  - ""
required_artifacts:
  - path: ""
    reason: ""
lead_measures:
  - ""
lag_measures:
  - ""
risks:
  - ""
dependencies:
  - domain: ""
    need: ""
b3_jobs_to_create:
  - ""
review_cadence: "weekly|per-cycle|on-change"
`

## Domain DoD Minimums

| B2 Domain | Done Means |
|---|---|
| Growth | ICP, message, channel, campaign hypothesis, and measurement loop are explicit. |
| Sales | Qualification, offer terms, objections, close path, and handoff are explicit. |
| Product | User value, scope, workflow, release candidate, and Product Done proof are explicit. |
| Ops | SOP, QA checklist, owner, support path, and incident/rollback note are explicit. |
| IT | Runtime, build/deploy, environment variable names only, access, backup, and dependency state are explicit. |
| Finance | Cost, price, margin, payment path, and burn risk are explicit. |
| People | Owner, role map, training, workload, and handoff are explicit. |
| Legal | Claims, privacy, IP, terms, consent, and external exposure are explicit. |

## B1 Acceptance Gate

B1 accepts a B2 DoD only when:

- it contains artifact paths or explicit TBD blockers;
- it names the B3 jobs required;
- it states what will be measured;
- it identifies cross-domain dependencies;
- it does not convert Product Done into Business Done by itself.

## Anti-Patterns

- "Done when the page looks good."
- "Done when A0 approves verbally."
- "Done when the build passes" without Ops, IT, Finance, Legal, Sales, Growth, and People gates.
- "B3 will figure it out."