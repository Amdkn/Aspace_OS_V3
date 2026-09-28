# A'Space Life OS — Structural Simulation Seed v1

## Purpose
Stress-test coordination structure before any real Wargame. Treat social posts/replies as typed handoffs and coordination messages, not public social media.

## Hard invariants
1. Linear In Progress iff claim.valid AND binding.active AND worker.fresh.
2. Linear Done or merged PR never resolves an IPBD automatically.
3. Beth can ALLOW, DENY, ALLOW_WITH_CONSTRAINTS, ESCALATE; no agent bypasses a Beth veto.
4. Morty routes by capability, not by persona or preferred model.
5. System-1 deterministic rule wins before any System-2/LLM escalation.
6. Stewardship is default accountability, never exclusive ownership.
7. Every consequential mutation must emit evidence/provenance.
8. Herdr is runtime/interface, not source of truth. Supabase IPBD/WorkGraph is shared machine state; Linear is human projection; GitHub is version/history; GWS is operational workspace.

## Actors
- Beth A1 — ADMIT/VETO; constitution and safety.
- Morty A1 — ROUTE/COMPILE; capability routing.
- Doctor11 — Life System-2 manager; human intent/time/energy/framework conflicts.
- Amy — PRESENT; human attention and ambiguity compression through Herdr.
- Rory — COHERE; cross-surface identity/state/structure/intent/evidence/time/authority.
- River — FLOW; webhooks, GWS workflows, receipts, idempotence.
- 12WY Curie A2 — converts strategy into cycles, weeks, calendar commitments.
- Pike A3 — 12WY vision/horizon responsibility.
- Una A3 — 12WY planning/outcome responsibility.
- La'an A3 — 12WY process-control/tactics responsibility.
- Doctor13 — Kernel System-2 manager.
- Ryan — BUILD; reversible bounded fabrication.
- Graham — REMEMBER; IPBD/WorkGraph/evidence/provenance.
- Doctor12 — Business System-2 manager.
- Clara — DESIGN; compiles mission topology/factory blueprints.
- Nardole — DISPATCH; leases, bindings, backpressure, recovery routing.

## Normal recursive loop
Signal -> Beth -> Morty -> smallest capable cell -> System-1 rule -> reversible action OR typed escalation -> worker -> evidence -> Rory reconciliation -> Amy human projection.
River transports events and GWS effects. Graham persists machine state. Nardole routes throughout, not only at ship.

## Success condition
The system minimizes A0 intervention, false active work, deadlocks, duplicate work, stale projections, unnecessary System-2 calls, and context rehydration while preserving authority boundaries and evidence.
