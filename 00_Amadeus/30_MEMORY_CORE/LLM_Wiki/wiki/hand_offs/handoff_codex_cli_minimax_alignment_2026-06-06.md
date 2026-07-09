---
source: Codex Desktop
date: 2026-06-06
type: handoff
status: ACTIVE
domain: Shadow_L0 / Codex_CLI / MiniMax / A'Space OS V2
tags: [#CodexCLI, #MiniMax, #ShadowL0, #AspaceOS, #handoff]
---

# Codex CLI MiniMax Alignment Handoff - 2026-06-06

## Purpose

Prepare Codex CLI as a frugal relay for A'Space OS V2 work when Codex Desktop
or Claude Desktop quotas become constrained.

## Runtime

- Canonical project root: `C:\Users\amado\ASpace_OS_V2`
- Codex home: `C:\Users\amado\.codex`
- Frugal profile: `codex -p minimax`
- Model: `MiniMax-M3`
- Provider: `minimax`
- Base URL: `https://api.minimax.io/v1`
- Secret storage: `MINIMAX_API_KEY` environment variable only
- Codex memories: enabled in `C:\Users\amado\.codex\config.toml`

## Evidence

- Official MiniMax Codex Token Plan documentation:
  `https://platform.minimax.io/docs/token-plan/codex`
- Local Codex provider config accepted by `codex -p minimax exec`.

## Start Commands

The new official PowerShell alias `codexm` has been created in the PowerShell profiles:
```powershell
codexm
```
This is a wrapper function equivalent to:
```powershell
$env:MINIMAX_API_KEY = [Environment]::GetEnvironmentVariable("MINIMAX_API_KEY","User")
codex -p minimax -C C:\Users\amado\ASpace_OS_V2
```

Validation command:

```powershell
codexm exec --skip-git-repo-check "Reply with exactly: OK_MINIMAX"
```

Observed proof: the MiniMax profile returned `OK_MINIMAX` via `codexm` on 2026-06-06.

## Bootstrap Read Order

1. `C:\Users\amado\.codex\memories\ASPACE_OS_CODEX_BOOTSTRAP.md`
2. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md`
3. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\index.md`
4. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`
5. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\README.md`
6. `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\agents\Codex_CLI\Context.md`

## Operating Doctrine

- Use `C:\Users\amado\ASpace_OS_V2`; never create an apostrophe variant.
- LLM Wiki is durable memory; Codex memories are local operational reminders.
- Codex CLI is the local implementation and verification harness.
- Use `$shadow-l0-handoff-brief` when state is unclear or after quota pressure.
- Use `$archive-and-document` before archival, deprecation, or final handoff.
- Never write API key values into docs, commits, memory, logs, or chat.

## Current Known State

- Hermes official Nous runtime was migrated to MiniMax-M3 locally and on the VPS
  per LLM Wiki log 2026-06-06.
- Claude Code CLI has a separate MiniMax relay handoff.
- Codex CLI now has its own MiniMax relay profile.
- Residual warning: Codex may warn that `MiniMax-M3` is unknown model metadata;
  the provider call still works.
- Residual warning: a fresh shell may need to reload `MINIMAX_API_KEY` from the
  user environment before invoking `codex -p minimax`.
- Residual warning: the validation run loaded local hooks/plugins and reported
  about 23,884 tokens for a tiny prompt. For strict frugality, a lean relay
  launcher should reduce nonessential hooks/plugins before long batches.
- Residual warning: nonblocking local warnings appeared for plugin cache access,
  missing `legacy_notify`, unsupported PowerShell shell snapshot, and some skill
  icon metadata.

## Next Safe Action

Open a new Codex CLI relay session with:

```powershell
codex -p minimax -C C:\Users\amado\ASpace_OS_V2
```

Then ask it to read the bootstrap and run `$shadow-l0-handoff-brief`.
