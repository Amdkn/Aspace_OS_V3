# RORY — Terra / Life OS Supabase + Persistence Maturity Audit

Date: 2026-09-29
Lane: RORY / PERSISTENCE
World: Terra / Life OS 2026
Supabase project: `Life OS` / `hjweyhpmrxqsxfbibsnc`
Purpose: establish the backend/persistence half of Terra Code→API convergence before Clara architecture design.

## Executive finding

Supabase Life OS is a real, healthy, user-scoped persistence backend with domain/framework tables and RLS.

However, it is **not synchronized with Terra's current persistence protocol**.

The most important mismatch is structural:

Terra code now depends on:
- per-item `version`;
- tombstone `_deleted`;
- conflict detection against server version;
- outbox retries.

The live Supabase tables contain **neither `version` nor `_deleted`**.

No migration in the Terra repository defines those columns.

Therefore this is not merely an unapplied migration discovered in the repo. The local-first protocol was implemented/tested in code without completing its cloud data contract.

## Maturity classification

Using the shared audit rubric:
**Rory assesses Terra persistence as M3 — integrated, but pre-convergence.**

The database exists, is secured at row level for user data, and has meaningful historical content. But M4 requires schema-contract parity, migration proofs, replay/reconciliation and current operational evidence.

## 1. Supabase project state

Project:
- name: `Life OS`;
- id: `hjweyhpmrxqsxfbibsnc`;
- region: `us-east-2`;
- status: `ACTIVE_HEALTHY`;
- Postgres 17.6.

No Edge Functions are currently deployed.

No `public` tables are currently present in a Realtime publication.

The active cloud surface is therefore primarily PostgREST/Auth through `supabase-js`.

## 2. Public persistence model is substantial

Framework tables:
- `fw_12wy`;
- `fw_deal`;
- `fw_gtd`;
- `fw_ikigai`;
- `fw_life_wheel`;
- `fw_para`.

Life Domain tables:
- `ld01_business`;
- `ld02_finance`;
- `ld03_health`;
- `ld04_cognition`;
- `ld05_relations`;
- `ld06_habitat`;
- `ld07_creativity`;
- `ld08_impact`.

Additional state:
- `ikigai_visions`;
- `life_wheel_ambitions`;
- `symphony_state`;
- `sys_agent_veto`;
- `sys_shell_routing`;
- `user_profiles`.

This proves Terra is beyond a mock persistence layer.

## 3. RLS and user isolation exist

Framework/domain tables use user isolation equivalent to:
`user_id = auth.uid()`.

Ikigai visions and Life Wheel ambitions have separate own-user CRUD policies.

`symphony_state` has:
- anonymous SELECT;
- service-role INSERT/UPDATE.

The browser uses an anon/publishable-style client surface, not a service-role key.

This is directionally correct for personal user data, though policy optimization/security items remain.

## 4. P0 — local sync protocol and cloud schema disagree

Terra `src/lib/outbox/sync.ts` does:

1. read server `version`;
2. compare server and local versions;
3. detect conflicts;
4. upsert a payload containing:
   - `version`;
   - potentially `_deleted`;
   - `user_id`;
   - `type`;
   - `updated_at`.

Live schema introspection across all relevant public tables:

- `has_version = false`;
- `has_deleted = false`.

No SQL migration under Terra `supabase/` adds these columns.
The directory currently only contains configuration/readme support files.

Repo-wide search finds the version/tombstone protocol only in TypeScript/tests, not in a deployed schema migration.

### Consequence

The code path:
`.select('version')`
cannot satisfy its intended contract against the current live schema.

The upsert of a tombstone/version payload also cannot be relied upon.

Therefore:
**the outbox strategy is architecturally ahead of the cloud schema and is not end-to-end complete.**

## 5. P0 — offline migration/recovery is not certified locally either

Executed:
`npx tsx scripts/test-offline-recovery.ts`

Result:
**FAIL**

Failure:
`NotFoundError: No objectStore named outbox in this database`.

This means the IndexedDB migration/recovery path can encounter an existing DB state without the V2 outbox store expected by current code.

The same synchronization design is thus broken at both boundaries:
- local old-state → current IndexedDB;
- current outbox → live Supabase schema.

Clara/Ryan should treat these as one migration/reconciliation mission, not two unrelated bugs.

## 6. Cloud data is stale relative to September Terra

Live row/freshness evidence:

| Table | Rows | Freshest |
|---|---:|---|
| fw_12wy | 13 | 2026-06-22 |
| fw_deal | 4 | 2026-06-22 |
| fw_gtd | 5 | 2026-06-22 |
| fw_ikigai | 10 | 2026-06-22 |
| fw_life_wheel | 1 | 2026-06-17 |
| fw_para | 4 | 2026-06-22 |
| ikigai_visions | 20 | 2026-06-22 |
| ld01..ld08 | 1 each | 2026-06-22 |
| life_wheel_ambitions | 8 | 2026-06-22 |
| symphony_state | 2 | 2026-07-03 |

