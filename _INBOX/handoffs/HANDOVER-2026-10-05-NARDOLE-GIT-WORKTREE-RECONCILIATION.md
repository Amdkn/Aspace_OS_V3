# HANDOVER — Nardole Git / Worktree Reconciliation

Date: 2026-10-05
Lane: Nardole / DISPATCH / INTERCONNECTION
Repo: Amdkn/Aspace_OS_V3
Canonical policy: docs/governance/GIT_BRANCH_WORKTREE_LIFECYCLE_V4.md

## Verified current state

Latest local reconciliation command completed successfully.

- worktrees: **16**
- local branches: **27**
- latest confirmed remote-tracking count before the last retirement: **106**
- Ryan-MachineFabric / `feat/ryan-harness-runtime-p1p4-2026-09-28`:
  - clean
  - `git cherry origin/main HEAD` empty
  - PR #210 merged
  - worktree retired
  - local branch retired
  - remote branch explicitly deleted

## Important forensic correction

Two worktrees that had appeared massively dirty disappeared from both the filesystem and Git worktree registry between forensic checks:

- `C:/Users/amado/ASpace_OS_V3/.worktree_review_233`
- `C:/Users/amado/orca/workspaces/ASpace_OS_V3/Agy-Bill`

Observed earlier:
- review233: ~8965 status entries, mostly staged deletions
- Agy-Bill: ~8979 status entries, mostly staged deletions

Observed later:
- both paths absent
- both absent from `git worktree list`
- `review/agy-bill-224-2026-09-29` local + remote-tracking refs absent

Do **not** claim Nardole removed them; disappearance was observed externally and remains unattributed.

## Homes already converged to current main

Fast-forwarded and pushed to their `Amdkn/*` home refs:

- Doctor11
- Doctor12
- Doctor13
- Rick

Already at main before that:
- Amy
- Clara
- Nardole
- Rory

Yaz was not touched because a live shell had its cwd in the Yaz worktree.

## Live-process vetoes observed

Processes with cwd in these homes/worktrees:

- Graham — live cmd.exe
- Yaz — live cmd.exe
- Ryan — live cmd.exe + bash shells

Treat these as ACTIVE until rechecked.

## Remaining worktrees of interest

### Root main
`C:/Users/amado/ASpace_OS_V3`

Last observed:
- dirty: 86 entries
- behind current origin/main
- no reset/pull/clean authorized

Rule: route useful local state out before making root an exact integration mirror.

### recover/219-functional-928661
Path:
`C:/Users/amado/ASpace_Worktrees/manual_sparse/219-928661`

Last observed:
- dirty: 11 entries
- no unique commits at HEAD vs origin/main
- Issue #219 OPEN
- contains local code/evidence changes:
  - FACTORY_BLUEPRINT.json
  - process_broker.py
  - run_v0_local_acceptance.py
  - acceptance.json
  - AMF evidence JSONs
  - serve snapshots / manual evidence

Classification: **DIRTY_SALVAGE**
Do not clean/reset. This is the next high-value DC Sovereign evidence cell.

### Agy
Branch:
`feat/antigravity-council-of-doctors-2026-09-28`

Last observed:
- 7 unique commits vs main
- 1 untracked file:
  `10_Tech_OS/council/global_agent_projection_20260928.json`
- PR #187 CLOSED, NOT MERGED
- no process owner at last liveness scan

Classification: **ARCHIVE_OR_SALVAGE**, not disposable.

### River
Branch:
`Amdkn/River`

Last observed:
- clean
- 4 unique commits vs main:
  - 16253806 feat(system-one): reconcile River reflex canary with fractal mesh
  - ce5bff73 docs(handover): record River branch reconciliation
  - 8750271d docs(mirofish): record River runtime preflight
  - 21353598 evidence(mirofish): persist provider failure canary
- PR #198 CLOSED, NOT MERGED
- institutional home branch, so do not delete the home

Classification: **HOME_WITH_UNIQUE_HISTORY**.
Recommended next action:
1. preserve current River head with an archive tag;
2. inspect whether those 4 commits should be salvaged into a fresh bounded PR;
3. only after disposition, fast-forward home to current main.

### Bill
Branch:
`Amdkn/Bill`

Last observed:
- no unique commits vs main
- untracked `50_Distillation/_raw_inbox/`
- no live process owner at last scan

Classification: **HOME_DIRTY_UNTRACKED**.
Inspect raw inbox before deciding ignore/archive/promote, then sync home.

### Graham
Branch:
`Amdkn/Graham`

Last observed:
- clean
- 1 unique commit vs main
- live cmd.exe in worktree

Classification: **ACTIVE_HOME_WITH_UNIQUE_HISTORY**.
Do not touch until liveness/mission is reconciled.

### Yaz
Branch:
`Amdkn/Yaz`

Last observed:
- clean
- no unique commits vs main
- significantly behind current main
- live cmd.exe in worktree

Classification: **ACTIVE_HOME_STALE**.
When shell/session ends, fast-forward home to current main and push.

### Ryan
Branch:
`feat/ryan-discover-ai-m0-m7-2026-09-29`

Last observed:
- dirty: 7
- 9 unique commits vs main
- multiple live shells/processes

Classification: **ACTIVE_MISSION**.
Do not retire or reset.

## Retired/archived during prior waves

Not exhaustive; authoritative receipts:
- `10_Tech_OS/reports/GIT_BRANCH_RETIREMENT_WAVE1_2026-10-04.json`
- `10_Tech_OS/reports/GIT_BRANCH_RETIREMENT_WAVES2_8_2026-10-04.json`
- `10_Tech_OS/reports/WORKTREE_RECONCILIATION_WAVE1_2026-10-04.json`

Important archive tags include:
- archive/recover-jules-314-dirty-2026-10-04
- archive/dc-sovereign-case-collision-2026-10-04
- archive/pr332-truth-projection-rebase-2026-10-04
- archive/mirofish-pr204-canary-2026-10-04
- archive/dc-p6-local-salvage-2026-10-04
- archive/backup-River-pre-reconcile-20260928

## Next execution order

1. **recover/219 DIRTY_SALVAGE**
   - compare local dirty files against current main and Issue #219 acceptance gates;
   - preserve/promote only genuinely useful DC Sovereign evidence/code;
   - no reset/clean.

2. **River unique-history disposition**
   - archive current home head;
   - classify 4 commits for salvage PR vs archive-only;
   - then converge River home to current main.

3. **Bill raw inbox**
   - inspect `50_Distillation/_raw_inbox/`;
   - classify as source input vs generated residue;
   - route to canonical storage or ignore rule before home sync.

4. **Agy PR #187**
   - preserve untracked global agent projection;
   - decide salvage PR vs archive-only for 7 unique commits;
   - retire temporary mission worktree after preservation.

5. **Active homes**
   - recheck Graham / Yaz / Ryan process liveness;
   - never fast-forward/reset while an active harness shell owns the cwd.

6. **Root main convergence LAST**
   - classify 86 dirty entries;
   - route useful state into bounded branches/archives;
   - only then make root exact clean mirror of origin/main.

## Safety invariants

- No `reset --hard` on dirty worktrees/root.
- No bulk stash/clean.
- No branch/worktree retirement without dirty + unique-history + liveness checks.
- Preserve closed-unmerged or local-only state with archive tags before retirement.
- Institutional `Amdkn/*` home refs are not disposable mission branches.
- GitHub merge/CI truth is not runtime truth.
