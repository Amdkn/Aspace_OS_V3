# SUPERVISION SDLC BOARD (Round 1 Finalized)

## Doctor13 Kernel Core [COMPLETE]
- **Immediate Action:** Independently review Ryan PR #160.
- **Owner:** Yaz.
- **PR/Session Evidence:** PR #160.
- **Blocker:** SOH-20 blocked by SOH-19; SOH-42 blocked by SOH-21.
- **New Jules Capacity Allowed:** Only if unlocking these critical SOH-19/SOH-21 Kernel blockers.

## Doctor11 Life Core [COMPLETE]
- **Immediate Action:** Merge PR #161 into `feature/soh-29-source-map-reconciliation-17166659983655281860`, then merge into PR #156. After SOH-29 closes, launch River (SOH-30).
- **Owner:** Doctor11 (Merge), River (Next Action), Amy (Following Action).
- **PR/Session Evidence:** PR #161 PASS, PR #156. Amy readiness/ADR IN_PROGRESS.
- **Blocker:** River SOH-30 blocks Amy SOH-33 implementation.
- **New Jules Capacity Allowed:** Yes (>80% weight applies).

## Doctor12 Buzz Core [IN_PROGRESS]
- **Immediate Action:** Review PASS PR #162 (Bill), then PR #159 (Clara). Provide feedback to Nardole (SOB-1) to reconcile those outputs.
- **Owner:** Doctor12 (Review), Nardole (Reconciliation).
- **PR/Session Evidence:** PR #162, PR #159. Doctor12 IN_PROGRESS, Nardole reconciliation IN_PROGRESS.
- **Blocker:** None currently.
- **New Jules Capacity Allowed:** Yes (>80% weight applies).

## Capacity Policy Enforcement (Manager Directive)
- Any NEW Jules capacity after the 9 base Companion lanes is strictly allocated to >80% Life + Business (0.90 combined ratio).
- Only critical Kernel blockers (e.g., SOH-19, SOH-21) can bypass this limit.
- **NOTE:** This is a management rule to be implemented by Doctor13 -> Ryan on their existing Linear sub-issues. PR #164 must be marked DO_NOT_MERGE and superseded by proper Companion execution.
