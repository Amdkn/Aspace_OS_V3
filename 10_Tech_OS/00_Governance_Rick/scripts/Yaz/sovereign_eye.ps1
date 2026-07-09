# Sovereign Eye - Chrome Debugging Watchdog & Launcher
# Author: Rick Supreme
# Version: 2.0 (Persistent Mode)

$ErrorActionPreference = "SilentlyContinue"
$ChromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$Port = 9222
$Profile = "Default"
$LogPath = "C:\Aspace00\logs\sovereign_eye.log"

if (!(Test-Path "C:\Aspace00\logs")) { New-Item -ItemType Directory "C:\Aspace00\logs" }

function Write-SovereignLog {
    param($Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $FormattedMessage = "[$Timestamp] $Message"
    echo $FormattedMessage
    $FormattedMessage | Out-File -FilePath $LogPath -Append
}

Write-SovereignLog "--- Sovereign Eye V2: Engaging Persistent Vision ---"

# 1. Check if Chrome is already running with debugging on 9222
$conn = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($conn) {
    Write-SovereignLog "Sovereign Eye already active on Port $Port. Vision synchronized."
    exit 0
}

# 2. Check for zombie processes holding the profile
Write-SovereignLog "Checking for Chrome instances..."
$chromeProcesses = Get-Process chrome -ErrorAction SilentlyContinue
if ($chromeProcesses) {
    Write-SovereignLog "Found existing Chrome instances. Attempting to inject debugging flags..."
    # Note: On Windows, you can't easily inject a flag into a running process. 
    # Must restart to enable DevTools.
    Stop-Process -Name "chrome" -Force
    Start-Sleep -Seconds 2
}

# 3. Clear SingletonLock
$LockFile = "$env:LOCALAPPDATA\Google\Chrome\User Data\SingletonLock"
if (Test-Path $LockFile) {
    Write-SovereignLog "Clearing session lock..."
    Remove-Item $LockFile -Force
}

# 4. Launch with Restore and Debugging
Write-SovereignLog "Launching Sovereign Chrome (Profile: $Profile, Port: $Port)..."
Start-Process $ChromePath -ArgumentList "--remote-debugging-port=$Port", "--profile-directory=$Profile", "--restore-last-session", "--no-first-run"

# 5. Verification Loop
$timeout = 20
$elapsed = 0
while ($elapsed -lt $timeout) {
    $conn = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    if ($conn) {
        Write-SovereignLog "SUCCESS: Vision Restored. Sovereign Eye is Listening."
        exit 0
    }
    Start-Sleep -Seconds 1
    $elapsed++
}

Write-SovereignLog "CRITICAL: Sovereign Eye failed to bind port. Check manual locks."
exit 1
