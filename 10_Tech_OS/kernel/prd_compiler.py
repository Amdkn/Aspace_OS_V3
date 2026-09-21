#!/usr/bin/env python3
import re
import argparse
import sys
from typing import Dict, List

REQUIRED_SECTIONS = [
    "Scope",
    "Owner",
    "Dependencies",
    "Acceptance",
    "Evidence",
    "Exclusive Files"
]

def compile_prd(raw_text: str) -> str:
    """
    Compiles a raw Linear mandate text into a structured, bounded PRD.
    Enforces the inclusion of required sections and assigns default roles.
    """
    sections_found: Dict[str, str] = {}
    current_section = None
    current_content: List[str] = []

    req_map = {req.lower(): req for req in REQUIRED_SECTIONS}

    # Regex to match a line that starts with optional '#' or '-',
    # then one of the required sections, then optional ':'
    pattern = r'^(?:#+|-)?\s*(' + '|'.join(REQUIRED_SECTIONS) + r')\s*:?\s*$'
    pattern_re = re.compile(pattern, re.IGNORECASE)

    for line in raw_text.split("\n"):
        match = pattern_re.match(line)
        if match:
            if current_section:
                sections_found[current_section] = "\n".join(current_content).strip()
            # Normalize to standard case
            matched_text = match.group(1).strip().lower()
            current_section = req_map[matched_text]
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        sections_found[current_section] = "\n".join(current_content).strip()

    missing = [req for req in REQUIRED_SECTIONS if req not in sections_found]
    if missing:
        raise ValueError(f"Missing required sections: {', '.join(missing)}")

    lines = [
        "# Bounded PRD",
        "",
        "**Primary Spec**: Clara",
        "**Mechanism Gatekeeper**: Rick",
        ""
    ]

    for req in REQUIRED_SECTIONS:
        lines.append(f"## {req}")
        lines.append(sections_found[req])
        lines.append("")

    return "\n".join(lines).strip()

def main():
    parser = argparse.ArgumentParser(description="Compile a raw Linear mandate into a bounded PRD.")
    parser.add_argument("input_file", help="Path to the raw mandate text file.")
    parser.add_argument("output_file", help="Path to write the bounded PRD Markdown file.")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            raw_text = f.read()
    except Exception as e:
        print(f"Error reading {args.input_file}: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        compiled_prd = compile_prd(raw_text)
    except ValueError as e:
        print(f"Error compiling PRD: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(compiled_prd + "\n")
    except Exception as e:
        print(f"Error writing {args.output_file}: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Successfully compiled {args.input_file} to {args.output_file}")

if __name__ == "__main__":
    main()
