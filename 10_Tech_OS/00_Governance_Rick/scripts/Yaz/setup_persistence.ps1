# Setup Task Scheduler for Docker Persistence
# Author: Rick Supreme

$TaskName = "AaaS_Docker_Persistence"
$ScriptPath = "C:\Aspace00\scripts\docker_persistence.ps1"
$Action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ExecutionPolicy Bypass -File $ScriptPath"
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -RunLevel Highest -Force

Write-Host "SUCCESS: Task $TaskName registered for automatic persistence."
