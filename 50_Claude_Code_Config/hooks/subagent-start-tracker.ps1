# subagent-start-tracker.ps1
# Hook 3 — SubagentStart A3 Twin tracker (Sobriété Rick scope corrigé)
# ADR-META-005 RATIFIED 2026-06-21 | Rick C137 GO conditionnel + throttle 1/10 fan-out
# Responsabilité unique : appender dans ~/.claude/logs/a3-spawns.logl à chaque A3 spawn.

$ErrorActionPreference = 'SilentlyContinue'
$logDir = "$env:USERPROFILE\.claude\logs"
$logFile = Join-Path $logDir "a3-spawns.logl"
$maxBytes = 5MB

try {
    if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

    $agentType = if ($env:CLAUDE_SUBAGENT_TYPE) { $env:CLAUDE_SUBAGENT_TYPE } else { "UNKNOWN" }
    $agentId = if ($env:CLAUDE_AGENT_ID) { $env:CLAUDE_AGENT_ID } else { "noid" }
    $sessionId = if ($env:CLAUDE_SESSION_ID) { $env:CLAUDE_SESSION_ID } else { "nosession" }
    $fanoutDepth = 0
    if ($env:CLAUDE_FANOUT_DEPTH -and $env:CLAUDE_FANOUT_DEPTH -match '^\d+$') {
        $fanoutDepth = [int]$env:CLAUDE_FANOUT_DEPTH
    } elseif ($env:CLAUDE_PARENT_SPAWN_GROUP_ID) {
        # heuristic fallback : si parent group ID set, assume depth >= 1
        $fanoutDepth = 1
    }

    # Sobriété patch Rick #2 — throttle 1/10 fan-out (sample modulo 10 si fanout_depth > 0)
    $shouldLog = $true
    $throttleMod = 10
    if (Test-Path $logFile) {
        $fileSize = (Get-Item $logFile).Length
        if ($fileSize -gt $maxBytes) {
            # Anti-fragilité : si >5MB → throttle devient 1/100 (Sobriété auto-adaptive)
            $throttleMod = 100
        }
    }

    if ($fanoutDepth -gt 0) {
        $existingCount = 0
        if (Test-Path $logFile) {
            $existingCount = (Get-Content $logFile -Encoding UTF8 | Measure-Object).Count
        }
        if (($existingCount + 1) % $throttleMod -ne 0) {
            $shouldLog = $false
        }
    }

    if ($shouldLog) {
        $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        # Canon A3 detection : match A3-{enterprise|discovery|orville|snw|protostar|cerritos}-
        $canonTag = if ($agentType -match '^a3-(enterprise|discovery|orville|snw|protostar|cerritos)-') { "CANON" } else { "UNKNOWN" }
        $line = "$ts | A3_SPAWN | $agentType | $sessionId | $agentId | fanout=$fanoutDepth | $canonTag"
        Add-Content -Path $logFile -Value $line -Encoding UTF8
    }

    exit 0
} catch {
    exit 0
}