# Jules Provider Operating Model v2

Status: **proposed canonical replacement for the legacy Closure Swarm**
Scope: A'Space use of Google Jules as an execution provider

## Principle

**Jules is a runtime/provider, not a project manager, backlog scanner, gatekeeper, branch owner, or merge authority.**

Identity, authority, runtime and effect are separate:

```
Holon / Capability identity
        ↓
GitHub / mission authority
        ↓
Runtime broker
        ↓
Jules | Hermes | Codex | Antigravity | other provider
        ↓
ChangeSet / evidence
        ↓
A'Space Effect Adapter
        ↓
Draft PR
        ↓
CI
        ↓
S2 review
        ↓
S1 gate
        ↓
merge / release
```

Provider substitution must not change GitHub authority.

## What Jules may do

As an S3 execution provider, a Jules lease may:
- read one explicitly selected repository and execution packet;
- inspect the bounded Issue/sub-issue and linked evidence;
- reason, edit and test inside the leased scope;
- produce a ChangeSet, test evidence and execution receipt;
- optionally propose a branch/PR payload to the S3 GitHub Effect Adapter.

## What Jules may not do

Jules itself must not:
- crawl all open Issues;
- decide which Issue becomes executable;
- create parallel sessions merely because capacity exists;
- close Issues/Projects/Milestones;
- change Project portfolio state;
- merge PRs;
- delete branches;
- modify workflows;
- release/deploy;
- receive S1/A0 permanent credentials;
- infer authority from confidence or provider state;
- retry a failed mission by creating a new session without RecoveryPolicy.

## JulesExecutionPacket.v1

Every Jules session must be created from one typed packet:

```yaml
JulesExecutionPacket:
  mission_id:
  work_id:
  execution_cell_id:
  return_to:
  repo:
  issue_or_subissue:
  base_sha:
  capability_need:
  allowed_paths: []
  acceptance:
    tests: []
    evidence: []
  effect_class:
  reversibility:
  authority_profile: S3
  provider: jules
  provider_mode:
  dedup_key:
  retry_budget:
  deadline_or_lease:
```

The packet is produced by A'Space orchestration, not inferred from “all open Issues”.

## Eligibility gate

Before Jules is invoked, all must be true:

1. Work is an **executable cell**, not a parent Mission/Objective/Epic.
2. Exactly one repository is authoritative for the mutation.
3. Acceptance criteria are executable/testable.
4. A steward/return_to exists.
5. Base SHA is pinned.
6. Allowed mutation scope is bounded.
7. Effect is reversible or explicitly governed.
8. No unresolved human-only authority/secret/payment/legal choice exists.
9. No active session already owns the dedup key.
10. Previous failure, if any, has a classified recovery decision.

If any check fails: **do not create a Jules session**.

## Dedup and retry

Canonical dedup key:

`repo + execution_cell_id + base_sha + capability_version`

Rules:
- max one ACTIVE lease per dedup key;
- `FAILED_PRECONDITION` trips a circuit breaker immediately;
- generic retry budget starts at **0**;
- retry requires a new recovery decision/evidence;
- changing provider is a recovery action, not a duplicate session;
- completed output does not imply accepted work.

The Agent-OS #1 incident demonstrates why this is mandatory.

## Concurrency

M0 default:
- maximum **3** simultaneous Jules leases globally;
- maximum **1** per execution cell;
- no refill from raw backlog size.

Concurrency may rise only after observability proves low duplication/failure rates.

## Event-driven dispatch

No cron polling loop.

Preferred trigger:

```
GitHub webhook / Project transition
        ↓
A'Space Gateway
        ↓
Nardole eligibility + dedup
        ↓
HostPolicy
        ↓
Runtime broker
        ↓
Jules lease
```

A GitHub Project item or Issue becomes Jules-eligible only after an explicit execution transition. Merely being Open is not sufficient.

## GitHub authority

Jules never receives permanent GitHub private keys.

GitHub effects use the A'Space authority boundary:
- short-lived S3 installation token;
- narrow repo scope;
- narrow effect set;
- receipt for every mutation.

Preferred M0:
- Jules returns ChangeSet/evidence;
- A'Space S3 Effect Adapter applies the ChangeSet on a fresh branch;
- A'Space opens a **Draft PR**.

If provider-native PR creation cannot be bound to the S3 authority contract, it remains disabled.

## PR lifecycle

Provider output:
`ChangeSet + evidence`

Then:

```
S3 Effect Adapter
  → bounded branch
  → commit
  → Draft PR
  → CI
  → S2 review
  → S1 merge gate
  → merge
  → standard branch retirement
```

No publisher may call `gh pr merge` automatically.

No runtime/provider may delete branches.

## Waiting state

`AWAITING_USER_FEEDBACK` is not an invitation for generic autonomous nudging.

Classify:
- TECHNICAL_REVERSIBLE → route to S2/RuntimeBroker with typed clarification;
- AUTH/SECRET/MONEY/LEGAL/IRREVERSIBLE → human blocker;
- DUPLICATE/STale → close provider lease without creating another session.

## Failure state

`FAILED` routes to RecoveryPolicy:

```
FAILED
  ↓
classify cause
  ├ provider/transient → optional provider retry
  ├ base drift → rebase/reissue packet
  ├ contract invalid → return to S2/Clara
  ├ authority missing → HostPolicy
  ├ duplicate → close lease
  └ irreducible → Donna / DLQ
```

Failure never means “uncovered Issue → dispatch again”.

## Sources and repositories

The Jules source registry may expose many repositories for discovery.
That is **not** an execution allowlist.

Each execution packet authorizes exactly one repo.
Cross-repo missions must be decomposed into separate cells with explicit return_to.

## Existing Jules drafts

Legacy open draft PRs in Life/Mobile/Business are frozen as reconciliation inputs.

For each:
- map to current Issue/Project/Milestone truth;
- compare against current main;
- keep useful patches/evidence;
- supersede/close duplicates;
- review through S2;
- merge only through S1.

Do not mass-merge them because they are green.

## Provider-neutrality

The same ExecutionPacket / authority / recovery semantics must work for:
- Jules;
- Hermes;
- Codex;
- Antigravity;
- future runtimes.

Runtime identity is metadata, never governance authority.

## M0 canary

First future Jules use must be one deliberately selected low-risk child execution cell.

PASS requires:
- exactly one Jules session;
- no duplicate session;
- no global Issue crawl;
- one bounded ChangeSet;
- one Draft PR created by A'Space authority;
- CI result observed;
- no auto-merge;
- explicit S2/S1 continuation;
- branch retirement receipt after merge/closure.

Until that canary passes, Jules automation remains disabled.
