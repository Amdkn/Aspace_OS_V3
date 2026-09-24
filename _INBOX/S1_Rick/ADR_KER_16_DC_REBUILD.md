# ADR: Bounded Escalation for KER-16 (Desktop Commander Audit)

**Status:** Proposed
**Context:** KER-16 - Desktop Commander remote access audit & rebuild
**Location:** `_INBOX/S1_Rick/ADR_KER_16_DC_REBUILD.md`

## 1. Context & Blocker

The mandate for [KER-16](https://linear.app/aspace-os/issue/KER-16/bedrock-audit-and-rebuild-desktop-commander-remote-access-idempotent) requires auditing and rebuilding the Desktop Commander remote access architecture on the physical Windows host `Amd-PC`.

The core requirements include:
- Establishing ground truth (npm versions, processes, PowerShell aliases, Scheduled Tasks, OAuth state).
- Proving idempotence via real foreground/background executions on the Windows machine.
- Proving end-to-end success via a "real remote call from ChatGPT".

**Blocker:**
I am executing within an isolated, headless Linux sandbox (`devbox 6.8.0 x86_64 GNU/Linux`). I have no live network, RDP, or remote shell access to `Amd-PC`. I cannot query `Get-CimInstance Win32_Process`, read `C:\Users\amado\AppData\Roaming\npm`, verify Scheduled Tasks, or simulate the interactive OAuth device flow.

The mandate explicitly forbids:
- "Fabricating remote ChatGPT end-to-end success".
- Proceeding when "requirements are materially ambiguous or need human interaction" without STOPPING and proposing an ADR for the Doctor/Rick review path.

## 2. Decision

To comply with the mandate's strict anti-fabrication rules, I am halting execution and escalating this ADR to the human operator (Amadeus / A0 / Rick).

We must execute this investigation via **Delegated Telemetry**. I will provide the required telemetry gathering scripts here. The operator must run them on `Amd-PC` and paste the raw outputs back to me so I can perform the "root-cause analysis" and formulate the "minimal architecture" offline, before we finalize any scripts.

## 3. Required Action (Delegated Telemetry)

Operator, please execute the following PowerShell commands on `Amd-PC` and return the output:

### A. Ground Truth: Binaries & Versions
```powershell
# npm package version
npm list -g desktop-commander

# real binary paths
Get-Command desktop-commander | Format-List *
Get-Command dc | Format-List *
```

### B. Ground Truth: Processes
```powershell
Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and ($_.CommandLine -like '*desktop-commander*' -or $_.CommandLine -like '*supervisor.mjs*') } | Select-Object ProcessId, CommandLine, ParentProcessId
```

### C. Ground Truth: Persistence / Tasks
```powershell
Get-ScheduledTask -TaskName "ASpace Desktop Commander", "ASpace DC Migration" -ErrorAction SilentlyContinue | Get-ScheduledTaskInfo
```

### D. Ground Truth: Aliases & Profile
```powershell
Get-Alias dc -ErrorAction SilentlyContinue
Get-Content $PROFILE -ErrorAction SilentlyContinue | Select-String "desktop-commander|dc"
```

### E. Ground Truth: State & Logs (Metadata only, do NOT paste raw tokens)
```powershell
Get-ChildItem -Path "$env:USERPROFILE\.desktop-commander" -Recurse | Select-Object FullName, LastWriteTime, Length
Get-Content "$env:USERPROFILE\.desktop-commander\remote.log" -Tail 20
```

## 4. Consequences
Once the raw output of these telemetry blocks is provided, I will be able to analyze the exact point of failure (e.g., node process spawning loops, stale wrapper layers, or OAuth races) and propose the exact canonical `DC.bat` or scheduled task XML needed to achieve the required idempotent architecture.