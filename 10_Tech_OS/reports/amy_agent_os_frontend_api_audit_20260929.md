# AMY — Agent OS Frontend / API / Runtime Presence Audit

Date: 2026-09-29
Lane: AMY / INTERFACE
Scope: Agent OS frontend and its local API surface, before Clara architecture design.

## Executive finding

Agent OS Desktop is not currently a Supabase-backed interface. The UI is a hybrid of:

1. browser-local state (`localStorage`, local storage adapters);
2. optional PocketBase adapter;
3. Vite development middleware exposed as `/api/*`;
4. local SQLite `uc.db`, filesystem reports and Python scripts behind `/api/tech-os/*`;
5. hard-coded or inferred service/agent statuses.

Therefore the current UI cannot be treated as a live projection of the Agent OS Supabase backend.

## Source state

- Parent repo: `Amdkn/Agent-OS`.
- Parent HEAD observed: `4b73326954b602134a51ed9bad147d187a9479b0`.
- Parent branch observed: `snapshot/tera-2026-09-27` (same commit as local main).
- Parent gitlink for `desktop`: `7c6dc8bb1907a583a02d2f80b6df3c410dcf56bd`.
- Actual Desktop working repo HEAD: `c0dc5d28148c9d8a33d7222bd6740b30b1005f65` on `docs/aspace-world-federation-2026-09-28`.
- Parent repo therefore sees `desktop` as modified.

This is already one concrete source of Agent OS ↔ backend snapshot drift.

## Frontend persistence

`src/App.tsx` restores and mirrors session state through:
- `agent-os.session.v3`;
- compatibility with `agent-os.session.v2`;
- `localStorage`.

The package has no `@supabase/supabase-js` dependency.

Storage code also exposes:
- local Agent OS storage;
- optional PocketBase adapter configured through browser local storage.

Conclusion: browser/session persistence and backend orchestration state are separate planes.

## API surface actually consumed

Frontend calls local paths such as:
- `/api/tech-os/workflows`;
- `/api/tech-os/execute`;
- `/api/tech-os/kernel-state`;
- `/api/tech-os/telemetry`;
- `/api/tech-os/subagents`;
- `/api/tech-os/subagents/invoke`;
- `/api/tech-os/graham-graph`;
- `/api/tech-os/graham/checkpoints`;
- `/api/tech-os/osdk/*`;
- `/api/workspace/health`;
- `/api/workspace/chat`;
- `/api/arms/*`;
- `/api/routeurs/*`.

These are implemented primarily as Vite development-server middleware in `desktop/tools/*.ts`, not as a stable versioned backend API.

### Important local backend fact

`tools/tech-os-api.ts` reads directly from:
- `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db`;
- filesystem reports;
- local Python scripts;
- local process/telemetry probes.

It does not project the live `aspace` Supabase schema.

## Runtime presence is not trustworthy yet

### Live HTTP evidence at 2026-09-29 ~00:58 EDT

- `http://127.0.0.1:5555/` -> HTTP 200.
- `/api/tech-os/telemetry` -> HTTP 200 with current CPU/RAM sample.
- `/api/workspace/health` -> HTTP 200, Hermes platform healthy.
- `/api/tech-os/kernel-state` -> HTTP 200 and reads local `uc.db`.
- `/api/tech-os/subagents` -> HTTP 200 but:
  - `totalAgents: 0`;
  - `agents: []`;
  - `leases_count: 0`.

### Why the roster is empty

The API expects:
- `10_Tech_OS/subagents/subagents_tech_os_roster.json`;
- `10_Tech_OS/scheduler/scheduled_tasks_manifest.json`.

Both paths are currently absent in V3.

### False-positive status paths

`Doctor13Kernel/index.tsx` contains static service declarations such as:
- Agent OS Web = OPERATIONAL;
- Antigravity Runtime = OPERATIONAL;
- Python workflow engine = ONLINE.

`tools/tech-os-api.ts` also assigns several companion/doctor states to `active` based on identity when roster data exists, e.g. River “Event Bus Écoute”, Rory “Local-First Vérifié”, doctors “Gouvernance Active”.

These values are descriptive defaults, not proof of a live worker.

## Amy diagnosis

The UI currently conflates at least five states:

1. declared capability exists;
2. UI app/service is reachable;
3. local process/listener is alive;
4. work/session binding exists;
5. a worker has a fresh claim/heartbeat and is actually executing.

These must not share one boolean `active` or `OPERATIONAL`.

## Interface contract Amy proposes for Clara to design around

Amy is not selecting the final backend architecture. The interface needs one typed projection, tentatively:

`RuntimePresenceProjection`

Minimum fields:
- `entity_id`;
- `entity_kind` (agent / doctor / companion / service / harness);
- `declared_capability`;
- `runtime_state`;
- `runtime_reason`;
- `source_of_truth`;
- `observed_at`;
- `expires_at` or `ttl_seconds`;
- `process_evidence`;
- `session_binding_id`;
- `work_id`;
- `claim_valid`;
- `provider`;
- `repo / branch / head_sha / pr_number`;
- `evidence_refs[]`.

Suggested runtime state vocabulary:
`UNKNOWN | OFFLINE | STARTING | LIVE | WAITING | STALE | FAILED`.

UI rule:
**no status badge is green solely because a capability exists in a registry or because a component has a static default.**

## Frontend/API convergence requirements before implementation

Clara should receive these as design inputs:

1. Replace static runtime truth with one typed presence endpoint/projection.
2. Keep browser UX state (window layout, theme, local drafts) separate from orchestration state.
3. Version the API contract consumed by Agent OS instead of making Vite middleware itself the architecture.
4. Keep localhost/process probing behind a server-side adapter.
5. Map `uc.db` and Supabase state explicitly instead of letting both silently represent “current state”.
6. Display provenance and freshness for runtime claims.
7. Define degraded behavior when Supabase, local kernel, or process observer is unavailable.
8. Never put Supabase service-role credentials into Agent OS Desktop.

## Amy handoff

Return-to: CLARA / DESIGN-FORGE after Rory backend packet is available.
Dependency: Rory must define the backend/state discrepancies and available authoritative evidence.
Amy's acceptance criterion: Clara can design a frontend contract without hard-coded presence, direct service-role access, or ambiguity between local UI state and orchestrator state.
