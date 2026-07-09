---
source: Codex / Shadow L0
date: 2026-05-17
type: executor-strategy
domain: L0_Tech_OS / Shadow_L0 / Symphony
tags: [#CodexCLI #GeminiCLI #ClaudeCode #MiniMax #Symphony #LLM_Wiki #ShadowL0]
status: active-codex-configured
---

# Shadow L0 Executor Mesh — Codex-first replacement for Hermes/OpenClaw/Paperclip

## 1. Purpose

This document defines how Shadow L0 should coordinate Codex CLI, Gemini CLI, and Claude Code CLI after Hermes retrogradation.

The target is not another heavy dashboard. The target is a headless execution mesh:

```text
Tracker -> Symphony -> Executor -> Proof -> Tracker / LLM_Wiki
```

## 2. Current Executor Roles

| Executor | Primary role | Strength | Use when |
|---|---|---|---|
| Codex CLI | Default local implementation executor | Code edits, tests, docs, Context7 discipline, local filesystem work | Need reliable patching, evidence, repo-aware execution |
| Gemini CLI | High-quota scout and large-context doer | Broad context, fast research, cheap iteration, Google quota pool | Need exploration, rough implementation, long-context analysis |
| Claude Code CLI via MiniMax | Bulk Claude-style executor on Token Plan | Anthropic-compatible agent workflows without draining Claude subscription quota | Need Claude Code ergonomics with MiniMax capacity |
| Claude Anthropic | Premium arbitration | Highest-judgment architecture and final review | Rick Prime / high-risk decisions only |

## 3. Codex CLI Configuration State

Configured file:

```text
C:\Users\amado\.codex\config.toml
```

Configured MCP:

```text
context7 -> npx -y @upstash/context7-mcp
```

Configured hooks:

```text
C:\Users\amado\.codex\hooks.json
C:\Users\amado\.codex\hooks\context7_session_start.ps1
C:\Users\amado\.codex\hooks\context7_user_prompt_submit.ps1
C:\Users\amado\.codex\hooks\context7_pre_tool_use.ps1
```

Configured profiles:

```toml
[profiles.shadow_l0_safe]
sandbox_mode = "workspace-write"
approval_policy = "on-request"

[profiles.shadow_l0_exec]
sandbox_mode = "workspace-write"
approval_policy = "never"

[profiles.shadow_l0_yolo]
sandbox_mode = "danger-full-access"
approval_policy = "never"
```

## 4. Codex Execution Policy

### `shadow_l0_safe`

Use for:

- architecture edits;
- docs updates;
- tracker/API configuration;
- any work touching secrets, WSL, providers, MCP, hooks, or dependencies.

Command pattern:

```powershell
codex exec -p shadow_l0_safe --json --cd <workspace> "<mission>"
```

### `shadow_l0_exec`

Use for:

- routine code edits;
- tests;
- deterministic docs generation;
- non-secret local repo work.

Command pattern:

```powershell
codex exec -p shadow_l0_exec --json --cd <workspace> "<mission>"
```

### `shadow_l0_yolo`

Use only when all are true:

- workspace is disposable or fully backed up;
- no secrets are reachable;
- branch/worktree is isolated;
- task is bounded by timeout and explicit output proof;
- Symphony can mark the run failed and route to Donna if proof is missing.

Command pattern:

```powershell
codex exec -p shadow_l0_yolo --json --cd <isolated-workspace> "<mission>"
```

## 5. Symphony Routing Rule

Symphony should select executors by work type:

| Payload type | Default executor | Fallback |
|---|---|---|
| Repo patch / tests | Codex `shadow_l0_exec` | Gemini CLI |
| Docs/config/provider/MCP | Codex `shadow_l0_safe` | Claude Anthropic review |
| Broad research / context compression | Gemini CLI | Codex safe |
| Claude-style bulk implementation | Claude Code via MiniMax | Codex exec |
| High-risk architecture | Claude Anthropic | Codex safe |

## 6. Required Agent Capsule

Every durable Shadow L0 agent must have:

```text
Soul.md
Agent.md
Heartbeat.md
Tools.md
Context.md
```

Minimum semantics:

- `Soul.md`: identity, tone, non-negotiables, role boundary.
- `Agent.md`: exact layer, owner, supervisor, deliverables.
- `Heartbeat.md`: cadence, stale threshold, wake-up trigger, proof target.
- `Tools.md`: allowed tools, forbidden tools, profile, MCP scope.
- `Context.md`: current mission, tracker pointers, wiki links.

## 7. Replacement for Paperclip AI organization

Paperclip-style org/team/task management is replaced by:

```text
LLM_Wiki entities      -> org chart, identities, doctrine
Trackers              -> current tasks and state
Symphony              -> routing and dispatch
Executor profiles     -> actual local work
Proof artifacts       -> reports, logs, tracker comments, wiki updates
```

## 8. Docs Dogmatique Sources

Context7 sources used on 2026-05-17:

- `/openai/codex`: `codex exec`, `--json`, `--sandbox`, `--dangerously-bypass-approvals-and-sandbox`, config keys `sandbox_mode`, `approval_policy`, MCP commands.
- `/google-gemini/gemini-cli`: `gemini -p`, `--output-format json|stream-json`, `--approval-mode plan`, `mcpServers`, `security.disableYoloMode`.
- `/anthropics/claude-code`: stdio MCP configuration, managed settings, bypass-permission governance.

## 9. Secret Handling

- No API key belongs in this document.
- MiniMax key should remain local and masked.
- Executor prompts should refer to environment variable names only.
- Any pasted key is considered exposed and must be rotated.

## 10. Residual Risk

- Codex profiles are configured, but Symphony is not yet implemented as a daemon.
- Gemini and Claude Code profile files are not yet normalized in this document.
- Heartbeat is currently a file/protocol requirement, not an active scheduler.
- `shadow_l0_yolo` is intentionally available but must be treated as isolated-workspace only.

*Documente Docs Dogmatique — Shadow L0 executor mesh and Codex CLI strategy — 2026-05-17 — Codex*
