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
import hashlib
import json
import logging
import sqlite3
import time
import datetime
import os
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


def init_ledger(db_path: str):
    """Initializes the usage ledger SQLite database."""
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usage_ledger (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                operation_id TEXT,
                tool TEXT NOT NULL,
                capability TEXT,
                action TEXT,
                is_replay INTEGER NOT NULL DEFAULT 0,
                state TEXT NOT NULL,
                latency_ms INTEGER NOT NULL,
                error_detail TEXT,
                receipt_ref TEXT
            )
        """)
        conn.commit()


def log_usage(
    db_path: str,
    tool: str,
    state: str,
    latency_ms: int,
    operation_id: str | None = None,
    capability: str | None = None,
    action: str | None = None,
    is_replay: bool = False,
    error_detail: str | None = None,
    receipt_ref: str | None = None,
):
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO usage_ledger (
                timestamp, operation_id, tool, capability, action,
                is_replay, state, latency_ms, error_detail, receipt_ref
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.datetime.now(datetime.timezone.utc).isoformat(),
                operation_id,
                tool,
                capability,
                action,
                1 if is_replay else 0,
                state,
                latency_ms,
                error_detail,
                receipt_ref,
            ),
        )
        conn.commit()


def build_gateway(name, fs_url, process_url=None, browser_url=None, usage_db="gateway_usage.db"):
    init_ledger(usage_db)
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
        start_time = time.monotonic()
        try:
            s = surface()
            states = [
                (s["backends"][key].get("aggregate") or "UNKNOWN")
                for key in ("filesystem", "process", "browser")
            ]
            if states[0] in {"ONLINE", "UP"} and states[1] in {"ONLINE", "UP"}:
                aggregate = "ONLINE" if states[2] in {"ONLINE", "UP"} else "DEGRADED"
            else:
                aggregate = "DEGRADED"
            resp = {
                "schema": "aspace.dc.health.v1",
                "aggregate": aggregate,
                "backends": s["backends"],
            }
            log_usage(usage_db, "amf_health", "SUCCEEDED", int((time.monotonic() - start_time)*1000))
            return json.dumps(resp, indent=2)
        except Exception as exc:
            log_usage(usage_db, "amf_health", "FAILED", int((time.monotonic() - start_time)*1000), error_detail=str(exc))
            raise

    @mcp.tool()
    def amf_capabilities() -> str:
        """Lists the unified filesystem/process/browser capability surface."""
        start_time = time.monotonic()
        try:
            resp = surface()
            log_usage(usage_db, "amf_capabilities", "SUCCEEDED", int((time.monotonic() - start_time)*1000))
            return json.dumps(resp, indent=2)
        except Exception as exc:
            log_usage(usage_db, "amf_capabilities", "FAILED", int((time.monotonic() - start_time)*1000), error_detail=str(exc))
            raise

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
        """Executes a typed filesystem/process operation with durable replay semantics.

        Browser invocation is intentionally refused until P3 exposes the production
        Native Messaging command path; browser availability is still reported truthfully.
        """
        start_time = time.monotonic()
        try:
            s = surface()
            cap = next((c for c in s["capabilities"] if c["capability_id"] == capability), None)
            if not cap:
                resp = {"state": "DENIED", "error": "UNKNOWN_CAPABILITY", "capability": capability}
                log_usage(usage_db, "amf_execute", "DENIED", int((time.monotonic() - start_time)*1000), operation_id, capability, action, False, "UNKNOWN_CAPABILITY")
                return json.dumps(resp)

            if capability.startswith("browser."):
                resp = {
                    "state": "UNAVAILABLE",
                    "error": "BROWSER_EXECUTION_REQUIRES_P3_PRODUCTION_BRIDGE",
                    "capability": capability,
                    "availability": cap.get("availability"),
                }
                log_usage(usage_db, "amf_execute", "UNAVAILABLE", int((time.monotonic() - start_time)*1000), operation_id, capability, action, False, "BROWSER_EXECUTION_REQUIRES_P3_PRODUCTION_BRIDGE")
                return json.dumps(resp, indent=2)

            backend = fs if capability.startswith("machine.fs.") else process
            if not backend.configured:
                resp = {"state": "UNAVAILABLE", "error": "BACKEND_NOT_CONFIGURED", "capability": capability}
                log_usage(usage_db, "amf_execute", "UNAVAILABLE", int((time.monotonic() - start_time)*1000), operation_id, capability, action, False, "BACKEND_NOT_CONFIGURED")
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
                receipt = backend.execute(op)
                is_replay = bool(receipt.get("replayed")) or bool(receipt.get("reconciled_after_restart"))
                state = receipt.get("state", "UNKNOWN")
                error_detail = None
                if state in ("FAILED", "DENIED", "DLQ", "UNKNOWN"):
                    evidence = receipt.get("evidence")
                    error_detail = str(evidence) if evidence else None
                log_usage(usage_db, "amf_execute", state, int((time.monotonic() - start_time)*1000), operation_id, capability, action, is_replay, error_detail, receipt.get("operation_id"))
                return json.dumps(receipt, indent=2)
            except Exception as exc:
                resp = {"state": "FAILED", "error": type(exc).__name__, "detail": str(exc)}
                log_usage(usage_db, "amf_execute", "FAILED", int((time.monotonic() - start_time)*1000), operation_id, capability, action, False, str(exc))
                return json.dumps(resp, indent=2)
        except Exception as outer_exc:
            log_usage(usage_db, "amf_execute", "FAILED", int((time.monotonic() - start_time)*1000), operation_id, capability, action, False, str(outer_exc))
            return json.dumps({"state": "FAILED", "error": type(outer_exc).__name__, "detail": str(outer_exc)}, indent=2)

    @mcp.tool()
    def amf_get_receipt(operation_id: str) -> str:
        """Retrieves a durable filesystem receipt.

        Process receipts are returned by process operations/replay; a process receipt
        lookup endpoint is intentionally not fabricated here.
        """
        start_time = time.monotonic()
        try:
            resp = fs.get_receipt(operation_id)
            log_usage(usage_db, "amf_get_receipt", "SUCCEEDED", int((time.monotonic() - start_time)*1000), operation_id=operation_id)
            return json.dumps(resp, indent=2)
        except Exception as exc:
            log_usage(usage_db, "amf_get_receipt", "FAILED", int((time.monotonic() - start_time)*1000), operation_id=operation_id, error_detail=str(exc))
            return json.dumps({"status": "error", "error": str(exc)}, indent=2)

    @mcp.tool()
    def amf_usage(limit: int = 100) -> str:
        """Retrieves the vendor-independent local usage ledger for projection hooks."""
        start_time = time.monotonic()
        try:
            with sqlite3.connect(usage_db) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute(
                    "SELECT * FROM usage_ledger ORDER BY timestamp DESC LIMIT ?",
                    (limit,)
                ).fetchall()
            resp = {"schema": "aspace.dc.usage-ledger.v1", "records": [dict(r) for r in rows]}
            log_usage(usage_db, "amf_usage", "SUCCEEDED", int((time.monotonic() - start_time)*1000))
            return json.dumps(resp, indent=2)
        except Exception as exc:
            log_usage(usage_db, "amf_usage", "FAILED", int((time.monotonic() - start_time)*1000), error_detail=str(exc))
            raise

    return mcp


def main():
    parser = argparse.ArgumentParser(description="A'Space Sovereign DC Unified MCP Gateway")
    parser.add_argument("--amf-url", required=True, help="M0 filesystem daemon URL")
    parser.add_argument("--process-url", help="Process broker URL")
    parser.add_argument("--browser-url", help="M1 browser/session daemon URL")
    parser.add_argument("--name", default="aspace-dc", help="MCP server name")
    parser.add_argument("--usage-db", default="gateway_usage.db", help="Path to SQLite usage ledger")
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="MCP transport",
    )
    parser.add_argument("--host", default="127.0.0.1", help="HTTP bind host")
    parser.add_argument("--port", type=int, default=8001, help="HTTP port")
    args = parser.parse_args()

    mcp = build_gateway(args.name, args.amf_url, args.process_url, args.browser_url, usage_db=args.usage_db)
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
