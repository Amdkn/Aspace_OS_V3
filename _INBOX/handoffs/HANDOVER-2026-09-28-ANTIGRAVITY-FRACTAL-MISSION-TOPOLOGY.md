# HANDOVER — 2026-09-28 — Antigravity Fractal Mission Topology

## Inputs reconciled
- User requirement: Factory Missions must run loops in the loop; no fixed Bill -> Clara -> Ryan -> Review -> Nardole pipeline.
- Rory handover: `HANDOVER-2026-09-28-RORY-FRACTAL-COHERENCE-TO-CLARA.md`.
- Rory architecture: `40_Memory_Wiki_OKF/architecture/design_fractal_compagnons_doctors_system1_system2.md`.
- Clara Design-of-Design: `HANDOVER-2026-09-28-CLARA-DESIGN-OF-DESIGN-FRACTAL-FACTORY.md`.
- Existing Antigravity recursive Council proof: commits `e0a342b3`, `912b68d1`, `10960e81`; PR #187.

## Runtime correction
Council roles are no longer a mandatory pipeline. A mission is compiled as cells with:
- SDLC phase;
- orchestration pattern;
- capability pole;
- serial / parallel / reentrant mode;
- bounded outcome and evidence.

Supported patterns in v1:
`ORCHESTRATOR_WORKER`, `PIPELINE`, `SWARM`, `MESH`, `HIERARCHICAL`, `DETERMINISTIC_REFLEX`.

Compiler:
`scripts/council_mission.py`.

Machine-readable contracts:
`10_Tech_OS/council/FACTORY_CONTRACTS.schema.json` with `FactoryBlueprint`, `CapabilityNeed`, `EscalationPacket`.

Canary:
`10_Tech_OS/council/examples/factory_mission_canary.json`.

## Capability model
- Bill = DISCOVER / external sensing and R&D capture.
- Clara = DESIGN / Factory Designer / Design-of-Design.
- Ryan = BUILD / fabrication.
- Yaz = SENSE/OBSERVE / proprioception.
- Graham = REMEMBER / state, recall and provenance.
- Nardole = DISPATCH throughout the mission.
- Amy = PRESENT / human interface.
- Rory = COHERE / deterministic reconciliation.
- River = FLOW / webhook-first automation.
- Donna = RECOVER / causal DLQ immune service; not a Council seat.

Doctors 11/12/13 are System-2 managers by domain, not exclusive owners of their three historical Companions. Rick is only the constitutional/cross-Core gatekeeper after local resolution fails.

## System-1 first
Default activation:
`event -> deterministic rule -> reversible action OR EscalationPacket -> Doctor/System-2 -> worker -> evidence -> Rory reconcile`.

Webhook first; cron second; agent last. Zero anomaly means zero LLM.

## Next execution
Use the mission canary shape for the first Bill R&D ingestion mission from YouTube/papers/repos, then let Clara compile the resulting FactoryBlueprint and Ryan build only bounded reversible cells. Nardole routes continuously; Monitor/Learn may reopen the smallest affected cell.

No new ontology is created by this handover; these are executable interaction contracts over existing A'Space capabilities.
