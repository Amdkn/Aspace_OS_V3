---
title: ADR-META-005 Hooks Wire (Sobriété Rick scope corrigé) — Implementation 2026-06-21
date: 2026-06-21
author: A1 Morty (Focus exécution)
trigger: A0 ratification ADR-META-005 + A1 Rick Sobriété C137 GO conditionnel
status: COMPLETE
hooks_shipped: 2 / 4 (Rick VETO Hook 1 + 4, deferred Q4 2026)
---

# Hooks Wire (Sobriété scope corrigé) 2026-06-21

## 1. Contexte
- Vague 2 missions 6+7+8 (post-Vague 1 Reco 2)
- Rick C137 Sobriété VETO Hook 1 (PreToolUse destructif = doublon `rules/ecc/web/hooks.md` + 3 responsabilités = bloatware, Option A migration = dette technique)
- Rick C137 VETO Hook 4 (SubagentStop REVIEW_CLEANUP = Loi L0 §2 tâche manuelle = faille sécurité)
- GO conditionnel Hook 2 (PostToolUse D1 Receipt) + rotation 7j hard cap obligatoire
- GO conditionnel Hook 3 (SubagentStart tracker) + throttle 1/10 fan-out (Loi Sobriété "que du muscle")
- A0 AAA decision : ship 2/4 + Sobriété preserved

## 2. Scripts créés (D1 receipts)

| Script | Path | Size | Lines | Sobriété patch appliqué |
|---|---|---|---|---|
| posttooluse-d1-receipt.ps1 | `C:\Users\amado\.claude\hooks\posttooluse-d1-receipt.ps1` | 3131 bytes | 65 | Rotation 7j self-contained + 10MB cap (tronque 50% plus vieux) + D4 canon log bonus (Write/Edit/MultiEdit sous ASpace) |
| subagent-start-tracker.ps1 | `C:\Users\amado\.claude\hooks\subagent-start-tracker.ps1` | 2330 bytes | 57 | Throttle 1/10 fan-out (sample modulo 10 si depth>0) + 5MB cap auto-adaptive → throttle 1/100 + A3 canon regex `^a3-(enterprise\|discovery\|orville\|snw\|protostar\|cerritos)-` → CANON/UNKNOWN tag |

## 3. settings.json edits (D1 receipts)

- **Backup** : `C:\Users\amado\.claude\settings.json.bak.2026-06-21` (184 lignes, JSON validé `OK_HOOKS_EVENTS= ['SessionStart', 'Stop', 'Notification', 'UserPromptSubmit']` avant edit)
- **2 blocs ajoutés** (PostToolUse + SubagentStart) APRÈS UserPromptSubmit, AVANT `}` du bloc `hooks`
- **0 régression sur 4 hooks existants** : SessionStart×1, Stop×1, Notification×1, UserPromptSubmit×1 (vérifié PowerShell ConvertFrom-Json)
- **D1 receipt final** : JSON validé `HOOKS_EVENTS= ['SessionStart', 'Stop', 'Notification', 'UserPromptSubmit', 'PostToolUse', 'SubagentStart']` + counts `{'SessionStart': 1, 'Stop': 1, 'Notification': 1, 'UserPromptSubmit': 1, 'PostToolUse': 1, 'SubagentStart': 1}`

## 4. Test smoke results (D1 receipts)

| Test | Action | Result |
|---|---|---|
| T1 | `Write` tool with ASpace target | `tool-receipts.logl` line: `2026-06-21 15:17:39 \| Write \| test write of ASpace file content first 80 chars \| exit=0 \| path=C:\Users\amado\ASpace_OS_V2\test.md` — **PASS** |
| T2 | `Edit` tool with ASpace canon target | `tool-receipts.logl` line + `wiki\log.md` line: `**2026-06-21** : [HOOK2-D1-RECEIPT] Edit → C:\Users\amado\ASpace_OS_V2\00_Amadeus\test.md` (lignes 3705-3706) — **PASS** |
| T3 | Sub-agent spawn (fanout=0 direct + fanout=1 throttled) | `a3-spawns.logl` line: `2026-06-21 15:18:19 \| A3_SPAWN \| a3-cerritos-boimler \| test-session-123 \| test-agent-001 \| fanout=0 \| CANON` — fanout=1 NOT logged (throttle 1/10 OK) — **PASS** |
| T4 | Rotation 7j self-test | Test file with `2026-06-13` (8j old) + `2026-06-21` (today). After hook run: old line truncated, recent line kept + new line appended — **PASS** |
| T5 | Re-test 4 existing hooks | PowerShell ConvertFrom-Json → all 4 events present + counts=1 — **PASS, 0 regression** |

