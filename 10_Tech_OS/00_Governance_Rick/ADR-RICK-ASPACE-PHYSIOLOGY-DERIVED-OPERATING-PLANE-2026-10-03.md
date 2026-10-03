# ADR — A'Space Physiology as a Derived Living-State Operating Plane

Date: 2026-10-03  
Status: PROPOSED FOR CANON / WARGAME PASS  
Wargame: #436  
Parents: #317 Anthology · #318 Embodied Holons · #323 Blind Spots · #405 Anti-Amnesia

## Decision

A'Space recognizes **Physiology** as a derived operating plane answering:

> What is the organism's living condition now?

Physiology is **not** a fifth independent SSOT and does not create a new database, hierarchy, institutional actor or scheduler.

The existing semantic/historical planes remain:

- **Cosmology** — why / horizons / values / institutional universe.
- **Ontology** — what / valid entity and relation semantics.
- **Topology** — where/how authority, surfaces, embodiments and return paths connect.
- **Anthology** — what happened through time with provenance.

Physiology is a **cross-sectional projection at time t** derived from existing authoritative observations.

## Why this is needed

The four planes explain meaning, structure, connection and history, but they do not by themselves provide a compact operational answer to questions such as:

- Is an institutional holon active, idle, degraded or merely represented by an online runtime?
- Are resources abundant while attention/context/review capacity is saturated?
- Are effect leases or recovery pressure accumulating?
- Are current GitHub/Linear/GWS/WorkGraph projections fresh or stale?
- Is the organism healthy despite green technical surfaces, or blocked because a real outcome is UNKNOWN?

The requirement is therefore irreducible as an **operational lens**, but reducible to existing evidence/state sources for storage.

## Non-duplication rule

A'Space already has graph-native concepts for dynamic context: entities, sessions, leases, agents and current state. Physiology MUST consume these rather than recreate them under a new schema.

Default storage rule:

> Existing tables, events, receipts, JSON payloads, runtime observations and projections first. Schema evolution only after a demonstrated query/performance/retention need.

No `aspace.physiology_*` migration is authorized by #436.

## Canonical model

```text
COSMOLOGY   why / horizons
ONTOLOGY    what / valid semantics
TOPOLOGY    where / connections / authority
ANTHOLOGY   what happened / temporal provenance
     │
     └──── authoritative state + observations ────┐
                                                  ▼
                                         PHYSIOLOGY
                                 living-state projection at t
                                                  │
                                                  ▼
                                         Context Compiler
```

Anthology is longitudinal. Physiology is cross-sectional.

A Physiology snapshot must be replayable back to Anthology/evidence sources.

## Required dimensions

A Physiology projection may include:

- institutional state;
- embodiment state;
- runtime state;
- workload/commitment state;
- effect leases/fencing;
- resource/inference/machine capacity;
- attention/context pressure;
- continuity/recovery pressure;
- freshness by source;
- contradictions;
- UNKNOWNs;
- evidence/provenance refs.

It MUST keep these axes distinct. For example:

`runtime ONLINE != holon ACTIVE`

`PR OPEN != work DONE`

`CI GREEN != external outcome proven`

`resource abundance != usable attention capacity`

## Forbidden semantics

Physiology MUST NOT contain authoritative fields equivalent to:

- `next_action`;
- `next_gate_to_execute`;
- `global_priority_decision`;
- institutional ownership reassignment.

It observes and compiles living state. It does not think for the holon.

WorkGraph remains a ledger of commitments/effects/leases, not the brain of the organism.

## Responsibility boundaries

- **Yaz / OBSERVE** — senses behavior, drift, cost, telemetry and runtime/resource signals.
- **Graham / STATE** — temporal normalization, provenance, replay, snapshot/context compilation.
- **Rory / COHERE** — semantic reconciliation when valid projections disagree.
- **Nardole / DISPATCH** — routes accepted CapabilityNeeds/returns after an authorized decision; Physiology itself never routes work.
- **Agent OS / CubeFarm** — render and expose the projection; presentation never becomes authority.
- **Donna / RECOVER** — handles irreducible UNKNOWN/DLQ after ordinary reconciliation is exhausted.
- **Institutional holon** — wakes, reconstructs its world, reprioritizes and decides.

## Temporal truth contract

Every source observation used by Physiology carries:

```yaml
observed_at:
valid_until:
scope:
source_ref:
evidence_refs:
supersedes:
superseded_by:
freshness:
```

Project ChatGPT sources are historical observations, not automatic current canon.

Allowed temporal classes:

`CURRENT | HISTORICAL | SUPERSEDED | CONTRADICTED | EXPERIMENTAL | PROPOSED | UNKNOWN`

## First canary

Use the existing Jules multi-profile / open-PR wave.

The canary must prove that one snapshot can separately represent:

- institutional identity;
- embodiment/runtime bodies;
- workload state;
- resource pressure;
- current GitHub PR state;
- stale historical Project Source statements;
- contradictions/UNKNOWN;
- replayable evidence refs;

without emitting a next action.

## Promotion status

#436 Wargame: **PASS WITH CONSTRAINT**.

This ADR may become canonical after Forge/constitutional review. Runtime/schema expansion is explicitly out of scope for this promotion.
