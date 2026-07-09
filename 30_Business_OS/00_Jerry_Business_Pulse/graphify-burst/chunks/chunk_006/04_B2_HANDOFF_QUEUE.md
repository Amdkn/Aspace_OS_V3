---
id: B1_B2_HANDOFF_QUEUE_CEOS_DESKTOP
layer: L2_Business_Pulse
kind: CEO_Command_Center
status: PHASE_1_SKELETON
created: 2026-06-07
parent_jerry: J01_Jerry_Prime_LD01_Business
project_slug: ceo-desktop
---

# B2 Handoff Queue — CEO's Desktop

B1 (A0) writes here before B2 work begins. B2 does not invent direction; B2 translates direction into domain Rocks, gates, and tactic specs for the 8 SOB.

In Phase 1, all 8 SOB domains are seeded as **PENDING**. They will be moved to ACCEPTED in Cycle C2 (Domain Activation Prep) once a B2 manager is named per domain.

## Queue

| Status | B2 Domain | Direction Item | Why Now | Required Output | Evidence Path |
|--------|-----------|----------------|---------|-----------------|---------------|
| PENDING | Growth   | Name the ICP variant + first experiment velocity target for the desktop | The desktop must surface Growth pulse first — it's the leading indicator | Growth pulse column spec + 1 experiment brief | `B2_Business_Domains/01_Growth_Superman_Guardians/` (Phase 2) |
| PENDING | Sales    | Define qualification + handoff to Product | Without qualification, Growth pulse is noise | Sales handoff script + qualification matrix | `B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/` (Phase 2) |
| PENDING | Product  | Bound the desktop's own scope as a Product | The desktop is not a product, but it has a Product column — that column needs DoD | Product Done definition (build vs. buy vs. junction-only) | `B2_Business_Domains/03_Product_Flash_Avengers/` (Phase 2) |
| PENDING | Ops      | Define delivery/SOP gate for the desktop's weekly review ritual | The weekly review must run without A0 hero-moding | Ops gate checklist for 12WY weekly review | `B2_Business_Domains/04_Ops_Batman_Fantastic4/` (Phase 2) |
| PENDING | IT       | Confirm runtime/access/deploy assumptions for the desktop surface | The desktop must open in < 2s; runtime must be sovereign | Environment + deploy note + MCP/CLI health check | `B2_Business_Domains/05_IT_Cyborg_KangDynasty/` (Phase 2) |
| PENDING | Finance  | Estimate cost-to-run for the desktop (compute, storage, MCP spend) | Avoid hidden recurring burn on the command center | Margin note + monthly burn ledger | `B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/` (Phase 2) |
| PENDING | People   | Name owner/load for each of the 8 B3 squad leads | Prevent founder-mode overload on A0 | Role/load note per squad | `B2_Business_Domains/07_People_GreenLantern_XMen/` (Phase 2) |
| PENDING | Legal    | Review IP/terms/data boundary for the desktop as a sovereign surface | The desktop holds business data — boundary must be explicit | Legal risk note + IP/license boundary | `B2_Business_Domains/08_Legal_Aquaman_Eternals/` (Phase 2) |

## Handoff Rule

A row leaves **PENDING** only when the B2 domain has accepted it and produced either PASS, CONDITIONAL, or BLOCKED with an evidence path.

In Phase 1, no row has moved yet. Phase 2 (Cycle C2) will promote the first 1–2 rows to ACCEPTED with a DoD draft.

## Phase 1 Close-Out

When Phase 1 closes (end of Cycle C1), this queue must show:

- 8 SOB rows, all with at least a PENDING status and a direction item;
- at least 1 row with a B2 manager name (even if PENDING);
- at least 1 row with a Beth/Morty safety status;
- a decision-charter entry ratifying the queue.
