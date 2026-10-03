# Graham Temporal Truth + Context Compiler v1

Date: 2026-10-03  
Parent mission: #448  
Design owner: Clara / DESIGN-FORGE  
Semantic owner: Graham / STATE-PROVENANCE-TEMPORAL TRUTH  
Build owner: Ryan / industrialisation  
Reconciliation: Rory  
Observation: Yaz  
Routing: Nardole

## Decision

A'Space will not treat Project Sources, GitHub state, WorkGraph rows, runtime observations, Linear, GWS or Agent OS as a universal truth source.

Graham maintains temporal meaning.

The canonical transformation is:

```
source/event
  -> temporal normalization
  -> Temporal Canon Graph
  -> Anthology + Physiology(t)
  -> Context Compiler
  -> ContextCapsule
  -> holon wake
  -> holon decides
```

Physiology is a derived living-state view. It never becomes a scheduler, authority source or competing SSOT.

## Semantic planes

- Cosmology: why.
- Ontology: what exists and which relations are valid.
- Topology: where/how things are connected and embodied.
- Anthology: what happened over time.
- Physiology: how the organism appears to live now, derived from evidence.
- Canon Graph: which interpretation is accepted for a scope and interval.
- Context Compiler: which minimum verified world slice a holon needs now.

Canon Graph and Context Compiler are transformation infrastructure between the planes, not additional cosmologies.

## Core contracts

### TemporalClaim

Represents one sourced assertion valid only within an explicit scope/time/evidence envelope.

Required semantics:

- immutable claim identity;
- source reference;
- correlation identity where available;
- observed time;
- scope;
- assertion payload;
- evidence references;
- epistemic/temporal state;
- optional validity interval;
- supersedes/superseded_by relations;
- contradicts relations;
- never silently deleted when superseded.

Allowed temporal states:

`CURRENT | HISTORICAL | SUPERSEDED | CONTRADICTED | EXPERIMENTAL | PROPOSED | UNKNOWN`

### CanonTransition

Represents a justified change in accepted interpretation.

A CanonTransition never rewrites the old TemporalClaim. It links the old and new interpretation and records:

- subject/scope;
- before;
- after;
- effective_at;
- resolution authority;
- evidence;
- reason;
- contradiction refs;
- resulting canon head.

### ContextCapsule

A ContextCapsule is a bounded, source-linked mission context for one institutional holon.

It must include only what is required to understand the current mission and authority:

- compiled_at;
- holon institutional identity;
- mission/work/correlation IDs;
- accepted canon slice;
- relevant anthology window;
- Physiology snapshot/reference;
- authority envelope;
- WorkGraph neighborhood;
- source/repo slice;
- evidence head;
- contradictions;
- unknowns;
- peers/dependencies where required;
- return_to.

A ContextCapsule is NOT:
- a full repo dump;
- a replay of all chat history;
- a giant role prompt;
- an identity generator;
- an instruction telling the holon what conclusion to reach.

### PhysiologySnapshot

A Physiology snapshot is derived at time t from source observations.

Every dimension carries:
- value;
- source_ref;
- source_observed_at;
- freshness/TTL when relevant;
- epistemic state;
- unknown reason;
- evidence refs.

If the evidence cannot establish a global state, the state remains UNKNOWN.

## Truth rules

1. Latest timestamp alone never establishes authority.
2. Source freshness never overrides source jurisdiction.
3. Superseded truth remains historically addressable.
4. Contradiction is preserved until an authorized reconciliation occurs.
5. UNKNOWN is a real result.
6. GitHub activity cannot prove runtime liveness by itself.
7. WorkGraph 0 claim/0 binding cannot prove runtime OFFLINE by itself.
8. A merged PR proves source mutation, not downstream effect.
9. An issue closed state is not equivalent to accepted outcome.
10. Physiology derives; it does not mutate truth sources.

## state_at and state_now

