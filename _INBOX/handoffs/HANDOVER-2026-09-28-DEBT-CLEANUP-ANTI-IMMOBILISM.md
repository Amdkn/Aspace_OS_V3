# HANDOVER — 2026-09-28 — Anti-immobilism / debt cleanup / continuity reset

## Purpose

Resume A'Space V3 from a **truthful executable state** after removing the technical debt and design rules that had turned safety mechanisms into global immobilism.

This handover supersedes older continuity notes for the topics covered here.

Do **not** rebuild context from stale branches, old Orca worktrees, historical Linear `In Progress` states, or old README doctrine.

## First read order

1. `MEMORY.md`
2. `40_Memory_Wiki_OKF/AGENTS.md`
3. this handover
4. `ASPACE_ACTIVE_INTENTS.yaml`
5. `ASPACE_WORKSPACE_REGISTRY.json`
6. Supabase project `biyecksylqonuovqmbtz`, schema `aspace`
7. Linear SOH/SOB
8. GitHub `Amdkn/Aspace_OS_V3`

## Canonical main at handover creation

- Repo: `Amdkn/Aspace_OS_V3`
- Main: `9047917be90fe5babe0d668a882982d47991772a`
- Root worktree: `C:/Users/amado/ASpace_OS_V3`
- Root branch at handover authoring: `docs/handover-debt-cleanup-2026-09-28`
- Nested Coach OS repo commit promoted during cleanup:
  - `omk-services/OMK-DESKTOP-WEB-OS@df8423b582638064bdbd1bee0a286e84300d9093`

## Merged cleanup sequence

### PR #178 — anti-immobilism
Merged commit: `4529a7fc54497de491aaa01e0bc279d892ffb8ab`

Removed design rules that froze Life/Business:

- `hermes_cron.ps1` no longer forbids Life/Business execution.
- unrelated Kernel debt cannot globally block Life/Business.
- ambiguity defaults to the smallest reversible assumption.
- escalation is reserved for irreversible decisions, safety, unavailable credentials, or destructive contradictions.
- canceled/superseded blockers no longer freeze descendants.
- only explicit `[NO_AUTODISPATCH]` opts out of fleet dispatch.
- untagged issues in the three canonical projects can be classified by project fallback.
- Companion concurrency is runtime configurable:
  - `ASPACE_COMPANION_PARALLELISM`
  - `ASPACE_MAX_DISPATCH_PER_TICK`
  - per-Core active limits
  - `ASPACE_MAX_ACTIVE`
- default remains conservative: one active session per Companion.
- `50_Distillation` is a memory/canon promotion gate, not a Capture/execution gate.
- mandatory `IPBD → SDD → ADR → PRD → TDD` was replaced by **smallest sufficient contract**.
- root doctrine no longer says disk is the unique universal truth.

Validation at merge:
- Python compile PASS.
- PowerShell parse PASS.
- 28/28 targeted Kernel tests PASS.

### PR #179 — IPBD capture recovered from ghost worktree
Merged commit: `e0876db169f5d71b9042461f37b39ec10afa7599`

Recovered and versioned the active IPBD path that had existed live but only in stale local state:

- `scripts/aspace_capture.py`
- `scripts/test_aspace_capture.py`
- `10_Tech_OS/kernel/supabase/functions/aspace-intent-capture/`
- IPBD migrations
- Doctor11 IPBD ADR
- Workspace Registry IPBD metadata and current surface stewardship

Validated live Supabase contract:
- 6 IPBD tables:
  - `capture_event`
  - `intent`
  - `intent_source`
  - `intent_link`
  - `intent_transition`
  - `capture_cursor`
- 3 views:
  - `v_intent_inbox`
  - `v_intent_open`
  - `v_intent_unresolved_age`
- private `aspace.capture_ipbd(...)`
- public restricted `public.aspace_capture_ipbd(...)`
- Edge Function `aspace-intent-capture` ACTIVE, version 1.
- local-first capture tests: 3/3 PASS.

Important:
- capture writes local NDJSON outbox before network projection.
- no session death may erase unresolved IPBD.
- do not invent a parallel intent ledger.

### PR #180 — worktree reconciliation
Merged commit: `9be542fd1bf0b7b6bb1f13a508a8b338fdc07bd3`

Removed stale Orca/worktree debt and made identity sync reproducible.

Deleted:
- broken `.orca-preparing` worktrees.
- old fish/temporary worktrees:
  - opah
  - scup
  - snook
  - stickleback
- stale workspace-registry worktree after useful content was promoted.
- old sandbox/review worktrees after proof preservation.

Preserved useful untracked work before deletion:
- Bill Coach OS Discovery Interview Canvas moved into its real nested repo and pushed.

Added:
- `scripts/sync_orca_identity_worktrees.py`

