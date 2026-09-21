#!/usr/bin/env python3
import sys
import os
import argparse

def parse_mandate(content):
    """
    Parses the raw Linear mandate texts into structured bounded sections.
    """
    sections = {
        "scope": [],
        "dependencies": [],
        "acceptance": [],
        "evidence": [],
        "exclusive_files": []
    }

    current_section = "scope" # Default everything to scope until we hit a known header

    for line in content.split('\n'):
        line_stripped = line.strip().lower()

        # Check for headers
        if line.startswith('#'):
            header_text = line.lstrip('#').strip().lower()
            if 'scope' in header_text:
                current_section = 'scope'
                continue
            elif 'dependenc' in header_text:
                current_section = 'dependencies'
                continue
            elif 'acceptance' in header_text:
                current_section = 'acceptance'
                continue
            elif 'evidence' in header_text:
                current_section = 'evidence'
                continue
            elif 'exclusive files' in header_text:
                current_section = 'exclusive_files'
                continue

        # We ignore explicit owner sections as we override them deterministically
        if line.startswith('#') and 'owner' in line.lower():
            current_section = None
            continue

        if current_section:
            sections[current_section].append(line)

    return {
        "scope": "\n".join(sections["scope"]).strip(),
        "dependencies": "\n".join(sections["dependencies"]).strip(),
        "acceptance": "\n".join(sections["acceptance"]).strip(),
        "evidence": "\n".join(sections["evidence"]).strip(),
        "exclusive_files": "\n".join(sections["exclusive_files"]).strip()
    }

def compile_prd(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    parsed = parse_mandate(content)

    # Defaults for missing sections
    scope = parsed['scope'] if parsed['scope'] else "Not explicitly defined."
    dependencies = parsed['dependencies'] if parsed['dependencies'] else "None explicitly defined."
    acceptance = parsed['acceptance'] if parsed['acceptance'] else "Standard acceptance criteria apply."
    evidence = parsed['evidence'] if parsed['evidence'] else "Standard evidence required."
    exclusive_files = parsed['exclusive_files'] if parsed['exclusive_files'] else "None explicitly defined."

    prd = f"""# Bounded PRD

## Scope
{scope}

## Owner
Primary Spec: Clara
Gatekeeper: Rick

## Dependencies
{dependencies}

## Acceptance
{acceptance}

## Evidence
{evidence}

## Exclusive Files
{exclusive_files}
"""
    return prd

def main():
    parser = argparse.ArgumentParser(description="Deterministic Linear mandate to PRD compiler.")
    parser.add_argument("input_file", help="Path to the raw Linear mandate markdown file")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: File {args.input_file} not found.", file=sys.stderr)
        sys.exit(1)

    prd_content = compile_prd(args.input_file)
    print(prd_content)

if __name__ == "__main__":
    main()
