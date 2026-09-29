# CLARA INPUT — Terra / Life OS Full-Stack Code→API Convergence

Date: 2026-09-29
Target lane: CLARA / DESIGN-FORGE
Coordination: GitHub #243
Status: PRE-DESIGN INPUT — implementation intentionally not started.

## Inputs accepted

### Amy / INTERFACE
Commit:
`b4e56e7e73b1d68680b5758aafa8e156045299d1`

Artifacts:
- `10_Tech_OS/reports/amy_terra_frontend_api_maturity_20260929.md`
- `_INBOX/handoffs/HANDOVER-2026-09-29-AMY-TERRA-FRONTEND-TO-CLARA.md`

### Rory / PERSISTENCE
Commit:
`5f9ff47e3c14770413a9147012d84e17eb7736de`

Artifacts:
- `10_Tech_OS/reports/rory_terra_supabase_backend_maturity_20260929.md`
- `_INBOX/handoffs/HANDOVER-2026-09-29-RORY-TERRA-SUPABASE-TO-CLARA.md`

## Maturity diagnosis

Audit rubric:
- M1 Prototype
- M2 Functional Product
- M3 Integrated Platform
- M4 Converged Runtime
- M5 Operationally Certified

**Terra is M3 — Integrated Platform, pre-convergence.**

This is not a low-maturity system.

Terra already contains:
- a large real React/Vite Life OS;
- six framework applications;
- eight Life Domains;
- IndexedDB local persistence;
- outbox/retry/conflict logic;
- Supabase Auth/RLS persistence;
- API bridge code;
- Blackboard SQLite/event/lock/artifact system;
- CLI;
- MCP;
- auth middleware;
- contract/event schemas;
- Business/Linear integration intentions;
- validation/test infrastructure;
- a successful production Vite build.

Its problem is **horizontal convergence**, not missing vertical features.

## What blocks M4

Five contracts currently disagree:

1. **Code ↔ Type contracts**
   - B3 matrix/swarm consumers do not match current descriptor/task types.
   - strict TypeScript fails.

2. **IndexedDB ↔ Supabase data contract**
   - local code requires `version` + `_deleted`;
   - cloud schema has neither.

3. **Client ↔ API contract**
   - duplicate Business bridge servers;
   - duplicate Business bridge clients;
   - CLI and Linear clients reference routes that do not exist.

4. **API ↔ Runtime contract**
   - UI :4444 is live;
   - :3001 API not running at audit;
   - :4445 Blackboard not running at audit;
   - gate requires Blackboard receipts that cannot currently exist.

5. **Repo identity ↔ Startup contract**
   - Terra federation canon points to `ASpace_Worlds/Life_OS_2026`;
   - current running process is canonical;
   - launcher still hard-codes legacy `C:/Users/amado/Life-OS-2026`.

Clara's design must remove these disagreements without flattening all persistence layers into one database.

# 1. Current executable topology

```text
                       ┌─────────────────────────┐
                       │ React / Vite :4444      │
                       │ Zustand + Frameworks    │
                       └────────────┬────────────┘
                                    │
               ┌────────────────────┼─────────────────────┐
               │                    │                     │
               ▼                    ▼                     ▼
      IndexedDB DomainDB     HTTP clients :3001     Blackboard client
      + local outbox         /api/bridge            :4445/api/blackboard
               │                    │                     │
               │             ┌──────┴──────┐              │
               ▼             ▼             ▼              ▼
       Supabase direct    api/server   server/api     Blackboard SQLite
       supabase-js        simple       harness        events/locks/artifacts
       RLS data                        auth+tenant
               │
               ▼
       Life OS Supabase
       public domain/FW tables

Other consumers:
CLI ── stale :3001/api/bridge/events
MCP ── tool registry/adapters
Linear client ── missing :3001/api/bridge/linear/sync
Migration service ── missing Supabase RPC run_adr003_migration
```

This graph is the starting point; do not invent a greenfield architecture.

# 2. Assets to preserve

## A. React domain applications
Do not rebuild the Life OS UI/frameworks.

## B. IndexedDB local-first UX
Local reads must stay non-blocking and offline-capable.

## C. Supabase Auth/RLS
User-domain cloud durability and isolation are useful existing infrastructure.

## D. Cross-category event contracts
Tests already prove:
- dispatch;
- rejection;
- idempotency;
- blocking;
- scopes.

These should become the common API/event envelope.

## E. Authenticated API harness
`server/api/harness.ts` has materially better properties than the simple bridge:
- scopes;
- tenant;
- Zod;
- audit;
- rate limit;
- correlation/causation envelope.

Do not lose these semantics.

## F. Blackboard concepts
Workspaces, events, locks, artifacts and action receipts are valuable execution-plane concepts.

## G. MCP
MCP provides an existing machine/agent-facing surface and should reuse domain services, not duplicate business logic.

# 3. Surfaces that must converge or retire

## Duplicate Business bridge servers

### `api/server.ts` / `api/bridge/business-bridge.ts`
Simple, unauthenticated, alternate response contract.

