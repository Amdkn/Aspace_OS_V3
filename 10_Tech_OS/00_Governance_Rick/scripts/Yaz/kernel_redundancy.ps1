# Agent Kernel Port Redundancy - Level C
# Author: Rick Supreme

$LogFile = "C:\Aspace00\logs\kernel_redundancy.log"
$McpConfigFile = "C:\Users\amado\.gemini\antigravity\mcp_config.json"

function Write-Log {
    param($Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$Timestamp] $Message" | Add-Content $LogFile
}

function Get-NextAvailablePort {
    param($StartPort)
    $port = $StartPort
    while ($true) {
        if (!(Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue)) {
            return $port
        }
        $port++
    }
}

Write-Log "--- Redundancy Engine Checking Channels ---"

# Check if Port 9222 is blocked by a non-Chrome process
$connection = Get-NetTCPConnection -LocalPort 9222 -ErrorAction SilentlyContinue
if ($connection) {
    $owner = Get-Process -Id $connection.OwningProcess -ErrorAction SilentlyContinue
    if ($owner.ProcessName -ne "chrome") {
        Write-Log "CONFLICT: Port 9222 occupied by $($owner.ProcessName). Negotiating new channel..."
        $newPort = Get-NextAvailablePort 9223
        Write-Log "New redundant channel assigned: $newPort"
        
        # Update MCP Config to use new port for Chrome tools if needed
        # (Cette partie nécessite un parsing JSON prudent pour éviter de corrompre la config)
        Write-Log "Ready to update mcp_config.json with port $newPort"
    }
}

Write-Log "--- Redundancy Engine Finished ---"
