# AMY — Terra / Life OS Frontend + API Maturity Audit

Date: 2026-09-29
Lane: AMY / INTERFACE
World: Terra = `C:/Users/amado/ASpace_Worlds/Life_OS_2026` -> `Amdkn/Life-OS-2026`
Purpose: diagnose Terra maturity and its Code→API convergence before Clara architecture design.

## Maturity rubric used for this audit

This is an audit rubric, not an A'Space canonical ontology:

- **M1 — Prototype**: UI or isolated functions, little durable state.
- **M2 — Functional Product**: real domain features and persistence, limited integration.
- **M3 — Integrated Platform**: multiple domains/services/contracts work, but interfaces are not yet converged.
- **M4 — Converged Runtime**: one coherent API/state contract, portable gates, end-to-end recovery and observability.
- **M5 — Operationally Certified**: replayable production evidence, failure recovery, deployment/runtime identity and migrations continuously verified.

**Amy assessment: Terra is M3 / Integrated Platform, pre-convergence.**
It is materially beyond prototype/product stage, but not yet M4 because the code, local APIs, local Blackboard, cloud persistence and runtime identity do not share one executable contract.

## 1. Canonical source and runtime identity

Federation canon:
- Terra physical repo: `C:/Users/amado/ASpace_Worlds/Life_OS_2026`
- GitHub: `Amdkn/Life-OS-2026`
- Terra junction: `C:/Users/amado/ASpace_Worlds/Terra`
- Astra projection: `ASpace_OS_V3/Worlds/Terra`.

Observed canonical Terra:
- branch: `docs/aspace-world-federation-2026-09-28`
- HEAD: `831b6856713efc2080de5cb837441324addada35`
- code base: `origin/main@3718ee652838eee498195b5dded83701fdb56aec`.

### Source identity defect

A second physical directory exists:
`C:/Users/amado/Life-OS-2026`

It contains the same older code HEAD but its configured remote points to `Amdkn/ASpace_OS_V3.git`, not `Amdkn/Life-OS-2026`.

The canonical Terra launcher still contains:
`cd /d "C:\Users\amado\Life-OS-2026"`

So the launcher names the wrong physical clone.

Current live `:4444` process was independently inspected and is actually running from:
`C:/Users/amado/ASpace_Worlds/Life_OS_2026/node_modules/...`

Conclusion:
**current runtime happens to be canonical, but startup identity is not guaranteed by the launcher.**

M4 requirement: resolve runtime root from the workspace registry/federation identity, not a stale hard-coded clone.

## 2. Frontend maturity — high

Terra is a substantial React 19 / TypeScript / Vite Web OS, not a shell mock.

Repository contains:
- six framework apps plus Agent Portal;
- eight Life Domain stores;
- Zustand state;
- IndexedDB persistence;
- Supabase client;
- local API clients;
- Blackboard event/lock/artifact client;
- MCP adapter;
- CLI;
- auth middleware;
- cross-category event contracts;
- Business bridge;
- tests and validation gates.

The live Vite UI responds at:
`http://127.0.0.1:4444/` -> HTTP 200.

Minor presentation debt:
the root HTML title still reports `My Google AI Studio App`, which is provenance debt rather than a functional blocker.

## 3. Persistence maturity — local-first code exists

`src/lib/idb.ts` is now genuinely local-first.

Current `getAll()`:
1. initializes IndexedDB;
2. starts Supabase pull asynchronously;
3. starts outbox replay asynchronously;
4. returns local records immediately.

Current writes:
- commit into IndexedDB;
- create an outbox entry when authenticated;
- increment a per-item `version`;
- delete through a logical tombstone `_deleted=true`;
- retry cloud sync with exponential backoff.

This is more mature than the older PRDs that described a cloud-blocking read path.

## 4. But offline-first is not yet end-to-end certified

The repo contains `scripts/test-offline-recovery.ts`.

Live execution:
**FAIL**

First failure:
`NotFoundError: No objectStore named outbox in this database`.

The test/fixture opened a database state for which the required V2 `outbox` store was absent.

Therefore the code has an offline/outbox design, but migration/recovery across existing IndexedDB states is not yet proven.

Amy implication:
the UI must not display “synced/offline safe” merely because the outbox code exists.

## 5. API surface is rich but fragmented

### Surface A — direct browser Supabase

`src/lib/supabase.ts`
creates a Supabase client directly in the browser using:
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`

This is appropriate for user-scoped RLS data, but it means some persistence bypasses Terra's local HTTP API.

### Surface B — Business bridge implementation #1

`api/server.ts` + `api/bridge/business-bridge.ts`

- port 3001;
- `/api/bridge/life-to-business`;
- `/api/bridge/business-to-life`;
- simple validation;
- no auth/tenant enforcement;
- no event envelope.

There is no package script that makes this server the obvious canonical runtime.

### Surface C — Business bridge implementation #2

`server/api/harness.ts`

Same endpoint names, but materially different contract:
- strict bind `127.0.0.1:3001`;
- auth scopes;
- tenant enforcement;
- path sanitization;
- rate limiting;
- audit;
- Zod;
- correlation/causation event envelope.

The integration tests target THIS implementation and all pass.

Therefore Terra has **two implementations of the same API with incompatible security/response semantics**.

### Surface D — Blackboard API

`server/blackboard/index.ts`
- Express + Better-SQLite3;
- workspaces;
- events;
- locks;
- artifacts;
- A3 cron dispatcher;
- default port 4445.

Frontend client:
`src/lib/blackboard/client.ts`
correctly defaults to:
`http://localhost:4445/api/blackboard`.

