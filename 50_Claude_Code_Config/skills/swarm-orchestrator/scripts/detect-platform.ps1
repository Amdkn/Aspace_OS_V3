# Swarm Orchestrator - Platform Detection Script
# Detects which CLI is running (Claude Code, Codex, or Gemini)

$ErrorActionPreference = "Stop"

function Get-CurrentPlatform {
    $env:CLAUDE_CODE = $env:CLAUDE_CODE  # Claude Code sets this
    $env:CODEX_CLI = $env:CODEX_CLI      # Codex CLI sets this
    $env:GEMINI_CLI = $env:GEMINI_CLI    # Gemini CLI sets this

    if ($env:CLAUDE_CODE) {
        return "claude_code"
    } elseif ($env:CODEX_CLI) {
        return "codex"
    } elseif ($env:GEMINI_CLI) {
        return "gemini"
    } else {
        # Fallback: detect by process name or parent
        $processName = (Get-Process -Id $PID).ProcessName
        if ($processName -match "claude|codex|gemini") {
            return $processName.ToLower()
        }
        return "unknown"
    }
}

$platform = Get-CurrentPlatform

$result = @{
    platform = $platform
    timestamp = Get-Date -IsoFormat
    pid = $PID
    hostname = $env:COMPUTERNAME
}

$result | ConvertTo-Json -Compress