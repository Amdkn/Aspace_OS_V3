#!/usr/bin/env python3
"""prd_compiler.py — Compiles Linear mandate text into a bounded PRD.

This script acts deterministically (no LLM) to parse raw text and format
it into a structured PRD Markdown file, enforcing required fields and
automatically assigning Clara (Spec) and Rick (Gatekeeper).
"""

import argparse
import re
import sys
from typing import Dict, List

REQUIRED_FIELDS = [
    "Scope",
    "Owner",
    "Dependencies",
    "Acceptance",
    "Evidence",
    "Exclusive Files"
]

def parse_mandate(text: str) -> Dict[str, str]:
    """Parses the raw mandate text to extract required fields."""
    parsed: Dict[str, List[str]] = {}
    current_field = None

    lines = text.splitlines()

    for line in lines:
        matched = False
        for field in REQUIRED_FIELDS:
            # Match field names at the beginning of the line, case-insensitive, with optional markdown syntax
            # It handles things like "**Scope**:", "Scope:", "## Scope", etc.
            match = re.match(rf"^(?:\*\*|### |## |# )?(?i:{field})(?:\*\*|:)?\s*[:\s]?\s*(.*)", line)
            if match:
                current_field = field
                content = match.group(1).strip()
                # Clean up any trailing colons if it accidentally captured them
                if content.startswith(":"):
                     content = content[1:].strip()
                parsed[current_field] = [content] if content else []
                matched = True
                break

        if not matched and current_field:
            parsed[current_field].append(line)

    # Clean up parsed text
    result: Dict[str, str] = {}
    for k, v in parsed.items():
        result[k] = "\n".join(v).strip()

    return result

def compile_prd(mandate_text: str) -> str:
    """Compiles parsed mandate text into a PRD Markdown string."""
    parsed_fields = parse_mandate(mandate_text)

    missing_fields = [f for f in REQUIRED_FIELDS if f not in parsed_fields or not parsed_fields[f]]
    if missing_fields:
        raise ValueError(f"Missing required fields in mandate: {', '.join(missing_fields)}")

    markdown = []
    markdown.append("# Bounded PRD\n")
    markdown.append("## Metadata\n")
    markdown.append("- **Primary Spec:** Clara")
    markdown.append("- **Gatekeeper:** Rick")
    markdown.append(f"- **Owner:** {parsed_fields['Owner']}\n")

    for field in REQUIRED_FIELDS:
        if field == "Owner":
            continue
        markdown.append(f"## {field}\n")
        markdown.append(f"{parsed_fields[field]}\n")

    return "\n".join(markdown).strip() + "\n"

def main():
    parser = argparse.ArgumentParser(description="Compile Linear mandate into a bounded PRD.")
    parser.add_argument("input", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="Input raw mandate file (default: stdin)")
    parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout, help="Output PRD file (default: stdout)")

    args = parser.parse_args()

    try:
        text = args.input.read()
        prd = compile_prd(text)
        args.output.write(prd)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