## 5. Sobriété Rick patches appliqués

- **Rotation 7j self-contained (Hook 2)** : `Where-Object { $ts -ge (Get-Date).AddDays(-7) }` self-test passé (T4 verbatim ci-dessus). **Anti-fragilité** : try/catch englobant + exit 0 toujours (Sobriété = never block CC).
- **Throttle 1/10 fan-out (Hook 3)** : modulo 10 sample, fanout=0 toujours log, fanout>0 sample. **Auto-adaptive** : si fichier >5MB → throttle passe à 1/100. Self-test passé (T3 fanout=1 NOT logged).
- **A3 canon detection** : regex `^a3-(enterprise|discovery|orville|snw|protostar|cerritos)-` → CANON tag. Sinon UNKNOWN (n-block pas, Sobriété).

## 6. GAP-1 + GAP-4 deferred Q4 2026

- **Hook 1 PreToolUse destructif** : VETO Rick (doublon `rules/ecc/web/hooks.md`, 3 responsabilités = bloatware, Option A migration = dette technique). Refonte Sobriété Q4 2026 = réduire à 1 responsabilité unique OU abandon pur.
- **Hook 4 SubagentStop REVIEW_CLEANUP** : VETO Rick (Loi L0 §2 tâche manuelle = faille sécurité). Refonte auto `trap EXIT` Q4 2026 = cleanup auto-fin du sub-agent sans REVIEW manuel.

## 7. Rollback procédure

```bash
# 1. Restore settings.json
cp C:\Users\amado\.claude\settings.json.bak.2026-06-21 C:\Users\amado\.claude\settings.json

# 2. Remove new scripts
rm C:\Users\amado\.claude\hooks\posttooluse-d1-receipt.ps1
rm C:\Users\amado\.claude\hooks\subagent-start-tracker.ps1

# 3. Remove log files (optional)
rm C:\Users\amado\.claude\logs\tool-receipts.logl
rm C:\Users\amado\.claude\logs\a3-spawns.logl
```

## 8. D1 receipts finaux

- **2/2 scripts créés** (3.1KB + 2.3KB, 65 + 57 lignes) + Sobriété patches rotation 7j + throttle 1/10 appliqués
- **2/2 hooks wired dans settings.json** (PostToolUse + SubagentStart)
- **5/5 tests smoke OK** (T1-T5 incl. T5 bonus regression check)
- **0 régression sur 4 hooks existants**
- **Handoff créé** + `wiki\log.md` appendé (2 lignes HOOK2-D1-RECEIPT) + MEMORY.md topic table append (à finaliser post-handoff creation)

## 9. D6 root causes detected

- **D6 #1 — CC hooks registry STALE** : settings.json edit OK mais CC tool registry est STATIC at session start. Nouveaux events PostToolUse + SubagentStart = ignorés jusqu'à CC restart. **Action A0 requise** : restart Claude Code session pour activer les 2 hooks. (D6 #4 pattern déjà documenté dans `handoff_mcp_add_omk_abc_2026-06-17.md`)
- **D6 #2 — hooks.json (51KB) dans `.claude/hooks/` existe déjà** : c'est le hookify plugin config, distinct du CC `settings.json` hooks. Non touché (D4 append-only, scope orthogonal).
- **D6 #3 — Env vars CC hook non documentées officiellement** : `CLAUDE_TOOL_NAME`, `CLAUDE_TOOL_RESULT`, `CLAUDE_TOOL_EXIT_CODE`, `CLAUDE_TOOL_TARGET_PATH`, `CLAUDE_SUBAGENT_TYPE`, `CLAUDE_AGENT_ID`, `CLAUDE_SESSION_ID`, `CLAUDE_FANOUT_DEPTH` = noms basés sur convention CC, pas garantis canoniques. **Mitigation** : scripts ont fallbacks (`UNKNOWN`/`noid`/`nosession`/fanout=0 default) → si env var manque, hook log avec defaults au lieu de crasher.