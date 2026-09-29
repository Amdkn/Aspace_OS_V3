# CLARA INPUT — Agent OS Full-Stack Unification Pre-Design Packet

Date: 2026-09-29
Target lane: CLARA / DESIGN-FORGE
Coordination: GitHub #211
Status: PRE-DESIGN INPUT — architecture intentionally not chosen yet.

## Inputs accepted

### Amy / INTERFACE
Commit:
`c2091d7164c7e6e125d6e8504eb5204f21b49b32`

Artifacts:
- `10_Tech_OS/reports/amy_agent_os_frontend_api_audit_20260929.md`
- `_INBOX/handoffs/HANDOVER-2026-09-29-AMY-AGENT-OS-FRONTEND-TO-CLARA.md`

### Rory / PERSISTENCE
Commit:
`8e988da70c692cfdca70d873eae041e0201481ef`

Artifacts:
- `10_Tech_OS/reports/rory_agent_os_supabase_backend_audit_20260929.md`
- `_INBOX/handoffs/HANDOVER-2026-09-29-RORY-AGENT-OS-SUPABASE-TO-CLARA.md`

## Problem statement

Agent OS currently has several legitimate state planes, but no explicit composition contract between them.

### Plane A — Frontend UX state
Examples:
- open windows;
- selected tabs;
- theme;
- user-local session;
- transient drafts.

Current authority:
browser localStorage / local adapters.

This state should not become orchestration truth.

### Plane B — Local runtime truth
Examples:
- listener exists;
- process is alive;
- CPU/RAM observation;
- Hermes local health;
- a Python worker is actually executing.

Current evidence:
local process/port probes, Vite middleware, filesystem and scripts.

This state is ephemeral and must carry observation time / TTL.

### Plane C — Local orchestration state
Examples:
- `uc.db` work/event/lease state;
- kernel scripts;
- local evidence/checkpoints.

Current authority:
Tech OS local kernel.

This state is currently consumed directly by `/api/tech-os/*`.

### Plane D — Cloud orchestration / durable coordination
Examples:
- intents;
- cloud work;
- claims;
- session bindings;
- evidence;
- world snapshots.

Current authority:
Supabase schema `aspace`.

This plane is durable but currently stale for runtime presence.

### Plane E — Source / version truth
Examples:
- Agent-OS parent commit;
- Desktop nested repo/submodule commit;
- branches;
- dirty state;
- PRs.

Current authority:
Git / GitHub.

A parent SHA alone is insufficient when nested HEADs have advanced.

## Current contradictions to design out

### C1 — Amy and Supabase desynchronized
Agent OS Desktop has no Supabase JS client and does not read `aspace`.
It reads local APIs and local state.

### C2 — Runtime presence is unreliable
At audit:
- Agent OS `:5555` is reachable;
- telemetry is live;
- Workspace health is live;
- `/api/tech-os/subagents` returns zero agents;
- Supabase has zero active/waiting session bindings;
- Supabase has zero claims;
- some UI/service statuses remain hard-coded as ONLINE/OPERATIONAL.

No single current badge answers “is this worker actually alive and owning work?”.

### C3 — Local kernel and cloud state are parallel
`/api/tech-os/kernel-state` reads `uc.db`.
Supabase `aspace.work/event/claim/session_binding` is separate.
There is no explicit reconciliation proof in the UI.

### C4 — Agent OS source snapshot is stale
Supabase Agent OS world sync records:
- parent SHA `4b73326...`;
- committed Desktop gitlink `7c6dc8b...`.

Actual Desktop HEAD:
`c0dc5d2...`.

Therefore the cloud world catalog can be “successful” while not representing the active nested frontend source.

### C5 — Vite dev middleware is carrying backend semantics
Agent OS frontend currently depends on `desktop/tools/*.ts` Vite server middleware for kernel, workflow, workspace, routing and observability APIs.

Development transport must not silently become the permanent API architecture.

### C6 — Supabase internal schema is not a browser API
The `aspace` schema has RLS but no client policies and is not published to Realtime.
The existing Edge Function is a bounded intent ingress, not a general state-query API.

## Non-negotiable architecture invariants

### I1 — No fake runtime status
A registry entry, scheduled task, installed capability, UI component or persisted `status='active'` is not sufficient proof of liveness.

### I2 — Presence is derived, not declared
Runtime presence must be computed from fresh evidence with timestamps and expiry.

### I3 — Provenance travels with state
Every UI-visible runtime/work state needs:
- source plane;
- observed_at;
- freshness/TTL;
- evidence reference;
- reason.

### I4 — Work ownership is stronger than presence
A worker can be LIVE without owning work.
Owning work requires a valid claim/lease/binding contract.

### I5 — Local-first does not mean cloud-blind
Local `uc.db` may remain authoritative for machine execution, but divergence from Supabase must be explicit and observable.

### I6 — Cloud-durable does not mean process-live
Supabase session/work rows are historical/durable state unless accompanied by fresh runtime evidence.

### I7 — Frontend never receives service-role credentials
Browser integration must use a bounded public/authenticated projection or a server-side gateway.