### `server/api/harness.ts`
Authenticated, tested, typed/event-oriented.

Clara must select ownership and provide a retirement/migration map.
There must not be two production implementations of the same route.

## Duplicate Business bridge clients

- `src/lib/api/client.ts`
- `src/lib/bridge/business-bridge.ts`

Same purpose, slightly different typing/host spelling.

Replace with one generated/versioned or hand-typed canonical client.

## Broken endpoint consumers

### CLI
Current default:
`:3001/api/bridge/events`
No matching route.

### Linear
Current target:
`:3001/api/bridge/linear/sync`
No matching route.

### Migration
Current target:
Supabase RPC `run_adr003_migration`
No such RPC live.

Each must become a real adapter behind the same service contract or be removed from active claims.

# 4. Required target separation of concerns

Clara chooses implementation details, but the architecture must preserve these semantic layers.

## Layer A — UI State
Examples:
- windows;
- selected app;
- temporary forms;
- local visual state.

Authority:
browser/Zustand/local UI persistence.

Not API orchestration truth.

## Layer B — Domain Local State
Examples:
- PARA;
- Ikigai;
- Life Wheel;
- 12WY;
- GTD;
- DEAL;
- LD01-LD08.

Authority:
local-first DomainDB/IndexedDB for immediate UX.

Cloud replication is asynchronous.

## Layer C — Domain Cloud Durability
Authority:
Supabase user-scoped tables + RLS.

It must implement the same concurrency/deletion contract as Layer B.

## Layer D — Execution Ledger
Examples:
- actions;
- receipts;
- locks;
- artifacts;
- integration attempts.

Candidate authority:
Blackboard.

This is distinct from personal domain data.

## Layer E — Integration Adapters
Examples:
- Business OS;
- Linear;
- Google Workspace;
- future external systems.

These should never be embedded as direct ad hoc fetches throughout React stores.

## Layer F — Machine/Agent Access
CLI and MCP.

They must call the same application/domain service contracts as the HTTP layer.

# 5. Canonical API Runtime requirement

Terra needs **one canonical externally visible local HTTP API runtime**.

This does not require one process internally, but from the consumer contract it must provide:
- one base URL/config source;
- one version namespace;
- one health/readiness model;
- one auth/tenant model;
- one error envelope;
- one correlation/idempotency scheme;
- one endpoint registry.

Example semantic shape, not a mandated path:

```text
/api/v1/
  health
  runtime
  domains/*
  frameworks/*
  blackboard/*
  integrations/business/*
  integrations/linear/*
  migrations/*
  evidence/*
```

Clara may choose another naming scheme.

Invariant:
**React, CLI and MCP must not each maintain independent endpoint truth.**

# 6. Domain service layer

Before HTTP/MCP/CLI adapters, define reusable application services.

Conceptual examples:
- `LifeDomainService`
- `FrameworkService`
- `SyncService`
- `BlackboardService`
- `BusinessBridgeService`
- `LinearSyncService`
- `MigrationService`

Adapters become thin:

```text
React client ─┐
HTTP handler ─┼──> Domain/Application Service ──> persistence/adapters
CLI adapter ──┤
MCP tool ─────┘
```

This is the central meaning of **Code→API unification**:
existing code becomes one reusable application contract, not several copied endpoint handlers.

# 7. Local-first synchronization contract

This is a P0 design artifact.

Current code intends:
- local version counter;
- tombstones;
- outbox;
- retry/backoff;
- server-version conflict detection.

Clara must formalize:

## Record envelope
At minimum:
- `id`;
- `user_id`;
- `version` or alternative concurrency token;
- deletion/tombstone representation;
- `created_at`;
- `updated_at`;
- optional source/device id.

## Mutation envelope
At minimum:
- idempotency key;
- entity/table;
- operation;
- expected/current version;
- payload;
- occurred_at;
- actor/device.

## Result
At minimum:
- applied;
- duplicate;
- conflict;
- rejected;
- retryable failure;
- permanent failure.

No silent overwrite.

# 8. Migration architecture

Terra needs two explicit migration tracks.

## IndexedDB migrations
Must guarantee old DBs gain:
- required stores;
- indexes;
- outbox;
- schema markers.

The failed offline-recovery test is the current gate.

## Supabase migrations
Must define:
- any `version`/tombstone contract;
- backfill;
- constraints/indexes;
- RLS updates;
- rollback.

No browser code may call a migration RPC that has not been versioned/deployed.

Migration receipts should include:
- migration id;
- source/target version;
- applied_at;
- affected rows;
- validation;
- rollback/evidence reference.

# 9. Blackboard convergence question

Clara must decide one of these semantics explicitly:

### Option semantic A
Blackboard = execution/event ledger only.

### Option semantic B
Blackboard = local server-side orchestration state + receipts.

### Option semantic C
Blackboard = event ledger plus integration outbox.

But it must not accidentally duplicate DomainDB's personal-data outbox without a boundary.

Recommended invariant:
- DomainDB outbox = replication of user domain records;
- Blackboard = execution/integration events and receipts.

