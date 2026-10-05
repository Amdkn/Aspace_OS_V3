#!/usr/bin/env python3
"""A'Space GitHub App System-One permission compiler.

Deterministic responsibilities:
- compile authority profiles into GitHub App manifests;
- explain effective permissions with deny-by-default semantics;
- generate a minimal registration form for GitHub's manifest flow;
- compute current -> desired reconciliation plans for existing Apps;
- never auto-widen or auto-apply permissions.

Actual GitHub UI/API mutation remains an external effect. This compiler only
authorizes a plan after explicit human approval; an executor must consume that
approved plan separately and verify the resulting live App state.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "10_Tech_OS" / "github_app_system1" / "authority_profiles.json"
HOMEPAGE = "https://github.com/Amdkn/Aspace_OS_V3"
MANIFEST_CALLBACK = "http://127.0.0.1:5555/github-app-manifest/callback"
VALID_LEVELS = {"read", "write", "admin"}
LEVEL_RANK = {"none": 0, "read": 1, "write": 2, "admin": 3}

# Human-facing permission catalog used for explanations.
# Every row omitted by a profile resolves to No access.
CATALOG = [
    "actions",
    "administration",
    "checks",
    "contents",
    "discussions",
    "issues",
    "metadata",
    "pull_requests",
    "repository_projects",
    "secrets",
    "statuses",
    "variables",
    "webhooks",
    "workflows",
]


class ApprovalRequired(RuntimeError):
    """Raised when an existing-App reconciliation lacks explicit approval."""


def load_profiles() -> dict:
    return json.loads(PROFILES.read_text(encoding="utf-8"))


def get_profile(name: str) -> tuple[dict, dict]:
    doc = load_profiles()
    try:
        return doc["defaults"], doc["profiles"][name]
    except KeyError as exc:
        raise SystemExit(f"Unknown profile: {name}") from exc


def validate(profile_name: str, defaults: dict, profile: dict) -> None:
    perms = profile.get("permissions", {})
    for key, level in perms.items():
        if level not in VALID_LEVELS:
            raise SystemExit(f"{profile_name}: invalid level {key}={level}")

    forbidden = set(defaults.get("forbidden_without_explicit_exception", []))
    bad = sorted(forbidden.intersection(perms))
    if bad:
        raise SystemExit(
            f"{profile_name}: forbidden permissions require explicit exception: {bad}"
        )


def effective_level(permission: str, profile: dict) -> str:
    if permission == "metadata":
        return "read (GitHub mandatory)"
    return profile.get("permissions", {}).get(permission, "none")


def canonical_level(permission: str, profile: dict) -> str:
    """Machine-comparable permission level."""
    if permission == "metadata":
        return "read"
    return profile.get("permissions", {}).get(permission, "none")


def manifest(profile_name: str) -> dict:
    defaults, profile = get_profile(profile_name)
    validate(profile_name, defaults, profile)

    out = {
        "name": profile["name"],
        "url": HOMEPAGE,
        "description": profile["description"],
        "public": defaults.get("public", False),
        "redirect_url": MANIFEST_CALLBACK,
        "default_permissions": profile.get("permissions", {}),
        "default_events": profile.get("events", []),
        "request_oauth_on_install": profile.get("request_oauth_on_install", False),
    }
    callback_urls = profile.get("callback_urls")
    if callback_urls:
        out["callback_urls"] = callback_urls

    # Webhooks are intentionally inactive until a sovereign HTTPS endpoint exists.
    out["hook_attributes"] = {
        "url": "https://gateway.invalid/github/events",
        "active": bool(defaults.get("webhook_active", False)),
    }
    return out


def desired_state(profile_name: str) -> dict:
    defaults, profile = get_profile(profile_name)
    validate(profile_name, defaults, profile)
    return {
        "permissions": {perm: canonical_level(perm, profile) for perm in CATALOG},
        "events": sorted(profile.get("events", [])),
        "request_oauth_on_install": bool(profile.get("request_oauth_on_install", False)),
        "webhook_active": bool(defaults.get("webhook_active", False)),
    }


def _normalize_current(current: dict) -> dict:
    permissions = current.get("permissions", {})
    unknown_permissions = sorted(set(permissions) - set(CATALOG))
    if unknown_permissions:
        raise ValueError(f"unknown current permissions: {unknown_permissions}")

    normalized_permissions = {}
    for permission in CATALOG:
        level = permissions.get(permission, "none")
        if level not in LEVEL_RANK:
            raise ValueError(f"invalid current level {permission}={level}")
        normalized_permissions[permission] = level

    # GitHub metadata is mandatory read. A snapshot that says none is stale or invalid.
    if normalized_permissions["metadata"] == "none":
        normalized_permissions["metadata"] = "read"

    return {
        "permissions": normalized_permissions,
        "events": sorted(set(current.get("events", []))),
        "request_oauth_on_install": bool(current.get("request_oauth_on_install", False)),
        "webhook_active": bool(current.get("webhook_active", False)),
    }


def reconciliation_plan(profile_name: str, current: dict) -> dict:
    """Compute deterministic current -> desired delta without applying anything."""
    current_norm = _normalize_current(current)
    desired = desired_state(profile_name)
    changes = []

    for permission in CATALOG:
        before = current_norm["permissions"][permission]
        after = desired["permissions"][permission]
        if before == after:
            continue
        changes.append(
            {
                "kind": "permission",
                "permission": permission,
                "current": before,
                "desired": after,
                "direction": (
                    "widen"
                    if LEVEL_RANK[after] > LEVEL_RANK[before]
                    else "narrow"
                ),
            }
        )

    for field in ("events", "request_oauth_on_install", "webhook_active"):
        before = current_norm[field]
        after = desired[field]
        if before != after:
            changes.append(
                {
                    "kind": "setting",
                    "setting": field,
                    "current": before,
                    "desired": after,
                    "direction": "change",
                }
            )

    return {
        "schema": "aspace.github-app-reconciliation-plan.v1",
        "profile": profile_name,
        "current": current_norm,
        "desired": desired,
        "changes": changes,
        "requires_explicit_approval": bool(changes),
        "contains_permission_widening": any(
            change.get("direction") == "widen" for change in changes
        ),
        "approved": False,
        "execution_authorized": False,
    }


def approve_reconciliation(plan: dict, *, approved: bool) -> dict:
    """Return an executor-consumable plan only after explicit approval."""
    out = json.loads(json.dumps(plan))
    if not out.get("changes"):
        out["approved"] = True
        out["execution_authorized"] = False
        out["reason"] = "no changes required"
        return out
    if not approved:
        raise ApprovalRequired("explicit human approval required before reconciliation")
    out["approved"] = True
    out["execution_authorized"] = True
    out["reason"] = "explicit approval recorded; external executor may apply exact delta"
    return out


def markdown_matrix() -> str:
    doc = load_profiles()
    names = list(doc["profiles"])
    header = ["Permission", *names]
    rows = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    for perm in CATALOG:
        cells = [perm]
        for name in names:
            profile = doc["profiles"][name]
            cells.append(effective_level(perm, profile))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def registration_form(profile_name: str) -> str:
    payload = json.dumps(manifest(profile_name), separators=(",", ":"))
    return f"""<!doctype html>
