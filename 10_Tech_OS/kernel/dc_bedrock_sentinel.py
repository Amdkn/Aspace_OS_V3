import sys
import ctypes
from ctypes import wintypes
import time
import os
import subprocess
import json
from pathlib import Path

# Create unique mutex to prevent duplicate execution
ERROR_ALREADY_EXISTS = 183
mutex_name = r"Global\ASpace_DC_Bedrock_Mutex"

def get_clean_env():
    env = os.environ.copy()
    proxy_vars = [
        "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
        "http_proxy", "https_proxy", "all_proxy",
        "LLMTRIM_PROXY", "NO_PROXY", "no_proxy"
    ]
    for var in proxy_vars:
        env.pop(var, None)
    return env

def main():
    if sys.platform == "win32":
        handle = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
        last_error = ctypes.windll.kernel32.GetLastError()

        if last_error == ERROR_ALREADY_EXISTS:
            print(json.dumps({"ok": True, "status": "already_running"}))
            sys.exit(0)

    # We hold the mutex, start daemon loop.
    STATUS_PATH = Path.home() / ".desktop-commander" / "managed" / "status.json"
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)

    status_data = {"status": "running", "details": "Started by Sentinel"}
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        json.dump(status_data, f)

    gateway_proc = None
    try:
        clean_env = get_clean_env()

        # Resolve the repository root intelligently. If AMF_REPO_ROOT is set, use it.
        repo_root_env = os.environ.get("AMF_REPO_ROOT")
        if repo_root_env:
            REPO_ROOT = Path(repo_root_env).resolve()
        else:
            # Fallback if installed, assuming standard layout from original source tree
            # But the safer way is to rely on environment variable injected by the installer/launcher
            raise RuntimeError("AMF_REPO_ROOT environment variable must be set to locate the gateway.py.")

        GATEWAY_PY = REPO_ROOT / "10_Tech_OS" / "machine_fabric" / "gateway" / "gateway.py"

        # M0 daemon url and other parameters would be dynamically resolved, but we use defaults/env overrides for now.
        amf_url = os.environ.get("AMF_M0_URL", "http://127.0.0.1:8001")
        cmd = [sys.executable, str(GATEWAY_PY), "--amf-url", amf_url, "--transport", "streamable-http", "--port", "8001"]

        creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        gateway_proc = subprocess.Popen(cmd, env=clean_env, creationflags=creation_flags, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        while True:
            if gateway_proc.poll() is not None:
                # Gateway died, restart it
                status_data["details"] = "Gateway restarted"
                gateway_proc = subprocess.Popen(cmd, env=clean_env, creationflags=creation_flags, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            with open(STATUS_PATH, "w", encoding="utf-8") as f:
                status_data["heartbeat"] = time.time()
                json.dump(status_data, f)
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    except SystemExit:
        pass
    except Exception as e:
        status_data["details"] = f"Failed to start: {str(e)}"
        with open(STATUS_PATH, "w", encoding="utf-8") as f:
            json.dump(status_data, f)
    finally:
        if gateway_proc and gateway_proc.poll() is None:
            gateway_proc.terminate()
            try:
                gateway_proc.wait(timeout=5)
            except:
                gateway_proc.kill()

        if sys.platform == "win32":
            ctypes.windll.kernel32.ReleaseMutex(handle)

if __name__ == "__main__":
    main()
