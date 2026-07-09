#!/usr/bin/env python3
"""
mcp-plane.py — Symphony Lane B MCP server for Plane.so (GTD workspace).

A'Space OS V2 — Sovereign Twin Runtime.
Created 2026-06-15 by A0 mandate (Symphony Phase 2). Rewritten 2026-06-15 to
proxy tool calls to the live Plane.so REST API via httpx.AsyncClient
(Plane.so has no MCP endpoint — REST + GraphQL only, verified D1).

This MCP server exposes Plane.so GTD operations to the Symphony agent runtime.
Plane hosts the GTD Inbox -> Next Actions -> Today -> Done flow operated by the
USS Cerritos crew (Mariner/Boimler/Tendi/Freeman/Rutherford).

Usage:
    "C:/Python314/python.exe" mcp-plane.py

Auth:
    Set PLANE_API_KEY env var (User scope) before running.
    Set PLANE_WORKSPACE_SLUG and PLANE_PROJECT_ID for the active project.
    If PROJECT_ID is empty, the MCP falls back to stub mode (D7 — never crash).

Doctrine anchors:
- ADR-META-001 D1 (verify before assert), D2 (research-first), D7 (no crash)
- Symphony Adapter — Plane.so (L1 Shadow GTD), 2026-05-13
- SDD-008 §3.1 (Cerritos GTD workflow)

State resolution:
    Plane stores issues with a state UUID, not a state name. The MCP fetches
    the project's states list once and caches the name→UUID mapping in a
    module-level dict. If a GTD state name from the spec (e.g. "Inbox") does
    not exist in the live project, the affected tool falls back to the stub
    data and emits a clear warning to stderr (D6 — root-cause transparency).

    As of D1 verification 2026-06-15, the live project only contains the 5
    default Plane states (Backlog, Todo, In Progress, Done, Cancelled) — the
    spec's GTD names have not been created in the live workspace yet. A0
    follow-up: create the 7 GTD states in Plane UI or via API before
    promoting this MCP to production mode.
"""
from __future__ import annotations

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

# Auth from env var (Test Key Pragma 2026-06-15 — never hardcoded)
API_KEY: str = os.environ.get("PLANE_API_KEY", "")
BASE_URL: str = os.environ.get("PLANE_BASE_URL", "https://api.plane.so/api/v1")
WORKSPACE_SLUG: str = os.environ.get("PLANE_WORKSPACE_SLUG", "aspace-core")
PROJECT_ID: str = os.environ.get("PLANE_PROJECT_ID", "")

# GTD state mapping (from spec §3)
GTD_STATES: list[str] = ["Inbox", "Next Actions", "Today", "Waiting For", "Done", "Cancelled", "Trash"]

# Live-mode headers (D1 — verified X-API-Key auth against api.plane.so 2026-06-15)
HEADERS: dict[str, str] = (
    {"X-API-Key": API_KEY, "Content-Type": "application/json"} if API_KEY else {}
)

# Module-level cache: state name -> UUID (populated lazily by _load_state_map)
_STATE_NAME_TO_UUID: dict[str, str] = {}
_STATES_LOADED: bool = False

server = Server("plane-mcp")


# ---------------------------------------------------------------------------
# Stub layer (preserved from v0 — used when API_KEY is empty OR when the
# live API returns no UUID for a requested GTD state name).
# ---------------------------------------------------------------------------


def _stub_issues(state: str | None = None) -> list[dict[str, Any]]:
    base = [
        {
            "id": "stub-iss-1",
            "sequence_id": 1,
            "name": "Review YouTube ingestion handoff",
            "state": "Inbox",
            "labels": ["@L1", "domain:GTD"],
            "priority": "high",
        },
        {
            "id": "stub-iss-2",
            "sequence_id": 2,
            "name": "Rotate VERCEL_TOKEN post-deploy (Test Key Pragma phase 4)",
            "state": "Next Actions",
            "labels": ["@L0", "@5-min"],
            "priority": "urgent",
        },
        {
            "id": "stub-iss-3",
            "sequence_id": 3,
            "name": "Verify /login E2E with A0 (signin + signup toggle)",
            "state": "Today",
            "labels": ["@L1", "@deep-work"],
            "priority": "high",
        },
    ]
    if state:
        return [i for i in base if i["state"] == state]
    return base


