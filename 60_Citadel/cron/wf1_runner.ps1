<#
wf1_runner.ps1 - LE RUN LOOP (True Agent Autonomy, option 1 - ADR-L1-WF-001 + critique A+ 2026-07-06).
PAS un cron a heure fixe : une boucle while(true) qui relance un worker M3 headless DES que le
precedent finit. Chaque worker = 1 iteration (1 item + preuve + worklog), etat porte par le filesystem.
Le plan MiniMax (5.1B tokens) travaille au lieu de dormir.

PATCH PS-1 (2026-07-06, wargame 12, additive) :
  - Logs split : wf1_runner.log = runner state only ; wf1_worker.log = worker stdout/stderr par iter
  - Max-time guard : worker > 600 s sans worklog append -> kill explicite rc=124 (signal thrashing)
  - Ces patches sont additifs (zéro hard-delete du canon original)

Gates (kill-switches, verifies A CHAQUE iteration - retirer un flag = arret au tour suivant) :
- decisions/enable_wf1.flag ABSENT -> exit (cascade GO Spock)
- data/beth_repos.flag PRESENT hors Fenetre Fable -> pause 30 min (Beth veto vie - les workers
  n'interpellent personne mais on respecte le gel hors fenetre)
- decisions/STOP_WF1_RUNNER.flag PRESENT -> exit immediat (arret d'urgence dedie)

Usage : .\wf1_runner.ps1            (boucle infinie)
        .\wf1_runner.ps1 -Once     (1 iteration, test)
Install 24/7 : schtask ONSTART via install-loops.ps1 (ajoute) + demarrage immediat detache.
#>
[CmdletBinding()]
param([switch]$Once)

$ErrorActionPreference = "Continue"
$Citadel = $PSScriptRoot | Split-Path -Parent
$Dec = Join-Path $Citadel "decisions"
$LogDir = Join-Path $Citadel "logs"
$Log = Join-Path $LogDir "wf1_runner.log"             # runner state only
$WorkerLog = Join-Path $LogDir "wf1_worker.log"       # NEW (PATCH PS-1): worker stdout/stderr par iter
$Worklog = Join-Path $Citadel "loops\logs\worklog.md"  # NEW (PATCH PS-1): surveille append worklog
$PromptFile = Join-Path $Citadel "loops\domains\wf1-morty\WORKER_PROMPT.md"
$MaxWorkerSeconds = 600                                # NEW (PATCH PS-1): no-worklog kill threshold
$null = New-Item -ItemType Directory -Force -Path $LogDir

# env M3 (User scope -> process) : le runner tourne headless, jamais de valeur loggee
$env:ANTHROPIC_AUTH_TOKEN=[Environment]::GetEnvironmentVariable('ANTHROPIC_AUTH_TOKEN','User')
$env:ANTHROPIC_API_KEY=[Environment]::GetEnvironmentVariable('ANTHROPIC_API_KEY','User')
$env:ANTHROPIC_BASE_URL  = [Environment]::GetEnvironmentVariable('ANTHROPIC_BASE_URL','User')

function Log([string]$m) {
  $line = "$(Get-Date -Format s) [wf1-runner] $m"
  Add-Content -LiteralPath $Log -Value $line -Encoding UTF8
  Write-Host $line
}

function LogWorker([int]$iterN, [string]$text) {
  if ([string]::IsNullOrWhiteSpace($text)) { return }
  $header = "=== iter $iterN · $(Get-Date -Format s) ==="
  Add-Content -LiteralPath $WorkerLog -Value $header -Encoding UTF8
  Add-Content -LiteralPath $WorkerLog -Value $text -Encoding UTF8
  Add-Content -LiteralPath $WorkerLog -Value ("=" * 60) -Encoding UTF8
}

function Get-WorklogMtime {
  if (Test-Path $Worklog) { (Get-Item $Worklog).LastWriteTime } else { [DateTime]::MinValue }
}

# SINGLETON GUARD v4 : exclut PID courant ET son PPID (le wrapper shell qui a lancé ce script)
$myPPID = (Get-CimInstance Win32_Process -Filter "ProcessId=$PID").ParentProcessId
$others = Get-CimInstance Win32_Process | Where-Object {
  $_.Name -match 'powershell' -and
  $_.CommandLine -match '-File.*wf1_runner\.ps1' -and
  $_.ProcessId -ne $PID -and
  $_.ProcessId -ne $myPPID
}
if ($others) { Log "singleton: runner deja vivant (PID $($others[0].ProcessId)) - exit"; exit 0 }

Log "RUN LOOP start (Once=$Once) - workers M3 headless, pas d'heures fixes"
$iter = 0
while ($true) {
  $iter++
  if (Test-Path (Join-Path $Dec "STOP_WF1_RUNNER.flag")) { Log "STOP flag - exit"; break }
  if (-not (Test-Path (Join-Path $Dec "enable_wf1.flag"))) { Log "enable_wf1 absent (GO revoque) - exit"; break }
  $fableWindow = Test-Path (Join-Path $Dec "FABLE_WINDOW.flag")
  $bethRepos = Test-Path (Join-Path $Citadel "data\beth_repos.flag")
  if ($bethRepos -and -not $fableWindow) { Log "Beth repos actif (hors fenetre) - pause 30 min"; Start-Sleep -Seconds 1800; continue }

  Log "iteration $iter - spawn worker (no-mcp)"
  $worklogMtimeBefore = Get-WorklogMtime
  $prompt = Get-Content $PromptFile -Raw
  $t0 = Get-Date
  Set-Location $Citadel

  # NEW (PATCH PS-2, 2026-07-07, wargame 26 / 13 M2): idempotence run-id
  # Format: <ISO-yyyyMMddHHmm>-<6-char-sha1-of-prompt>. Fichier STATE dans decisions/.
  # But : si un ticket est re-feed dans la meme minute (re-feed Boimler, restart runner),
  # on SKIP le spawn plutot que de re-traiter. Fenetre dedup = 90 s (couvre les doubles
  # spawn en cascade, laisse passer un meme ticket le lendemain).
  $RunIdFile = Join-Path $Dec "WF1_LAST_RUNID.txt"
  $runIdStamp = Get-Date -Format 'yyyyMMddHHmm'
  $promptHash = [System.BitConverter]::ToString(
                  [System.Security.Cryptography.SHA1]::Create().ComputeHash(
                    [System.Text.Encoding]::UTF8.GetBytes($prompt))
                ).Replace('-','').Substring(0,6).ToLower()
  $runId = "$runIdStamp-$promptHash"
  if (Test-Path $RunIdFile) {
    $prev = Get-Content $RunIdFile -Raw -ErrorAction SilentlyContinue
    if ($prev -and ($prev -match '^(\d{12})-([0-9a-f]{6})$')) {
      $prevStamp = $Matches[1]; $prevHash = $Matches[2]
      $prevDt = [datetime]::ParseExact($prevStamp, 'yyyyMMddHHmm', $null)
      $age = (Get-Date) - $prevDt
      if ($prevHash -eq $promptHash -and $age.TotalSeconds -lt 90) {
        Log "iteration $iter DEDUP run_id=$runId (meme hash, age=$([int]$age.TotalSeconds)s) - skip spawn"
        Start-Sleep -Seconds 30
        continue
      }
    }
  }

  # NEW (PATCH PS-1): worker output vers wf1_worker.log (PAS wf1_runner.log)
  # Lance en background, poll toutes les 10s, kill si > MaxWorkerSeconds ET worklog inchangé
  $workerOutFile = [System.IO.Path]::GetTempFileName()
  $workerErrFile = [System.IO.Path]::GetTempFileName()
  # claude = ExternalScript (.ps1 shim npm). Approche wrapper .ps1 temp :
  #   - evite le quoting hell de -Command avec chemins/prompts complexes
  #   - -File est plus robuste que -Command pour Start-Process
  #   - reinjecte env vars M3 (auth) explicitement dans le child isolé
  # FLAGS VERIFIES via claude --help : --bare (skip CLAUDE.md/hooks/plugins) +
  #   --strict-mcp-config --mcp-config mcp-empty.json (zero MCP global)
  #   --dangerously-skip-permissions (bypass confirmations)
  $promptFile = [System.IO.Path]::GetTempFileName() + ".txt"
  [System.IO.File]::WriteAllText($promptFile, $prompt, [System.Text.Encoding]::UTF8)
  $claudePs1 = "C:\Users\amado\AppData\Roaming\npm\claude.ps1"
  $McpEmpty   = Join-Path $PSScriptRoot "mcp-empty.json"
  $wrapScript = @"
`$env:ANTHROPIC_API_KEY    = '$($env:ANTHROPIC_API_KEY -replace "'","''")'
`$env:ANTHROPIC_AUTH_TOKEN = '$($env:ANTHROPIC_AUTH_TOKEN -replace "'","''")'
`$env:ANTHROPIC_BASE_URL   = '$($env:ANTHROPIC_BASE_URL -replace "'","''")'
Set-Location '$($Citadel -replace "'","''")'
& '$claudePs1' -p (Get-Content -LiteralPath '$($promptFile -replace "'","''")' -Raw -Encoding UTF8) ``
    --bare --dangerously-skip-permissions ``
    --strict-mcp-config --mcp-config '$($McpEmpty -replace "'","''")'
exit `$LASTEXITCODE
"@
  $wrapperFile = [System.IO.Path]::GetTempFileName() + ".ps1"
  [System.IO.File]::WriteAllText($wrapperFile, $wrapScript, [System.Text.Encoding]::UTF8)
  $proc = Start-Process -FilePath "powershell.exe" `
                        -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $wrapperFile) `
                        -RedirectStandardOutput $workerOutFile `
                        -RedirectStandardError $workerErrFile `
                        -WorkingDirectory $Citadel `
                        -NoNewWindow -PassThru
  # NEW (PATCH PS-3, 2026-07-08, fix Opus-flagged D6) : WriteAllText a ligne 145 ne s'executait pas.
  # Root cause (D6 D1) : l'assignation `$proc = Start-Process ... -PassThru` dans ce contexte wrapper-inline
  # semble evaluer a $null malgre spawn reussi (le worker demarre, le log dit "spawn worker", mais
  # $proc ne porte pas l'objet Process - probablement un quirk de -PassThru avec -FilePath powershell.exe).
  # Symptome : 58 iter completees, WF1_LAST_RUNID.txt absent du filesystem.
  # Fix PS-3 :
  #   (a) try/catch explicite + log du chemin exact
  #   (b) write UNCONDITIONALLY apres spawn reussi (sortie de Start-Process avec code 0 ou process handle valide)
  #   (c) on garde la semantique "ecrit seulement si on a essaye de spawn" = l'iteration a demarre un worker
  $spawnOk = $false
  if ($proc) { $spawnOk = $true }
  if ($spawnOk) {
    try {
      [System.IO.File]::WriteAllText($RunIdFile, $runId, [System.Text.Encoding]::UTF8)
      Log "iteration $iter run-id persisted: $runId ($([int]((Get-Item $RunIdFile).Length)) bytes)"
    } catch {
      Log "iteration $iter run-id WRITE FAILED: $($_.Exception.Message) path=$RunIdFile"
    }
  } else {
    Log "iteration $iter SPAWN FAILED (proc null) - skip"; Start-Sleep -Seconds 45; continue
  }
  $killed = $false
  $killReason = ""
  while (-not $proc.HasExited) {
    Start-Sleep -Seconds 10
    $elapsed = [int]((Get-Date) - $t0).TotalSeconds
    if ($elapsed -gt $MaxWorkerSeconds) {
      $wmtime = Get-WorklogMtime
      if ($wmtime -le $worklogMtimeBefore) {
        # Pas d'append worklog dans la fenêtre = thrashing probable
        try { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue } catch {}
        $killed = $true
        $killReason = "TIMEOUT-no-worklog-${elapsed}s"
        Log "iteration $iter $killReason -> kill (rc=124)"
        break
      }
    }
  }
  if (-not $killed) { $proc.WaitForExit() }
  $dur = [int]((Get-Date) - $t0).TotalSeconds
  $rc = if ($killed) { 124 } else { $proc.ExitCode }
  Log "iteration $iter done in ${dur}s (rc=$rc)"

  # Capture worker output (stdout + stderr) dans wf1_worker.log
  $txt = ""
  foreach ($f in @($workerOutFile, $workerErrFile)) {
    if (Test-Path $f) {
      $t = Get-Content -LiteralPath $f -Raw -ErrorAction SilentlyContinue
      if ($t) { $txt += $t + "`n" }
      Remove-Item -LiteralPath $f -Force -ErrorAction SilentlyContinue
    }
  }
  if ($txt) { LogWorker $iter $txt }
  # Nettoyage fichiers temp (prompt + wrapper)
  if ($promptFile  -and (Test-Path $promptFile))  { Remove-Item -LiteralPath $promptFile  -Force -ErrorAction SilentlyContinue }
  if ($wrapperFile -and (Test-Path $wrapperFile)) { Remove-Item -LiteralPath $wrapperFile -Force -ErrorAction SilentlyContinue }

  if ($Once) { Log "Once mode - exit"; break }
  Start-Sleep -Seconds 45  # respiration entre workers (pas des heures : 45 s)
}
Log "RUN LOOP end"
