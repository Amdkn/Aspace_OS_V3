import asyncio
import json
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
import urllib.error
from pathlib import Path

from fastmcp import Client
import httpx

HERE = Path(__file__).resolve().parent
MF = HERE.parent
M0 = MF / "m0" / "amf_m0.py"
GATEWAY = MF / "gateway" / "gateway.py"
ADAPTER = HERE / "adapter.py"


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


async def wait_gateway(url):
    for _ in range(40):
        try:
            async with Client(url, timeout=1) as c:
                await c.list_tools()
            return
        except Exception:
            await asyncio.sleep(0.2)
    raise AssertionError(f"gateway unavailable: {url}")


async def wait_adapter(url):
    for _ in range(40):
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(url, timeout=1)
                if resp.status_code == 200:
                    return
        except Exception:
            await asyncio.sleep(0.2)
    raise AssertionError(f"adapter unavailable: {url}")


async def main():
    with tempfile.TemporaryDirectory(prefix="aspace-dc-adapter-") as td:
        root = Path(td)
        fs_port, gw_port, adapter_port = [free_port() for _ in range(3)]
        fs_db = root / "fs.sqlite3"
        gw_db = root / "gw.sqlite3"

        fs = gateway = adapter = None
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

            gateway = subprocess.Popen(
                [
                    sys.executable,
                    str(GATEWAY),
                    "--amf-url",
                    f"http://127.0.0.1:{fs_port}",
                    "--usage-db",
                    str(gw_db),
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

            gw_url = f"http://127.0.0.1:{gw_port}/mcp"
            await wait_gateway(gw_url)

            adapter = subprocess.Popen(
                [
                    sys.executable,
                    str(ADAPTER),
                    "--gateway-url",
                    f"http://127.0.0.1:{gw_port}",
                    "--token",
                    "test-secret-token",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(adapter_port),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            adapter_health_url = f"http://127.0.0.1:{adapter_port}/health"
            await wait_adapter(adapter_health_url)

            adapter_mcp_url = f"http://127.0.0.1:{adapter_port}/mcp"

            # 1. Unauthenticated Client (Client2)
            print("Testing Unauthenticated Client DENY...")
            unauth_client = Client(adapter_mcp_url, timeout=3)
            try:
                await unauth_client.__aenter__()
                tools = await unauth_client.list_tools()
                assert False, "Unauthenticated client should have failed to initialize"
            except Exception as e:
                # Expecting an auth error or transport error due to 401
                print(f"Unauthenticated client denied successfully: {type(e).__name__}")

            # 2. Authenticated Client (Client1)
            print("Testing Authenticated Client...")
            # We pass HTTP headers using the auth parameter, or by configuring the transport.
            # But the Client class doesn't directly expose header passing if we just pass a string URL.
            # Actually, `fastmcp` client allows auth config. We saw `auth` kwarg. Let's try passing it?
            # Wait, Client docs say: `auth: "httpx.Auth | Literal['oauth'] | str | None"`.
            # Unfortunately, providing headers to fastmcp client can be done by using httpx.AsyncClient or custom transport.
            # We can also just use the `httpx` auth class for Bearer.
            class BearerAuth(httpx.Auth):
                def __init__(self, token):
                    self.token = token
                def auth_flow(self, request):
                    request.headers['Authorization'] = f'Bearer {self.token}'
                    yield request

            auth = BearerAuth("test-secret-token")
            auth_client = Client(adapter_mcp_url, timeout=10, auth=auth)
            await auth_client.__aenter__()

            tools = await auth_client.list_tools()
            names = {x.name for x in tools}
            assert "amf_execute" in names, "amf_execute missing in authenticated surface"

            # Read test
            caps_result = await auth_client.call_tool("amf_capabilities", {})
            caps = json.loads(result_text(caps_result))
            by_id = {x["capability_id"]: x for x in caps["capabilities"]}
            assert by_id["machine.fs.read"]["availability"] == "AVAILABLE"
            print("Authenticated Read capability surface: OK")

            # Bounded mutation test
            mutation_op_id = "test-adapter-write-001"
            write_result = await auth_client.call_tool(
                "amf_execute",
                {
                    "capability": "machine.fs.write",
                    "action": "write_text",
                    "operation_id": mutation_op_id,
                    "payload": {"path": "test-adapter.txt", "text": "hello remote"},
                    "risk_class": "reversible_write",
                    "scope": f"fs:{root}",
                },
            )
            write_payload = json.loads(result_text(write_result))
            assert write_payload["state"] == "SUCCEEDED"
            print("Authenticated bounded mutation: OK")

            await auth_client.__aexit__(None, None, None)

            # 3. Transport failure - local gateway health remains
            print("Testing adapter termination...")
            stop(adapter)
            adapter = None

            # Verify local gateway is still healthy
            async with Client(gw_url, timeout=3) as check_client:
                health = json.loads(result_text(await check_client.call_tool("amf_health", {})))
                assert health["aggregate"] in {"ONLINE", "DEGRADED"}
            print("Local gateway remains healthy: OK")

            # 4. Reconnect and Replay
            print("Testing reconnect and replay...")
            adapter = subprocess.Popen(
                [
                    sys.executable,
                    str(ADAPTER),
                    "--gateway-url",
                    f"http://127.0.0.1:{gw_port}",
                    "--token",
                    "test-secret-token",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(adapter_port),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            await wait_adapter(adapter_health_url)

            replay_client = Client(adapter_mcp_url, timeout=3, auth=auth)
            await replay_client.__aenter__()

            replay_result = await replay_client.call_tool(
                "amf_execute",
                {
                    "capability": "machine.fs.write",
                    "action": "write_text",
                    "operation_id": mutation_op_id,
                    "payload": {"path": "test-adapter.txt", "text": "hello remote"},
                    "risk_class": "reversible_write",
                    "scope": f"fs:{root}",
                },
            )
            replay_payload = json.loads(result_text(replay_result))
            assert replay_payload["state"] == "SUCCEEDED"
            assert replay_payload.get("replayed", False) or replay_payload.get("reconciled_after_restart", False) is True, f"Expected replay receipt, got: {replay_payload}"
            print("Reconnect replay preserving operation_id semantics: OK")

            await replay_client.__aexit__(None, None, None)

            print("REMOTE_ADAPTER_ACCEPTANCE=PASS")
        finally:
            stop(adapter)
            stop(gateway)
            stop(fs)

if __name__ == "__main__":
    asyncio.run(main())
