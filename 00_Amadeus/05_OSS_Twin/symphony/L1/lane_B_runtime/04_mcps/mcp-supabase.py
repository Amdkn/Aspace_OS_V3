#!/usr/bin/env python3
"""
mcp-supabase.py — Symphony Lane B MCP server for Supabase Cloud (multi-project).

A'Space OS V2 — Sovereign Twin Runtime.
Created 2026-06-15 by A0 mandate (anti-pause + multi-orgs orchestration).

This MCP server exposes Supabase REST/PostgREST operations across all FREE
projects A0 owns on Supabase Cloud. Projects are loaded at boot from env
vars (SUPABASE_<SLUG>_URL + SUPABASE_<SLUG>_ANON_KEY, optional SERVICE_ROLE_KEY).
Pattern mirrors mcp-plane.py: httpx async client + anon/service_role key +
stub fallback when keys are missing.

The flagship tool is `supabase_anti_pause_ping` which does a trivial GET on
each configured project's /rest/v1/ endpoint, generating DB activity every
few days to prevent the 1-week inactivity pause rule (D6 — activity inference,
not officially documented as such).

Usage:
    "C:/Python314/python.exe" mcp-supabase.py

Auth:
    Per-project env vars. Pattern: SUPABASE_<SLUG>_URL + SUPABASE_<SLUG>_ANON_KEY
    + optional SUPABASE_<SLUG>_SERVICE_ROLE_KEY for admin tasks.
    Slug convention: lowercase + underscores.

Doctrine anchors:
- ADR-META-001 D1 (verify before assert), D2 (research-first), D7 (no crash)
- Symphony Adapter — Supabase (L1 Shadow Multi-Tenant), 2026-06-15
- Test Key Pragma (env var User scope, never hardcoded in code)

D6 nuance — Supabase's official 7-day inactivity pause rule is documented
("Paused Free Plan projects are restorable for 90 days" — changelog 2024-06-24).
What counts as "activity" is NOT officially documented. We assume any HTTP
hit on /rest/v1/ counts (D6 inference: API key auth forces DB query → activity).
"""
from __future__ import annotations

import asyncio
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

# ── Project registry ──────────────────────────────────────────────────────────
# D2: Each project gets URL + anon_key + optional service_role_key from env.
# Slug is the env-var prefix.
# A0 adds new entries by setting 2-3 env vars per project, no code change.

PROJECT_SLUGS: list[str] = []  # populated at boot from env scan
PROJECTS: dict[str, dict[str, str]] = {}  # slug -> {url, anon_key, service_role_key}

# ── Helpers ──────────────────────────────────────────────────────────────────

# Field suffixes, ordered longest-first so endswith() matches the most specific.
# This handles BOTH single-word slugs (SUPABASE_LIFE_OS_URL -> slug=life_os, field=URL)
# AND multi-underscore field names (SUPABASE_LIFE_OS_ANON_KEY -> slug=life_os, field=ANON_KEY).
_FIELD_SUFFIXES: tuple[str, ...] = ("SERVICE_ROLE_KEY", "ANON_KEY", "URL")


def _parse_env_key(key: str, prefix: str) -> tuple[str, str] | None:
    """Return (slug, field) for a SUPABASE_<SLUG>_<FIELD> env var, or None if not parseable.

    D6 fix 2026-06-17: use longest-suffix matching instead of rsplit('_', 1).
    Previous rsplit broke multi-underscore fields like ANON_KEY on multi-word slugs
    (e.g. SUPABASE_LIFE_OS_ANON_KEY was split as ('LIFE_OS_ANON', 'KEY') instead
    of ('LIFE_OS', 'ANON_KEY'), so ANON_KEY never matched _VALID_FIELDS).
    """
    if not key.startswith(prefix):
        return None
    rest = key[len(prefix):]
    for suffix in _FIELD_SUFFIXES:
        if rest == suffix:
            return None  # No slug, just SUPABASE_URL — skip
        if rest.endswith("_" + suffix):
            slug_raw = rest[: -(len(suffix) + 1)]
            if not slug_raw:
                return None
            return slug_raw.lower(), suffix
    return None


def _load_projects() -> None:
    """Scan env vars for SUPABASE_<SLUG>_{URL,ANON_KEY,SERVICE_ROLE_KEY} triplets."""
    seen: dict[str, dict[str, str]] = {}
    prefix = "SUPABASE_"
    for key, val in os.environ.items():
        parsed = _parse_env_key(key, prefix)
        if parsed is None:
            continue
        slug, field = parsed
        if field == "URL":
            seen.setdefault(slug, {})["url"] = val.rstrip("/")
        elif field == "ANON_KEY":
            seen.setdefault(slug, {})["anon_key"] = val
        elif field == "SERVICE_ROLE_KEY":
            seen.setdefault(slug, {})["service_role_key"] = val
    # Only keep projects that have at least URL + ANON_KEY
    PROJECTS.clear()
    PROJECT_SLUGS.clear()
    for slug, cfg in seen.items():
        if "url" in cfg and "anon_key" in cfg:
            PROJECTS[slug] = cfg
            PROJECT_SLUGS.append(slug)


