#!/usr/bin/env python3
"""dc_sovereign_daemon.py — Persistent Windows Runtime for DC Sovereign

Background daemon owner that separates the user-session worker lifecycle
from the machine daemon, ensuring a proxy-isolated launch environment,
idempotent true PID/lease/state tracking, and stale PID recovery.
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path

STATE_DIR = Path.home() / ".aspace" / "dc_sovereign"
STATE_FILE = STATE_DIR / "state.json"
GATEWAY_PATH = Path(__file__).resolve().parent.parent / "gateway" / "gateway.py"

def get_clean_env() -> dict:
    """Returns the current environment stripped of toxic proxy variables."""
    env = os.environ.copy()
    proxy_vars = [
        "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
        "http_proxy", "https_proxy", "all_proxy",
        "LLMTRIM_PROXY", "NO_PROXY", "no_proxy"
    ]
    for var in proxy_vars:
        env.pop(var, None)
    return env

def get_state() -> dict:
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"daemon_pid": None, "worker_pid": None, "status": "down"}

def save_state(state: dict):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def is_process_running(pid: int) -> bool:
    if not pid:
        return False
    try:
        # psutil isn't guaranteed, use standard OS methods
        if sys.platform == "win32":
            res = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True)
            return str(pid) in res.stdout
        else:
            os.kill(pid, 0)
            return True
    except OSError:
        return False

def start_worker():
    """Starts the user-session worker in a proxy-isolated environment."""
    clean_env = get_clean_env()
    python_exe = sys.executable
    cmd = [python_exe, str(GATEWAY_PATH), "--amf-url", "http://127.0.0.1:8000", "--name", "aspace-dc-sovereign", "--transport", "streamable-http", "--port", "8002"]

    creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    proc = subprocess.Popen(cmd, env=clean_env, creationflags=creation_flags)
    return proc.pid

def main():
    daemon_pid = os.getpid()
    state = get_state()

    # Idempotent start: if daemon is already running elsewhere, exit
    if state.get("daemon_pid") and is_process_running(state["daemon_pid"]):
        if state["daemon_pid"] != daemon_pid:
            print("Daemon already running")
            sys.exit(0)

    # Initialize state
    state["daemon_pid"] = daemon_pid
    state["status"] = "starting"
    save_state(state)

    worker_pid = state.get("worker_pid")

    try:
        while True:
            # Stale PID recovery & watchdog
            if not is_process_running(worker_pid):
                worker_pid = start_worker()
                state["worker_pid"] = worker_pid
                state["status"] = "running"
                save_state(state)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        state["status"] = "stopped"
        state["daemon_pid"] = None
        save_state(state)

if __name__ == "__main__":
    main()
