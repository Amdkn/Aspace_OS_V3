# sessionstart-premortem-pending-detector.ps1
# Anti-forgetting hook for /premortem-fill skill.
# At session start, scans wiki/hand_offs/*_premortem_pending_actions.md
# and surfaces ⚠️ warnings so A0 cannot forget pending actions.

$ErrorActionPreference = 'SilentlyContinue'

$homedir = $env:USERPROFILE
$handoffsDir = Join-Path $homedir 'ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs'

if (-not (Test-Path $handoffsDir)) {
    return
}

$pendingFiles = Get-ChildItem -Path $handoffsDir -Filter '*_premortem_pending_actions.md' -ErrorAction SilentlyContinue

if (-not $pendingFiles) {
    return
}

Write-Host ''
Write-Host '⚠️  [premortem-fill] pending A0 actions detected:' -ForegroundColor Yellow

foreach ($f in $pendingFiles) {
    $target = $f.BaseName -replace '_premortem_pending_actions$', ''
    $content = Get-Content $f.FullName -Raw
    # Count "### F" markers
    $count = ([regex]::Matches($content, '### F\d+')).Count
    Write-Host "    - $target : $count pending action(s)" -ForegroundColor Yellow
    Write-Host "      file: $($f.FullName)" -ForegroundColor Gray
}

Write-Host ''
Write-Host '  -> run `/premortem-fill [target]` to refresh, or `GO pour [F-id]` to act on a specific pending action.' -ForegroundColor Cyan
Write-Host ''
