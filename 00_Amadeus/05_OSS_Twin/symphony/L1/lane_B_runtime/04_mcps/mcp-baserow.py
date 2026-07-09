#!/usr/bin/env python3
"""
mcp-baserow.py — Symphony Lane B MCP server for Baserow (Life Wheel / 12WY tables).

A'Space OS V2 — Sovereign Twin Runtime.
Created 2026-06-15 by A0 mandate (Symphony Phase 2).
Re-written 2026-06-15 to proxy the official Baserow remote MCP server over SSE
(was: stub-mode). See ADR-META-001 D1 / D2 / D4 / D6.

This MCP server exposes Baserow 12 Week Year (12WY) operations to the Symphony
agent runtime. Baserow hosts the canonical 12WY tables: Quarter Intent, The 12 Rocks,
and The Warp Core (USS SNW / Curie, A2 manager).

Usage:
    "C:/Python314/python.exe" mcp-baserow.py

Auth (Test Key Pragma 2026-06-15 — never hardcoded):
    Set BASEROW_MCP_URL env var (User scope) to the official Baserow SSE endpoint,
    e.g. https://api.baserow.io/mcp/<token>/sse
    The 4 base table IDs may be overridden with BASEROW_TABLE_* env vars.

Doctrine anchors:
- ADR-META-001 D1 (verify before assert), D2 (research-first), D4 (append-only),
  D6 (root-cause: SDK upgrade from stub → real client), D7 (cost-of-escalation)
- Symphony Adapter — Baserow (L1 Shadow Life OS), 2026-05-14
- SDD-008 §2 Pilier 2 (Baserow = 12 Week Year)

Architecture:
    stdio MCP server (this file)
        → on first call_tool, opens a long-lived SSE client
        → forwards list_tools + call_tool to the official Baserow remote MCP
        → on disconnect / error, falls back to stub mode (D7)
"""
from __future__ import annotations

import asyncio
import os
import sys
from contextlib import asynccontextmanager
from typing import Any

