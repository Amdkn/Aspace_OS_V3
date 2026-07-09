<#
serve.ps1 — Citadelle A0 Windows native launcher (P0).

Per ADR-LD01-006 §C2 (Windows natif PS, pas Docker).
Per ADR-LD01-007 §5 (persistance + auto-démarrage gated Gate #3).

Usage:
  .\serve.ps1                # start server in foreground (logs to logs/citadel.log)
  .\serve.ps1 -RunCollectors # run 3 collectors first, then start server
  .\serve.ps1 -Stop          # stop running server

DOCTRINE : lecture seule sur sources canoniques. Démarre juste stdlib http.server.
#>
[CmdletBinding()]
param(
  [switch]$RunCollectors,
  [switch]$Stop,
  [string]$Host = "127.0.0.1",
  [int]$Port = 8770
)

$ErrorActionPreference = "Stop"
$CitadelRoot = $PSScriptRoot | Split-Path -Parent
Set-Location $CitadelRoot

$LogDir = Join-Path $CitadelRoot "logs"
$PidFile = Join-Path $LogDir "citadel.pid"
$LogFile = Join-Path $LogDir "citadel.log"
$null = New-Item -ItemType Directory -Force -Path $LogDir

function Write-CitadelLog {
  param([string]$Message, [string]$Level = "INFO")
  $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
  $line = "$ts [$Level] $Message"
  Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
  Write-Host $line
}

function Stop-Citadel {
  if (Test-Path $PidFile) {
    $pid_old = Get-Content $PidFile -ErrorAction SilentlyContinue
    if ($pid_old) {
      try {
        Stop-Process -Id $pid_old -Force -ErrorAction Stop
        Write-CitadelLog "stopped pid=$pid_old"
      } catch {
        Write-CitadelLog "no running process pid=$pid_old ($($_.Exception.Message))" "WARN"
      }
    }
    Remove-Item $PidFile -Force
  }
  Write-CitadelLog "Citadelle A0 stopped"
}

function Start-Citadel {
  Write-CitadelLog "starting Citadelle A0 on http://${Host}:${Port}"
  $env:CITADEL_HOST = $Host
  $env:CITADEL_PORT = $Port
  $proc = Start-Process -FilePath "python" `
    -ArgumentList "$CitadelRoot\serve.py" `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $LogFile `
    -WorkingDirectory $CitadelRoot `
    -WindowStyle Hidden `
    -PassThru
  Set-Content -LiteralPath $PidFile -Value $proc.Id
  Write-CitadelLog "started pid=$($proc.Id) log=$LogFile"
  Start-Sleep -Seconds 2
  try {
    $health = Invoke-RestMethod -Uri "http://${Host}:${Port}/api/health" -TimeoutSec 5
    Write-CitadelLog "health check OK: $($health.status) (doctrine=$($health.doctrine))"
  } catch {
    Write-CitadelLog "health check FAILED: $($_.Exception.Message)" "ERROR"
    throw
  }
}

function Invoke-Collectors {
  $collectors = @(
    "collector_01_harnesses.py",
    "collector_04_skills.py",
    "collector_06_connections.py",
    "collector_07_decisions.py",
    "collector_08_agents.py",
    "collector_09_frameworks.py",
    "collector_10_domains.py",
    "collector_11_memory.py",
    "collector_12_zora.py",
    "collector_13_harnesses_live.py"
  )
  foreach ($c in $collectors) {
    $path = Join-Path $CitadelRoot "collectors" $c
    Write-CitadelLog "running $c"
    & python $path
    if ($LASTEXITCODE -ne 0) {
      throw "collector $c failed exit=$LASTEXITCODE"
    }
  }
  Write-CitadelLog "all 10 collectors OK"
}

if ($Stop) {
  Stop-Citadel
  exit 0
}

if ($RunCollectors) {
  Invoke-Collectors
}

# If already running, restart
if (Test-Path $PidFile) {
  Stop-Citadel
}

Start-Citadel
Write-CitadelLog "Citadelle A0 ready — http://${Host}:${Port}/"
Write-Host ""
Write-Host "Try:"
Write-Host "  curl http://${Host}:${Port}/api/health"
Write-Host "  curl http://${Host}:${Port}/api/harnesses          (Pilier 1)"
Write-Host "  curl http://${Host}:${Port}/api/harnesses/live    (Pilier runtime state)"
Write-Host "  curl http://${Host}:${Port}/api/skills"
Write-Host "  curl http://${Host}:${Port}/api/connections"
Write-Host "  curl http://${Host}:${Port}/api/decisions"
Write-Host "  curl http://${Host}:${Port}/api/agents"
Write-Host "  curl http://${Host}:${Port}/api/frameworks"
Write-Host "  curl http://${Host}:${Port}/api/domains"
Write-Host "  curl http://${Host}:${Port}/api/memory"
Write-Host "  curl http://${Host}:${Port}/api/zora              (8 dimensions Jack)"
Write-Host "  curl http://${Host}:${Port}/api/zora/last-run"
Write-Host "  open http://${Host}:${Port}/          (Bridge UI)"
Write-Host "  open http://${Host}:${Port}/decisions  (Decisions page)"
Write-Host "  open http://${Host}:${Port}/agents     (Agents page)"
Write-Host "  open http://${Host}:${Port}/frameworks (Frameworks page)"
Write-Host "  open http://${Host}:${Port}/domains    (Domaines page)"
Write-Host "  open http://${Host}:${Port}/memory     (Memory page)"
Write-Host "  open http://${Host}:${Port}/zora       (Zora nightly digest — gated)"
Write-Host "  open http://${Host}:${Port}/harnesses  (Harnesses live — runtime state)"
Write-Host "  Status gate AUTO-START : .\install-autostart.ps1 -Status"
Write-Host "  Status gate WATCHDOG   : .\watchdog.ps1"
Write-Host "  Status gate ZORA       : .\install-zora.ps1 -Status"
Write-Host "  Status gate CANONIC    : curl http://${Host}:${Port}/api/decisions/status"