# A'Space GitHub V4 — Control Plane Setup

Date: 2026-10-05  
Status: CANONICAL SETUP PROPOSAL — repository structure and target operating model; live GitHub App permission reconciliation remains owned by the separate Work session / #555.  
Scope: `Amdkn/Aspace_OS_V3` as the engineering control plane for A'Space V4.  
Related: `GITHUB_PRIMITIVE_TOPOLOGY_V4.md`, `GITHUB_OPERATING_MODEL_V1.md`, `GIT_BRANCH_WORKTREE_LIFECYCLE_V4.md`, `ASPACE_GATEWAY_NATIVE_GITHUB_V0.md`, `ASPACE_GITHUB_APP_CAPACITY_AND_PROMOTION_V1.md`, #542, #555, #557.

## 0. Constitutional boundary

GitHub is the **engineering control plane** of A'Space V4.

It is **not**:
- the institutional brain;
- the unique memory;
- the holon identity substrate;
- the runtime;
- the universal scheduler;
- the only source of truth for Life or Business effects.

A'Space V4 must preserve the 10D / fractal model:

```text
A0 / S1 / S2 / S3 institutional holons
            │
            ├── GitHub = engineering control plane
            ├── Linear = institutional governance projection
            ├── GWS = Life/Business effects and collaboration
            ├── WorkGraph = execution continuity / receipts
            ├── Temporal Truth = historical/current interpretation
            └── Agent OS / CubeFarm = human/operational projections
```

GitHub coordinates engineering effects while the institutional identity, authority and mission lineage remain portable across runtimes and surfaces.

## 1. Current observed baseline

Observed through the GitHub API on 2026-10-05:

| Surface | Observed state | V4 reading |
|---|---|---|
| Repository | `Amdkn/Aspace_OS_V3` | current canonical engineering repo |
| Visibility | **public** | explicit policy decision still required; do not silently change |
| Default branch | `main` | canonical integrated trunk |
| Issues | enabled | executable / concretely blocked cells only |
| Projects | enabled | portfolio / possibility-space |
| Wiki | enabled | human-readable canon mirror |
| Discussions | enabled | exploration / RFC / research |
| Releases | available | promoted immutable version records |
| Head branch cleanup | `delete_branch_on_merge=true` | aligned with V4 branch lifecycle |
| Merge modes | squash + merge commit + rebase all allowed | policy not yet converged to one preferred path |
| Auto-merge | disabled | keep disabled until S1/review gates are proven |
| Update branch | disabled | acceptable; no implicit branch rewriting |
| Rulesets | **none observed** | major governance gap; target M1 after advisory gates stabilize |
| Custom GitHub agents | 1 observed: `nardole-dispatch.agent.md` | mesh is partial, not empty |
| Workflows | DC Foundation, Forge, GitHub Operating Model, Kernel Continuity, Native GitHub Control Plane, OKF | deterministic substrate already exists |

This snapshot is an observation, not a permanent truth. Re-observe before applying settings.

## 2. Eight-plane setup

### Plane A — Primitive topology

Canonical rule:

| GitHub primitive | A'Space V4 function |
|---|---|
| **Discussion** | exploration, hypotheses, research, architecture alternatives |
| **Wiki / docs** | stable doctrine, vocabulary, playbooks, maps |
| **Project** | portfolio, possibility-space, sequencing, stewardship, maturity |
| **Milestone** | bounded convergence / certification / cutover |
| **Issue** | executable cell or concretely blocked cell |
| **Pull Request** | exact mutation + review + evidence |
| **Action / Check** | deterministic verification / bridge |
| **Release** | immutable promoted version + rollback reference |
| **Agent** | GitHub-native embodiment / adapter, never institutional identity |
| **GitHub App / webhook** | authority + event transport boundary |

No primitive substitutes for all others.

### Plane B — Portfolio topology

Keep portfolio state out of Issue debt.

Current canonical portfolios:
- **Project #8 — Universal Constructor / Fractal Composition**: possibility-space, M0/M1/M2 projection, capability composition.
- **Project #9 — Foundation convergence**: cross-program foundation state.
- **Project #10 — Agent OS Capability & Harness Control Plane**: provider/runtime/authority/reconciliation surfaces referenced by #560–#562.

