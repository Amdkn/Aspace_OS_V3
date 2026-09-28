# Discovery Packet 03 — Anthropic AI-Native SDLC

- mission_id: MISSION-20260928T131628Z-factory-loop-canary
- cell_id: C02
- owner: Bill / DISCOVER
- source: "The AI-Native SDLC playbook"
- author: Louis Claxton / Anthropic
- published: 2026-08-21
- primary: https://claude.com/blog/the-ai-native-sdlc-playbook
- repo reference: https://github.com/anthropics/claude-code

## Primary claims
1. Code generation is no longer the only bottleneck; pressure moves to planning, review/test and deploy/governance.
2. Anthropic frames the SDLC as a **loop**, not a one-way linear process, with AI embedded at each stage.
3. Each stage emits a committed artifact the next stage can read: intent → spec → plan → code/tests → PR/review findings → incident/control-band signal.
4. The commit chain is treated as audit trail; humans remain accountable at judgment-heavy gates.
5. Every artifact should have one declared source of truth, or at minimum explicit linkage between authoritative systems.
6. Production control-band breaches can generate the next intent, closing the loop.

## Novelty vs A'Space V3
- **High-value transfer:** artifact acceptance as a trigger; receipts between cells; explicit SSOT-per-artifact; control-band → new intent.
- **Already present in stronger form:** A'Space separates semantic authority, execution truth, evidence and projections rather than making Git the universal SSOT.
- **Generalize:** `CLAUDE.md` is a vendor-specific instance of a harness-readable context contract, not the canonical A'Space format.

## Direct contradiction to preserve
Anthropic's Build section says implementation starts after an accepted plan. A'Space's parallel-session protocol explicitly permits a **bounded, reversible BUILD cell before global Discovery/Design closes** when local dependencies are satisfied. Do not overwrite A'Space with a mandatory global Plan→Build barrier.

The synthesis is:
- global mission = graph/re-entrant;
- each cell = explicit prerequisites + authority + evidence;
- irreversible/high-blast-radius mutations = stronger gate;
- bounded reversible experiments = can start early.

## Candidate patterns
- ArtifactReceipt
- ArtifactAccepted → typed trigger
- SSOTLink
- ControlBandBreach → Intent
- HarnessContextContract
- JudgmentGate

## Confidence
- Anthropic claims: HIGH (primary source)
- transfer to A'Space: HIGH for artifact/trigger/SSOT primitives
- vendor-specific workflow shape: do not promote wholesale
