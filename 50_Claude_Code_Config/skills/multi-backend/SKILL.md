---
name: multi-backend
description: Cross-backend agentic delegation via MCP stdio — routes A0 intentions to Claude Code (default), Codex CLI (code tasks), or Hermes Agent (messaging/kanban) using Anthropic Agent SDK + Hermes MCP server + Codex MCP server. Implements orchestrator-workers pattern with isolated context windows.
---

# /multi-backend — A0 Cross-Backend Delegation

> **Skill Symphony Multi-Backend** — invocable par A0 Amadeus via `/multi-backend <intention> [<backend-hint>]`.
>
> **Composé de 4 sources canon** :
> 1. Anthropic CC Agent SDK (`code.claude.com/docs/en/agent-sdk`) — programmatique Python/TS
> 2. OpenAI Codex CLI MCP Server (`developers.openai.com/codex`) — JSON-RPC stdio
> 3. Hermes Agent MCP Server (`hermes-agent.nousresearch.com/docs/user-guide/features/mcp`) — 10 tools messaging
> 4. Aspace bridge `agent-os-to-symphony.sh` (`10_Tech_OS/agent-os-bridge/`) — D4 append-only

## Architecture (4-tiers delegation)

```
A0 (Claude Code / Main Agent)
    ↓
[swarm-orchestrator] detect backend by:
    ├─ Default = Claude Code (lead agent coord)
    ├─ backend-hint="codex" → Codex CLI (Rust MCP server)
    ├─ backend-hint="hermes" → Hermes Agent (Python MCP server)
    └─ backend-hint="auto" → CC decides based on task nature
    ↓
[Sub-agents // isolated context windows per Anthropic canon]
    ├─ Workers execute via MCP stdio (universal lingua franca)
    ├─ Hermes: 10 tools (conversations_list, messages_send, channels_list, events_poll...)
    ├─ Codex: JSON-RPC App Server + MCP server mode
    └─ CC: Agent SDK sub-agents (Task tool, same tools, isolated context)
    ↓
[Results returned to Main Agent via `parent_tool_use_id`]
    ↓
[A0 reçoit résumés synthétisés — jamais outputs bruts (D7 cost-of-escalation)]
```

## E-Myth delegation canon (Anthropic orchestrator-workers)

| Rôle E-Myth | = Backend | Pattern |
|---|---|---|
| **Visionnaire** | A0 (CC, divinité) | Émet intention, valide résultat |
| **Manager** | CC Agent SDK sub-agents | "A central LLM dynamically breaks down tasks, delegates them to worker LLMs" |
| **Technicien** | Codex CLI (code) / Hermes Agent (messaging/kanban) | Tool-calling LLM, isolated context |

## Workflow canonique (5 steps)

### Step 1 — Air Lock (Turn 1)
`/multi-backend` clarifie :
1. **Intention A0** : quel livrable concret ?
2. **Backend hint** : "auto" / "codex" / "hermes" / "cc"
3. **Cadence** : one-shot / cycle / until-done
4. **Critères succès** : 3-5 vérifiables (D1 receipt)

### Step 2 — Backend detection
Si `auto` : analyser intention et router selon nature :
- **Code writing/refactor/build-fix** → Codex CLI (Rust MCP server, 96.3% du repo)
- **Messaging/kanban/twin runtime/cron** → Hermes Agent (Python MCP server, 10 tools)
- **Orchestration/strategic/coordination** → CC sub-agents (Agent SDK)

### Step 3 — Spawn sub-agents via MCP stdio
**Pattern canon Anthropic** : "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions."

Pour Codex : JSON-RPC App Server over stdio (`codex app --mode server` ou invocation MCP).
Pour Hermes : `hermes mcp serve` expose 10 tools aux MCP clients (CC, Cursor, Codex).

### Step 4 — Context isolation (D7 ROI)
**Hermes verbatim** : "Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns."

**CC verbatim** : "SubagentStart | When a subagent is spawned ; SubagentStop | When a subagent finishes".

### Step 5 — Synthesis + A0 validation
Retour au Main Agent via `parent_tool_use_id` → synthèse D1 receipts (file counts, byte counts, grep) → TTS stop hook Hortense.

## Doctrine ancrage (D1-D8)

- **D1 verify-before-assert** : tous claims cross-backend doivent fournir receipts filesystem (`mcp__symphony-supabase__supabase_query` ou `mcp__hostinger-dns__DNS_getDNSRecordsV1`)
- **D2 research-first** : lire canon (handoff/AGENTS.md/ADR) AVANT spawn cross-backend
- **D3 nuance** : A0 = Stratège (Visionnaire), CC = Manager (orchestrator), A3/Codex/Hermes = Techniciens (workers)
- **D4 no-self-contradiction** : log.md append-only, state.json versionné
- **D7 cost-of-escalation** : A0 passif board observer ; sub-agents isolés = zero-context-cost ; max 2 itérations avant escalate
- **D8 cross-agent** : "Codex and Gemini CLI can be invoked from the same Hermes routing pattern, but Claude is the primary executor" (handoff_business_os_resumption §2.3)

## Fichiers canon liés

- `C:\Users\amado\.claude\skills\swarm-orchestrator\SKILL.md` — orchestrateur dispatch
- `C:\Users\amado\.claude\skills\symphony-fabuleux-discipline\SKILL.md` — 4 piliers production
- `C:\Users\amado\.claude\skills\symphony-phase2-batch\SKILL.md` — 8 sub-agents // Phase 2
- `C:\Users\amado\.claude\skills\replicate-squads\SKILL.md` — squad folders sync
- `C:\Users\amado\.claude\commands\routine.md` — orchestrateur 3-tiers
- `C:\Users\amado\.claude\skills\multi-goal\SKILL.md` — goal-driven loop
- `C:\Users\amado\.claude\skills\multi-loop-karpathy\SKILL.md` — Karpathy cycle
- `C:\Users\amado\.claude\skills\multi-routines-12wy\SKILL.md` — cycle 12WY

## Sources externes

- https://code.claude.com/docs/en/agent-sdk (Anthropic Agent SDK Python/TS)
- https://code.claude.com/docs/en/sub-agents (CC sub-agents isolés)
- https://code.claude.com/docs/en/hooks (SubagentStart/Stop, TeammateIdle)
- https://www.anthropic.com/engineering/building-effective-agents (orchestrator-workers)
- https://github.com/openai/codex (Rust 96.3%, v0.141.0)
- https://developers.openai.com/codex (Codex SDK + MCP + App Server JSON-RPC)
- https://github.com/NousResearch/hermes-agent (MIT, 199k stars, v0.17.0)
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp (Hermes-as-MCP-server)
- https://modelcontextprotocol.io (MCP canon, "USB-C port for AI")

## Usage

```
/multi-backend <intention> [<backend-hint>]
```

Exemples :
- `/multi-backend "implement Life-OS-2026 BETA V2.0 multi-tenant RLS" codex`
- `/multi-backend "sync Hermes kanban.db with 12WY Q3 items" hermes`
- `/multi-backend "research Saru 1000T Anti-paperclip pattern" auto`
- `/multi-backend "ship W2 milestone by 07/26" auto`