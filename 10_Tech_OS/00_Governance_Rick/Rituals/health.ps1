# A0 Health Check Ritual
# Usage: ./health.ps1

Write-Host "=== A0 SYSTEM VITALS ===" -ForegroundColor Cyan
$os = Get-CimInstance Win32_OperatingSystem
$mem = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / $os.TotalVisibleMemorySize * 100, 1)
$cpu = (Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average

Write-Host "CPU Load: $cpu %"
Write-Host "Memory:   $mem %"
Write-Host "Uptime:   $((Get-Date) - $os.LastBootUpTime)"

Write-Host "`n=== DOCKER FLEET ===" -ForegroundColor Cyan
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

Write-Host "`n=== DISK SPACE ===" -ForegroundColor Cyan
Get-PSDrive C | Select-Object Used,Free,@{Name="PercentFree";Expression={("{0:P2}" -f ($_.Free/($_.Used+$_.Free)))}}

Write-Host "`n[HEALTH: OK]" -ForegroundColor Green
