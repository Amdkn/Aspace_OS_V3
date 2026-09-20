#!/usr/bin/env python3
"""dc_recovery_daemon.py — Desktop Commander Recovery Path (Proxy-Free).

Garantit le démarrage idempotent de supervisor.mjs (Desktop Commander)
en s'assurant qu'il n'hérite d'aucune variable d'environnement proxy
(LLMTrim ou autre) qui pourrait bloquer son rôle de canal de récupération.
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path

SUPERVISOR_PATH = Path.home() / ".desktop-commander" / "managed" / "supervisor.mjs"

def get_clean_env() -> dict:
    """Retourne l'environnement courant purgé des variables proxy."""
    env = os.environ.copy()
    proxy_vars = [
        "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
        "http_proxy", "https_proxy", "all_proxy",
        "LLMTRIM_PROXY"
    ]
    for var in proxy_vars:
        env.pop(var, None)
    return env

def is_supervisor_running() -> bool:
    """Vérifie si node.exe/node tourne déjà le supervisor."""
    try:
        # pgrep n'est pas fiable sur Windows, on utilise process lookup multiplateforme ou fallback
        if sys.platform == "win32":
            res = subprocess.run(["wmic", "process", "where", "name='node.exe'", "get", "CommandLine"],
                                 capture_output=True, text=True)
            return "supervisor.mjs" in res.stdout
        else:
            res = subprocess.run(["pgrep", "-f", "supervisor.mjs"], capture_output=True)
            return res.returncode == 0
    except Exception:
        return False

def start_supervisor() -> dict:
    """Démarre supervisor.mjs si non lancé et de manière proxy-free."""
    if is_supervisor_running():
        return {"ok": True, "status": "already_running"}

    if not SUPERVISOR_PATH.exists():
        return {"ok": False, "status": "not_found", "error": f"Fichier introuvable: {SUPERVISOR_PATH}"}

    clean_env = get_clean_env()

    try:
        # Lancement détaché
        cmd = ["node", str(SUPERVISOR_PATH)]
        if sys.platform == "win32":
            subprocess.Popen(cmd, env=clean_env, creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            subprocess.Popen(cmd, env=clean_env, start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return {"ok": True, "status": "started", "proxy_stripped": True}
    except Exception as e:
        return {"ok": False, "status": "failed", "error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        running = is_supervisor_running()
        print(json.dumps({"running": running}))
        sys.exit(0 if running else 1)

    res = start_supervisor()
    print(json.dumps(res))
    sys.exit(0 if res["ok"] else 1)
