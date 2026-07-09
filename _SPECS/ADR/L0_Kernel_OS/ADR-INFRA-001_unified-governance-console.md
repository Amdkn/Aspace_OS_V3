---
id: ADR-INFRA-001
title: Unified Governance Console — one dashboard, governance-apps not isolated dashboards
status: ACCEPTED
date: 2026-06-03
deciders: [A0 Amadeus]
implemented_by: Codex CLI (local Windows docs + VPS disk work) + Hermes (VPS-internal docs/exec)
recorded_by: Claude Code (A2)
domain: L0 Tech_OS / Infrastructure Governance / VPS
tags: [#ADR #infra #governance #dashboard #vps #hermes #codex #console #canonical_rule #doc_ownership]
related: [ADR-HERMES-001, ADR-RICK-001]
---

# ADR-INFRA-001 — Unified Governance Console

## Status
**ACCEPTED** — A0 ruling, 2026-06-03 ("Go pour ADR"). Implemented by Codex + Hermes; recorded by Claude Code.

## Context
A'Space's infrastructure governance was fragmenting into **separate surfaces** (Hermes Agent dashboard, a
Token-Governance dashboard, etc.) and there was a **reflex to spin up an isolated dashboard per concern**.
That reflex multiplies surfaces, services, and drift. Codex (via SSH) structured Hermes on the VPS and
**merged the governance surfaces into a single console**; Hermes validated it.

## Decision

### D1 — One canonical governance console
**URL** : `https://aspace-dashboard.148.230.92.235.sslip.io/` (Next.js app, `aspace-dashboard.service`
active/enabled, loopback `127.0.0.1:9119` exposed via Caddy HTTPS). Sidebar = the **canonical entry point**.
Routes today: `/` Overview · `/infrastructure` (CPU, disk, memory, monitoring policy) · `/tokens` (Token
Governance). External surfaces linked, not duplicated: Hermes Agent (`:8642`), Hermes Workspace (`:3001`),
Dokploy (`:3002`).

### D2 — No isolated dashboards: new dashboards = governance-apps
Every new dashboard becomes a **governance app inside this console**, never a standalone surface:
```
/srv/aspace/dashboard/app/<domain>/        # page.tsx
/srv/aspace/dashboard/app/api/<domain>/    # route.ts (auth-gated → 401 without session)
+ an entry in /srv/aspace/dashboard/components/Sidebar.tsx
npm run lint && npm run build
```
Backed by skills: VPS `aspace-governance-dashboard`, local Codex `dashboard-builder` + `hermes-vps-runtime-ops`.

### D3 — Documentation ownership (the who-documents-where rule)
- **Codex documents LOCALLY on Windows** (the local canon / source).
- **Hermes (inside the VPS) documents INSIDE the server** (`/srv/aspace/...` — the deployed copy).
- **Claude Code (A2)** maintains the local LLM Wiki and reconciles drift between the two
  (this ADR + `concepts/concept_aspace_governance_dashboard.md`).
The `/srv/aspace/` tree is a **deployment**; the local `C:\Users\amado\ASpace_OS_V2\...` is the **source**.
Any rule change must be re-synced on both sides.

## Validation (Codex/Hermes)
lint PASS · build PASS · `/` `/infrastructure` `/tokens` = 200 · `/api/*` = 401 (auth) · service
active/enabled · secret-scan PASS.

## Consequences
- ✅ One mental model + one service for infra governance; no surface sprawl.
- ✅ Adding a concern is a bounded, repeatable act (app + api + Sidebar + lint/build) — not a new deploy.
- ✅ Clear doc-ownership (Codex=local, Hermes=VPS, Claude=reconcile) kills the "documented on the wrong side" drift.
- ⚠️ **Open risk: Supabase disk at 79%** (target 25-50%). **Codex is actively working on disk-usage reduction.**
  Next governance app = **Supabase Health** (analytics / realtime / supavisor) or **Cleanup Approvals** (reduce
  disk *without* dangerous automation) — NOT "CPU/orchestration" (already covered in `/infrastructure`).
- ⚠️ Security: admin APIs stay auth-gated (401); gateways/dashboards loopback + Caddy (echoes ADR-HERMES-001).

## Related
- `ADR-HERMES-001` (Hermes Desktop-native / Workspace-remote topology — same VPS, same loopback+Caddy posture).
- `concepts/concept_aspace_governance_dashboard.md` (local wiki concept).
- Skills: `~/.hermes/skills/aspace-governance-dashboard` (VPS), local `.codex/skills/{dashboard-builder,hermes-vps-runtime-ops}`.
