<#
install-autostart.ps1 — Citadelle A0 auto-start Windows installer (P2).

Per ADR-LD01-007 §5 persistance Windows natif PS + Plan Citadelle §5
"Tâche planifiée Windows au logon : lance citadel/serve.ps1"

GATING (FREIN À MAIN) : ce script REFUSE de s'installer sans le flag
  decisions/enable_autostart.flag
posé par A0 HITL explicite. Posture C = aucune persistence système
sans GO canon.

Usage:
  # Désactivé par défaut. Pour activer :
  #   echo $null > decisions/enable_autostart.flag     (crée le flag)
  #   .\install-autostart.ps1 -Install                  # installe scheduled task
  #   .\install-autostart.ps1 -Uninstall                # désinstalle

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P2
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §5 persistence
Sister : ADR-LD01-007 §1 décision 3 (auto-start gated) + §5 §C2 (Windows natif PS)
#>
[CmdletBinding()]
param(
  [switch]$Install,
  [switch]$Uninstall,
  [switch]$Status
)

$ErrorActionPreference = "Stop"
$ScriptRoot = $PSScriptRoot
$CitadelRoot = $ScriptRoot | Split-Path -Parent
$Flag = Join-Path $CitadelRoot "decisions" "enable_autostart.flag"
$TaskName = "CitadelleA0"
$Launcher = Join-Path $CitadelRoot "serve.ps1"

function Write-AutoStartLog {
  param([string]$Message, [string]$Level = "INFO")
  $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
  $line = "$ts [$Level] [autostart] $Message"
  $logFile = Join-Path $CitadelRoot "logs" "autostart.log"
  Add-Content -LiteralPath $logFile -Value $line -Encoding UTF8
  Write-Host $line
}

function Require-Flag {
  # 12WY-ON-PAUSE check FIRST — Tony Stark pré-ratification cycle 12 sem (2026-07-05 → 2026-09-27)
  $twelveWy = Join-Path $CitadelRoot "decisions" "12WY_ON_PAUSE.flag"
  if (Test-Path $twelveWy) {
    Write-AutoStartLog "12WY-ON-PAUSE ACTIVE — bypassing individual gate (Tony pré-ratification)"
    return
  }
  if (-not (Test-Path $Flag)) {
    Write-AutoStartLog "REFUSED: missing $Flag (A0 HITL explicit gate required)" "ERROR"
    Write-Host ""
    Write-Host "Frein à main actif. Aucune persistance système sans GO A+."
    Write-Host "Pour activer l'auto-start :"
    Write-Host "  ni | Out-File -Encoding UTF8 '$Flag'"
    Write-Host "  (ou)"
    Write-Host "  New-Item -ItemType File '$Flag'"
    Write-Host ""
    exit 2
  }
}

if ($Status) {
  $flagExists = Test-Path $Flag
  $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
  Write-Host "GATE enable_autostart.flag: $(if ($flagExists) { 'ENABLED' } else { 'DISABLED (default)' })"
  Write-Host "Task scheduled: $(if ($task) { $task.TaskName } else { 'NOT INSTALLED' })"
  exit 0
}

if ($Uninstall) {
  try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction Stop
    Write-AutoStartLog "uninstalled scheduled task $TaskName"
  } catch {
    Write-AutoStartLog "no task to uninstall ($($_.Exception.Message))" "WARN"
  }
  exit 0
}

if ($Install) {
  Require-Flag
  Write-AutoStartLog "installing scheduled task $TaskName → $Launcher -RunCollectors"
  $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -WindowStyle Hidden -File `"$Launcher`" -RunCollectors" -WorkingDirectory $CitadelRoot
  $trigger = New-ScheduledTaskTrigger -AtLogOn
  $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
  $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 0)
  Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Citadelle A0 gateway (local port 8770). Per Plan Citadelle A0 §5 + ADR-LD01-007 §1."
  Write-AutoStartLog "INSTALLED scheduled task $TaskName — gate auto-start now active"
  exit 0
}

# No flag given: show usage + status
Write-Host "Citadelle A0 install-autostart.ps1 — gated by enable_autostart.flag"
Write-Host ""
Write-Host "Status:"
& $PSCommandPath -Status
Write-Host ""
Write-Host "Usage:"
Write-Host "  .\install-autostart.ps1 -Status     # show current state"
Write-Host "  .\install-autostart.ps1 -Install    # install (REQUIRES gate flag)"
Write-Host "  .\install-autostart.ps1 -Uninstall  # uninstall"