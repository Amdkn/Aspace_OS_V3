<#
install-loops.ps1 - installeur schtasks 24/7 pour toutes les loops Citadelle (P3, ADR-L1-WF-001).
Generalise install-book-cron.ps1 (Mavis). Le vrai 24/7 = Windows Task Scheduler :
survit aux redemarrages, ne depend d'aucune session CC (leve la limite 7j/REPL-idle).

Gating par loop (Portes over Freins, WARMODE-002) - installer != activer, chaque script
reste self-gated par son flag (exit 2 si absent) :
- book         : enable_book_loop.flag (pose)
- zora         : enable_zora.flag (pose)
- heartbeat_os : enable_heartbeat.flag (observation only)
- wf3-sim      : enable_wf3.flag (pose UNIQUEMENT par cascade GO_SPOCK_UNIQUE)

Usage : .\install-loops.ps1 -Install | -Uninstall | -Status
#>
[CmdletBinding()]
param([switch]$Install, [switch]$Uninstall, [switch]$Status)

$ErrorActionPreference = "Stop"
$CitadelRoot = $PSScriptRoot | Split-Path -Parent
$Python = "C:\Python314\python.exe"
$LogFile = Join-Path (Join-Path $CitadelRoot "logs") "install_loops.log"
$null = New-Item -ItemType Directory -Force -Path (Split-Path $LogFile)

$Loops = @(
  @{ Name = "AspaceLoopBook";      Script = "book_loop.py";      Hours = 4;  Desc = "WF2 Book COO Loop Engineering (self-gated enable_book_loop.flag). Append-only. /ship jamais automatique." },
  @{ Name = "AspaceLoopZoraNuit";  Script = "zora-nuit.py";      Hours = 24; Desc = "Zora nuit (self-gated enable_zora.flag)." },
  @{ Name = "AspaceLoopHeartbeat"; Script = "heartbeat_os.py";   Hours = 4;  Desc = "War Room heartbeat OS-level : airlock Beth + collector + Telegram. Observation only." },
  @{ Name = "AspaceLoopWF3Sim";    Script = "wf3_sim_runner.py"; Hours = 12; Desc = "WF3 MiroFish sims deterministes (self-gated enable_wf3.flag, cascade GO)." }
)

function Log([string]$m) {
  $line = "$(Get-Date -Format s) [install-loops] $m"
  Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
  Write-Host $line
}

if ($Status -or (-not $Install -and -not $Uninstall)) {
  foreach ($l in $Loops) {
    $t = Get-ScheduledTask -TaskName $l.Name -ErrorAction SilentlyContinue
    if ($t) { $msg = "INSTALLED (every $($l.Hours)h, state=$($t.State))" } else { $msg = "NOT INSTALLED" }
    Write-Host ("{0,-22} {1}" -f $l.Name, $msg)
  }
  exit 0
}

if ($Uninstall) {
  foreach ($l in $Loops) {
    try { Unregister-ScheduledTask -TaskName $l.Name -Confirm:$false -ErrorAction Stop; Log "uninstalled $($l.Name)" }
    catch { Log "no task $($l.Name)" }
  }
  exit 0
}

foreach ($l in $Loops) {
  $script = Join-Path (Join-Path $CitadelRoot "cron") $l.Script
  if (-not (Test-Path $script)) { Log "SKIP $($l.Name): script absent ($script)"; continue }
  $action = New-ScheduledTaskAction -Execute $Python -Argument ('"' + $script + '"') -WorkingDirectory (Join-Path $CitadelRoot "cron")
  $start = (Get-Date).AddMinutes(3)
  $trigger = New-ScheduledTaskTrigger -Once -At $start -RepetitionInterval (New-TimeSpan -Hours $l.Hours) -RepetitionDuration (New-TimeSpan -Days 3650)
  $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
  $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 10)
  Register-ScheduledTask -TaskName $l.Name -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description $l.Desc -Force | Out-Null
  Log "INSTALLED $($l.Name) - every $($l.Hours)h ($($l.Script))"
}
Log "done. Rappel : installer != activer - chaque script reste self-gated par son flag."
& $PSCommandPath -Status
