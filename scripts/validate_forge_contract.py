#!/usr/bin/env python3
"""Validate A'Space GitHub Forge continuity contracts."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

MARKER = "<!-- forge-continuity-contract:v2 -->"
SECTIONS = [
    "Mission / return-to",
    "Existing canonical state",
    "Capability / accountable owner",
    "Mutation",
    "Authority / state ownership",
    "Test / evidence",
    "Failure / UNKNOWN / recovery",
    "Continuation / release gate",
]
PLACEHOLDER = re.compile(r"^\s*(?:<!--.*?-->|TBD|TODO|N/?A)?\s*$", re.I | re.S)


def _section_text(body: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        re.M | re.S,
    )
    match = pattern.search(body)
    return match.group(1).strip() if match else ""


def validate(body: str, strict: bool = False) -> list[str]:
    errors: list[str] = []
    if MARKER not in body:
        if strict:
            return [f"missing marker {MARKER}"]
        return []

    for heading in SECTIONS:
        text = _section_text(body, heading)
        visible = re.sub(r"<!--.*?-->", "", text, flags=re.S).strip()
        if not text:
            errors.append(f"missing section: {heading}")
        elif not visible or PLACEHOLDER.match(visible):
            errors.append(f"section has no evidence: {heading}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event")
    parser.add_argument("--body-file")
    parser.add_argument("--body-env")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    body = ""
    strict = args.strict
    if args.event:
        event = json.loads(Path(args.event).read_text(encoding="utf-8"))
        pr = event.get("pull_request") or {}
        body = pr.get("body") or ""
        title = str(pr.get("title") or "")
        strict = strict or title.startswith("[FORGE]")
    elif args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")
    elif args.body_env:
        body = os.environ.get(args.body_env, "")
    else:
        parser.error("one body source is required")

    errors = validate(body, strict=strict)
    if errors:
        print("FORGE_CONTINUITY_CONTRACT_FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FORGE_CONTINUITY_CONTRACT_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
