# A'Space V4 — Git Branch & Worktree Lifecycle

Status: canonical governance
Date: 2026-10-04
Stewardship: Clara/Forge + Nardole/Dispatch + Graham/State + Yaz/Observe + Ryan/Build

## Why this exists

A'Space uses many parallel harnesses, Jules workers, persistent holon homes, recovery lanes,
and short-lived implementation branches. Git branches and filesystem worktrees therefore
must be reconciled as two projections of the same execution history.

A branch is not a task, an agent, or a holon identity.

## Current audit snapshot — 2026-10-04

Repository: `Amdkn/Aspace_OS_V3`

Observed:
- 281 remote branches after fetch/prune;
- 116 local branches;
- 0 open pull requests at audit time;
- only 8 remote branches are direct ancestors of `origin/main`;
- many merges use squash/rebase, so ancestor-merged count is NOT a safe retirement classifier;
- at least 17 remote branch names are currently checked out by local worktrees;
- the root checkout `C:\Users\amado\ASpace_OS_V3` is dirty and was 159 commits behind `origin/main` at audit time.

Therefore: no bulk delete, reset, or pull from the dirty root checkout.

## Canonical branch classes

### 1. Protected institutional refs — KEEP

Examples:
- `main`
- explicitly approved long-lived `Amdkn/<Holon>` home refs
- release refs/tags
- any ref required by a live deployment or runtime contract

Long-lived holon refs are navigation/home pointers, not permanent development streams.
Mission mutations should still occur on bounded mission branches.

### 2. Mission branches — SHORT LIVED

Examples:
- `feat/*`
- `fix/*`
- `docs/*`
- `design/*`
- `test/*`

Lifecycle:
`create -> worktree -> PR -> CI/review -> merge -> retire branch -> retire worktree`.

Default target: main.

### 3. Worker branches — EPHEMERAL

Examples:
- `jules-*`
- `autopublish/*`
- `AUTO_CREATE_PR*`

These must not accumulate indefinitely.

After a merged PR they are immediate retirement candidates.
Closed-unmerged worker branches receive a short salvage window, then either:
- preserve unique work through a new bounded branch/PR; or
- archive a unique head; or
- retire as no-value residue.

### 4. Recovery/backup branches — TTL BOUNDED

Examples:
- `recover/*`
- `backup/*`

Recovery is a temporary state, not a permanent namespace.

Every recovery branch needs:
- origin incident/issue;
- owner;
- evidence;
- expiry/reconciliation condition.

After reconciliation, retire it.

## Evidence hierarchy for branch retirement

Never classify solely with `git branch --merged`.

Use this order:

1. PR state and exact head branch.
2. PR merge/close evidence and CI/review evidence.
3. Reachability in `origin/main`.
4. Patch equivalence against `origin/main` for squash/rebase merges.
5. Unique commit inspection.
6. Active worktree and dirty filesystem state.
7. Runtime/session liveness for runtime-owned worktrees.

## Retirement verdicts

### RETIRE_MERGED
PR merged or patch-equivalent to main, no active dirty worktree, no unresolved effect.

Action:
- delete remote branch;
- remove clean worktree;
- delete local branch;
- fetch/prune;
- record receipt.

### RETIRE_SUPERSEDED
Work intentionally replaced by a newer accepted path.

If unique commits matter:
- preserve them using an annotated archival tag or a new bounded salvage PR.
Then retire the branch.

### SALVAGE_REQUIRED
Closed/unmerged or orphan branch contains unique useful commits.

Action:
- do NOT delete;
- create the smallest new bounded branch from current main;
- cherry-pick only the wanted commits;
- open one focused PR;
- retire the old branch after acceptance.

### KEEP_ACTIVE
Branch is checked out by a live worktree, has an open PR, has an active claim/lease,
or belongs to a live harness session.

### KEEP_HOME
Approved persistent holon home ref.

The home branch should periodically converge to main and should not become an
unbounded private fork.

### REVIEW_ORPHAN
No PR, no known claim, no current worktree, unique commits exist.

Requires Graham/Nardole provenance review before deletion.

## Local worktree law

Never remove a worktree because its remote branch disappeared.

Before worktree retirement check:
1. `git status --porcelain` is empty;
2. no unpushed/unreferenced commit needs preservation;
3. no active harness/session owns the path;
4. branch outcome is merged/superseded/archived;
5. evidence/return_to has been written.

Then:
```
git worktree remove <path>
git branch -d <branch>
git worktree prune
git fetch --prune
```

For squash-merged branches, `git branch -d` may refuse because ancestry was rewritten.
Use force deletion only AFTER PR/patch-equivalence evidence proves safe retirement.

## Locked and detached worktrees

A locked worktree is never force-removed until its harness/process ownership is checked.

A detached worktree must be checked for reachable commits:
- if HEAD is already reachable from main/tag, it may be retired;
- if HEAD contains unique useful work, tag or salvage it first.

## Root checkout law

`C:\Users\amado\ASpace_OS_V3` should become a clean integration mirror of `origin/main`.

Do not develop directly in root main.

Current dirty root must first be reconciled:
- inventory tracked modifications and untracked artifacts;
- route useful changes into bounded branches/worktrees;
- archive or ignore generated residue;
- only after all useful state is preserved, restore root main to exact `origin/main`.

Never `reset --hard` the current dirty root before that reconciliation.

## Remote deletion order

For normal merged mission branches:
1. PR merged + evidence complete.
2. Remote branch may be auto-deleted by GitHub.
3. Local reconciler sees deleted upstream.
4. If worktree clean/inactive, remove worktree and local branch.
5. `fetch --prune`.

For legacy branches:
1. classify in dry-run;
2. process batches of <= 20;
3. verify receipt after each batch;
4. stop on any unexpected dirty/unique state.

## Recommended GitHub settings

- protect `main`;
- require relevant CI checks before merge;
- prefer squash or rebase consistently;
- enable automatic deletion of PR head branches after merge;
- do not auto-delete protected home/release refs;
- use Actions for remote branch-hygiene reports;
- use AMF/DC/local reconciler for filesystem worktree truth.

## Branch hygiene Action

GitHub Actions may classify remote state:
- merged PR head;
- closed-unmerged PR head;
- age;
- branch naming class;
- reachability/patch equivalence.

It must be read-only by default.

A cloud Action cannot prove local worktree cleanliness on Amd-PC.
Filesystem retirement therefore requires an AMF/DC/local receipt.

## Two-phase A'Space retirement

Phase A — GitHub/Cloud:
`PR/evidence -> RETIRE_CANDIDATE`

Phase B — Machine/local:
`candidate -> worktree/liveness/dirty check -> RETIRE_CONFIRMED`

Then remote/local refs are pruned.

This prevents GitHub truth from destroying uncommitted machine state.

## Batch policy for the current 281 branches

Wave size: maximum 20 branch retirements.

Priority:
1. merged worker branches;
2. merged mission branches;
3. patch-equivalent branches;
4. closed-unmerged workers with no useful delta;
5. recovery branches whose incident is closed;
6. orphans only after provenance review.

Do not start with persistent Amdkn/* homes or runtime-owned worktrees.

## Definition of Done

Branch hygiene is healthy when:
- no stale merged worker branches remain remotely;
- no abandoned clean worktrees remain locally;
- root main is clean and synchronized;
- persistent holon homes are explicitly allowlisted;
- every remaining non-main branch has a live PR, live worktree/claim, recovery reason, or archival purpose;
- branch count reflects active execution, not historical memory.
