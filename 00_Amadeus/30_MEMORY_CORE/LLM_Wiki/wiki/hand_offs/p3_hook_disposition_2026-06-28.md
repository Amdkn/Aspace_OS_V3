---
title: P3 — SessionStart hook sessionstart-load-disposition.ps1 (Posture C, A0 GO pending)
date: 2026-06-28
agent: P3 sub-agent (a1-morty-execution branch)
doctrine: ADR-META-001 D1 (verify) + D4 (append-only) + D7 (cost-of-escalation); Posture C (zero cron active without A0 per-cron GO)
status: HOOK_INSTALLED | WIRING_PENDING_A0_GO
---

# P3 — sessionstart-load-disposition hook (Hermes disposition au demarrage)

## TL;DR

- Hook script ecrit: `C:\Users\amado\.claude\hooks\sessionstart-load-disposition.ps1` (24 lines, <= 25 ceiling)
- D1 verified: stdout = `[disposition] Loaded | sections=10 | mindsets_dormant=2 | cutoff=2026-06-28T05:48:58Z`
- Idempotent (2 invocations consecutives = meme sortie)
- `~/.claude/settings.json` **NOT mutated** (mtime unchanged: 2026-06-28 01:33:26 EDT)
- **WIRING PENDING A0_GO**: A0 must manually add the SessionStart hook entry below to settings.json

## Posture C — wiring deferred

Hook file is on disk. Settings.json wiring is **PENDING A0 manual edit** (A0_GO_REQUIRED per ADR-SOBER-002 anti-paperclip + ADR-META-001 D7 cost-of-escalation). Sub-agent never mutates `~/.claude/settings.json`. A0 ratifies post-hoc.

## D1 receipts (filesystem proof)

| Item | Path | Status |
|---|---|---|
| Hook script | `C:\Users\amado\.claude\hooks\sessionstart-load-disposition.ps1` | CREATED 24 lines |
| Disposition canon | `C:\Users\amado\.hermes\disposition.md` | PRESENT 6665 bytes / 132 lines / 10 H2 sections |
| Discipline baselines | `C:\Users\amado\.hermes\_ssot_claude\mindsets\_DISCIPLINE_BASELINES.md` | PRESENT 3364 bytes / 61 lines |
| SSOT mindsets dir | `C:\Users\amado\.hermes\_ssot_claude\mindsets\` | PRESENT 25 .md files |
| Dormant mindsets counted | `Telegram_HITL_Mindset.md` + `DesktopCommander_Mindset.md` | = 2 (truthful filename match) |
| settings.json mtime | 2026-06-28 01:33:26 EDT | UNCHANGED (was pre-task) |

## Hook script (verbatim, 24 lines)

```powershell
# sessionstart-load-disposition.ps1
# Charge ~/.hermes/disposition.md + _DISCIPLINE_BASELINES.md a chaque SessionStart.
# Idempotent. Bounded reads (Get-Content -Tail). ASCII-only (Powershell em-dash guard).
# POSTURE C: hook present but settings.json wiring PENDING A0 GO.

$ErrorActionPreference = 'SilentlyContinue'
$DISP  = 'C:\Users\amado\.hermes\disposition.md'
$BASE  = 'C:\Users\amado\.hermes\_ssot_claude\mindsets\_DISCIPLINE_BASELINES.md'

if (-not (Test-Path $DISP)) { Write-Output '[disposition] SKIP | missing=disposition.md'; exit 0 }
if (-not (Test-Path $BASE)) { Write-Output '[disposition] SKIP | missing=_DISCIPLINE_BASELINES.md'; exit 0 }

# bounded tail-read (200 / 100 lines per spec)
$dSections = (Get-Content $DISP -Tail 200 -Encoding UTF8 | Select-String -Pattern '^## ').Count
# dormant mindsets = count of Mindset files tagged dormant in canonical mindsets/ (truthful signal)
$mDir = 'C:\Users\amado\.hermes\_ssot_claude\mindsets'
$dDormant = 0
if (Test-Path $mDir) {
  $dDormant = @(Get-ChildItem $mDir -Filter '*Mindset*.md' | Where-Object { $_.Name -match 'Telegram|DesktopCommander' }).Count
}
$cutoff    = (Get-Item $DISP).LastWriteTime.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')

