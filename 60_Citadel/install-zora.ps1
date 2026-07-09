<#
install-zora.ps1 — Zora nightly cron installer (P3 backend).

Per Plan Citadelle §6 + §11 : LE cron (1 cron, 1×/nuit, lecture seule, sortie 1 fichier).
Posture C strict : no cron without GO A+.

GATING (FREIN À MAIN) : ce script REFUSE de s'installer sans le flag
  decisions/enable_zora.flag
posé par A0 HITL explicite.

Usage :
  # Désactivé par défaut. Pour activer :
  #   New-Item -ItemType File "decisions/enable_zora.flag"
  #   .\install-zora.ps1 -Install
  #   .\install-zora.ps1 -Uninstall

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P3 backend
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §6 + §11
#>
[CmdletBinding()]
param(
  [switch]$Install,
  [switch]$Uninstall,
  [switch]$Status,
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$CitadelRoot = $PSScriptRoot | Split-Path -Parent
$Flag = Join-Path $CitadelRoot "decisions" "enable_zora.flag"
$TaskName = "CitadelleZoraNightly"
$ScriptPath = Join-Path $CitadelRoot "cron" "zora-nuit.py"
$LogFile = Join-Path $CitadelRoot "logs" "zora.log"
$null = New-Item -ItemType Directory -Force -Path (Split-Path $LogFile)

function Write-ZoraLog {
  param([string]$Message, [string]$Level = "INFO")
  $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
  $line = "$ts [$Level] [zora-install] $Message"
  Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
  Write-Host $line
}

function Require-Flag {
  # 12WY-ON-PAUSE check FIRST — Tony Stark pré-ratification cycle 12 sem (2026-07-05 → 2026-09-27)
  $twelveWy = Join-Path $CitadelRoot "decisions" "12WY_ON_PAUSE.flag"
  if (Test-Path $twelveWy) {
    Write-ZoraLog "12WY-ON-PAUSE ACTIVE — bypassing individual gate (Tony pré-ratification)"
    return
  }
  if (-not (Test-Path $Flag)) {
    Write-ZoraLog "REFUSED: missing $Flag — A0 HITL gate required (Posture C — no cron without GO)"
    Write-Host ""
    Write-Host "Pour activer le cron Zora :"
    Write-Host "  New-Item -ItemType File '$Flag'"
    Write-Host ""
    exit 2
  }
}

if ($Status) {
  $flagExists = Test-Path $Flag
  $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
  Write-Host "GATE enable_zora.flag: $(if ($flagExists) { 'ENABLED' } else { 'DISABLED (default — Posture C)' })"
  Write-Host "Task scheduled: $(if ($task) { $task.TaskName } else { 'NOT INSTALLED' })"
  Write-Host "Last output: $(Get-ChildItem (Join-Path $CitadelRoot 'cron' 'output') -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Select-Object Name)"
  exit 0
}

if ($DryRun) {
  Write-Host "Zora dry run (Posture C permissive — does NOT touch schedule) :"
  & python $ScriptPath --dry-run
  exit 0
}

if ($Uninstall) {
  try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction Stop
    Write-ZoraLog "uninstalled scheduled task $TaskName"
  } catch {
    Write-ZoraLog "no task to uninstall ($($_.Exception.Message))" "WARN"
  }
  exit 0
}

if ($Install) {
  Require-Flag
  Write-ZoraLog "installing scheduled task $TaskName — 1×/nuit à 02:00 ET"
  $action = New-ScheduledTaskAction -Execute "python" -Argument "`"$ScriptPath`"" -WorkingDirectory (Join-Path $CitadelRoot "cron")
  $trigger = New-ScheduledTaskTrigger -Daily -At "02:00"
  $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
  $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
  Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Zora nightly digest (1×/nuit 02:00 ET, 4 recos max, append-only). Per Plan Citadelle §6."
  Write-ZoraLog "INSTALLED $TaskName — gated by enable_zora.flag"
  exit 0
}

Write-Host "Zora nightly install — gated by enable_zora.flag"
& $PSCommandPath -Status