#!/usr/bin/env python3
import argparse
import sys
import re
from pathlib import Path

def compile_prd(raw_text: str) -> str:
    """
    Compiles a raw Linear mandate text into a structured, bounded Markdown PRD.
    Enforces the inclusion of Scope, Owner, Dependencies, Acceptance, Evidence,
    and Exclusive Files.
    Automatically assigns Clara as Primary Spec and Rick as Gatekeeper.
    """

    sections_to_extract = ["Scope", "Owner", "Dependencies", "Acceptance", "Evidence", "Exclusive Files"]
    sections_content = {k: "Not specified" for k in sections_to_extract}

    lines = raw_text.splitlines()
    current_section = None
    current_content = []

    for line in lines:
        stripped = line.strip()
        found_section = False
        for sec in sections_to_extract:
            if stripped.lower().startswith(sec.lower() + ":"):
                if current_section:
                    sections_content[current_section] = "\n".join(current_content).strip()
                current_section = sec
                current_content = [stripped[len(sec)+1:].strip()]
                found_section = True
                break

        if not found_section and current_section:
            current_content.append(line)

    if current_section:
        sections_content[current_section] = "\n".join(current_content).strip()

    for k, v in sections_content.items():
        if not v:
            sections_content[k] = "Not specified"

    prd = [
        "# Bounded PRD",
        "",
        "## Roles",
        "- **Primary Spec**: Clara",
        "- **Gatekeeper**: Rick",
        "",
        "## Scope",
        sections_content["Scope"],
        "",
        "## Owner",
        sections_content["Owner"],
        "",
        "## Dependencies",
        sections_content["Dependencies"],
        "",
        "## Acceptance",
        sections_content["Acceptance"],
        "",
        "## Evidence",
        sections_content["Evidence"],
        "",
        "## Exclusive Files",
        sections_content["Exclusive Files"]
    ]

    return "\n".join(prd) + "\n"

def main():
    parser = argparse.ArgumentParser(description="Compile raw Linear mandate into bounded PRD.")
    parser.add_argument("input_file", help="Path to raw Linear mandate text file")
    parser.add_argument("output_file", help="Path to output markdown PRD file")

    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    raw_text = input_path.read_text(encoding="utf-8")
    prd_content = compile_prd(raw_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(prd_content, encoding="utf-8")
    print(f"Compiled PRD saved to {output_path}")

if __name__ == "__main__":
    main()
