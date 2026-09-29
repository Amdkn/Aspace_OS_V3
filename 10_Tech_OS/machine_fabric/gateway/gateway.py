#!/usr/bin/env python3
"""A'Space Sovereign DC Unified MCP Gateway.

One MCP surface over the already-proven Machine Fabric primitives:
- filesystem -> M0 durable mutation daemon
- process -> process broker
- browser -> M1 runtime presence/health until P3 production bridge

Transports:
- stdio
- loopback Streamable HTTP

The gateway does not bypass HostPolicy/operation_id/receipt semantics.
"""

from __future__ import annotations

import argparse
import sqlite3
import time
from datetime import datetime
import hashlib
import json
import logging
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from fastmcp import FastMCP

logger = logging.getLogger(__name__)

SURFACE_SCHEMA = "aspace.dc.capability-surface.v1"
PROCESS_VERSION = "1.0.0"
BROWSER_VERSION = "0.1.0"

PROCESS_CAPS = {
    "machine.process.start": {"actions": [{"name": "start", "risk_class": "consequential"}]},
    "machine.process.interact": {"actions": [{"name": "write_stdin", "risk_class": "consequential"}]},
    "machine.process.read": {"actions": [{"name": "read", "risk_class": "read"}]},
    "machine.process.stop": {"actions": [{"name": "stop", "risk_class": "consequential"}]},
}


class JsonHttpClient:
    def __init__(self, base_url: str | None):
        self.base_url = base_url.rstrip("/") if base_url else None

    @property
    def configured(self) -> bool:
        return bool(self.base_url)

    def request(self, method: str, path: str, data=None, timeout: float = 10.0):
        if not self.base_url:
            raise RuntimeError("backend not configured")
        url = f"{self.base_url}{path}"
        req = Request(url, method=method)
        if data is not None:
            body = json.dumps(data).encode("utf-8")
            req.add_header("Content-Type", "application/json; charset=utf-8")
            req.add_header("Content-Length", str(len(body)))
            req.data = body
        try:
            with urlopen(req, timeout=timeout) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {"error": f"HTTP_{exc.code}", "detail": raw}
            payload.setdefault("http_status", exc.code)
            return payload
        except URLError as exc:
            raise RuntimeError(f"connection failed: {exc.reason}") from exc

    def health(self):
        return self.request("GET", "/health")

    def capabilities(self):
        return self.request("GET", "/capabilities")

    def execute(self, op):
        return self.request("POST", "/operations", data=op)

    def get_receipt(self, operation_id):
        return self.request("GET", f"/receipts/{operation_id}")




import threading
import sqlite3
import time
from datetime import datetime

class UsageLedger:
    def __init__(self, db_path="gateway_ledger.sqlite3"):
        self.db_path = db_path
        self._lock = threading.Lock()
        self._init_db()

    def _init_db(self):
        with self._lock:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS tool_calls (
                        invocation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        operation_id TEXT,
                        tool_name TEXT NOT NULL,
                        capability TEXT,
                        timestamp TEXT NOT NULL,
                        latency_ms REAL NOT NULL,
                        state TEXT NOT NULL,
                        error TEXT,
                        is_replay INTEGER NOT NULL DEFAULT 0,
                        effect_new INTEGER NOT NULL DEFAULT 1,
                        receipt_ref TEXT
                    )
                ''')
                # Limit retention to last 10000 records
                conn.execute('''
                    CREATE TRIGGER IF NOT EXISTS rotate_tool_calls
                    AFTER INSERT ON tool_calls
                    BEGIN
                        DELETE FROM tool_calls WHERE invocation_id NOT IN (
                            SELECT invocation_id FROM tool_calls ORDER BY invocation_id DESC LIMIT 10000
                        );
                    END;
                ''')
                conn.commit()

    def record_call(self, tool_name, latency_ms, state, operation_id=None, capability=None, error=None, is_replay=False, effect_new=True, receipt_ref=None):
        with self._lock:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    '''INSERT INTO tool_calls (operation_id, tool_name, capability, timestamp, latency_ms, state, error, is_replay, effect_new, receipt_ref)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (operation_id, tool_name, capability, datetime.now().isoformat(), latency_ms, state, error, 1 if is_replay else 0, 1 if effect_new else 0, receipt_ref)
                )
                conn.commit()

    def has_operation(self, operation_id):
        if not operation_id:
            return False
        with self._lock:
            with sqlite3.connect(self.db_path) as conn:
                cur = conn.execute('SELECT 1 FROM tool_calls WHERE operation_id = ? LIMIT 1', (operation_id,))
                return cur.fetchone() is not None

    def get_tool_inventory(self):
        with self._lock:
            with sqlite3.connect(self.db_path) as conn:
                cur = conn.execute('SELECT tool_name, COUNT(*) as count, AVG(latency_ms) as avg_latency FROM tool_calls GROUP BY tool_name')
                return [{"tool": row[0], "count": row[1], "avg_latency": row[2]} for row in cur.fetchall()]

def _canonical_json(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True)


