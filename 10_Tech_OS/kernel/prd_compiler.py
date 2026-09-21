#!/usr/bin/env python3
"""prd_compiler.py — Linear mandate to bounded PRD compiler.

Parses raw Linear mandate texts deterministically without LLMs and outputs
a structured Markdown PRD enforcing Scope, Owner, Dependencies, Acceptance, Evidence, and Exclusive Files.
Automatically assigns Clara as Primary Spec and Rick as Gatekeeper.
"""

import argparse
import re
import sys

def parse_linear_mandate(raw_text: str) -> dict:
    sections = {
        "Scope": "",
        "Dependencies": "",
        "Acceptance": "",
        "Evidence": "",
        "Exclusive Files": ""
    }

    current_section = None

    section_patterns = {
        "Scope": re.compile(r'^(?:Scope|Description)\s*:', re.IGNORECASE),
        "Dependencies": re.compile(r'^Dependencies\s*:', re.IGNORECASE),
        "Acceptance": re.compile(r'^(?:Acceptance|Acceptance Criteria)\s*:', re.IGNORECASE),
        "Evidence": re.compile(r'^Evidence\s*:', re.IGNORECASE),
        "Exclusive Files": re.compile(r'^Exclusive Files\s*:', re.IGNORECASE),
    }

    for line in raw_text.splitlines():
        matched = False
        for sec, pattern in section_patterns.items():
            if pattern.match(line.strip()):
                current_section = sec
                content = re.sub(pattern, '', line.strip()).strip()
                if content:
                    sections[sec] += content + "\n"
                matched = True
                break

        if not matched and current_section:
            sections[current_section] += line + "\n"

    for k in sections:
        sections[k] = sections[k].strip() or "N/A"

    return sections

def compile_prd(raw_text: str) -> str:
    sections = parse_linear_mandate(raw_text)

    prd = []
    prd.append("# Bounded PRD")
    prd.append("")
    prd.append("## Scope")
    prd.append(sections["Scope"])
    prd.append("")
    prd.append("## Owner")
    prd.append("- **Primary Spec:** Clara")
    prd.append("- **Gatekeeper:** Rick")
    prd.append("")
    prd.append("## Dependencies")
    prd.append(sections["Dependencies"])
    prd.append("")
    prd.append("## Acceptance")
    prd.append(sections["Acceptance"])
    prd.append("")
    prd.append("## Evidence")
    prd.append(sections["Evidence"])
    prd.append("")
    prd.append("## Exclusive Files")
    prd.append(sections["Exclusive Files"])

    return "\n".join(prd)

def main():
    parser = argparse.ArgumentParser(description="Linear mandate to bounded PRD compiler")
    parser.add_argument("input_file", help="Path to the raw Linear mandate file")
    parser.add_argument("output_file", nargs='?', help="Path to output PRD file (optional, prints to stdout if omitted)")

    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    prd_content = compile_prd(raw_text)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(prd_content)
    else:
        print(prd_content)

if __name__ == "__main__":
    main()