Policy:
- persistent identity worktrees follow `origin/main` when idle.
- dirty worktrees are **never** auto-reset.
- branch divergence must mean active bounded work, not stale context.

Identity worktrees:
- Amy
- Bill
- Clara
- Doctor11
- Doctor12
- Doctor13
- Graham
- Nardole
- Rick
- River
- Rory
- Ryan
- Yaz

At the final verification before this handover:
- all 13 identity worktrees were clean.
- all 13 were `ahead=0 / behind=0`.
- all 13 were at `9047917b`.
- total registered worktrees = root + 13 identities = 14.

### PR #181 — Supabase hardening + migration history
Merged commit: `9047917be90fe5babe0d668a882982d47991772a`

Fixed real Supabase debt:

- pinned `search_path` on:
  - `aspace.touch_updated_at`
  - `aspace.enforce_work_transition`
  - `aspace.log_intent_transition`
  - `aspace.forbid_intent_delete`
  - `aspace.touch_intent_updated_at`
  - `public.audit_memberships_changes`
- FORCE RLS enabled on all newer IPBD tables.
- 15 missing FK covering indexes added.
- local migration filenames aligned to actual Supabase remote migration history.

Remote migration history:
- `20260927121424_aspace_machine_blackboard_v1`
- `20260927122738_aspace_rls_and_world_catalog_v1`
- `20260927175528_aspace_shared_board_views_v1`
- `20260927225031_aspace_ipbd_intent_ssot_v1`
- `20260927230005_aspace_ipbd_capture_rpc_v1`
- `20260928034812_harden_aspace_security_and_fk_indexes`

Supabase advisors after hardening:
- `function_search_path_mutable`: cleared.
- `unindexed_foreign_keys`: cleared.
- remaining `RLS enabled no policy` is intentional INFO:
  - `aspace` is private.
  - anon/authenticated have no table SELECT privileges.
  - do not create permissive policies merely to silence the advisor.
- `unused_index` immediately after index creation is not actionable.

Read:
- `10_Tech_OS/kernel/supabase/SECURITY.md`

## Anti-immobilism invariants

These are now the operating rules.

### 1. Capture before certification

IPBD/raw operational signals may be captured immediately.

Distillation, OKF, ontology, documentation or TTS must not block:
- Capture
- read-only diagnosis
- simulation
- reversible edits
- isolated tests
- bounded branch/worktree execution

### 2. Smallest sufficient contract

Do not force every intention through every document type.

Use only the contract required by risk:
- simple reversible work may compile IPBD directly to bounded Work.
- durable architectural decisions may require ADR/PRD/TDD.
- evidence remains mandatory for promotion/closure.

### 3. Typed truth, not one global SSOT

- filesystem = local artifact reality
- GitHub = version/history/artifact lineage
- Supabase `aspace.intent/capture_event` = shared IPBD
- Supabase WorkGraph = shared machine execution state
- Linear = human governance/control surface
- OKF = durable certified memory
- local `uc.db` = sovereign local cache/projection

No tool globally outranks all others.
Reconcile by type + provenance + freshness.

### 4. Stewardship is accountability, not exclusivity

Current primary surfaces:
- Ryan → GitHub software factory
- Rory → Linear / Life governance A1–A3
- Graham → Supabase shared state/IPBD/evidence
- Amy → Herdr persistent harness interface
- River → Google Workspace workflow plane + Jev reflex plane
- Yaz → Tinybird / LiDAR-style behavioral observability

Every surface remains shared where the work requires it.

### 5. In Progress means execution exists

Linear `In Progress` is permitted only when there is:
- an unexpired claim,
- an active session binding,
- a freshly observed executing worker.

A queued, waiting, old, historic or merely attached session is not In Progress.

## Linear reconciliation completed

Before reconciliation:
- SOH In Progress: 21
- SOB In Progress: 4
- total false In Progress: 25
- Supabase claims: 0
- active session bindings: 0
- running work: 0

Action:
- all 25 moved from `In Progress` to `Backlog`.
- each received a reconciliation comment with the reactivation rule.

Final:
- SOH In Progress = 0
- SOB In Progress = 0

Important:
- no intent was canceled by this action.
- status truth was corrected; intent was preserved.

## WorkGraph reconciliation

Before final reconciliation:
- 9 `aspace.work` rows were `waiting`.
- 3 already had externally completed outcomes:
  - work 2 / SOB-92 / PR #159
  - work 3 / SOB-1
  - work 4 / SOB-90 / PR #162
- all three had **no pre-execution prediction**.

Because WorkGraph law forbids fake retrospective success:
- no prediction was fabricated.
- these three were classified `failed` with reconciliation metadata:
  - external outcome exists
  - governance contract was violated
  - do not rewrite history as WorkGraph `done`

Final WorkGraph status:
- `failed`: 3
- `waiting`: 6
- claims: 0
- active sessions: 0
- running work: 0

