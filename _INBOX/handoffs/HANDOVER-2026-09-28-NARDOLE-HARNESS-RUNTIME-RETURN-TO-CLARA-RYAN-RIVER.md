# HANDOVER — 2026-09-28 — NARDOLE / Harness Runtime Audit → CLARA → RYAN → RIVER

## Mission
- parent: GitHub #194 — A'Space Machine Fabric
- design: #196 / PR #201
- build: #197 / PR #202
- River continuity: #200 + MiroFish handovers
- routing owner: Nardole / DISPATCH
- decision: reopen the smallest missing DESIGN cell; do not revoke AMF M0 filesystem proof.

## Audit verdict
Ryan correctly implemented the accepted M0 filesystem slice. The missing prerequisite is not “more M0”; it is a typed Harness Runtime contract between machine mutation sovereignty and River/FLOW orchestration.

The observed MiroFish failure is the concrete counterexample:
- parent process truth did not equal child/background process truth;
- DC termination left child pip processes alive;
- two installs overlapped and contaminated an environment;
- River later recovered by building a clean isolated runtime and explicit preflight.

Therefore River must never orchestrate opaque shell/harness processes directly as the architectural contract.

## Existing proof preserved
- Ryan M0: crash/restart/replay no duplicate effect remains PASS.
- Graham: policy provenance PASS; capability-version provenance still BLOCKS M0 SHIPPED.
- M1 Chrome and M2 private remote remain HOLD.
- No false In Progress may be created from this handover.
## P0 — inherited M0 provenance micro-cell (orthogonal)
Clara chooses the minimal capability-version binding contract.
Ryan patches ledger + receipt + semantic fingerprint only as required.
Graham recertifies.
This P0 does not block Clara from designing P1-P4 in parallel.

## P1 — Runtime Identity & Environment Contract
CLARA defines typed `runtime.inspect` / `harness.inspect` and `environment_fingerprint`.
Minimum fingerprint:
harness + version; provider/model; workspace/worktree; cwd; runtime + version; venv/container; dependency/lock hash; PATH/proxy profile; credential profile reference (never raw secret); session/conversation id; parent/child pid set; timeout/quota; authority scopes; capability_version + policy_version.

RYAN acceptance:
- deterministic JSON fingerprint;
- same environment => same canonical fingerprint;
- meaningful runtime/config drift => new fingerprint;
- no global install is required merely to inspect;
- receipt binds fingerprint + capability/policy versions.

RIVER consumes P1 for HarnessSelector and RuntimePreflight. River may reject/abstain; it may not rewrite environment truth.

## P2 — Runtime Prepare + Isolation Contract
CLARA defines `runtime.prepare` / `harness.prepare` as idempotent, scoped preparation.
No silent global Python/Node/package mutation.

RYAN acceptance:
- isolated venv/container/runtime root;
- pinned dependency evidence / lock provenance;
- repeated prepare is idempotent;
- failed prepare leaves a receipt and bounded cleanup/compensation path;
- runtime drift is observable through P1.
## P3 — Process-Tree Lifecycle Contract
CLARA defines `harness.launch/resume/wait/cancel/observe` over a process group/job, not one parent PID.

RYAN acceptance:
- durable launch operation_id;
- parent + children/background process inventory;
- heartbeat and stale detection;
- cancel targets the complete owned process tree;
- timeout cannot leave an untracked owned child;
- restart reconciliation answers launched/accepted/alive/effect-known/resumable/retry-safe;
- unknown effect => UNKNOWN/DLQ, never blind replay.

This directly closes the defect observed when DC force-terminated the parent while pip children survived.

## P4 — Harness Adapter + Execution Receipt / FLOW Contract
CLARA defines one adapter protocol for Antigravity, Jules, Hermes, Codex and Claude.
Required objects:
`HarnessExecutionRequest`, `HarnessExecutionReceipt`, artifact refs, stdout/stderr refs, provider/runtime fingerprint, policy decision, lifecycle state, reconcile result and recovery hint.

RYAN builds the generic adapter substrate + at least one bounded adapter required for the canary.
RIVER owns composition:
`SimulationRequest -> HarnessSelector -> RuntimePreflight -> launch -> observe -> ArtifactWait -> HarnessExecutionReceipt -> RoryReconcile -> AmyPresent`.

River chooses a harness by capability/availability/quota/latency. HostPolicy/AMF retains authority. River must not bypass AMF through privileged shell flags.

## First certification canary
Use the existing MiroFish incident as vertical slice.
Required forced scenario:
1. River selects the prepared runtime/provider.
2. Ryan substrate launches one bounded MiroFish run.
3. A child/background process is observable.
4. Force parent/harness interruption.
5. Reconcile process tree + artifacts.
6. Produce a durable failure/success HarnessExecutionReceipt.
7. Answer deterministically:
   - launched?
   - task accepted?
   - child survived?
   - effect/artifact produced: YES / NO / UNKNOWN?
   - resumable?
   - retry safe?
   - receipt exists?
8. UNKNOWN routes to Donna/RECOVER; no blind retry.

Success does NOT require Chrome or remote networking.

## Routing / dependencies
- Clara P1-P4 DESIGN may proceed while P0 provenance patch is being closed.
- Ryan BUILD begins only against accepted P1-P4 contract deltas; no redesign from BUILD.
- River FLOW can continue read-only preflight work but may not treat ad-hoc shell orchestration as certified Harness Runtime.
- Yaz observes lifecycle/latency/orphans/health.
- Graham binds provenance/receipts/environment versions.
- Rory reconciles runtime/worker/WorkGraph contradictions.
- Nardole owns return-to, retry/backpressure and smallest-cell reopen.
- Donna owns UNKNOWN/DLQ recovery.
- Doctor13/Doctor11/Rick only if the local mesh cannot resolve authority/semantic conflict.

## Exact next owners
1. Clara / DESIGN: compile P1-P4 into existing Machine Fabric FactoryBlueprint/contracts; do not create a parallel ontology.
2. Ryan / BUILD: implement bounded P1-P4 substrate after Clara acceptance; preserve #202 M0 proof.
3. River / FLOW: consume the substrate and execute the MiroFish harness-runtime certification canary.
4. Nardole: converge receipts and decide next cell; Chrome M1 remains HOLD until this prerequisite is accepted.
