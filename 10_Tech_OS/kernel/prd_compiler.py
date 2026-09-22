#!/usr/bin/env python3
"""prd_compiler.py — Compilateur déterministe de mandats Linear en PRD borné.

Usage: python3 prd_compiler.py --file <path> --issue_id <id> --forge_group <group>
"""
import argparse
import re
from pathlib import Path
import sys

def parse_mandate(text: str) -> dict:
    sections = {
        "Scope": "",
        "Dependencies": "",
        "Acceptance": "",
        "Evidence": "",
        "Exclusive Files": ""
    }

    current_section = None
    lines = text.splitlines()

    section_map = {
        "scope": "Scope",
        "dependencies": "Dependencies",
        "acceptance": "Acceptance",
        "evidence": "Evidence",
        "exclusive files": "Exclusive Files",
        "exclusive_files": "Exclusive Files"
    }

    parsed_content = {k: [] for k in sections.keys()}

    for line in lines:
        matched = False

        # Check if line is a header like "Scope:" or "## Scope"
        header_match = re.match(r'^(?:\#+\s*)?([a-zA-Z_ ]+)\s*:?$', line.strip())
        if header_match:
            candidate = header_match.group(1).strip().lower()
            if candidate in section_map:
                current_section = section_map[candidate]
                matched = True

        # Or check inline like "**Scope:** content"
        inline_match = re.match(r'^[*_\s]*([a-zA-Z_ ]+?)[*_\s]*:\s*[*_\s]*(.*)$', line.strip())
        if inline_match and not matched:
            candidate = inline_match.group(1).strip().lower()
            if candidate in section_map:
                current_section = section_map[candidate]
                if inline_match.group(2).strip():
                    parsed_content[current_section].append(inline_match.group(2).strip())
                matched = True

        if not matched and current_section:
            parsed_content[current_section].append(line)

    for k in sections:
        # cleanup empty lines at start and end
        content_str = "\n".join(parsed_content[k]).strip()
        sections[k] = content_str

    # If nothing was parsed into sections, maybe just put everything in Scope
    if all(not v for v in sections.values()):
        sections["Scope"] = text.strip()

    return sections

def generate_prd(issue_id, sections):
    owner = "Clara (Primary Spec) / Rick (Mechanism Gatekeeper)"

    prd = f"# PRD: {issue_id}\n\n"
    prd += "## Owner\n"
    prd += f"{owner}\n\n"

    for section in ["Scope", "Dependencies", "Acceptance", "Evidence", "Exclusive Files"]:
        prd += f"## {section}\n"
        content = sections.get(section, "")
        if content:
            prd += f"{content}\n\n"
        else:
            prd += "None specified.\n\n"

    return prd.strip() + "\n"

def main():
    parser = argparse.ArgumentParser(description="Compile raw Linear mandate into bounded PRD.")
    parser.add_argument("--file", required=True, help="Path to raw Linear mandate file")
    parser.add_argument("--issue_id", required=True, help="Linear Issue ID (e.g., FPRD-001_FOR-4)")
    parser.add_argument("--forge_group", required=True, help="Forge Group (e.g., FORGE_F0)")

    args = parser.parse_args()

    input_file = Path(args.file)
    if not input_file.exists():
        print(f"Error: File {args.file} not found.", file=sys.stderr)
        sys.exit(1)

    raw_text = input_file.read_text(encoding="utf-8")

    sections = parse_mandate(raw_text)
    prd_content = generate_prd(args.issue_id, sections)

    kernel_dir = Path(__file__).resolve().parent
    root_dir = kernel_dir.parent.parent

    out_dir = root_dir / "10_Tech_OS" / "PRD_Autonomy" / args.forge_group
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / f"{args.issue_id}.md"
    out_file.write_text(prd_content, encoding="utf-8")

    print(f"Bounded PRD compiled successfully: {out_file}")

if __name__ == "__main__":
    main()
