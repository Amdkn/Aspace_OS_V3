param(
  [switch]$Apply,
  [switch]$BootstrapMissing
)

$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path $PSScriptRoot -Parent
$UserRoot = 'C:\Users\amado'
$WorldRoot = Join-Path $UserRoot 'ASpace_Worlds'
$Astra = Join-Path $UserRoot 'ASpace_OS_V3'
$Sol = Join-Path $UserRoot 'agent-os'
$Terra = Join-Path $WorldRoot 'Life_OS_2026'
$Luna = Join-Path $WorldRoot 'Luna'
$RepoPool = Join-Path $WorldRoot '_repos'

function Ensure-Directory([string]$Path) {
  if (-not $Apply) { Write-Output "WOULD_MKDIR $Path"; return }
  New-Item -ItemType Directory -Force -Path $Path | Out-Null
}

function Ensure-Junction([string]$Path, [string]$Target) {
  if (Test-Path $Path) {
    $item = Get-Item $Path -Force
    if ($item.LinkType -eq 'Junction' -and ($item.Target -contains $Target)) {
      return 'present'
    }
    return "occupied:$($item.LinkType)"
  }
  if (-not $Apply) {
    Write-Output "WOULD_JUNCTION $Path -> $Target"
    return 'would_link'
  }
  if (-not (Test-Path $Target)) { throw "Missing target: $Target" }
  New-Item -ItemType Directory -Force -Path (Split-Path $Path -Parent) | Out-Null
  New-Item -ItemType Junction -Path $Path -Target $Target | Out-Null
  return 'linked'
}

function Ensure-Clone([string]$Path, [string]$Repo) {
  if (Test-Path (Join-Path $Path '.git')) { return 'present' }
  if (-not $BootstrapMissing) { return 'registered_missing' }
  if (-not $Apply) {
    Write-Output "WOULD_CLONE $Repo -> $Path"
    return 'would_clone'
  }
  New-Item -ItemType Directory -Force -Path (Split-Path $Path -Parent) | Out-Null
  git clone --filter=blob:none $Repo $Path
  if ($LASTEXITCODE -ne 0) { throw "Clone failed: $Repo" }
  return 'cloned'
}

Ensure-Directory $WorldRoot
Ensure-Directory $Luna
Ensure-Directory $RepoPool

$worlds = [ordered]@{
  Astra = @{ path = (Join-Path $WorldRoot 'Astra'); target = $Astra }
  Sol   = @{ path = (Join-Path $WorldRoot 'Sol'); target = $Sol }
  Terra = @{ path = (Join-Path $WorldRoot 'Terra'); target = $Terra }
}
$result = [ordered]@{
  schema = 'aspace.world-federation-evidence.v1'
  generated_at = (Get-Date).ToUniversalTime().ToString('o')
  apply = [bool]$Apply
  worlds = [ordered]@{}
  astra_mounts = [ordered]@{}
  luna_repositories = [ordered]@{}
  compatibility = [ordered]@{}
}

foreach ($name in $worlds.Keys) {
  $spec = $worlds[$name]
  $result.worlds[$name] = @{
    state = Ensure-Junction $spec.path $spec.target
    path = $spec.path
    target = $spec.target
  }
}

$astraWorlds = Join-Path $Astra 'Worlds'
Ensure-Directory $astraWorlds
foreach ($name in @('Sol','Terra')) {
  $result.astra_mounts[$name] = @{
    state = Ensure-Junction (Join-Path $astraWorlds $name) $worlds[$name].target
    target = $worlds[$name].target
  }
}
$result.astra_mounts['Luna'] = @{
  state = Ensure-Junction (Join-Path $astraWorlds 'Luna') $Luna
  target = $Luna
}

$missing = [ordered]@{
  '01-OMK-Business-OS' = @{
    path = Join-Path $RepoPool '01-OMK-Business-OS'
    repo = 'https://github.com/Amdkn/01-OMK-Business-OS.git'
  }
  'The-OMK-Office1.0-JaaS' = @{
    path = Join-Path $RepoPool 'The-OMK-Office1.0-JaaS'
    repo = 'https://github.com/Amdkn/The-OMK-Office1.0-JaaS.git'
  }
}
foreach ($name in $missing.Keys) {
  $spec=$missing[$name]
  $cloneState=Ensure-Clone $spec.path $spec.repo
  $result.luna_repositories[$name] = @{ clone_state=$cloneState; source=$spec.path }
}
$lunaSources = [ordered]@{
  'BusinessOS' = 'C:\Users\amado\BusinessOS_analysis'
  'Business-Office-3-OS' = 'C:\Users\amado\Business-Office-3-OS'
  '01-OMK-Business-OS' = (Join-Path $RepoPool '01-OMK-Business-OS')
  'The-OMK-Office1.0-JaaS' = (Join-Path $RepoPool 'The-OMK-Office1.0-JaaS')
  'The-OMK-Mobile-Back-Office' = 'C:\Users\amado\The-OMK-Mobile-Back-Office'
  'The-OMK-Office-V1-JaaS-Landing-Site-Web' = 'C:\Users\amado\The-OMK-Office-V1-JaaS-Landing-Site-Web'
  'OMK-DESKTOP-WEB-OS' = 'C:\Users\amado\ASpace_OS_V3\30_Business_OS\10_Projects\coach-os-app'
  '00-omk-saas-os' = 'C:\Users\amado\00-omk-saas-os'
}

foreach ($name in $lunaSources.Keys) {
  $source=$lunaSources[$name]
  $state = if (Test-Path $source) { Ensure-Junction (Join-Path $Luna $name) $source } else { 'source_missing' }
  $remote = if (Test-Path $source) { (git -C $source remote get-url origin 2>$null) -join '' } else { '' }
  $head = if (Test-Path $source) { (git -C $source rev-parse --short HEAD 2>$null) -join '' } else { '' }
  $result.luna_repositories[$name] = @{
    state=$state
    source=$source
    remote=$remote
    head=$head
  }
}

$result.compatibility['Agent_OS'] = @{
  path = Join-Path $Astra 'Agent_OS'
  target = $Sol
  policy = 'legacy alias retained'
}
$result.compatibility['Life_OS_2026'] = @{
  path = Join-Path $Astra 'Life_OS_2026'
  target = $Terra
  policy = 'legacy alias retained'
}
$exclude = Join-Path $Astra '.git\info\exclude'
if ($Apply -and (Test-Path $exclude)) {
  $raw = Get-Content $exclude -Raw
  if ($raw -notmatch '(?m)^/Worlds/$') {
    Add-Content -Path $exclude -Value ([Environment]::NewLine + '/Worlds/')
  }
}

$desktop = Join-Path $Sol 'desktop'
$listener = Get-NetTCPConnection -LocalPort 5555 -State Listen -ErrorAction SilentlyContinue
$result['sol_desktop'] = @{
  path = $desktop
  remote = ((git -C $desktop remote get-url origin 2>$null) -join '')
  head = ((git -C $desktop rev-parse --short HEAD 2>$null) -join '')
  configured_port = 5555
  listener_active = [bool]$listener
}

$report = Join-Path $RepoRoot '10_Tech_OS\reports\world_federation_20260928.json'
if ($Apply) {
  $result | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 $report
  Write-Output "EVIDENCE $report"
}
$result | ConvertTo-Json -Depth 8
