# River FLOW Consumer Contract — Harness Runtime

River consumes published capabilities; River does not own BUILD artifacts.

## Input

River receives a Nardole DispatchEnvelope, not a ChatGPT handover.

Required:
- work_id / correlation_id;
- capability_id + version;
- lease/fencing token;
- typed inputs;
- required harness capabilities;
- return_route.

River claims the dispatch and creates HarnessExecutionRequest.
## Composition

River composes:

DispatchEnvelope
-> HarnessSelector
-> runtime.inspect
-> runtime.prepare when required
-> harness.launch/resume
-> observe/wait
-> ArtifactWait
-> collect
-> HarnessExecutionReceipt

Selection factors may include:
capability fit, evidence level, availability, quota, latency and cost.

HostPolicy/AMF decides authority.
River may reject/abstain; it may not grant itself permission.
## Continuation

River does not decide WorkGraph truth after execution.

It emits HarnessExecutionReceipt and stops owning the decision.

Rory consumes the receipt and emits ReconcileDecision.
Nardole consumes that decision and routes ContinuationEnvelope.

If Nardole routes NEXT_FLOW back to River, River may continue the next workflow cell under a new lease while preserving correlation_id.

If route is RYAN, CLARA or DONNA, River releases ownership.
## Failure semantics

Parent process death is only an observation.

River must not infer:
- task completion from root exit;
- child death from parent death;
- failure from missing stdout alone;
- safe retry from an exception alone.

UNKNOWN effect state is explicit and routes to Donna.

Transient provider/harness failure may become RETRY_SAFE only after Rory reconciliation and declared replay semantics.

No direct Linear/Supabase governance mutation is authorized by the harness adapter.
