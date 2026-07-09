<#
.SYNOPSIS
    A'Space OS V2 — Setup junctions sentinelles, env vars, subst drives.

.DESCRIPTION
    Idempotent. Crée les 9 junctions racine `_\` + 5 sub-junctions Business OS Links,
    exporte les variables d'environnement portables, propose subst drives B:/P:.

    Implémente ADR-FS-001 (junctions doctrine) + ADR-FS-002 (ce script).

.PARAMETER Apply
    Sans ce flag = dry-run (montre ce qui serait fait).
    Avec = exécute réellement.

.PARAMETER Audit
    Liste toutes les junctions du tree ASpace_OS_V2 + flag les broken.

.PARAMETER InstallProfile
    Append les lignes `$env:ASPACE_*` au profil PowerShell utilisateur.

.EXAMPLE
    .\Setup-ASpace-Junctions.ps1                  # dry-run
    .\Setup-ASpace-Junctions.ps1 -Apply           # exécute
    .\Setup-ASpace-Junctions.ps1 -Audit           # audit seul
    .\Setup-ASpace-Junctions.ps1 -InstallProfile  # patch profile.ps1

.NOTES
    Auteur : A2 Claude Code sous mandat A0 Amadeus
    Canon  : 10_Tech_OS\12_Blueprints\02-ADR\ADR-FS-002_setup-junctions-script.md
    Date   : 2026-05-22
#>

[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$Audit,
    [switch]$InstallProfile
)

$ErrorActionPreference = 'Stop'
$Root = 'C:\Users\amado\ASpace_OS_V2'

if (-not (Test-Path $Root)) {
    Write-Host "FATAL: ASPACE_ROOT not found: $Root" -ForegroundColor Red
    exit 1
}

# ============================================================
# Sentinelles racine `_\`
# ============================================================
$Sentinels = [ordered]@{
    'biz'  = '30_Business_OS'
    'para' = '20_Life_OS\24_PARA_Enterprise'
    'proj' = '20_Life_OS\24_PARA_Enterprise\01_Projects_Picard'
    'area' = '20_Life_OS\24_PARA_Enterprise\02_Areas_Spock'
    'res'  = '20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi'
    'arch' = '20_Life_OS\24_PARA_Enterprise\04_Archives_Data'
    'snw'  = '20_Life_OS\23_12WY_SNW'
    'gtd'  = '20_Life_OS\25_GTD_Cerritos'
    'deal' = '20_Life_OS\26_DEAL_Protostar'
}

# ============================================================
# Sub-junctions Business OS Links (resources, archives, life OS transverses)
# ============================================================
$BizLinksBase = Join-Path $Root '30_Business_OS\00_Jerry_Business_Pulse\04_Business_Domains\00_Links'
$BizLinks = [ordered]@{
    'res'  = '20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi'
    'arch' = '20_Life_OS\24_PARA_Enterprise\04_Archives_Data'
    'snw'  = '20_Life_OS\23_12WY_SNW'
    'gtd'  = '20_Life_OS\25_GTD_Cerritos'
    'deal' = '20_Life_OS\26_DEAL_Protostar'
}

function Set-Junction {
    param(
        [string]$Source,
        [string]$Target,
        [switch]$DryRun
    )
    if (-not (Test-Path $Target)) {
        Write-Host "  MISS target: $Target" -ForegroundColor Yellow
        return 'MISS'
    }
    if (Test-Path $Source) {
        $item = Get-Item $Source -Force
        if ($item.LinkType -eq 'Junction' -and $item.Target[0] -eq $Target) {
            Write-Host "  SKIP (already correct): $Source" -ForegroundColor DarkGray
            return 'SKIP'
        }
        if ($DryRun) {
            Write-Host "  WOULD REPLACE: $Source -> $Target" -ForegroundColor Cyan
            return 'WOULD-REPLACE'
        }
        $item.Delete()
    }
    if ($DryRun) {
        Write-Host "  WOULD CREATE: $Source -> $Target" -ForegroundColor Cyan
        return 'WOULD-CREATE'
    }
    New-Item -ItemType Junction -Path $Source -Target $Target | Out-Null
    Write-Host "  CREATED: $Source -> $Target" -ForegroundColor Green
    return 'CREATED'
}

function Audit-Junctions {
    Write-Host ""
    Write-Host "=== AUDIT: Junctions ASpace_OS_V2 tree ===" -ForegroundColor Cyan
    $junctions = Get-ChildItem -Path $Root -Recurse -Directory -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.LinkType -in 'Junction','SymbolicLink' }
    $ok = 0; $broken = 0
    foreach ($j in $junctions) {
        $target = $j.Target -join ';'
        $exists = Test-Path $target
        $status = if ($exists) { 'OK'; $ok++ } else { 'BROKEN'; $broken++ }
        $relSrc = $j.FullName.Replace($Root + '\','')
        $relTgt = $target.Replace($Root + '\','')
        $color = if ($exists) { 'Gray' } else { 'Red' }
        Write-Host ("  [{0,-6}] {1} -> {2}" -f $status, $relSrc, $relTgt) -ForegroundColor $color
    }
    Write-Host ""
    Write-Host "  Total: $($junctions.Count) | OK: $ok | BROKEN: $broken" -ForegroundColor $(if ($broken -gt 0) { 'Red' } else { 'Green' })
}

function Install-Profile {
    $profilePath = $PROFILE.CurrentUserAllHosts
    if (-not (Test-Path $profilePath)) {
        New-Item -ItemType File -Path $profilePath -Force | Out-Null
    }
    $marker = '# === ASpace_OS_V2 env (ADR-FS-002) ==='
    $existing = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
    if ($existing -and $existing.Contains($marker)) {
        Write-Host "Profile already patched (marker found)" -ForegroundColor Yellow
        return
    }
    $snippet = @'

# === ASpace_OS_V2 env (ADR-FS-002) ===
$env:ASPACE_ROOT  = 'C:\Users\amado\ASpace_OS_V2'
$env:ASPACE_BIZ   = "$env:ASPACE_ROOT\30_Business_OS"
$env:ASPACE_PARA  = "$env:ASPACE_ROOT\20_Life_OS\24_PARA_Enterprise"
$env:ASPACE_SHORT = "$env:ASPACE_ROOT\_"
# Optional subst drives (uncomment to enable per-session)
# subst B: $env:ASPACE_BIZ 2>$null
# subst P: $env:ASPACE_PARA 2>$null
# === END ASpace ===
'@
    Add-Content -Path $profilePath -Value $snippet
    Write-Host "Profile patched: $profilePath" -ForegroundColor Green
}

# ============================================================
# Main
# ============================================================
Write-Host "ASpace OS V2 - Junctions Setup" -ForegroundColor Magenta
Write-Host "Root: $Root"
$mode = if ($Apply) { 'APPLY' } else { 'DRY-RUN' }
$modeColor = if ($Apply) { 'Green' } else { 'Yellow' }
Write-Host "Mode: $mode" -ForegroundColor $modeColor
Write-Host ""

if ($Audit) {
    Audit-Junctions
    exit 0
}

if ($InstallProfile) {
    Install-Profile
    exit 0
}

# --- Sentinelles racine `_\` ---
Write-Host "[1/2] Sentinelles racine '_\'" -ForegroundColor Magenta
$short = Join-Path $Root '_'
if (-not (Test-Path $short)) {
    if ($Apply) {
        New-Item -ItemType Directory -Path $short | Out-Null
        Write-Host "  CREATED dir: $short" -ForegroundColor Green
    } else {
        Write-Host "  WOULD CREATE dir: $short" -ForegroundColor Cyan
    }
}
foreach ($k in $Sentinels.Keys) {
    $src = Join-Path $short $k
    $tgt = Join-Path $Root $Sentinels[$k]
    Set-Junction -Source $src -Target $tgt -DryRun:(-not $Apply) | Out-Null
}

# --- Sub-junctions Business OS Links ---
Write-Host ""
Write-Host "[2/2] Business OS Links" -ForegroundColor Magenta
if (-not (Test-Path $BizLinksBase)) {
    Write-Host "  MISS BizLinksBase: $BizLinksBase" -ForegroundColor Yellow
} else {
    foreach ($k in $BizLinks.Keys) {
        $src = Join-Path $BizLinksBase $k
        $tgt = Join-Path $Root $BizLinks[$k]
        Set-Junction -Source $src -Target $tgt -DryRun:(-not $Apply) | Out-Null
    }
}

Write-Host ""
Write-Host "Done. Run with -Audit to verify, -InstallProfile to patch PowerShell profile." -ForegroundColor Magenta
