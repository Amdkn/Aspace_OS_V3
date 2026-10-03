# HANDOVER — Clara Temporal Truth → Graham / Ryan / Rory

Date: 2026-10-03  
Parent Issue: #448

## Consume, do not reopen

Closed inputs:
- #323 Blind-Spots Wargame
- #436 Physiology Wargame

Open integrations:
- #318 Embodied Holons
- #333 Agent OS AI-Native Capability Fabric
- #405 Anti-Amnesia

## Canonical design

`40_Memory_Wiki_OKF/architecture/GRAHAM_TEMPORAL_TRUTH_CONTEXT_COMPILER_V1.md`

Schema:

`10_Tech_OS/kernel/contracts/TEMPORAL_TRUTH_CONTEXT_V1.schema.json`

Ryan packet:

`10_Tech_OS/kernel/temporal_truth/RYAN_BUILD_PACKET.md`

## Responsibilities

Graham owns temporal semantics and context compilation.

Ryan builds the reusable implementation and deterministic contracts.

Rory independently owns contradiction/coherence decisions; Ryan/Graham must not silently auto-resolve them.

Yaz supplies observations.

Nardole routes consequences and return_to.

Agent OS later exposes the stable capabilities but does not own their semantics.

## Immediate next action

Graham: review the schema against the temporal-source corpus and issue only semantic corrections.

Ryan: after Graham semantic acceptance, implement G0/G1/G2 first. Use Jules only as a bounded coding instrument.

Rory: prepare the smallest explicit ReconciliationDecision contract required by G3.

## Canary order

1. Temporal historical replay.
2. Canon resurrection attack.
3. Temporal split-brain.
4. Rory reconciliation.
5. ContextCapsule.
6. #318 Ryan runtime migration.
7. Agent OS exposure.
8. #405 intent continuity.

## Forbidden

No Physiology v2.
No Blind-Spots v2.
No central runner.
No latest-write-wins.
No deletion of superseded truth.
No giant role prompt.
No UNKNOWN coercion.
No new DB unless a demonstrated storage capability gap requires it.
