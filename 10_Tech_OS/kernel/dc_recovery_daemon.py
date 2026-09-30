#!/usr/bin/env python3
"""dc_recovery_daemon.py — Desktop Commander Recovery Path (Proxy-Free).

Garantit le démarrage idempotent et antifragile de Desktop Commander
via la Sentinelle Bedrock (dc_bedrock_sentinel.py) ou DC.bat,
en s'assurant qu'il n'hérite d'aucune variable d'environnement proxy
(LLMTrim, 9router, omniroute ou autre) et en garantissant l'absence de régression.
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path

SENTINEL_PATH = Path.home() / ".desktop-commander" / "managed" / "dc_bedrock_sentinel.py"
SUPERVISOR_PATH = Path.home() / ".desktop-commander" / "managed" / "supervisor.mjs"
DC_BAT_PATH = Path.home() / "DC.bat"
STATUS_PATH = Path.home() / ".desktop-commander" / "managed" / "status.json"

def get_clean_env() -> dict:
    """Retourne l'environnement courant purgé des variables proxy."""
    env = os.environ.copy()
    proxy_vars = [
        "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
        "http_proxy", "https_proxy", "all_proxy",
        "LLMTRIM_PROXY", "NO_PROXY", "no_proxy"
    ]
    for var in proxy_vars:
        env.pop(var, None)
    return env

