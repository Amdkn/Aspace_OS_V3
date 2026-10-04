# GitHub Primitive Topology — A'Space V4

Status: canonical governance rule
Origin: issue overload / Zero Open Issues migration
Related: #512 #405 #317 #388

## Problem

A'Space temporarily used GitHub Issues as a universal persistence surface because the other GitHub primitives were not yet fully exploited.

That was useful for anti-amnesia, but it creates false backlog:
an idea, a canon decision, a roadmap item, a release gate and an executable cell all appear as the same object: an open Issue.

## Primitive law

### Discussions = exploration / collective cognition
Use for:
- hypotheses;
- architecture debates;
- discovery packets;
- alternative designs;
- cross-agent routing conversations;
- questions that may produce zero implementation.

A Discussion may produce:
- a Wiki/canon update;
- a Project item;
- an Issue;
- nothing.

It is not executable work by default.

### Wiki / canonical docs = durable explanation
Use for:
- architecture doctrine;
- vocabulary;
- M0/M1/M2 semantics;
- role/capability definitions;
- historical decisions;
- playbooks;
- stable maps and indexes.

Canon should not remain open merely because it may evolve.

### Projects = portfolio / possibility-space projection
Use for:
- dormant possibilities;
- capability portfolio;
- sequencing;
- priority;
- ownership/stewardship;
- status across many repos/issues;
- M0/M1/M2 projected scale;
- evidence maturity.

A Project item does not require an open Issue.

### Milestones = convergence boundary
Use for:
- release;
- certification wave;
- migration/cutover;
- bounded program outcome.

Milestones answer: what must converge together?

### Issues = executable or concretely blocked cells
Open Issue means one of:
1. executable now;
2. blocked by a named dependency;
3. waiting for a concrete external event/evidence.

If none applies, do not keep it open.

### Pull Requests = mutation + review + proof
A PR is the proposed repository effect.
It carries exact code/doc change, review and CI evidence.

### Actions = deterministic verification / automation
Use for:
- CI;
- contract validation;
- scheduled reconciliation;
- evidence generation;
- drift checks;
- closure automation where deterministic.

Actions do not decide institutional semantics.

### Releases = immutable promoted versions
Use for:
- promoted products;
- certified capability bundles;
- release notes;
- rollback references.

## Migration rule for the current open-Issue debt

For every open Issue classify:

- EXECUTE → remains open Issue.
- BLOCKED_CONCRETE → remains open Issue with dependency.
- EXPLORE → migrate to Discussion, then close Issue.
- CANON → migrate to Wiki/canonical docs, then close Issue.
- PORTFOLIO/DORMANT → migrate to Project, then close Issue.
- RELEASE_GROUP → attach to Milestone; close parent issue if it has no executable work.
- SUPERSEDED → cross-link successor and close not_planned.
- COMPLETED → attach evidence and close completed.

## Zero-Open-Issues target

Zero open Issues is allowed and desirable when no executable/blocked cell exists.

It does NOT mean:
- no roadmap;
- no research;
- no architecture;
- no possibilities.

Those live in Discussions, Wiki/docs, Projects and Milestones.

## Creation gate

Before creating any new Issue ask:

1. Is there a concrete executable effect?
2. Is there a specific acceptance criterion?
3. Is there a named owner/steward?
4. Is it actionable or blocked by a concrete dependency?

If not, prefer Discussion / Wiki / Project instead.

## Transport rule

Use ChatGPT native GitHub integration for repository-native coordination whenever available.
Do not consume DC/AMF quota to tunnel ordinary GitHub operations.

DC/AMF is reserved for machine-local effects and evidence.