It also has its own IndexedDB read cache for offline fallback.

At audit time no Blackboard service was live and the canonical repo contained no `data/blackboard.sqlite`.

### Surface E — CLI mismatch

`cli/life-os.ts` defaults:
`VITE_BLACKBOARD_API_URL=http://localhost:3001/api/bridge/events`

But:
- the bridge does not expose `/events`;
- Blackboard lives under `:4445/api/blackboard/events`.

This is a broken endpoint contract.

### Surface F — Linear adapter

`src/lib/linear/client.ts` expects:
`http://localhost:3001/api/bridge/linear/sync`.

No matching route was found in either audited 3001 server.

It falls back to appending a Blackboard event, but that fallback also requires the 4445 Blackboard runtime.

## 6. MCP / Tooling maturity — real but independent

Terra contains an MCP launcher and tool registry.

Registered scoped capabilities include:
- get/update 12WY tactics;
- get Life Wheel domains;
- Blackboard post;
- holding/Stripe;
- web audit;
- document parser;
- Linear sync.

MCP auth test:
**PASS**.

This shows Terra already has a useful tool/control-plane primitive. It is not yet unified with the browser HTTP API, Blackboard lifecycle and Supabase sync contract.

## 7. Contract tests — strong signal

Executed:
- server auth middleware test -> PASS;
- MCP auth test -> PASS;
- API harness test -> PASS;
- cross-category contract integration tests -> PASS.

Cross-category tests prove:
- successful dispatch;
- structured rejection;
- idempotency;
- blocked-contract behavior;
- authorized scope constraints.

This is one of Terra's strongest M3 assets and should be reused by Clara rather than replaced.

## 8. Type/build maturity is split

### Production Vite build
`npm run build` -> **PASS**

Evidence:
- 2304 modules transformed;
- main JS chunk approximately 1.24 MB minified / 320 KB gzip;
- build approximately 1m16s.

Warnings:
- mixed static/dynamic imports for auth and migration service;
- >500 KB chunk warning.

### Strict TypeScript
`npm run lint` / `tsc --noEmit` -> **FAIL**

The failures are concentrated in B3 cognitive/matrix contracts:
- `B3WorkerDescriptor`;
- `MatrixWorker`;
- `B3TaskProfile`.

Consumers expect properties absent/renamed in the current types:
- `id`;
- `intelligence`;
- `determinism`;
- `incarnationType`;
- `estimatedTokenCost`;
- `estimatedLatencyMs`;
- `ioAuthorizations`;
- `requiredIntelligence`;
- `requiredDeterminism`.

This is **internal Code↔Contract drift**.

A build succeeding despite this should not be promoted as full contract health.

## 9. Validation gate maturity

Official:
`npm run gate`

Fails on Windows before application checks because:
`TZ=America/New_York ...`
is Unix shell syntax.

Manual gate with `TZ` correctly injected:
- no placeholders -> PASS;
- timezone -> PASS;
- strict typing -> FAIL;
- execution proof -> FAIL because `data/blackboard.sqlite` is absent and no `action_receipt` can be proven.

Therefore Terra's own quality gate says:
**NOT RELEASE-CERTIFIED**.

## 10. Amy convergence diagnosis

Terra is not suffering from lack of code. It is suffering from **too many partially overlapping integration surfaces**.

Current graph:

```text
React / Zustand
 ├─ IndexedDB DomainDB
 │   └─ direct Supabase REST through supabase-js
 ├─ /api/bridge :3001
 │   ├─ simple api/server implementation
 │   └─ authenticated server/api/harness implementation
 ├─ Blackboard :4445
 │   ├─ SQLite events
 │   ├─ locks
 │   └─ action receipts
 ├─ Linear client -> assumed /api/bridge/linear/sync
 ├─ CLI -> stale /api/bridge/events default
 └─ MCP -> tooling registry / adapters
```

This is M3 breadth without M4 convergence.

## 11. Amy requirements for Clara

Do not redesign the Life OS UI.

Clara should make the code surfaces converge behind explicit contracts:

1. **One canonical local API runtime**
   - exact lifecycle;
   - exact bind/ports;
   - versioned namespace;
   - health endpoint;
   - no duplicate route implementation.

2. **One frontend API client layer**
   - no duplicated Business bridge clients;
   - typed request/response schemas;
   - auth/tenant propagation;
   - correlation IDs;
   - degraded-state representation.

3. **Explicit direct-Supabase boundary**
   - user domain data may stay direct/RLS if intentional;
   - orchestration/migrations/privileged operations must stay server-side.

4. **Blackboard role must be explicit**
   - durable local execution/event ledger vs cache vs outbox;
   - startup ownership;
   - receipt contract.

5. **CLI/MCP/React must consume the same domain service contracts**
   rather than three subtly different endpoint maps.

6. **Runtime-source identity**
   must be resolved from Terra federation/workspace registry, not stale hard-coded paths.

7. **No “synced” UI claim without addressable sync evidence.**

## Amy acceptance gate for M4

Terra can be called API-converged only when:
- one endpoint map is canonical;
- all clients derive from it;
- duplicate bridge server is retired or explicitly layered;
- CLI, MCP and browser can execute equivalent bounded actions through the same contracts;
- typecheck passes;
- canonical gate is cross-platform;
- Blackboard receipt evidence exists;
- local-first recovery test passes end-to-end;
- startup resolves canonical Terra identity.
