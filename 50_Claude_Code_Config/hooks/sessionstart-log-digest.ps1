# sessionstart-log-digest.ps1
# "Lecture intelligente" of canon wiki/log.md at session start.
# The file is 360KB+/3700+ lines and full of machine-tick noise, so we NEVER cat
# it. We tail a window, drop the high-frequency automation lines, and surface only
# the last few MEANINGFUL entries, hard-capped so context can never explode.
# ASCII-ONLY (PowerShell breaks on em-dash / ellipsis - CLAUDE.md guardrail).

$ErrorActionPreference = 'SilentlyContinue'
$LOG = "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md"
if (-not (Test-Path $LOG)) { exit 0 }

# tail window only (bounded read)
$tailWindow = 400
$lines = Get-Content $LOG -Tail $tailWindow -Encoding UTF8

# noise filter: symphony ticks, owner patches, raw HTTP, stderr spam, separators
$noise = 'TICK|OWNER (PATCH|POST)|HTTP \d{3}|stderr:|polled=|A1:.*A2:.*A3:'
$signal = $lines | Where-Object { $_ -notmatch $noise -and $_.Trim() -ne '' }

# keep the last 12 meaningful lines, truncate each to 200 chars
$keep = $signal | Select-Object -Last 12 | ForEach-Object {
  if ($_.Length -gt 200) { $_.Substring(0,200) + '...' } else { $_ }
}

if (-not $keep) { exit 0 }

Write-Output "## wiki/log.md smart digest (curated signal, last 12 of $tailWindow tail)"
$keep | ForEach-Object { Write-Output $_ }
Write-Output "## (full canon log = 3700+ lines; tail-read only, never cat)"

# isolated per-turn journal: last 8 lines for session continuity (bounded)
$JOURNAL = "C:\Users\amado\.claude\logs\turn-journal.md"
if (Test-Path $JOURNAL) {
  $jt = Get-Content $JOURNAL -Tail 8 -Encoding UTF8 | ForEach-Object {
    if ($_.Length -gt 200) { $_.Substring(0,200) + '...' } else { $_ }
  }
  if ($jt) {
    Write-Output ""
    Write-Output "## turn-journal.md (last 8 per-turn auto-entries, isolated from canon)"
    $jt | ForEach-Object { Write-Output $_ }
  }
}
exit 0
