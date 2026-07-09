#!/usr/bin/env python3
"""
mcp-obsidian.py — Symphony Lane B MCP server for Obsidian (PARA vault, local FS).

A'Space OS V2 — Sovereign Twin Runtime.
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

This MCP server exposes the Obsidian PARA vault to the Symphony agent runtime
via direct filesystem access (offline-first, no cloud). Reads MANIFEST.md frontmatter
in each PARA folder (01_Projects / 02_Areas / 03_Resources / 04_Archives).
Operated by Picard (USS Enterprise, A2 manager).

Usage:
    "C:/Python314/python.exe" mcp-obsidian.py

Auth:
    None (local filesystem access only). No API key required.

Doctrine anchors:
- ADR-META-001 D1, D2
- Symphony Adapter — Obsidian (L1 Shadow Life OS), 2026-05-14
- SDD-008 §2 Pilier 1 (Obsidian = PARA)
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import TextContent, Tool
except ImportError:
    print("[!] MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Local vault path (no API key — offline-first sovereign)
VAULT_ROOT: Path = Path(
    os.environ.get(
        "OBSIDIAN_VAULT_PATH",
        str(Path.home() / "ASpace_OS_V2" / "20_Life_OS" / "24_PARA_Enterprise"),
    )
)

# PARA folder names (canon)
PARA_FOLDERS: dict[str, str] = {
    "projects": "01_Projects",
    "areas": "02_Areas",
    "resources": "03_Resources",
    "archives": "04_Archives",
}

server = Server("obsidian-mcp")

# Frontmatter parser — minimal YAML subset (key: value, no nested structures)
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL | re.MULTILINE)


def parse_frontmatter(content: str) -> dict[str, str]:
    """Parse simple YAML frontmatter (key: value per line)."""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}
    fm: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm


def _list_in_folder(folder: str) -> list[dict[str, Any]]:
    folder_path = VAULT_ROOT / folder
    if not folder_path.exists():
        return []
    items: list[dict[str, Any]] = []
    for child in sorted(folder_path.iterdir()):
        if child.is_dir():
            manifest = child / "MANIFEST.md"
            entry: dict[str, Any] = {
                "name": child.name,
                "path": str(child.relative_to(VAULT_ROOT)),
                "kind": "folder",
            }
            if manifest.exists():
                try:
                    content = manifest.read_text(encoding="utf-8")
                    fm = parse_frontmatter(content)
                    entry["manifest"] = fm
                except OSError:
                    pass
            items.append(entry)
    return items


def _search_vault(query: str) -> list[dict[str, Any]]:
    """Case-insensitive substring search across all .md files in the vault."""
    if not VAULT_ROOT.exists():
        return []
    q = query.lower()
    hits: list[dict[str, Any]] = []
    for md in VAULT_ROOT.rglob("*.md"):
        try:
            content = md.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if q in content.lower():
            hits.append(
                {
                    "path": str(md.relative_to(VAULT_ROOT)),
                    "snippet": content[:200],
                }
            )
            if len(hits) >= 25:
                break
    return hits


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="obsidian_list_projects",
            description="List items in 01_Projects (PARA) — read MANIFEST.md frontmatter per folder.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="obsidian_list_areas",
            description="List items in 02_Areas (PARA) — Life Wheel + Business domains.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="obsidian_list_resources",
            description="List items in 03_Resources (PARA) — knowledge base, templates, references.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="obsidian_list_archives",
            description="List items in 04_Archives (PARA) — completed projects, deprecated notes.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="obsidian_search",
            description="Full-text search across the vault (case-insensitive substring).",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query string."}
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="obsidian_get_note",
            description="Read a note by vault-relative path. Returns content + parsed frontmatter.",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Vault-relative path to the .md file (e.g. '01_Projects/foo/MANIFEST.md').",
                    }
                },
                "required": ["path"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    if name == "obsidian_list_projects":
        return [TextContent(type="text", text=f"Projects: {_list_in_folder(PARA_FOLDERS['projects'])}")]

    if name == "obsidian_list_areas":
        return [TextContent(type="text", text=f"Areas: {_list_in_folder(PARA_FOLDERS['areas'])}")]

    if name == "obsidian_list_resources":
        return [TextContent(type="text", text=f"Resources: {_list_in_folder(PARA_FOLDERS['resources'])}")]

    if name == "obsidian_list_archives":
        return [TextContent(type="text", text=f"Archives: {_list_in_folder(PARA_FOLDERS['archives'])}")]

    if name == "obsidian_search":
        query = arguments.get("query", "")
        if not query:
            return [TextContent(type="text", text="[!] Empty query")]
        hits = _search_vault(query)
        return [TextContent(type="text", text=f"Search hits ({len(hits)}): {hits}")]

    if name == "obsidian_get_note":
        rel_path = arguments.get("path", "")
        full = VAULT_ROOT / rel_path
        if not full.exists() or not full.is_file():
            return [TextContent(type="text", text=f"[!] Note not found: {rel_path}")]
        try:
            content = full.read_text(encoding="utf-8")
        except OSError as exc:
            return [TextContent(type="text", text=f"[!] Failed to read: {exc}")]
        fm = parse_frontmatter(content)
        return [
            TextContent(
                type="text",
                text=f"Note: path={rel_path} frontmatter={fm} content_length={len(content)}",
            )
        ]

    raise ValueError(f"Unknown tool: {name}")


async def main() -> None:
    print(
        f"[+] Obsidian MCP server starting (Symphony Lane B / PARA vault) at {VAULT_ROOT}",
        file=sys.stderr,
    )
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