Project items may exist without open Issues.

An Issue opens only when the item has:
1. a concrete effect;
2. observable acceptance;
3. named accountable capability;
4. executable or concretely blocked state.

### Plane C — Authority topology

Five GitHub Apps are the **technical authority envelopes**:

| App | Responsibility envelope |
|---|---|
| **A'Space Gateway** | ingress, observation, transport, webhook delivery |
| **A'Space A0 Orchestrator** | user/A0 orchestration boundary and user-scope operations |
| **A'Space S1 Gatekeeper** | review, checks, release/promotion gate |
| **A'Space S2 Managers** | planning, delegation, bounded management mutations |
| **A'Space S3 Workers** | code/branch/PR/evidence mutations |

Important:
- Apps are **not holons**.
- rank is **not cognitive limitation**.
- permissions are ceilings, not mandatory token grants.
- permanent authority, temporary promotion, installation scope and token scope are separate.
- user-owned Projects V2 are a distinct authority plane from repository/classic Projects.

The live permission reconciliation currently performed in the separate Work branch remains authoritative for actual installed permissions. This setup document must not duplicate or race that work.

### Plane D — Source-control topology

```text
main
 ├─ persistent approved Home refs: Amdkn/<Holon>
 └─ temporary Mission refs:
      feat/*
      fix/*
      docs/*
      design/*
      test/*
```

Laws:
- root `main` = integration mirror, not development workspace;
- mission branch = bounded mutation only;
- worker/recovery branches are ephemeral/TTL-bound;
- branch existence != active work;
- worktree existence != live holon;
- merge does not prove deployment;
- retirement requires GitHub + filesystem evidence.

Normal lifecycle:

`Issue/Cell → branch/worktree → PR → CI/review → merge → evidence → retire branch → retire worktree`

### Plane E — Agent/runtime topology

Institutional holon identity stays provider-neutral.

```text
Executable GitHub cell
        │
        ▼
Capability / authority / effect contract
        │
        ▼
Gateway + Nardole + HostPolicy
        │
        ├── GitHub-native agent
        ├── Codex
        ├── Claude
        ├── Hermes
        ├── Jules
        ├── Antigravity
        └── future runtime
        │
        ▼
ChangeSet / evidence / PR / check / receipt
```

The Issue states **what capability and effect are needed**, not which provider “owns” the work.

Current native agent surface is partial: only Nardole is observed in `.github/agents/`. Additional agents should be thin projections over existing A'Space contracts, not copied constitutions.

### Plane F — Verification and release topology

Current workflows are useful substrate, but V4 must keep four truths separate:

```text
PR mutation
   ↓
CI / deterministic checks
   ↓
S2 semantic review
   ↓
S1 promotion gate
   ↓
merge
   ↓
target-specific CD / effect
   ↓
runtime observation
   ↓
release/evidence/rollback
```

Rules:
- green CI != runtime truth;
- merged PR != deployed effect;
- runtime online != holon active;
- release records promoted immutable state, not raw branch state.

### Plane G — Evidence / temporal truth / recovery

Every engineering effect should preserve:
- mission_id / work_id / cell_id;
- correlation_id;
- capability/version;
- authority/policy/fencing;
- branch/commit/PR/release refs;
- evidence and provenance;
- effect identity;
- `return_to`;
- explicit `UNKNOWN` when truth cannot be established.

Graham/Temporal Truth records accepted interpretation by bounded authority.
Donna/Recovery handles UNKNOWN/reconciliation.
GitHub does not coerce ambiguity into SUCCESS.

### Plane H — 10D Directory Consciousness / War Room

Before major architecture or product brainstorming, compile a portfolio map rather than reading repositories from scratch.

For each repository/capability track:
- Tech/Life/Business purpose and beneficiaries;
- current / proposed / verified capabilities;
- M0/M1/M2 intrinsic and projected scale;
- relations such as `COMPOSES_WITH / EMBODIES / EXTENDS / VALIDATES / OBSERVES / CONTROLS`;
- interfaces, dependencies and open executable cells;
- provenance, freshness and evidence maturity.

