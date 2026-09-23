$ErrorActionPreference = 'Stop'
$health = 'http://127.0.0.1:43118/health'
try {
  $r = Invoke-RestMethod $health -TimeoutSec 2
  if ($r.ok) { exit 0 }
} catch {}

$existing = Get-CimInstance Win32_Process | Where-Object {
  $_.CommandLine -match 'jules_mcp_proxy\.mjs'
}
if ($existing) {
  Start-Sleep -Seconds 2
  try {
    $r = Invoke-RestMethod $health -TimeoutSec 2
    if ($r.ok) { exit 0 }
  } catch {}
  throw "Jules proxy process exists but health endpoint is unavailable; refusing duplicate launch."
}

$env:GOOGLE_JULES_API_KEY = [Environment]::GetEnvironmentVariable('GOOGLE_JULES_API_KEY','User')
if (-not $env:GOOGLE_JULES_API_KEY) { throw 'GOOGLE_JULES_API_KEY missing from USER environment' }
node 'C:\Users\amado\ASpace_OS_V3\10_Tech_OS\kernel\jules_mcp_proxy.mjs'
