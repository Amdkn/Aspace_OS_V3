# Harness Runtime Fabric — Clara Design Contract v0.1

Date: 2026-09-28
Parent mission: GitHub #194
Design cell: #196
Build cell: #197
FLOW consumer: #200

## Problem

Ryan can build machine capabilities, but BUILD remains coupled to later workflow execution when capability use is passed manually through ChatGPT sessions or handovers.

The missing structure is a runtime-native continuation contract:
Ryan publishes a certified capability once, then exits the critical path.
River composes that capability into workflows.
Rory reconciles execution truth.
Nardole routes the next action and return path.

ChatGPT group conversations and handover markdown are development/debug surfaces only.
They are never required for production continuation.
## Core cycle

The runtime cycle is:

CapabilityReleaseReceipt
-> Nardole DispatchEnvelope
-> River HarnessExecutionRequest
-> AMF policy + lease + runtime identity
-> inspect / prepare / launch / observe / wait / collect
-> HarnessExecutionReceipt
-> Rory ReconcileDecision
-> Nardole ContinuationEnvelope
-> DONE | NEXT_FLOW | RETRY | DONNA | RYAN | CLARA

No Companion owns the whole cycle.

Ryan owns capability fabrication and certification.
River owns workflow composition.
Rory owns coherence verdict.
Nardole owns routing, leases, retry/backpressure and return-to.
## Ryan liberation rule

Ryan is released when a capability version reaches PUBLISHED with:

- capability_id;
- capability_version;
- contract_ref;
- artifact/build refs;
- acceptance evidence refs;
- policy_version compatibility;
- runtime adapter metadata;
- rollback/removal contract;
- publication receipt.

Ryan does not remain attached to each future execution.

A runtime failure returns to Ryan only when Rory classifies the defect as:
BUILD_DEFECT or ADAPTER_DEFECT.

Workflow choice, retries, waiting and continuation belong to River/Nardole.
Semantic contract gaps return to Clara.
Unknown effect state returns to Donna.
## P1 — Runtime Identity

Every runtime execution has a RuntimeFingerprint.

Minimum fields:
- harness + harness version;
- adapter + adapter version;
- provider/model when applicable;
- workspace/worktree;
- cwd;
- runtime kind/version;
- venv/container/runtime root;
- dependency/lock hash;
- PATH/proxy profile hash;
- credential profile reference, never raw secret;
- session/conversation identity when applicable;
- process group identity;
- timeout/quota profile;
- authority scopes;
- capability_version;
- policy_version.

Same effective environment must yield the same canonical fingerprint.
Meaningful drift must yield a different fingerprint.
## P2 — Prepare / isolation

runtime.prepare and harness.prepare are idempotent scoped operations.

Preparation may create:
- isolated venv;
- isolated runtime root;
- bounded container;
- pinned dependency cache;
- generated config under the owned runtime root.

Preparation may not silently:
- install global Python/Node;
- mutate machine PATH globally;
- change system proxy;
- reuse a contaminated runtime;
- widen credentials/authority.

Every prepare returns a receipt with:
fingerprint_before, fingerprint_after, changed_refs, cleanup/compensation.
## P3 — Process-tree lifecycle

A harness execution is owned as a process group/job, never as one parent PID.

Lifecycle operations:
inspect, launch, resume, observe, wait, cancel, collect, reconcile.

The runtime tracks:
- root process;
- child/background process set;
- process-group/job identity;
- start time;
- heartbeat;
- last observation;
- stdout/stderr refs;
- artifact refs;
- timeout/deadline;
- cancellation state.

Parent exit does not imply task completion.
Parent death does not imply child death.
Cancellation targets the complete owned tree.
## P4 — Harness adapter protocol

Antigravity, Jules, Hermes, Codex and Claude implement the same adapter boundary.

Adapter methods:
- inspect(request)
- prepare(request)
- launch(request)
- observe(execution_id)
- wait(execution_id, condition)
- cancel(execution_id)
- collect(execution_id)
- reconcile(execution_id)

Adapters translate provider-specific mechanics only.
They do not own policy, WorkGraph truth or retry authority.

River selects adapters by required capability, availability, quota, latency and evidence level.
AMF HostPolicy remains the authority gate.
## Runtime-native continuation objects

