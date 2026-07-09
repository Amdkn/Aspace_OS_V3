---
source: Shadow_L0
date: 2026-05-18
type: agent-capsule
agent: Claude_Code_CLI
version: 2
tags: [#AgentCapsule, #ClaudeCode, #Tools, #MiniMax, #Durable]
---

# Tools - Claude Code CLI Capability Surface

## Provider (Durable Configuration)

Claude Code CLI runs on **MiniMax Token Plan Anthropic-compatible backbone** :

| Env Var (Windows User scope) | Value | Source |
|---|---|---|
| `ANTHROPIC_AUTH_TOKEN` | `<MiniMax PAT, 125 chars>` | platform.minimax.io |
| `ANTHROPIC_BASE_URL` | `https://api.minimax.io/anthropic` | MiniMax canonical international |
| `ANTHROPIC_MODEL` | `MiniMax-M2.7` | model name (PascalCase exact) |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | `1` | reduce telemetry |
| `API_TIMEOUT_MS` | `3000000` | 50 min for long missions |

All five are **Windows User env vars** - durable across reboots, Claude Code reinstalls, system updates. Env vars take **priority over `~/.claude/settings.json`** per MiniMax official docs.

The `~/.claude/settings.json` `env` block mirrors these (except `ANTHROPIC_AUTH_TOKEN` which is intentionally absent from JSON - never in clear text in any file) and provides per-model aliasing :

```json
"env": {
  "ANTHROPIC_BASE_URL": "https://api.minimax.io/anthropic",
  "ANTHROPIC_MODEL": "MiniMax-M2.7",
  "ANTHROPIC_SMALL_FAST_MODEL": "MiniMax-M2.7",
  "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M2.7",
  "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M2.7",
  "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M2.7",
  "API_TIMEOUT_MS": "3000000",
  "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
}
```

-> `/model sonnet`, `/model opus`, `/model haiku` all map to MiniMax-M2.7 internally (no broken alias).

## Rotation Procedure

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\.claude\bin\Set-MiniMaxAuth.ps1"
```

Masked SecureString input - token never in chat, never in process list, never in shell history. Per Test Key Pragma doctrine (`~/.claude/CLAUDE.md`), A0 can also paste a fresh PAT in chat for rapid verification before the durable masked install (post-test rotation expected).

## Allowed Tools (capability surface)

### Built-in Claude Code Tools (always available)

| Tool | Purpose |
|---|---|
| Read, Write, Edit, Glob, Grep | Filesystem (default trust zone : `C:\Users\amado\`) |
| Bash | PowerShell + bash via Git Bash; bypass-allowed wildcards in settings.json |
| WebFetch, WebSearch | External research (Docs Dogmatique) |
| Skill | Invoke `/skill-creator` and other skills (Claude is the only CLI authorized to invoke `/skill-creator`) |
| TodoWrite | In-session task tracking |
| Agent | Spawn subagents for parallel research |
| AskUserQuestion | Structured Turn-1 clarification (3-Turn Air Lock) |

### MCP Servers (when connected)

| MCP | Purpose | Auth source |
|---|---|---|
| `context7` | Library docs lookup (mandatory before any provider/MCP/CLI config per Docs Dogmatique) | API key in `.claude.json` |
| `airtable` | Read/write A'Space bases (auto-disconnects sometimes) | Desktop UI |
| `clickup` | Task management | Desktop UI |
| `notion` | Knowledge base | Desktop UI |
| `supabase` | Self-hosted database | PAT |
| `playwright` | Browser automation | None |
| `desktop-commander` | Process / file management on Windows | None |

When MCPs disconnect mid-session -> Claude continues with direct CLI / curl fallback (per God Mode CLI Stack doctrine).

### Shadow L0 Wrappers (for cross-CLI dispatch)

| Wrapper | Purpose |
|---|---|
| `shadow_l0_safe "X"` | Dispatch read-only mission to Codex |
| `shadow_l0_exec "X"` | Dispatch implementation mission to Codex |
| `shadow_l0_yolo "X"` | Dispatch isolated experiment to Codex |
| (Gemini equiv TBD) | Will be `gemini -p "X"` once Gemini capsule has wrapper |

## Forbidden Tools

- Log `ANTHROPIC_AUTH_TOKEN` value anywhere (only variable name)
- Edit Anthropic-namespace files (`.anthropic/`, `~/.config/anthropic/`) - those are reserved for the harness
- Use any other Claude API endpoint that bypasses MiniMax routing (would silently consume Anthropic native quota and break the "no autonomy violation" contract)
- Invoke autonomous Claude SDK launches (Anthropic policy refusal - that's why we're on MiniMax)

## Quota Awareness

Two distinct quota envelopes (per `concept_heartbeat_2026` Fallback Roles) :

| Layer | Limit type | Recovery |
|---|---|---|
| MiniMax Token Plan | `4500 model requests / 5 hours` (Plus plan) + `45,000 weekly` | 429 -> fallback to Gemini per Heartbeat routing |
| Claude Code session | Local TUI context window + 5h plan limit | `/compact` or restart |

When MiniMax 429 hits -> `heartbeat-tick.ps1` routes the mission to Gemini per the fallback chain. Persona (Doctor.Companion) invariant. Logged as `HEARTBEAT_ROUTE | preferred=Claude_Code_CLI | actual=Gemini_CLI | reason=minimax-429`.

## Cross-refs

- `Heartbeat.md` - tempo + 3-checks + fallback roles
- `Soul.md` - identity (TBD)
- `Agent.md` - mission scope (TBD)
- `~/.claude/CLAUDE.md` Test Key Pragma - the rotation contract
- `~/.claude/bin/Set-MiniMaxAuth.ps1` - the rotation script
- `concept_god_mode_cli_stack` - the CLI surface this runs on
- `concept_heartbeat_2026` - the tick pattern
- https://platform.minimax.io/docs/token-plan/claude-code - external canon