try:
    from mcp.client.session import ClientSession
    from mcp.client.sse import sse_client
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import TextContent, Tool
except ImportError:
    print("[!] MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# --- Env var contract (Test Key Pragma — never hardcoded) -------------------------
API_KEY: str = os.environ.get("BASEROW_API_KEY", "")
BASE_URL: str = os.environ.get("BASEROW_BASE_URL", "https://api.baserow.io/api")
DATABASE_ID: str = os.environ.get("BASEROW_DATABASE_ID", "284361")
TABLE_QUARTER_INTENT: str = os.environ.get("BASEROW_TABLE_QUARTER_INTENT", "955428")
TABLE_TWELVE_ROCKS: str = os.environ.get("BASEROW_TABLE_TWELVE_ROCKS", "955426")
TABLE_WARP_CORE: str = os.environ.get("BASEROW_TABLE_WARP_CORE", "955429")
# Primary signal for SSE mode: if set, proxy the remote MCP at this URL.
MCP_URL: str = os.environ.get("BASEROW_MCP_URL", "").strip()

server = Server("baserow-mcp")

# Life Wheel domains (LD01-LD08) for cross-reference with 12WY Rocks
LIFE_WHEEL_DOMAINS: list[str] = [
    "LD01_Business",
    "LD02_Finance",
    "LD03_Health",
    "LD04_Cognition",
    "LD05_Social",
    "LD06_Family",
    "LD07_Creativity",
    "LD08_Impact",
]


# --- Stub helpers (fallback when no MCP_URL or SSE unreachable) -------------------
def _stub_tables() -> list[dict[str, Any]]:
    return [
        {
            "id": TABLE_QUARTER_INTENT,
            "name": "Quarter Intent",
            "database_id": DATABASE_ID,
            "purpose": "Quarterly vision per A'Space layer (L0/L1/L2)",
        },
        {
            "id": TABLE_TWELVE_ROCKS,
            "name": "The 12 Rocks",
            "database_id": DATABASE_ID,
            "purpose": "Quarterly concrete objectives (12 max)",
        },
        {
            "id": TABLE_WARP_CORE,
            "name": "The Warp Core",
            "database_id": DATABASE_ID,
            "purpose": "Weekly decomposition W1-W12 (50/30/20 L2/L1/L0)",
        },
    ]


def _stub_life_wheel() -> dict[str, Any]:
    return {
        "cycle": "H1-C2",
        "domains": {domain: {"score": 0, "status": "Not Started"} for domain in LIFE_WHEEL_DOMAINS},
        "average": 0,
    }


def _stub_scorecard() -> dict[str, Any]:
    return {
        "cycle": "H1-C2",
        "week": "W1",
        "rocks_total": 12,
        "rocks_done": 0,
        "rocks_in_progress": 0,
        "rocks_blocked": 0,
        "completion_pct": 0,
    }


def _stub_error(tool_name: str, exc: BaseException) -> list[TextContent]:
    return [
        TextContent(
            type="text",
            text=(
                f"[!] {tool_name} SSE proxy failed: {type(exc).__name__}: {exc}. "
                f"Falling back to stub. Set BASEROW_MCP_URL or fix network."
            ),
        )
    ]


# --- SSE proxy to the official Baserow remote MCP --------------------------------
@asynccontextmanager
async def _remote_session() -> Any:
    """Yield a live ClientSession to the remote Baserow MCP, or None on failure.

    Uses D2 — verify before assert: the initialize() call is awaited and any
    exception is caught and logged to stderr; the caller falls back to stub.
    """
    if not MCP_URL:
        yield None
        return
    try:
        # No headers — auth is in the URL path (D1 receipt from session 2026-06-15).
        async with sse_client(MCP_URL, timeout=10.0, sse_read_timeout=60.0) as (
            read_stream,
            write_stream,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                yield session
    except Exception as exc:  # noqa: BLE001 — D7: never crash host agent
        print(f"[!] Baserow SSE proxy unavailable: {exc}", file=sys.stderr)
        yield None


def _flatten_remote_content(result: Any) -> list[TextContent]:
    """Convert a remote CallToolResult to local TextContent list.

    D1: serialize the structured content / text content into a single readable
    block, preserving the contract that local callers get TextContent only.
    """
    out: list[TextContent] = []
    content = getattr(result, "content", None) or []
    for item in content:
        text = getattr(item, "text", None)
        if text is not None:
            out.append(TextContent(type="text", text=text))
        else:
            # Image / Audio / ResourceLink / EmbeddedResource: stringify the repr
            out.append(TextContent(type="text", text=f"[remote-content] {item!r}"))
    structured = getattr(result, "structuredContent", None)
    if structured:
        out.append(TextContent(type="text", text=f"[structured] {structured}"))
    is_error = getattr(result, "isError", False)
    if is_error:
        # Prefix all previous items with an error marker
        out = [TextContent(type="text", text="[REMOTE ERROR]")] + out
    return out or [TextContent(type="text", text="(empty remote result)")]


# --- Stable local tool contract (deterministic Symphony wiring) ------------------
_LOCAL_TOOL_NAMES: frozenset[str] = frozenset(
    {
        "baserow_list_tables",
        "baserow_get_life_wheel_score",
        "baserow_get_12wy_scorecard",
        "baserow_log_metric",
    }
)


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="baserow_list_tables",
            description="List the 3 canonical 12WY tables in the configured Baserow database.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="baserow_get_life_wheel_score",
            description="Compute current Life Wheel score per LD01-LD08 domain for the active cycle.",
            inputSchema={
                "type": "object",
                "properties": {
                    "cycle": {
                        "type": "string",
                        "description": "Cycle tag (e.g. H1-C2). Default: latest active.",
                    }
                },
            },
        ),
        Tool(
            name="baserow_get_12wy_scorecard",
            description="Fetch 12 Week Year scorecard (rocks done, in progress, blocked, completion %).",
            inputSchema={
                "type": "object",
                "properties": {
                    "week": {
                        "type": "string",
                        "description": "Week tag (e.g. W3). Default: current Warp Core week.",
                    }
                },
            },
        ),
        Tool(
            name="baserow_log_metric",
            description="Log a metric row into a Baserow table (proxies remote MCP if BASEROW_MCP_URL set, else stub).",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_id": {
                        "type": "string",
                        "description": "Target table ID (955426/955428/955429).",
                    },
                    "values": {
                        "type": "object",
                        "description": "Field name -> value mapping (user_field_names=true).",
                    },
                },
                "required": ["table_id", "values"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    # Path A: try to forward to the remote Baserow MCP via SSE.
    if name in _LOCAL_TOOL_NAMES and MCP_URL:
        try:
            async with _remote_session() as session:
                if session is not None:
                    result = await session.call_tool(name, arguments or {})
                    return _flatten_remote_content(result)
        except Exception as exc:  # noqa: BLE001 — D7
            return _stub_error(name, exc)

    # Path B: stub fallback (no MCP_URL or SSE failed).
    if name == "baserow_list_tables":
        return [TextContent(type="text", text=f"Tables: {_stub_tables()}")]

    if name == "baserow_get_life_wheel_score":
        cycle = arguments.get("cycle", "H1-C2")
        wheel = _stub_life_wheel()
        wheel["cycle"] = str(cycle)
        return [TextContent(type="text", text=f"Life Wheel score: {wheel}")]

    if name == "baserow_get_12wy_scorecard":
        week = arguments.get("week", "W1")
        card = _stub_scorecard()
        card["week"] = str(week)
        return [TextContent(type="text", text=f"12WY scorecard: {card}")]

    if name == "baserow_log_metric":
        table_id = arguments.get("table_id", TABLE_TWELVE_ROCKS)
        values = arguments.get("values", {})
        if not API_KEY and not MCP_URL:
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[!] BASEROW_API_KEY and BASEROW_MCP_URL both unset — stub log. "
                        f"table_id={table_id} values={values}"
                    ),
                )
            ]
        return [
            TextContent(
                type="text",
                text=f"[+] Metric logged (stub): table_id={table_id} values={values}",
            )
        ]

    raise ValueError(f"Unknown tool: {name}")


async def main() -> None:
    if MCP_URL:
        print(
            f"[+] Baserow MCP server starting (Symphony Lane B / 12WY Warp Core) "
            f"via SSE proxy -> {MCP_URL[:60]}...",
            file=sys.stderr,
        )
    else:
        print(
            "[!] BASEROW_MCP_URL not set — Baserow MCP server starting in STUB mode "
            "(Symphony Lane B / 12WY Warp Core).",
            file=sys.stderr,
        )
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