def is_dc_running() -> bool:
    """Vérifie si node.exe tourne déjà le remote ou le supervisor Desktop Commander."""
    try:
        if sys.platform == "win32":
            cmd = ["powershell.exe", "-NoProfile", "-Command",
                   "Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and ($_.CommandLine -like '*desktop-commander*' -or $_.CommandLine -like '*supervisor.mjs*') } | Select-Object -ExpandProperty ProcessId"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            pids = res.stdout.strip().split()
            return len(pids) > 0
        else:
            res = subprocess.run(["pgrep", "-f", "desktop-commander"], capture_output=True)
            return res.returncode == 0
    except Exception:
        return False

def get_dc_status() -> dict:
    """Récupère le statut vivant de Desktop Commander."""
    running = is_dc_running()
    status_data = {}
    if STATUS_PATH.exists():
        try:
            with open(STATUS_PATH, "r", encoding="utf-8") as f:
                status_data = json.load(f)
        except Exception:
            pass
    return {
        "running": running,
        "sentinel_status": status_data.get("status", "unknown"),
        "details": status_data.get("details", "")
    }

def start_dc() -> dict:
    """Démarre Desktop Commander de manière proxy-free, antifragile et idempotente."""
    if is_dc_running():
        return {"ok": True, "status": "already_running"}

    clean_env = get_clean_env()

    # Priorité 1 : Sentinelle Bedrock Python
    if SENTINEL_PATH.exists():
        try:
            # Set repo root so the sentinel can find gateway.py when installed elsewhere
            clean_env["AMF_REPO_ROOT"] = str(Path(__file__).resolve().parent.parent.parent)

            python_exe = "C:\\Python314\\pythonw.exe" if Path("C:\\Python314\\pythonw.exe").exists() else sys.executable
            creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
            subprocess.Popen([python_exe, str(SENTINEL_PATH)], env=clean_env, creationflags=creation_flags)
            return {"ok": True, "status": "started_via_bedrock_sentinel"}
        except Exception as e:
            pass

    # Priorité 2 : DC.bat
    if DC_BAT_PATH.exists():
        try:
            res = subprocess.run(["cmd.exe", "/c", str(DC_BAT_PATH)], env=clean_env, capture_output=True, text=True, timeout=30)
            return {"ok": res.returncode == 0, "status": "started_via_bedrock_bat", "stdout": res.stdout[:200]}
        except Exception as e:
            return {"ok": False, "status": "failed", "error": str(e)}

    # Priorité 3 : Fallback supervisor.mjs
    if SUPERVISOR_PATH.exists():
        try:
            cmd = ["node", str(SUPERVISOR_PATH)]
            if sys.platform == "win32":
                subprocess.Popen(cmd, env=clean_env, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen(cmd, env=clean_env, start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return {"ok": True, "status": "started", "proxy_stripped": True}
        except Exception as e:
            return {"ok": False, "status": "failed", "error": str(e)}

    return {"ok": False, "status": "not_found", "error": f"Ni {SENTINEL_PATH}, ni {DC_BAT_PATH} introuvables."}

def stop_dc():
    if sys.platform == "win32":
        cmd = ["powershell.exe", "-NoProfile", "-Command",
               "Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and ($_.CommandLine -like '*desktop-commander*' -or $_.CommandLine -like '*supervisor.mjs*') } | Stop-Process -Force -ErrorAction SilentlyContinue"]
        subprocess.run(cmd, capture_output=True)
        cmd_python = ["powershell.exe", "-NoProfile", "-Command",
                      "Get-CimInstance Win32_Process | Where-Object { ($_.Name -eq 'python.exe' -or $_.Name -eq 'pythonw.exe') -and ($_.CommandLine -like '*dc_bedrock_sentinel.py*' -or $_.CommandLine -like '*gateway.py*') } | Stop-Process -Force -ErrorAction SilentlyContinue"]
        subprocess.run(cmd_python, capture_output=True)
    else:
        subprocess.run(["pkill", "-f", "desktop-commander"], capture_output=True)
        subprocess.run(["pkill", "-f", "dc_bedrock_sentinel.py"], capture_output=True)
        subprocess.run(["pkill", "-f", "gateway.py"], capture_output=True)

    if STATUS_PATH.exists():
        try:
            STATUS_PATH.unlink()
        except:
            pass
    return {"ok": True, "status": "stopped"}

def install_dc():
    dc_root = Path.home() / ".aspace" / "dc"
    runtime_dest = dc_root / "runtime"

    # 1. Clear existing runtime if any
    import shutil
    if runtime_dest.exists():
        shutil.rmtree(runtime_dest, ignore_errors=True)

    runtime_dest.mkdir(parents=True, exist_ok=True)

    # 2. Copy the complete machine_fabric tree
    repo_root = Path(__file__).resolve().parent.parent.parent
    src_mf = repo_root / "10_Tech_OS" / "machine_fabric"

    if src_mf.exists():
        shutil.copytree(src_mf, runtime_dest / "machine_fabric")

    # 3. Create config.json pointing to the runtime
    config_path = dc_root / "config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump({
            "runtime_root": str(runtime_dest),
            "gateway_path": str(runtime_dest / "machine_fabric" / "gateway" / "gateway.py"),
            "m0_path": str(runtime_dest / "machine_fabric" / "m0" / "amf_m0.py"),
            "process_path": str(runtime_dest / "machine_fabric" / "process" / "process_broker.py"),
            "session_daemon_path": str(runtime_dest / "machine_fabric" / "m1" / "session_daemon.py")
        }, f, indent=2)

    # 4. Copy sentinel
    SENTINEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    src_sentinel = Path(__file__).parent / "dc_bedrock_sentinel.py"
    if src_sentinel.exists():
        shutil.copy2(src_sentinel, SENTINEL_PATH)

    # 5. Copy launchers and this daemon to the dc_root to be independent of the repo
    shutil.copy2(Path(__file__), dc_root / "dc_recovery_daemon.py")

    # Generate standalone dc.bat
    dc_bat_content = """@echo off
python "%~dp0dc_recovery_daemon.py" %*
"""
    with open(dc_root / "dc.bat", "w", encoding="utf-8") as f:
        f.write(dc_bat_content)

    # We must generate an independent dc.ps1 for the installed location
    # because the one in the repo expects the repo structure.
    dc_ps1_content = """param (
    [Parameter(Position=0)]
    [string]$Action = "start"
)

$ErrorActionPreference = "Stop"
$scriptPath = $MyInvocation.MyCommand.Path
$dcRoot = Split-Path $scriptPath -Parent
$daemonPath = Join-Path $dcRoot "dc_recovery_daemon.py"

if (-not (Test-Path $daemonPath)) {
    Write-Error "Daemon not found at $daemonPath. Install is broken."
    exit 1
}

& python $daemonPath $Action
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
"""
    with open(dc_root / "dc.ps1", "w", encoding="utf-8") as f:
        f.write(dc_ps1_content)

    return {"ok": True, "status": "installed"}

def uninstall_dc():
    stop_dc()
    try:
        if SENTINEL_PATH.exists():
            SENTINEL_PATH.unlink()
        if STATUS_PATH.exists():
            STATUS_PATH.unlink()

        import shutil
        dc_root = Path.home() / ".aspace" / "dc"
        if dc_root.exists():
            shutil.rmtree(dc_root, ignore_errors=True)
    except:
        pass
    return {"ok": True, "status": "uninstalled"}

def update_dc():
    install_dc()
    stop_dc()
    time.sleep(1)
    res = start_dc()
    return {"ok": res["ok"], "status": "updated"}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("action", nargs="?", default="start", choices=["start", "stop", "restart", "status", "install", "uninstall", "update"])
    args = parser.parse_args()

    if args.action == "status":
        status = get_dc_status()
        print(json.dumps(status))
        sys.exit(0 if status["running"] else 1)
    elif args.action == "start":
        res = start_dc()
        print(json.dumps(res))
        sys.exit(0 if res["ok"] else 1)
    elif args.action == "stop":
        res = stop_dc()
        print(json.dumps(res))
        sys.exit(0)
    elif args.action == "restart":
        stop_dc()
        time.sleep(1)
        res = start_dc()
        print(json.dumps(res))
        sys.exit(0 if res["ok"] else 1)
    elif args.action == "install":
        res = install_dc()
        print(json.dumps(res))
        sys.exit(0)
    elif args.action == "uninstall":
        res = uninstall_dc()
        print(json.dumps(res))
        sys.exit(0)
    elif args.action == "update":
        res = update_dc()
        print(json.dumps(res))
        sys.exit(0 if res["ok"] else 1)
