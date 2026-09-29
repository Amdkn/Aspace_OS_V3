# RORY — Agent OS Backend / Supabase / Runtime State Audit

Date: 2026-09-29
Lane: RORY / PERSISTENCE
Scope: Agent OS Backend Supabase project, persistence, runtime state and reconciliation before Clara architecture design.

## Executive finding

The Supabase project `Agent OS Backend` is healthy as a service, but it is not currently synchronized with the live Agent OS Desktop/runtime.

The backend has a substantial internal `aspace` schema, but:
- there are no active/waiting session bindings;
- there are no live claims;
- Agent OS world synchronization is stale;
- the last Agent OS snapshot does not include the current Desktop submodule HEAD;
- no `aspace` table is published through Supabase Realtime;
- RLS is enabled across the `aspace` tables, but no client policies exist;
- the current frontend does not consume this backend directly.

This is a state-plane reconciliation problem, not a database availability problem.

## Project

Supabase project:
- name: `Agent OS Backend`;
- project id: `biyecksylqonuovqmbtz`;
- region: `us-west-2`;
- project status: `ACTIVE_HEALTHY`;
- Postgres: 17.6.

## Backend state model observed

The `aspace` schema contains state primitives including:
- `intent`;
- `capture_event`;
- `work`;
- `work_dependency`;
- `claim`;
- `session_binding`;
- `event`;
- `evidence`;
- `sync_run`;
- `workspace_world`;
- `world_asset`;
- `world_entity`;
- `dlq`;
- `prediction`;
- `tape`.

Views include:
- `v_active_sessions`;
- `v_session_mesh`;
- `v_work_board`;
- `v_agent_os_entities`;
- `v_world_catalog`;
- `v_intent_*`.

## Freshness snapshot

Observed around 2026-09-29 00:59 EDT:

| Object | Rows | Freshest persisted timestamp |
|---|---:|---|
| capture_event | 3 | 2026-09-28 02:46:56 UTC |
| claim | 0 | none |
| event | 6 | 2026-09-28 20:46:45 UTC |
| intent | 11 | 2026-09-28 07:51:48 UTC |
| session_binding | 13 | 2026-09-27 17:48:54 UTC |
| sync_run | 2 | 2026-09-27 12:36:49 UTC |
| work | 16 | 2026-09-28 14:21:29 UTC |

Live queries show:
- `session_binding where status in ('active','waiting')` -> **0 rows**;
- `claim` -> **0 rows**.

Therefore Supabase currently contains no proof that any Agent OS worker is actively bound/claimed.

## Session views are not sufficient as a liveness oracle

`v_active_sessions` selects session bindings whose persisted status is `active` or `waiting`.

It does **not** itself apply:
- a freshness TTL;
- a live claim requirement;
- a process heartbeat;
- a worker PID/process check;
- a provider health check.

`v_session_mesh` exposes all bindings but also has no liveness derivation.

Rory conclusion:
**persisted binding status != runtime presence**.

## Agent OS world synchronization drift

Latest successful Agent OS world sync:
- sync id: `2ec3a3d3-d4ca-47c3-ae77-a2837eebc070`;
- source branch recorded: `main`;
- source git SHA: `4b73326954b602134a51ed9bad147d187a9479b0`;
- source root: `C:/Users/amado/ASpace_OS_V3/00_Amadeus/10_Observers/agent-os`;
- mode: `snapshot`;
- assets: 178;
- entities: 262;
- completed: `2026-09-27 12:36:49 UTC`.

Agent OS entities have `max_synced_at = 2026-09-27 12:33:33 UTC`.

At audit time this snapshot was roughly 1 day 16 hours old.

### Nested-repo mismatch

Parent Agent-OS HEAD:
`4b73326954b602134a51ed9bad147d187a9479b0`.

The committed desktop gitlink in that parent:
`7c6dc8bb1907a583a02d2f80b6df3c410dcf56bd`.

