# lighthouse-audit.ps1 — Get Lighthouse perf score for a URL.
# Strategy: PageSpeed Insights API (no install, no auth) → fallback local `lighthouse` CLI if installed.
# Usage:  lighthouse-audit.ps1 -Url <agency-url>
# Output: single JSON object to stdout
#
# Returns:
#   { "url": "...", "perf": 0-100, "tti_ms": int, "total_bytes": int, "source": "psi"|"local"|"none", "error": null|string }
#
# Exit codes: 0 success (perf available), 0 partial (perf=null but no crash), 3 hard fail.

[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Url,
  [string]$PsiApiKey  = $env:GOOGLE_PSI_API_KEY,
  [int]$TimeoutSec    = 60
)

$ErrorActionPreference = 'Stop'

if ($Url -notmatch '^https?://') { $Url = "https://$Url" }

function Out-Result([hashtable]$obj) {
  Write-Output ([pscustomobject]$obj | ConvertTo-Json -Compress -Depth 5)
}

# --- Strategy 1: PageSpeed Insights API (free, low rate) ---
try {
  $psiUrl = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$([System.Uri]::EscapeDataString($Url))&strategy=desktop&category=performance"
  if ($PsiApiKey) { $psiUrl += "&key=$PsiApiKey" }

  $resp = Invoke-RestMethod -Uri $psiUrl -TimeoutSec $TimeoutSec -ErrorAction Stop
  $perf = [int]([math]::Round($resp.lighthouseResult.categories.performance.score * 100))
  $tti  = [int]$resp.lighthouseResult.audits.interactive.numericValue
  $tot  = [int]$resp.lighthouseResult.audits.'total-byte-weight'.numericValue

  Out-Result @{
    url         = $Url
    perf        = $perf
    tti_ms      = $tti
    total_bytes = $tot
    source      = 'psi'
    error       = $null
  }
  exit 0
} catch {
  $psiError = $_.Exception.Message
  # fall through to local lighthouse
}

# --- Strategy 2: local `lighthouse` CLI (npm i -g lighthouse) ---
$lh = Get-Command lighthouse -ErrorAction SilentlyContinue
if ($lh) {
  try {
    $tmpJson = Join-Path $env:TEMP "lh-$(Get-Random).json"
    & lighthouse $Url --output=json --output-path=$tmpJson --only-categories=performance --quiet --chrome-flags="--headless --no-sandbox" 2>$null | Out-Null
    if (Test-Path $tmpJson) {
      $r = Get-Content $tmpJson -Raw | ConvertFrom-Json
      $perf = [int]([math]::Round($r.categories.performance.score * 100))
      $tti  = [int]$r.audits.interactive.numericValue
      $tot  = [int]$r.audits.'total-byte-weight'.numericValue
      Remove-Item $tmpJson -Force
      Out-Result @{ url = $Url; perf = $perf; tti_ms = $tti; total_bytes = $tot; source = 'local'; error = $null }
      exit 0
    }
  } catch {
    # fall through
  }
}

# --- Both strategies failed: report partial ---
Out-Result @{
  url         = $Url
  perf        = $null
  tti_ms      = $null
  total_bytes = $null
  source      = 'none'
  error       = "PSI: $psiError; local lighthouse not available or failed"
}
exit 0   # not a hard fail — pipeline continues with null perf
