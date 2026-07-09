# Omega Bridge Protocol - System-to-Agent Communication
# Author: Rick Supreme

$BridgeDir = "C:\Aspace00\bridge"
$SignalFile = "$BridgeDir\signals.json"
$LogFile = "$BridgeDir\events.log"

if (!(Test-Path $BridgeDir)) { New-Item -ItemType Directory $BridgeDir -Force }

function Send-SovereignSignal {
    param(
        [string]$Type,
        [string]$Level,
        [string]$Message,
        [hashtable]$Metadata = @{}
    )
    
    $Signal = @{
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        type = $Type
        level = $Level
        message = $Message
        metadata = $Metadata
    }
    
    $Signal | ConvertTo-Json -Compress | Out-File -FilePath $SignalFile -Append
    # Fix: $(Type) instead of $Type to avoid drive collision in strings
    "[$($Signal.timestamp)][$Level] $($Type): $Message" | Out-File -FilePath $LogFile -Append
}
