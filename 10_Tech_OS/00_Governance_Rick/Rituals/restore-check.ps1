# A0 Restore Check Ritual
# Usage: ./restore-check.ps1

Write-Host "=== RESTORE DRILL (SIMULATION) ===" -ForegroundColor Yellow

$latestBackup = Get-ChildItem "C:\Aspace00\A0_Memory\Backups" | Sort-Object CreationTime -Descending | Select-Object -First 1

if ($null -eq $latestBackup) {
    Write-Host "[FAIL] No backups found in A0_Memory." -ForegroundColor Red
    exit 1
}

Write-Host "Latest Artifact: $($latestBackup.Name)"
Write-Host "Verifying Integrity..."

$configPath = "$($latestBackup.FullName)\openclaw.json"
if (Test-Path $configPath) {
    $json = Get-Content $configPath | Out-String | ConvertFrom-Json
    if ($json.gateway.mode -eq "local") {
        Write-Host " - Config Logic: VALID" -ForegroundColor Green
    } else {
        Write-Host " - Config Logic: INVALID" -ForegroundColor Red
    }
} else {
    Write-Host " - Config File: MISSING" -ForegroundColor Red
}

Write-Host "[DRILL COMPLETE]" -ForegroundColor Cyan
