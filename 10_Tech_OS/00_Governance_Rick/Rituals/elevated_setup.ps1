# Elevated A0 Ritual Installer
# This script must be run as Administrator to register the scheduled tasks.

$StatusScript = "C:\Aspace00\Rituals\A0-Status.ps1"
$TaskName = "A0-Ritual-90m"

Write-Host "Registering A0 Ritual: $TaskName" -ForegroundColor Cyan

# Create Task
schtasks /Create /F /RL HIGHEST /RU SYSTEM /SC MINUTE /MO 90 /TN $TaskName /TR "powershell -NoProfile -ExecutionPolicy Bypass -File $StatusScript"

# Run once
schtasks /Run /TN $TaskName

Write-Host "Victory. Ritual heartbeat is active." -ForegroundColor Green
Pause
