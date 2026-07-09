# A0 Backup Ritual
# Usage: ./backup.ps1

$backupRoot = "C:\Aspace00\A0_Memory\Backups"
$timestamp = Get-Date -Format "yyyyMMdd-HHmm"
$targetDir = "$backupRoot\Backup-$timestamp"

Write-Host "=== A0 MEMORY SNAPSHOT ===" -ForegroundColor Cyan
Write-Host "Target: $targetDir"

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

# Critical Configs
Write-Host "Snapshotting Brain Configs..."
Copy-Item "C:\Aspace00\aspace_a0_amadeus\00_Amadeus\03_OpenClaw_Body\.openclaw\openclaw.json" "$targetDir\openclaw.json"
Copy-Item "C:\Aspace00\aspace_a0_amadeus\00_Amadeus\03_OpenClaw_Body\.env" "$targetDir\env.backup"

# User Data (Example)
# Write-Host "Snapshotting Rilcot OS Data..."
# docker run --rm --volumes-from supabase_db_rilcot-os -v $targetDir:/backup postgres pg_dumpall > $targetDir/db_dump.sql

Write-Host "[BACKUP COMPLETE]" -ForegroundColor Green