Actual Desktop repo HEAD:
`c0dc5d28148c9d8a33d7222bd6740b30b1005f65`.

Therefore a parent SHA alone is insufficient to prove the Agent OS UI/source world is synchronized. The sync fingerprint must include nested repo/submodule gitlinks and observed working HEADs.

## Data API / Realtime boundary

Observed:
- no public tables in `public`;
- `aspace` tables are internal;
- no `anon` / `authenticated` RLS policies were found for `aspace`;
- no `aspace` table appears in the Supabase Realtime publication;
- Supabase security advisor reports 19 `aspace` tables with RLS enabled and no policy.

This is not automatically an error if the schema is intentionally service-side. It means the frontend must **not** be connected directly to these tables until Clara defines an explicit API/auth boundary.

## Existing API entrypoint

Public RPC:
`public.aspace_capture_ipbd(...)`.

Edge Function:
`aspace-intent-capture`
- status: ACTIVE;
- `verify_jwt=false`;
- uses a custom `x-aspace-capture-token` SHA-256 check;
- calls `public.aspace_capture_ipbd` using the project service-role key server-side.

Important:
- service role remains server-side in the function;
- this function is a bounded intent-capture ingress, not a general Agent OS query/sync API;
- its custom-token authentication model needs to be treated separately from future user-facing/runtime APIs.

## Realtime / Presence implications

Current Supabase documentation distinguishes:
- Broadcast for most realtime application events;
- Presence for online/offline state and counters, used sparingly;
- Postgres Changes as a simpler option, with scalability limitations and per-subscriber authorization cost.

Rory design input:
Do not expose every internal `aspace` table through Postgres Changes merely to make the UI look live.

Prefer an explicit projection of runtime state and broadcast only the minimal change envelope required by the UI.

## Backend liveness contract required before Clara design

Rory does not choose the final schema, but Clara needs a backend contract that can derive one runtime state from multiple evidence sources.

Minimum evidence dimensions:
- declared capability / registry identity;
- process observation;
- provider health;
- session binding;
- work id;
- claim existence + expiry;
- latest event timestamp;
- evidence artifact;
- repo / branch / head SHA / PR;
- last successful synchronization;
- freshness TTL.

Suggested semantics:
- `LIVE`: fresh process/provider observation + fresh session binding + valid claim when work is owned;
- `WAITING`: fresh binding with explicit waiting state, no execution claim required;
- `STALE`: prior live/bound state but evidence older than TTL;
- `OFFLINE`: explicit process/provider absence;
- `FAILED`: recent failure evidence;
- `UNKNOWN`: not enough evidence.

A database row should never become `LIVE` merely from a stored enum.

## API Projection Layer requirement

Before Amy consumes Supabase state, Clara should design one stable query boundary.

Candidate implementation mechanisms for Clara to choose among:
- read-only versioned RPC;
- Edge Function API;
- security-invoker projection view behind a server;
- server-side Broadcast channel fed from reconciliation;
- combination of the above.

Constraints:
- no service role in browser;
- no blanket `anon/authenticated` grants;
- no direct exposure of raw orchestration tables before RLS/auth model exists;
- no duplicate truth between `uc.db` and Supabase without explicit reconciliation semantics.

## Sync contract requirement

A future Agent OS world sync receipt must fingerprint at least:
- parent repo SHA;
- parent branch;
- each nested repo/submodule committed gitlink;
- each nested repo observed HEAD;
- dirty/clean state;
- sync started/completed timestamps;
- asset/entity counts;
- sync status;
- evidence URI.

A successful parent snapshot with changed nested HEAD must be considered stale for UI/source representation.

## Rory handoff

Return-to: CLARA / DESIGN-FORGE.
Dependency: consume Amy frontend/API audit at commit `c2091d7164c7e6e125d6e8504eb5204f21b49b32`.

Rory acceptance criterion:
Clara can design a single persistence/reconciliation contract in which runtime presence, UI status, local kernel state, Supabase bindings/claims and source snapshots cannot silently disagree.
