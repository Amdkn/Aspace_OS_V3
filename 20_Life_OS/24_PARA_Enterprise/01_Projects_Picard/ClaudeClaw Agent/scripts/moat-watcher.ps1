# A'Space OS — The Watcher (Windows Native — Polling Mode)
# Monitors Drawbridge signals and triggers Gemini CLI automation

$projectPath = (Get-Item $PSScriptRoot).Parent.FullName
$moatPath = Join-Path $projectPath ".moat"
$targetFile = "moat-tasks-detail.json"
$targetPath = Join-Path $moatPath $targetFile
$geminiPath = "C:\Users\amado\AppData\Roaming\npm\gemini.ps1"

Write-Host "[A'Space Watcher Active — POLLING MODE]" -ForegroundColor Yellow
Write-Host "Monitoring: $targetPath" -ForegroundColor Cyan
Write-Host "Checking for tasks every 1 second..."

while ($true) {
    if (Test-Path $targetPath) {
        try {
            $json = Get-Content $targetPath -Raw | ConvertFrom-Json
            $pendingTasks = $json | Where-Object { $_.status -eq "to do" }
            
            if ($pendingTasks) {
                Write-Host ""
                Write-Host "[$(Get-Date -Format 'HH:mm:ss')] ⚡ Trigger: $($pendingTasks.Count) Task(s) Found." -ForegroundColor Yellow
                Write-Host "🤖 DELEGATING TO GEMINI CLI..." -ForegroundColor Green
                
                # Execute the CLI with Start-Process to avoid parsing issues
                $processParams = @{
                    FilePath = "powershell.exe"
                    ArgumentList = "-ExecutionPolicy Bypass", "-File", $geminiPath, "-p", "'/bridge yolo'", "--approval-mode", "yolo"
                    Wait = $true
                    NoNewWindow = $true
                }
                Start-Process @processParams
                
                # Sleep a bit to allow the CLI to finish and update the JSON
                Start-Sleep -Seconds 10
            }
        } catch {
            Write-Host "Error processing tasks: $_" -ForegroundColor Red
        }
    }
    Start-Sleep -Seconds 1
}
