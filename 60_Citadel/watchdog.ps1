<#
watchdog.ps1 — Citadelle A0 watchdog natif PS (P2).

Per ADR-LD01-006 §C2 + Plan Citadelle §5 : "Watchdog : re-lance si port
8770 mort (script PS 20 lignes, log .claude/logs/citadel.log)."

GATING (FREIN À MAIN) : ce script REFUSE de tourner sans le flag
  decisions/enable_watchdog.flag
posé par A0 HITL explicite.

Usage:
  .\watchdog.ps1 -Once     # check + relance si nécessaire (1 cycle)
  .\watchdog.ps1 -Loop 60  # loop check toutes les 60s

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P2
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §5
Sister : ADR-LD01-007 §1 décision 3 (auto-start gated) + §5 natif PS
#>
[CmdletBinding()]
param(
  [switch]$Once,
  [int]$Loop = 0,
  [int]$Port = 8770
)

$ErrorActionPreference = "Stop"
$CitadelRoot = $PSScriptRoot | Split-Path -Parent
$Flag = Join-Path $CitadelRoot "decisions" "enable_watchdog.flag"
$LogFile = Join-Path $CitadelRoot "logs" "watchdog.log"

$null = New-Item -ItemType Directory -Force -Path (Split-Path $LogFile)

function Watchdog-Log {
  param([string]$Message, [string]$Level = "INFO")
  $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
  $line = "$ts [$Level] [watchdog] $Message"
  Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
  Write-Host $line
}

function Test-Port {
  param([int]$Port)
  try {
    $conn = New-Object System.Net.Sockets.TcpClient
    $iar = $conn.BeginConnect("127.0.0.1", $Port, $null, $null)
    $success = $iar.AsyncWaitHandle.WaitOne(2000, $false)
    if ($success -and $conn.Connected) {
      $conn.Close()
      return $true
    }
    $conn.Close()
  } catch {}
  return $false
}

function Restart-Server {
  Watchdog-Log "port ${Port} DOWN — restart"
  $launcher = Join-Path $CitadelRoot "serve.ps1"
  & $launcher
  Start-Sleep -Seconds 2
  if (Test-Port -Port $Port) {
    Watchdog-Log "port ${Port} UP after restart"
  } else {
    Watchdog-Log "port ${Port} STILL DOWN after restart" "ERROR"
  }
}

if ($Once) {
  # 12WY-ON-PAUSE check FIRST
  $twelveWy = Join-Path $CitadelRoot "decisions" "12WY_ON_PAUSE.flag"
  if (-not (Test-Path $twelveWy)) {
    if (-not (Test-Path $Flag)) {
      Watchdog-Log "REFUSED: missing $Flag (A0 HITL explicit gate required)" "ERROR"
      exit 2
    }
  } else {
    Watchdog-Log "12WY-ON-PAUSE ACTIVE — bypassing individual gate (Tony pré-ratification)"
  }
  if (Test-Port -Port $Port) {
    Watchdog-Log "port ${Port} OK — no action"
  } else {
    Restart-Server
  }
  exit 0
}

if ($Loop -gt 0) {
  $twelveWy = Join-Path $CitadelRoot "decisions" "12WY_ON_PAUSE.flag"
  if (-not (Test-Path $twelveWy)) {
    if (-not (Test-Path $Flag)) {
      Watchdog-Log "REFUSED: missing $Flag (A0 HITL explicit gate required)" "ERROR"
      exit 2
    }
  }
  Watchdog-Log "starting loop every ${Loop}s"
  while ($true) {
    if (-not (Test-Port -Port $Port)) { Restart-Server }
    Start-Sleep -Seconds $Loop
  }
}

# No flags: show usage + status
$flagExists = Test-Path $Flag
Write-Host "Citadelle A0 watchdog.ps1 — gated by enable_watchdog.flag"
Write-Host ""
Write-Host "Status:"
Write-Host "  GATE enable_watchdog.flag: $(if ($flagExists) { 'ENABLED' } else { 'DISABLED (default — no watching)' })"
Write-Host "  Active: $(if ($flagExists -and (Test-Port -Port $Port)) { 'port ' + $Port + ' OK' } else { 'OFF' })"
Write-Host ""
Write-Host "Usage (FREIN À MAIN — gate required):"
Write-Host "  New-Item -ItemType File '$Flag'   # A0 HITL — enables watchdog"
Write-Host "  .\watchdog.ps1 -Once             # single health check"
Write-Host "  .\watchdog.ps1 -Loop 60          # loop every 60s"