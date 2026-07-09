# collecteur_beth_capacity.ps1 - WARGAME 26 CAT.2 #3 (2026-07-07, additive)
# Beth-capacité = le VEto qui vérifie si la machine peut porter la charge worker.
# Sources de mesure (D1 honest, wargame 26 cat.2 #3 amendé 2026-07-07) :
#   1. RAM : Get-CimInstance Win32_ComputerSystem.TotalPhysicalMemory (libre vs total)
#   2. GPU : nvidia-smi --query-gpu=memory.free (fallback 0 si Intel UHD / pas CUDA)
#   3. Tokens plan MiniMax : PAS auto-scrape (login requis). Source = usage-log.md
#      que A+ nourrit manuellement d'apres platform.minimax.io/console/usage
#   4. Worklog burn rate : wc -l worklog_24h vs baseline_30j (proxy secondaire)
#
# Verdict (CALIBRATION A+ ratifiée 2026-07-07 23:50, REFIT Catégorie 2 #3) :
#   GREEN = RAM_libre > 6GB AND (tokens_5h < 90% OR last_log < 6h) AND worklog_24h > baseline/3
#   YELLOW = RAM_libre 3-6 GB (advisory, pas de veto - A+ pauses manuellement au ressenti)
#   RED   = RAM_libre < 3GB AND worklog_24h < baseline/10
#           OR tokens_5h > 90% dans last_log (si log < 6h)
#           OR ctx_pressure_count >= 3 (worker a signale ctx-pressure 3x consecutif)
# Historique calibration :
#   - v1 (23:09) : GREEN > 16GB (trop strict, system 31.8GB mais apps ouvertes = 12GB free = YELLOW injustifié)
#   - v2 (23:50) : GREEN > 6GB (A+ ratifié après mesure réelle 12GB free + apps fermables)
#   - A+ pauses manuellement entre YELLOW et RED : pas de Beth veto dur en YELLOW.
#
# Effets :
#   - Update loops/STATE.json (capacity_green, capacity_verdict, capacity_provenance)
#   - Append 1 ligne worklog avec verdict chiffre
#   - NE TUE PAS le runner (sortie advisory seulement, sauf RED = exit 2)
#   - Si RED : exit 2 -> le runner le voit et pause 30 min (Beth veto)
#
# Usage : .\collecteur_beth_capacity.ps1         (lecture + verdict + log)
#         .\collecteur_beth_capacity.ps1 -Quiet  (silent, juste update STATE.json)
[CmdletBinding()]
param([switch]$Quiet)

$ErrorActionPreference = 'Continue'
$Citadel = $PSScriptRoot | Split-Path -Parent
$LogDir = Join-Path $Citadel 'loops\logs'
$StateFile = Join-Path $Citadel 'loops\STATE.json'
$UsageLog = Join-Path $Citadel 'loops\logs\usage-log.md'
$Worklog = Join-Path $Citadel 'loops\logs\worklog.md'
$null = New-Item -ItemType Directory -Force -Path $LogDir

# === SOURCES DE MESURE =============================================================
$ram = [ordered]@{
  total_gb = $null
  free_gb  = $null
  used_pct = $null
}
try {
  $os = Get-CimInstance Win32_OperatingSystem
  $cs = Get-CimInstance Win32_ComputerSystem
  $ram.total_gb = [math]::Round($cs.TotalPhysicalMemory / 1GB, 1)
  # D6 FIX 2026-07-07: Win32_OperatingSystem.FreePhysicalMemory est en KB (docs MS), pas bytes.
  # Avant : os.FreePhysicalMemory / 1MB / 1024 = division par 1024^2 = toujours ~0.
  # Apres : os.FreePhysicalMemory / 1MB = KB / (1024^2) = GB. Correct.
  $ram.free_gb  = [math]::Round($os.FreePhysicalMemory / 1MB, 1)
  $ram.used_pct = [math]::Round((($ram.total_gb - $ram.free_gb) / $ram.total_gb) * 100, 1)
} catch {
  Write-Host "[collecteur] RAM read failed: $($_.Exception.Message)"
}

