# ADR-D11 — Universal IPBD Capture & Intent Persistence

**Date:** 2026-09-27
**Manager:** Doctor11
**Integrity:** Rory
**Interface:** Amy
**Flow:** River
**Existing Linear contracts:** SOH-13, SOH-31, SOH-55, SOH-56, SOH-57, SOH-117

## Decision

A'Space must not depend on the lifetime of a chat, agent session, cron process, browser tab or model context to remember an unresolved human intention.

The canonical ingress is IPBD:

- I — Intention
- B — Besoin
- P — Problematique
- D — Desir

Every capture preserves the verbatim source before any normalization. The system may classify, link, summarize or route an intention later, but it must not erase the originating signal.

## Truth chain

1. Local outbox first — ~/.aspace/intent/outbox.ndjson
2. Machine SSOT — Supabase Aspace OS / Agent OS Backend / aspace
3. Human Blackboard — Linear
4. Versioned artifacts — GitHub
5. Human interface — Amy / Herdr / Life OS
6. Effectors — River / Google Workspace CLI / Opal / approved automation

ASPACE_WORKSPACE_REGISTRY answers WHERE. ADE_REGISTRY answers WHO. Supabase WorkGraph/IPBD answers NOW.

## Supabase contract

- aspace.capture_event — append-first ingress, idempotent by dedupe_key
- aspace.intent — durable intent state
- aspace.intent_source — provenance
- aspace.intent_link — Linear/GitHub/WorkGraph/Workspace references
- aspace.intent_transition — state history
- aspace.capture_cursor — hook watermarks
- aspace.v_intent_inbox — GTD capture inbox
- aspace.v_intent_open — unresolved intentions
- aspace.v_intent_unresolved_age — forgotten-intent detector

An intent row cannot be deleted. Terminal states RESOLVED, CLOSED, and CANCELED require an explicit closure_reason.

## Capture hook

scripts/aspace_capture.py writes the event to the local outbox before remote I/O.

If Supabase is unavailable, the capture is still durable locally. aspace_capture.py sync later replays pending rows. Remote writes are idempotent.

The PC never stores the Agent OS Backend Supabase service-role key. It sends captures to the aspace-intent-capture Edge Function using a dedicated capture token. The Edge Function performs the privileged projection inside Supabase.

## Companion responsibilities

### Rory — Integrity of Integrity

Owns persistence, provenance, closure gates, deduplication, reconciliation and integrity between Supabase and the human-visible Linear projection.

Rory does not become the executor of every Linear issue.

### Amy — Interface of Interface

Owns the Intention Console and human-facing projections. Herdr may provide the agentic pane/workspace surface; Life OS and Stitch may provide richer views.

The UI is never the SSOT.

### River — Flow of Flow

Owns event flow after capture: approved transitions toward Calendar, Tasks, Drive, Sheets, Docs, Apps Script, Workspace Events, Opal and other effectors.

Every consequential mutation must return evidence to the WorkGraph/intent record.

## GTD mapping

IPBD is upstream of the five GTD stages:

Capture -> Clarify -> Organize -> Review -> Engage

The capture hook only guarantees that the signal cannot vanish. It does not guess the next action, project, area or priority at ingress.

## Failure model

- Chat dies -> intent remains.
- Local network fails -> outbox remains.
- Supabase fails -> outbox remains and sync retries.
- Duplicate hook fires -> dedupe_key returns the existing intent.
- Agent misclassifies -> verbatim origin remains.
- User abandons intent -> explicit CANCELED + closure reason.
- Intent succeeds -> explicit RESOLVED/CLOSED + evidence.

## Acceptance

A replacement ChatGPT/Hermes/Jules/Codex session can recover unresolved A0 intent without reconstructing prior chat history by reading:

1. ASPACE_WORKSPACE_REGISTRY.json
2. Supabase aspace.v_intent_open
3. relevant Linear issue(s)
4. GitHub evidence

This is the persistence foundation required before the Amy Intention Console becomes the primary UX.
