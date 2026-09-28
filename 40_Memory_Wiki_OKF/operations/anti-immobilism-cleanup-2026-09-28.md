---
type: Operations memory
title: Anti-immobilism cleanup — truthful execution state
description: Operational memory for the anti-immobilism cleanup, truthful execution reconciliation, worktree hygiene, and evidence-first delivery rules.
date: 2026-09-28
tags: [aspace, anti-immobilism, workgraph, linear, orca, supabase, ipbd, git]
generated: { by: chatgpt-github-forge, at: 2026-09-28T12:55:00-04:00 }
okf_version: "0.2"
confidence: machine-verified
---

# Anti-immobilism cleanup — 2026-09-28

## What failed

A'Space had accumulated rules that were locally sensible but globally paralysing:

- Life/Business could be frozen by unrelated Kernel debt.
- ambiguity forced STOP instead of a reversible assumption.
- every IPBD was treated as if it needed SDD→ADR→PRD→TDD.
- Distillation/OKF could become a pre-execution toll.
- a canceled blocker could freeze descendants forever.
- only specially tagged PRD issues were dispatchable.
- one Companion lane was hard-coded as doctrine rather than safe runtime default.
- Linear could remain `In Progress` with no claim, binding or worker.
- live IPBD/Supabase code existed only in a stale worktree.
- Orca identities stayed 20+ commits behind `main`.
- local/remote branches mixed active work, merged residue and historical closed PRs.

## Permanent correction

### Capture first

Capture/IPBD ingress must never depend on session life, network availability, Distillation or long-memory promotion.

### Risk-proportional gates

Read, diagnose, simulate, test and make bounded reversible edits without unrelated gates.
Escalate only for irreversible, destructive, safety-sensitive or credential-blocked decisions.

### Smallest sufficient contract

Artifact depth follows risk.
Do not force every intention through every document type.

### Truth is typed

- filesystem: artifact reality
- GitHub: versioned history
- Supabase IPBD/WorkGraph: shared machine state
- Linear: human governance
- OKF: certified long memory
- `uc.db`: local sovereign projection/cache

### Status truth

`In Progress` requires:
- unexpired claim
- active binding
- fresh executing worker

Anything else is Backlog/Waiting/Review/etc., not execution.

### Never retroactively fake WorkGraph success

If external work completed without the required pre-execution prediction:
- preserve the external evidence.
- mark governance failure honestly.
- never fabricate an earlier prediction.

### Identity worktrees must not rot

Persistent Doctor/Companion worktrees follow `origin/main` when idle.
Dirty worktrees are never auto-reset.
Use `scripts/sync_orca_identity_worktrees.py`.

## Verified cleanup outcome

- PRs #178–#181 merged.
- 28/28 targeted Kernel tests passed.
- 3/3 IPBD local-first tests passed.
- 13 persistent identity worktrees reconciled clean to current main.
- broken preparation/fish worktrees removed.
- 25 false Linear In Progress states reset to Backlog.
- final Linear In Progress count: 0.
- WorkGraph: 3 governance-failed externally completed rows; 6 legitimate waiting rows.
- Supabase mutable-search-path and unindexed-FK advisor findings cleared.
- IPBD migration filenames aligned to remote migration history.
- local branches reduced to main + 13 identity branches.
- 3 local-only unique branches preserved as archive tags before deletion.
- 20 remote branches of merged PRs deleted.
- 144 remote branches of closed-unmerged PRs intentionally quarantined.

## Residuals that are intentional

- RLS-without-policy INFO remains on private `aspace` tables because anon/authenticated have no table privileges.
- new indexes may report unused until meaningful workload exists.
- 144 closed-unmerged PR branches remain historical quarantine.
- Hermes automatic dispatcher remains disabled until Bot-Mode is re-certified against truthful claim/binding rules.

## Reuse rule

If a future agent tries to “fix” the system by adding another global gate, another universal SSOT, another mandatory documentation cascade, or another fake In Progress state, treat that as a regression.

The direction is:

**Capture → smallest sufficient contract → reversible bounded execution → evidence → outcome → distill durable learning after proof.**