This is historical/persistent content, not evidence of current Terra runtime synchronization.

One auth user exists; the latest sign-in observed is 2026-09-18.
No identity details are required for this architecture audit.

## 7. Migration API drift

`src/services/migration.service.ts` calls:
`supabase.rpc('run_adr003_migration')`.

Live Supabase introspection:
**no function named `run_adr003_migration` exists.**

The frontend migration path therefore references a cloud RPC that is absent.

This is another direct Code↔Backend contract break.

## 8. Blackboard persistence is a second durable plane

Terra also contains a Better-SQLite3 Blackboard with:
- workspaces;
- events;
- locks;
- artifacts;
- action receipts.

The A3 validation gate explicitly expects:
`data/blackboard.sqlite`
and at least one `action_receipt`.

Canonical Terra currently has:
- no `data/` directory;
- no Blackboard DB;
- no execution receipt proof;
- no live Blackboard service observed during audit.

Rory interpretation:
Blackboard is a designed persistence/execution ledger, but it is not yet an operationally proven part of the current Terra runtime.

## 9. Current persistence planes

Terra currently has at least four state planes:

### P1 — Browser IndexedDB
Local user/domain/framework working state.

### P2 — Browser outbox
Pending cloud mutations, retries and conflicts.

### P3 — Supabase
User-scoped durable cloud persistence.

### P4 — Blackboard SQLite
Execution events, locks, workspaces, artifacts, receipts.

There is also `symphony_state` in Supabase and application/Zustand state.

M4 does not require collapsing these into one database.
It requires explicit ownership, transitions and reconciliation among them.

## 10. Realtime maturity

No Life OS public table is currently in a Supabase Realtime publication.

No Edge Functions are deployed.

This is not automatically a defect: Terra already uses local-first caching and may not need Postgres Changes for every domain mutation.

But Clara must explicitly decide:
- what needs realtime propagation;
- what remains pull/reconcile;
- what is ephemeral presence;
- what is durable event/evidence state.

Do not turn all domain tables into Realtime merely to claim convergence.

## 11. Security maturity

Current security advisor findings include:

### ERROR
- `public.wrappers_fdw_stats`: RLS disabled in public schema.

### WARN
- mutable search_path on:
  - `tg_set_updated_at`;
  - `handle_new_user`;
  - `trg_symphony_state_touch`.
- `wrappers` extension installed in public schema.
- `handle_new_user()` executable by anon/authenticated while SECURITY DEFINER.
- `rls_auto_enable()` executable by anon/authenticated while SECURITY DEFINER.
- leaked-password protection is not enabled.

These are P1 hardening issues.

They are distinct from the P0 convergence failures.

## 12. Performance maturity

Supabase advisors report:
- repeated `auth.uid()` evaluation in many RLS policies;
- 31 currently unused indexes.

These are optimization opportunities, not evidence that the architecture is unusable.

Do not delete indexes solely from this one observation without workload evidence.

## 13. Contract/event maturity is stronger than persistence deployment

Terra's cross-category contract integration tests PASS for:
- dispatch;
- rejection;
- idempotency;
- blocked contract;
- scope authorization.

This is valuable.

Clara should align persistence/API implementations to these contract semantics rather than replace them with ad hoc CRUD.

## 14. Rory convergence requirements

### A. Schema compatibility contract
Every syncable entity needs a versioned cloud schema matching local concurrency semantics.

Clara must decide whether:
- `version` + tombstone become canonical columns;
- or the local outbox changes to another conflict protocol.

But code and cloud cannot remain different.

### B. Migration ledger
Add explicit, reversible migrations for:
- IndexedDB versions/object stores;
- Supabase schema;
- any data backfill.

The migration state itself must be observable.

### C. Reconciliation receipt
A sync wave must record:
- local source revision;
- outbox count before/after;
- successful operations;
- conflicts;
- retries/dead letters;
- cloud schema/version;
- timestamps;
- evidence URI.

### D. Blackboard ownership
Define whether Blackboard is:
- execution/event ledger;
- offline queue;
- orchestration store;
- or all of these with typed boundaries.

Do not duplicate the DomainDB outbox and Blackboard event queue without explicit semantics.

### E. Supabase API boundary
Keep personal domain data under RLS.
Privileged migrations/integrations must use server-side APIs, not browser RPCs that presume missing privileged functions.

## 15. Rory acceptance gate for M4

Terra persistence can be considered converged when:
- live schema equals the sync contract;
- IndexedDB migration/recovery passes;
- cloud retry/replay is tested against the real schema;
- migration RPCs/routes referenced by code actually exist;
- cloud freshness is explainable;
- Blackboard has an explicit runtime owner and receipt evidence;
- local/cloud conflicts cannot be silently overwritten;
- security P0/P1 items are classified and bounded.
