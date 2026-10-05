# Jules Closure Swarm Incident Audit — 2026-10-05

Status: **CONTAINED**
Owner: Nardole / DISPATCH-INTERCONNECTION
Scope: Jules sessions, local scheduler, legacy publisher, GitHub effects

## Executive finding

The legacy `00_Operations/jules_swarm` control plane became an autonomous scheduler/gate/merge loop that no longer matches the A'Space GitHub Operating Model.

It was not merely a Jules worker. It:
- crawled open Issues across multiple repositories;
- auto-approved plans;
- nudged waiting sessions;
- created new Jules sessions with `AUTO_CREATE_PR` and `requirePlanApproval=false`;
- recovered Jules ChangeSets into local worktrees/branches;
- opened PRs;
- automatically merged green Jules PRs with branch deletion;
- invoked Antigravity as a second supervisory decision layer.

That authority overlaps Nardole, S2 review, S1 gate, GitHub Projects, branch lifecycle, and HostPolicy.

## Containment performed

Windows Scheduled Task:
`ASpace Jules Antigravity Closure Swarm`

Observed before containment:
- runner: `00_Operations/jules_swarm/run_tick.ps1`
- interval: every 5 minutes
- scheduled duration: 3 hours per registration
- last observed run: 2026-10-05 05:49:06 local
- last observed result: 3
- next observed run before disable: 05:54:05

Containment:
- Scheduled Task disabled;
- no `run_tick.ps1` process remained;
- Jules MCP proxy deliberately left online as transport/read interface;
- historical supervisors `ASpace Hermes Jules Supervisor`, `ASpace Jules Completion Watch`, and `ASpace Jules Fleet Supervisor 5m` were already disabled.

## Execution volume

Forensic local evidence:
- tick logs: **633**
- first tick log: `tick-20261002-063019.log`
- last tick log: `tick-20261005-054908.log`
- keeper history entries: **635**
- auto-published PRs recorded by publisher state: **34**
- Jules sources visible through proxy: **45 repositories**

Publisher activation:
`2026-10-02T18:30:34.902161+00:00`

## Current 100-session audit

Read-only Jules inspection after containment:

| State | Count | Interpretation |
|---|---:|---|
| FAILED | **85** | all 85 are duplicate sessions for `Amdkn/Agent-OS #1` |
| COMPLETED | **14** | historical outputs across Astra/Terra/Luna-related repos |
| AWAITING_USER_FEEDBACK | **1** | Life OS #109 |
| IN_PROGRESS | **0** | no active Jules execution remains |

### Failed family

All 85 FAILED sessions have the same logical target:

`Amdkn/Agent-OS #1 — [AGENT-OS][FRACTAL-HOLON] Control plane: hierarchy ≠ identity ≠ stewardship ≠ runtime`

The final keeper tick attempted yet another dispatch and received:
`400 FAILED_PRECONDITION`.

This is a retry/dedup/circuit-breaker failure, not 85 independent work items.

### Completed sessions

Current completed set:
- `16747692619086489624` — Aspace_OS_V3 #222
- `13435022830012982524` — Aspace_OS_V3 #207
- `123363717900059492` — historical 13e Docteur / Yaz-Ryan-Graham session
- `5362069408040447720` — Business-Office-3-OS #2
- `14048242369761474536` — Aspace_OS_V3 #219
- `10808731965819602480` — Life-OS-2026 #109
- `1449804890686472815` — Life-OS-2026 #105
- `16595203227135328502` — Life-OS-2026 #90
- `3437763578590245109` — The-OMK-Mobile-Back-Office #29
- `15138110105046895363` — Life-OS-2026 #93
- `12445478783326656512` — Aspace_OS_V3 #318
- `17234858273267160781` — Life-OS-2026 #88
- `7782632579374977414` — Aspace_OS_V3 #485
- `2164587241585309927` — Aspace_OS_V3 #484

Jules currently reports no attached PRs for these 14 completed sessions. Some outputs were previously recovered/published through the local publisher or provider-created draft PRs.

### Waiting session

`10438573096344858338`
- source: Life-OS-2026
- logical target: #109
- state: AWAITING_USER_FEEDBACK

A second Life #109 session is already COMPLETED, so this is also duplicate coverage and must not be automatically nudged.

## Current GitHub workload seen by the old keeper

