#!/usr/bin/env python3
"""
prd_compiler.py — Compiles a raw Linear mandate into a bounded PRD.
Enforces inclusion of Scope, Owner, Dependencies, Acceptance, Evidence, and Exclusive Files.
Automatically assigns Clara as Primary Spec and Rick as Gatekeeper.
"""

import sys
from pathlib import Path
from typing import Dict

REQUIRED_SECTIONS = [
    "Scope",
    "Owner",
    "Dependencies",
    "Acceptance",
    "Evidence",
    "Exclusive Files"
]

def parse_mandate(text: str) -> Dict[str, str]:
    """Parses raw text into sections."""
    parsed = {sec: "" for sec in REQUIRED_SECTIONS}

    current_section = "Scope"

    for line in text.split('\n'):
        line_stripped = line.strip()
        lower_line = line_stripped.lower()

        matched_section = None
        for sec in REQUIRED_SECTIONS:
            # Match headers like "Scope:", "## Scope", "- Scope:"
            if lower_line.startswith(sec.lower() + ":") or \
               lower_line.startswith("## " + sec.lower()) or \
               lower_line.startswith("- " + sec.lower() + ":"):
                matched_section = sec
                break

        if matched_section:
            current_section = matched_section

            # Remove header from line
            if lower_line.startswith(matched_section.lower() + ":"):
                line = line_stripped[len(matched_section)+1:].strip()
            elif lower_line.startswith("- " + matched_section.lower() + ":"):
                line = line_stripped[len(matched_section)+3:].strip()
            else:
                line = "" # It was a ## Header

        if line.strip():
            if parsed[current_section]:
                parsed[current_section] += "\n" + line
            else:
                parsed[current_section] = line

    return parsed

def compile_prd(raw_text: str, title: str = "Bounded PRD") -> str:
    """Compiles parsed mandate into formatted PRD markdown."""
    parsed = parse_mandate(raw_text)

    # Enforce assignments
    parsed["Owner"] = "Clara (Primary Spec), Rick (Gatekeeper)"

    # Provide defaults for empty sections to enforce inclusion
    for sec in REQUIRED_SECTIONS:
        if not parsed[sec].strip() and sec != "Owner":
            parsed[sec] = "None specified."

    lines = [f"# {title}", ""]

    for sec in REQUIRED_SECTIONS:
        lines.append(f"## {sec}")
        lines.append(parsed[sec].strip())
        lines.append("")

    return "\n".join(lines).strip() + "\n"

def main():
    if len(sys.argv) < 2:
        print("Usage: prd_compiler.py <input_file> [output_file]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: {input_path} does not exist.")
        sys.exit(1)

    raw_text = input_path.read_text(encoding='utf-8')
    title = f"PRD: {input_path.stem}"
    compiled = compile_prd(raw_text, title=title)

    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
        output_path.write_text(compiled, encoding='utf-8')
        print(f"Compiled PRD saved to {output_path}")
    else:
        print(compiled)

if __name__ == "__main__":
    main()