`state_at(subject, t, scope)` resolves the best supported interpretation whose evidence and validity cover t.

`state_now(subject, scope)` resolves against the latest admissible evidence per authority/freshness rules.

Both return:
- resolved value if support is sufficient;
- provenance/evidence;
- temporal state;
- contradictions;
- confidence/support metadata if defined by the implementation;
- UNKNOWN when support is insufficient.

They must not erase lower-level known facts merely because the aggregate state is UNKNOWN.

Example:

```
GitHub recent mutations         = KNOWN
WorkGraph claims = 0            = KNOWN
WorkGraph bindings = 0          = KNOWN
Jules global runtime state      = UNKNOWN
```

## Reconciliation with Rory

Graham detects temporal contradiction; Rory owns coherence arbitration.

Typed path:

```
TemporalClaims
   -> ContradictionPacket
   -> Rory ReconciliationDecision
   -> CanonTransition
   -> new canon head
```

Graham persists the transition and preserves all prior claims.

Rory may choose:
- ACCEPT_CLAIM_A
- ACCEPT_CLAIM_B
- MERGE_SCOPES
- SPLIT_SCOPE
- REQUIRE_MORE_EVIDENCE
- PRESERVE_UNKNOWN
- REOPEN_CAPABILITY
- ESCALATE_AUTHORITY

## Context compilation

The compiler gathers only the mission neighborhood:

```
Institutional identity
+ constitutional invariants
+ current objective/IPBD
+ CanonGraph slice
+ recent relevant Anthology episodes
+ Physiology reference
+ WorkGraph neighborhood
+ repo/source slice
+ evidence head
+ authority
+ contradictions/unknowns
+ return_to
= ContextCapsule
```

Compilation is deterministic where possible and evidence-linked everywhere.

The compiler may truncate by relevance/time/budget, but it must never silently drop:
- authority constraints;
- unresolved contradictions;
- UNKNOWN state;
- return_to;
- current evidence head.

## Holon Wake

Wake is not scheduling.

A wake only makes an institutional holon aware that its world may have changed.

After wake, the holon receives/reconstructs a ContextCapsule and may decide:
- act;
- investigate;
- wait;
- ask a peer;
- request a capability;
- abandon/reframe a mission;
- escalate;
- do nothing.

WorkGraph cannot prescribe the semantic next step.

## Agent OS projection

Agent OS may expose:
- `canon.resolve`
- `canon.state_at`
- `context.compile`
- `anthology.replay`
- `physiology.snapshot`
- `contradiction.list`

through MCP/API/CLI/harness adapters.

Agent OS does not own their semantics. Graham does.

## Anti-amnesia

#405 should feed this layer through a typed IntentEpisode/AnthologyRef:

```
conversation intention
 -> captured event
 -> classified by ontology
 -> TemporalClaim/AnthologyEpisode
 -> projected to GitHub | Linear | GWS | WorkGraph as appropriate
 -> same correlation_id
 -> same return_to
```

GitHub is never the universal destination.

## Gates

G0 Schema validation  
G1 Temporal Truth Canary  
G2 Temporal Split-Brain  
G3 Graham/Rory reconciliation  
G4 Context Compiler  
G5 #318 runtime migration / same holon  
G6 #333 Agent OS exposure  
G7 #405 Anti-Amnesia integration

Gate = evidence inside one continuous mission.

## Release acceptance

The capability is releasable only if all are demonstrated:

1. old true statements remain queryable historically;
2. superseded claims cannot resurrect silently;
3. `state_at(T)` reproduces known historical states;
4. split-brain keeps uncertainty local and explicit;
5. Rory resolution creates a transition instead of rewriting history;
6. ContextCapsule is bounded and source-linked;
7. Ryan can migrate runtime with same institutional identity/mission/authority/evidence/return_to;
8. no central runner selects the holon's semantic next step;
9. Agent OS exposes contracts without taking ownership;
10. #405 captured intent survives disappearance of the originating chat.
