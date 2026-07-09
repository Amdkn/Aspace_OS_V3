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
project: "00 Agency as a Service"
cycle: "C1"
product_status: "CONDITIONAL"
ops_status: "CONDITIONAL"
it_status: "CONDITIONAL"
finance_status: "CONDITIONAL"
legal_status: "CONDITIONAL"
sales_status: "PASS"
growth_status: "CONDITIONAL"
people_status: "CONDITIONAL"
evidence:
  product: "B2_Business_Domains/03_Product_Flash_Avengers/04_AAAS_PRODUCT_ROCK.md"
  ops: "B2_Business_Domains/04_Ops_Batman_Fantastic4/04_AAAS_OPS_ROCK.md"
  it: "B2_Business_Domains/05_IT_Cyborg_KangDynasty/04_AAAS_IT_ROCK.md"
  finance: "B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/04_AAAS_FINANCE_ROCK.md"
  legal: "B2_Business_Domains/08_Legal_Aquaman_Eternals/04_AAAS_LEGAL_ROCK.md"
  sales: "B3_Warp_Core_Execution/02_Sales_MartianManhunter_Illuminati/JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md"
  growth: "B3_Warp_Core_Execution/01_Growth_Superman_Guardians/JTBD-001_*.md"
  people: "B2_Business_Domains/07_People_GreenLantern_XMen/04_AAAS_PEOPLE_ROCK.md"
gate_notes:
  sales: "PASS_INTERNAL: diagnostic-to-proposal packet produced; external proposal send remains gated by Product, Ops, Finance, and Legal proof."
next_unblock_action: "Execute 00 Agency as a Service / Product / JTBD-001_AAAS_MVP_DEMO_BOUNDARY.md, then Ops, Finance, Legal, IT, People, Growth in the chosen order."
```
