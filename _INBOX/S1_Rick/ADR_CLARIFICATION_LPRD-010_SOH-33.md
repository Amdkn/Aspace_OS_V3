# ADR CLARIFICATION: LPRD-010 / SOH-33

**Context:** The SOH-33 mandate instructs to "Prepare the Life Core observability implementation under Amy Interface. Start from the existing SOH-29/PR156 feature branch. CURRENT BLOCKERS: SOH-30 and SOH-31. Do not implement past blockers until plan approval. Scope is Life interface/observability projection only; no Kernel orchestration and no Business changes."

**Observation:** SOH-30 and SOH-31 are explicitly stated as current blockers.

**Request:** To adhere to the instruction to "Do not implement past blockers until plan approval", I am submitting this ADR for approval of the conceptual plan for SOH-33 before proceeding with implementation.

**Proposed Design (Observability Projection under Amy Interface):**
1. **Source of Truth:** Utilize the `20_Life_OS/source_map.json` reconciled in SOH-29. This source map acts as the definitive index for the state of 12WY, PARA, and Wheel frameworks.
2. **Amy Interface Integration:** Design a React/Next.js component structure (conceptual only, implementation paused) intended for the `agent-os/desktop/src/apps/amy-interface` application (running on port 5555).
3. **Data Fetching:** The component will consume the `source_map.json` and its referenced JSON files (e.g., `pulse.json`, `state.json`) to project a unified Life OS observability dashboard.
4. **Scope Constraint:** The design strictly focuses on read-only projection (observability) for the Amy interface. It will not alter Kernel orchestration (L0) or Business OS (L2) structures.

Please review this conceptual plan. Once SOH-30 and SOH-31 blockers are resolved and this plan is approved, I will proceed with the implementation phase.
