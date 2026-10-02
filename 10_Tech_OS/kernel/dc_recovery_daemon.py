#!/usr/bin/env python3
"""dc_recovery_daemon.py — Desktop Commander Recovery Path (Proxy-Free).

Garantit le démarrage idempotent et antifragile de Desktop Commander
via le runtime souverain A'Space; le Desktop Commander hébergé reste un fallback explicite,
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
SOVEREIGN_DC_SCRIPT = Path(__file__).resolve().parents[1] / "machine_fabric" / "runtime" / "dc.ps1"
SOVEREIGN_ROOT = Path.home() / ".aspace" / "dc"
HOSTED_FALLBACK_ENV = "ASPACE_ALLOW_HOSTED_DC_FALLBACK"

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


def hosted_fallback_allowed(env: dict | None = None) -> bool:
    """Hosted Desktop Commander is an explicit fallback, never the default path."""
    source = os.environ if env is None else env
    return str(source.get(HOSTED_FALLBACK_ENV, "")).strip().lower() in {"1", "true", "yes", "on"}


def recovery_order(env: dict | None = None) -> list[str]:
    """Machine-readable recovery policy."""
    order = ["sovereign_repo_runtime", "sovereign_local_launcher"]
    if hosted_fallback_allowed(env):
        order.extend(["hosted_bedrock_sentinel", "hosted_legacy_supervisor"])
    return order


def start_sovereign_dc(clean_env: dict) -> dict:
    """Start the repo-owned Sovereign DC control plane."""
    if not SOVEREIGN_DC_SCRIPT.exists():
        return {"ok": False, "status": "sovereign_script_missing", "path": str(SOVEREIGN_DC_SCRIPT)}
    try:
        cmd = [
            "powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass",
            "-File", str(SOVEREIGN_DC_SCRIPT), "start",
            "-Root", str(SOVEREIGN_ROOT),
        ]
        res = subprocess.run(cmd, env=clean_env, capture_output=True, text=True, timeout=30)
        payload = {}
        if res.stdout.strip():
            try:
                payload = json.loads(res.stdout)
            except Exception:
                payload = {"stdout": res.stdout[:500]}
        return {
            "ok": res.returncode == 0,
            "status": "sovereign_started" if res.returncode == 0 else "sovereign_failed",
            "returncode": res.returncode,
            "runtime": payload,
            "stderr": res.stderr[:500],
        }
    except Exception as exc:
        return {"ok": False, "status": "sovereign_failed", "error": str(exc)}


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
    """Start A'Space machine access with Sovereign DC as primary authority.

    Hosted Desktop Commander is deliberately opt-in. This prevents an installed
    hosted fallback from re-entering the critical path or spawning device-auth UI
    during autonomous recovery.
    """
    clean_env = get_clean_env()

    # Priority 1: repo-owned Sovereign DC. Its control script is idempotent.
    sovereign = start_sovereign_dc(clean_env)
    if sovereign.get("ok"):
        return sovereign

    # Priority 2: installed local sovereign launcher, retained for compatibility.
    if DC_BAT_PATH.exists():
        try:
            res = subprocess.run(
                ["cmd.exe", "/c", str(DC_BAT_PATH)],
                env=clean_env,
                capture_output=True,
                text=True,
                timeout=30,
            )
            if res.returncode == 0:
                return {
                    "ok": True,
                    "status": "started_via_sovereign_local_launcher",
                    "stdout": res.stdout[:200],
                }
        except Exception:
            pass

    # Hosted fallback is never selected implicitly.
    if not hosted_fallback_allowed(clean_env):
        return {
            "ok": False,
            "status": "sovereign_unavailable_hosted_fallback_disabled",
            "recovery_order": recovery_order(clean_env),
            "sovereign": sovereign,
            "hint": f"Set {HOSTED_FALLBACK_ENV}=1 only for an explicit hosted fallback session.",
        }

    if SENTINEL_PATH.exists():
        try:
            python_exe = "C:\\Python314\\pythonw.exe" if Path("C:\\Python314\\pythonw.exe").exists() else sys.executable
            creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
            subprocess.Popen([python_exe, str(SENTINEL_PATH)], env=clean_env, creationflags=creation_flags)
            return {"ok": True, "status": "started_via_explicit_hosted_bedrock_sentinel"}
        except Exception:
            pass

    if SUPERVISOR_PATH.exists():
        try:
            cmd = ["node", str(SUPERVISOR_PATH)]
            if sys.platform == "win32":
                subprocess.Popen(cmd, env=clean_env, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen(cmd, env=clean_env, start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return {"ok": True, "status": "started_via_explicit_hosted_legacy_supervisor", "proxy_stripped": True}
        except Exception as exc:
            return {"ok": False, "status": "hosted_fallback_failed", "error": str(exc)}

    return {
        "ok": False,
        "status": "not_found",
        "error": "Sovereign DC unavailable and no explicit hosted fallback runtime was found.",
    }

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        status = get_dc_status()
        print(json.dumps(status))
        sys.exit(0 if status["running"] else 1)

    res = start_dc()
    print(json.dumps(res))
    sys.exit(0 if res["ok"] else 1)
