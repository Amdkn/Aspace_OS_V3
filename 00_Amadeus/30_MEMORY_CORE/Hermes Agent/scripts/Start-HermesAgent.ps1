$ErrorActionPreference = "Stop"

$distro = "ASpace-L0"
$memoryRoot = "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent"
$logDir = Join-Path $memoryRoot "logs"
$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logFile = Join-Path $logDir "hermes-startup-$stamp.log"

New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Write-Log {
    param([string]$Message)
    $line = "$(Get-Date -Format o) $Message"
    Add-Content -Path $logFile -Value $line
}

Write-Log "Hermes Agent startup bootstrap begin."
Write-Log "Distro: $distro"

$windowsScript = Join-Path $memoryRoot "scripts\start-hermes-agent.sh"
Write-Log "Windows bootstrap script: $windowsScript"

$scriptBody = (Get-Content -Raw -Path $windowsScript).Replace("`r`n", "`n").Replace("`r", "`n")
$payload = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($scriptBody))
$output = & wsl.exe -d $distro -- bash -lc "printf '%s' '$payload' | base64 -d | bash" 2>&1
$exitCode = $LASTEXITCODE
$output | ForEach-Object { Write-Log $_ }
Write-Log "WSL bootstrap exit code: $exitCode"

if ($exitCode -ne 0) {
    throw "Hermes Agent startup bootstrap failed with exit code $exitCode. See $logFile"
}

Write-Log "Hermes Agent startup bootstrap complete."
