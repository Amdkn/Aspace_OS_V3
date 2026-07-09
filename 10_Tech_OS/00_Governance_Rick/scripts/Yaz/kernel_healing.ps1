# Agent Kernel Heartbeat & Self-Healing - Level B
# Author: Rick Supreme

$LogFile = "C:\Aspace00\logs\kernel_healing.log"
$Targets = @(9222, 9223)

function Write-Log {
    param($Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$Timestamp] $Message" | Add-Content $LogFile
}

function Test-Heartbeat {
    param($Port)
    try {
        $connection = New-Object System.Net.Sockets.TcpClient
        $connection.Connect("127.0.0.1", $Port)
        $connection.Close()
        return $true
    } catch {
        return $false
    }
}

Write-Log "--- Heartbeat & Self-Healing Engine Active ---"

foreach ($Port in $Targets) {
    if (!(Test-Heartbeat $Port)) {
        Write-Log "CRITICAL: Heartbeat failed on Port $Port. Initiating Self-Healing..."
        
        # 1. Identify owner
        $processId = (Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue).OwningProcess
        if ($processId) {
            Write-Log "Hard-killing Zombie Process $processId on Port $Port..."
            Stop-Process -Id $processId -Force
        }
        
        # 2. Port Switching Logic (Level C Preliminary)
        if ($Port -eq 9222) {
            Write-Log "Switching potential Chrome traffic to fallback port 9223..."
        }
    }
}
