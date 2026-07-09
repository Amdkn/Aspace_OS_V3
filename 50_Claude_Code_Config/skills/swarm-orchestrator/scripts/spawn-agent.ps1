# Swarm Orchestrator - Sub-Agent Spawning for Claude Code
# Uses native Agent tool to launch background sub-agents

param(
    [Parameter(Mandatory=$true)]
    [string]$AgentType,

    [Parameter(Mandatory=$true)]
    [string]$TaskDescription,

    [string]$AgentName = ""
)

$ErrorActionPreference = "Stop"

# Detect platform
$platformDetect = & "$PSScriptRoot\detect-platform.ps1" | ConvertFrom-Json
$platform = $platformDetect.platform

if ($platform -ne "claude_code") {
    Write-Error "spawn-agent.ps1 is designed for Claude Code CLI. Detected: $platform"
    exit 1
}

# Map agent type to canonical agent name
$agentMap = @{
    "code-reviewer" = "code-reviewer"
    "tdd-guide" = "tdd-guide"
    "build-error-resolver" = "build-error-resolver"
    "security-reviewer" = "security-reviewer"
    "refactor-cleaner" = "refactor-cleaner"
    "doc-updater" = "doc-updater"
    "e2e-runner" = "e2e-runner"
    "general-purpose" = "general-purpose"
    "planner" = "planner"
    "architect" = "architect"
}

$canonicalAgent = $agentMap[$AgentType]
if (-not $canonicalAgent) {
    $canonicalAgent = "general-purpose"
}

$runId = [System.Guid]::NewGuid().ToString("N").Substring(0, 8)
$displayName = if ($AgentName) { $AgentName } else { "$AgentType-$runId" }

$result = @{
    run_id = $runId
    agent_type = $AgentType
    canonical_agent = $canonicalAgent
    task = $TaskDescription
    display_name = $displayName
    platform = $platform
    timestamp = Get-Date -IsoFormat
    status = "spawned"
}

$result | ConvertTo-Json -Compress

# The actual Agent spawning is done via the Claude Code Agent tool
# This script generates the task metadata for tracking