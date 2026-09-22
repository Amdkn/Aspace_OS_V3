# KPRD-001: [K0] Linear↔WorkGraph reconciliation + stale-state reaper

## Context
We need a deterministic mechanism to reconcile the true state from Linear with our local WorkGraph (`uc.db`) to detect and fix state drifts.
Linear acts as the primary truth, but our local state may drift if a hook is missed or a task is abandoned locally without being cleared.

## Goal
Build deterministic reconciliation between fresh Linear state, WorkGraph/uc.db, and active harness/Jules ownership. Detect abandoned In Progress, completed-but-unprojected work, and drift. Never infer success from UI cache.

## Acceptance Criteria
- Create `10_Tech_OS/kernel/linear_reconciler.py`. It should read from Linear MCP events in `event` table (`linear_mcp_update`) to detect:
    - `abandoned_in_progress`: Work is claimed but Linear is not active/in progress.
    - `ownership_drift`: Work is claimed by harness A but Linear says it's owned by harness B.
    - `completed_but_unprojected`: Linear is done but local state is not 'done'.
    - `state_drift`: Local state is 'done' but Linear is not done.
- Create `10_Tech_OS/kernel/linear_reaper.py`. It should consume the report from `linear_reconciler.py` to fix drift by safely resetting `abandoned_in_progress` and `ownership_drift` to `pending` and clearing the claim.
- Create `10_Tech_OS/kernel/test_linear_reconciler.py` to verify this logic works.
- DO NOT EDIT other unrelated domains or authority contracts.
