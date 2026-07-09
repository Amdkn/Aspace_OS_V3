---
source: Codex / Shadow L0
date: 2026-05-16
type: hooks-configuration
domain: L0_Tech_OS / Hermes_Agent
tags: [#Codex #Context7 #Hooks #DocsDogmatique #ShadowL0]
status: active
---

# Context7 Codex Hooks — 2026-05-16

## Intent

Configure Codex hooks so the A'Space Docs Dogmatique is injected systematically into Codex sessions and turns.

This is a Codex/Shadow L0 discipline layer, not a Hermes Agent runtime hook.

## Files Changed

Codex global hooks config:

```text
C:\Users\amado\.codex\hooks.json
```

Hook scripts:

```text
C:\Users\amado\.codex\hooks\context7_session_start.ps1
C:\Users\amado\.codex\hooks\context7_user_prompt_submit.ps1
C:\Users\amado\.codex\hooks\context7_pre_tool_use.ps1
```

## Hook Events

### SessionStart

Injects Shadow L0 doctrine at startup, resume, or clear:

```text
Read local README/AGENTS entry point first.
Use Context7 MCP before durable changes to Hermes, providers, MCP, hooks, WSL, or modern dependencies.
Fallback only to official vendor docs or local upstream source, explicitly labeled.
Never expose API keys.
Document source, file changed, validation command, residual risk, and secret-handling note.
```

### UserPromptSubmit

Runs on every user prompt.

If the prompt looks technical/configuration-sensitive, it injects a stronger Context7 checkpoint. Otherwise it injects the standing rule that Context7 must be used when the turn becomes docs/config/provider/dependency-sensitive.

### PreToolUse

Runs before supported tool calls matching:

```text
Bash|apply_patch|Edit|Write|mcp__.*
```

For sensitive tool inputs touching Codex/Hermes/provider/MCP/WSL/doc config, it adds a model-visible warning:

```text
Confirm Context7 or official docs have been consulted, keep secrets out of output, and document validation/residual risk.
```

This hook does not block by default. It is a doctrine/attention guard, not an enforcement boundary.

## Installed hooks.json

Shape:

```json
{
  "hooks": {
    "SessionStart": "...",
    "UserPromptSubmit": "...",
    "PreToolUse": "..."
  }
}
```

Codex official docs confirm:

- `SessionStart` supports extra developer context via `hookSpecificOutput.additionalContext`.
- `UserPromptSubmit` supports common JSON output fields and turn-scope behavior.
- `PreToolUse` supports `systemMessage` and `hookSpecificOutput.additionalContext`.
- Hooks are discovered from `~/.codex/hooks.json`.

## Verification

Syntax checks:

```powershell
Get-Content C:\Users\amado\.codex\hooks.json | ConvertFrom-Json
[scriptblock]::Create((Get-Content -Raw C:\Users\amado\.codex\hooks\context7_session_start.ps1))
[scriptblock]::Create((Get-Content -Raw C:\Users\amado\.codex\hooks\context7_user_prompt_submit.ps1))
[scriptblock]::Create((Get-Content -Raw C:\Users\amado\.codex\hooks\context7_pre_tool_use.ps1))
```

Synthetic hook tests:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\.codex\hooks\context7_session_start.ps1
'{"prompt":"Configure Hermes MCP provider with MiniMax"}' | powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\.codex\hooks\context7_user_prompt_submit.ps1
'{"tool_name":"apply_patch","tool_input":{"command":"*** Update File: C:\\Users\\amado\\.codex\\config.toml"}}' | powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\.codex\hooks\context7_pre_tool_use.ps1
```

Codex runtime smoke test:

```powershell
codex exec --skip-git-repo-check --ephemeral --json "Reply exactly: codex-hook-ok"
```

Observed result:

```text
codex-hook-ok
```

No hook failure blocked the run.

## Residual Risk

Codex hooks are guidance and guardrail surfaces, not a total enforcement boundary.

The official docs note that `PreToolUse` does not intercept every possible tool path. Codex still needs to obey the doctrine in reasoning, not rely only on hooks.

## Sources

- OpenAI Codex Hooks docs: `https://developers.openai.com/codex/hooks`
- Local Codex feature list: `codex features list`
- Local Codex MCP config: `C:\Users\amado\.codex\config.toml`
- Context7 Codex MCP config: Doc 09

---

*Documenté Docs Dogmatique — Context7 hooks pour Codex Shadow L0 — 2026-05-16 — Codex*
