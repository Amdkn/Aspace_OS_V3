# posttooluse-skill-pocock-check.ps1
# L0 Skill Creator Reflex hook — ADR-LD01-003 + Plan Lightning L0 §3 (gate b RATIFIED 2026-07-04T23:08 ET).
#
# Mécanise le réflexe Skill Creator : à chaque Write/Edit de SKILL.md dans `**/.claude/skills/**`,
# appelle skill_creator_reflex.py en lecture seule + append le verdict dans
# skill_creator_reflex_log.md.
#
# DESIGN (sober Rick §8 — anti-Ultron §S5) :
#   - fires ONLY on Write|Edit|MultiEdit dont le path match `**/.claude/skills/**/SKILL.md`
#   - skip canon files (`_TRASH`, `_archive`, `agent-os/citadel/`)
#   - skill_creator_reflex.py est lecture-seule sur SKILL.md + append-only log
#   - timeout-capped (30s) — ne peut jamais hang une session
#   - LOG-ONLY : exit 0 toujours (L0 = signale, JAMAIS block — ADR-002 §S5)
#   - si le verdict = FAIL, le hook retourne stdout mais n'interrompt pas le turn
#
# Anti-Ultron check :
#   ✓ lecture seule sur SKILL.md
#   ✓ append-only log (skill_creator_reflex_log.md)
#   ✓ idempotent (re-run safe)
#   ✓ exit 0 always = pas de block
#   ✓ skip canon files + agent-os/
#   ✓ A0 HITL override possible (Tony Stark overruling, traçabilité dans source)
#
# Hook payload: lit stdin JSON (Claude Code PostToolUse hook format) avec tool_input.file_path.

$ErrorActionPreference = 'SilentlyContinue'
$LOG_HOOK = "C:\Users\amado\agent-os\citadel\logs\posttooluse-skill-pocock.log"
$REFLEX_LOG = "C:\Users\amado\agent-os\citadel\logs\skill_creator_reflex_log.md"
$REFLEX_SCRIPT = "C:\Users\amado\agent-os\citadel\tools\skill_creator_reflex.py"
New-Item -ItemType Directory -Force -Path (Split-Path $LOG_HOOK) | Out-Null

function Write-HookReceipt($line) {
  $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
  Add-Content -Path $LOG_HOOK -Value "[$ts] $line" -Encoding UTF8
}

# --- read hook stdin ---
$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { Write-HookReceipt "no-stdin, exit 0"; exit 0 }
try { $hook = $raw | ConvertFrom-Json } catch { Write-HookReceipt "bad-json, exit 0"; exit 0 }

$file = $hook.tool_input.file_path
if ([string]::IsNullOrWhiteSpace($file)) { Write-HookReceipt "no-file-path, exit 0"; exit 0 }

# --- gate 1: seulement les SKILL.md dans .claude/skills/ ---
# matcher path = ...skills/<name>/SKILL.md (sans les _TRASH/, _archive/, agent-os/)
if ($file -notmatch '[\\\/]\.claude[\\\/]skills[\\\/][^\\/]+[\\\/]SKILL\.md$') {
  exit 0
}
# skip _TRASH / _archive (canon retire)
if ($file -match '[\\\/]_(TRASH|archive)[\\\/]') { exit 0 }
# skip le L0 skill creator reflex lui-même (pas récursif)
if ($file -match '[\\\/]agent-os[\\\/]') { exit 0 }

if (-not (Test-Path $file)) { Write-HookReceipt "file-not-found $file"; exit 0 }
if (-not (Test-Path $REFLEX_SCRIPT)) { Write-HookReceipt "reflex-script-missing $REFLEX_SCRIPT"; exit 0 }

# --- invoke skill_creator_reflex.py avec timeout 30s ---
Write-HookReceipt "FIRE skill=$file"
$job = Start-Job -ScriptBlock {
  param($scriptPath, $target)
  $out = & python $scriptPath $target 2>&1 | Out-String
  [pscustomobject]@{ code = $LASTEXITCODE; out = $out }
} -ArgumentList $REFLEX_SCRIPT, $file

if (Wait-Job $job -Timeout 30) {
  $res = Receive-Job $job
  $tail = ($res.out -split "`n" | Select-Object -Last 5) -join ' | '
  if ($res.code -eq 0) {
    Write-HookReceipt "PASS skill=$file  $tail"
  } else {
    Write-HookReceipt "FAIL($($res.code)) skill=$file  $tail"
  }
} else {
  Stop-Job $job
  Write-HookReceipt "TIMEOUT(30s) skill=$file  (capped, hook returned exit 0)"
}
Remove-Job $job -Force

# exit 0 toujours : L0 = signale, JAMAIS block
exit 0