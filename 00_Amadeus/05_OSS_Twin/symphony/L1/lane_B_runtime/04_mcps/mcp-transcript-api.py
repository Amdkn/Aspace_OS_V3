#!/usr/bin/env python3
"""
mcp-transcript-api.py — Symphony Lane B MCP proxy for transcriptapi.com.

A'Space OS V2 — Sovereign Twin Runtime.
Created 2026-06-21 by A0 mandate (YouTube transcript API for 12WY Q3 cycle).

This MCP server proxies a remote MCP server (transcriptapi.com/mcp) over HTTPS
into Claude Code's stdio. The remote server exposes 6 YouTube tools
(get_youtube_transcript, search_youtube, get_channel_latest_videos,
search_channel_videos, list_channel_videos, list_playlist_videos).

The previous config used `npx -y mcp-remote@latest` which is a generic OAuth
proxy that hangs on `transcriptapi.com` (D6 — the server is OAuth-protected
but accepts static Bearer tokens, and mcp-remote waits for OAuth metadata
discovery that completes but the static Bearer is never injected). This
proxy replaces it with a thin JSON-RPC forwarder: every stdio message goes
out as an HTTPS POST to /mcp with the Bearer in the Authorization header,
and the SSE response is decoded and written back to stdout.

D6 receipts 2026-06-21:
- transcriptapi.com/mcp POST initialize -> 200, serverInfo.name="Transcript API" v2.13.1
- transcriptapi.com/mcp POST tools/list -> 200, 6 tools listed
- mcp-remote proxy spawn -> blocks on "Discovering OAuth server configuration..."

Auth:
    TRANSCRIPT_API_KEY env var User scope. Never hardcode in code/.json/.md.
    Required scope: mcp:access (from WWW-Authenticate header probe).

Doctrine anchors:
- ADR-META-001 D1 (verify before assert), D2 (research-first), D7 (no crash)
- Test Key Pragma (env var User scope, never hardcoded in code)
- D4 append-only — this file is new, no other file modified
"""
from __future__ import annotations

import json
import logging
import os
import sys
from typing import Any

try:
    import httpx
except ImportError:
    print("[!] httpx not installed. Run: pip install httpx", file=sys.stderr)
    sys.exit(1)

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import TextContent, Tool
except ImportError:
    print("[!] MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

ENDPOINT = "https://transcriptapi.com/mcp"
BEARER = os.environ.get("TRANSCRIPT_API_KEY", "").strip()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [transcript-api-mcp] %(levelname)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("transcript-api-mcp")

# ── Tool registry (forwarded verbatim from remote server) ─────────────────────
# D1: tools/list proxied at boot via _remote_list_tools(); cached in _REMOTE_TOOLS.
# We expose the exact same names so Claude Code routes calls through the proxy
# and the proxy just forwards them HTTPS-side.

_REMOTE_TOOLS: list[dict[str, Any]] = []


async def _remote_post(payload: dict[str, Any]) -> dict[str, Any] | None:
    """Send a single JSON-RPC request to the upstream MCP server. Returns the
    decoded `result` field, or None on transport/HTTP error."""
    if not BEARER:
        log.error("TRANSCRIPT_API_KEY env var not set — cannot proxy")
        return None
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(ENDPOINT, json=payload, headers=headers)
    except httpx.HTTPError as e:
        log.error("Upstream POST failed: %s", e)
        return None
    if r.status_code != 200:
        log.error("Upstream HTTP %d: %s", r.status_code, r.text[:300])
        return None
    # Response is SSE-encoded JSON-RPC.
    body = r.text
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("data:"):
            data = line[5:].strip()
            if not data:
                continue
            try:
                msg = json.loads(data)
            except json.JSONDecodeError:
                continue
            if "result" in msg:
                return msg["result"]
            if "error" in msg:
                log.error("Upstream RPC error: %s", msg["error"])
                return None
    log.error("No result found in SSE response: %s", body[:300])
    return None


async def _remote_list_tools() -> list[dict[str, Any]]:
    """D1: probe upstream tools/list at boot so we know which tools to expose."""
    payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}
    result = await _remote_post(payload)
    if result is None:
        return []
    return result.get("tools", [])


async def _remote_call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Forward a tools/call to the upstream server, return the raw result."""
    payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments},
    }
    result = await _remote_post(payload)
    return result if result is not None else {"error": "upstream_unreachable"}


# ── MCP server wiring ─────────────────────────────────────────────────────────

server: Server = Server("transcript-api-mcp")


def _to_tool_spec(remote: dict[str, Any]) -> Tool:
    """Convert an upstream tool descriptor into the local MCP Tool type."""
    return Tool(
        name=remote["name"],
        description=remote.get("description", ""),
        inputSchema=remote.get("inputSchema", {"type": "object", "properties": {}}),
    )


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    if not _REMOTE_TOOLS:
        return []
    return [_to_tool_spec(t) for t in _REMOTE_TOOLS]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    result = await _remote_call_tool(name, arguments)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    return [TextContent(type="text", text=text)]


# ── Entry point ───────────────────────────────────────────────────────────────


async def main() -> None:
    if not BEARER:
        log.warning(
            "TRANSCRIPT_API_KEY not set. Server will start but every call "
            "returns upstream_unreachable. Set it via:\n"
            "  [Environment]::SetEnvironmentVariable('TRANSCRIPT_API_KEY', 'sk_...', 'User')"
        )
    log.info("Booting transcript-api MCP proxy → %s", ENDPOINT)
    discovered = await _remote_list_tools()
    if discovered:
        _REMOTE_TOOLS.extend(discovered)
        log.info("Discovered %d upstream tool(s): %s", len(discovered), [t["name"] for t in discovered])
    else:
        log.warning("0 upstream tools discovered — server will expose an empty list")
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
