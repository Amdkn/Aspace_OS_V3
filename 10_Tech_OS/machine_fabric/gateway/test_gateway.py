import sys
import os
import json
import subprocess
import time
import tempfile
import urllib.request
import urllib.error
import asyncio
from pathlib import Path
from fastmcp import Client

def run_test():
    root = Path(__file__).resolve().parent.parent
    amf_m0 = root / "m0" / "amf_m0.py"
    gateway = root / "gateway" / "gateway.py"

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        db_path = tdp / "amf.db"

        m0_proc = subprocess.Popen(
            [sys.executable, str(amf_m0), "serve", "--db", str(db_path), "--allowed-root", str(tdp), "--port", "0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        daemon_start = m0_proc.stdout.readline()
        try:
            start_info = json.loads(daemon_start)
            port = start_info["port"]
        except Exception as e:
            print(f"Failed to start daemon: {daemon_start}")
            m0_proc.terminate()
            sys.exit(1)

        amf_url = f"http://127.0.0.1:{port}"
        print(f"AMF M0 daemon running on {amf_url}")

        test_file = tdp / "test.txt"
        test_file.write_text("hello world")

        # Test Stdio transport
        gateway_proc_stdio = subprocess.Popen(
            [sys.executable, str(gateway), "--amf-url", amf_url],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        try:
            # MCP Initialize
            init_req = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "test-client", "version": "1.0.0"}
                }
            }
            gateway_proc_stdio.stdin.write(json.dumps(init_req) + "\n")
            gateway_proc_stdio.stdin.flush()
            resp = gateway_proc_stdio.stdout.readline()
            if "protocolVersion" not in resp:
                raise AssertionError(f"STDIO initialize failed: {resp}")
            print("STDIO Init: OK")

            # Tools List
            list_req = {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {}
            }
            gateway_proc_stdio.stdin.write(json.dumps(list_req) + "\n")
            gateway_proc_stdio.stdin.flush()
            resp = gateway_proc_stdio.stdout.readline()
            if "amf_execute" not in resp:
                raise AssertionError(f"STDIO tools/list failed: {resp}")
            print("STDIO Tools List: OK")

            # Tools Call (Read)
            call_req = {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "amf_execute",
                    "arguments": {
                        "capability": "machine.fs.read",
                        "action": "read_text",
                        "operation_id": "op-test-1",
                        "payload": {"path": "test.txt"},
                        "risk_class": "read",
                        "scope": f"fs:{str(tdp)}"
                    }
                }
            }
            gateway_proc_stdio.stdin.write(json.dumps(call_req) + "\n")
            gateway_proc_stdio.stdin.flush()
            resp = gateway_proc_stdio.stdout.readline()

            if "hello world" not in resp:
                raise AssertionError(f"STDIO FS Read failed: {resp}")
            print("STDIO FS Read: OK")

            # Tools Call (Write - reversible)
            call_req_write = {
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {
                    "name": "amf_execute",
                    "arguments": {
                        "capability": "machine.fs.write",
                        "action": "write_text",
                        "operation_id": "op-test-2",
                        "payload": {"path": "test2.txt", "text": "test mutation"},
                        "risk_class": "reversible_write",
                        "scope": f"fs:{str(tdp)}"
                    }
                }
            }
            gateway_proc_stdio.stdin.write(json.dumps(call_req_write) + "\n")
            gateway_proc_stdio.stdin.flush()
            resp = gateway_proc_stdio.stdout.readline()

            if "SUCCEEDED" not in resp:
                raise AssertionError(f"STDIO FS Write failed: {resp}")
            print("STDIO FS Write: OK")

            # Test replay
            gateway_proc_stdio.stdin.write(json.dumps(call_req_write) + "\n")
            gateway_proc_stdio.stdin.flush()
            resp = gateway_proc_stdio.stdout.readline()
            if "SUCCEEDED" not in resp:
                raise AssertionError(f"STDIO FS Write replay failed: {resp}")
            print("STDIO FS Write Replay: OK")

            # Restart gateway preserving durable receipts test
            gateway_proc_stdio.terminate()
            gateway_proc_stdio.wait()

            gateway_proc_stdio = subprocess.Popen(
                [sys.executable, str(gateway), "--amf-url", amf_url],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            gateway_proc_stdio.stdin.write(json.dumps(init_req) + "\n")
            gateway_proc_stdio.stdin.flush()
            gateway_proc_stdio.stdout.readline()

            gateway_proc_stdio.stdin.write(json.dumps(call_req_write) + "\n")
            gateway_proc_stdio.stdin.flush()
            resp = gateway_proc_stdio.stdout.readline()
            if "SUCCEEDED" not in resp:
                raise AssertionError(f"STDIO FS replay across restart failed: {resp}")
            print("STDIO FS Replay Across Restart: OK")

        finally:
            gateway_proc_stdio.terminate()
            gateway_proc_stdio.wait()

        # Test real MCP Streamable HTTP transport with the FastMCP client.
        gateway_proc_http = subprocess.Popen(
            [sys.executable, str(gateway), "--amf-url", amf_url, "--transport", "streamable-http", "--host", "127.0.0.1", "--port", "8055"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        async def probe_http():
            last_error = None
            for _ in range(30):
                try:
                    async with Client("http://127.0.0.1:8055/mcp", timeout=3) as c:
                        tools = await c.list_tools()
                        names = {t.name for t in tools}
                        if "amf_execute" not in names or "amf_health" not in names:
                            raise AssertionError(f"HTTP tool surface mismatch: {sorted(names)}")
                        result = await c.call_tool("amf_health", {})
                        return names, result
                except Exception as exc:
                    last_error = exc
                    await asyncio.sleep(0.2)
            raise AssertionError(f"Streamable HTTP MCP probe failed: {last_error}")

        try:
            names, _ = asyncio.run(probe_http())
            print("Streamable HTTP Init/Tools/Health: OK", sorted(names))
        finally:
            m0_proc.terminate()
            m0_proc.wait()
            gateway_proc_http.terminate()
            gateway_proc_http.wait()

run_test()
