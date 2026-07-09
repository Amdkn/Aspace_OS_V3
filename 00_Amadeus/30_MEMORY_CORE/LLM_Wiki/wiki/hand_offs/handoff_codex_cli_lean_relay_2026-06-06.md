---
source: Codex CLI handoff (post-God-Mode request)
date: 2026-06-06
type: handoff
status: ACTIVE
domain: Shadow_L0 / Codex_CLI / MiniMax / A'Space OS V2
tags: [#CodexCLI, #MiniMax, #LeanRelay, #Hooks, #AspaceOS, #handoff]
---

# Codex CLI Lean Relay Handoff - 2026-06-06

## Why this handoff exists

On 2026-06-06 the user reported that the existing `codexm` profile was slow because the 6 trusted A'Space doctrine hooks (Context7, Skill Reflex, Archive) were injected into every prompt. The MiniMax relay validation run consumed about 23,884 tokens for a trivial "Reply with exactly: OK_MINIMAX" prompt, mostly hooks/plugins/MCPs.

The previous handoff (`handoff_codex_cli_minimax_alignment_2026-06-06.md`) listed this as residual risk. This handoff closes it by introducing a hooks-free, plugins-free, MCP-free CODEX_HOME.

## What changed

### 1. New lean CODEX_HOME at C:\Users\amado\ASpace_OS_V2\.codex-m3-lean

Files:
- `config.toml` - TOML config with no [hooks.state.*], no [plugins.*], no [mcp_servers.*]. Sets model=MiniMax-M3, provider=minimax, model_instructions_file=lean-instructions.md, features.multi_agent=false, features.memories=false, profiles.minimax block, [model_providers.minimax] block.
- `lean-instructions.md` - 6-line instructions that REPLACE the project AGENTS.md. Tells the model to be concise, skip doctrine, only act on explicit requests.
- `README.md` - explains purpose, what is dropped, and maintenance rules. Lean home stays lean.

### 2. PowerShell profile CODEX_MINIMAX block updated

Replaced at `C:\Users\amado\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` (CODEX_MINIMAX:START..END).

Functions exposed:
- `codexm` (alias `codexml`) - sets `$env:CODEX_HOME = C:\Users\amado\ASpace_OS_V2\.codex-m3-lean`, loads MINIMAX_API_KEY (User env first, then Process env fallback), then runs `codex -p minimax -C C:\Users\amado\ASpace_OS_V2`.
- `codexm-f` (alias `codexm-full`) - clears `$env:CODEX_HOME` and runs the full default `~/.codex` home (hooks/plugins/MCPs intact).

Source of truth: file content verified by `Get-Content` after the patch.

## Start commands

Open a new PowerShell window so the updated profile loads.

```powershell
codexm exec --skip-git-repo-check "Reply with exactly: OK_LEAN_MINIMAX"
```

Expected: a single line `OK_LEAN_MINIMAX` with no doctrine context loaded.

## Validation

Inside the Codex CLI host shell, two checks were run:

1. `codex -p minimax exec --skip-git-repo-check "Reply with exactly: OK_LEAN_MINIMAX"` with `$env:CODEX_HOME` pointing at the lean home. The output confirmed the lean profile was loaded (`workdir: C:\Users\amado\ASpace_OS_V2`, `model: MiniMax-M3`, `provider: minimax`, `session id: 019e9d0e-1c44-7213-80a5-6f33e013c906`). The MiniMax API call then failed with `stream disconnected before completion: error sending request for url (https://api.minimax.io/v1/responses)`. Same failure for OpenAI and Google endpoints tested with `Invoke-WebRequest`.

2. `Invoke-WebRequest https://api.minimax.io/v1/models`, `Invoke-WebRequest https://api.openai.com/v1/models`, `Invoke-WebRequest https://www.google.com` all returned `The underlying connection was closed: An unexpected error occurred on a receive`.

Interpretation: the Codex CLI config and the PowerShell wrapper are working; the host shell sandbox is currently blocking outbound HTTPS. The original `OK_MINIMAX` validation from earlier in the day was on a host shell with network access. The end-to-end proof must be re-run from a host shell that has outbound HTTPS to api.minimax.io.

## Residual risks

- The Codex CLI host shell cannot reach api.minimax.io right now. Verify host network policy and re-run `codexm exec --skip-git-repo-check "Reply with exactly: OK_LEAN_MINIMAX"` from a fresh PowerShell window.
- The lean profile disables `[features] memories = false` so Codex will not generate local memories from lean sessions. Codex memories in `~/.codex` are still produced by `codexm-f` / full sessions.
- The `multi_agent = false` toggle in the lean profile prevents `/agent` subagents. Use `codexm-f` when subagent workflows are needed.
- `model_instructions_file` replaces AGENTS.md, so lean sessions do NOT see A'Space doctrine. The user must explicitly state the mission for the session.
- `MINIMAX_API_KEY` must be set in User env or in the parent Process env. If both are empty, `codexm` prints a warning and Codex will error with `Missing environment variable: MINIMAX_API_KEY`.
- The PowerShell profile is unsigned and requires an `ExecutionPolicy` that allows unsigned local scripts on the user machine. If a fresh PowerShell refuses to load the profile, sign it or set `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` once.

## Secret handling

`MINIMAX_API_KEY` is read from the User or Process environment only. No key value is written to `config.toml`, `lean-instructions.md`, the PowerShell profile, the bootstrap memory, the handoff doc, or this log entry. To rotate the key, update `[Environment]::SetEnvironmentVariable("MINIMAX_API_KEY", $newKey, "User")` from an interactive shell; never commit it to git.

## Next safe action

From a fresh PowerShell window with outbound HTTPS to api.minimax.io, run:

```powershell
codexm exec --skip-git-repo-check "Reply with exactly: OK_LEAN_MINIMAX"
```

Then re-measure token count by running the same prompt through `codexm-f` (full) and comparing session JSON output. Target: lean at least 5x smaller than full for the trivial prompt.

## Open follow-up: skill proposal

The lean relay setup is now a 3+ step repeatable workflow (audit config, write lean TOML + instructions, patch PowerShell profile, validate). Consider crystallizing it as a Codex skill `codex-cli-lean-relay` for future relay work. Boundary: only fires when the user names a Codex CLI profile and complains about overhead or quotas. Defer until at least one full validation cycle is observed in the wild.
