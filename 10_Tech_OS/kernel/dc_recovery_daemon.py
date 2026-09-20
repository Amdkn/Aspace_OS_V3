#!/usr/bin/env python3
"""dc_recovery_daemon.py — Desktop Commander Recovery Path (Proxy-Free).

Garantit le démarrage idempotent de Desktop Commander / supervisor
en s'assurant qu'il n'hérite d'aucune variable d'environnement proxy
(LLMTrim, 9router, omniroute ou autre) qui pourrait bloquer son rôle de canal de récupération.
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path

SUPERVISOR_PATH = Path.home() / ".desktop-commander" / "managed" / "supervisor.mjs"
DC_BAT_PATH = Path.home() / "DC.bat"

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
            # Utilise PowerShell sans wmic pour compatibilité universelle
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

def start_dc() -> dict:
    """Démarre Desktop Commander de manière proxy-free et idempotente."""
    if is_dc_running():
        return {"ok": True, "status": "already_running"}

    clean_env = get_clean_env()

    if DC_BAT_PATH.exists():
        try:
            res = subprocess.run(["cmd.exe", "/c", str(DC_BAT_PATH)], env=clean_env, capture_output=True, text=True, timeout=30)
            return {"ok": res.returncode == 0, "status": "started_via_bedrock_bat", "stdout": res.stdout[:200]}
        except Exception as e:
            return {"ok": False, "status": "failed", "error": str(e)}

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

    return {"ok": False, "status": "not_found", "error": f"Ni {DC_BAT_PATH} ni {SUPERVISOR_PATH} introuvables."}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        running = is_dc_running()
        print(json.dumps({"running": running}))
        sys.exit(0 if running else 1)

    res = start_dc()
    print(json.dumps(res))
    sys.exit(0 if res["ok"] else 1)
