#!/usr/bin/env python3
"""Advisory GitHub Operating Model coach.

M0 behavior: emit teaching notices and warnings, never fail the workflow.
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def emit(kind: str, message: str) -> None:
    print(f"::{kind}::{message}")


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("No GitHub event payload available.")
        return 0

    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    pr = event.get("pull_request") or {}
    title = str(pr.get("title") or "")
    body = str(pr.get("body") or "")
    head = str(((pr.get("head") or {}).get("ref")) or "")
    base = str(((pr.get("base") or {}).get("ref")) or "")

    notices = [
        "Pull Request = mutation proposal. Merge integrates code; it does not prove deployment.",
        "CI green = tested integration conditions only; runtime health requires runtime observation.",
        "Every mission branch should have a closure path: merge/supersede/salvage, then branch/worktree retirement.",
    ]
    for notice in notices:
        emit("notice", notice)

    warnings: list[str] = []
    if not body.strip():
        warnings.append("PR body is empty; document mission, mutation, evidence, recovery, and continuation.")
    if base == "main" and head == "main":
        warnings.append("PR head is main; normal A'Space development should use a bounded mission branch.")
    if body and "return-to" not in body.lower() and "return_to" not in body.lower():
        warnings.append("No explicit return_to detected in PR body.")
    if body and "evidence" not in body.lower():
        warnings.append("No explicit evidence section detected in PR body.")
    if body and not any(token in body.lower() for token in ("rollback", "recovery", "compensation", "unknown")):
        warnings.append("No failure/recovery/rollback language detected in PR body.")

    for warning in warnings:
        emit("warning", warning)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        lines = [
            "# A'Space GitHub Operating Model — advisory",
            "",
            f"- PR: **{title or '(untitled)'}**",
            f"- Head: `{head or '?'}`",
            f"- Base: `{base or '?'}`",
            "",
            "## Concept",
            "",
            "This workflow is **M0 advisory only**. It does not block the PR.",
            "",
            "- PR = proposed mutation.",
            "- CI = evidence for integration acceptance.",
            "- Merge = integration into the base branch.",
            "- CD/deployment = separate promotion step.",
            "- Runtime health = separate observed truth.",
            "",
            "## Advisory findings",
            "",
        ]
        if warnings:
            lines.extend([f"- ⚠️ {w}" for w in warnings])
        else:
            lines.append("- ✅ No basic operating-model warning detected.")
        Path(summary).write_text("\n".join(lines) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
