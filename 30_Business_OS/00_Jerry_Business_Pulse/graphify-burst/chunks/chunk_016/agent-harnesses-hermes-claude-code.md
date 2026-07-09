---
id: PEOPLE-HARNESS-001
title: "Agent Harnesses — the bodies of A'Space agents (Hermes + Claude Code)"
category: "People / Agent Harness / Embodiment"
status: CANONICAL_FROM_A0 (content provided by A0 2026-06-02 — Hermes/Nous + Claude Code feature surfaces)
source: A0_directive + hermes-workspace.com + hermes-agent.nousresearch.com docs
date: 2026-06-02
tags: [#people #harness #hermes #claude_code #nousresearch #model_agnostic #affordability #swarm #cron #heartbeat]
---

# Agent Harnesses — the bodies of A'Space agents

> [!IMPORTANT]
> **People doctrine extension (A0 2026-06-02).** Beyond the agent *Lore* (the X-Men roster, the
> identity), a People principle is that **the harness IS the agent's body**. An A'Space capsule is
> only as capable as the harness it runs in. The two primary bodies are **Claude Code** and
> **Hermes** (Nous Research), chosen for **agnosticism** (model-swappable) and **affordability**
> (GLM 4.7 Flash via OpenRouter, MiniMax token plan, … more later). The Hermes ecosystem is becoming
> *incontournable*, especially the Hermes Workspace.

## Why these two harnesses (the selection doctrine)

- **Model-agnostic** : the body must not be welded to one brain. Swap GLM 4.7 Flash (OpenRouter) /
  MiniMax (token plan) / Claude / others without changing the capsule. (Matches the compute-frugality
  doctrine: cheap default models, premium reserved.)
- **Affordable** : GLM 4.7 Flash + MiniMax token plan keep a 24/7 swarm economically viable.
- **Sovereign-friendly** : provider routing, fallback providers, credential pools, MCP, local backends.

## Hermes Workspace — the live control plane (https://hermes-workspace.com/)

Turns the workspace into a control plane: **unlimited Hermes Agents, 1 orchestrator, 0 humans
dispatching**. Key surfaces:
- **Swarm Mode** — persistent **tmux-backed workers** keep context across tasks, rotate safely, report
  **proof-bearing checkpoints**; **role-based dispatch** (builders / reviewers / docs / research / ops
  / triage / QA / lab) so the human isn't the task router; a **byte-verified review gate** protects
  release branches before PRs ship; autonomous PR/issue lanes + repair playbook.
- **Orchestrator Chat** — one task, a decomposed mission, or a full broadcast.
- **Multi-Agent Control Plane** — persistent agents, roles, state, runtime, routing wires in one view.
- **Kanban TaskBoard** — backlog / ready / running / review / blocked / done.
- **Reports + Inbox** — checkpoints, blockers, handoffs, ready-for-human decisions.
- **TUI** — attach to tmux workers or live shell/log stream.
- Inside: Chat (SSE streaming, tool-call render, multi-session) · **Memory** (browse/search/edit) ·
  **Skills** (2,000+, marketplace, agentskills.io standard) · **MCP** (catalog + marketplace + CRUD) ·
  Files+Terminal (Monaco + PTY) · Operations (presets Sage/Trader/Builder/Scribe/Ops) · **Conductor**
  (mission dispatch + decomposition, Swarm fallback) · Agent View · **Dashboard** (sessions, model mix,
  **cost ledger**, attention card) · Themes · Security (auth on every route, CSP, path-traversal guard,
  fail-closed remote bind) · **PWA + Tailscale** (any device on the tailnet) · capability gates.

## Hermes Agent — the autonomous body (https://hermes-agent.nousresearch.com)

- **Core**: Tools & Toolsets (per-platform enable/disable) · **Skills** (progressive disclosure,
  agentskills.io) · **Persistent Memory** (MEMORY.md / USER.md across sessions) · **Context Files**
  (auto-discovers `.hermes.md`, **AGENTS.md**, **CLAUDE.md**, **SOUL.md**, `.cursorrules`) · Context
  References (`@` inject files/folders/git-diffs/URLs) · **Checkpoints** (snapshot + `/rollback`).
- **Automation**: **Scheduled Tasks (cron)** · **Subagent Delegation** (`delegate_task`, isolated
  context, restricted toolsets, 3 concurrent default) · **Code Execution** (`execute_code`, sandboxed
  RPC) · **Event Hooks** (logging/alerts/webhooks, tool interception, guardrails) · Batch Processing.
- **Media & Web**: Voice Mode · Browser Automation (Browserbase/Browser-Use/local CDP) · Vision &
  Image Paste · Image Generation (FAL.ai, 9 models) · Voice & TTS (Edge free, ElevenLabs, OpenAI,
  **MiniMax**, …).
- **Integrations**: **MCP** (stdio/HTTP, per-server filtering) · **Provider Routing** (cost/speed/
  quality sorting, whitelist/blacklist/priority) · **Fallback Providers** · **Credential Pools**
  (rotation on rate-limit) · **Prompt caching** (cross-session 1h prefix, always-on) · Memory
  Providers (Honcho/Mem0/Supermemory/…) · **API Server** (OpenAI-compatible) · IDE/ACP (VS Code/Zed/
  JetBrains) · Batch.
- **Customization**: **SOUL.md** (primary identity, first in system prompt) · Skins/Themes ·
  **Plugins** (tools/hooks, memory providers, context engines).

## Heartbeat / autonomy

Cron scheduled tasks (Hermes Agent) — ref NousResearch/hermes-agent issue #15400 — or equivalent give
the **fluid automation + autonomy** A'Space wants: the harness wakes itself on schedule, runs a tick,
reports a checkpoint. This is the Hermes-native equivalent of the Shadow L0 `heartbeat-tick.ps1` mesh.

## A'Space mapping (why this is People doctrine)

- **The harness = the body**; the SOUL.md/AGENTS.md/CLAUDE.md = the identity People onboards into it.
- Hermes' **Context Files** auto-load A'Space's own `AGENTS.md` / `CLAUDE.md` / `SOUL.md` → the canon
  drives the body natively.
- Hermes **Swarm + role dispatch + byte-verified review gate** ≈ the B3 swarm + Build Gate doctrine.
- **MEMORY.md / checkpoints / rollback** ≈ the wiki-log-as-memory + Donna DLQ safety net.
- **Provider routing + credential pools + fallback** ≈ the compute-frugality + quota-aware fallback chain.
- Cron ≈ Shadow L0 heartbeat. IT (Cyborg) owns the *runtime*; People (X-Men) owns onboarding the
  *member* into the harness with dignity + ethics.

*Resource captured from A0-provided content (Hermes/Nous + Claude Code feature surfaces), 2026-06-02.
Feeds People doctrine v2 (harness layer PE13–PE18).*
