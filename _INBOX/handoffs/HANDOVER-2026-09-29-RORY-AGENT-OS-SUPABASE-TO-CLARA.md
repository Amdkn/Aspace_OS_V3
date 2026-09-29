# HANDOVER — 2026-09-29 — RORY → CLARA — AGENT OS SUPABASE / STATE

## Mission
Provide the backend/persistence half of the Agent OS Full-Stack Unification analysis before Clara architecture design.

## Verified facts
- Supabase `Agent OS Backend` is ACTIVE_HEALTHY.
- Canonical backend domain is schema `aspace`, not `public`.
- 13 session bindings exist, but none are currently `active/waiting`.
- `claim` has zero rows.
- latest session_binding update is from 2026-09-27.
- latest Agent OS world sync is from 2026-09-27 and is ~1d16h stale at audit.
- successful world sync recorded parent `Agent-OS@4b73326`.
- parent gitlink records Desktop `7c6dc8b`, while actual Desktop HEAD is `c0dc5d2`.
- `aspace` tables have RLS but no client policies.
- no `aspace` table is in the Realtime publication.
- public intent capture exists via Edge Function -> RPC, but this is not a general state API.

## Backend problem
Supabase persistence, local `uc.db`, live processes and Agent OS source snapshots are separate evidence planes and are not reconciled into a single runtime-presence projection.

## Required Clara input
Use `10_Tech_OS/reports/rory_agent_os_supabase_backend_audit_20260929.md`.
Consume Amy commit `c2091d7164c7e6e125d6e8504eb5204f21b49b32` in parallel.

## Design guardrails
- persisted status != liveness;
- live work ownership requires claim/lease semantics;
- runtime state needs freshness TTL and evidence;
- parent repo SHA alone is not a complete Agent OS sync fingerprint;
- do not expose raw `aspace` tables directly to browser before auth/RLS contract;
- no service-role secret in frontend;
- design one explicit API Projection Layer and one reconciliation protocol before UI integration.
