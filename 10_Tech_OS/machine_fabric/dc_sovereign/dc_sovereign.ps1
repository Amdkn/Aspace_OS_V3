param(
  [Parameter(Mandatory=$true)]
  [ValidateSet('install','start','stop','restart','status','update','uninstall')]
  [string]$Command
)

$ErrorActionPreference = 'Stop'
$DaemonScript = Join-Path $PSScriptRoot "dc_sovereign_daemon.py"
$StateDir = Join-Path $env:USERPROFILE ".aspace\dc_sovereign"
$StateFile = Join-Path $StateDir "state.json"
$TaskName = "ASpace DCSovereign Daemon"

if (-not (Test-Path $StateDir)) {
    New-Item -ItemType Directory -Force -Path $StateDir | Out-Null
}

function Get-State {
    if (Test-Path $StateFile) {
        return (Get-Content -Raw $StateFile | ConvertFrom-Json)
    }
    return @{}
}

function Save-State {
    param([hashtable]$State)
    $State | ConvertTo-Json | Set-Content -Path $StateFile -Encoding UTF8
}

function Is-Running {
    param([int]$pid)
    if ($pid -eq 0 -or $null -eq $pid) { return $false }
    try {
        $proc = Get-Process -Id $pid -ErrorAction SilentlyContinue
        return ($null -ne $proc)
    } catch {
        return $false
    }
}

switch ($Command) {
    'status' {
        $state = Get-State
        $daemonPid = if ($null -ne $state.daemon_pid) { $state.daemon_pid } else { 0 }
        $workerPid = if ($null -ne $state.worker_pid) { $state.worker_pid } else { 0 }

        $daemonRunning = Is-Running -pid $daemonPid
        $workerRunning = Is-Running -pid $workerPid

        # probe health of worker process/gateway
        $health = "UNKNOWN"
        if ($workerRunning) {
            try {
                $response = Invoke-RestMethod -Uri "http://127.0.0.1:8002/health" -Method Get -TimeoutSec 2 -ErrorAction SilentlyContinue
                if ($null -ne $response) {
                    $health = "ONLINE"
                } else {
                    $health = "DEGRADED"
                }
            } catch {
                $health = "DEGRADED"
            }
        } else {
            $health = "DOWN"
        }

        $result = @{
            daemon_pid = $daemonPid
            daemon_running = $daemonRunning
            worker_pid = $workerPid
            worker_running = $workerRunning
            worker_health = $health
            status = if ($daemonRunning) { "UP" } else { "DOWN" }
        }
        $result | ConvertTo-Json | Write-Host
        if (-not $daemonRunning) { throw "Daemon is not running" }
    }
    'start' {
        $state = Get-State
        $daemonPid = if ($null -ne $state.daemon_pid) { $state.daemon_pid } else { 0 }
        if (Is-Running -pid $daemonPid) {
            Write-Host "DC Sovereign daemon is already running (PID: $daemonPid)."
            return
        }
        Write-Host "Starting DC Sovereign daemon via Scheduled Task / background..."

        $python = "python"

        # We use Scheduled Task if it exists, otherwise fallback to Start-Process for tests
        $taskExists = $false
        if ($PSVersionTable.OS -match "Windows") {
            try {
                $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
                if ($null -ne $task) {
                    $taskExists = $true
                }
            } catch {}
        }

        if ($taskExists) {
            Start-ScheduledTask -TaskName $TaskName
        } else {
            Start-Process -FilePath $python -ArgumentList $DaemonScript -WindowStyle Hidden
        }

        Start-Sleep -Seconds 2

        $newState = Get-State
        if (Is-Running -pid $newState.daemon_pid) {
            Write-Host "Started successfully."
        } else {
            Write-Error "Failed to start daemon."
            throw "Failed to start daemon"
        }
    }
    'stop' {
        $state = Get-State
        $daemonPid = if ($null -ne $state.daemon_pid) { $state.daemon_pid } else { 0 }
        $workerPid = if ($null -ne $state.worker_pid) { $state.worker_pid } else { 0 }

        if (Is-Running -pid $daemonPid) {
            Stop-Process -Id $daemonPid -Force -ErrorAction SilentlyContinue
            Write-Host "Stopped daemon ($daemonPid)."
        }
        if (Is-Running -pid $workerPid) {
            Stop-Process -Id $workerPid -Force -ErrorAction SilentlyContinue
            Write-Host "Stopped worker ($workerPid)."
        }

        $state.daemon_pid = $null
        $state.worker_pid = $null
        $state.status = "stopped"
        Save-State -State $state
    }
    'restart' {
        & $PSCommandPath -Command "stop"
        & $PSCommandPath -Command "start"
    }
    'install' {
        Write-Host "Installing DC Sovereign..."
        if ($PSVersionTable.OS -match "Windows") {
            try {
                # Create Logon task
                $action = New-ScheduledTaskAction -Execute "python" -Argument $DaemonScript
                $trigger = New-ScheduledTaskTrigger -AtLogOn
                $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest
                $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -DontStopOnIdleEnd -ExecutionTimeLimit (New-TimeSpan -Days 3650)
                Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force
                Write-Host "Created Windows Scheduled Task '$TaskName'."
            } catch {
                Write-Warning "Could not create Scheduled Task (are you admin?). This step is LOCAL-ONLY."
            }
        } else {
            Write-Host "Skipping Scheduled Task creation on non-Windows environment (LOCAL-ONLY)."
        }
        Write-Host "Done."
    }
    'update' {
        Write-Host "Updating DC Sovereign..."
        & $PSCommandPath -Command "restart"
    }
    'uninstall' {
        & $PSCommandPath -Command "stop"
        if ($PSVersionTable.OS -match "Windows") {
            try {
                Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
                Write-Host "Removed Windows Scheduled Task '$TaskName'."
            } catch {
                Write-Warning "Failed to remove Scheduled Task."
            }
        }
        if (Test-Path $StateDir) {
            Remove-Item -Path $StateDir -Recurse -Force
        }
        Write-Host "Uninstalled DC Sovereign artifacts."
    }
}
