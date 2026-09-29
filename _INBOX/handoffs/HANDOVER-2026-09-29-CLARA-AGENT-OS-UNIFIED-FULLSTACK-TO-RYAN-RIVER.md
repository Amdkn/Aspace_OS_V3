# HANDOVER — Clara Agent OS Unified Full-Stack → Ryan / River

Date: 2026-09-29
Parent evidence: GitHub #211
Primary implementation owner: Ryan
Parallel FLOW owner: River

## Inputs consumed

- Amy frontend/API audit commit c2091d71
- Rory Supabase/persistence audit commit 8e988da7
- Clara predesign convergence commit 05f0fd38

Do not re-audit from scratch.

## Final architecture

Agent OS is a local-first projection fabric over:
UX state,
runtime evidence,
WorkGraph/uc.db execution state,
Supabase durable coordination,
Git/GitHub source state,
Graham evidence/provenance.

No fake universal SSOT.

Amy consumes only versioned projections from a local Projection Gateway.
## Durable artifacts

- 10_Tech_OS/agent_os_fullstack/DESIGN_CONTRACT.md
- 10_Tech_OS/agent_os_fullstack/FACTORY_BLUEPRINT.json
- 10_Tech_OS/agent_os_fullstack/contracts/AGENT_OS_PROJECTIONS.schema.json
- 10_Tech_OS/agent_os_fullstack/contracts/PRESENCE_STATE_MACHINE.json
- 10_Tech_OS/agent_os_fullstack/implementation/RYAN_BUILD_PACKET.md
- 10_Tech_OS/agent_os_fullstack/implementation/RIVER_FLOW_PACKET.md

## Ryan

Ryan builds continuously G0 -> G8:
Projection Gateway,
RuntimeObservation,
WorkGraph ownership adapter,
Supabase outbox/sync,
nested Git fingerprint,
Rory reconciliation API,
Amy migration,
realtime reconnect,
end-to-end canary.

Gates are evidence checkpoints, not stopping points.

Ryan also owns the supporting skills/hooks/runtime configs/CLI profiles/service config.
## River

River starts consuming capabilities as soon as G1/G3 are published.

River runs:
observation normalization,
local->cloud sync,
cloud ingress after policy/dispatch,
projection invalidation,
retry/backpressure,
safe reconciliation actions.

River does not install/configure runtimes, secrets, adapters or toolchains.
Missing plumbing returns as CapabilityNeed to Ryan.

## Non-negotiable acceptance

- no hard-coded LIVE;
- LIVE != owning;
- Supabase outage does not stop local execution;
- replay does not duplicate cloud projection;
- cloud stale state cannot overwrite local execution truth;
- nested repo drift is visible;
- no service-role in browser;
- realtime reconnect heals via snapshot;
- one work_id traces UI -> WorkGraph -> runtime -> Supabase -> GitHub -> evidence;
- Projection Gateway restart loses no execution truth;
- Vite middleware is not production contract;
- River can operate after Ryan exits.

Next owner: Ryan begins G0 immediately. River may begin FLOW integration when Ryan publishes G1/G3 capabilities.
