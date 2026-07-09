---
source: Codex / Rick A1
date: 2026-05-16
type: configuration-state
domain: L0_Tech_OS / Hermes_Agent
tags: [#Hermes #persistence #WindowsTaskScheduler #WSL2 #SSHFS-policy]
status: active
---

# Hermes Agent Persistence State — 2026-05-16

## Intent

Hermes Agent is pinned as a Windows app on the taskbar. The app must remain operational after a Windows reboot without requiring manual WSL service recovery.

## Current Runtime Shape

Hermes runs inside WSL distro `ASpace-L0` under Linux user `amadeus`.

Windows opens the dashboard as an app/pinned browser surface:

- Dashboard: `http://127.0.0.1:9119`
- Gateway health: `http://127.0.0.1:8642/health`
- Workspace UI: `http://127.0.0.1:3000`

WSL user services:

- `hermes-gateway.service`
- `hermes-dashboard.service`
- `hermes-workspace.service`

All three services are enabled with `systemctl --user enable` and verified active on 2026-05-16.

## Dashboard Mode

The dashboard service is configured with TUI/chat exposure enabled:

```bash
hermes dashboard --port 9119 --host 127.0.0.1 --no-open --tui
```

This matters because Kanban is not the discussion surface. Mental model:

- Sessions / Chat: discussion and continuity.
- Kanban: workflow and task state.
- Gateway: API/process heartbeat.

## Windows Persistence

Windows Task Scheduler task:

```text
Hermes Agent Persistent Startup
```

Trigger:

```text
At logon, 30 second delay
```

Action:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\scripts\Start-HermesAgent.ps1"
```

Last manual verification:

```text
LastRunTime: 2026-05-16 00:42:05 America/New_York
LastTaskResult: 0
```

## Bootstrap Scripts

Windows entrypoint:

```text
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\scripts\Start-HermesAgent.ps1
```

Hermes service payload:

```text
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\scripts\start-hermes-agent.sh
```

The PowerShell script reads the shell payload on Windows, normalizes line endings, base64-encodes it, then sends it to WSL through `bash -lc`.

This avoids using `/mnt/c` as a WSL file bridge.

## Isolation Rule

Do not use `/mnt/c` / DrvFS as the durable integration layer between Windows and WSL for Hermes Agent.

Approved boundary:

```text
Windows <-> SSHFS <-> WSL
```

Rationale:

- Preserves WSL isolation.
- Avoids accidental Windows filesystem coupling inside Linux services.
- Keeps Hermes service runtime anchored in `/home/amadeus`.
- Makes Windows access an explicit mounted view rather than an implicit shared root.

Current bootstrap exception:

- Windows Task Scheduler may invoke `wsl.exe`.
- PowerShell may transmit a command payload into WSL.
- WSL must not depend on `/mnt/c/...` paths to start Hermes.

## Verification Commands

Windows:

```powershell
Get-ScheduledTask -TaskName "Hermes Agent Persistent Startup"
Get-ScheduledTaskInfo -TaskName "Hermes Agent Persistent Startup"
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8642/health
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:9119
```

WSL:

```bash
systemctl --user is-active hermes-gateway hermes-dashboard hermes-workspace
ss -tlnp | grep -E ':8642|:9119|:3000'
curl -fsS http://127.0.0.1:8642/health
curl -fsS -o /dev/null -w "dashboard:%{http_code}\n" http://127.0.0.1:9119
```

Latest observed healthy output:

```text
hermes-gateway: active
hermes-dashboard: active
hermes-workspace: active
gateway health: {"status": "ok", "platform": "hermes-agent"}
dashboard: 200
```

## Logs

Startup logs are written to:

```text
C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\logs\hermes-startup-*.log
```

Most recent verified log during setup:

```text
hermes-startup-20260516_004213.log
```

## Residual Notes

The pinned Windows app is a browser shell. It depends on the local dashboard endpoint being available after login.

If the app opens before the scheduled task finishes, refresh after 30-60 seconds.

Secrets were previously observed in handoff/config context. Treat any exposed provider keys or gateway tokens as rotated-required.
