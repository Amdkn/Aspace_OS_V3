# Ghost Shell Bootstrapper
# Author: Rick Supreme

$LogFile = "C:\Aspace00\logs\ghost_shell_boot.log"

function Write-Log {
    param($Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$Timestamp] $Message" | Add-Content $LogFile
}

Write-Log "Initializing Ghost Shell Local VPS..."

# Wake up WSL2 and run initialization
try {
    Write-Log "Waking up WSL2 Ubuntu-24.04 as amdkn7..."
    wsl -d Ubuntu-24.04 -u amdkn7 -- bash -c "~/scripts/vps_boot.sh"
    Write-Log "WSL2 Initialization triggered successfully."
} catch {
    Write-Log "ERROR: Failed to trigger WSL2 script: $_"
}

Write-Log "Ghost Shell Bootstrapper finished."
