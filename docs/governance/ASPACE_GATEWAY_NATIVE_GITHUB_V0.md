# A'Space Gateway v0 — Native GitHub Control Plane

Status: implementation contract  
Mission: #542  
Executable gates: #543 #544 #545 #546  
Bootstrap: #547

## 1. Purpose

A'Space Gateway is the federated membrane for **connectivity, presence, sessions, transport and surface federation**.

It is not an agent, scheduler, source of truth, capability registry, or policy authority.

### Architectural boundaries

| Layer | Owns |
|---|---|
| AI-Native Capability Fabric | typed abilities and their adapters |
| A'Space Gateway | connection, session, presence, delivery, federation |
| Nardole | dispatch, topology, backpressure, return_to |
| HostPolicy | authority, fencing, reversibility, permissions |
| Graham | temporal truth, provenance, context compilation |
| River | flow/composition |
| AMF | machine effects and durable receipts |
| Donna | UNKNOWN / recovery / DLQ |
| Amy / Agent OS | human-facing projection |

The Gateway transports existing A'Space coordinates; it must not invent parallel identity, authority, evidence, or work semantics.

## 2. Reused contracts

Do not fork these concerns:

- #333 — AI-Native Capability Fabric
- #471 — InterFabricEnvelope.v1
- #448 — Temporal Truth / Context Compiler
- #318 — Embodied Holon identity/runtime separation
- #484 — Reflex Fabric
- #485 — RecoveryPort / Donna

## 3. Core protocol

Every Gateway message MUST preserve or explicitly reject:

- institutional_holon_id
- embodiment_id
- runtime_id
- device/node identity
- surface_id
- session_id + lineage
- mission_id / work_id / cell_id / correlation_id
- capability_id + version
- authority / policy / fencing
- resource / budget lease
- operation / effect identity
- evidence + temporal provenance
- return_to

Protocol roles are orthogonal to institutional identity:

`operator | holon | runtime | node | surface | worker`

## 4. Presence model

Presence is multi-axis, never a single ONLINE badge:

- institutional_state
- embodiment_state
- runtime_state
- workload_state
- freshness / TTL
- provenance

A healthy runtime does not imply an active holon.
An inactive runtime does not erase the holon.

## 5. Session fabric

The session layer MUST support:

- durable lineage;
- reconnect / resume;
- runtime migration;
- multi-surface attach/detach;
- duplicate delivery detection;
- explicit delivery ambiguity;
- fencing of stale writers.

Runtime/provider replacement MUST NOT widen authority or mutate identity.

## 6. GitHub-native control plane

GitHub is a **control plane**, not the runtime.

### Primitive topology

| GitHub primitive | A'Space use |
|---|---|
| Discussions | exploration, RFC, research, alternatives |
| Wiki / canonical docs | durable doctrine and playbooks |
| Projects | portfolio, possibility-space, sequencing |
| Milestones | bounded convergence / release boundary |
| Issues | executable or concretely blocked cells |
| Pull Requests | exact mutation + review + proof |
| Actions / Checks | deterministic verification / evidence |
| Releases | immutable promotion / rollback reference |
| Agents | GitHub-hosted embodiments, never institutional identity |
| Webhooks / GitHub App | ingress/egress to external A'Space runtimes |

### Ingress

Relevant events may include:

- issue / issue_comment;
- pull_request / review;
- workflow_run / check_run;
- discussion promotion;
- release.

They are normalized into an existing A'Space envelope before dispatch.

### Egress

Results return to the primitive that matches their semantics:

- exploration → Discussion;
- executable work → Issue;
- mutation → PR;
- deterministic verdict → Check/Action;
- portfolio state → Project;
- release boundary → Milestone;
- promoted version → Release.

## 7. Provider neutrality

A GitHub Issue MUST express the needed capability/holon and acceptance contract, not a hard-coded provider.

Possible embodiments include:

- GitHub-hosted Copilot / Codex / Claude;
- Hermes;
- Codex local;
- Claude Code local;
- Antigravity;
- Jules;
- Browser Harness;
- local inference;
- future runtimes.

Provider selection happens after capability, authority, health, cost/quota and policy checks.

## 8. ChatGPT branch vs Git branch

A **ChatGPT branch** is conversational exploration/context.

A **Git branch** is a short-lived repository mutation.

Do not use Git branches as long-term memory.

Git branch lifecycle:

`mission branch → PR → CI/review → merge → delete`

Durable reasoning belongs in:

`Discussion | Wiki/docs | Project | Issue | PR evidence | Release`

Persistent holon homes `Amdkn/<Holon>` remain institutional anchors, not feature backlogs.

## 9. Native GitHub bootstrap

The repository workflow `.github/workflows/native-github-control-plane.yml` is idempotent and owns only repository-native projection work:

1. create/find the dedicated Gateway v0 milestone;
2. attach #542–#547;
3. create/find the Gateway RFC Discussion;
4. add Gateway issues to the Foundation Project V2 when token permissions allow;
5. mirror `docs/wiki/*.md` into the GitHub Wiki;
6. post an evidence receipt on #547.

If a native API permission is unavailable, the workflow MUST report the gap instead of faking success.

## 10. Sovereign canary

PASS requires one mission to cross multiple surfaces and at least two runtimes:

`GitHub/CLI → Agent OS → runtime A → runtime migration → runtime B → AMF reversible effect → durable receipt → reconnect`

Invariant through the whole run:

- same institutional holon;
- same work/correlation identity;
- same authority/fencing;
- same evidence lineage;
- same effect identity;
- same return_to.

No duplicate effect and no silent coercion of UNKNOWN are allowed.

## 11. Audit-to-Automaton continuity (2026-10-05)

See [session synthesis and decisions](SESSION_2026_10_05_AUDIT_TO_AUTOMATON.md) for the dated portfolio audit, Work/Chat/harness roles, Solarpunk source coverage and [proposed Automaton M0/M1/M2 integration](../architecture/AUTOMATON_GATEWAY_M0_M1_M2_PROPOSAL.md).

This is a documentation and design proposal attached to #545/#546. It does not certify an installed adapter, dispatch a provider, or replace the #560–#562 execution gates.