### CapabilityReleaseReceipt
Published by Ryan after BUILD certification.

### DispatchEnvelope
Issued by Nardole when a published capability can satisfy a READY work cell.
It binds work_id, correlation_id, capability version, lease and return route.

### HarnessExecutionRequest
Issued by River after claiming the dispatch.
It contains typed inputs, desired artifacts, timeout, authority and replay policy.

### HarnessExecutionReceipt
Produced by the runtime regardless of success/failure.
It captures runtime fingerprint, process truth, artifacts/effects and recovery hints.

### ReconcileDecision
Produced by Rory from receipt + WorkGraph truth.
It never directly performs the next action.

### ContinuationEnvelope
Produced/routed by Nardole from Rory's decision.
This is the machine replacement for a human handover.
## ReconcileDecision outcomes

Rory returns exactly one routing class:

- ACCEPT_CONTINUE
  Evidence is coherent; route to next workflow cell.

- COMPLETE
  Acceptance is satisfied; route terminal result to origin/consumer.

- RETRY_SAFE
  Same operation/cell may retry under declared replay policy.

- RECOVER_UNKNOWN
  Effect state is unknown; route to Donna/DLQ.

- REOPEN_BUILD
  Capability implementation/adapter defect; route to Ryan.

- REOPEN_DESIGN
  Contract/authority/semantic gap; route to Clara.

- HOLD
  Dependency, quota, temporal wait or human approval is unresolved.

Rory does not choose the worker. Nardole does.
## Nardole return routing

Every DispatchEnvelope contains a return_route:

origin_intent
mission_id
work_id
cell_id
correlation_id
origin_capability
terminal_consumer
evidence_sink
on_success
on_retry
on_unknown
on_build_defect
on_design_gap

Nardole preserves correlation_id across the full cycle.

When River emits a receipt:
receipt -> Rory -> ReconcileDecision -> Nardole route.

No ChatGPT session needs to be awake for that return path.
No new session is created merely to carry state.
## WorkGraph mapping

Reuse existing WorkGraph identities and append-only event semantics.

Suggested event kinds:
- capability_release
- dispatch_envelope
- harness_execution_requested
- runtime_prepared
- harness_execution_started
- harness_observed
- harness_execution_receipt
- rory_reconcile_decision
- continuation_routed
- continuation_resolved

Existing claim/session_binding/lease mechanisms remain authoritative for live ownership.
Linear status is never machine truth.

The design does not introduce a second scheduler or second work database.
## No-handover invariant

A markdown handover may explain a development change to a human session.
It must not be required for:

- selecting a harness;
- resuming a workflow;
- knowing what Ryan built;
- knowing where a result returns;
- retrying after a transient failure;
- detecting UNKNOWN/DLQ;
- reopening BUILD/DESIGN;
- deciding terminal completion.

Those decisions must be recoverable from typed contracts + WorkGraph events + durable receipts.

A fresh process can reconstruct the next action without reading ChatGPT history.
## First certification canary

Use the existing MiroFish incident.

1. Ryan publishes the bounded Harness Runtime capability.
2. Nardole emits DispatchEnvelope to River.
3. River selects prepared MiroFish runtime.
4. Runtime launches one bounded run with child/background visibility.
5. Force parent/harness interruption.
6. Runtime reconciles process tree + artifacts.
7. Emit HarnessExecutionReceipt.
8. Rory emits ReconcileDecision.
9. Nardole routes the continuation automatically.

The canary must answer:
launched? accepted? child survived?
artifact/effect = YES / NO / UNKNOWN?
resumable? retry-safe? receipt exists?
## Acceptance

The architecture is accepted when:

- Ryan can terminate his BUILD session after CapabilityReleaseReceipt;
- River can start/resume execution without reading Ryan handover/chat;
- Rory can reconcile solely from machine state + receipts;
- Nardole can route the next owner/cell solely from ReconcileDecision;
- forced interruption cannot strand unowned children;
- UNKNOWN never becomes blind retry;
- same correlation_id survives retries and provider changes;
- no false In Progress is created;
- one end-to-end MiroFish canary returns to the correct next cell automatically.

This is the point where Ryan becomes a forger of reusable capabilities rather than a permanent workflow operator.
