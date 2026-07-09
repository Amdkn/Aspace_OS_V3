$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$compose = Join-Path $root "compose.yml"
$envFile = Join-Path $root ".env"

function Restart-Stack {
  docker compose -f $compose --env-file $envFile restart | Out-Null
}

try {
  $resp = Invoke-WebRequest -Uri "http://localhost:8000/healthz" -UseBasicParsing -TimeoutSec 5
  if ($resp.StatusCode -ne 200) { Restart-Stack }
} catch {
  Restart-Stack
}

# If any container is unhealthy/exited, restart
$ps = docker compose -f $compose --env-file $envFile ps --format json | ConvertFrom-Json
$bad = $false
foreach ($c in $ps) {
  if ($c.State -match "exited|unhealthy") { $bad = $true }
}
if ($bad) { Restart-Stack }