def _headers(slug: str, *, service_role: bool = False) -> dict[str, str]:
    """Build Supabase auth headers for a given project slug."""
    cfg = PROJECTS[slug]
    key = cfg.get("service_role_key") if service_role else cfg.get("anon_key")
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }


def _liveness_table(slug: str) -> str:
    """Return a table name that is exposed via PostgREST and can be probed with anon key.

    D6 fix 2026-06-17: PostgREST root (/rest/v1/) now REQUIRES the secret/service_role
    key (returns 401 "Secret API key required" with publishable key). So health/anti-pause
    probes must hit /rest/v1/<table> instead. Each project can override via env var
    SUPABASE_<SLUG>_LIVENESS_TABLE; default = "user_profiles" (Life OS canon).
    """
    env_key = f"SUPABASE_{slug.upper()}_LIVENESS_TABLE"
    if env_key in os.environ:
        return os.environ[env_key]
    # Per-project fallback: Life OS canon has user_profiles
    return "user_profiles"


def _stub_projects() -> list[dict[str, Any]]:
    """Stub project list — used when no env vars are set (D7 fallback)."""
    return []


# ── Tool implementations ────────────────────────────────────────────────────

async def _list_projects() -> list[dict[str, Any]]:
    if not PROJECTS:
        return _stub_projects()
    out = []
    for slug in PROJECT_SLUGS:
        cfg = PROJECTS[slug]
        out.append({
            "slug": slug,
            "url": cfg["url"],
            "has_service_role": "service_role_key" in cfg,
        })
    return out


async def _query(slug: str, table: str, select: str = "*", limit: int = 100) -> dict[str, Any]:
    if slug not in PROJECTS:
        return {"error": f"Project '{slug}' not configured (no env vars)"}
    url = f"{PROJECTS[slug]['url']}/rest/v1/{table}"
    params = {"select": select, "limit": str(limit)}
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(url, headers=_headers(slug), params=params)
    return {
        "status": r.status_code,
        "slug": slug,
        "table": table,
        "rows": r.json() if r.status_code == 200 else [],
    }


async def _list_tables(slug: str) -> dict[str, Any]:
    """Probe a known table to verify liveness + return its presence."""
    if slug not in PROJECTS:
        return {"error": f"Project '{slug}' not configured"}
    table = _liveness_table(slug)
    url = f"{PROJECTS[slug]['url']}/rest/v1/{table}?select=id&limit=0"
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(url, headers=_headers(slug))
    return {
        "status": r.status_code,
        "slug": slug,
        "liveness_table": table,
        "alive": r.status_code == 200,
        "hint": "PostgREST table probe — HTTP 200 means project is alive. Use /rest/v1/<table>?select=* to query specific tables.",
    }


async def _get_metrics(slug: str) -> dict[str, Any]:
    """Best-effort metrics: liveness probe + auth.users count (RLS-respecting)."""
    if slug not in PROJECTS:
        return {"error": f"Project '{slug}' not configured"}
    url_root = PROJECTS[slug]["url"]
    table = _liveness_table(slug)
    async with httpx.AsyncClient(timeout=10.0) as client:
        # Liveness probe on a known table (works with publishable key)
        r_live = await client.get(
            f"{url_root}/rest/v1/{table}?select=id&limit=0",
            headers=_headers(slug),
        )
        # Probe auth.users for user count (may be 401 with anon key on real auth schema)
        r_users = await client.get(
            f"{url_root}/rest/v1/users",
            headers={**_headers(slug), "Range": "0-0", "Prefer": "count=exact"},
        )
        count_hdr = r_users.headers.get("content-range", "0/0")
        total = count_hdr.split("/")[-1] if "/" in count_hdr else "0"
    return {
        "status": "alive" if r_live.status_code == 200 else "unhealthy",
        "slug": slug,
        "liveness_table": table,
        "rest_table_status": r_live.status_code,
        "auth_users_count": total if r_users.status_code == 200 else "n/a (RLS or 401)",
        "note": "Approximate count via Content-Range header. For real-time usage, query Supabase Studio.",
    }