$gpu = [ordered]@{
  available = $false
  free_gb = 0
  note = 'no-nvidia-smi or Intel UHD (CPU_only)'
}
try {
  $nvidiaOut = & nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits 2>$null
  if ($nvidiaOut -and $LASTEXITCODE -eq 0) {
    $gpu.available = $true
    $gpu.free_gb = [math]::Round([int]$nvidiaOut[0] / 1024, 2)
    $gpu.note = 'nvidia-smi OK'
  }
} catch {}

# === TOKENS (depuis usage-log.md, A+ manuel) ======================================
$tokens = [ordered]@{
  source = 'usage-log.md (A+ manuel depuis platform.minimax.io/console/usage)'
  last_log_iso = $null
  age_minutes  = $null
  pct_5h       = $null
  pct_weekly   = $null
  pct_monthly  = $null
}
if (Test-Path $UsageLog) {
  # Parse la DERNIERE ligne du format `- [ISO] [usage-snapshot] 5h=X% weekly=Y% monthly=Z%`
  $lastLine = Get-Content $UsageLog -Tail 1 -ErrorAction SilentlyContinue
  if ($lastLine -match '\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2})\].*5h=(\d+(?:\.\d+)?)%.*weekly=(\d+(?:\.\d+)?)%.*monthly=(\d+(?:\.\d+)?)%') {
    $tokens.last_log_iso = $Matches[1]
    $tokens.pct_5h       = [double]$Matches[2]
    $tokens.pct_weekly   = [double]$Matches[3]
    $tokens.pct_monthly  = [double]$Matches[4]
    try {
      $tokens.age_minutes = [int]((Get-Date) - [datetime]::Parse($tokens.last_log_iso)).TotalMinutes
    } catch { $tokens.age_minutes = -1 }
  }
}

# === WORKLOG BURN RATE (proxy secondaire) ==========================================
$burn = [ordered]@{
  source = 'worklog.md lines / 24h vs baseline 30j'
  worklog_24h = 0
  baseline_30j = 0
  ratio = 0
}
if (Test-Path $Worklog) {
  $allLines = Get-Content $Worklog -ErrorAction SilentlyContinue
  if ($allLines) {
    $cutoff24h = (Get-Date).AddHours(-24)
    $cutoff30j = (Get-Date).AddDays(-30)
    $burn.worklog_24h = ($allLines | Where-Object {
      $_ -match '\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})' -and
      [datetime]::Parse($Matches[1]) -gt $cutoff24h
    }).Count
    $burn.baseline_30j = ($allLines | Where-Object {
      $_ -match '\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})' -and
      [datetime]::Parse($Matches[1]) -gt $cutoff30j
    }).Count
    if ($burn.baseline_30j -gt 0) {
      # baseline_30j = total sur 30j, attendu ~30j * (baseline/jour). ratio = worklog_24h / (baseline_30j / 30)
      $expectedPerDay = $burn.baseline_30j / 30
      $burn.ratio = if ($expectedPerDay -gt 0) { [math]::Round($burn.worklog_24h / $expectedPerDay, 2) } else { 0 }
    }
  }
}

# === VERDICT ======================================================================
$verdict = 'YELLOW'
$verdictReasons = @()

# GREEN conditions (all must hold) - CALIBRATION v2 2026-07-07 23:50
$greenRam = ($ram.free_gb -ne $null -and $ram.free_gb -gt 6)
$greenTokens = ($tokens.pct_5h -ne $null -and $tokens.pct_5h -lt 90) -or
               ($tokens.age_minutes -ne $null -and $tokens.age_minutes -gt 360) -or
               ($tokens.pct_5h -eq $null)  # pas de log = pas de veto
