---
source: Shadow_L0
date: 2026-05-17
type: agent-capsule
agent: Codex_CLI
tags: [#AgentCapsule, #Codex, #Context]
---

# Context

## Current State

Codex CLI is the default local implementation executor for Shadow L0.

Known local wrappers live in the Windows PowerShell profile:

`C:\Users\amado\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`

2026-06-06 relay state:

- Codex CLI has a frugal MiniMax profile in `C:\Users\amado\.codex\config.toml`.
- Launch with `codexm` (which wraps `codex -p minimax -C C:\Users\amado\ASpace_OS_V2`).
- Provider: `minimax`; model: `MiniMax-M3`; base URL: `https://api.minimax.io/v1`.
- Secret source: `MINIMAX_API_KEY` environment variable only.
- Validation proof: `codexm exec --skip-git-repo-check "Reply with exactly: OK_MINIMAX"` returned `OK_MINIMAX`.
- Codex memories are enabled, but Memory Core and LLM Wiki remain canonical.

## Memory Anchors

- `30_MEMORY_CORE/README.md`
- `Shadow_L0/README.md`
- `LLM_Wiki/wiki/index.md`
- `LLM_Wiki/wiki/log.md`
- `LLM_Wiki/wiki/hand_offs/handoff_codex_cli_minimax_alignment_2026-06-06.md`

## Handoff Notes

When a decision becomes durable, update LLM Wiki rather than Hermes.

For quota-pressure relays, read:

1. `C:\Users\amado\.codex\memories\ASPACE_OS_CODEX_BOOTSTRAP.md`
2. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\README.md`
3. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`

Then use `$shadow-l0-handoff-brief` and keep secrets out of the transcript.
