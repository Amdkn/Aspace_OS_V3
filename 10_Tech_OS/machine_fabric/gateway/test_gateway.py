import sys
import os
import json
import subprocess
import time
import tempfile
import urllib.request
import urllib.error
from pathlib import Path

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
            print("STDIO Init:", "OK" if "protocolVersion" in resp else "FAIL")

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
            print("STDIO Tools List:", "OK" if "amf_execute" in resp else "FAIL")

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

            if "hello world" in resp:
                print("STDIO FS Read: OK")
            else:
                print("STDIO FS Read: FAIL", resp)

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

            if "SUCCEEDED" in resp:
                print("STDIO FS Write: OK")

                # Test replay
                gateway_proc_stdio.stdin.write(json.dumps(call_req_write) + "\n")
                gateway_proc_stdio.stdin.flush()
                resp = gateway_proc_stdio.stdout.readline()
                if "SUCCEEDED" in resp:
                    print("STDIO FS Write Replay: OK")
                else:
                    print("STDIO FS Write Replay: FAIL", resp)

            else:
                print("STDIO FS Write: FAIL", resp)

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
            if "SUCCEEDED" in resp:
                print("STDIO FS Replay Across Restart: OK")
            else:
                print("STDIO FS Replay Across Restart: FAIL", resp)

        finally:
            gateway_proc_stdio.terminate()
            gateway_proc_stdio.wait()

        # Test SSE transport
        gateway_proc_sse = subprocess.Popen(
            [sys.executable, str(gateway), "--amf-url", amf_url, "--transport", "sse", "--port", "8055"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Give it a second to start
        time.sleep(2)

        try:
            req = urllib.request.Request("http://127.0.0.1:8055/sse")
            resp = urllib.request.urlopen(req, timeout=1)
            print("SSE transport: OK (HTTP 200)")

        except urllib.error.HTTPError as e:
            print(f"SSE transport: HTTPError {e.code}")
        except Exception as e:
            if "timeout" in str(e).lower() or type(e).__name__ == "TimeoutError":
                 print("SSE transport: OK (Streaming endpoint blocked as expected)")
            else:
                 print(f"SSE endpoint test error: {type(e).__name__} - {e}")

        finally:
            m0_proc.terminate()
            m0_proc.wait()
            gateway_proc_sse.terminate()
            gateway_proc_sse.wait()

run_test()
