#!/usr/bin/env python3
"""Unified MCP Gateway over A'Space Machine Fabric.

Exposes the Machine Fabric primitives via a real MCP surface using FastMCP.
Includes both stdio (default) and loopback Streamable HTTP (SSE) transports.
Routing requires AMF HostPolicy semantics (operation_id/receipt).
"""

import argparse
import sys
import json
import logging
import asyncio
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import hashlib

from fastmcp import FastMCP

logger = logging.getLogger(__name__)

class AMFClient:
    def __init__(self, amf_url):
        self.amf_url = amf_url

    def request(self, method, path, data=None):
        url = f"{self.amf_url}{path}"
        req = Request(url, method=method)
        if data is not None:
            body = json.dumps(data).encode("utf-8")
            req.add_header("Content-Type", "application/json; charset=utf-8")
            req.add_header("Content-Length", str(len(body)))
            req.data = body
        try:
            with urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as e:
            body = e.read().decode("utf-8")
            try:
                err_data = json.loads(body)
                if "state" in err_data and err_data["state"] == "DENIED":
                    return err_data
                raise Exception(f"AMF Error: {err_data.get('error', 'unknown')} - {err_data.get('detail', 'none')}")
            except json.JSONDecodeError:
                raise Exception(f"HTTP Error {e.code}: {body}")
        except URLError as e:
            raise Exception(f"Connection failed: {e.reason}")

    def health(self):
        return self.request("GET", "/health")

    def capabilities(self):
        return self.request("GET", "/capabilities")

    def execute(self, op):
        return self.request("POST", "/operations", data=op)

    def get_receipt(self, op_id):
        return self.request("GET", f"/receipts/{op_id}")


def main():
    parser = argparse.ArgumentParser(description="A'Space Machine Fabric Unified MCP Gateway")
    parser.add_argument("--amf-url", required=True, help="URL of AMF daemon (e.g. http://127.0.0.1:8000)")
    parser.add_argument("--name", default="amf-gateway", help="Name of MCP server")
    parser.add_argument("--transport", default="stdio", choices=["stdio", "sse"], help="MCP transport to use (default: stdio)")
    parser.add_argument("--port", type=int, default=8001, help="Port to use for SSE transport (default: 8001)")
    args = parser.parse_args()

    client = AMFClient(args.amf_url)

    mcp = FastMCP(args.name)

    @mcp.tool()
    def amf_health() -> str:
        """Returns the aggregate health of the A'Space Machine Fabric."""
        try:
            h = client.health()
            return json.dumps(h, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": str(e)})

    @mcp.tool()
    def amf_capabilities() -> str:
        """Lists available capabilities from the AMF daemon."""
        try:
            c = client.capabilities()
            return json.dumps(c, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": str(e)})

    @mcp.tool()
    def amf_execute(capability: str, action: str, operation_id: str, payload: dict, risk_class: str = "consequential", scope: str = "default", precondition: dict = None) -> str:
        """Executes a typed operation via the AMF daemon with strict policy and durable receipt.

        Args:
            capability: The capability to use, e.g., 'machine.fs.read' or 'machine.process.start'
            action: The specific action to execute.
            operation_id: Unique idempotent operation ID across retries.
            payload: Arguments/payload for the action.
            risk_class: Risk level, e.g., 'read', 'reversible_write', 'consequential'.
            scope: Access scope.
            precondition: Optional conditions for the action.
        """
        op = {
            "schema": "aspace.machine.operation.v1",
            "operation_id": operation_id,
            "capability": capability,
        }

        try:
            caps = client.capabilities()["capabilities"]
            cap_ver = next((c["version"] for c in caps if c["capability_id"] == capability), "0.1.0")

            op["capability_version"] = cap_ver
            op["action"] = action
            op["authority"] = {
                "risk_class": risk_class,
                "scopes": [scope],
                "approval_ref": None
            }
            op["precondition"] = precondition or {}
            op["replay"] = "return_receipt"
            op["payload"] = payload

            def canonical_json(val):
                return json.dumps(val, separators=(",", ":"), sort_keys=True)

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

            op["fingerprint"] = hashlib.sha256(canonical_json(material).encode("utf-8")).hexdigest()

            result = client.execute(op)
            return json.dumps(result, indent=2)

        except Exception as e:
            return json.dumps({"status": "error", "error": str(e)})

    @mcp.tool()
    def amf_get_receipt(operation_id: str) -> str:
        """Retrieves a durable receipt for a previous operation."""
        try:
            r = client.get_receipt(operation_id)
            return json.dumps(r, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": str(e)})

    if args.transport == "sse":
        mcp.run(transport="sse", port=args.port)
    else:
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
