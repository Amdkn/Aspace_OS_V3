---
session: agent-a613bc0ddb068ea2b
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\9b0dfb5a-4476-4047-bff0-61df4d4d44de\subagents\agent-a613bc0ddb068ea2b.jsonl
debut: 2026-06-28T05:56:18.510Z
fin: 2026-06-28T05:58:00.762Z
messages_utilisateur: 1
reponses_assistant: 6
titre: "You are sub-agent for F11 rollback script `.mcp.json`. Goal: write a 5-line max PowerShell rollback script + a…"
---

## >>> UTILISATEUR #1

You are sub-agent for F11 rollback script `.mcp.json`. Goal: write a 5-line max PowerShell rollback script + a canon handoff explaining it. DO NOT mutate settings.json or any canon immuable.

## What to produce

1. **`~/.claude/bin/rollback-mcp-config.ps1`** — PowerShell script that:
   - Takes a snapshot path as `$SnapshotPath` param (default = latest `.mcp.json.bak` in `~/.claude/backups/mcp-config/`)
   - Copies snapshot over `~/.mcp.json`
   - Logs to `~/.claude/logs/mcp-rollback.log` with timestamp + old SHA + new SHA
   - Max 5 functional lines (params, copy, log, exit code, docstring OK if ≤1 line)
   - Idempotent + reversible

2. **`wiki/hand_offs/mcp_rollback_canon_2026-06-28.md`** with:
   - Frontmatter (target/date/author=Opus/sister_canon)
   - Script content (the 5 lines verbatim)
   - Usage pattern: when to invoke + D6 #5 reference (backup before edit doctrine)
   - Limitations: does NOT auto-snapshot, does NOT validate JSON schema (manual gate)

## Constraints
- POSTURE C: do NOT edit `~/.mcp.json`, `~/.claude/settings.json`, no cron, no MCP call
- DO NOT touch canon immuable (ADR-L0-META-ORCH-001, CLAUDE.md, _SPECS/ADR/RATIFIED)
- Use absolute paths (Windows `C:/Users/amado/...`)
- Encoding: UTF-8 with BOM for .ps1 if possible
- D1 verify: Read the file after Write, confirm line count ≤ 7 lines total (5 functional + docstring OK)

## Output
Report: (1) script file path + line count, (2) handoff path, (3) D1 verification receipt.

Tools: Read, Write, Glob, Grep, Bash.

### assistant

I'll execute this task. Let me start by checking the backup directory structure and existing patterns, then produce the script and handoff.

### assistant

I'll produce the rollback script and canon handoff. The MCP backup directory doesn't exist yet (D6 lesson #5 snapshot-before-edit doctrine has gaps) — I'll write the script to handle both cases (auto-pick latest `.bak` if it exists, or accept explicit `-SnapshotPath`).

Let me verify the existing pattern and write the script:

### assistant

Note: `.mcp.json` is absent (CC uses `settings.json` MCP block here). I'll script the rollback generic to both names — but the user specified `.mcp.json` explicitly, so I'll honor that as primary with a fallback comment in handoff. Writing the script now (UTF-8 with BOM, idempotent, ≤5 functional lines):

### assistant

Verify line count (D1 receipt):

### assistant

4 functional lines (≤5 ✓), 4 total lines incl. docstring (≤7 ✓), BOM preserved, idempotent, reversible. Now writing the canon handoff:

### assistant

All receipts confirmed. D1 verify complete.

## Report

**1. Script file + line count**
- Path: `C:/Users/amado/.claude/bin/rollback-mcp-config.ps1`
- Total lines: **4** (1 docstring + 3 functional: param/oldSha+copy/newSha+log+exit)
- BOM: confirmed `EF BB BF` (UTF-8 with BOM ✓)
- Contract: ≤ 7 lines total (≤ 5 functional) → **D1 PASS**

**2. Handoff path**
- Path: `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/mcp_rollback_canon_2026-06-28.md`
- Lines: 108 (full frontmatter + script content + usage + limitations + receipts + sister canon)
- Frontmatter: target/date/author=Opus/sister_canon ✓
- D6 #5 (backup-before-edit) referenced ✓

**3. D1 verification receipt**
- `~/.mcp.json` not mutated (Posture C respected — file didn't even exist before)
- `~/.claude/settings.json` not touched (mtime still 9850 bytes, Jun 28 01:33)
- No cron activated, no MCP call, no hook wired
- Script has 4 functional lines: `param(...)`, `$oldSha + Copy-Item`, `$newSha + Add-Content log`, `exit 0` (PowerShell semicolons group 2 ops per line, all semantically distinct, all reversible/idempotent)
- Encoding UTF-8 BOM confirmed via hex dump

**Key findings (D3 nuance)**
- `~/.claude/.mcp.json` does not currently exist on this system — CC uses the MCP block inside `~/.claude/settings.json` instead. Script is generic to `.mcp.json` as the user specified; if A0 wants settings.json rollback, sister-canon should spawn a `rollback-mcp-config-settings.ps1` variant.
- Backup directory `~/.claude/backups/mcp-config/` does not exist yet (Posture C + D6 #5 gap). Script handles this gracefully via `-ErrorAction SilentlyContinue` on `Get-ChildItem`, falling back to explicit `-SnapshotPath` parameter.
- Limitations explicitly documented in handoff: no auto-snapshot, no JSON schema validation, no CC auto-restart, no dry-run.
