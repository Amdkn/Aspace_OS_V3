param(
  [ValidateSet("install","status","url","stop","start","restart","update","uninstall")]
  [string]$Command="status",
  [string]$Root=(Join-Path $HOME ".aspace\dc"),
  [string]$RepoRoot="",
  [string]$AllowedRoot=$HOME,
  [switch]$NoAutostart,
  [switch]$PurgeData
)

$ErrorActionPreference="Stop"
$Root=[IO.Path]::GetFullPath($Root)
$Manifest=Join-Path $Root "run\runtime.json"
$Config=Join-Path $Root "config.json"
$InstalledSupervisor=Join-Path $Root "supervisor.py"
$InstalledControl=Join-Path $Root "dc.ps1"
$Launcher=Join-Path $Root "launch.cmd"
$RunKey="HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$RunName="ASpace Sovereign DC"

function Get-RepoRoot {
  if($RepoRoot){ return [IO.Path]::GetFullPath($RepoRoot) }
  if(Test-Path $Config){
    try {
      $cfg=Get-Content $Config -Raw | ConvertFrom-Json
      if($cfg.repo_root){ return [IO.Path]::GetFullPath([string]$cfg.repo_root) }
    } catch {}
  }
  $candidate=(Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..") -ErrorAction SilentlyContinue)
  if($candidate -and (Test-Path (Join-Path $candidate.Path "10_Tech_OS\machine_fabric\gateway\gateway.py"))){ return $candidate.Path }
  throw "repo_root unavailable; pass -RepoRoot or run from the repository"
}
function Read-Manifest {
  if(-not (Test-Path $Manifest)){ return $null }
  try { return Get-Content $Manifest -Raw | ConvertFrom-Json } catch { return $null }
}
function Test-Pid([int]$PidValue){ return [bool](Get-Process -Id $PidValue -ErrorAction SilentlyContinue) }
function Write-Config([string]$repo,[bool]$autostart){
  New-Item -ItemType Directory -Force $Root | Out-Null
  [ordered]@{
    schema="aspace.dc.install.v1"
    repo_root=$repo
    allowed_root=[IO.Path]::GetFullPath($AllowedRoot)
    root=$Root
    autostart=$autostart
    installed_at=[DateTimeOffset]::UtcNow.ToString("o")
  } | ConvertTo-Json -Depth 6 | Set-Content $Config -Encoding UTF8
}
function Install-DC {
  $repo=Get-RepoRoot
  $srcSupervisor=Join-Path $repo "10_Tech_OS\machine_fabric\runtime\supervisor.py"
  $srcControl=Join-Path $repo "10_Tech_OS\machine_fabric\runtime\dc.ps1"
  if(-not (Test-Path $srcSupervisor)){ throw "Missing supervisor: $srcSupervisor" }
  New-Item -ItemType Directory -Force $Root,(Join-Path $Root "data"),(Join-Path $Root "logs"),(Join-Path $Root "run") | Out-Null
  Copy-Item $srcSupervisor $InstalledSupervisor -Force
  Copy-Item $srcControl $InstalledControl -Force
  $autostart=-not $NoAutostart
  Write-Config $repo $autostart
  $pwsh=(Get-Command powershell.exe).Source
  if(-not $pwsh){ $pwsh="powershell.exe" }
  $cmd='@echo off'+[Environment]::NewLine+('"{0}" -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "{1}" start -Root "{2}" >nul 2>&1' -f $pwsh,$InstalledControl,$Root)+[Environment]::NewLine
  [IO.File]::WriteAllText($Launcher,$cmd,(New-Object Text.UTF8Encoding($false)))
  if($autostart){
    if($IsWindows){
      if(Test-Path (Join-Path $HOME "DC.bat")){ Remove-Item (Join-Path $HOME "DC.bat") -Force -ErrorAction SilentlyContinue }
      New-Item -Path $RunKey -Force | Out-Null
      Set-ItemProperty -Path $RunKey -Name $RunName -Value ('"{0}"' -f $Launcher)
    }
  }
  [pscustomobject]@{ok=$true;state="INSTALLED";root=$Root;repo_root=$repo;autostart=$autostart}
}
function Start-DC {
  $m=Read-Manifest
  if($m -and (Test-Pid ([int]$m.supervisor_pid))){
    return [pscustomobject]@{ok=$true;state="ALREADY_RUNNING";gateway_url=$m.gateway_url;supervisor_pid=$m.supervisor_pid;generation=$m.generation}
  }
  if(Test-Path $Manifest){ Remove-Item $Manifest -Force -ErrorAction SilentlyContinue }
  $repo=Get-RepoRoot
  $supervisor=$(if(Test-Path $InstalledSupervisor){$InstalledSupervisor}else{Join-Path $repo "10_Tech_OS\machine_fabric\runtime\supervisor.py"})
  if(-not (Test-Path $supervisor)){ throw "Missing supervisor: $supervisor" }
  $python=(Get-Command python).Source
  $pythonw=Join-Path (Split-Path $python) "pythonw.exe"
  if(-not (Test-Path $pythonw)){ $pythonw=$python }
  $old=@{}
  foreach($k in @("HTTP_PROXY","HTTPS_PROXY","ALL_PROXY","http_proxy","https_proxy","all_proxy","LLMTRIM_PROXY","NO_PROXY","no_proxy")){
    $old[$k]=[Environment]::GetEnvironmentVariable($k,"Process")
    [Environment]::SetEnvironmentVariable($k,$null,"Process")
  }
  $env:NO_PROXY="127.0.0.1,localhost"
  $env:no_proxy="127.0.0.1,localhost"
  $env:ASPACE_DC_ROOT=$Root
  $env:ASPACE_DC_REPO_ROOT=$repo
  $env:ASPACE_DC_ALLOWED_ROOT=[IO.Path]::GetFullPath($AllowedRoot)
  try {
    $supOut=Join-Path $Root "logs\supervisor.out.log"
    $supErr=Join-Path $Root "logs\supervisor.err.log"
    Start-Process -FilePath $pythonw -ArgumentList ('"{0}"' -f $supervisor) -WindowStyle Hidden -RedirectStandardOutput $supOut -RedirectStandardError $supErr | Out-Null
  } finally {
    foreach($k in $old.Keys){ [Environment]::SetEnvironmentVariable($k,$old[$k],"Process") }
    Remove-Item Env:\ASPACE_DC_ROOT,Env:\ASPACE_DC_REPO_ROOT,Env:\ASPACE_DC_ALLOWED_ROOT -ErrorAction SilentlyContinue
  }
  $deadline=(Get-Date).AddSeconds(20)
  do {
    Start-Sleep -Milliseconds 250
    $new=Read-Manifest
    if($new -and (Test-Pid ([int]$new.supervisor_pid))){
      return [pscustomobject]@{ok=$true;state="STARTED";gateway_url=$new.gateway_url;supervisor_pid=$new.supervisor_pid;generation=$new.generation}
    }
  } while((Get-Date) -lt $deadline)
  throw "DC runtime did not become ready"
}
function Stop-DC {
  $m=Read-Manifest
  if(-not $m){ return [pscustomobject]@{ok=$true;state="ALREADY_STOPPED"} }
  $pidValue=[int]$m.supervisor_pid
  if(Test-Pid $pidValue){
    & taskkill /PID $pidValue /T /F | Out-Null
    $deadline=(Get-Date).AddSeconds(8)
    do { Start-Sleep -Milliseconds 200 } while((Test-Pid $pidValue) -and (Get-Date) -lt $deadline)
  }
  Remove-Item $Manifest -Force -ErrorAction SilentlyContinue
  [pscustomobject]@{ok=$true;state="STOPPED";previous_supervisor_pid=$pidValue}
}
function Show-Status {
  $m=Read-Manifest
  if(-not $m){ return [pscustomobject]@{schema="aspace.dc.control.v1";state="STOPPED";reason="NO_MANIFEST"} }
  if(-not (Test-Pid ([int]$m.supervisor_pid))){ return [pscustomobject]@{schema="aspace.dc.control.v1";state="STOPPED";reason="SUPERVISOR_DEAD"} }
  $services=[ordered]@{}
  foreach($p in $m.pids.PSObject.Properties){ $services[$p.Name]=[ordered]@{pid=[int]$p.Value;alive=(Test-Pid ([int]$p.Value))} }
  $health=[ordered]@{}
  $healthOk=$true
  foreach($h in $m.health_urls.PSObject.Properties){
    try {
      $health[$h.Name]=Invoke-RestMethod $h.Value -TimeoutSec 2
      if($health[$h.Name].aggregate -eq "UNAVAILABLE"){ $healthOk=$false }
    } catch {
      $health[$h.Name]=@{aggregate="UNAVAILABLE";reason=$_.Exception.Message}
      $healthOk=$false
    }
  }
  $core=($healthOk) -and $services.m0.alive -and $services.process.alive -and $services.session.alive -and $services.gateway.alive
  [pscustomobject]@{schema="aspace.dc.control.v1";state=$(if($core){"ONLINE"}else{"DEGRADED"});gateway_url=$m.gateway_url;generation=$m.generation;supervisor_pid=$m.supervisor_pid;services=$services;health=$health;started_at=$m.started_at}
}
function Uninstall-DC {
  Stop-DC | Out-Null
  if($IsWindows){
    if(Test-Path $RunKey){ Remove-ItemProperty -Path $RunKey -Name $RunName -ErrorAction SilentlyContinue }
  }
  foreach($p in @($InstalledSupervisor,$InstalledControl,$Launcher,$Config)){ Remove-Item $p -Force -ErrorAction SilentlyContinue }
  if($PurgeData){ foreach($p in @((Join-Path $Root "data"),(Join-Path $Root "logs"),(Join-Path $Root "run"))){ Remove-Item $p -Recurse -Force -ErrorAction SilentlyContinue } }
  [pscustomobject]@{ok=$true;state="UNINSTALLED";purged_data=[bool]$PurgeData}
}

switch($Command){
  "install" { Install-DC | ConvertTo-Json -Depth 10 }
  "status" { Show-Status | ConvertTo-Json -Depth 12 }
  "url" { $m=Read-Manifest; if($m){$m.gateway_url}else{""} }
  "stop" { Stop-DC | ConvertTo-Json -Depth 8 }
  "start" { Start-DC | ConvertTo-Json -Depth 8 }
  "restart" { Stop-DC | Out-Null; Start-Sleep -Milliseconds 500; Start-DC | ConvertTo-Json -Depth 8 }
  "update" {
    $was=(Show-Status).state -ne "STOPPED"
    Install-DC | Out-Null
    if($was){ Stop-DC | Out-Null; Start-Sleep -Milliseconds 500; [pscustomobject]@{ok=$true;state="UPDATED";runtime=(Start-DC)} | ConvertTo-Json -Depth 10 }
    else { [pscustomobject]@{ok=$true;state="UPDATED"} | ConvertTo-Json -Depth 8 }
  }
  "uninstall" { Uninstall-DC | ConvertTo-Json -Depth 8 }
}
