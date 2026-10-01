import asyncio
import json
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
import os
from pathlib import Path

from fastmcp import Client

HERE = Path(__file__).resolve().parent
MF = HERE.parent
M0 = MF / "m0" / "amf_m0.py"
PROC = MF / "process" / "process_broker.py"
BROWSER = MF / "m1" / "session_daemon.py"
GATEWAY = HERE / "gateway.py"

def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p

def post(url, payload):
    b = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=b, method="POST", headers={
            "Content-Type": "application/json",
            "Content-Length": str(len(b)),
            "Connection": "close"
        }
    )
    with urllib.request.urlopen(req, timeout=3) as r:
        return r.status, json.loads(r.read().decode("utf-8"))

def start_json_line(cmd):
    env = {**os.environ, "PYTHONPATH": str(Path(__file__).resolve().parents[2])}
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    try:
        line = p.stdout.readline()
        if not line:
            import time
            time.sleep(1)
            line = p.stdout.readline()
        data = json.loads(line)
        return p, data
    except Exception as e:
        stderr_out = p.stderr.read()
        p.kill()
        raise RuntimeError(f"Failed to start {cmd} with line {repr(line)}: {e}\nSTDERR:\n{stderr_out}")

def stop(p):
    p.terminate()
    try:
        p.wait(timeout=2)
    except subprocess.TimeoutExpired:
        p.kill()

def result_text(result):
    if hasattr(result, "content") and result.content:
        return result.content[0].text
    return str(result)

async def wait_client(url):
    client = Client(url)
    for _ in range(30):
        try:
            await client.__aenter__()
            return client
        except Exception:
            time.sleep(0.1)
    raise RuntimeError("Failed to connect to gateway MCP")

async def main():
    print("Testing AMF Presence (amf_presence tool)...")
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        m0_db = tdp / "m0.db"
        proc_db = tdp / "proc.db"
        sess_db = tdp / "sess.db"
        usage_db = tdp / "usage.db"

        pm0, pm0_d = start_json_line(
            [sys.executable, str(M0), "serve", "--db", str(m0_db), "--allowed-root", str(tdp), "--port", "0"]
        )
        url0 = f"http://127.0.0.1:{pm0_d['port']}"
        

        pproc, pproc_d = start_json_line(
            [sys.executable, str(PROC), "--db", str(proc_db), "--allowed-root", str(tdp), "--allow-exe", "echo", "--port", "0"]
        )
        urlproc = f"http://127.0.0.1:{pproc_d['port']}"
        

        psess, psess_d = start_json_line(
            [sys.executable, str(BROWSER), "--db", str(sess_db), "--port", "0"]
        )
        urlsess = f"http://127.0.0.1:{psess_d['port']}"
        
        import time
        time.sleep(1)

        p_gw = free_port()
        env = {**os.environ, "PYTHONPATH": str(Path(__file__).resolve().parents[2])}
        pgw = subprocess.Popen(
            [
                sys.executable, str(GATEWAY),
                "--amf-url", url0,
                "--process-url", urlproc,
                "--browser-url", urlsess,
                "--usage-db", str(usage_db),
                "--transport", "streamable-http",
                "--host", "127.0.0.1",
                "--port", str(p_gw),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env
        )

        gw_url = f"http://127.0.0.1:{p_gw}/mcp"
        client = None

        try:
            client = await wait_client(gw_url)

            # Test 1: Initial presence
            presence_resp = json.loads(result_text(await client.call_tool("amf_presence", {})))
            assert presence_resp["schema"] == "aspace.dc.presence.v1"
            
            backends = presence_resp["backends"]
            
            
            assert "filesystem" in backends
            assert backends["filesystem"]["active"] == True
            
            assert "process" in backends
            assert backends["process"]["active"] == True
            assert backends["process"]["orphaned_sessions"] == 0
            
            if "browser" in backends:
                assert backends["browser"]["active"] == False
                assert backends["browser"].get("degraded_reason") in [None, "NO_WORKER_EVER_REGISTERED"] or "RemoteDisconnected" in str(backends["browser"].get("degraded_reason")) or "NO_WORKER_EVER_REGISTERED" in str(backends["browser"].get("degraded_reason")) or "Remote end closed connection" in str(backends["browser"].get("degraded_reason"))
            print("Initial presence with no browser worker: OK")

            # Test 2: Browser worker registers
            w_id = "test-worker-1"
            s_id = "test-session-1"
            post(urlsess + "/worker/register", {"worker_id": w_id, "session_id": s_id, "capabilities": ["browser.dom.action"]})
            time.sleep(1)
            presence_resp = json.loads(result_text(await client.call_tool("amf_presence", {})))
            backends = presence_resp["backends"]
            
            
            assert backends["browser"]["active"] == True
            assert backends["browser"]["worker_id"] == w_id
            assert backends["browser"]["session_id"] == s_id
            assert "degraded_reason" not in backends["browser"] or backends["browser"]["degraded_reason"] is None
            print("Browser presence ACTIVE after registration: OK")

            # Test 3: Browser worker TTL expires (simulated by sleep > LEASE_TTL of 2.0s)
            time.sleep(2.5)
            
            presence_resp = json.loads(result_text(await client.call_tool("amf_presence", {})))
            backends = presence_resp["backends"]
            assert backends["browser"]["active"] == False
            assert backends["browser"]["ttl_expired"] == True
            assert backends["browser"]["worker_id"] == w_id # Still tracks the stale worker ID
            assert "WORKER_TTL_EXPIRED_STALE" in backends["browser"].get("degraded_reason", "")
            print("Browser presence STALE/DEGRADED after TTL expiration: OK")

            # Test 4: Heartbeat restores presence
            req = urllib.request.Request(urlsess + "/health", headers={"Connection": "close"})
            health_state = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
            fence = health_state.get("fencing_token") or health_state["presence"]["fencing_token"]
            
            post(urlsess + "/worker/heartbeat", {"worker_id": w_id, "fencing_token": fence})
            
            presence_resp = json.loads(result_text(await client.call_tool("amf_presence", {})))
            backends = presence_resp["backends"]
            assert backends["browser"]["active"] == True
            assert backends["browser"]["ttl_expired"] == False
            print("Browser presence RESTORED after heartbeat: OK")
            
            print("All AMF presence tests passed!")

        finally:
            if client:
                try:
                    await client.__aexit__(None, None, None)
                except Exception:
                    pass
            stop(pgw)
            stop(psess)
            stop(pproc)
            stop(pm0)

if __name__ == "__main__":
    asyncio.run(main())
