# Agent OS Unified Full-Stack Projection Fabric — Clara Design v1

Date: 2026-09-29
Input: Amy frontend/API audit + Rory Supabase/persistence audit + Clara predesign packet #211
Primary BUILD owner: Ryan
FLOW consumer/operator: River

## Decision

Do not "connect React to Supabase".

Agent OS becomes a local-first projection fabric over several legitimate truth planes:
UX state, runtime evidence, WorkGraph/uc.db execution state, Supabase durable coordination, Git/GitHub source state and evidence/provenance.

No single plane becomes a fake universal SSOT.
The architecture makes divergence explicit, typed and reconcilable.

## Authority matrix

- UX/window/session preferences: Agent OS local UI state.
- Runtime liveness: fresh local RuntimeObservation + TTL.
- Work ownership/execution: WorkGraph/uc.db claim + lease + binding.
- Durable shared coordination/history: Supabase `aspace` projection.
- Source/version truth: Git/GitHub including nested repository HEADs.
- Evidence/provenance: durable receipts/artifact refs under Graham.
- UI presentation: Amy; never an authority source.
## Component architecture

Amy React Desktop
  -> Agent OS Projection Gateway (local service, versioned API)
      -> Runtime Evidence Adapter (Yaz observations / AMF)
      -> WorkGraph Adapter (uc.db)
      -> Supabase Sync Adapter (service-side credentials only)
      -> Git Source Fingerprint Adapter
      -> Evidence Adapter (Graham receipts)
      -> Reconciliation Engine (Rory rules)
      -> Projection Cache + Event Stream

River consumes published capabilities behind this gateway; River does not configure runtimes or credentials.
Ryan builds/version-controls adapters, skills, hooks, runtime profiles, CLI profiles, webhooks and service configuration.

Vite middleware may remain a development transport only. The durable API contract belongs to the Projection Gateway.

## Public read models

The UI consumes versioned projections, not raw storage tables:

- RuntimePresenceProjection
- WorkProjection
- SourceProjection
- EvidenceProjection
- SyncHealthProjection
- MissionProjection

Every projection must expose provenance, observed_at, freshness, evidence refs and degradation reasons.
## Runtime presence

Presence is derived; it is never written directly by Amy.

Inputs:
RuntimeObservation
+ session binding
+ claim/lease
+ recent execution event
+ provider/harness health
= RuntimePresenceProjection

State vocabulary:
UNKNOWN | OFFLINE | STARTING | LIVE | WAITING | STALE | FAILED

Ownership is separate:
LIVE does not imply owning work.
Owning work requires a fresh valid claim/lease/binding.

TTL is evidence-type specific and encoded with the observation.
Expired evidence cannot sustain LIVE.

Examples:
- process alive + provider healthy + valid fresh claim/binding => LIVE / owning.
- process alive + no work => LIVE / idle.
- registry exists but no fresh runtime evidence => UNKNOWN or OFFLINE.
- Supabase active row but local runtime absent => OFFLINE/FAILED locally.
- local runtime alive while cloud stale => LIVE + SYNC_DEGRADED.
## Reconciliation model

Do not use generic last-write-wins between uc.db and Supabase.

Local execution path:
WorkGraph/uc.db -> append event/outbox -> Sync Bridge -> Supabase durable projection.

Cloud-to-local path is intentionally narrower:
intent/approval/event ingress -> validation/policy -> Nardole dispatch -> local WorkGraph.

Supabase must never silently overwrite local execution ownership.

Every replicated mutation carries:
event_id, source_node, work_id/correlation_id when available,
entity version, observed_at, idempotency key, source authority and evidence ref.

Conflict classes:
- LOCAL_NEWER
- CLOUD_NEWER_BUT_NONAUTHORITATIVE
- OWNERSHIP_CONFLICT
- STALE_BINDING
- SOURCE_DRIFT
- MISSING_RUNTIME_EVIDENCE
- DUPLICATE_EVENT
- UNKNOWN

Rory emits reconciliation findings; River executes safe sync/retry flows; Donna receives unknown-effect cases.
## API Projection Layer

Browser -> Projection Gateway only.

Read:
GET /v1/projections/runtime-presence
GET /v1/projections/work/:work_id
GET /v1/projections/mission/:work_id
GET /v1/projections/source
GET /v1/projections/evidence/:entity_id
GET /v1/projections/sync-health

Writes allowed from UI are bounded:
POST /v1/intents
POST /v1/approvals/:approval_id
POST /v1/user-actions/:action_id

No generic browser endpoint may mutate claim, lease, session_binding or raw orchestration tables.

