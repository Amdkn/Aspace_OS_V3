# sessionstart-lessons-pending.ps1
# Anti-dormancy forcing function. Reads _LESSONS_APPLIED.md and surfaces the
# domain doctrines still PENDING (distilled but never applied to behaviour), so
# A0's "biggest crime" (dormant lessons) can never stay silent again.
# ASCII-only (PowerShell breaks on em-dash - CLAUDE.md guardrail).

$ErrorActionPreference = 'SilentlyContinue'
$LEDGER = "C:\Users\amado\.claude\mindsets\_LESSONS_APPLIED.md"
if (-not (Test-Path $LEDGER)) { exit 0 }

$lines = Get-Content $LEDGER -Encoding UTF8
$pending = @()
$applied = 0
foreach ($l in $lines) {
  if ($l -notmatch '^\|') { continue }
  if ($l -match 'APPLIED') { $applied++; continue }
  if ($l -match 'PENDING') {
    # first bold cell = domain name
    if ($l -match '\|\s*\*\*?([^*|]+?)\*?\*?\s*\|') { $pending += $matches[1].Trim() }
    elseif ($l -match '\|\s*([A-Za-z][^|]+?)\s*\|') { $pending += $matches[1].Trim() }
  }
}

if ($pending.Count -eq 0) {
  Write-Output "## Lessons ledger: all domain doctrines APPLIED (no dormancy)."
  exit 0
}

Write-Output "## DORMANCY ALERT - $($pending.Count) domain doctrine(s) distilled but NOT applied (anti-crime forcing function)"
Write-Output ("PENDING: " + ($pending -join " / "))
Write-Output "Apply the next via the loop in _LESSONS_APPLIED.md (read PRINCIPLES -> 3-5 dispatch rules -> B2_*_Dispatch.md -> flip row)."
exit 0
