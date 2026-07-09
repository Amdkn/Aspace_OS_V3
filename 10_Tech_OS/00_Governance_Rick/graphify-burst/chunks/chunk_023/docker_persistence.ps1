# Strategic Persistence & Self-Healing Script
# Author: Rick Supreme

$DockerPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
$ChromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$LogFile = "C:\Aspace00\logs\docker_persistence.log"

function Write-Log {
    param($Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$Timestamp] $Message" | Out-File -FilePath $LogFile -Append
}

if (!(Test-Path "C:\Aspace00\logs")) { New-Item -ItemType Directory -Path "C:\Aspace00\logs" }

Write-Log "Starting Strategic Persistence Check..."

# 1. Ensure Docker Desktop
if (!(Get-Process "Docker Desktop" -ErrorAction SilentlyContinue)) {
    Write-Log "Docker Desktop is not running. Starting..."
    Start-Process $DockerPath
    while (!(docker info 2>$null)) { Start-Sleep -Seconds 5 }
}

# 2. Check Critical Containers
$Containers = @(
    "supabase_db_rilcot-os_1_",
    "openclaw-gateway",
    "03_openclaw_body-sovereign-bot-1",
    "03_openclaw_body-n8n-1"
)

foreach ($name in $Containers) {
    if (docker inspect $name 2>$null) {
        $Status = docker inspect --format '{{.State.Status}}' $name
        if ($Status -ne "running") {
            Write-Log "Container $name is $Status. Restarting..."
            docker start $name
        }
    }
}

# 3. Ensure Ollama
if (!(Get-Process "ollama" -ErrorAction SilentlyContinue)) {
    Write-Log "Ollama process not found. Starting..."
    if (Test-Path "$env:LOCALAPPDATA\Ollama\ollama app.exe") {
        Start-Process "$env:LOCALAPPDATA\Ollama\ollama app.exe"
    }
}

# 4. Ensure Sovereign Browser (Chrome Debugging)
$BrowserProcess = Get-CimInstance Win32_Process -Filter "Name = 'chrome.exe' AND CommandLine LIKE '%--remote-debugging-port=9222%'"
if (!$BrowserProcess) {
    Write-Log "Sovereign Browser (Port 9222) not found. Starting..."
    Start-Process $ChromePath -ArgumentList "--remote-debugging-port=9222", "--no-first-run", "--no-default-browser-check"
}

Write-Log "Strategic Persistence Check Completed."
