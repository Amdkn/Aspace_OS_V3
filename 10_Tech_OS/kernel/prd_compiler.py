import argparse
import os
import re
import sys
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
    sections = {}
    current_section = None
    current_content = []

    for line in text.splitlines():
        line_stripped = line.strip()
        matched_section = None
        for req in REQUIRED_SECTIONS:
            # Match variations like "Scope:", "### Scope", "Scope :"
            pattern = rf'^(?:#+\s*)?{re.escape(req)}\s*[:-]?\s*(.*)$'
            match = re.match(pattern, line_stripped, re.IGNORECASE)
            if match:
                matched_section = req
                remainder = match.group(1).strip()
                break

        if matched_section:
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = matched_section
            current_content = []
            if remainder:
                current_content.append(remainder)
        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    missing = [req for req in REQUIRED_SECTIONS if req not in sections or not sections[req]]
    if missing:
        raise ValueError(f"Missing required sections: {', '.join(missing)}")

    return sections

def compile_prd(mandate_id: str, forge_group: str, raw_text: str, output_base_dir: str = "10_Tech_OS/PRD_Autonomy") -> str:
    sections = parse_mandate(raw_text)

    prd_content = f"""# PRD: {mandate_id}

## Primary Spec
Clara

## Gatekeeper
Rick

## Scope
{sections['Scope']}

## Owner
{sections['Owner']}

## Dependencies
{sections['Dependencies']}

## Acceptance
{sections['Acceptance']}

## Evidence
{sections['Evidence']}

## Exclusive Files
{sections['Exclusive Files']}
"""
    output_dir = os.path.join(output_base_dir, forge_group)
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{mandate_id}.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(prd_content)

    return file_path

def main():
    parser = argparse.ArgumentParser(description="Deterministic PRD Compiler")
    parser.add_argument("--mandate-id", required=True, help="Mandate ID (e.g., FPRD-001_FOR-4)")
    parser.add_argument("--forge-group", required=True, help="Forge Group (e.g., FORGE_F0)")
    parser.add_argument("--input", required=True, help="Path to raw mandate text file")
    parser.add_argument("--output-dir", default="10_Tech_OS/PRD_Autonomy", help="Base output directory")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        raw_text = f.read()

    try:
        out_path = compile_prd(args.mandate_id, args.forge_group, raw_text, args.output_dir)
        print(f"Successfully compiled PRD to {out_path}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
