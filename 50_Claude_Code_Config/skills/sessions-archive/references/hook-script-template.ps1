# session-start-current.ps1 — TEMPLATE
# Recreate this file at C:\Users\amado\.claude\bin\session-start-current.ps1
# if it is missing. Wired in ~/.claude/settings.json hooks.SessionStart.
# Purpose: resolve the 'current' alias at every Claude Code startup and signal
#          the active session ID so A0 can /sessions load current in 1 command.

$ErrorActionPreference = 'SilentlyContinue'

$aliasesPath = Join-Path $env:USERPROFILE '.claude\session-aliases.json'
$marker = '[session-start]'

if (-not (Test-Path $aliasesPath)) {
    Write-Host "$marker No aliases file yet ($aliasesPath). Run /sessions alias to create one."
    exit 0
}

try {
    $raw = Get-Content $aliasesPath -Raw
    $aliases = $raw | ConvertFrom-Json
    $current = $aliases.aliases.current
}
catch {
    Write-Host "$marker Could not parse aliases file: $_"
    exit 0
}

if (-not $current) {
    Write-Host "$marker No 'current' alias set. Create one via /sessions alias <id> current."
    exit 0
}

$projectsDir = Join-Path $env:USERPROFILE '.claude\projects\C--Users-amado'
$sessPath = Join-Path $projectsDir $current.sessionPath

if (Test-Path $sessPath) {
    $sizeKB = [math]::Round((Get-Item $sessPath).Length / 1KB, 1)
    Write-Host ""
    Write-Host "================================================================="
    Write-Host "  $marker ACTIVE SESSION 'current'"
    Write-Host "  File   : $($current.sessionPath)"
    Write-Host "  Size   : $sizeKB KB"
    Write-Host "  Resume : /sessions load current"
    Write-Host "================================================================="
    Write-Host ""
}
else {
    Write-Host "$marker WARNING: 'current' alias points to missing file:"
    Write-Host "         $sessPath"
    Write-Host "         Update via /sessions alias <id> current"
}

exit 0
