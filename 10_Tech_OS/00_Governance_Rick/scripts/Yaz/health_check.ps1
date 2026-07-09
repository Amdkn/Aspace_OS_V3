# A0 Health Check & Self-Healing (Rick Supreme Pattern)

$Services = @(
    @{ Name = "Coolify Bridge"; Port = 8080 },
    @{ Name = "GitHub Bridge"; Port = 8081 },
    @{ Name = "n8n Engine"; Port = 5678 }
)

Write-Host "--- Aspace00 System Audit ---" -ForegroundColor Yellow

foreach ($Svc in $Services) {
    $Check = Test-NetConnection -ComputerName localhost -Port $Svc.Port -WarningAction SilentlyContinue
    if ($Check.TcpTestSucceeded) {
        Write-Host "[OK] $($Svc.Name) is active on port $($Svc.Port)" -ForegroundColor Green
    } else {
        Write-Host "[FAIL] $($Svc.Name) is down on port $($Svc.Port)" -ForegroundColor Red
        if ($Svc.Name -like "*Bridge*") {
            Write-Host "Triggering Self-Healing for Bridges..." -ForegroundColor Cyan
            powershell -ExecutionPolicy Bypass -File "C:\Aspace00\A0_Supreme\scripts\mcp_bridges\start_bridges.ps1"
        }
    }
}