### I8 — Source synchronization includes nested repos
World snapshot fingerprint must include parent SHA + committed gitlinks + observed nested HEADs + dirty state.

### I9 — Failure/degradation is a first-class state
Supabase unavailable, local runtime unavailable, provider unavailable and sync stale must have distinct representations.

## Required architecture contracts

Clara's design should output explicit contracts for the following.

### 1. RuntimePresenceProjection

A versioned read model for UI/runtime consumers.

Minimum semantic fields:
- identity;
- entity kind;
- declared capability;
- runtime state;
- runtime reason;
- provider;
- work id;
- session binding id;
- claim state;
- process observation;
- source snapshot;
- observed_at;
- expires_at / TTL;
- repo / branch / head / PR;
- evidence refs.

Minimum state vocabulary:
`UNKNOWN | OFFLINE | STARTING | LIVE | WAITING | STALE | FAILED`.

Clara may refine names, but must retain the semantic distinction.

### 2. API Projection Layer

Define the boundary that Agent OS Desktop consumes.

It must answer:
- which read models are public to the UI;
- which mutations are allowed;
- where auth is enforced;
- how API versions evolve;
- how local-only data is bridged;
- how cloud-only data is projected;
- which endpoints are synchronous vs event-driven.

Implementation mechanism remains open:
- local gateway;
- Edge Functions;
- RPC;
- server adapter;
- combination.

### 3. Runtime Evidence Ingestion

Define how fresh local observations enter the unified state model.

Examples of evidence:
- process PID/listener;
- heartbeat;
- provider canary;
- harness session;
- work lease;
- latest event;
- filesystem/gitrepo fingerprint.

Important:
Supabase Presence may be useful for ephemeral online state, but it must not replace durable work/claim/evidence semantics.

### 4. Reconciliation Protocol

Define:
- local -> cloud sync;
- cloud -> UI projection;
- conflict detection;
- stale detection;
- ownership of updates;
- idempotency key;
- retry/backpressure;
- recovery after offline periods.

No silent last-write-wins between `uc.db` and `aspace`.

### 5. Source Sync Receipt

Minimum:
- world id;
- parent repo / branch / SHA;
- nested repo path;
- committed gitlink;
- observed nested HEAD;
- dirty flag;
- asset/entity counts;
- start/end;
- result;
- evidence URI.

### 6. Intent / Work / Session write separation

The architecture must distinguish:
- intent capture;
- work creation;
- work claiming;
- session binding;
- runtime heartbeat;
- evidence return;
- closure/reconciliation.

The current `aspace-intent-capture` Edge Function may remain one ingress, but must not become an overloaded generic control API.

## Realtime design questions Clara must answer

Do not choose by fashion. For each signal, choose a semantic transport:

- **Broadcast**: transient state/update envelopes;
- **Presence**: ephemeral membership/online state;
- **Postgres Changes**: database change subscription where appropriate;
- **poll/read projection**: recovery and authoritative refresh.

Required property:
a client can reconnect after missing realtime messages and reconstruct correct state from an authoritative projection.

## Runtime presence acceptance matrix

| Situation | UI status expectation |
|---|---|
| Process alive + provider healthy + fresh binding + valid claim | LIVE / owning |
| Process alive + no work | LIVE / idle |
| Fresh waiting binding + no claim | WAITING |
| Persisted active binding older than TTL | STALE |
| Registry exists but no runtime evidence | UNKNOWN/OFFLINE, never LIVE |
| Local process healthy but Supabase stale | LIVE locally + SYNC DEGRADED |
| Supabase fresh but local process absent | OFFLINE/FAILED locally, not LIVE |
| Provider auth failure | FAILED(provider) |
| Source snapshot parent clean but nested HEAD differs | SOURCE STALE |

## Current concrete baseline that architecture must improve

- UI port 5555 is reachable.
- local telemetry works.
- Workspace Hermes health works.
- local kernel state endpoint works.
- subagent roster endpoint currently returns zero agents.
- roster and scheduled-task manifest expected by API are absent.
- Supabase has no active/waiting bindings and no claims.
- Agent OS world snapshot is stale versus Desktop HEAD.
- `aspace` is not currently a direct realtime/browser schema.

## Explicitly open design choices

Clara retains authority to decide:
- whether presence projection lives in Postgres, local gateway or both;
- whether Realtime Broadcast and/or Presence is used;
- whether Vite middleware is replaced, wrapped or reduced to development;
- whether local `uc.db` remains execution authority;
- how bidirectional reconciliation is orchestrated;
- whether a dedicated runtime-heartbeat table/event stream is justified;
- how auth identities map to A'Space agents/services.

## Definition of design completion

Clara's design is ready for Ryan only when it includes:

1. component diagram;
2. read/write API contracts;
3. runtime presence state machine;
4. reconciliation sequence;
5. source sync sequence;
6. auth/RLS boundary;
7. realtime semantics;
8. offline/degraded behavior;
9. migration path from current Vite/local API;
10. test/evidence plan proving Amy UI and Rory backend cannot silently disagree.

No implementation should begin merely from “connect Supabase to React”.
