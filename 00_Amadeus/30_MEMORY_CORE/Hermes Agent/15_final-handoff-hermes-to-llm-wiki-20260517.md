---
source: Codex / Shadow L0
date: 2026-05-17
type: final-handoff
domain: L0_Tech_OS / Hermes_Agent / LLM_Wiki / Shadow_L0
tags: [#Hermes #LLM_Wiki #FinalHandoff #ClaudeCode #GeminiCLI #CodexCLI #Symphony #MiniMax]
status: final-handoff-active
---

# Final Handoff — Hermes Agent -> LLM Wiki / Shadow L0 Mesh

## 1. Executive Decision

Hermes Agent is closed as an operational runtime for the current 12WY cycle.

Do not repair Hermes unless Amadeus explicitly reopens a Hermes-specific mission.

Live coordination now uses:

```text
LLM_Wiki
  -> persistent memory, org chart, agent identities

Symphony
  -> headless router, tracker reader, payload normalizer

Shadow L0 Executor Mesh
  -> Codex CLI
  -> Gemini CLI
  -> Claude Code CLI via MiniMax Token Plan
```

## 2. What Hermes Becomes

Hermes is retained as an archive and abstraction source:

- MiniMax Anthropic-compatible provider notes.
- Context7 MCP and Codex hook setup history.
- Baserow/Plane credential state and smoke-test reports.
- Evidence of why dashboard-bound orchestration is too fragile for this cycle.

Hermes is no longer:

- the Kanban of record;
- the heartbeat system;
- the agent identity runtime;
- the required local dashboard;
- the dependency that blocks L0 work.

## 3. Canonical Files For Continuation

Claude Code and Gemini CLI should read these first:

```text
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\schema.md
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\index.md
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\entities\entity_shadow_l0_executor_mesh.md
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\concepts\concept_agent_capsule.md
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\13_hermes-retrogradation-shadow-l0-20260517.md
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\14_shadow-l0-executor-mesh-codex-strategy-20260517.md
```

## 4. Codex CLI Local Terminal Fix

Issue observed in Antigravity terminal:

```text
shadow_l0_safe: not recognized
codex: not recognized
Not inside a trusted directory and --skip-git-repo-check was not specified.
```

Root cause:

```text
C:\Users\amado\AppData\Local\OpenAI\Codex\bin
```

was not available in that terminal session's `PATH`, the Shadow L0 helper functions were not yet installed in the PowerShell profile, and Codex `exec` still enforces the git/trusted-directory check even when the interactive UI is set to Full Access.

Fix applied:

```text
C:\Users\amado\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

The following functions now exist:

```text
shadow_l0_safe
shadow_l0_exec
shadow_l0_yolo
```

Aliases:

```text
sl0-safe
sl0-exec
sl0-yolo
```

User `PATH` was also updated to include:

```text
C:\Users\amado\AppData\Local\OpenAI\Codex\bin
```

For already-open terminals, run:

```powershell
$env:Path = "C:\Users\amado\AppData\Local\OpenAI\Codex\bin;$env:Path"
. $PROFILE
```

For new terminals, this should load automatically.

All three helper functions include:

```text
--skip-git-repo-check
```

This is required for execution from `C:\Users\amado` or other non-repo control-room directories.

## 5. Codex CLI Profiles

Configured in:

```text
C:\Users\amado\.codex\config.toml
```

Profiles:

```text
shadow_l0_safe  -> workspace-write + approval on-request
shadow_l0_exec  -> workspace-write + approval never
shadow_l0_yolo  -> danger-full-access + approval never
```

Usage:

```powershell
shadow_l0_safe "Summarize the current repo and list risks"
shadow_l0_exec "Run tests and fix deterministic failures"
shadow_l0_yolo "Only inside isolated disposable workspace"
```

Direct usage:

```powershell
codex exec -p shadow_l0_safe --json --cd C:\Users\amado "<mission>"
```

## 6. Claude Code Handoff

Claude Code should treat Hermes as closed and use LLM Wiki as the memory substrate.

Read order:

1. `LLM_Wiki/wiki/schema.md`
2. `LLM_Wiki/wiki/index.md`
3. `LLM_Wiki/wiki/entities/entity_shadow_l0_executor_mesh.md`
4. `LLM_Wiki/wiki/concepts/concept_agent_capsule.md`
5. This handoff file.

Claude Code via MiniMax target:

```text
MiniMax-M2.7
Anthropic-compatible endpoint: https://api.minimax.io/anthropic
```

Secret handling:

```text
Use environment variable names only.
Never print the MiniMax Token Plan key.
If the key was pasted into chat or docs, rotate it.
```

Required operating mode:

```text
Use the Agent Capsule files for identity.
Use Symphony payloads for tasks.
Write proof artifacts back to tracker or LLM Wiki.
Do not require Hermes to be running.
```

## 7. Gemini CLI Handoff

Gemini CLI should act as:

- high-quota scout;
- broad context analyst;
- fallback implementation doer;
- LLM Wiki summarizer/linter when Codex or Claude are quota constrained.

Read order:

1. `LLM_Wiki/wiki/schema.md`
2. `LLM_Wiki/wiki/index.md`
3. `LLM_Wiki/wiki/log.md`
4. `LLM_Wiki/wiki/entities/entity_shadow_l0_executor_mesh.md`
5. `LLM_Wiki/wiki/concepts/concept_agent_capsule.md`

Recommended non-interactive pattern:

```powershell
gemini -p "Read @C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\index.md and summarize Shadow L0 state" --output-format stream-json
```

Safety:

```text
Do not let Gemini write production files without a tracker payload and proof contract.
Prefer analysis/lint/spec compression unless Symphony explicitly dispatches implementation.
```

## 8. Agent Capsule Standard

Agent identities now live as file-based capsules:

```text
Soul.md
Agent.md
Heartbeat.md
Tools.md
Context.md
```

Template:

```text
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\agent_capsules\_TEMPLATE
```

This replaces:

- Hermes runtime identities;
- OpenClaw agent files as live dependency;
- Paperclip AI team/task hierarchy as active runtime.

## 9. Remaining Work

1. Create real capsules for:
   - Codex Shadow L0
   - Gemini Shadow L0
   - Claude Code + MiniMax Shadow L0
   - Rick C137 / Rick Prime split if needed
2. Normalize Gemini CLI settings.
3. Normalize Claude Code + MiniMax local Windows config.
4. Implement heartbeat as file-first protocol, then later automation.
5. Wire Symphony to choose executor profile from payload metadata.

## 10. Validation Proof

Validated by Codex:

```text
codex-cli 0.130.0-alpha.5
context7 MCP enabled
shadow_l0_safe function installed in PowerShell profile
shadow_l0_exec function installed in PowerShell profile
shadow_l0_yolo function installed in PowerShell profile
shadow_l0_safe from C:\Users\amado returns: ok
plaintext_secret_hits=0
```

## 11. Residual Risk

- Existing open terminals need reload or restart before aliases work.
- `shadow_l0_yolo` is dangerous and must be used only in isolated/disposable workspaces.
- Claude Code + MiniMax Windows-local config still needs a dedicated masked setup doc.
- Gemini CLI settings still need normalization.
- Heartbeat is specified, not automated.

*Documente Docs Dogmatique — Final handoff Hermes vers LLM Wiki pour Claude Code et Gemini CLI — 2026-05-17 — Codex*
