# founder-find.ps1 — Best-effort founder LinkedIn + email lookup.
# Usage:  founder-find.ps1 -AgencyName "Modgility" [-Domain "modgility.com"]
# Output: JSON to stdout
#
# Returns: { "agency": "...", "linkedin": "https://linkedin.com/in/..."|null, "email": "...@..."|null, "source": "html-scrape"|"google"|"apollo"|"none" }
#
# Strategy (cheapest first):
#   1. Scrape the agency homepage for `linkedin.com/in/...` + `mailto:` patterns
#   2. Scrape /about, /team, /contact subpages
#   3. (FUTURE) Apollo MCP / Hunter / web search — not implemented yet, returns null
#
# This script is intentionally non-failing: if nothing found, returns nulls and exit 0.
# The downstream enrich pipeline tolerates missing founder data.

[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$AgencyName,
  [string]$Domain,
  [int]$TimeoutSec = 12
)

$ErrorActionPreference = 'Continue'  # don't crash on any single subpage fail

function Out-Result([hashtable]$obj) {
  Write-Output ([pscustomobject]$obj | ConvertTo-Json -Compress)
}

if (-not $Domain) {
  # Derive a guess from the agency name
  $Domain = ($AgencyName -replace '[^a-zA-Z0-9]', '').ToLower() + '.com'
}
$base = if ($Domain -match '^https?://') { $Domain } else { "https://$Domain" }

$linkedinUrl = $null
$email       = $null
$sourceTag   = 'none'

$pathsToTry = @('', '/about', '/about-us', '/team', '/contact', '/founder', '/leadership')

foreach ($p in $pathsToTry) {
  try {
    $u = "$base$p"
    $resp = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec $TimeoutSec `
              -UserAgent 'Mozilla/5.0 (compatible; ASpace-Enrich/1.0)' `
              -MaximumRedirection 4 -ErrorAction Stop
    $h = $resp.Content

    if (-not $linkedinUrl -and $h -match 'https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9\-_/%]+') {
      $linkedinUrl = $Matches[0] -replace '["''\s<>].*$', ''
      $sourceTag   = 'html-scrape'
    }
    if (-not $email -and $h -match 'mailto:([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})') {
      $candidate = $Matches[1]
      # Filter generic role inboxes — these aren't "founder" emails
      if ($candidate -notmatch '^(info|hello|contact|support|sales|hi|team|admin|noreply|no-reply)@') {
        $email = $candidate
        if ($sourceTag -eq 'none') { $sourceTag = 'html-scrape' }
      }
    }
    if ($linkedinUrl -and $email) { break }
  } catch {
    # silent — try next path
  }
}

# Future hooks: Apollo MCP, Hunter API, Google search via WebSearch
# For now, return what we have.

Out-Result @{
  agency   = $AgencyName
  linkedin = $linkedinUrl
  email    = $email
  source   = $sourceTag
}
exit 0
