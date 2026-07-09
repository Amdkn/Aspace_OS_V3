# AAAS Finance Transverse Money Control OS  ## Purpose Finance is the transverse money gate for 00 Agency as a Service. It ensures pricing, margin, costs, cash timing, payment terms, refunds, taxes, approvals, and leakage controls are explicit before B2/B3 work becomes operational.  ## Operating Thesis AaaS needs Finance to keep pricing, margin, labor load, client payment timing, tooling cost, and delivery profitability visible before agency work scales.  ## Eight-Domain Finance Interface | Domain | Finance Surface | Required Proof | | --- | --- | --- |
| Growth | CAC, channel spend, promotion economics | Spend cap, CAC proxy, learning metric |
| Sales | Price, quote, payment terms, discounts | Approved quote and payment boundary |
| Product | Unit economics, package margin, cost-to-serve | Price/margin model and exclusions |
| Ops | Labor, supplies, delivery cost, exceptions | Cost owner and leakage path |
| IT | Tooling, subscriptions, automation cost | System cost and approval owner |
| Finance | Budget, cash, accounts, tax/refund risk | Finance decision log and controls |
| People | Compensation, staffing load, capacity cost | Labor/capacity cost and approval path |
| Legal | Taxes, refunds, liabilities, entity obligations | Legal/Finance boundary and review route |

## Finance Control Loop
1. Identify the price, cost, payment, budget, tax, refund, or leakage surface.
2. Name the B2 owner, B3 agent, and approval owner.
3. Build or update the price/margin/cost model.
4. Confirm cash timing, payment terms, and exception/refund path.
5. Confirm Ops delivery cost, People capacity cost, IT tooling cost, and Legal/tax boundary.
6. Record decision, proof, and escalation route.
7. Emit Finance readiness before launch, spend, billing, or commitment.

## Readiness States
- FINANCE_READY: work can proceed inside the named money boundary.
- NEEDS_MODEL: return to Finance/B2 because pricing, cost, or cash proof is missing.
- BLOCKED_LEAKAGE: route to Donna/DLQ or B1 because unpriced labor, margin risk, or payment/tax risk is unsafe.

## Project Constraint
No offer, client workflow, or delivery package may launch without price, margin, cost, payment, refund, and leakage boundary.

## Finance Metrics
- Gross margin or contribution margin.
- CAC/spend cap where relevant.
- Cash timing and receivables risk.
- Unpriced labor count.
- Tooling/subscription cost.
- Refund/exception exposure.
- Leakage or margin drift.