The remaining six waiting rows are backlog/waiting projections, not running execution.

## Git branch cleanup

### Local

Final local branches are intentionally only:
- `main`
- `Amdkn/Amy`
- `Amdkn/Bill`
- `Amdkn/Clara`
- `Amdkn/Doctor11`
- `Amdkn/Doctor12`
- `Amdkn/Doctor13`
- `Amdkn/Graham`
- `Amdkn/Nardole`
- `Amdkn/Rick`
- `Amdkn/River`
- `Amdkn/Rory`
- `Amdkn/Ryan`
- `Amdkn/Yaz`

Deleted local merged/superseded branches included:
- old `Yaz` duplicate
- old review/sandbox/fish branches
- #178–#181 feature/fix branches
- #168/#169 workspace branch
- old merged harness selector branch
- old local preservation branch after ancestry verification

### Local-only unique branches archived before deletion

These had unique commits and no remote branch, so they were converted to pushed annotated tags before deleting the branch refs:

- `archive/2026-09-28/pr-8-branch`
- `archive/2026-09-28/pr156`
- `archive/2026-09-28/temp-rebase-187`

No unique commit was discarded.

### Remote

Remote branch inventory before final cleanup:
- 164 non-main branches.
- 20 had merged PRs.
- 144 had closed-unmerged PRs.
- 0 had no PR record.
- 0 open PRs.

Action:
- the 20 merged-PR branches were deleted.
- the 144 closed-unmerged branches remain as **historical quarantine**.

Do not treat those 144 branches as active execution.
They are preserved because closed-unmerged PRs can still contain unique historical work.
Any future purge must first deduplicate or archive their unique commits.

## Runtime / scheduled tasks observed during cleanup

- `ASpace Desktop Commander`: Running.
- `ASpace Hermes Jules Supervisor`: Disabled.
- `ASpace Hermes TechOS Dispatcher`: Disabled.
- `ASpace Jules Proxy`: configured; proxy health returned OK with its own MCP PID.
- `ASpace_V3_Battement`: Ready.
- `Hermes_Gateway`: Disabled.

Two `google-jules-mcp` processes were investigated:
- one belongs to the canonical Jules proxy.
- one is an Antigravity language-server MCP sidecar.
- the second was **not** a zombie and was not killed.

Do not re-enable Hermes scheduled dispatch merely to make the system look active.
Re-enable only after the persistent Hermes/Orca Bot-Mode path is explicitly certified against the current claim/binding rules.

## Known residuals — deliberate, not hidden

### 1. 144 remote closed-unmerged PR branches

State: quarantined historical corpus.

Not an execution blocker.
Not safe to delete blindly.
Future cleanup should create a semantic/patch-equivalence ledger first.

### 2. Six WorkGraph waiting rows

State: legitimate waiting/backlog projections.
No worker is running them.
Linear is no longer lying about execution.

### 3. Hermes scheduler disabled

This is a safety state after previous zombie/quota incidents, not a doctrine that Life/Business must stop.
Manual or bounded execution can proceed.
Automated dispatch should be re-certified before reactivation.

## Immediate next session objective

Do **not** reopen ontology/topology cleanup merely because this handover exists.

The next session should resume from value production:

1. read current IPBD open intents from Supabase.
2. select a Life or Business value intent with a clear outcome.
3. compile only the smallest sufficient contract.
4. acquire claim/bind active worker before setting Linear In Progress.
5. produce evidence/outcome.
6. close or transition the originating IPBD based on outcome evidence.
7. measure reduced A0 dependence, not ticket throughput.

For the Q4 premortem/wargame work, keep the key failure invariant:

> Projection completion is not intent resolution.

A PR, ticket, WorkGraph row, document or UI state may close while the originating IPBD remains unresolved.

## Verification commands

### Root + worktrees

```powershell
cd C:\Users\amado\ASpace_OS_V3
git status --short --branch
python scripts\sync_orca_identity_worktrees.py
git worktree list
```

Expected:
- root clean on current main after this handover PR is merged.
- 13 identity worktrees clean.
- 0 ahead / 0 behind when idle.

### Kernel targeted tests

```powershell
cd C:\Users\amado\ASpace_OS_V3\10_Tech_OS\kernel
python -m unittest test_kernel_fleet_tick.py test_uc_workgraph.py test_fleet_ownership.py
```

Known last result:
- 28/28 PASS.

### IPBD local-first

```powershell
cd C:\Users\amado\ASpace_OS_V3
python scripts\test_aspace_capture.py
```

Known last result:
- 3/3 PASS.

## Bottom line

The cleanup changed the system from:

`documentation/gates/status theater → blocked execution`

to:

`capture → smallest sufficient contract → bounded execution → evidence → outcome → memory after proof`

The next agent must preserve this direction.