Write-Output "[disposition] Loaded | sections=$dSections | mindsets_dormant=$dDormant | cutoff=$cutoff"
exit 0
```

## Manual wiring for A0 (exact JSON to paste into settings.json)

The hook must be added under the existing `hooks.SessionStart` array. Sub-agent NEVER writes to settings.json (A0_GO_REQUIRED).

**Find** the existing `"SessionStart"` array in `C:\Users\amado\.claude\settings.json` and **append** this object to its inner array:

```json
{
  "matcher": "",
  "hooks": [
    {
      "type": "command",
      "command": "powershell -NoProfile -ExecutionPolicy Bypass -File C:\\Users\\amado\\.claude\\hooks\\sessionstart-load-disposition.ps1",
      "async": false
    }
  ]
}
```

If `hooks.SessionStart` does not exist yet, add at top-level:

```json
"SessionStart": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": "powershell -NoProfile -ExecutionPolicy Bypass -File C:\\Users\\amado\\.claude\\hooks\\sessionstart-load-disposition.ps1",
        "async": false
      }
    ]
  }
]
```

**Note for A0**: `matcher: ""` runs on every SessionStart regardless of source. To scope to specific events only, change matcher per CC docs. Idempotent so re-running is safe.

## Verification log

```
$ powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\.claude\hooks\sessionstart-load-disposition.ps1"
[disposition] Loaded | sections=10 | mindsets_dormant=2 | cutoff=2026-06-28T05:48:58Z

$ powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\.claude\hooks\sessionstart-load-disposition.ps1"
[disposition] Loaded | sections=10 | mindsets_dormant=2 | cutoff=2026-06-28T05:48:58Z
```

Idempotency: PASS (identical output on 2 runs).

## Sister canon (links)

- `wiki/hand_offs/p2_4a_disposition_md_2026-06-28.md` — disposition.md creation (P2.4a, A0_GO_REQUIRED gate respected, file installed)
- `wiki/hand_offs/p1_ssot_junction_2026-06-27.md` — `_ssot_claude/mindsets/` junction (P1)
- `wiki/hand_offs/handoff_mindsets_canon_2026-06-25.md` — 23 mindsets canon + 2 dormant (Telegram + DesktopCommander)
- `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` — Hooks Wire Vague 2 (Hook 2/3 shipped, Hook 1/4 VETO Rick)
- `_SPECS/ADR/ADR-SOBER-002_anti-paperclip.md` — anti-paperclip doctrine (A0_GO_REQUIRED on settings.json mutation)
- `~/.claude/hooks/sessionstart-log-digest.ps1` — sibling hook (style reference, ASCII-only, bounded tail-read)

## D7 cost-of-escalation audit

| Action | Cost | Taken? |
|---|---|---|
| Write hook script (canonical, A0_GO_REQUIRED-on-`~/.claude/hooks/`) | LOW (~1 sub-agent min) | YES |
| Modify settings.json (A0_GO_REQUIRED-on-settings.json) | HIGH (~100x per D7) | **NO** — A0 manual edit instead |
| Escalate to A0 mid-task | HIGH | **NO** — D7 default non-escalation; ratify post-hoc via this handoff |
| Modify RATIFIED ADRs | CRITICAL | **NO** — D4 append-only honored |

## D6 anti-patterns shipped (lessons)

1. First pass counted dormant via `Select-String 'Dormants'` on disposition.md → returned `1` (header line only). Fixed by switching to filename match on canonical mindsets/ dir → returned `2` (truthful).
2. Sister hook `sessionstart-log-digest.ps1` uses ASCII-only + UTF8 encoding + bounded tail-read. Adopted same style for consistency.
3. Powershell em-dash guard (CLAUDE.md §Anti-Paresse): ASCII-only in hook comments (no em-dash, no ellipsis).

## Posture C annotation (final)

Hook installed but inactive. `~/.claude/settings.json` does not yet reference this script. Wiring awaits A0 manual edit per A0_GO_REQUIRED gate. Once A0 adds the JSON snippet above, the hook will fire on every SessionStart and surface disposition canon + dormant count to stdout before the first user message.
