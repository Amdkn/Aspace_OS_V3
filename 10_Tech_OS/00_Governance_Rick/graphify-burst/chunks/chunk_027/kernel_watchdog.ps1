# Agent Kernel Watchdog - Level A
# Author: Rick Supreme

$ErrorActionPreference = "SilentlyContinue"
$LogFile = "C:\Aspace00\logs\kernel_watchdog.log"

function Write-Log {
    param($Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$Timestamp] $Message" | Add-Content $LogFile
}

Write-Log "--- Agent Kernel Watchdog Started ---"

while ($true) {
    # 1. Check for hanging Python processes (Zombies)
    $zombies = Get-Process python -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -eq "" -and $_.CPU -lt 0.01 }
    foreach ($zombie in $zombies) {
        Write-Log "Detected potential zombie Python process ($($zombie.Id)). Monitoring..."
    }

    # 2. Check Port 9222 (Chrome DevTools)
    $port9222 = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
    if (!$port9222) {
        Write-Log "ALERT: Port 9222 (Chrome) is DOWN. Waiting for auto-restart by IDE..."
    }

    # 3. Check Sovereign Terminal
    # Note: On cherche le serveur fastmcp
    $mcpServer = Get-Process python -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*sovereign_terminal*" }
    if (!$mcpServer) {
        Write-Log "ALERT: Sovereign Terminal process is MISSING. Triggering restart protocol..."
        # Trigger IDE reload via config touch
        (Get-Item "C:\Users\amado\.gemini\antigravity\mcp_config.json").LastWriteTime = Get-Date
    }

    Start-Sleep -Seconds 10
}
