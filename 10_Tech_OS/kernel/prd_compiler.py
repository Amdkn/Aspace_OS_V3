#!/usr/bin/env python3
import argparse
import sys
import os
import re

def parse_section(text, section_names):
    """
    Attempts to find the content of a section.
    Matches either:
    1. A markdown heading like `## SectionName` or `# SectionName` followed by its content until the next heading.
    2. A line starting with `SectionName:` followed by its content until the next known section key or empty line.
    """

    # Try finding markdown heading first
    for name in section_names:
        # Match ## Name, # Name, or ### Name
        pattern = re.compile(r'^#{1,3}\s*' + re.escape(name) + r'\s*\n(.*?)(?=^#{1,3}\s|\Z)', re.MULTILINE | re.IGNORECASE | re.DOTALL)
        match = pattern.search(text)
        if match:
            return match.group(1).strip()

    # Try finding inline key-value or block
    for name in section_names:
        pattern = re.compile(r'^' + re.escape(name) + r':\s*(.*?)(?=^[A-Z][a-zA-Z\s]+:|\Z)', re.MULTILINE | re.IGNORECASE | re.DOTALL)
        match = pattern.search(text)
        if match:
            return match.group(1).strip()

    return "TBD"


def compile_prd(mandate_text):
    """Compiles a raw text mandate into a bounded PRD in Markdown format."""

    scope_str = parse_section(mandate_text, ["Scope"])
    owner_str = parse_section(mandate_text, ["Owner", "Assignee"])
    deps_str = parse_section(mandate_text, ["Dependencies", "Depends On"])
    acc_str = parse_section(mandate_text, ["Acceptance Criteria", "Acceptance"])
    evidence_str = parse_section(mandate_text, ["Evidence"])
    files_str = parse_section(mandate_text, ["Exclusive Files", "Files"])

    prd = f"""# Bounded PRD

## Scope
{scope_str}

## Owner
Owner: {owner_str}
Primary Spec: Clara
Gatekeeper: Rick

## Dependencies
{deps_str}

## Acceptance Criteria
{acc_str}

## Evidence
{evidence_str}

## Exclusive Files
{files_str}
"""
    return prd

def main():
    parser = argparse.ArgumentParser(description="Compile a raw Linear mandate into a bounded PRD.")
    parser.add_argument("--mandate-file", "-f", required=True, help="Path to the input raw mandate text file.")
    parser.add_argument("--out-file", "-o", required=True, help="Path to the output Markdown PRD file.")

    args = parser.parse_args()

    if not os.path.exists(args.mandate_file):
        print(f"Error: Mandate file not found: {args.mandate_file}", file=sys.stderr)
        sys.exit(1)

    with open(args.mandate_file, "r", encoding="utf-8") as f:
        mandate_text = f.read()

    prd_content = compile_prd(mandate_text)

    with open(args.out_file, "w", encoding="utf-8") as f:
        f.write(prd_content)

    print(f"PRD compiled successfully to {args.out_file}")

if __name__ == "__main__":
    main()
