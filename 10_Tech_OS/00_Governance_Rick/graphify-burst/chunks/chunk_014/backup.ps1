$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$backupDir = Join-Path $root "backups"
if (!(Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir | Out-Null }
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFile = Join-Path $backupDir "mc_db_$ts.sql"
$container = "openclaw-mission-control-db-1"

# Dump DB from container
$dump = docker exec $container pg_dump -U postgres -d mission_control
$dump | Set-Content -Path $backupFile -Encoding UTF8

Write-Output "Backup written: $backupFile"
