#!/usr/bin/env python3
"""dc_recovery_daemon.py — Desktop Commander Recovery Path (Proxy-Free).

Garantit le démarrage idempotent et antifragile de Desktop Commander
via la Sentinelle Bedrock (dc_bedrock_sentinel.py) et supprime les dépendances superflues
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

    # SOH-16 Cleanup: Remove accidental complexity and duplicate scheduled tasks
    if sys.platform == "win32":
        try:
            # Clean legacy scheduled tasks (keep only 'ASpace Desktop Commander' if any, but SOH-16 says remove duplicates like Migration)
            subprocess.run(["powershell.exe", "-NoProfile", "-Command",
                "Get-ScheduledTask | Where-Object { $_.TaskName -match 'ASpace DC Migration|LegacyDC' } | Unregister-ScheduledTask -Confirm:$false"],
                capture_output=True, timeout=15)
        except Exception:
            pass

    # Priorité 1 : Sentinelle Bedrock Python
    if SENTINEL_PATH.exists():
        try:
            python_exe = "C:\\Python314\\pythonw.exe" if Path("C:\\Python314\\pythonw.exe").exists() else sys.executable
            creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
            subprocess.Popen([python_exe, str(SENTINEL_PATH)], env=clean_env, creationflags=creation_flags)
            return {"ok": True, "status": "started_via_bedrock_sentinel"}
        except Exception as e:
            pass

    # Priorité 2 : Fallback supervisor.mjs
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

    return {"ok": False, "status": "not_found", "error": f"Le fichier {SENTINEL_PATH} est introuvable."}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        status = get_dc_status()
        print(json.dumps(status))
        sys.exit(0 if status["running"] else 1)

    res = start_dc()
    print(json.dumps(res))
    sys.exit(0 if res["ok"] else 1)
