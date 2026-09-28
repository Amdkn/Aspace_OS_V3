param([ValidateSet('rick','doctor13-kernel','doctor11-life','doctor12-buzz')][string]$Agent='rick')
$Root=Split-Path -Parent $PSScriptRoot
Set-Location $Root
Write-Host "A'Space Antigravity Council | $Agent | $Root" -ForegroundColor Cyan
& agy --agent $Agent --effort high