Service-role Supabase credentials remain server-side in the Projection Gateway/Sync Adapter.
## Realtime semantics

Local UI:
- authoritative snapshot via GET projections;
- SSE or WebSocket event stream for low-latency invalidation/update envelopes;
- reconnect always performs full projection refresh.

Supabase:
- durable Postgres rows remain recovery truth for cloud projections;
- Realtime Broadcast/Presence may accelerate notifications but never substitute durable reconstruction;
- Postgres Changes may be used only on explicitly projected server-side tables/views;
- missed realtime events must be recoverable by rereading the projection.

Presence channels are advisory ephemeral membership, never work ownership.

## Offline/degraded operation

Supabase unavailable:
- local runtime + uc.db continue;
- local outbox persists;
- UI shows SYNC_DEGRADED;
- River retries with backoff;
- no fake cloud success.

Local runtime unavailable:
- cloud/history remains visible;
- presence becomes OFFLINE/FAILED/STALE according to evidence age;
- mutation requiring local authority is denied/held.

uc.db unavailable:
- runtime may be observable LIVE;
- ownership becomes UNKNOWN;
- dangerous work mutations are blocked.

Provider auth failure:
- FAILED(provider), not OFFLINE(machine).

Projection Gateway unavailable:
- Amy shows gateway unavailable/UNKNOWN; cached data is visibly stale.
## Source synchronization

A world/source fingerprint includes:
- world/repo id;
- parent repo URL/branch/HEAD;
- committed gitlinks/submodule SHAs;
- observed nested repository HEADs;
- nested branches;
- dirty flags;
- worktree paths;
- active PR/commit refs when known;
- observed_at.

Parent-clean does not imply source-current if nested HEAD differs.

SourceSyncReceipt records before/after fingerprint, changed refs, result and evidence URI.

GitHub is first-class collaboration state:
Discussion = exploration
Issue = accepted contract
Project = composition
PR = mutation + proof
Review = independent assessment
Worktree = execution surface

MissionProjection links WorkGraph + GitHub + runtime + evidence instead of duplicating them.
## Companion responsibilities

Ryan / BUILD-CAPABILITY:
- Projection Gateway service;
- adapters;
- runtime collectors/hooks;
- Sync Bridge;
- CLI/runtime configs;
- service install/start/recovery;
- schemas/tests;
- no business workflow ownership after publication.

River / FLOW:
- operate observation->normalize->sync workflows;
- retries/backpressure;
- projection invalidation;
- event choreography;
- consume capabilities published by Ryan;
- no environment/toolchain plumbing.

Yaz / SENSE:
- process/port/session/provider/child-process RuntimeObservation.

Graham / STATE:
- receipt provenance, version history, replay identity.

Rory / COHERE:
- reconciliation findings and contradiction classification.

Nardole / DISPATCH:
- claims/leases/bindings and routing.

Amy / PRESENT:
- render projections only; never infer liveness.

Donna / RECOVER:
- unknown effect / irreconcilable divergence.
## Continuous implementation gates

These are evidence gates inside one continuous mission, not future-project parking lots.

G0 — Projection contracts + local gateway skeleton.
G1 — RuntimeObservation -> RuntimePresenceProjection with TTL.
G2 — WorkGraph adapter and ownership-aware presence.
G3 — Supabase outbox/sync projection + idempotent replay.
G4 — source fingerprint including nested repos.
G5 — Rory reconciliation + SyncHealthProjection.
G6 — Amy migration away from hard-coded status.
G7 — realtime reconnect/recovery semantics.
G8 — end-to-end production canary.

Ryan continues G0->G8 unless a typed CapabilityNeed blocks him.
River begins as soon as G1/G3 published capabilities are consumable and runs FLOW in parallel.

## End-to-end acceptance

The mission closes only when all are true:

1. Amy cannot display LIVE without fresh runtime evidence.
2. LIVE and ownership are visibly separate.
3. local runtime can stay usable with Supabase offline.
4. reconnect/replay does not duplicate cloud projection events.
5. cloud stale state cannot override local execution truth.
6. nested Desktop HEAD drift is visible as SOURCE_STALE.
7. browser contains no Supabase service-role secret.
8. a missed realtime window heals from snapshot read.
9. one work_id can be traced UI -> WorkGraph -> runtime -> Supabase -> GitHub -> evidence.
10. killing/restarting the Projection Gateway does not lose execution truth.
11. no Vite-only middleware is required for production semantics.
12. Ryan can publish the substrate and leave; River can continue operations without his session/context.
