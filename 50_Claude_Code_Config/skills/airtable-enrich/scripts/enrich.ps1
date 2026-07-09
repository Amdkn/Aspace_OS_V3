# enrich.ps1 — Main pipeline for /airtable-enrich.
# Reads all `1-Raw` leads from an Airtable base/table, runs the 3 sub-scripts per record,
# PATCHes results back in batches of 10, logs to LLM_Wiki.
#
# Usage examples:
#   enrich.ps1 -Service aaas-solaris-marketing
#   enrich.ps1 -Service aaas-solaris-marketing -Limit 5
#   enrich.ps1 -Service aaas-solaris-marketing -DryRun
#   enrich.ps1 -BaseId appXXX -TableId tblYYY

[CmdletBinding()]
param(
  [string]$Service,
  [string]$BaseId,
  [string]$TableId,
  [int]$Limit = 0,
  [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Path
$SkillDir    = Split-Path -Parent $ScriptDir
$KnownBases  = Join-Path $SkillDir 'references\known-bases.md'
$WikiLog     = 'C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md'

function Write-Step($msg) { Write-Host "[airtable-enrich] $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "  OK  $msg"             -ForegroundColor Green }
function Write-Skip($msg) { Write-Host "  SKIP $msg"             -ForegroundColor Yellow }
function Write-Fail($msg) { Write-Host "  FAIL $msg"             -ForegroundColor Red }

# --- 1. Resolve token ---
$Token = [Environment]::GetEnvironmentVariable('AIRTABLE_BEARER_AUTH', 'User')
if (-not $Token) { $Token = $env:AIRTABLE_BEARER_AUTH }
if (-not $Token) {
  Write-Fail "AIRTABLE_BEARER_AUTH missing. See ~/.claude/CLAUDE.md §Test Key Pragma."
  exit 3
}
$Headers = @{ Authorization = "Bearer $Token"; 'Content-Type' = 'application/json' }

# --- 2. Resolve base/table from --service or --base/--table ---
if ($Service -and (-not $BaseId -or -not $TableId)) {
  if (-not (Test-Path $KnownBases)) {
    Write-Fail "$KnownBases not found"
    exit 2
  }
  $lines = Get-Content $KnownBases
  $found = $false
  foreach ($line in $lines) {
    # Match table row: | `service-name` | `appXXX` | `tblYYY` | ...
    if ($line -match '^\|\s*`([\w-]+)`\s*\|\s*`(app[^`]+)`\s*\|\s*`(tbl[^`]+)`') {
      if ($Matches[1] -eq $Service) {
        $BaseId  = $Matches[2]
        $TableId = $Matches[3]
        $found   = $true
        break
      }
    }
  }
  if (-not $found) {
    Write-Fail "Service '$Service' not in $KnownBases. Add a row there or pass -BaseId/-TableId."
    exit 2
  }
}
if (-not $BaseId -or -not $TableId) {
  Write-Fail "Must provide either -Service <name> OR both -BaseId and -TableId"
  exit 2
}

$ServiceLabel = if ($Service) { $Service } else { "$BaseId/$TableId" }
Write-Step "Service: $ServiceLabel"
Write-Step "Base: $BaseId  Table: $TableId"
if ($DryRun) { Write-Step "DRY RUN - no PATCH will be sent" }

# --- 3. Fetch all 1-Raw records (paginated) ---
$ApiBase = "https://api.airtable.com/v0/$BaseId/$TableId"
$filter  = [Uri]::EscapeDataString("{Statut d'Enrichissement}='1-Raw'")
$allRecords = @()
$offset = $null
do {
  $url = "$ApiBase`?filterByFormula=$filter&pageSize=100"
  if ($offset) { $url += "&offset=$offset" }
  try {
    $resp = Invoke-RestMethod -Uri $url -Headers $Headers -Method Get -ErrorAction Stop
  } catch {
    Write-Fail "Airtable fetch failed: $($_.Exception.Message)"
    exit 4
  }
  $allRecords += $resp.records
  $offset = $resp.offset
} while ($offset)

$total = @($allRecords).Count
if ($Limit -gt 0 -and $total -gt $Limit) {
  $allRecords = @($allRecords | Select-Object -First $Limit)
}
$workCount = @($allRecords).Count
Write-Step "Found $total leads at Statut=1-Raw  (processing $workCount this run)"

if ($workCount -eq 0) {
  Write-Step "Nothing to enrich. Exit clean."
  exit 0
}

# --- 4. Per-record pipeline ---
$updates  = @()       # for batch PATCH
$rejects  = @()       # records to mark 3-Rejeté
$logLines = @()

foreach ($rec in $allRecords) {
  $name    = $rec.fields.'Nom de l''Agence'
  $url     = $rec.fields.'URL du Site Web'
  $sector  = $rec.fields.'Secteur d''Activité'
  $currQ   = if ($rec.fields.'Note Globale de Qualité') { [double]$rec.fields.'Note Globale de Qualité' } else { 0.0 }
  $currCmt = if ($rec.fields.'Commentaires Internes') { $rec.fields.'Commentaires Internes' } else { '' }

  Write-Step "[$($rec.id)] $name  ($sector)"

  if (-not $url) {
    Write-Skip "no URL → mark 3-Rejeté"
    $rejects += @{ id = $rec.id; fields = @{ "Statut d'Enrichissement" = "3-Rejeté"; "Commentaires Internes" = "$currCmt`n--- Rejeté $(Get-Date -Format yyyy-MM-dd) ---`nNo usable URL" } }
    $logLines += "  - [$($rec.id)] $name - REJECTED: no URL"
    continue
  }

  # Sub-pipelines
  $lh = & "$ScriptDir\lighthouse-audit.ps1" -Url $url 2>$null | ConvertFrom-Json
  $fp = & "$ScriptDir\footprint-detect.ps1" -Url $url 2>$null | ConvertFrom-Json
  $ff = & "$ScriptDir\founder-find.ps1" -AgencyName $name -Domain $url 2>$null | ConvertFrom-Json

  # Score recalc
  $base       = if ($lh.perf -ne $null) { [math]::Min([double]$lh.perf / 10.0, 10.0) } else { 0.0 }
  $archBonus  = switch ($fp.strength) { 'strong' { 1.0 } 'medium' { 0.5 } default { 0.0 } }
  $ageBonus   = 0.0
  if ($fp.archetype -eq 'AR/03' -and $fp.age_under_24mo -eq $true) { $ageBonus = 1.0 }
  elseif ($fp.archetype -eq 'AR/03' -and $fp.age_hint) { $ageBonus = 0.5 }
  $multiBonus = if ($fp.archetype -eq 'multi') { 0.5 } else { 0.0 }
  $foundBonus = 0.0
  if ($ff.linkedin) { $foundBonus += 0.5 }
  if ($ff.email)    { $foundBonus += 0.5 }

  $computed = [math]::Min($base + $archBonus + $ageBonus + $multiBonus + $foundBonus, 10.0)
  $newQ     = [math]::Round([math]::Max($computed, $currQ), 2)  # don't downgrade

  # Build comment block
  $signalsTxt = if ($fp.signals.Count -gt 0) { ($fp.signals -join ', ') } else { 'none' }
  $perfTxt    = if ($lh.perf -ne $null) { "$($lh.perf)/100 (source=$($lh.source))" } else { "n/a ($($lh.source))" }
  $founderTxt = if ($ff.linkedin -or $ff.email) { "$($ff.linkedin) | $($ff.email)" } else { 'not found' }
  $ageTxt     = if ($fp.age_hint) { $fp.age_hint + ($(if ($fp.age_under_24mo) { ' (likely <24mo)' } else { '' })) } else { 'n/a' }

  $newComment = @"
$currCmt
--- Enrichi $(Get-Date -Format yyyy-MM-dd) ---
Archetype: $($fp.archetype) ($($fp.strength))
Signals: $signalsTxt
Lighthouse: $perfTxt
Founder: $founderTxt
Age: $ageTxt
Quality: $currQ -> $newQ
"@

  # Build PATCH payload — only set fields we have data for
  $fields = @{
    "Statut d'Enrichissement" = "2-Enrichi"
    "Note Globale de Qualité" = $newQ
    "Commentaires Internes"   = $newComment
  }
  if ($lh.perf -ne $null)  { $fields["Score de Friction Technique / Lighthouse"] = [int]$lh.perf }
  if ($ff.email)            { $fields["Email du Fondateur"]                       = $ff.email }
  if ($ff.linkedin)         { $fields["Lien LinkedIn du Fondateur"]               = $ff.linkedin }

  $updates += @{ id = $rec.id; fields = $fields }
  $founderFlag = if ($ff.linkedin -or $ff.email) { 'yes' } else { 'no' }
  Write-Ok "$($fp.archetype) | perf=$($lh.perf) | Q=$currQ to $newQ | founder=$founderFlag"
}

# --- 5. PATCH back in batches of 10 ---
$enriched = 0
$rejected = 0

function Send-Batch($items, $label) {
  if ($items.Count -eq 0) { return 0 }
  if ($DryRun) {
    Write-Step "DRY RUN - would PATCH $($items.Count) $label records"
    return $items.Count
  }
  $sent = 0
  for ($i = 0; $i -lt $items.Count; $i += 10) {
    $end = [math]::Min($i + 9, $items.Count - 1)
    $batch = $items[$i..$end]
    $body = @{ records = @($batch); typecast = $true } | ConvertTo-Json -Depth 10
    try {
      $resp = Invoke-RestMethod -Uri $ApiBase -Method Patch -Headers $Headers -Body $body -ErrorAction Stop
      $sent += $resp.records.Count
      Write-Ok "PATCHed batch of $($resp.records.Count) ($label)"
    } catch {
      Write-Fail "PATCH batch failed: $($_.Exception.Message)"
    }
  }
  return $sent
}

$enriched = Send-Batch $updates 'enriched'
$rejected = Send-Batch $rejects 'rejected'

# --- 6. Log to LLM_Wiki ---
$date = Get-Date -Format 'yyyy-MM-dd'
$skipped = $workCount - $enriched - $rejected
$logEntry = @"

## [$date] enrich  | $ServiceLabel - $workCount raw leads processed ($enriched enriched, $rejected rejected, $skipped skipped)

**Pipeline** : lighthouse (PSI/local) + footprint scan (HubSpot/Make/n8n/Stripe regex) + founder scrape (LinkedIn + mailto from /about, /team, /contact). Idempotent — only touches Statut='1-Raw'.

**Base** : $BaseId / $TableId
**Mode** : $(if ($DryRun) { 'DRY RUN' } else { 'LIVE' })
$($logLines -join "`n")
"@

if (-not $DryRun -and (Test-Path $WikiLog)) {
  Add-Content -Path $WikiLog -Value $logEntry
  Write-Ok "Logged to $WikiLog"
}

Write-Step "DONE - $enriched enriched, $rejected rejected, $skipped skipped (of $workCount processed)"
if ($enriched -eq 0 -and $rejected -eq 0 -and -not $DryRun -and $workCount -gt 0) { exit 5 }
exit 0
