The goal is to build the persistent Windows runtime for A Space Sovereign Desktop Commander (DC) based on issue #214.

Requirements:
- Idempotent install/start/stop/restart/status/update/uninstall commands
- Background daemon owner, true PID/lease/state
- User-session worker lifecycle separate from machine daemon
- Proxy-isolated DC launch environment (no proxy drift)
- Stale PID recovery
- Watchdog/health monitoring
- Uninstall/rollback support
- Stable local alias/launcher (`dc_sovereign.ps1` or similar)
- Do NOT depend on hosted Desktop Commander, Tailscale, or a foreground terminal.
- Reuse existing Machine Fabric/Harness Runtime primitives (e.g., `dc_recovery_daemon.py`, `gateway.py`, etc.).
- Add deterministic tests and evidence.

Plan:
1. Create a `10_Tech_OS/machine_fabric/dc_sovereign/` directory.
2. Inside, create a PowerShell module/script `dc_sovereign.ps1` that implements the commands: `install`, `start`, `stop`, `restart`, `status`, `update`, `uninstall`.
   - It will use `dc_recovery_daemon.py` or a dedicated Python script `dc_sovereign_daemon.py` to start the process without a terminal.
   - It should strip proxies (using the same logic as `get_clean_env()` in `dc_recovery_daemon.py`).
   - Use `Start-Process -NoNewWindow` or similar to run in the background as a daemon.
   - It will store its PID and status in `~/.aspace/dc_sovereign/state.json`.
3. Create `10_Tech_OS/machine_fabric/dc_sovereign/dc_sovereign_daemon.py` to act as the actual background daemon. It will:
   - Handle the health check/watchdog loop.
   - Manage the separate user-session worker lifecycle.
   - Update `state.json` with truthful PIDs and leases.
4. Add unit tests for `dc_sovereign_daemon.py` to ensure it correctly recovers stale PIDs, ignores proxies, and properly manages state.
5. Create an evidence JSON file `10_Tech_OS/reports/dc_sovereign_214_evidence.json` asserting the requirements are met.
6. Commit the changes referencing #214.
