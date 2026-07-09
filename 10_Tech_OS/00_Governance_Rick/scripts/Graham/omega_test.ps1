# Omega Test - Pulse Check
# Author: Rick Supreme

. "C:\Aspace00\scripts\omega_bridge.ps1"
. "C:\Aspace00\scripts\omega_audio.ps1"

Write-Host "--- Gravity Claw Pulse Check ---" -ForegroundColor Cyan

# Test des signaux et sons
Write-Host "Testing Signal: SUCCESS..."
Send-SovereignSignal -Type "SYSTEM" -Level "SUCCESS" -Message "Omega Bridge Operational"
Play-SovereignSound -SoundName "success"
Start-Sleep -Seconds 1

Write-Host "Testing Signal: NOTIFY..."
Send-SovereignSignal -Type "BMAD" -Level "NOTIFY" -Message "Waiting for Architect"
Play-SovereignSound -SoundName "notify"
Start-Sleep -Seconds 1

Write-Host "Testing Signal: ALERT..."
Send-SovereignSignal -Type "KERNEL" -Level "ALERT" -Message "Testing Healing Cycle"
Play-SovereignSound -SoundName "alert"

Write-Host "Pulse Check Complete." -ForegroundColor Green
