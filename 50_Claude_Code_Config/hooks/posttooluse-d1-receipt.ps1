# posttooluse-d1-receipt.ps1
# Hook 2 — PostToolUse D1 Receipt (Sobriété Rick scope corrigé)
# ADR-META-005 RATIFIED 2026-06-21 | Rick C137 GO conditionnel + rotation 7j
# Responsabilité unique : appender dans ~/.claude/logs/tool-receipts.logl après chaque tool call.

$ErrorActionPreference = 'SilentlyContinue'
$logDir = "$env:USERPROFILE\.claude\logs"
$logFile = Join-Path $logDir "tool-receipts.logl"
$errFile = Join-Path $logDir "tool-receipts-error.logl"
$wikiLog = "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md"
$maxBytes = 10MB
$retentionDays = 7

try {
    if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

    # Sobriété patch Rick #1 — rotation 7j self-contained (logique self-cleaning, pas de cron externe)
    if (Test-Path $logFile) {
        $fileSize = (Get-Item $logFile).Length
        if ($fileSize -gt $maxBytes) {
            # Anti-fragilité : si >10MB → tronque les 50% plus vieux (garde récents)
            $lines = Get-Content $logFile -Encoding UTF8
            $halfIdx = [Math]::Floor($lines.Count / 2)
            $lines[$halfIdx..($lines.Count - 1)] | Set-Content $logFile -Encoding UTF8
        } else {
            # Rotation 7j : tronque entries > 7 jours
            $cutoff = (Get-Date).AddDays(-$retentionDays)
            $kept = Get-Content $logFile -Encoding UTF8 | Where-Object {
                $line = $_
                if ($line -match '^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})') {
                    try {
                        $ts = [datetime]::Parse($Matches[1])
                        $ts -ge $cutoff
                    } catch { $true }
                } else { $true }
            }
            $kept | Set-Content $logFile -Encoding UTF8
        }
    }

    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $tool = if ($env:CLAUDE_TOOL_NAME) { $env:CLAUDE_TOOL_NAME } else { "UNKNOWN" }
    $result = if ($env:CLAUDE_TOOL_RESULT) { $env:CLAUDE_TOOL_RESULT } else { "" }
    $first80 = ($result -replace "`r?`n", " ").Substring(0, [Math]::Min(80, $result.Length))
    $exitCode = if ($env:CLAUDE_TOOL_EXIT_CODE) { $env:CLAUDE_TOOL_EXIT_CODE } else { "0" }
    $targetPath = if ($env:CLAUDE_TOOL_TARGET_PATH) { $env:CLAUDE_TOOL_TARGET_PATH } else { "" }

    $line = "$ts | $tool | $first80 | exit=$exitCode | path=$targetPath"
    Add-Content -Path $logFile -Value $line -Encoding UTF8

    # Phase bonus : si Write/Edit/MultiEdit sous ASpace_OS_V2 → append extra ligne dans wiki\log.md (D4 canon log)
    $writeTools = @('Write', 'Edit', 'MultiEdit')
    if ($writeTools -contains $tool -and $targetPath -like '*ASpace_OS_V2*') {
        if (Test-Path $wikiLog) {
            $wikiLine = "**$([DateTime]::Parse($ts.Split(' ')[0]).ToString('yyyy-MM-dd'))** : [HOOK2-D1-RECEIPT] $tool → $targetPath"
            Add-Content -Path $wikiLog -Value $wikiLine -Encoding UTF8
        }
    }

    exit 0
} catch {
    $errLine = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | HOOK2_ERROR | $($_.Exception.Message)"
    Add-Content -Path $errFile -Value $errLine -Encoding UTF8
    exit 0
}