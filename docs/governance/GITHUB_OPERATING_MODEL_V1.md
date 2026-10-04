# A'Space GitHub Operating Model v1

Status: proposed operating standard
Scope: Amdkn/Aspace_OS_V3 and reusable satellites
Purpose: make Git/GitHub/CI/CD/Observability fundamentals explicit inside A'Space execution

## Golden path

```
Issue / executable cell
  -> branch + isolated worktree
  -> Pull Request
  -> CI / review
  -> merge to main
  -> release candidate
  -> target-specific CD
  -> runtime observation
  -> evidence / rollback knowledge
  -> cleanup branch + worktree
```

This is the default path. Exceptions must be explicit.

## Mental model

- Git = local/distributed history, commits, branches and worktrees.
- GitHub = collaboration and governance of that history.
- CI = proves whether a proposed mutation is acceptable to integrate.
- CD = promotes an accepted mutation toward a real target/environment.
- Observability = proves what actually happened after promotion.

Do not collapse these truths:

- PR merged != deployed.
- CI green != runtime healthy.
- branch exists != work active.
- Issue open != executable task.
- worktree exists != agent alive.
- runtime online != institutional holon active.

## Seven operating reflexes

1. `main` is integrated state, not a normal development workspace.
2. Mission branches are temporary and need a closure condition.
3. A Pull Request is a mutation proposal with evidence and rollback thinking.
4. CI answers whether integration is acceptable.
5. CD answers whether/how an accepted version is promoted.
6. A release/tag names an immutable promoted version candidate.
7. GitHub primitives are typed:
   - Discussions = exploration
   - Wiki/docs = canon/explanation
   - Projects = portfolio/possibility-space
   - Milestones = convergence/release boundary
   - Issues = executable or concretely blocked cells
   - PRs = mutation + review + proof
   - Actions = deterministic verification/automation
   - Releases = promoted immutable versions

## Seven questions for every artifact

Before creating or keeping an Issue, branch, PR, Action, release, deployment or worktree, be able to answer:

1. Why does it exist?
2. Who is accountable for it?
3. Which truth does it represent?
4. What allows it to advance?
5. What closes it?
6. Where is the evidence?
7. How do we recover or roll back?

If these answers are missing, the artifact is not ready to become active execution state.

## Issue lifecycle

An open Issue means:
- executable now; or
- blocked by a concrete named dependency/event.

Exploration belongs in Discussion.
Stable doctrine belongs in docs/Wiki.
Dormant roadmap possibilities belong in Projects.

An executable Issue should name:
- observable signal;
- canonical mission / return_to;
- smallest verifiable outcome;
- accountable capability;
- evidence already available;
- authority constraints;
- PASS / FAILED / UNKNOWN continuation.

## Branch + worktree lifecycle

Normal mutation branches:
`feat/*`, `fix/*`, `docs/*`, `design/*`, `test/*`.

Worker branches:
`jules-*`, `autopublish/*`, `AUTO_CREATE_PR*` are ephemeral.

Development happens in bounded worktrees, not root `main`.

Lifecycle:
```
create branch
 -> create/use isolated worktree
 -> mutate
 -> PR
 -> CI/review
 -> merge
 -> retire remote branch
 -> verify local worktree is clean/inactive
 -> remove worktree/local branch
```

See `docs/governance/GIT_BRANCH_WORKTREE_LIFECYCLE_V4.md`.

## Pull Request contract

Every meaningful PR should explain:
- Mission / return_to
- Existing canonical state reused
- Capability / accountable owner
- Smallest mutation
- Authority / state ownership
- Test / evidence
- Failure / UNKNOWN / recovery
- Continuation / release gate

The PR is not a project plan. It is one bounded mutation proposal.

## CI law

CI may verify deterministic conditions such as:
- compilation;
- tests;
- schemas/contracts;
- lint/static analysis;
- security checks;
- build reproducibility;
- documentation integrity.

CI must not claim:
- production runtime truth;
- semantic acceptance that requires human/holon judgment;
- external effect truth that it did not observe.

## CD law

CD begins only after integration acceptance.

A product must define a target-specific ReleaseProfile before automated promotion is considered authoritative.

Generic lifecycle:
```
merged
 -> release candidate
 -> target/environment selection
 -> deploy/apply
 -> migration/config
 -> health check
 -> bounded canary
 -> promote
 -> release record
 -> rollback known
```

Do not create one giant universal deployment workflow for all A'Space worlds.

## Observability law

After promotion, runtime evidence comes from the runtime/environment itself.

Yaz/OBSERVE or the target's telemetry should be able to distinguish:
- deployed artifact/version;
- process/service health;
- functional canary result;
- stale/unknown observation;
- rollback state.

## Teaching mode

A'Space should teach GitHub at the moment each primitive is used.

Examples:

**Pull Request**
> A PR proposes a mutation of the base branch. CI may validate the proposal. Merge integrates it; deployment is a separate concern.

**Worktree**
> A worktree is another physical checkout of the same Git repository, usually attached to another branch.

**Action / check**
> A check verifies a condition. A green check does not by itself prove production/runtime health.

Teaching notices should be advisory first. Enforcement should only be enabled after the rule is stable and low-noise.

## Capability stewardship

- Clara / DESIGN-FORGE: keep PR and architecture boundaries coherent.
- Ryan / BUILD: build from bounded branches/worktrees; never normalize direct development on root main.
- Yaz / OBSERVE: distinguish CI evidence from runtime evidence.
- Graham / STATE: preserve commit -> PR -> release -> deployment -> evidence lineage.
- Nardole / DISPATCH: prevent orphan branches/worktrees and preserve return_to.
- Donna / RECOVER: handle partially completed pipelines and UNKNOWN effects.
- Rory / COHERE: reconcile contradictory projections/statuses.
- River / FLOW: compose release/deployment flows without absorbing product authority.

These are stewardship affinities, not exhaustive identity definitions.

## Maturity levels

### M0 — Advisory
- docs and templates explain the model;
- advisor Action produces notices/warnings but does not block;
- existing CI remains authoritative only for its own tested conditions.

### M1 — Guarded
After evidence that rules are stable:
- selected invariants become required checks;
- branch naming/PR contract may become enforced;
- release profiles are validated.

### M2 — Automated release governance
Only after product-specific CD is proven:
- environment protection;
- deployment approvals;
- canary/promotion/rollback automation;
- release receipts.

## Definition of healthy

A'Space GitHub is healthy when:
- `main` is an integrated trunk;
- active branches correspond to active execution;
- PRs are bounded and evidence-backed;
- CI and CD are visibly distinct;
- releases/deployments have traceable versions;
- runtime truth is not inferred from CI;
- closed work retires branches/worktrees;
- future possibilities live outside open Issue debt.
