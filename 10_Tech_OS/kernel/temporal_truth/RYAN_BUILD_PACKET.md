# Ryan Build Packet — Temporal Truth + Context Compiler

Parent: #448  
Architecture: Graham Temporal Truth + Context Compiler v1  
Semantic owner: Graham  
Build owner: Ryan  
Coding worker: Jules when bounded cells are accepted  
Independent coherence: Rory  
Observation: Yaz

## Mission

Industrialize Graham's temporal semantics without inventing another scheduler, SSOT or giant context store.

This is ONE mission. G0-G7 are gates, not future projects.

## First implementation slice

Build the smallest local deterministic library/API that can:

1. validate the four v1 schemas;
2. ingest TemporalClaims append-only with immutable `observed_at` + distinct `recorded_at`, `subject`, `predicate`, `scope` and `source_authority`;
3. query `state_at(subject, predicate, t, scope)`;
4. query `state_now(subject, predicate, scope)`;
5. record supersession/contradiction through relations/transitions without mutating or deleting the original claim;
6. create CanonTransition after an explicit reconciliation decision;
7. compile one bounded ContextCapsule;
8. derive/read a PhysiologySnapshot without mutating source truth.

Do not start with a new database service. Reuse existing durable stores/evidence primitives unless a proven capability gap requires otherwise.

## G1 Temporal Truth Canary fixture

Encode the known Jules historical sequence as fixture claims:

`0 active -> 15 slots -> 12 IN_PROGRESS -> 12 PR open -> 7 PR open`

Assertions:

- every claim remains addressable;
- the correct value is returned at each historical timestamp;
- reinjecting the old `0 active` observation later records a later `recorded_at` but preserves its original `observed_at`, and does not make it CURRENT;
- provenance remains intact.

## G2 Split-Brain fixture

Inputs:
- GitHub recent mutation evidence;
- WorkGraph 0 claim;
- WorkGraph 0 binding;
- no fresh runtime observation establishing ONLINE/OFFLINE.

Expected:
- scope-distinct CURRENT facts may coexist without being forced into a contradiction;
- GitHub mutation state = KNOWN;
- WorkGraph claim count = KNOWN 0;
- WorkGraph binding count = KNOWN 0;
- aggregate Jules runtime = UNKNOWN.

Any implementation returning OFFLINE from these facts fails.

## G3 Reconciliation

Expose a function that consumes Rory's explicit decision and creates CanonTransition.

No automatic LLM reconciliation in the core library.

## G4 Context Compiler

Inputs are explicit references/queries. Output is `aspace.context-capsule.v1`.

Compiler requirements:
- deterministic mandatory sections;
- replayable `source_cutoff_at`;
- bounded optional sections;
- evidence refs;
- unresolved contradiction/UNKNOWN preservation;
- authority + return_to never truncated;
- no free-form "you are Ryan" identity reconstruction.

## G5 #318 canary

When #318 is ready, use the released compiler for the runtime migration canary.

Ryan runtime A dies.
A ContextCapsule is compiled.
Runtime B receives the capsule.
The institutional Ryan must continue with the same mission/correlation/authority/evidence/return_to.

The new runtime is allowed to make a new decision. It must not be forced to execute a stored "next step".

## G6 Agent OS ports

After core semantics pass:
- register/expose `canon.resolve`;
- `canon.state_at`;
- `context.compile`;
- `physiology.snapshot`;
- `anthology.replay`.

Do not copy semantic logic into each adapter.

## G7 Anti-amnesia

Integrate #405 only after the temporal core is stable.

Captured intent becomes an event/claim/anthology episode and is projected according to ontology.

## Required evidence

Every PR must provide:
- tests;
- negative tests;
- replay fixture;
- proof UNKNOWN is preserved;
- proof provenance, freshness and epistemic state remain distinct;
- proof subject-only latest-write-wins is impossible;
- proof superseded history remains queryable;
- proof no new scheduler is introduced;
- rollback notes.

## Stop conditions

Emit CapabilityNeed instead of widening scope if:
- a storage primitive cannot represent append-only temporal relations;
- an authority/reconciliation question is unresolved;
- ContextCapsule requires data not currently addressable by evidence refs;
- #318 needs new institutional semantics rather than implementation.

Otherwise continue through the next gate.
