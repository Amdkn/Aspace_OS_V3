$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$envPath = Join-Path $root ".env"

docker compose --project-name aspace-wikijs --env-file $envPath -f (Join-Path $root "docker-compose.yml") down
if ($LASTEXITCODE -ne 0) {
    throw "docker compose down failed."
}