# ---------------------------------------------------------------------------
# Live REST proxy layer (httpx.AsyncClient, X-API-Key auth)
# ---------------------------------------------------------------------------


def _live_enabled() -> bool:
    """Return True iff all four live-mode env vars are set."""
    return bool(API_KEY) and bool(PROJECT_ID) and bool(WORKSPACE_SLUG) and bool(BASE_URL)


async def _plane_get(path: str) -> dict[str, Any] | list[Any]:
    """GET BASE_URL+path with X-API-Key. Raise on non-2xx. Return JSON."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(BASE_URL + path, headers=HEADERS)
        resp.raise_for_status()
        return resp.json() if resp.content else {}


async def _plane_post(path: str, body: dict[str, Any]) -> dict[str, Any]:
    """POST JSON to BASE_URL+path with X-API-Key. Raise on non-2xx. Return JSON."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.post(BASE_URL + path, headers=HEADERS, json=body)
        resp.raise_for_status()
        return resp.json() if resp.content else {}


async def _plane_patch(path: str, body: dict[str, Any]) -> dict[str, Any]:
    """PATCH JSON to BASE_URL+path with X-API-Key. Raise on non-2xx. Return JSON."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.patch(BASE_URL + path, headers=HEADERS, json=body)
        resp.raise_for_status()
        return resp.json() if resp.content else {}


async def _load_state_map() -> dict[str, str]:
    """Fetch project's states and populate the name->UUID cache.

    Returns the cache dict. On any error, returns whatever was loaded so far
    (possibly empty). Idempotent: a second call is a no-op.
    """
    global _STATES_LOADED
    if _STATES_LOADED:
        return _STATE_NAME_TO_UUID
    if not _live_enabled():
        return _STATE_NAME_TO_UUID
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/states/"
    try:
        data = await _plane_get(path)
        results = data.get("results", []) if isinstance(data, dict) else []
        for s in results:
            name = s.get("name")
            sid = s.get("id")
            if name and sid:
                _STATE_NAME_TO_UUID[name] = sid
        _STATES_LOADED = True
    except (httpx.HTTPError, ValueError, KeyError) as exc:
        print(
            f"[!] _load_state_map failed: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
    return _STATE_NAME_TO_UUID


def _resolve_state_uuid(state_name: str) -> str | None:
    """Synchronous lookup against the cached state map. Returns UUID or None."""
    return _STATE_NAME_TO_UUID.get(state_name)


# ---------------------------------------------------------------------------
# Live tool implementations
# ---------------------------------------------------------------------------


async def _live_list_issues(state: str | None) -> list[dict[str, Any]]:
    """GET .../issues/?state=<uuid> (state UUID resolved from name first)."""
    params: list[str] = []
    if state:
        await _load_state_map()
        uuid = _resolve_state_uuid(state)
        if uuid is None:
            raise ValueError(
                f"State name {state!r} has no UUID in live workspace (loaded "
                f"{len(_STATE_NAME_TO_UUID)} states: {sorted(_STATE_NAME_TO_UUID)})"
            )
        params.append(f"state={uuid}")
    params.append("per_page=50")
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/?{'&'.join(params)}"
    data = await _plane_get(path)
    results = data.get("results", []) if isinstance(data, dict) else []
    # Normalize to a stable shape (id, sequence_id, name, state, priority, labels)
    out: list[dict[str, Any]] = []
    for i in results:
        out.append(
            {
                "id": i.get("id"),
                "sequence_id": i.get("sequence_id"),
                "name": i.get("name"),
                "state": i.get("state"),
                "priority": i.get("priority"),
                "labels": i.get("labels", []),
            }
        )
    return out


async def _live_create_issue(
    name: str,
    description: str,
    state: str,
    labels: list[str],
) -> dict[str, Any]:
    """POST .../issues/ with resolved state UUID."""
    body: dict[str, Any] = {"name": name}
    if description:
        body["description_html"] = f"<p>{description}</p>"
    if state:
        await _load_state_map()
        uuid = _resolve_state_uuid(state)
        if uuid is None:
            raise ValueError(
                f"State name {state!r} has no UUID in live workspace"
            )
        body["state"] = uuid
    if labels:
        body["labels"] = labels
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/"
    return await _plane_post(path, body)


async def _live_update_state(issue_id: str, new_state: str) -> dict[str, Any]:
    """PATCH .../issues/{issue_id}/ with resolved state UUID."""
    await _load_state_map()
    uuid = _resolve_state_uuid(new_state)
    if uuid is None:
        raise ValueError(
            f"State name {new_state!r} has no UUID in live workspace"
        )
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/{issue_id}/"
    return await _plane_patch(path, {"state": uuid})


# ---------------------------------------------------------------------------
# A0 expansion 2026-06-22 — 7 new live helpers (D4 append-only).
# Sub-work items + automation (Cerritos 5-stage extension).
# ---------------------------------------------------------------------------


async def _live_create_sub_work_item(
    parent_id: str,
    name: str,
    description: str,
    state: str,
) -> dict[str, Any]:
    """POST .../issues/ with parent=<parent_id> — D6 root cause fix 2026-06-22.

    Plane API does not expose a dedicated /sub-issues/ endpoint (404).
    D1 verified 2026-06-22 via curl direct : PATCH/POST /issues/ with
    `parent` field accepted, returns full issue payload.
    """
    body: dict[str, Any] = {"name": name, "parent": parent_id}
    if description:
        body["description_html"] = f"<p>{description}</p>"
    if state:
        await _load_state_map()
        uuid = _resolve_state_uuid(state)
        if uuid is None:
            raise ValueError(
                f"State name {state!r} has no UUID in live workspace"
            )
        body["state"] = uuid
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/"
    return await _plane_post(path, body)


async def _live_set_priority(issue_id: str, priority: str) -> dict[str, Any]:
    """PATCH .../issues/{issue_id}/ with priority field (urgent/high/medium/low/none)."""
    body: dict[str, Any] = {"priority": priority}
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/{issue_id}/"
    return await _plane_patch(path, body)


async def _live_set_assignee(issue_id: str, assignee_id: str) -> dict[str, Any]:
    """POST .../issues/{issue_id}/assignees/{assignee_id}/ — link user to issue."""
    path = (
        f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}"
        f"/issues/{issue_id}/assignees/{assignee_id}/"
    )
    return await _plane_post(path, {})


async def _live_set_labels(issue_id: str, labels: list[str]) -> dict[str, Any]:
    """PATCH .../issues/{issue_id}/ with labels array (replaces existing)."""
    body: dict[str, Any] = {"labels": labels}
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/{issue_id}/"
    return await _plane_patch(path, body)


async def _live_add_parent(issue_id: str, parent_id: str) -> dict[str, Any]:
    """PATCH .../issues/{issue_id}/ with parent field (retroactive link)."""
    body: dict[str, Any] = {"parent": parent_id}
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/{issue_id}/"
    return await _plane_patch(path, body)


async def _live_archive_issue(issue_id: str) -> dict[str, Any]:
    """PATCH .../issues/{issue_id}/ → state=Cancelled (D7 archive, never delete)."""
    await _load_state_map()
    uuid = _resolve_state_uuid("Cancelled")
    if uuid is None:
        raise ValueError("State 'Cancelled' has no UUID in live workspace")
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/issues/{issue_id}/"
    return await _plane_patch(path, {"state": uuid})


async def _live_create_module(
    name: str,
    description: str,
    start_date: str,
    target_date: str,
    status: str,
) -> dict[str, Any]:
    """POST .../modules/ — group Rocks canon under one umbrella."""
    body: dict[str, Any] = {"name": name, "status": status}
    if description:
        body["description_html"] = f"<p>{description}</p>"
    if start_date:
        body["start_date"] = start_date
    if target_date:
        body["target_date"] = target_date
    path = f"/workspaces/{WORKSPACE_SLUG}/projects/{PROJECT_ID}/modules/"
    return await _plane_post(path, body)


# ---------------------------------------------------------------------------
# MCP tool surface
# ---------------------------------------------------------------------------


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="plane_list_issues",
            description="List Plane issues for the active project, optionally filtered by state.",
            inputSchema={
                "type": "object",
                "properties": {
                    "state": {
                        "type": "string",
                        "enum": GTD_STATES,
                        "description": "Optional GTD state filter.",
                    }
                },
            },
        ),
        Tool(
            name="plane_get_inbox",
            description="List issues in the Inbox state (Mariner capture zone).",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="plane_get_next_actions",
            description="List issues in the Next Actions state (Boimler clarify zone).",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="plane_get_today",
            description="List issues in the Today state (Capt. Freeman engage zone).",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="plane_create_issue",
            description="Create a new Plane issue. Live mode requires PLANE_API_KEY + PLANE_PROJECT_ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Issue title."},
                    "description": {"type": "string", "description": "Issue body (Markdown).", "default": ""},
                    "state": {
                        "type": "string",
                        "enum": ["Inbox", "Next Actions", "Today", "Waiting For"],
                        "description": "Initial GTD state.",
                        "default": "Inbox",
                    },
                    "labels": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Labels (e.g. @L0, @L1, @L2, domain:GTD, @deep-work).",
                        "default": [],
                    },
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="plane_update_state",
            description="Update a Plane issue's state (GTD state transition).",
            inputSchema={
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string", "description": "Plane issue UUID."},
                    "new_state": {
                        "type": "string",
                        "enum": GTD_STATES,
                        "description": "Target GTD state.",
                    },
                },
                "required": ["issue_id", "new_state"],
            },
        ),
        # A0 expansion 2026-06-22 — Sub-work items + automation (Cerritos 5-stage).
        # D4 append-only : 7 nouveaux tools sans modifier les 6 existants.
        Tool(
            name="plane_create_sub_work_item",
            description="Create a sub-work item (nested issue) under a parent issue. Bridge 12WY Rock → Tactics W1-W12.",
            inputSchema={
                "type": "object",
                "properties": {
                    "parent_id": {"type": "string", "description": "Parent issue UUID (Rock canon Q3 2026)."},
                    "name": {"type": "string", "description": "Sub-work item title (e.g. 'W3 Tactic: Auto-research Phase 2 kickoff')."},
                    "description": {"type": "string", "description": "Sub-work item body (Markdown).", "default": ""},
                    "state": {
                        "type": "string",
                        "enum": ["Inbox", "Next Actions", "Today", "Waiting For"],
                        "description": "Initial GTD state (default Today for current week).",
                        "default": "Today",
                    },
                },
                "required": ["parent_id", "name"],
            },
        ),
        Tool(
            name="plane_set_priority",
            description="Set priority on a Plane issue (urgent/high/medium/low/none).",
            inputSchema={
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string", "description": "Plane issue UUID."},
                    "priority": {
                        "type": "string",
                        "enum": ["urgent", "high", "medium", "low", "none"],
                        "description": "Priority level.",
                    },
                },
                "required": ["issue_id", "priority"],
            },
        ),
        Tool(
            name="plane_set_assignee",
            description="Assign a Plane issue to a user UUID (typically amdkn777).",
            inputSchema={
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string", "description": "Plane issue UUID."},
                    "assignee_id": {"type": "string", "description": "User UUID (Plane member). amdkn777 = default."},
                },
                "required": ["issue_id", "assignee_id"],
            },
        ),
        Tool(
            name="plane_set_labels",
            description="Set labels on a Plane issue (e.g. ['12WY-W3', 'domain:GTD', '@L1']).",
            inputSchema={
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string", "description": "Plane issue UUID."},
                    "labels": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Labels to set (replaces existing).",
                    },
                },
                "required": ["issue_id", "labels"],
            },
        ),
        Tool(
            name="plane_add_parent",
            description="Add a parent to an existing issue retroactively (sub-work item → Rock canon link).",
            inputSchema={
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string", "description": "Sub-work item UUID (child)."},
                    "parent_id": {"type": "string", "description": "Parent issue UUID (Rock canon)."},
                },
                "required": ["issue_id", "parent_id"],
            },
        ),
        Tool(
            name="plane_archive_issue",
            description="Archive a Plane issue by transitioning it to Cancelled state (D7 cost-of-escalation: archive, never delete).",
            inputSchema={
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string", "description": "Plane issue UUID."},
                },
                "required": ["issue_id"],
            },
        ),
        Tool(
            name="plane_create_module",
            description="Create a Module in Plane project (group sub-work items / Rocks canon under one umbrella).",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Module name (e.g. '12WY Cycle Q3 2026')."},
                    "description": {"type": "string", "description": "Module description (Markdown).", "default": ""},
                    "start_date": {"type": "string", "description": "ISO 8601 start date (e.g. '2026-06-15').", "default": ""},
                    "target_date": {"type": "string", "description": "ISO 8601 target date (e.g. '2026-09-07').", "default": ""},
                    "status": {
                        "type": "string",
                        "enum": ["backlog", "planned", "in-progress", "paused", "completed", "cancelled"],
                        "description": "Module status (default 'in-progress' for current Q3 2026).",
                        "default": "in-progress",
                    },
                },
                "required": ["name"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    # ---- plane_list_issues -------------------------------------------------
    if name == "plane_list_issues":
        state = arguments.get("state")
        if _live_enabled():
            try:
                issues = await _live_list_issues(state)
                return [
                    TextContent(
                        type="text",
                        text=f"Issues (live, project={PROJECT_ID[:8]}…): {issues}",
                    )
                ]
            except (httpx.HTTPError, ValueError) as exc:
                print(f"[!] plane_list_issues live failed: {exc}", file=sys.stderr)
        return [TextContent(type="text", text=f"Issues (stub): {_stub_issues(state)}")]

    # ---- plane_get_inbox ---------------------------------------------------
    if name == "plane_get_inbox":
        if _live_enabled():
            try:
                issues = await _live_list_issues("Inbox")
                return [TextContent(type="text", text=f"Inbox (live): {issues}")]
            except (httpx.HTTPError, ValueError) as exc:
                print(f"[!] plane_get_inbox live failed: {exc}", file=sys.stderr)
        return [TextContent(type="text", text=f"Inbox (stub): {_stub_issues('Inbox')}")]

    # ---- plane_get_next_actions -------------------------------------------
    if name == "plane_get_next_actions":
        if _live_enabled():
            try:
                issues = await _live_list_issues("Next Actions")
                return [TextContent(type="text", text=f"Next Actions (live): {issues}")]
            except (httpx.HTTPError, ValueError) as exc:
                print(f"[!] plane_get_next_actions live failed: {exc}", file=sys.stderr)
        return [TextContent(type="text", text=f"Next Actions (stub): {_stub_issues('Next Actions')}")]

    # ---- plane_get_today ---------------------------------------------------
    if name == "plane_get_today":
        if _live_enabled():
            try:
                issues = await _live_list_issues("Today")
                return [TextContent(type="text", text=f"Today (live): {issues}")]
            except (httpx.HTTPError, ValueError) as exc:
                print(f"[!] plane_get_today live failed: {exc}", file=sys.stderr)
        return [TextContent(type="text", text=f"Today (stub): {_stub_issues('Today')}")]

    # ---- plane_create_issue ------------------------------------------------
    if name == "plane_create_issue":
        if not API_KEY:
            return [
                TextContent(
                    type="text",
                    text=(
                        "[!] PLANE_API_KEY not set — stub create. "
                        f"name={arguments.get('name')!r} state={arguments.get('state', 'Inbox')!r}"
                    ),
                )
            ]
        if not _live_enabled():
            return [
                TextContent(
                    type="text",
                    text=(
                        "[!] PLANE_PROJECT_ID not set — stub create. "
                        f"name={arguments.get('name')!r} state={arguments.get('state', 'Inbox')!r}"
                    ),
                )
            ]
        try:
            created = await _live_create_issue(
                name=str(arguments.get("name", "Untitled")),
                description=str(arguments.get("description", "")),
                state=str(arguments.get("state", "Inbox")),
                labels=list(arguments.get("labels", [])),
            )
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[+] Issue created (live): id={created.get('id')} "
                        f"sequence_id={created.get('sequence_id')} "
                        f"name={created.get('name')!r}"
                    ),
                )
            ]
        except (httpx.HTTPError, ValueError) as exc:
            print(f"[!] plane_create_issue live failed: {exc}", file=sys.stderr)
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[!] plane_create_issue live failed: {exc}. "
                        f"name={arguments.get('name')!r} state={arguments.get('state', 'Inbox')!r}"
                    ),
                )
            ]

    # ---- plane_update_state ------------------------------------------------
    if name == "plane_update_state":
        issue_id = str(arguments.get("issue_id", ""))
        new_state = str(arguments.get("new_state", ""))
        if not API_KEY:
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[!] PLANE_API_KEY not set — stub update. "
                        f"issue_id={issue_id!r} new_state={new_state!r}"
                    ),
                )
            ]
        if not _live_enabled():
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[!] PLANE_PROJECT_ID not set — stub update. "
                        f"issue_id={issue_id!r} new_state={new_state!r}"
                    ),
                )
            ]
        try:
            updated = await _live_update_state(issue_id, new_state)
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[+] Issue {issue_id} -> {new_state} (live). "
                        f"response_keys={sorted(updated.keys()) if isinstance(updated, dict) else 'non-dict'}"
                    ),
                )
            ]
        except (httpx.HTTPError, ValueError) as exc:
            print(f"[!] plane_update_state live failed: {exc}", file=sys.stderr)
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[!] plane_update_state live failed: {exc}. "
                        f"issue_id={issue_id!r} new_state={new_state!r}"
                    ),
                )
            ]

    # ---- A0 expansion 2026-06-22 : 7 new dispatchers (D4 append-only) -----

    # ---- plane_create_sub_work_item ---------------------------------------
    if name == "plane_create_sub_work_item":
        if not API_KEY or not _live_enabled():
            return [
                TextContent(
                    type="text",
                    text=f"[!] PLANE_API_KEY/PROJECT_ID not set — stub sub-work item. "
                    f"parent_id={arguments.get('parent_id')!r} name={arguments.get('name')!r}",
                )
            ]
        try:
            created = await _live_create_sub_work_item(
                parent_id=str(arguments.get("parent_id", "")),
                name=str(arguments.get("name", "Untitled sub-work item")),
                description=str(arguments.get("description", "")),
                state=str(arguments.get("state", "Today")),
            )
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[+] Sub-work item created (live): id={created.get('id')} "
                        f"parent_id={arguments.get('parent_id')!r} "
                        f"name={created.get('name')!r}"
                    ),
                )
            ]
        except (httpx.HTTPError, ValueError) as exc:
            print(f"[!] plane_create_sub_work_item live failed: {exc}", file=sys.stderr)
            return [TextContent(type="text", text=f"[!] plane_create_sub_work_item live failed: {exc}")]

    # ---- plane_set_priority -----------------------------------------------
    if name == "plane_set_priority":
        if not API_KEY or not _live_enabled():
            return [TextContent(type="text", text=f"[!] stub set_priority. issue_id={arguments.get('issue_id')!r}")]
        try:
            updated = await _live_set_priority(
                issue_id=str(arguments.get("issue_id", "")),
                priority=str(arguments.get("priority", "none")),
            )
            return [TextContent(type="text", text=f"[+] Priority set (live). issue_id={arguments.get('issue_id')!r}")]
        except (httpx.HTTPError, ValueError) as exc:
            return [TextContent(type="text", text=f"[!] plane_set_priority live failed: {exc}")]

    # ---- plane_set_assignee ----------------------------------------------
    if name == "plane_set_assignee":
        if not API_KEY or not _live_enabled():
            return [TextContent(type="text", text=f"[!] stub set_assignee. issue_id={arguments.get('issue_id')!r}")]
        try:
            await _live_set_assignee(
                issue_id=str(arguments.get("issue_id", "")),
                assignee_id=str(arguments.get("assignee_id", "")),
            )
            return [TextContent(type="text", text=f"[+] Assignee set (live). issue_id={arguments.get('issue_id')!r}")]
        except (httpx.HTTPError, ValueError) as exc:
            return [TextContent(type="text", text=f"[!] plane_set_assignee live failed: {exc}")]

    # ---- plane_set_labels -------------------------------------------------
    if name == "plane_set_labels":
        if not API_KEY or not _live_enabled():
            return [TextContent(type="text", text=f"[!] stub set_labels. issue_id={arguments.get('issue_id')!r}")]
        try:
            await _live_set_labels(
                issue_id=str(arguments.get("issue_id", "")),
                labels=list(arguments.get("labels", [])),
            )
            return [TextContent(type="text", text=f"[+] Labels set (live). issue_id={arguments.get('issue_id')!r} labels={arguments.get('labels')!r}")]
        except (httpx.HTTPError, ValueError) as exc:
            return [TextContent(type="text", text=f"[!] plane_set_labels live failed: {exc}")]

    # ---- plane_add_parent -------------------------------------------------
    if name == "plane_add_parent":
        if not API_KEY or not _live_enabled():
            return [TextContent(type="text", text=f"[!] stub add_parent. issue_id={arguments.get('issue_id')!r}")]
        try:
            await _live_add_parent(
                issue_id=str(arguments.get("issue_id", "")),
                parent_id=str(arguments.get("parent_id", "")),
            )
            return [TextContent(type="text", text=f"[+] Parent set (live). issue_id={arguments.get('issue_id')!r} parent_id={arguments.get('parent_id')!r}")]
        except (httpx.HTTPError, ValueError) as exc:
            return [TextContent(type="text", text=f"[!] plane_add_parent live failed: {exc}")]

    # ---- plane_archive_issue ----------------------------------------------
    if name == "plane_archive_issue":
        if not API_KEY or not _live_enabled():
            return [TextContent(type="text", text=f"[!] stub archive. issue_id={arguments.get('issue_id')!r}")]
        try:
            await _live_archive_issue(issue_id=str(arguments.get("issue_id", "")))
            return [TextContent(type="text", text=f"[+] Issue archived (Cancelled state, live). issue_id={arguments.get('issue_id')!r}")]
        except (httpx.HTTPError, ValueError) as exc:
            return [TextContent(type="text", text=f"[!] plane_archive_issue live failed: {exc}")]

    # ---- plane_create_module ----------------------------------------------
    if name == "plane_create_module":
        if not API_KEY or not _live_enabled():
            return [TextContent(type="text", text=f"[!] stub create_module. name={arguments.get('name')!r}")]
        try:
            created = await _live_create_module(
                name=str(arguments.get("name", "Untitled module")),
                description=str(arguments.get("description", "")),
                start_date=str(arguments.get("start_date", "")),
                target_date=str(arguments.get("target_date", "")),
                status=str(arguments.get("status", "in-progress")),
            )
            return [
                TextContent(
                    type="text",
                    text=(
                        f"[+] Module created (live): id={created.get('id')} "
                        f"name={created.get('name')!r}"
                    ),
                )
            ]
        except (httpx.HTTPError, ValueError) as exc:
            return [TextContent(type="text", text=f"[!] plane_create_module live failed: {exc}")]

    raise ValueError(f"Unknown tool: {name}")


async def main() -> None:
    mode = "LIVE" if _live_enabled() else "STUB"
    print(
        f"[+] Plane MCP server starting (Symphony Lane B / GTD) "
        f"mode={mode} workspace={WORKSPACE_SLUG} project_id={PROJECT_ID or '(unset)'}",
        file=sys.stderr,
    )
    if mode == "LIVE":
        # Pre-warm the state map so the first tool call is fast (and so a
        # misconfigured project surfaces immediately at startup, not on the
        # first request — D6 root-cause visibility).
        mapping = await _load_state_map()
        print(
            f"[+] State map loaded: {len(mapping)} states "
            f"({sorted(mapping.keys())})",
            file=sys.stderr,
        )
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
