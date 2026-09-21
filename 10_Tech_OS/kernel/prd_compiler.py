#!/usr/bin/env python3
import sys
import re
import argparse

def compile_prd(mandate_text: str) -> str:
    """
    Deterministically compiles a raw Linear mandate text into a structured, bounded Markdown PRD.
    """

    headers = ["Scope", "Description", "Dependencies", "Acceptance Criteria", "Acceptance", "Evidence", "Exclusive Files"]
    header_pattern = r'^(' + '|'.join(headers) + r'):'

    lines = mandate_text.splitlines()

    sections = {
        "scope": [],
        "dependencies": [],
        "acceptance": [],
        "evidence": [],
        "exclusive_files": []
    }

    current_section = "scope" # Default to scope if no header

    for line in lines:
        match = re.match(header_pattern, line.strip(), re.IGNORECASE)
        if match:
            header_name = match.group(1).lower()
            if header_name in ("scope", "description"):
                current_section = "scope"
            elif header_name == "dependencies":
                current_section = "dependencies"
            elif header_name in ("acceptance criteria", "acceptance"):
                current_section = "acceptance"
            elif header_name == "evidence":
                current_section = "evidence"
            elif header_name == "exclusive files":
                current_section = "exclusive_files"

            # Add the rest of the line if there's content after the colon
            content = line.strip()[len(match.group(0)):].strip()
            if content:
                sections[current_section].append(content)
        else:
            sections[current_section].append(line)

    scope_text = '\n'.join(sections["scope"]).strip()
    if not scope_text:
        # fallback if everything is empty
        scope_text = mandate_text.strip()

    deps_text = '\n'.join(sections["dependencies"]).strip() or "None"
    acc_text = '\n'.join(sections["acceptance"]).strip()
    ev_text = '\n'.join(sections["evidence"]).strip()
    excl_text = '\n'.join(sections["exclusive_files"]).strip()

    prd_template = f"""# Bounded PRD

## Scope
{scope_text}

## Owner
Primary Spec: Clara
Gatekeeper: Rick

## Dependencies
{deps_text}

## Acceptance
{acc_text}

## Evidence
{ev_text}

## Exclusive Files
{excl_text}
"""
    return prd_template

def main():
    parser = argparse.ArgumentParser(description="Linear mandate to bounded PRD compiler.")
    parser.add_argument("input", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="Input raw mandate file or stdin")
    parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout, help="Output markdown PRD file or stdout")

    args = parser.parse_args()

    mandate_text = args.input.read()
    prd_text = compile_prd(mandate_text)

    args.output.write(prd_text)

if __name__ == "__main__":
    main()
