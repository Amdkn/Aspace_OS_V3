# HANDOVER — 2026-09-29 — RORY → CLARA — TERRA SUPABASE/PERSISTENCE MATURITY

## Maturity
Terra backend/persistence = **M3 Integrated, pre-convergence**.

## Strong assets
- healthy Supabase Life OS project;
- real framework/domain schema;
- RLS/user isolation;
- IndexedDB local-first design;
- outbox retry/conflict concept;
- Blackboard event/lock/artifact model;
- passing cross-category contract tests.

## P0 blockers
1. current TypeScript outbox requires `version` + `_deleted`;
2. live Supabase schema has neither field;
3. no repo migration defines them;
4. offline-recovery test fails because an existing IndexedDB state lacks `outbox`;
5. frontend calls RPC `run_adr003_migration`, absent from live Supabase;
6. cloud domain/framework data is stale (mostly June/July);
7. Blackboard DB/action receipts required by gate are absent from canonical runtime.

## P1 hardening
Supabase advisor:
- RLS disabled on `wrappers_fdw_stats`;
- SECURITY DEFINER functions callable by anon/authenticated;
- mutable function search paths;
- wrappers extension in public;
- RLS performance optimizations;
- unused indexes.

## Clara input
`10_Tech_OS/reports/rory_terra_supabase_backend_maturity_20260929.md`

Consume Amy Terra frontend/API audit before selecting the unified API architecture.
Do not collapse IndexedDB, Supabase and Blackboard into a fake single store; define ownership + reconciliation.
