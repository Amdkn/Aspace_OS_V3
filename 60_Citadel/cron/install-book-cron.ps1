<#
install-book-cron.ps1 — Book COO Loop Engineering cron installer (P3 NEW).

Per Plan L2 Dark Factory §3.4 + §6 MiroFish gouverneur compression :
- Wake Book COO sur chaque boundary Triptyque pour maintenir Loop Engineering Report visible

GATING (FREIN À MAIN ACTIF — Posture C strict, A0 HITL required pour enable) :
- REFUSE d'installer le scheduled task sans le flag `decisions/enable_book_loop.flag`
- L'install est un changement d'état système (Windows Task Scheduler)

Usage :
  # Désactivé par défaut. Pour activer :
  #   New-Item -ItemType File "decisions/enable_book_loop.flag"
  #   .\install-book-cron.ps1 -Install
  #   .\install-book-cron.ps1 -Uninstall
  #   .\install-book-cron.ps1 -Status
  #   .\install-book-cron.ps1 -RunOnce   # run sans installer scheduled task (testing)

Date : 2026-07-05 · Auteur : Mavis (MC/L1) — A0 GO "créer le Cron de Book"
Source : plan-l2-dark-factory-book-coo-compression-12wy.md §10
Sister : LD01/99_meta/plan_l2_dark_factory_sister.md §10-§11
#>
[CmdletBinding()]
param(
  [switch]$Install,
  [switch]$Uninstall,
  [switch]$Status,
  [switch]$RunOnce,
  [int]$EveryHours = 4
)

$ErrorActionPreference = "Stop"
$CitadelRoot = $PSScriptRoot | Split-Path -Parent
$Flag = Join-Path $CitadelRoot "decisions" "enable_book_loop.flag"
$TaskName = "CitadelleBookLoopEng"
$ScriptPath = Join-Path $CitadelRoot "cron" "book_loop.py"
$LogFile = Join-Path $CitadelRoot "logs" "book_loop_cron.log"
$null = New-Item -ItemType Directory -Force -Path (Split-Path $LogFile)

function Write-BookLoopLog {
  param([string]$Message, [string]$Level = "INFO")
  $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
  $line = "$ts [$Level] [book_loop_cron] $Message"
  Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
  Write-Host $line
}

function Require-Flag {
  # 12WY-ON-PAUSE check FIRST — Tony Stark pré-ratification cycle 12 sem (2026-07-05 → 2026-09-27)
  $twelveWy = Join-Path $CitadelRoot "decisions" "12WY_ON_PAUSE.flag"
  if (Test-Path $twelveWy) {
    Write-BookLoopLog "12WY-ON-PAUSE ACTIVE — bypassing individual gate (Tony pré-ratification)"
    return
  }
  if (-not (Test-Path $Flag)) {
    Write-BookLoopLog "REFUSED: missing $Flag — A0 HITL gate required (Posture C — no cron without GO)"
    Write-Host ""
    Write-Host "Pour activer Book Loop cron :"
    Write-Host "  New-Item -ItemType File '$Flag'"
    Write-Host ""
    exit 2
  }
}

if ($Status) {
  $flagExists = Test-Path $Flag
  $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
  Write-Host "GATE enable_book_loop.flag: $(if ($flagExists) { 'ENABLED' } else { 'DISABLED (default — Posture C)' })"
  Write-Host "Task scheduled: $(if ($task) { $task.TaskName + ' (every ' + $EveryHours + 'h)' } else { 'NOT INSTALLED' })"
  Write-Host "Last report: $(Get-ChildItem (Join-Path $CitadelRoot 'cron' 'output') -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Select-Object Name)"
  exit 0
}

if ($RunOnce) {
  Write-BookLoopLog "RunOnce (no scheduled task install — testing mode)"
  & python $ScriptPath
  exit $LASTEXITCODE
}

if ($Uninstall) {
  try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction Stop
    Write-BookLoopLog "uninstalled scheduled task $TaskName"
  } catch {
    Write-BookLoopLog "no task to uninstall ($($_.Exception.Message))" "WARN"
  }
  exit 0
}

if ($Install) {
  Require-Flag
  Write-BookLoopLog "installing scheduled task $TaskName — every ${EveryHours}h"
  $action = New-ScheduledTaskAction -Execute "python" -Argument "`"$ScriptPath`"" -WorkingDirectory (Join-Path $CitadelRoot "cron")
  $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) `
    -RepetitionInterval (New-TimeSpan -Hours $EveryHours) `
    -RepetitionDuration (New-TimeSpan -Days 365)
  $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
  $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 5)
  Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings `
    -Description "Book COO Loop Engineering Meta Harness Engineering cron (every ${EveryHours}h). Per Plan L2 Dark Factory §3.4 + §10. Anti-Ultron: lecture seule sources canoniques + append-only output. /ship JAMAIS automatique."
  Write-BookLoopLog "INSTALLED $TaskName — gated by enable_book_loop.flag"
  exit 0
}

Write-Host "Book Loop Engineering cron installer — gated by enable_book_loop.flag"
& $PSCommandPath -Status