---
id: B2_DOMAIN_GATE_MATRIX
layer: L2_Business_Pulse
status: SHADOW_ACTIVE
date: 2026-05-25
---

# B2 Domain Gate Matrix

Product is allowed to prototype. Product is not allowed to graduate alone.

A Summer's Verse project becomes operational only when each B2 domain has either:

- `PASS` with evidence path;
- `CONDITIONAL` with named risk and owner;
- `BLOCKED` with the next unblock action.

## Gate Order

| Order | Domain | Question | Minimum Proof |
|---|---|---|---|
| 1 | Product | Does the thing demonstrate real user value? | prototype path, user workflow, scope note |
| 2 | Ops | Can the thing be delivered repeatedly? | SOP, QA checklist, owner, incident note |
| 3 | IT | Can the thing run outside the maker's head? | env names only, build/deploy command, backup/access notes |
| 4 | Finance | Does the thing make economic sense? | pricing hypothesis, cost estimate, margin risk |
| 5 | Legal | Can it be shown/sold without unmanaged exposure? | claims/privacy/IP/terms note |
| 6 | Sales | Can a human sell and hand it off? | qualification, objection handling, next-step flow |
| 7 | Growth | Can the market understand why it matters? | ICP, message, channel, measurement loop |
| 8 | People | Can the team carry it without burnout? | role map, handoff, training/load note |

## Graduation Rule

`Product Done` means the artifact works.

`Business Done` means the artifact passed B2 gates and produced B3 execution logs.

If Ops, IT, Finance, Legal, Sales, Growth, or People is empty, the project is still in `PRODUCT_ONLY_PROTOTYPE`, even if the interface is beautiful and the build passes.

## Per-Project Gate Record

```yaml
project: ""
cycle: "C1"
product_status: "PASS|CONDITIONAL|BLOCKED"
ops_status: "PASS|CONDITIONAL|BLOCKED"
it_status: "PASS|CONDITIONAL|BLOCKED"
finance_status: "PASS|CONDITIONAL|BLOCKED"
legal_status: "PASS|CONDITIONAL|BLOCKED"
sales_status: "PASS|CONDITIONAL|BLOCKED"
growth_status: "PASS|CONDITIONAL|BLOCKED"
people_status: "PASS|CONDITIONAL|BLOCKED"
evidence:
  product: ""
  ops: ""
  it: ""
  finance: ""
  legal: ""
  sales: ""
  growth: ""
  people: ""
next_unblock_action: ""
```