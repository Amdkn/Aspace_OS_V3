# HANDOVER — Nardole Inter-Fabric Contract #471

Date: 2026-10-03
Owner: Nardole / DISPATCH-INTERCONNECTION
Issue: Amdkn/Aspace_OS_V3 #471
Parent gap: #323 CG2 Translation Contract Registry
Related: #458 #448 #333 #317 #318 #405

## Why this exists

A'Space now has several legitimate fabrics. The risk is no longer absence of
components but divergence of identifiers, authority, evidence, lifecycle and
return routing between fabrics.

The correction is NOT a new fabric or scheduler.
It is one minimal cross-fabric envelope.

## Artifacts

- `10_Tech_OS/kernel/contracts/INTER_FABRIC_ENVELOPE_V1.schema.json`
- `10_Tech_OS/kernel/interconnection/INTER_FABRIC_CONTRACT_V1.md`
- `10_Tech_OS/kernel/interconnection/TRANSLATION_CONTRACT_REGISTRY_V1.json`
- `10_Tech_OS/kernel/interconnection/INTER_FABRIC_ENVELOPE_V1.example.json`

## Invariant

A mission crossing Holon/Capability/Resource/Effect/Truth/Coordination must
retain the same correlation lineage, bounded authority, evidence lineage,
epistemic UNKNOWN and exact return_to.

The envelope carries coordinates; payload schemas keep domain meaning.

## What #471 does NOT replace

- #458 owns Temporal Handoff packet semantics.
- #448 owns Temporal Truth / CanonGraph / Context Compiler.
- #333 owns AI-Native Capability Fabric.
- #317 owns Anthology cross-surface topology.
- WorkGraph remains ledger/continuity substrate, not brain.
- Holons remain decision-makers.

## First canary

Use a bounded read-only capability such as `harness.list`.

Required path:
Capability → Resource/Harness → Truth/Observation → Coordination → Presentation.

Inject one legitimate UNKNOWN (runtime freshness unavailable).
PASS requires that capability identity stays known while runtime freshness
remains UNKNOWN and no UI/router invents LIVE.

## Review / ownership

Graham:
- verify observed_at/freshness/epistemic semantics align with #448/#455.

Rory:
- verify coexistence of legitimate cross-surface states and authority conflict rules.

Clara:
- only reopen DESIGN if the envelope conflicts with existing A-SPEC/capability contracts.

Ryan:
- implement adapters/tests only after semantic acceptance; do not create a new runtime.

Yaz:
- define independent observation for correlation loss, authority widening and stale replay.

Nardole:
- maintain registry, return_to, compatibility and smallest-cell reopen.

## Negative gates

FAIL if:
- authority widens in transit;
- correlation identity is silently replaced;
- UNKNOWN is coerced;
- stale duplicate creates a second mutation;
- raw secret enters the envelope;
- version mismatch is silently accepted;
- return_to disappears;
- a presentation surface becomes authority.

## Current state

Contract draft: WRITTEN
Schema: WRITTEN
Registry seed: WRITTEN
Example: WRITTEN
Semantic review: OPEN
Live cross-fabric canary: OPEN
Issue closure: NOT AUTHORIZED

Next action is validation + review, not another architecture layer.
