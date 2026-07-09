---
source: Codex / Shadow L0
date: 2026-05-17
type: architecture-retrogradation
domain: L0_Tech_OS / Hermes_Agent / Shadow_L0
tags: [#Hermes #Retrogradation #ShadowL0 #LLM_Wiki #Symphony #CodexCLI #GeminiCLI #ClaudeCode #MiniMax]
status: closed-runtime-retained-as-archive
---

# Hermes Agent — Retrogradation officielle vers abstraction LLM Wiki

## 1. Decision

Hermes Agent is no longer treated as a required runtime for A'Space L0 operations during this 12WY cycle.

Hermes is retrograded from:

```text
required local Kanban/runtime/orchestrator
```

to:

```text
historical archive + abstraction source for the LLM Wiki
```

This is a deliberate cycle-protection decision. Hermes troubleshooting must not consume L0 attention when the current 50/30/20 strategy requires L2 production and L1 cadence.

## 2. Why

Observed failure mode:

```text
Chrome pinned app -> http://127.0.0.1:9119 -> ERR_CONNECTION_REFUSED after reboot
```

Even when WSL services sometimes recover, the user-facing boot path remains fragile:

- Windows Task Scheduler timing.
- WSL networking and localhost forwarding.
- Dashboard process availability.
- Browser pinned app opening before services are ready.
- Split Windows/WSL operational state.

The issue is not worth deeper repair right now because Hermes has become a coordination dependency rather than a productivity multiplier.

## 3. New Position

Hermes is retained as:

- proof of prior Paperclip/OpenClaw/Hermes migration attempts;
- source of provider notes, especially MiniMax Anthropic-compatible configuration;
- source of Shadow L0 Context7/Codex hooks;
- evidence trail for Plane/Baserow/Symphony credential and smoke-test work;
- historical input for the LLM Wiki.

Hermes is no longer:

- required for daily task routing;
- required for Kanban state;
- required for agent identities;
- required for heartbeat;
- required for Symphony dispatch.

## 4. Replacement Architecture

```text
LLM_Wiki
  -> canonical memory, entity graph, agent identity substrate

Symphony Headless Router
  -> reads trackers, normalizes SOC payloads, selects executor

Shadow L0 Executor Mesh
  -> Codex CLI
  -> Gemini CLI
  -> Claude Code CLI via MiniMax Token Plan

Trackers
  -> L1: Baserow, Plane
  -> L2: Airtable, ClickUp, Notion
```

## 5. Agent Identity Replacement

Hermes-style runtime identity files are replaced by wiki-backed agent capsules:

```text
Soul.md       -> immutable identity / voice / boundaries
Agent.md      -> role, layer, responsibilities, escalation line
Heartbeat.md  -> cadence, last check, recurring duties, wake-up trigger
Tools.md      -> allowed tools, forbidden tools, MCP/CLI bindings
Context.md    -> current mission, trackers, relevant wiki links
```

These files should live under the LLM Wiki or be generated from it, not hidden inside a fragile local dashboard runtime.

## 6. Docs Dogmatique Sources

Context7 was consulted on 2026-05-17:

- `/openai/codex` for Codex CLI `exec`, profiles, sandbox and MCP configuration.
- `/google-gemini/gemini-cli` for Gemini CLI `-p`, `--output-format`, MCP settings, and approval modes.
- `/anthropics/claude-code` for Claude Code MCP and managed permission settings.

Local sources:

- `00_Amadeus/30_MEMORY_CORE/Hermes Agent/README.md`
- `00_Amadeus/05_OSS_Twin/symphony/README.md`
- `00_Amadeus/05_OSS_Twin/symphony/symphony-base.spec.md`
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/schema.md`

## 7. Operational Rule

For this cycle:

```text
Do not repair Hermes unless a later explicit mission says so.
Do not make Hermes a precondition for L0 work.
Use LLM_Wiki + Symphony + CLI executors instead.
```

## 8. Residual Risk

- Hermes files may still contain useful secrets references or stale commands; read with redaction discipline.
- Existing Windows Task Scheduler and WSL services may continue to exist, but they are now non-critical.
- Heartbeat is not yet implemented in the replacement mesh; it must be represented first as `Heartbeat.md` plus tracker cadence, then later automated.

*Documente Docs Dogmatique — Hermes retrogradation vers LLM Wiki abstraction — 2026-05-17 — Codex*
