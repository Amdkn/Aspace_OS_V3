# HANDOVER — 2026-09-29 — AMY → CLARA — AGENT OS FRONTEND / API

## Mission
Provide the frontend/interface half of the Agent OS Full-Stack Unification analysis before Clara architecture design.

## Verified facts
- Agent OS Desktop has no Supabase JS client dependency.
- Main session persistence is localStorage.
- Optional storage adapter is PocketBase/local, not Agent OS Supabase.
- Front uses Vite-local `/api/*` middleware as its backend façade.
- `/api/tech-os/*` reads local `uc.db`, filesystem reports and Python scripts.
- Local Agent OS is reachable at port 5555.
- Telemetry and Workspace health respond.
- `/api/tech-os/subagents` currently returns zero agents.
- Expected roster/scheduler JSON files are absent.
- Several UI/service statuses are hard-coded or identity-derived and are not live-worker evidence.
- Parent Agent-OS gitlink points to desktop `7c6dc8b`, while the actual desktop repo is at `c0dc5d2`.

## Interface problem
Amy and Supabase are not merely “out of sync”; they currently represent different state planes.

## Required Clara input
Use `10_Tech_OS/reports/amy_agent_os_frontend_api_audit_20260929.md`.

Do not begin final architecture until Rory's backend/Supabase packet is consumed.

## Design guardrails
- no green/ONLINE status without fresh evidence;
- browser UX state != orchestrator state;
- versioned typed API/projection between UI and backend;
- local process probing stays server-side;
- no service-role secret in frontend;
- presence must carry provenance + freshness + TTL.