The keeper's target repositories currently expose **20 open Issues**:
- Aspace_OS_V3: 12
- Life-OS-2026: 5
- Agent-OS: 1
- The-OMK-Mobile-Back-Office: 1
- Business-Office-3-OS: 1
- Agent-OS-Desktop: 0
- 01-OMK-Business-OS: 0
- BusinessOS: Issues disabled

The old keeper incorrectly treated “open Issue” as “Jules-executable work”.

The current set contains parent missions, architecture/fabric contracts, cross-OS migrations, objectives, canaries, authority/security work, and stateful migrations. None should be blindly dispatched wholesale by an open-Issue crawler.

## Current open PR surface

After containment:
- Aspace_OS_V3: one open PR (#556), current GitHub authority/permission work, not a legacy swarm PR.
- Life-OS-2026: 9 open draft PRs, several Jules/session-derived.
- The-OMK-Mobile-Back-Office: 2 open draft PRs.
- Business-Office-3-OS: 2 open draft PRs.
- Agent-OS: 0.
- Agent-OS-Desktop: 0.

These draft Jules outputs are **quarantine/reconciliation inputs**. They are not an auto-merge queue.

## Root causes

1. **Backlog = open Issues**
   No distinction between Project/epic/architecture and executable cell.

2. **No durable dedup key**
   Failed Agent-OS #1 was redispatched repeatedly.

3. **Failure caused refill**
   `FAILED` was treated as uncovered capacity instead of recovery state.

4. **Provider owned scheduling**
   Jules sessions were created by a local cron-like keeper rather than a GitHub/Gateway mission event.

5. **Provider output owned Git effects**
   Publisher created branches/worktrees/PRs and merged/deleted branches.

6. **Authority collapse**
   S3 execution, S2 review, S1 gate, Nardole dispatch, and Antigravity supervision were mixed in one loop.

7. **Cross-repo global crawl**
   Eight dispatch repos and 45 visible Jules sources created an unbounded discovery/authority surface.

8. **No circuit breaker**
   Repeated `FAILED_PRECONDITION` did not freeze the work key.

9. **No provider-neutral contract**
   Jules-specific session state became workflow truth.

10. **Five-minute polling loop**
    Repeated polling replaced event-driven GitHub primitives and generated 633 ticks.

## Preservation

Do not delete the legacy swarm directory or logs yet.
It is forensic evidence for:
- duplicate-session analysis;
- provider failure semantics;
- publisher branch/PR history;
- future migration tests.

The legacy launchers are local/ignored runtime files (`.git/info/exclude: 00_Operations/`) and therefore are not mutated by GitHub content APIs.

Amd-PC containment:
- original `install_task.ps1` and `run_tick.ps1` copied to
  `C:/Users/amado/Aspace_Quarantine/jules_swarm_legacy_launchers_20261005`;
- SHA-256 manifest written beside them;
- local `install_task.ps1` replaced by a fail-closed task-disabler;
- local `run_tick.ps1` replaced by a fail-closed no-op that logs and exits 64.

Original hashes:
- `install_task.ps1`: `987082BF9DF55854F36968630801E6C0CDB75C047D2B42C8304E34FBF671AB63`
- `run_tick.ps1`: `2200FD19A52FC8AB0B55B13FFD71FF841FB4FD58A828075FDDFE560BFF598BEA`

GitHub persists the governance/audit contract; Amd-PC persists the local kill-switch.

## Re-enable rule

The legacy Closure Swarm must never be re-enabled as-is.

Jules may return only through the provider-neutral contract in:
`docs/governance/JULES_PROVIDER_OPERATING_MODEL_V2.md`.


## Current workload eligibility conclusion

At audit time the legacy target set contained 20 open Issues. **Zero of those 20 are approved for blind whole-Issue Jules dispatch.**

Reason: the set mixes parent missions, architectural fabrics, migration objectives, state/release canaries, authority/security work, and broad research/build objectives.

A future Jules session may target one of those programs only after S2/Nardole decomposes it into a bounded `ExecutionCell` satisfying the provider v2 eligibility gate.

## Current source registry conclusion

The Jules proxy exposes 45 GitHub sources. This is discovery visibility only.

It must never be interpreted as:
- dispatch allowlist;
- current project list;
- authority scope;
- backlog scope.

A future `JulesExecutionPacket` authorizes exactly one repository and one bounded cell.
