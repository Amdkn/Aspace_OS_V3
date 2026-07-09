# footprint-detect.ps1 — Fetch URL HTML + scan for Solaris archetype signals.
# Usage:  footprint-detect.ps1 -Url <agency-url>
# Output: JSON to stdout (single object)
#
# Returns:
#   {
#     "url": "...",
#     "http_status": 200,
#     "archetype": "AR/01" | "AR/02" | "AR/03" | "AR/04" | "multi" | "unknown",
#     "strength":  "strong" | "medium" | "weak" | "none",
#     "signals":   ["HubSpot Form", "Stripe Pricing Table", ...],
#     "age_hint":  "© 2024" | null,
#     "age_under_24mo": true | false | null
#   }
#
# Exit codes: 0 success, 3 fetch failed, 4 invalid URL.

[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Url,
  [int]$TimeoutSec = 15
)

$ErrorActionPreference = 'Stop'

# Normalize URL
if ($Url -notmatch '^https?://') { $Url = "https://$Url" }
try { $null = [Uri]::new($Url) } catch { Write-Output (@{ url = $Url; http_status = 0; archetype = "unknown"; strength = "none"; signals = @(); age_hint = $null; age_under_24mo = $null; error = "invalid URL" } | ConvertTo-Json -Compress); exit 4 }

# Fetch HTML (follow redirects, basic UA)
$html = $null
$status = 0
try {
  $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec $TimeoutSec `
            -UserAgent 'Mozilla/5.0 (compatible; ASpace-Enrich/1.0)' `
            -MaximumRedirection 5 -ErrorAction Stop
  $html   = $resp.Content
  $status = $resp.StatusCode
} catch {
  $msg = $_.Exception.Message
  Write-Output (@{ url = $Url; http_status = 0; archetype = "unknown"; strength = "none"; signals = @(); age_hint = $null; age_under_24mo = $null; error = $msg } | ConvertTo-Json -Compress)
  exit 3
}

# Signal table — see references/archetype-signals.md for rationale
$signalDefs = @(
  @{ name = 'HubSpot Form';            archetype = 'AR/01'; strength = 'strong'; pattern = 'js\.hsforms\.net|hsforms\.net/forms/embed|js\.hs-scripts\.com' }
  @{ name = 'HubSpot Tracking';        archetype = 'AR/01'; strength = 'medium'; pattern = 'js\.hs-analytics\.net|data-hsjs|_hsq\.push' }
  @{ name = 'HubSpot Partner Badge';   archetype = 'AR/01'; strength = 'medium'; pattern = 'hubspot-partner|solutions/hubspot|class="hs-' }
  @{ name = 'Zapier Webhook';          archetype = 'AR/01'; strength = 'medium'; pattern = 'hooks\.zapier\.com|zapier\.com/embed' }
  @{ name = 'Stripe Pricing Table';    archetype = 'AR/01'; strength = 'weak';   pattern = 'js\.stripe\.com/v3|buy\.stripe\.com|stripe-pricing-table' }
  @{ name = 'Calendly';                archetype = 'AR/01'; strength = 'weak';   pattern = 'calendly\.com/|savvycal\.com/' }

  @{ name = 'Make.com Footprint';      archetype = 'AR/03'; strength = 'strong'; pattern = 'make\.com/scenario|integromat\.com|eu1\.make\.com|us1\.make\.com' }
  @{ name = 'n8n Footprint';           archetype = 'AR/03'; strength = 'strong'; pattern = 'n8n\.cloud|n8n\.io/community|<n8n-' }
  @{ name = 'OpenAI Reference';        archetype = 'AR/03'; strength = 'weak';   pattern = 'openai\.com|gpt-4|gpt-3\.5|anthropic\.com|claude API' }

  @{ name = 'YouTube/Vimeo Embed';     archetype = 'AR/02'; strength = 'medium'; pattern = 'youtube\.com/embed|player\.vimeo\.com/' }
  @{ name = 'Studio/Production kw';    archetype = 'AR/02'; strength = 'medium'; pattern = '\bstudio\b|production house|video production|creative production' }

  @{ name = 'Fractional CMO';          archetype = 'AR/04'; strength = 'strong'; pattern = 'fractional cmo|part-time cmo|interim marketing' }
)

$signalsHit = @()
$archScores = @{ 'AR/01' = 0; 'AR/02' = 0; 'AR/03' = 0; 'AR/04' = 0 }
$strengthWeight = @{ 'strong' = 3; 'medium' = 2; 'weak' = 1 }
$bestStrength = 'none'

foreach ($sd in $signalDefs) {
  if ($html -imatch $sd.pattern) {
    $signalsHit += $sd.name
    $archScores[$sd.archetype] += $strengthWeight[$sd.strength]
    if ($strengthWeight[$sd.strength] -gt $strengthWeight[$bestStrength]) {
      $bestStrength = $sd.strength
    }
  }
}
if ($bestStrength -eq 'none') { $bestStrength = 'none' }

# Winner archetype
$winning = $archScores.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1
$archetype = if ($winning.Value -eq 0) { 'unknown' } else { $winning.Key }

# Multi-archetype detection: ≥2 archetypes with strong-equivalent score (>= 3)
$strongCount = ($archScores.Values | Where-Object { $_ -ge 3 }).Count
if ($strongCount -ge 2) { $archetype = 'multi' }

# Age hint — look for copyright year or "Founded in YYYY"
$ageHint = $null
$ageUnder24 = $null
if ($html -match '(?:©|&copy;|Copyright)\s*(\d{4})') {
  $ageHint = "© $($Matches[1])"
  $year = [int]$Matches[1]
  $monthsAgo = ((Get-Date).Year - $year) * 12 + (Get-Date).Month
  $ageUnder24 = ($monthsAgo -le 24)
}
elseif ($html -match '(?i)founded in (\d{4})|since (\d{4})') {
  $yearStr = if ($Matches[1]) { $Matches[1] } else { $Matches[2] }
  $year = [int]$yearStr
  $ageHint = "Founded $year"
  $monthsAgo = ((Get-Date).Year - $year) * 12 + (Get-Date).Month
  $ageUnder24 = ($monthsAgo -le 24)
}

# Emit JSON
$out = [ordered]@{
  url              = $Url
  http_status      = $status
  archetype        = $archetype
  strength         = $bestStrength
  signals          = $signalsHit
  archetype_scores = $archScores
  age_hint         = $ageHint
  age_under_24mo   = $ageUnder24
}
Write-Output ($out | ConvertTo-Json -Compress -Depth 5)
exit 0
