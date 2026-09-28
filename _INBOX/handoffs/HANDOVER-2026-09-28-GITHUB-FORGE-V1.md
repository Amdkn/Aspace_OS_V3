# HANDOVER - 2026-09-28 - GitHub Forge v1

Lane: Ryan -> Bill -> Clara -> Nardole
Repo: Amdkn/Aspace_OS_V3
Branch: feat/github-forge-contract-v1-2026-09-28

## Objective
Make GitHub an executable shared software-factory surface without creating a new ontology or duplicate Issues/Projects.

## Real-state inspection before mutation
- main clean at eb9fe8c1.
- open PRs: 0.
- open Issues: #122-#129, all existing Bill discovery work.
- Projects enabled, but current gh token cannot read Projects v2 because read:project is missing; no Project mutation performed.
- Discussions disabled; Wiki enabled.
- Security: secret scanning + push protection enabled; Dependabot security updates disabled.
- main branch has no protection.
- only pre-existing workflow: OKF; current main run failed because OKF frontmatter ratchet regressed 30 -> 32.

## Changes in this branch
- Forge Signal issue form.
- Forge PR contract template.
- executable Forge Contract workflow, also reusable through workflow_call.
- Python validator + unit tests.
- repair of the two 2026-09-28 OKF additions responsible for the frontmatter regression.
- existing Bill Issues #122-#129 are reused as Discovery rather than duplicated.

## Contract
Signal -> Discovery (Bill) -> Design/Compile (Clara) -> Build (Ryan) -> Test -> Review -> Ship/Dispatch (Nardole) -> Evidence.

## Truth constraints
No Linear state was changed. No Supabase/GWS/Jev/LiDAR contract was mutated. No false In Progress state was created.
