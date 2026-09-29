import asyncio
import json
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

from fastmcp import Client

HERE = Path(__file__).resolve().parent
MF = HERE.parent
M0 = MF / "m0" / "amf_m0.py"
PROC = MF / "process" / "process_broker.py"
FIX = MF / "process" / "interactive_fixture.py"
BROWSER = MF / "m1" / "session_daemon.py"
GATEWAY = HERE / "gateway.py"


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def post(url, payload):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=body, method="POST", headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=3) as r:
        return json.loads(r.read().decode())


def start_json_line(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    line = p.stdout.readline().strip()
    if not line:
        err = p.stderr.read()
        raise RuntimeError(f"failed to start {cmd}: {err[-1200:]}")
    json.loads(line)
    return p


def stop(p):
    if not p:
        return
    if p.poll() is None:
        p.terminate()
        try:
            p.wait(4)
        except subprocess.TimeoutExpired:
            p.kill()
            p.wait(4)
    if p.stdout:
        p.stdout.close()
    if p.stderr:
        p.stderr.close()


def result_text(result):
    parts = []
    for item in getattr(result, "content", []) or []:
        text = getattr(item, "text", None)
        if text is not None:
            parts.append(text)
    return "\n".join(parts)


async def wait_client(url):
    last = None
    for _ in range(40):
        try:
            c = Client(url, timeout=4)
            await c.__aenter__()
            return c
        except Exception as exc:
            last = exc
            await asyncio.sleep(0.2)
    raise AssertionError(f"gateway unavailable: {last}")


async def main():
    with tempfile.TemporaryDirectory(prefix="aspace-dc-gateway-") as td:
        root = Path(td)
        fs_port, proc_port, browser_port, gw_port = [free_port() for _ in range(4)]
        fs_db = root / "fs.sqlite3"
        proc_db = root / "proc.sqlite3"
        browser_db = root / "browser.sqlite3"

        fs = proc = browser = gateway = client = None
        try:
            fs = start_json_line(
                [
                    sys.executable,
                    str(M0),
                    "serve",
                    "--db",
                    str(fs_db),
                    "--allowed-root",
                    str(root),
                    "--port",
                    str(fs_port),
                ]
            )
            proc = start_json_line(
                [
                    sys.executable,
                    str(PROC),
                    "--db",
                    str(proc_db),
                    "--allowed-root",
                    str(root),
                    "--allow-exe",
                    sys.executable,
                    "--port",
                    str(proc_port),
                ]
            )
            browser = start_json_line(
                [
                    sys.executable,
                    str(BROWSER),
                    "--db",
                    str(browser_db),
                    "--port",
                    str(browser_port),
                ]
            )
            gateway = subprocess.Popen(
                [
                    sys.executable,
                    str(GATEWAY),
                    "--amf-url",
                    f"http://127.0.0.1:{fs_port}",
                    "--process-url",
                    f"http://127.0.0.1:{proc_port}",
                    "--browser-url",
                    f"http://127.0.0.1:{browser_port}",
                    "--transport",
                    "streamable-http",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(gw_port),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            client = await wait_client(f"http://127.0.0.1:{gw_port}/mcp")
            tools = await client.list_tools()
            names = {x.name for x in tools}
            assert {"amf_health", "amf_capabilities", "amf_execute", "amf_get_receipt"} <= names

            caps_result = await client.call_tool("amf_capabilities", {})
            caps = json.loads(result_text(caps_result))
            by_id = {x["capability_id"]: x for x in caps["capabilities"]}
            assert by_id["machine.fs.read"]["availability"] == "AVAILABLE"
            assert by_id["machine.process.start"]["availability"] == "AVAILABLE"
            assert by_id["machine.process.read"]["availability"] == "AVAILABLE"
            assert by_id["browser.tabs.read"]["availability"] == "UNAVAILABLE"
            print("Unified capability inventory: OK")

            start_result = await client.call_tool(
                "amf_execute",
                {
                    "capability": "machine.process.start",
                    "action": "start",
                    "operation_id": "gw-process-start-001",
                    "payload": {"argv": [sys.executable, str(FIX)], "cwd": str(root)},
                    "risk_class": "consequential",
                    "scope": f"process:root:{root}",
                },
            )
            start_payload = json.loads(result_text(start_result))
            assert start_payload["state"] == "SUCCEEDED", start_payload
            session_id = start_payload["result"]["session_id"]
            print("Process start through unified MCP: OK")

            ready = False
            for i in range(25):
                read_result = await client.call_tool(
                    "amf_execute",
                    {
                        "capability": "machine.process.read",
                        "action": "read",
                        "operation_id": f"gw-process-read-{i:03d}",
                        "payload": {"session_id": session_id},
                        "risk_class": "read",
                        "scope": f"process:root:{root}",
                    },
                )
                read_payload = json.loads(result_text(read_result))
                if "READY" in read_payload.get("result", {}).get("text", ""):
                    ready = True
                    break
                await asyncio.sleep(0.1)
            assert ready
            print("Process read through unified MCP: OK")

            stop_result = await client.call_tool(
                "amf_execute",
                {
                    "capability": "machine.process.stop",
                    "action": "stop",
                    "operation_id": "gw-process-stop-001",
                    "payload": {"session_id": session_id},
                    "risk_class": "consequential",
                    "scope": f"process:root:{root}",
                },
            )
            stop_payload = json.loads(result_text(stop_result))
            assert stop_payload["state"] == "SUCCEEDED", stop_payload
            print("Process stop through unified MCP: OK")

            reg = post(
                f"http://127.0.0.1:{browser_port}/worker/register",
                {
                    "worker_id": "gateway-test-worker",
                    "session_id": "gateway-test-session",
                    "capabilities": ["browser.tabs.read", "browser.dom.action"],
                },
            )
            assert reg["fencing_token"] >= 1
            caps2 = json.loads(result_text(await client.call_tool("amf_capabilities", {})))
            by_id2 = {x["capability_id"]: x for x in caps2["capabilities"]}
            assert by_id2["browser.tabs.read"]["availability"] == "AVAILABLE"
            assert by_id2["browser.dom.action"]["availability"] == "AVAILABLE"
            assert by_id2["browser.debugger.attach"]["availability"] == "UNAVAILABLE"
            print("Browser presence UNAVAILABLE->AVAILABLE through unified MCP: OK")

            browser_exec = json.loads(
                result_text(
                    await client.call_tool(
                        "amf_execute",
                        {
                            "capability": "browser.dom.action",
                            "action": "set_text",
                            "operation_id": "browser-p3-boundary",
                            "payload": {"selector": "#x", "value": "y"},
                            "risk_class": "consequential",
                            "scope": "browser:tab:selected",
                        },
                    )
                )
            )
            assert browser_exec["state"] == "UNAVAILABLE"
            assert browser_exec["error"] == "BROWSER_EXECUTION_REQUIRES_P3_PRODUCTION_BRIDGE"
            print("Browser P3 authority boundary: OK")

            health = json.loads(result_text(await client.call_tool("amf_health", {})))
            assert health["backends"]["filesystem"]["aggregate"] == "ONLINE"
            assert health["backends"]["process"]["aggregate"] == "ONLINE"
            print("Normalized multi-backend health: OK")

            print("UNIFIED_GATEWAY_ACCEPTANCE=PASS")
        finally:
            if client is not None:
                await client.__aexit__(None, None, None)
            stop(gateway)
            stop(browser)
            stop(proc)
            stop(fs)


if __name__ == "__main__":
    asyncio.run(main())