async def _anti_pause_ping(targets: list[str] | None = None) -> dict[str, Any]:
    """The flagship tool: hit /rest/v1/<liveness_table> on each configured project.

    D6 fix 2026-06-17: was hitting /rest/v1/ root which now requires secret key.
    Now hits a known table (configurable per project, default = "user_profiles").
    Schedule via pg_cron or systemd timer to run at least once every 6 days.
    """
    if not PROJECTS:
        return {"error": "No projects configured. Set SUPABASE_<SLUG>_URL + ANON_KEY env vars."}
    slugs_to_ping = targets or PROJECT_SLUGS
    results = []
    async with httpx.AsyncClient(timeout=10.0) as client:
        for slug in slugs_to_ping:
            if slug not in PROJECTS:
                results.append({"slug": slug, "status": "not_configured"})
                continue
            table = _liveness_table(slug)
            url = f"{PROJECTS[slug]['url']}/rest/v1/{table}?select=id&limit=0"
            try:
                r = await client.get(url, headers=_headers(slug))
                results.append({
                    "slug": slug,
                    "table": table,
                    "status_code": r.status_code,
                    "alive": r.status_code == 200,
                    "latency_ms": r.elapsed.total_seconds() * 1000,
                })
            except httpx.HTTPError as exc:
                results.append({"slug": slug, "status": "error", "error": str(exc)})
    return {
        "anti_pause_pinged": len([r for r in results if r.get("alive")]),
        "total_projects": len(results),
        "results": results,
        "doctrine_note": (
            "D6 inference: any successful API hit generates DB activity. "
            "HYPOTHESE: this prevents 1-week inactivity pause. Not officially documented."
        ),
    }


async def _health_check() -> dict[str, Any]:
    """Quick liveness probe across all configured projects (table-based)."""
    if not PROJECTS:
        return {"error": "No projects configured"}
    out = []
    async with httpx.AsyncClient(timeout=5.0) as client:
        for slug in PROJECT_SLUGS:
            table = _liveness_table(slug)
            url = f"{PROJECTS[slug]['url']}/rest/v1/{table}?select=id&limit=0"
            try:
                r = await client.get(url, headers=_headers(slug))
                out.append({"slug": slug, "alive": r.status_code == 200, "status": r.status_code, "table": table})
            except httpx.HTTPError as exc:
                out.append({"slug": slug, "alive": False, "error": str(exc)})
    return {"projects": out}


# ── MCP server wiring ─────────────────────────────────────────────────────────

server = Server("supabase-mcp")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="supabase_list_projects",
            description="List all Supabase projects configured for the Symphony runtime (via env vars).",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="supabase_query",
            description="Query a Supabase table via PostgREST. Returns rows + status. Uses anon key (RLS).",
            inputSchema={
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Project slug (must match a SUPABASE_<SLUG>_* env var prefix)."},
                    "table": {"type": "string", "description": "Table name in public schema."},
                    "select": {"type": "string", "default": "*", "description": "PostgREST select clause."},
                    "limit": {"type": "integer", "default": 100, "description": "Max rows."},
                },
                "required": ["slug", "table"],
            },
        ),
        Tool(
            name="supabase_list_tables",
            description="Probe a Supabase project's PostgREST root to verify liveness and discover tables.",
            inputSchema={
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Project slug."},
                },
                "required": ["slug"],
            },
        ),
        Tool(
            name="supabase_get_metrics",
            description="Best-effort metrics: liveness + auth.users count. For real-time usage, query Studio.",
            inputSchema={
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Project slug."},
                },
                "required": ["slug"],
            },
        ),
        Tool(
            name="supabase_anti_pause_ping",
            description=(
                "FLAGSHIP ANTI-PAUSE TOOL. Trivial HTTP request to /rest/v1/ on each "
                "configured project, generating DB activity. Schedule via pg_cron or "
                "systemd timer to run every 5-6 days. D6 inference: prevents the 1-week "
                "inactivity pause. HYPOTHESE: not officially documented but logically sound."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "targets": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional: limit ping to specific slugs. Default: all configured projects.",
                    },
                },
            },
        ),
        Tool(
            name="supabase_health_check",
            description="Liveness probe across all configured projects (lightweight, no DB query).",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    if name == "supabase_list_projects":
        return [TextContent(type="text", text=f"Projects: {await _list_projects()}")]
    if name == "supabase_query":
        slug = arguments.get("slug", "")
        table = arguments.get("table", "")
        result = await _query(slug, table, arguments.get("select", "*"), arguments.get("limit", 100))
        return [TextContent(type="text", text=f"Query result: {result}")]
    if name == "supabase_list_tables":
        slug = arguments.get("slug", "")
        return [TextContent(type="text", text=f"Tables probe: {await _list_tables(slug)}")]
    if name == "supabase_get_metrics":
        slug = arguments.get("slug", "")
        return [TextContent(type="text", text=f"Metrics: {await _get_metrics(slug)}")]
    if name == "supabase_anti_pause_ping":
        targets = arguments.get("targets")
        return [TextContent(type="text", text=f"Anti-pause ping: {await _anti_pause_ping(targets)}")]
    if name == "supabase_health_check":
        return [TextContent(type="text", text=f"Health: {await _health_check()}")]
    raise ValueError(f"Unknown tool: {name}")


async def main() -> None:
    _load_projects()
    print(
        f"[+] Supabase MCP server starting — {len(PROJECTS)} project(s) configured: {PROJECT_SLUGS or 'STUB mode'}",
        file=sys.stderr,
    )
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
