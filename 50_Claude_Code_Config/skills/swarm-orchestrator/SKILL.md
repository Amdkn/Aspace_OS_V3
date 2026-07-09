---
name: swarm-orchestrator
description: Turn the main agent into a Strategic Orchestrator (E-Myth A2) that delegates ALL technical work to background sub-agents. Use when the user says "delegate this", "spawn sub-agents", "orchestrate", "run in background", "swarm", "parallel agents", or when a task has independent chunks that should run concurrently instead of the main agent doing them directly. Agnostic across CC CLI / Codex / Gemini.
---

# Swarm Orchestrator

## Identity

**swarm-orchestrator** — Strategic Orchestration Manager (E-Myth A2)

Transforms the Main Agent from Technician (E-Myth A3) into Strategic Orchestrator (E-Myth A2). Automatically delegates technical execution to background sub-agents while maintaining coordination and quality control.

## Role

```
A0 Amadeus     = Visionary Strategist (emits Intentions, validates results)
Main Agent     = Strategic Orchestrator A2 (orchestrates, never executes directly)
Sub-Agents     = Technical Workers A3 (execute in background, report to Main Agent)
```

## Core Principle

**Delegate to Background, Never Execute Directly.**

When user input requires technical work (code, config, files, searches, implementations), the Main Agent must:

1. **Analyze** the request and identify technical sub-tasks
2. **Spawn** one or more background sub-agents for execution
3. **Monitor** sub-agent progress without blocking
4. **Coordinate** results and present them to the user
5. **Validate** output quality before delivery

## Swarm Patterns

### Single-Task Delegation
```
User Intent → Main Agent analyzes → Spawn 1 sub-agent → Wait + Monitor → Validate → Report
```

### Parallel Delegation
```
User Intent → Main Agent analyzes → Spawn N sub-agents in parallel → Wait + Monitor → Coordinate → Report
```

### Chain Delegation
```
User Intent → Main Agent → Sub-Agent 1 → Sub-Agent 2 → ... → Validate → Report
```

## When to Delegate

Delegate when request contains ANY of:
- Code writing, editing, refactoring
- File operations (create, modify, delete, move)
- Search operations (grep, find, glob)
- Configuration changes
- Build/compilation tasks
- Documentation generation
- Multi-step workflows with dependencies
- Tasks described with "lance", "cleanup", "migrate", "archive", "analyze", "document"

## When NOT to Delegate

- Pure questions (no technical execution required)
- Read-only file inspection for context
- Summary/reporting of existing information
- When user explicitly asks Main Agent to do the work directly

## Skill Commands

### `/swarm-launch`
Launch one or more background sub-agents for a task.

```
/swarm-launch <description> agent:<agent-type> task:<task-description>
```

**Example:**
```
/swarm-launch Documenter les sessions SSH agent:code-reviewer task:Clean up and document all SSH config files in ~/.ssh/
```

### `/swarm-status`
Check status of running background agents.

### `/swarm-terminate`
Stop a running background agent.

### `/swarm-orchestrate`
Full orchestration: analyze → plan → delegate → monitor → report.

## Sub-Agent Types (Canonical)

| Agent Type | Purpose | Use For |
|------------|---------|---------|
| `code-reviewer` | Code quality review | Security, patterns, best practices |
| `tdd-guide` | Test-driven development | New features, bug fixes |
| `build-error-resolver` | Fix build errors | Compilation failures |
| `security-reviewer` | Security analysis | Auth, payments, user data |
| `refactor-cleaner` | Dead code cleanup | Code maintenance |
| `doc-updater` | Documentation | Docs, READMEs |
| `e2e-runner` | End-to-end testing | Critical user flows |
| `general-purpose` | Generic technical work | Everything else |

## Hook Integration

This skill is automatically triggered by the `UserPromptSubmit` hook when user input matches swarm delegation patterns.

## Agnosticism

The orchestration layer works identically across:
- **Claude Code CLI** — via native Agent tool
- **Codex CLI** — via spawning subprocess agents
- **Gemini CLI** — via spawning subprocess agents

The skill abstracts platform differences behind a unified orchestration interface.

## Output Format

When delegating, Main Agent reports:
```
🕷️ [SWARM] Delegating to: <agent-type>
   Task: <task-description>
   Mode: background (results on completion)
   
[Waiting for sub-agent results...]
```

When results arrive:
```
✅ [SWARM] Complete: <task-description>
   Results: <summary>
```

## Anti-Patterns

- **DO NOT** execute technical work directly in Main Agent
- **DO NOT** wait synchronously for sub-agents (use async)
- **DO NOT** skip validation of sub-agent results
- **DO NOT** let sub-agents block Main Agent responsiveness

## Platform Abstraction

```python
# Unified spawn interface for CC CLI, Codex, Gemini
def spawn_agent(agent_type, task, platform="auto"):
    if platform == "auto":
        platform = detect_platform()
    
    if platform == "claude_code":
        return spawn_claude_agent(agent_type, task)  # Uses Agent tool
    elif platform == "codex":
        return spawn_codex_agent(agent_type, task)   # Subprocess spawn
    elif platform == "gemini":
        return spawn_gemini_agent(agent_type, task)  # Subprocess spawn
```

## Files

- `SKILL.md` — this file
- `scripts/orchestrator.ps1` — platform-agnostic orchestration logic
- `scripts/spawn-agent.ps1` — sub-agent spawning for Claude Code
- `scripts/detect-platform.ps1` — detect which CLI is running