This powers the 10D War Room and prevents local implementation gates from amputating the whole objective.

## 3. Labels as coordinates, not ontology

Use labels to make executable state queryable without encoding the whole architecture into labels.

Recommended families:
- `needs:<holon/capability>`
- `authority:a0|s1|s2|s3`
- `runtime:<provider>`
- `state:canary|blocked|recovery|unknown`
- `spec:<domain>`
- `project:<program>`

Provider labels are routing hints, never institutional identity.

Avoid labels that duplicate Project fields or permanently encode temporary runtime assignment.

## 4. Main-branch governance target

### M0 — Advisory / current
- docs/templates explain the model;
- workflows report drift and contract failures;
- no new blocking ruleset is introduced blindly.

### M1 — Guarded / next
After the current checks are proven low-noise, create a **main ruleset** with:
- pull request required;
- branch deletion denied for `main`;
- force-push denied;
- conversations resolved before merge;
- required review/gate appropriate to S1 policy;
- one stable aggregate required check rather than path-filtered checks that may not run;
- bypass only through explicitly governed authority.

Do **not** make a path-filtered workflow required until an always-running aggregate gate exists.

### M2 — Automated release governance
Only after target-specific release profiles are proven:
- environments;
- deployment protection;
- canary promotion;
- rollback automation;
- release receipt.

## 5. Merge strategy target

Current repo allows squash, merge-commit and rebase.

For agent-heavy bounded mission branches, the preferred default should be **squash merge** because it:
- keeps one accepted mutation per PR;
- simplifies branch retirement;
- reduces worker-commit noise;
- keeps PR/evidence as the semantic review unit.

Do not disable the other methods until historical/release workflows are checked for dependency on merge commits or rebased ancestry.

## 6. Security and visibility decision gate

Observed today:
- repository visibility = **public**;
- MIT license;
- forking allowed.

This is a constitutional/publication decision, not a cleanup toggle.

Before V4 is considered “securely set up”, explicitly decide:
- which architecture/code is intentionally public;
- what belongs in private satellites or private data planes;
- whether forks should remain allowed;
- what secret/material must never enter Git history;
- whether public issue/discussion surfaces are acceptable for operational metadata.

No automatic visibility change is authorized by this document.

## 7. Setup ownership split

To avoid two ChatGPT branches racing the same GitHub state:

| Scope | Owner now |
|---|---|
| 5 GitHub Apps — actual installed permissions and second-factor interactive reconcile | **separate Work branch / #555** |
| Permission compiler and authority profiles | #557 / main |
| GitHub V4 topology and setup index | **this PR/document** |
| Gateway runtime/event federation | #542 / #544–#546 |
| Jules provider-neutral canary | #562 |
| branch/worktree filesystem retirement | AMF/DC local evidence path |
| portfolio / 10D capability map | Projects + War Room / Universal Constructor |

## 8. Definition of a clean GitHub V4 setup

A'Space GitHub V4 is structurally healthy when:

1. each GitHub primitive has one clear semantic role;
2. future possibilities do not inflate open-Issue debt;
3. main is protected and remains integrated truth;
4. active branches/worktrees correspond to live execution;
5. the five Apps have verified, scoped authority envelopes;
6. providers consume a common task/evidence contract;
7. checks validate only what they actually observe;
8. merge, deploy, runtime and external effect remain distinguishable;
9. UNKNOWN routes to reconciliation instead of blind retry;
10. releases carry immutable promotion/rollback references;
11. the 10D portfolio/capability map can be loaded before architectural brainstorming;
12. GitHub reduces A0 babysitting rather than becoming a new bureaucracy.

## 9. Immediate next gates — no new program

Do not create a new mega-epic for this setup.

The next concrete gates are already present:
- **#555** — finish actual GitHub App authority reconciliation;
- **#562** — one bounded provider-neutral Jules canary;
- **#542 / #544–#546** — complete Gateway native/event/runtime federation;
- **main ruleset** — only after an always-running aggregate gate exists and advisory signals are stable;
- **visibility/publication decision** — explicit Founder decision, not inferred.

Everything else belongs in Project / Discussion / docs until it becomes executable.
