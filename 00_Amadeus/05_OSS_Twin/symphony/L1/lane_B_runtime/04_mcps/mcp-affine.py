#!/usr/bin/env python3
"""
mcp-affine.py — Symphony Lane B MCP server for Affine (DEAL workspace).

A'Space OS V2 — Sovereign Twin Runtime.
Created 2026-06-15 by A0 mandate (Symphony Phase 2).
Updated 2026-06-15 by A3 cerritos-boimler: replace stub-data calls with real
streamable-http proxy to Affine's hosted MCP endpoint.

This MCP server exposes Affine DEAL (Define/Eliminate/Automate/Liberate) workspace
operations to the Symphony agent runtime. Affine is the document-first canvas with
infinite Edgeless mode for DEAL Blueprints (Holo Janeway / USS Protostar).

Architecture (2026-06-15):
    stdio MCP server (this file)
        -> streamablehttp_client(MCP_URL, headers={"Authorization": Bearer})
        -> ClientSession.initialize() + .list_tools()
        -> forwards list_tools + call_tool to the Affine hosted MCP server

    Fallback: if AFFINE_API_KEY is unset OR the streamable-http connect fails,
    the server stays alive in local stub mode (preserves the DEAL_DRAFTS_PATH
    file fallback and prior behavior). The Symphony host agent never crashes
    on transient network blips (D7 — cost of escalation > cost of stub).

Usage:
    "C:/Python314/python.exe" mcp-affine.py

Auth:
    Set AFFINE_API_KEY env var (User scope) before running.
    For self-hosted instances, set AFFINE_BASE_URL accordingly.
    The full MCP endpoint is computed as:
        {BASE_URL}/workspaces/{WORKSPACE_ID}/mcp
    e.g. https://app.affine.pro/api/workspaces/<UUID>/mcp

Doctrine anchors:
- ADR-META-001 D1 (verify before assert), D2 (research-first), D7 (no host crash)
- Symphony Adapter — Affine (L1 Shadow Life OS), 2026-05-14
- SDD-008 §2 Pilier 4 (Affine = DEAL)
"""
from __future__ import annotations

import asyncio
import logging
import os
import sys
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, AsyncIterator