<meta charset="utf-8">
<title>A'Space GitHub App Manifest — {html.escape(profile_name)}</title>
<h1>A'Space GitHub App Manifest — {html.escape(profile_name)}</h1>
<p>Review the compiled authority profile, then submit to GitHub.</p>
<pre>{html.escape(json.dumps(manifest(profile_name), indent=2))}</pre>
<form action="https://github.com/settings/apps/new" method="post">
  <input type="hidden" name="manifest" value="{html.escape(payload, quote=True)}">
  <button type="submit">Register preconfigured GitHub App</button>
</form>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_manifest = sub.add_parser("manifest")
    p_manifest.add_argument("profile", choices=["gateway", "a0", "s1", "s2", "s3"])

    p_explain = sub.add_parser("explain")
    p_explain.add_argument("profile", nargs="?", choices=["gateway", "a0", "s1", "s2", "s3"])

    p_form = sub.add_parser("form")
    p_form.add_argument("profile", choices=["gateway", "a0", "s1", "s2", "s3"])
    p_form.add_argument("--out", type=Path)

    p_reconcile = sub.add_parser("reconcile")
    p_reconcile.add_argument("profile", choices=["gateway", "a0", "s1", "s2", "s3"])
    p_reconcile.add_argument("--current", required=True, type=Path)
    p_reconcile.add_argument(
        "--approve",
        action="store_true",
        help="Explicitly authorize the exact emitted delta for an external executor.",
    )

    args = parser.parse_args()

    if args.cmd == "manifest":
        print(json.dumps(manifest(args.profile), indent=2))
        return 0

    if args.cmd == "explain":
        if args.profile:
            defaults, profile = get_profile(args.profile)
            validate(args.profile, defaults, profile)
            print(f"# {profile['name']}")
            for perm in CATALOG:
                print(f"{perm}: {effective_level(perm, profile)}")
        else:
            print(markdown_matrix())
        return 0

    if args.cmd == "form":
        page = registration_form(args.profile)
        if args.out:
            args.out.write_text(page, encoding="utf-8")
            print(args.out)
        else:
            print(page)
        return 0

    if args.cmd == "reconcile":
        current = json.loads(args.current.read_text(encoding="utf-8"))
        plan = reconciliation_plan(args.profile, current)
        if args.approve:
            plan = approve_reconciliation(plan, approved=True)
        print(json.dumps(plan, indent=2))
        return 0

    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())
