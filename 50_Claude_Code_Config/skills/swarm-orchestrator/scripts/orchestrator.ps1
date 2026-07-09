# Swarm Orchestrator - Main Coordination Script
# Coordinates background sub-agent execution for Claude Code
# Called by UserPromptSubmit hook to delegate technical work

param(
    [Parameter(Mandatory=$true)]
    [string]$UserPrompt,

    [string]$Action = "analyze"  # analyze | spawn | status | terminate
)

$ErrorActionPreference = "Stop"

# Detect platform
$platformDetect = & "$PSScriptRoot\detect-platform.ps1" | ConvertFrom-Json
$platform = $platformDetect.platform

# Patterns that trigger delegation
$delegatePatterns = @(
    "lance",
    "cleanup",
    "clean up",
    "migrate",
    "archive",
    "analyze",
    "document",
    "search",
    "find",
    "grep",
    "delete",
    "remove",
    "create",
    "write",
    "modify",
    "change",
    "update",
    "configur",
    "build",
    "compile",
    "test",
    "deploy",
    "install",
    "setup",
    "execute",
    "run",
    "check",
    "verify",
    "validate",
    "fix",
    "repair",
    "restore",
    "backup",
    "export",
    "import",
    "sync",
    "refresh",
    "generate",
    "process",
    "extract",
    "convert",
    "transform"
)

# Patterns that indicate NO delegation needed
$noDelegatePatterns = @(
    "^what is",
    "^how do i",
    "^can you explain",
    "^what does",
    "^what are",
    "^who is",
    "^what's",
    "^how does",
    "^why does",
    "^why is",
    "^when did",
    "^when is",
    "^where is",
    "^where does",
    "^which ",
    "^is there",
    "^are there",
    "^list the",
    "^show me",
    "^tell me about",
    "^describe"
)

function Test-ShouldDelegate {
    param([string]$prompt)

    # Check no-delegate patterns first
    foreach ($pattern in $noDelegatePatterns) {
        if ($prompt -match $pattern) {
            return $false
        }
    }

    # Check delegate patterns
    foreach ($pattern in $delegatePatterns) {
        if ($prompt -match $pattern) {
            return $true
        }
    }

    return $false
}

function Get-DelegationPlan {
    param([string]$prompt)

    # Simple keyword-based task classification
    $tasks = @()

    if ($prompt -match "cleanup|clean up|remove|delete|archive") {
        $tasks += @{
            type = "cleanup"
            agent = "refactor-cleaner"
            description = "Cleanup task detected in prompt"
        }
    }

    if ($prompt -match "document|doc|write README|write doc") {
        $tasks += @{
            type = "documentation"
            agent = "doc-updater"
            description = "Documentation task detected"
        }
    }

    if ($prompt -match "search|find|grep|glob|look for") {
        $tasks += @{
            type = "search"
            agent = "general-purpose"
            description = "Search task detected"
        }
    }

    if ($prompt -match "build|compile|install|setup|config") {
        $tasks += @{
            type = "build-config"
            agent = "general-purpose"
            description = "Build/config task detected"
        }
    }

    if ($prompt -match "fix|repair|debug|error|broken") {
        $tasks += @{
            type = "fix"
            agent = "build-error-resolver"
            description = "Fix task detected"
        }
    }

    if ($prompt -match "security|auth|password|token|secret|key|crypt") {
        $tasks += @{
            type = "security"
            agent = "security-reviewer"
            description = "Security task detected"
        }
    }

    if ($prompt -match "test|e2e|integration") {
        $tasks += @{
            type = "testing"
            agent = "e2e-runner"
            description = "Testing task detected"
        }
    }

    if ($tasks.Count -eq 0) {
        $tasks += @{
            type = "general"
            agent = "general-purpose"
            description = "General technical task"
        }
    }

    return $tasks
}

# Main logic
switch ($Action) {
    "analyze" {
        $shouldDelegate = Test-ShouldDelegate -prompt $UserPrompt
        $plan = if ($shouldDelegate) { Get-DelegationPlan -prompt $UserPrompt } else { @() }

        $result = @{
            action = "analyze"
            should_delegate = $shouldDelegate
            platform = $platform
            tasks = $plan
            timestamp = Get-Date -IsoFormat
        }

        $result | ConvertTo-Json -Compress
    }

    "spawn" {
        $shouldDelegate = Test-ShouldDelegate -prompt $UserPrompt
        if (-not $shouldDelegate) {
            Write-Output "NO_DELEGATION"
            exit 0
        }

        $plan = Get-DelegationPlan -prompt $UserPrompt
        $spawned = @()

        foreach ($task in $plan) {
            $spawnResult = & "$PSScriptRoot\spawn-agent.ps1" -AgentType $task.agent -TaskDescription "$($task.description): $UserPrompt"
            $spawned += $spawnResult | ConvertFrom-Json
        }

        $result = @{
            action = "spawn"
            delegated = $true
            platform = $platform
            spawned_agents = $spawned
            timestamp = Get-Date -IsoFormat
        }

        $result | ConvertTo-Json -Compress
    }

    "status" {
        # Return status of tracked agents
        $result = @{
            action = "status"
            platform = $platform
            timestamp = Get-Date -IsoFormat
        }
        $result | ConvertTo-Json -Compress
    }

    default {
        Write-Error "Unknown action: $Action"
        exit 1
    }
}