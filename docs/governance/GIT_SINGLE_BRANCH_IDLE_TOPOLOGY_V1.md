# A'Space Single-Branch Idle Topology

Status: canonical amendment
Date: 2026-10-05

## Core law

A holon identity is **not** a Git branch.

Persistent identity is carried by:
- worktree path / workspace identity;
- embodiment / registry metadata;
- capability and authority contracts;
- durable state/evidence.

A branch exists only for a bounded mutation.

## Idle topology

When no mutation is active:

```
main
├── root integration checkout         -> main
├── Amy home worktree                 -> detached at origin/main
├── Bill home worktree                -> detached at origin/main
├── Clara home worktree               -> detached at origin/main
├── Doctor11 home worktree            -> detached at origin/main
├── Doctor12 home worktree            -> detached at origin/main
├── Doctor13 home worktree            -> detached at origin/main
├── Graham home worktree              -> detached at origin/main
├── Nardole home worktree             -> detached at origin/main
├── Rick home worktree                -> detached at origin/main
├── River home worktree               -> detached at origin/main
├── Rory home worktree                -> detached at origin/main
├── Ryan home worktree                -> detached at origin/main
└── Yaz home worktree                 -> detached at origin/main
```

The number of persistent branches at idle should therefore be **one: `main`**.

## Mission activation

When a holon must mutate repository state:

```
detached home at origin/main
  -> fetch
  -> create bounded mission branch
  -> mutate/test
  -> PR
  -> CI/review
  -> merge or archive
  -> detach home back to origin/main
  -> delete mission branch
```

Recommended branch names:
- `feat/<mission>`
- `fix/<mission>`
- `docs/<mission>`
- `design/<mission>`
- `test/<mission>`

Do not create `Amdkn/<Holon>` branches merely to represent identity.

## Detached worktree semantics

A detached home worktree is healthy when:
- its HEAD equals the canonical integration commit expected for idle state;
- it is clean;
- no mission branch is required;
- its workspace/holon identity is known from path/registry, not HEAD branch name.

Detached does **not** mean orphaned when the worktree is an explicitly registered home.

## Mission closure

A mission branch closes by one of:
- merged;
- superseded;
- archived with evidence;
- abandoned after proof that no unique useful state remains.

After closure:
1. preserve unique state if needed;
2. detach the home worktree to current `origin/main`;
3. delete local branch;
4. delete remote branch;
5. fetch/prune.

## Historical branch references

Evidence snapshots may continue to contain historical values such as:
- `Amdkn/Graham`
- `Amdkn/Yaz`
- old Ryan mission branches

These are provenance facts, not live topology requirements.

## Why this is better

This removes:
- branch-per-agent identity coupling;
- permanent divergence between homes;
- fake active-work signals;
- repetitive home fast-forward maintenance;
- branch-count inflation.

It preserves:
- persistent workspaces;
- institutional identities;
- isolated mission execution;
- recovery/archive history through tags;
- clean GitHub topology.

## Current certified state — 2026-10-05

Verified:
- 14 worktrees;
- 1 local branch: `main`;
- 1 actual remote branch: `main`;
- root main clean and aligned with origin/main;
- idle homes detached from origin/main;
- prior unique Graham history preserved under `archive/graham-home-pre-detach-2026-10-05`;
- prior Ryan mission state preserved under `archive/ryan-discover-ai-m0-m7-2026-10-05`.

This is the target steady-state topology.
