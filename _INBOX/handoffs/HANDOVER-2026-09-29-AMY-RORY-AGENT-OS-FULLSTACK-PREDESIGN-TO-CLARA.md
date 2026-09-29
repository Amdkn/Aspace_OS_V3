# HANDOVER — 2026-09-29 — AMY + RORY → CLARA — AGENT OS FULL-STACK PREDESIGN

## Coordination
GitHub #211
`[AGENT-OS][FULLSTACK][PREDESIGN] Amy + Rory unification audit before Clara architecture`

## Inputs
Amy commit:
`c2091d7164c7e6e125d6e8504eb5204f21b49b32`

Rory commit:
`8e988da70c692cfdca70d873eae041e0201481ef`

Canonical Clara input:
`10_Tech_OS/reports/clara_input_agent_os_fullstack_unification_20260929.md`

## Design mission

Design the Agent OS full-stack integration so that:
- frontend status;
- local runtime/process status;
- local `uc.db` orchestration state;
- Supabase `aspace` state;
- Git/source state

can disagree temporarily but can never disagree **silently**.

## Two P0s

### P0-A — Amy ↔ Supabase desynchronization
Agent OS Desktop is currently local/API-driven, not a Supabase projection.

### P0-B — Runtime presence
Current UI badges, local endpoint health, Supabase bindings and claims do not share one liveness contract.

## Clara must produce

- API Projection Layer;
- RuntimePresenceProjection + state machine + TTL;
- local↔cloud reconciliation protocol;
- source sync fingerprint including nested repos;
- realtime semantics;
- auth/RLS boundary;
- migration plan from Vite-local middleware;
- verification/evidence plan.

## Guardrail

Do not collapse all state into one fake SSOT.
Preserve distinct authorities and make reconciliation explicit.

Do not hand to Ryan until the read/write contracts, presence semantics and migration gates are bounded.