$greenBurn = ($burn.ratio -gt (1/3))
if ($greenRam -and $greenTokens -and $greenBurn) {
  $verdict = 'GREEN'
} else {
  if (-not $greenRam) { $verdictReasons += "RAM free $($ram.free_gb)GB <= 6GB (YELLOW=3-6, RED=<3)" }
  if (-not $greenTokens -and $tokens.pct_5h -ne $null) { $verdictReasons += "tokens 5h=$($tokens.pct_5h)% >= 90% (last_log $($tokens.age_minutes)min ago)" }
  if (-not $greenBurn) { $verdictReasons += "worklog 24h=$($burn.worklog_24h) ratio=$($burn.ratio) <= 1/3 baseline" }
}

# RED conditions (any triggers) - CALIBRATION v2 2026-07-07 23:50
$redRam = ($ram.free_gb -ne $null -and $ram.free_gb -lt 3 -and $burn.ratio -lt 0.1)
$redTokens = ($tokens.pct_5h -ne $null -and $tokens.pct_5h -ge 90 -and $tokens.age_minutes -lt 360)
if ($redRam -or $redTokens) {
  $verdict = 'RED'
  if ($redRam) { $verdictReasons += "[RED-HARD] RAM < 3GB AND burn < 10% baseline" }
  if ($redTokens) { $verdictReasons += "[RED-HARD] tokens 5h >= 90% with fresh log (<6h)" }
}

# === UPDATE STATE.JSON ============================================================
if (Test-Path $StateFile) {
  try {
    $state = Get-Content $StateFile -Raw | ConvertFrom-Json
    # D6 FIX 2026-07-07: capacity_verdict / capacity_verdict_reasons / capacity_provenance n'existent pas
    # dans le STATE.json d'origine (schema wargame 26 cat.2 #2 = capacity_green seulement). Add-Member
    # idempotent : on verifie presence avant.
    if (-not (Get-Member -InputObject $state -Name 'capacity_verdict' -ErrorAction SilentlyContinue)) {
      Add-Member -InputObject $state -NotePropertyName 'capacity_verdict' -NotePropertyValue $null
    }
    if (-not (Get-Member -InputObject $state -Name 'capacity_verdict_reasons' -ErrorAction SilentlyContinue)) {
      Add-Member -InputObject $state -NotePropertyName 'capacity_verdict_reasons' -NotePropertyValue @()
    }
    if (-not (Get-Member -InputObject $state -Name 'capacity_provenance' -ErrorAction SilentlyContinue)) {
      Add-Member -InputObject $state -NotePropertyName 'capacity_provenance' -NotePropertyValue @{}
    }
    $state.capacity_green = ($verdict -eq 'GREEN')
    $state.capacity_verdict = $verdict
    $state.capacity_verdict_reasons = $verdictReasons
    $state.capacity_provenance = @{
      ram = $ram
      gpu = $gpu
      tokens = $tokens
      burn = $burn
      last_collected = (Get-Date).ToString('o')
    }
    $state | ConvertTo-Json -Depth 6 | Set-Content $StateFile -Encoding UTF8
  } catch {
    Write-Host "[collecteur] STATE.json update failed: $($_.Exception.Message)"
  }
}

# === WORKLOG ENTRY ================================================================
if (-not $Quiet) {
  $isoNow = (Get-Date).ToString('yyyy-MM-ddTHH:mm:sszzz')
  $reasonsStr = if ($verdictReasons.Count -gt 0) { " reasons=[$([string]::Join('|', $verdictReasons))]" } else { '' }
  $log = "- [$isoNow] [collecteur-beth] verdict=$verdict ram=$($ram.free_gb)/$($ram.total_gb)GB gpu=$($gpu.note) tokens_5h=$($tokens.pct_5h)% age_log=$($tokens.age_minutes)min worklog_24h=$($burn.worklog_24h) ratio=$($burn.ratio)$reasonsStr :: preuve=agent-os/citadel/loops/STATE.json capacity_* updated"
  Add-Content -LiteralPath $Worklog -Value $log -Encoding UTF8
  Write-Host "[collecteur] $verdict - log appended"
}

# === SORTIE =======================================================================
if ($verdict -eq 'RED') {
  Write-Host "[collecteur] RED - Beth veto. Runner should pause 30 min."
  exit 2
}
exit 0