param (
    [Parameter(Position=0)]
    [string]$Action = "start"
)

$ErrorActionPreference = "Stop"

$scriptPath = $MyInvocation.MyCommand.Path
$repoRoot = Split-Path $scriptPath -Parent

# Map actions directly to the dc_recovery_daemon.py CLI
$daemonPath = Join-Path $repoRoot "10_Tech_OS\kernel\dc_recovery_daemon.py"

if (-not (Test-Path $daemonPath)) {
    Write-Error "repo_root unavailable; pass -RepoRoot or run from the repository ($daemonPath not found)"
    exit 1
}

& python $daemonPath $Action
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
