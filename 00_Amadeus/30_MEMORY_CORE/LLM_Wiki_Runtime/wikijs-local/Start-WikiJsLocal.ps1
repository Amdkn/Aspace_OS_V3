$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$envPath = Join-Path $root ".env"

if (-not (Test-Path -LiteralPath $envPath)) {
    & (Join-Path $root "Initialize-WikiJsLocal.ps1")
}

docker compose --project-name aspace-wikijs --env-file $envPath -f (Join-Path $root "docker-compose.yml") up -d
if ($LASTEXITCODE -ne 0) {
    throw "docker compose up failed. Start Docker Desktop, then rerun Start-WikiJsLocal.ps1."
}
Write-Output "Wiki.js should be available at http://127.0.0.1:3080 after containers finish starting."