def _semantic_fingerprint(op):
    material = {
        "schema": op.get("schema"),
        "capability": op.get("capability"),
        "capability_version": op.get("capability_version"),
        "action": op.get("action"),
        "authority": op.get("authority"),
        "precondition": op.get("precondition"),
        "replay": op.get("replay"),
        "payload": op.get("payload") or {},
    }
    return hashlib.sha256(_canonical_json(material).encode("utf-8")).hexdigest()


def _safe_health(client: JsonHttpClient, backend: str):
    if not client.configured:
        return {
            "backend": backend,
            "aggregate": "UNAVAILABLE",
            "reason": "NOT_CONFIGURED",
            "capabilities": {},
        }
    try:
        value = client.health()
        value.setdefault("backend", backend)
        return value
    except Exception as exc:
        return {
            "backend": backend,
            "aggregate": "UNAVAILABLE",
            "reason": type(exc).__name__,
            "detail": str(exc),
            "capabilities": {},
        }


def _normalize_fs_capabilities(fs: JsonHttpClient):
    try:
        raw = fs.capabilities().get("capabilities", [])
    except Exception:
        raw = []
    return [
        {
            **cap,
            "backend": "filesystem",
            "availability": cap.get("health", "UNKNOWN"),
        }
        for cap in raw
    ]


def _normalize_process_capabilities(process_health):
    health_map = process_health.get("capabilities") or {}
    out = []
    for cap_id, contract in PROCESS_CAPS.items():
        out.append(
            {
                "schema": "aspace.machine.capability-manifest.v1",
                "capability_id": cap_id,
                "version": PROCESS_VERSION,
                "adapter": "amf.process.broker.v1",
                "requires_worker": False,
                "actions": contract["actions"],
                "health": health_map.get(cap_id, "UNAVAILABLE"),
                "availability": health_map.get(cap_id, "UNAVAILABLE"),
                "backend": "process",
            }
        )
    return out


def _normalize_browser_capabilities(browser_health):
    health_map = browser_health.get("capabilities") or {}
    out = []
    for cap_id in ("browser.tabs.read", "browser.dom.action", "browser.debugger.attach"):
        availability = health_map.get(cap_id, "UNAVAILABLE")
        out.append(
            {
                "schema": "aspace.machine.capability-manifest.v1",
                "capability_id": cap_id,
                "version": BROWSER_VERSION,
                "adapter": "amf.m1.chrome-native-messaging",
                "requires_worker": True,
                "actions": [],
                "health": availability,
                "availability": availability,
                "backend": "browser",
                "invocation": (
                    "P3_PRODUCTION_BRIDGE"
                    if cap_id in {"browser.tabs.read", "browser.dom.action"}
                    else "PRIVILEGED_SEPARATE_PATH"
                ),
            }
        )
    return out


