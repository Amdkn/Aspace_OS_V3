# Ryan Build Packet — Agent OS Unified Full-Stack

Primary owner: Ryan / BUILD-CAPABILITY
Consumer: River / FLOW
Design input: Clara Agent OS Unified Full-Stack Projection Fabric

## Mission

Build the complete substrate that makes Agent OS operationally truthful without turning River into infrastructure plumbing.

This is one continuous implementation mission. Gates are evidence checkpoints, not future-project boundaries.

Ryan owns:
- Projection Gateway service;
- versioned projection API;
- runtime observation adapters;
- WorkGraph adapter;
- Supabase sync adapter;
- Git source fingerprint adapter;
- evidence adapter;
- service config/start/recovery;
- skills/hooks/webhook/cron/runtime/CLI config required by the substrate;
- tests, receipts and rollback.

Ryan does not own long-lived workflow execution after capability publication.
## G0 — Projection Gateway

Create a production-local service distinct from Vite dev middleware.

Requirements:
- binds loopback by default;
- versioned /v1 API;
- health endpoint;
- config file/runtime profile;
- install/start/stop/restart instructions;
- service logs/receipts;
- no browser-exposed service-role secrets.

Initial reads:
runtime-presence, work, mission, source, evidence, sync-health.

Initial UI writes:
intent, approval, bounded user-action only.

Acceptance:
Agent OS Desktop can run without production semantics depending on Vite middleware.
## G1 — Runtime observation + presence

Implement RuntimeObservation collectors for at least:
process/listener, provider/harness health, session reference, heartbeat/last output where available.

Derive RuntimePresenceProjection via TTL and PRESENCE_STATE_MACHINE.json.

Remove hard-coded ONLINE/active status from the migrated Amy surfaces.

Acceptance:
registry-only agent never appears LIVE.
LIVE/idle and LIVE/owning are distinct.
Expired observation transitions to STALE.
## G2 — WorkGraph ownership

Read uc.db claim/lease/session binding/event state through an adapter.

Join ownership evidence with runtime presence without mutating either source.

Acceptance:
runtime LIVE + no claim => idle.
claim/lease conflict => ownership CONFLICT.
uc.db unavailable => ownership UNKNOWN, dangerous mutation held.
## G3 — Supabase sync bridge

Implement append/outbox synchronization from local WorkGraph/evidence into Supabase durable projections.

Rules:
- idempotency key per event;
- no generic last-write-wins;
- cloud rows cannot steal local execution ownership;
- durable retry/backoff;
- offline local outbox;
- readback/postcondition receipt.

Cloud-to-local ingress remains bounded to intent/approval/event envelopes that pass policy/dispatch before local WorkGraph mutation.

Acceptance:
replay produces zero duplicate projection events.
Supabase outage does not stop local execution.
## G4 — Source fingerprint

Implement SourceFingerprint for Agent OS and nested Desktop repository.

Capture:
parent branch/HEAD/dirty;
committed gitlink;
observed nested HEAD/branch/dirty;
worktree;
active PR when discoverable.

Acceptance:
parent clean + nested HEAD drift => SOURCE_STALE.
Current Desktop HEAD mismatch is visible in Agent OS UI projection.
## G5 — Reconciliation

Implement Rory-compatible contradiction classification and ReconciliationReceipt.

At minimum detect:
LOCAL_NEWER
CLOUD_NEWER_BUT_NONAUTHORITATIVE
OWNERSHIP_CONFLICT
STALE_BINDING
SOURCE_DRIFT
MISSING_RUNTIME_EVIDENCE
DUPLICATE_EVENT
UNKNOWN
CONSISTENT

Do not automatically repair UNKNOWN.

Acceptance:
every divergence has evidence refs and an explicit route/decision.
## G6 — Amy migration

Replace hard-coded/identity-derived runtime badges in the selected Agent OS surfaces with Projection Gateway data.

UI must show:
runtime state;
ownership separately;
sync degradation;
source stale/dirty;
observed time/freshness;
reason/evidence drill-down.

Do not rewrite the whole Desktop.
Migrate the surfaces that currently lie about presence first.

Acceptance:
UI cannot manufacture LIVE locally.
## G7 — Realtime + reconnect

Expose local projection updates by SSE or WebSocket.
Use Supabase Realtime only as acceleration/notification where useful.

On reconnect:
1. reconnect event channel;
2. refetch authoritative projection snapshot;
3. reconcile missed changes.

Acceptance:
drop the event connection, mutate backend state, reconnect, and prove UI heals without replay assumptions.
## G8 — End-to-end release canary

Use one real work_id.

Trace:
Amy Mission view
-> WorkGraph claim/lease
-> fresh runtime observation
-> Supabase durable projection
-> GitHub issue/PR/source state
-> Graham evidence refs
-> Rory reconciliation
-> Amy refreshed projection.

Then test:
Supabase offline;
Projection Gateway restart;
runtime process dies;
nested Desktop HEAD moves;
duplicate sync replay.

Mission closes only when the 12 Clara end-to-end acceptance conditions pass.

## Publication

When complete, publish a CapabilityReleaseReceipt for the Agent OS Projection Fabric.

River must be able to consume the released capabilities without reading Ryan's ChatGPT session or manually reproducing runtime/config setup.
