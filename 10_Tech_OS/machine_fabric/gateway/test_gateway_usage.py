import asyncio
import json
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from fastmcp import Client

HERE = Path(__file__).resolve().parent
MF = HERE.parent
M0 = MF / "m0" / "amf_m0.py"
GATEWAY = HERE / "gateway.py"

def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p

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

async def wait_client(url):
    for _ in range(40):
        try:
            c = Client(url, timeout=4)
            await c.__aenter__()
            return c
        except Exception:
            await asyncio.sleep(0.2)
    raise AssertionError(f"gateway unavailable")

async def main():
    with tempfile.TemporaryDirectory(prefix="aspace-dc-usage-") as td:
        root = Path(td)
        fs_port, gw_port = free_port(), free_port()
        fs_db = root / "fs.sqlite3"
        usage_db = root / "usage.sqlite3"

        test_file = root / "test.txt"
        test_file.write_text("hello usage")

        fs = start_json_line([
            sys.executable, str(M0), "serve", "--db", str(fs_db),
            "--allowed-root", str(root), "--port", str(fs_port)
        ])

        gateway_args = [
            sys.executable, str(GATEWAY),
            "--amf-url", f"http://127.0.0.1:{fs_port}",
            "--usage-db", str(usage_db),
            "--transport", "streamable-http",
            "--host", "127.0.0.1", "--port", str(gw_port)
        ]

        gateway = subprocess.Popen(gateway_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        try:
            client = await wait_client(f"http://127.0.0.1:{gw_port}/mcp")

            # Initial execute
            call_res = await client.call_tool(
                "amf_execute",
                {
                    "capability": "machine.fs.read",
                    "action": "read_text",
                    "operation_id": "op-usage-1",
                    "payload": {"path": "test.txt"},
                    "risk_class": "read",
                    "scope": f"fs:{str(root)}"
                }
            )

            # Check usage ledger via amf_usage
            usage_res = await client.call_tool("amf_usage", {})
            import types

            def get_text(res):
                if hasattr(res, "content") and res.content:
                    return res.content[0].text
                elif isinstance(res, list) and len(res) > 0 and hasattr(res[0], "text"):
                    return res[0].text
                return "{}"

            usage_data = json.loads(get_text(usage_res))
            records = usage_data.get("records", [])

            # Should have the amf_execute and the amf_usage
            amf_execs = [r for r in records if r["tool"] == "amf_execute"]
            assert len(amf_execs) == 1, f"Expected 1 execute, got {len(amf_execs)}: {amf_execs}"
            assert amf_execs[0]["is_replay"] == 0, "First execute should not be replay"
            assert amf_execs[0]["state"] == "SUCCEEDED"
            assert amf_execs[0]["operation_id"] == "op-usage-1"
            print("Initial ledger execution: OK")

            # Replay exactly
            call_res2 = await client.call_tool(
                "amf_execute",
                {
                    "capability": "machine.fs.read",
                    "action": "read_text",
                    "operation_id": "op-usage-1",
                    "payload": {"path": "test.txt"},
                    "risk_class": "read",
                    "scope": f"fs:{str(root)}"
                }
            )
            usage_res2 = await client.call_tool("amf_usage", {})
            usage_data2 = json.loads(get_text(usage_res2))
            amf_execs2 = [r for r in usage_data2.get("records", []) if r["tool"] == "amf_execute"]
            assert len(amf_execs2) == 2, "Expected 2 executes in ledger"
            replay_rec = [r for r in amf_execs2 if r["is_replay"] == 1]
            assert len(replay_rec) == 1, f"Expected 1 replay record: {amf_execs2}"
            print("Ledger replay detection: OK")

            await client.__aexit__(None, None, None)
            stop(gateway)

            # Restart gateway to test persistence
            gw_port2 = free_port()
            gateway_args[-1] = str(gw_port2)
            gateway2 = subprocess.Popen(gateway_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            client2 = await wait_client(f"http://127.0.0.1:{gw_port2}/mcp")
            usage_res3 = await client2.call_tool("amf_usage", {})
            usage_data3 = json.loads(get_text(usage_res3))

            amf_execs3 = [r for r in usage_data3.get("records", []) if r["tool"] == "amf_execute"]
            assert len(amf_execs3) == 2, "Expected ledger to persist across restarts"
            print("Ledger restart persistence: OK")

            await client2.__aexit__(None, None, None)
            stop(gateway2)

        finally:
            stop(fs)
            try: stop(gateway)
            except: pass
            try: stop(gateway2)
            except: pass

if __name__ == "__main__":
    asyncio.run(main())
