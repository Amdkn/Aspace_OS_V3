#!/usr/bin/env python3
import sys
import re
import argparse
import os

REQUIRED_SECTIONS = [
    "Scope",
    "Owner",
    "Dependencies",
    "Acceptance",
    "Evidence",
    "Exclusive Files"
]

def compile_prd(raw_text: str) -> str:
    extracted = {sec: [] for sec in REQUIRED_SECTIONS}
    current_sec = None

    for line in raw_text.splitlines():
        # Remove leading/trailing whitespaces to handle indentation in raw text
        stripped_line = line.strip()
        if not stripped_line:
            if current_sec:
                extracted[current_sec].append("")
            continue

        matched_sec = None
        for sec in REQUIRED_SECTIONS:
            # Match section name on a line, e.g., "Scope:", "## Scope", "- Scope -"
            pattern_full = r'^[\s#\*\-]*' + re.escape(sec) + r'\b\s*[:\-]?\s*$'
            if re.match(pattern_full, stripped_line, re.IGNORECASE):
                matched_sec = sec
                break
            # Match inline content, e.g., "Scope: implement a compiler"
            pattern_inline = r'^[\s#\*\-]*' + re.escape(sec) + r'\b\s*[:\-]\s*(.+)$'
            if re.match(pattern_inline, stripped_line, re.IGNORECASE):
                matched_sec = sec
                break

        if matched_sec:
            current_sec = matched_sec
            pattern_inline = r'^[\s#\*\-]*' + re.escape(matched_sec) + r'\b\s*[:\-]\s*(.+)$'
            m = re.match(pattern_inline, stripped_line, re.IGNORECASE)
            if m:
                extracted[current_sec].append(m.group(1).strip())
        else:
            if current_sec:
                extracted[current_sec].append(stripped_line)
            else:
                pass # Ignore text before first section

    for sec in REQUIRED_SECTIONS:
        # Join lines, remove leading/trailing newlines
        content = "\n".join(extracted[sec]).strip()
        if not content:
            raise ValueError(f"Missing or empty content for required section: {sec}")
        extracted[sec] = content

    lines = []
    lines.append("# Bounded PRD")
    lines.append("")
    lines.append("**Primary Spec**: Clara")
    lines.append("**Gatekeeper**: Rick")
    lines.append("")

    for sec in REQUIRED_SECTIONS:
        lines.append(f"## {sec}")
        lines.append(extracted[sec])
        lines.append("")

    return "\n".join(lines).strip() + "\n"

def main():
    parser = argparse.ArgumentParser(description="Deterministic PRD Compiler")
    parser.add_argument("input_file", help="Path to raw Linear mandate text file")
    parser.add_argument("output_file", help="Path to output bounded PRD Markdown file")
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    try:
        prd_content = compile_prd(raw_text)
    except ValueError as e:
        print(f"Error compiling PRD: {e}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)

    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(prd_content)

    print(f"Successfully compiled PRD to {args.output_file}")

if __name__ == "__main__":
    main()
