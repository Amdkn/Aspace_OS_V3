$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$envPath = Join-Path $root ".env"

docker compose --project-name aspace-wikijs --env-file $envPath -f (Join-Path $root "docker-compose.yml") ps
if ($LASTEXITCODE -ne 0) {
    throw "docker compose ps failed. Docker Desktop may not be running."
}
