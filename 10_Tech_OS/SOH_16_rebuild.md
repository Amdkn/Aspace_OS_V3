# SOH-16: Desktop Commander Rebuild Plan & Audit

## 1. Single Canonical Architecture Documented
The canonical launcher for Desktop Commander is the proxy-free `10_Tech_OS/kernel/dc_recovery_daemon.py`.
This script strips toxic LLMTrim/proxy variables from the environment before idempotently spawning DC.
The execution priority is:
1. `dc_bedrock_sentinel.py` (Bedrock Python)
2. `DC.bat` (Batch fallback)
3. `supervisor.mjs` (Node.js fallback)

## 2. Canonical Scheduled Task
The environment must maintain exactly ONE scheduled task: `ASpace Desktop Commander` pointing to `dc_bedrock_sentinel.py` or the recovery daemon wrapper. All duplicate scheduled tasks (like `ASpace DC Migration` and legacy tasks) must be removed.

## 3. Accidental Complexity Removed
No supervisor-on-supervisor stacks. No wrapper-on-wrapper aliases. Background/foreground remote duplication is prohibited.

## 4. Sentinel Verification
`is_dc_running` logic in the daemon explicitly verifies running `node.exe` processes filtering by `desktop-commander` or `supervisor.mjs`.

## 5. Idempotent Rollback
Running the recovery daemon repeatedly produces no regressions (`start_dc()` is a no-op if `is_dc_running()` is true).