try:
    from mcp.client.session import ClientSession
    from mcp.client.streamable_http import streamablehttp_client
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import TextContent, Tool
except ImportError:
    print("[!] MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config (Test Key Pragma 2026-06-15 — never hardcoded in .md/.json/.git)
# ---------------------------------------------------------------------------
API_KEY: str = os.environ.get("AFFINE_API_KEY", "")
# BASE_URL points at the API root. The MCP endpoint is derived below.
BASE_URL: str = os.environ.get("AFFINE_BASE_URL", "https://app.affine.pro/api")
WORKSPACE_ID: str = os.environ.get(
    "AFFINE_WORKSPACE_ID", "ef927d3a-5be0-41ed-b639-829b7f74939b"
)
# Affine hosted MCP endpoint — verified 2026-06-15 via curl
# (POST initialize -> HTTP 200, serverInfo confirms workspace id, protocol 2025-06-18).
MCP_URL: str = f"{BASE_URL.rstrip('/')}/workspaces/{WORKSPACE_ID}/mcp"

# Local fallback for DEAL drafts (Geordi Guides -> Affine DEAL pipeline).
DEAL_DRAFTS_PATH: Path = Path(
    os.environ.get(
        "AFFINE_DEAL_DRAFTS_PATH",
        str(
            Path.home()
            / "ASpace_OS_V2"
            / "20_Life_OS"
            / "24_PARA_Enterprise"
            / "03_Resources_Geordi"
            / "01_Guides"
            / "affine_deal_drafts.md"
        ),
    )
)

server = Server("affine-mcp")
logger = logging.getLogger("affine-mcp")

# ---------------------------------------------------------------------------
# Stubs (preserved verbatim from 2026-06-15 stub mode; used when API_KEY is
# unset or the streamable-http connection fails). Tests depend on the shape
# of these payloads (D5 — no surprise regressions).
# ---------------------------------------------------------------------------


def _stub_workspaces() -> list[dict[str, Any]]:
    """Stub workspace list — no real API call without AFFINE_API_KEY."""
    return [
        {
            "id": WORKSPACE_ID,
            "name": "A'Space DEAL Workspace",
            "kind": "DEAL",
            "url": f"https://app.affine.pro/workspace/{WORKSPACE_ID}",
            "edgeless": True,
        }
    ]


def _stub_deal_drafts() -> list[dict[str, Any]]:
    """Stub DEAL drafts read from local file or fallback mock."""
    if DEAL_DRAFTS_PATH.exists():
        try:
            content = DEAL_DRAFTS_PATH.read_text(encoding="utf-8")
            return [
                {
                    "id": "local-draft-1",
                    "title": "DEAL Drafts (local file)",
                    "source": str(DEAL_DRAFTS_PATH),
                    "content_excerpt": content[:500],
                    "state": "Define",
                }
            ]
        except OSError as exc:
            return [{"error": f"Failed to read {DEAL_DRAFTS_PATH}: {exc}"}]
    return [
        {
            "id": "stub-draft-1",
            "title": "Task Capture -> Plane (Blueprint)",
            "state": "Automate",
            "blueprint_type": "cli",
            "target_ryan": True,
        },
        {
            "id": "stub-draft-2",
            "title": "Email Triage -> Inbox Zero",
            "state": "Eliminate",
            "blueprint_type": "manual",
            "target_ryan": False,
        },
    ]


# ---------------------------------------------------------------------------
# Tool catalogue (stable Symphony contract — hardcoded so the local server
# always advertises the same 4 tools whether the upstream MCP is reachable
# or not; matches the prior shape byte-for-byte).
# ---------------------------------------------------------------------------


def _tool_definitions() -> list[Tool]:
    """Return the hardcoded list of 4 Affine DEAL tools (Symphony contract)."""
    return [
        Tool(
            name="affine_list_workspaces",
            description="List Affine workspaces accessible to the configured API key.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="affine_get_deal_draft",
            description="Fetch a DEAL (Define/Eliminate/Automate/Liberate) draft by ID from the workspace.",
            inputSchema={
                "type": "object",
                "properties": {
                    "draft_id": {
                        "type": "string",
                        "description": "DEAL draft identifier (AF-XXXXXXXX or full UUID).",
                    }
                },
                "required": ["draft_id"],
            },
        ),
        Tool(
            name="affine_create_deal_draft",
            description="Create a new DEAL draft in the workspace. Returns the new draft ID and URL.",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "DEAL draft title."},
                    "stage": {
                        "type": "string",
                        "enum": ["Define", "Eliminate", "Automate", "Liberated"],
                        "description": "Initial DEAL stage.",
                    },
                    "description": {
                        "type": "string",
                        "description": "Long-form description (Markdown).",
                        "default": "",
                    },
                    "blueprint_type": {
                        "type": "string",
                        "enum": ["iframe", "cli", "agent", "manual"],
                        "description": "Type of Blueprint this draft represents (Edgeless canvas).",
                        "default": "manual",
                    },
                    "target_ryan": {
                        "type": "boolean",
                        "description": "Flag ready for 13th Doctor (Ryan) codification.",
                        "default": False,
                    },
                },
                "required": ["title", "stage"],
            },
        ),
        Tool(
            name="affine_list_deal_drafts",
            description="List all DEAL drafts in the workspace (active stages only by default).",
            inputSchema={
                "type": "object",
                "properties": {
                    "stage_filter": {
                        "type": "string",
                        "enum": [
                            "Define",
                            "Eliminate",
                            "Automate",
                            "Liberated",
                            "Kept Manual",
                        ],
                        "description": "Optional: filter by DEAL stage.",
                    }
                },
            },
        ),
    ]


# ---------------------------------------------------------------------------
# Remote session (streamable-http proxy)
# ---------------------------------------------------------------------------


@asynccontextmanager
async def _remote_session() -> AsyncIterator[ClientSession | None]:
    """
    Yield a live ClientSession connected to the Affine hosted MCP, or None on
    failure. Catches all exceptions and returns None so the stdio server can
    keep running in stub mode (D7 — never crash the host agent).

    Lifecycle: the streamable-http connection stays open for the duration of
    the `async with` block. The caller is expected to keep it alive for the
    whole lifetime of the stdio MCP server (see `main()`).
    """
    if not API_KEY:
        logger.info("AFFINE_API_KEY unset — remote MCP disabled, stub mode only")
        yield None
        return

    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        async with streamablehttp_client(url=MCP_URL, headers=headers, timeout=30) as (
            read_stream,
            write_stream,
            _get_session_id,
        ):
            async with ClientSession(read_stream, write_stream) as remote:
                await remote.initialize()
                logger.info("Remote Affine MCP connected: %s", MCP_URL)
                yield remote
    except Exception as exc:  # noqa: BLE001 — D7 swallow + log
        logger.warning(
            "Remote Affine MCP unavailable (%s: %s) — falling back to stub mode",
            type(exc).__name__,
            exc,
        )
        yield None


