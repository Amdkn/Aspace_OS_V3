# ADR-RICK — Nine Companion Fractal Capability Mesh

**Date:** 2026-09-28  
**Status:** Accepted  
**Supersedes:** ADR-RICK-SIX-PARALLEL-SESSIONS-2026-09-28  
**Gatekeeper:** Rick / S1

## Decision

A'Space parallel execution is organized around the **nine Companions**, one persistent peer lane per specialty, managed by three Doctors and supervised cross-Core by Rick.

### Doctor13 / Kernel Core
- **Ryan — BUILD**: implementation, integration, Forge runtime, Actions, adapters, executable construction.
- **Yaz — OBSERVE**: observability, LiDAR, behavioral evidence, telemetry, validation, drift.
- **Graham — STATE**: Supabase, IPBD, WorkGraph, evidence, replay, shared machine state.

### Doctor11 / Life Core
- **Amy — INTERFACE**: human/agent interfaces, Herdr, harness exposure, Jev/System-One interface contract.
- **Rory — PERSISTENCE**: Life OS 2026 continuity, Linear Life Space, durable Life structures/projections.
- **River — FLOW**: Google Workspace workflows, effects, automation, Business-flow execution from Life Core.

### Doctor12 / Buzz Core
- **Bill — RESEARCH**: discovery, external evidence, user/customer/problem research, opportunity finding.
- **Clara — DESIGN / FORGE**: compile requirements into Forge designs, contracts, interfaces, acceptance, construction specs.
- **Nardole — DISPATCH / INTERCONNECTION**: route needs to specialists, wire capabilities, delivery/interconnection, cross-surface dispatch.

### S1
- **Rick — GATEKEEPER / ROUTER**: cross-Core conflict, priority, constitutional constraints, dependency routing and convergence.

## Fractal capability law

A Companion's specialty is a **shared capability service**, not an exclusive territory.

Examples:
- Amy can expose Jev to any Core.
- Ryan can build a Clara design for any Core.
- Yaz can observe any harness or workflow.
- Graham can persist evidence for any lane.
- Bill can research for Kernel/Life/Business.
- Nardole can dispatch interconnections across all three Doctors.

Stewardship = default accountability. It never means other agents cannot consume the capability.

## Forge recursion

Capabilities themselves pass through the same factory:

`Need → Bill Research → Clara Design/Forge → Ryan Build → Yaz Observe → Graham State/Evidence → Nardole Dispatch → consuming lane`

The sequence is **not mandatory when unnecessary**; use the smallest sufficient subset. Rick intervenes only for cross-Core arbitration or constitutional risk.

Example Jev:
- River's Wave-1 commit is provenance/canary evidence.
- Amy becomes interface steward for Jev exposure to Life/Core consumers.
- Clara compiles reusable Jev Forge contracts.
- Ryan builds adapters/integration.
- Yaz observes/calibrates behavior.
- Graham persists evidence/state.
- Nardole dispatches the capability to River or other consumers.
- deterministic host retains authority.

## GitHub communication bus

### Discussions = divergence / request discovery
Use when:
- the need is still ambiguous;
- research or design alternatives are open;
- multiple specialists may be relevant;
- cross-Core convergence is required.

Title convention:
`[NEED:<SPECIALIST>] <problem/outcome>`
or `[CROSS-CORE] <problem/outcome>`.

### Issues = executable contract
Create/convert when outcome, owner and acceptance are bounded.

Routing labels:
- `needs:ryan`
- `needs:yaz`
- `needs:graham`
- `needs:amy`
- `needs:rory`
- `needs:river`
- `needs:bill`
- `needs:clara`
- `needs:nardole`
- `route:rick` only for cross-Core arbitration
- `handoff`
- `evidence`

### PR = implementation proposal
Must reference the executable Issue and expected evidence.

### Action = deterministic middleware
Automate routing, validation, evidence checks and promotion, not architectural authority.

## Worktree isolation

Each persistent Companion session writes in its own worktree/branch:
`C:/Users/amado/orca/workspaces/ASpace_OS_V3/<Identity>`
→ `Amdkn/<Identity>`.

The shared root `C:/Users/amado/ASpace_OS_V3` is not a nine-session scratchpad.

A session may read shared root but must not mix its uncommitted work with another lane.

## Handoff message contract

Every inter-agent request contains:
- From
- To / requested specialty
- Originating IPBD or Issue
- Need / outcome
- Why this specialist
- Inputs/evidence
- Acceptance
- Reversible boundary
- Blocking? yes/no
- Response/handoff target

## Status truth

No Linear/GitHub Project item is "In Progress" merely because another agent needs it.
Execution state still requires claim + binding + observed worker where the WorkGraph contract applies.

## Success

The nine specialists can discover each other, request capabilities, route needs and converge through durable GitHub messages without A0 manually relaying every dependency.