This is an architectural hypothesis for Clara to validate, not a pre-made decision.

# 10. Supabase boundary

Browser-direct Supabase may remain for:
- user-scoped domain reads/writes;
- auth/session.

Server-only boundary should own:
- migrations;
- privileged integration credentials;
- cross-user/admin tasks;
- external API secrets;
- operational reconciliation.

No service-role key in browser.

# 11. Realtime strategy

Current Terra uses no Supabase Realtime publication.

Do not add Realtime universally.

Clara should classify signals:

### Local UI state
No cloud realtime required.

### User-domain sync
Outbox + pull/reconciliation may be sufficient.

### Execution events / action receipts
Could use event streaming/Broadcast if UI benefit is real.

### Agent/runtime presence
Use ephemeral presence only if Terra actually needs live membership.

Recovery rule:
every realtime optimization must have an authoritative read/reconcile path after reconnect.

# 12. B3 code-contract convergence

The current TS failures are highly concentrated and should become one bounded design/build cell.

Need one canonical schema for:
- `B3WorkerDescriptor`;
- `MatrixWorker`;
- `B3TaskProfile`.

Resolve field naming:
- `id`;
- `incarnation` vs `incarnationType`;
- `authorizations` vs `ioAuthorizations`;
- intelligence/determinism requirements;
- token/latency estimates.

Do not patch consumers individually until the canonical contract is selected.

# 13. Runtime identity and launcher

Canonical Terra runtime must start from federation identity.

Current stale hard-coded path:
`C:/Users/amado/Life-OS-2026`.

Canonical:
`C:/Users/amado/ASpace_Worlds/Life_OS_2026`.

Design should use:
- workspace registry;
- Terra alias;
- or a root resolver.

Startup receipt should record:
- resolved root;
- repo remote;
- branch;
- HEAD;
- dirty state;
- ports;
- services started.

# 14. Quality gate convergence

Current states:
- production Vite build: PASS;
- auth test: PASS;
- MCP auth: PASS;
- API harness: PASS;
- cross-category contracts: PASS;
- TypeScript strict: FAIL;
- offline recovery: FAIL;
- A3 execution receipt: FAIL;
- `npm run gate` on Windows: FAIL before checks because Unix `TZ=` syntax.

M4 gate must be:
- cross-platform or shell-independent;
- deterministic;
- able to start required disposable services;
- able to prove persistence migrations;
- able to create/read an action receipt;
- able to clean up all processes.

# 15. Security convergence

Clara must preserve RLS and include a hardening lane, but not mix P1 hardening with P0 convergence.

P1 evidence:
- public table without RLS: `wrappers_fdw_stats`;
- public SECURITY DEFINER execution warnings;
- mutable search_path warnings;
- wrappers extension in public;
- RLS performance warnings;
- unused index advisories.

Architecture should ensure migrations/advisors are part of release evidence.

# 16. Proposed migration waves for Ryan after Clara approves

Clara may modify ordering, but each wave must be independently reversible.

## Wave T1 — Contract stabilization
- B3 canonical types;
- API registry/types;
- endpoint inventory test.

## Wave T2 — Runtime/API consolidation
- select canonical :3001 runtime;
- remove/redirect duplicate bridge;
- health/readiness;
- typed client.

## Wave T3 — Local/cloud sync schema
- IndexedDB migration;
- Supabase migration;
- version/tombstone contract;
- real integration test.

## Wave T4 — Blackboard activation
- lifecycle;
- DB bootstrap;
- receipt proof;
- route through canonical API.

## Wave T5 — CLI/MCP/adapters
- remove stale hard-coded endpoints;
- shared service layer;
- Linear/Business adapters.

## Wave T6 — Release gate
- cross-platform gate;
- integration/recovery;
- source/runtime receipt;
- advisor checks.

No wave should require a wholesale UI rewrite.

# 17. Clara deliverables required before Ryan BUILD

1. component/service diagram;
2. canonical API runtime decision;
3. endpoint retirement map;
4. domain/application service contracts;
5. persistence ownership matrix;
6. local-first sync schema;
7. IndexedDB + Supabase migration plan;
8. Blackboard role/lifecycle;
9. auth/tenant/secret boundary;
10. CLI/MCP adapter model;
11. source/runtime startup contract;
12. B3 canonical types;
13. degraded/offline/reconnect semantics;
14. test/evidence matrix;
15. reversible implementation waves.

## Definition of M4

Terra reaches **M4 / Converged Runtime** only when a clean machine/session can:

1. resolve canonical Terra;
2. start the correct UI/API/Blackboard services;
3. pass typecheck;
4. pass local migration;
5. pass real cloud schema compatibility;
6. mutate domain data offline;
7. replay it once online without duplicate/silent overwrite;
8. execute a bounded action through HTTP, CLI and/or MCP using the same service contract;
9. persist an action receipt;
10. reconstruct correct state after restart;
11. pass the same release gate on the supported host environment.

Until then Terra remains M3, regardless of feature count.
