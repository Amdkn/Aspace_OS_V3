# restart_wf1.ps1 - purge tous les runners/workers WF1 puis lance UN runner (singleton)
$ErrorActionPreference = 'Continue'
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'wf1_runner\.ps1' -and $_.Name -match 'powershell' } | ForEach-Object {
  Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
  Write-Host ("killed runner " + $_.ProcessId)
}
# FILTRE STRICT (fix 2026-07-06 : l'ancien pattern large a tue la session Desktop d'A+, crash 4294967295)
# Un worker WF1 = ' -p ' + '--bare' ensemble. JAMAIS de kill sur 'claude' ou 'dangerously' seuls.
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match '--bare' -and $_.CommandLine -match ' -p ' } | ForEach-Object {
  Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
  Write-Host ("killed worker " + $_.ProcessId)
}
Start-Sleep -Seconds 2
Start-Process powershell -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-WindowStyle','Hidden','-File','C:\Users\amado\agent-os\citadel\cron\wf1_runner.ps1'
Write-Host 'runner v3 lance (singleton + bare + gardes Hermes PS-1)'
