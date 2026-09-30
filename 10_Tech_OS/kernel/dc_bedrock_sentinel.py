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

        dc_root = Path.home() / ".aspace" / "dc"
        config_path = dc_root / "config.json"

        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
            gateway_py = config.get("gateway_path")
            if not gateway_py or not Path(gateway_py).exists():
                raise RuntimeError(f"Configured gateway path not found: {gateway_py}")
        else:
            # Fallback for development/testing directly from tree
            repo_root_env = os.environ.get("AMF_REPO_ROOT")
            if repo_root_env:
                repo_root = Path(repo_root_env).resolve()
            else:
                repo_root = Path(__file__).resolve().parent.parent.parent
            gateway_py = str(repo_root / "10_Tech_OS" / "machine_fabric" / "gateway" / "gateway.py")

        import socket
        def free_port():
            s = socket.socket()
            s.bind(("127.0.0.1", 0))
            p = s.getsockname()[1]
            s.close()
            return p

        gw_port = free_port()
        amf_url = os.environ.get("AMF_M0_URL", "http://127.0.0.1:8001") # Still fallback logic for M0

        # Expose worker URL explicitly in run/runtime.json as requested
        run_dir = Path.home() / ".desktop-commander" / "managed"
        runtime_json = run_dir / "runtime.json"
        with open(runtime_json, "w", encoding="utf-8") as f:
            json.dump({
                "worker_url": f"http://127.0.0.1:{gw_port}",
                "fence": 1,
                "generation": int(time.time())
            }, f, indent=2)

        cmd = [sys.executable, gateway_py, "--amf-url", amf_url, "--transport", "streamable-http", "--port", str(gw_port)]

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
