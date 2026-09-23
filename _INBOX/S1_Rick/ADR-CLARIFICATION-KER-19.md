# ADR Clarification for KER-19: Needle 3 capability adapter

## Context
The execution of mandate KER-19 requires integrating the Cactus Needle 3 capability into an `IntelligenceRouter` and exposes EXTRACT, ACT, EMBED methods.
The mandate includes the following instruction: "only expose DECIDE if evidence justifies it."

## Issue
I was unable to locate the PRD file `10_Tech_OS/PRD_Autonomy/K2_SYSTEM1_DECISION/KPRD-020_KER-19.md` mentioned in the mandate to determine if there is design-time justification to expose the DECIDE capability.

## Proposed Action
Following the rule: "If requirements are materially ambiguous or need human interaction, STOP implementation and propose an ADR clarification for the Doctor/Rick review path", I am stopping implementation entirely to propose this clarification.

The `10_Tech_OS/kernel/intelligence/intelligence_router.py` implementation is blocked until the PRD `KPRD-020_KER-19.md` is provided or evidence is otherwise supplied.