def build_gateway(name, fs_url, process_url=None, browser_url=None, ledger_db="gateway_ledger.sqlite3"):
    ledger = UsageLedger(ledger_db)
    fs = JsonHttpClient(fs_url)
    process = JsonHttpClient(process_url)
    browser = JsonHttpClient(browser_url)
    mcp = FastMCP(name)

    def surface():
        fs_health = _safe_health(fs, "filesystem")
        process_health = _safe_health(process, "process")
        browser_health = _safe_health(browser, "browser")
        capabilities = (
            _normalize_fs_capabilities(fs)
            + _normalize_process_capabilities(process_health)
            + _normalize_browser_capabilities(browser_health)
        )
        return {
            "schema": SURFACE_SCHEMA,
            "backends": {
                "filesystem": fs_health,
                "process": process_health,
                "browser": browser_health,
            },
            "capabilities": capabilities,
        }



    @mcp.tool()
    def amf_health() -> str:
        """Returns normalized gateway/backend health without inventing liveness."""
        start_time = time.time()
        s = surface()
        states = [
            (s["backends"][key].get("aggregate") or "UNKNOWN")
            for key in ("filesystem", "process", "browser")
        ]

        if states[0] in {"ONLINE", "UP"} and states[1] in {"ONLINE", "UP"}:
            aggregate = "ONLINE" if states[2] in {"ONLINE", "UP"} else "DEGRADED"
        else:
            aggregate = "DEGRADED"

        result = {
            "schema": "aspace.dc.health.v1",
            "aggregate": aggregate,
            "backends": s["backends"],
            "tool_inventory": ledger.get_tool_inventory()
        }

        latency = (time.time() - start_time) * 1000
        ledger.record_call("amf_health", latency, "SUCCEEDED", effect_new=False)
        return json.dumps(result, indent=2)


    @mcp.tool()
    def amf_capabilities() -> str:
        """Lists the unified filesystem/process/browser capability surface."""
        start_time = time.time()
        s = surface()

        s["ledger"] = {
            "schema": "aspace.dc.ledger.v1",
            "retention": "bounded",
            "max_records": 10000,
            "storage": "local_sqlite",
            "quota_dependency": "zero"
        }

        s["projection_hooks"] = {
            "Amy": ["amf_execute"],
            "Graham": ["amf_health", "amf_capabilities", "amf_get_receipt"],
            "Yaz": ["amf_capabilities", "amf_health"]
        }

        latency = (time.time() - start_time) * 1000
        ledger.record_call("amf_capabilities", latency, "SUCCEEDED", effect_new=False)
        return json.dumps(s, indent=2)

    @mcp.tool()
    def amf_execute(
        capability: str,
        action: str,
        operation_id: str,
        payload: dict,
        risk_class: str = "consequential",
        scope: str = "default",
        precondition: dict | None = None,
    ) -> str:
        """Executes a typed filesystem/process operation with durable replay semantics."""
        start_time = time.time()

        # Check if this is a replay explicitly tracked in gateway
        is_replay = ledger.has_operation(operation_id)
        effect_new = not is_replay

        s = surface()
        cap = next((c for c in s["capabilities"] if c["capability_id"] == capability), None)
        if not cap:
            resp = {"state": "DENIED", "error": "UNKNOWN_CAPABILITY", "capability": capability}
            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_execute", latency, resp["state"], operation_id=operation_id, capability=capability, error=resp["error"], is_replay=is_replay, effect_new=False)
            return json.dumps(resp)

        if capability.startswith("browser."):
            resp = {
                "state": "UNAVAILABLE",
                "error": "BROWSER_EXECUTION_REQUIRES_P3_PRODUCTION_BRIDGE",
                "capability": capability,
                "availability": cap.get("availability"),
            }
            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_execute", latency, resp["state"], operation_id=operation_id, capability=capability, error=resp["error"], is_replay=is_replay, effect_new=False)
            return json.dumps(resp, indent=2)

        backend = fs if capability.startswith("machine.fs.") else process
        if not backend.configured:
            resp = {"state": "UNAVAILABLE", "error": "BACKEND_NOT_CONFIGURED", "capability": capability}
            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_execute", latency, resp["state"], operation_id=operation_id, capability=capability, error=resp["error"], is_replay=is_replay, effect_new=False)
            return json.dumps(resp, indent=2)

        op = {
            "schema": "aspace.machine.operation.v1",
            "operation_id": operation_id,
            "capability": capability,
            "capability_version": cap.get("version") or "0.1.0",
            "action": action,
            "authority": {
                "risk_class": risk_class,
                "scopes": [scope],
                "approval_ref": None,
            },
            "precondition": precondition or {},
            "replay": "return_receipt",
            "payload": payload,
        }
        op["fingerprint"] = _semantic_fingerprint(op)

        try:
            raw_result = backend.execute(op)
            state = raw_result.get("state", "UNKNOWN")
            error = raw_result.get("error")
            receipt_ref = raw_result.get("receipt")

            # If backend explicitly marks it as replay, it's not a new effect
            if raw_result.get("replay") == True:
                is_replay = True
                effect_new = False

            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_execute", latency, state, operation_id=operation_id, capability=capability, error=error, is_replay=is_replay, effect_new=effect_new, receipt_ref=receipt_ref)
            return json.dumps(raw_result, indent=2)
        except Exception as exc:
            state = "FAILED"
            error_type = type(exc).__name__
            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_execute", latency, state, operation_id=operation_id, capability=capability, error=error_type, is_replay=is_replay, effect_new=False)
            return json.dumps(
                {"state": state, "error": error_type, "detail": str(exc)},
                indent=2,
            )


    @mcp.tool()
    def amf_get_receipt(operation_id: str) -> str:
        """Retrieves a durable filesystem receipt."""
        start_time = time.time()
        try:
            result = fs.get_receipt(operation_id)
            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_get_receipt", latency, "SUCCEEDED", operation_id=operation_id, receipt_ref=operation_id, effect_new=False)
            return json.dumps(result, indent=2)
        except Exception as exc:
            latency = (time.time() - start_time) * 1000
            ledger.record_call("amf_get_receipt", latency, "FAILED", operation_id=operation_id, error=str(exc), effect_new=False)
            return json.dumps({"status": "error", "error": str(exc)}, indent=2)

    return mcp


def main():
    parser = argparse.ArgumentParser(description="A'Space Sovereign DC Unified MCP Gateway")
    parser.add_argument("--amf-url", required=True, help="M0 filesystem daemon URL")
    parser.add_argument("--process-url", help="Process broker URL")
    parser.add_argument("--browser-url", help="M1 browser/session daemon URL")
    parser.add_argument("--name", default="aspace-dc", help="MCP server name")
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="MCP transport",
    )
    parser.add_argument("--host", default="127.0.0.1", help="HTTP bind host")
    parser.add_argument("--port", type=int, default=8001, help="HTTP port")
    parser.add_argument("--ledger-db", default="gateway_ledger.sqlite3", help="SQLite DB path for usage ledger")
    args = parser.parse_args()

    mcp = build_gateway(args.name, args.amf_url, args.process_url, args.browser_url, args.ledger_db)
    if args.transport == "streamable-http":
        if args.host not in {"127.0.0.1", "localhost", "::1"}:
            raise SystemExit(
                "Refusing non-loopback bind without an explicit sovereign remote transport adapter."
            )
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
