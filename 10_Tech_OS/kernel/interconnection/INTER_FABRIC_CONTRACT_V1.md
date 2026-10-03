# A'Space V4 Inter-Fabric Contract v1

Issue: #471
Steward: Nardole / DISPATCH-INTERCONNECTION
Status: PROPOSED CONTRACT

## Purpose

A'Space now has multiple legitimate fabrics: Holon, Truth, Capability, Resource,
Effect, Coordination, Evolution and Presentation.

This contract does not create another fabric. It defines the smallest shared
coordinates that let one mission cross existing fabrics without losing identity,
authority, evidence, epistemic state or return routing.

## Core invariant

A fabric may transform its own payload semantics, but it MUST preserve the
cross-fabric coordinates carried by `InterFabricEnvelope.v1`.

No envelope may:
- decide the holon's next action;
- become a universal semantic authority;
- widen authority during transport;
- turn runtime presence into institutional identity;
- turn PR/test/API success into effect truth;
- coerce UNKNOWN into SUCCESS or FAIL;
- carry raw secrets.

## Separation of responsibilities

- Holon Fabric owns institutional identity and embodiment semantics.
- Truth Fabric owns temporal/provenance claims and context reconstruction.
- Capability Fabric owns capability contracts and reusable exposure.
- Resource Fabric owns compute/cognition/action leases and budgets.
- Effect Fabric owns operations, external effects and receipts.
- Coordination Fabric owns topology, dependencies, leases and return routing.
- Evolution Fabric owns research-to-capability reclassification.
- Presentation Fabric renders evidence-backed state without creating truth.

## Envelope coordinates

The shared envelope carries only coordinates needed by more than one fabric:

1. Identity: `holon_id`, institutional rank, optional home/embodiment/session refs.
2. Mission: `mission_id`, `work_id`, `cell_id`, `correlation_id`, parent correlation.
3. Capability: capability id/version and contract reference when relevant.
4. Authority: scoped authority, policy ref/version, mutation lease/fencing if effectful.
5. Resource: resource/budget lease references only; never provider credentials.
6. Effect: operation/effect identity and replay/idempotency semantics.
7. Truth: source authority, observation time, freshness, epistemic state, evidence.
8. Routing: origin layer, blocked outcome, `return_to`, recovery hint.
9. Compatibility: envelope version, payload schema/version and explicit lossy fields.

Fabric-specific meaning remains behind a typed payload reference.

## Preservation law

A producer MAY add fabric-local fields inside its payload.
A translator MAY emit a new payload type.
A translator MUST NOT silently modify:
- correlation identity;
- institutional actor identity;
- authority scope;
- capability version;
- operation/effect identity;
- evidence lineage;
- epistemic UNKNOWN;
- return_to.

Any intentional loss MUST be declared in `compatibility.lossy_fields`.

## Fencing law

Parallel embodiments of the same holon are allowed.
Exactly-once protection applies to conflicting mutation/effect scope, not to actor existence.

For consequential effects:
- an operation/fencing identity is required by the owning effect contract;
- stale/duplicate envelopes must not gain a second mutation lease;
- UNKNOWN effect state must route to reconciliation/recovery rather than blind replay.

## Relationship to existing contracts

#458 remains the typed temporal handoff contract:
ObservationPacket → TemporalClaim → ContradictionPacket → CanonTransition →
ContextCapsule → CapabilityNeed.

#448 remains the Temporal Truth / CanonGraph / Context Compiler mission.

#333 remains the Agent OS AI-Native Capability Fabric.

#317 remains the cross-surface Anthology topology.

#323 CG2 remains the Translation Contract Registry requirement.

This contract supplies their shared transport coordinates; it does not replace
their semantic schemas.

## Translation registry rule

Every producer→consumer boundary registered under CG2 must declare:
- producer payload schema/version;
- consumer payload schema/version;
- required envelope fields;
- preserved fields;
- lossy fields;
- authority change: forbidden by default;
- evidence transformation;
- UNKNOWN handling;
- negative test;
- adapter/steward.

A boundary requiring prose reconstruction is PARTIAL, not PASS.

## First canary

Use one bounded shared capability, preferably `harness.list`, because it is
read-only and already exercises Agent OS/runtime semantics.

Path:
Capability → Resource/Harness → Observation/Truth → Coordination → Presentation.

The same `correlation_id` must survive the entire path.

Inject one uncertainty, for example runtime freshness unavailable, while the
capability declaration itself remains known.

Expected result:
- capability identity remains KNOWN;
- runtime freshness can remain UNKNOWN;
- Amy/Agent OS must not render LIVE from registry presence alone;
- Nardole receives a parseable return route;
- no human prose is required to explain the mismatch.

## Negative tests

1. Authority widening during translation → FAIL CLOSED.
2. Correlation id replaced without parent lineage → FAIL.
3. UNKNOWN coerced into FAIL/SUCCESS → FAIL.
4. Stale envelope replays consequential mutation → FAIL.
5. Raw secret appears in resource fields → FAIL.
6. Payload version mismatch without explicit compatibility decision → FAIL.
7. return_to dropped at any mandatory continuation boundary → FAIL.
8. One optional fabric unavailable → remaining identity chain must stay intact.

## Acceptance

Contract acceptance requires:
- JSON Schema parses;
- representative envelope validates;
- translation registry entry exists;
- temporal semantics reviewed by Graham;
- coherence/authority conflicts reviewed by Rory/Nardole;
- one cross-fabric canary survives serialization and runtime/session replacement.

Only then should #471 close.

## Non-goal reminder

The purpose is not to make every object identical.
The purpose is to make heterogeneous fabrics composable without recreating
A0 or a ChatGPT session as the semantic bus.