def _result_to_textcontent(result: Any) -> list[TextContent]:
    """Convert an upstream CallToolResult into a list of TextContent.

    The official MCP SDK returns CallToolResult with .content (list of
    TextContent | ImageContent | EmbeddedResource). We keep TextContent
    shape so the stdio client always sees a serializable text payload.
    """
    contents: list[TextContent] = []
    for block in getattr(result, "content", []) or []:
        text = getattr(block, "text", None)
        if text is not None:
            contents.append(TextContent(type="text", text=text))
    if not contents:
        # Fall back to stringifying the result so callers always get *something*.
        contents.append(TextContent(type="text", text=str(result)))
    return contents


# ---------------------------------------------------------------------------
# Server handlers
# ---------------------------------------------------------------------------


@server.list_tools()
async def list_tools() -> list[Tool]:
    return _tool_definitions()


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Dispatch a tool call to the remote Affine MCP when reachable, else stub.

    D1 verify-before-assert: the remote tool list is logged on first connect,
    so we can later diff it against `_tool_definitions()` to detect upstream
    drift. The 4 hardcoded tools are the *Symphony* contract; upstream may
    expose more, which is fine — the stdio client only ever sees the 4 we
    advertise in `list_tools()`.
    """
    remote: ClientSession | None = getattr(call_tool, "_remote", None)

    if remote is not None:
        try:
            result = await remote.call_tool(name, arguments or {})
            return _result_to_textcontent(result)
        except Exception as exc:  # noqa: BLE001 — D7 swallow + log
            logger.warning(
                "Remote call_tool(%s) failed (%s: %s) — falling back to stub",
                name,
                type(exc).__name__,
                exc,
            )
            # fall through to stub path below

    # ----- Stub fallback (no remote session, or remote call failed) -----
    if name == "affine_list_workspaces":
        workspaces = _stub_workspaces()
        return [TextContent(type="text", text=f"Workspaces: {workspaces}")]

    if name == "affine_get_deal_draft":
        draft_id = arguments.get("draft_id", "")
        drafts = _stub_deal_drafts()
        match = next((d for d in drafts if d.get("id") == draft_id), None)
        if match is None:
            return [TextContent(type="text", text=f"[!] DEAL draft '{draft_id}' not found")]
        return [TextContent(type="text", text=f"DEAL draft: {match}")]

    if name == "affine_create_deal_draft":
        if not API_KEY:
            return [
                TextContent(
                    type="text",
                    text=(
                        "[!] AFFINE_API_KEY not set — stub create. "
                        "Set env var to enable real API calls."
                    ),
                )
            ]
        title = arguments.get("title", "Untitled")
        stage = arguments.get("stage", "Define")
        return [
            TextContent(
                type="text",
                text=(
                    f"[+] DEAL draft created (stub): title={title!r} stage={stage!r} "
                    f"workspace={WORKSPACE_ID}"
                ),
            )
        ]

    if name == "affine_list_deal_drafts":
        stage_filter = arguments.get("stage_filter")
        drafts = _stub_deal_drafts()
        if stage_filter:
            drafts = [d for d in drafts if d.get("state") == stage_filter]
        return [TextContent(type="text", text=f"DEAL drafts: {drafts}")]

    raise ValueError(f"Unknown tool: {name}")


# ---------------------------------------------------------------------------
# main() — keep the remote session alive for the lifetime of the stdio server
# ---------------------------------------------------------------------------


async def main() -> None:
    """Boot the stdio MCP server with a long-lived streamable-http upstream.

    We open the remote session once, attach it to `call_tool._remote` via a
    closure, and then run the stdio server. When the stdio server exits, the
    remote session context unwinds cleanly.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(name)s] %(levelname)s: %(message)s",
        stream=sys.stderr,
    )
    logger.info("Affine MCP server starting (Symphony Lane B / DEAL workspace)")
    logger.info("MCP_URL=%s (workspace=%s)", MCP_URL, WORKSPACE_ID)

    async with _remote_session() as remote:
        # Stash on the function object so `call_tool` can read it without
        # threading state through every call.
        call_tool._remote = remote  # type: ignore[attr-defined]
        if remote is None:
            logger.info("Running in STUB mode (no upstream MCP)")
        else:
            try:
                tools = await remote.list_tools()
                logger.info(
                    "Upstream MCP advertises %d tools (Symphony exposes %d)",
                    len(tools.tools),
                    len(_tool_definitions()),
                )
            except Exception as exc:  # noqa: BLE001 — best-effort log only
                logger.warning("list_tools() probe failed: %s", exc)

        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream, write_stream, server.create_initialization_options()
            )


if __name__ == "__main__":
    asyncio.run(main())
