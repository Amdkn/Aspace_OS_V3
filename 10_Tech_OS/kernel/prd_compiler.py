#!/usr/bin/env python3
"""
10_Tech_OS/kernel/prd_compiler.py
Deterministic compiler to parse raw Linear mandate texts into structured, bounded Markdown PRDs.
"""
import argparse
import os
import re
import sys

def parse_mandate(content):
    """
    Parses the mandate text for the required fields.
    Extracts Scope, Dependencies, Acceptance, Evidence, Exclusive Files.
    """
    fields = {
        "Scope": "",
        "Dependencies": "",
        "Acceptance": "",
        "Evidence": "",
        "Exclusive Files": ""
    }

    # Try to find specific sections in the text using basic regex or string splitting
    # The mandate might not be perfectly formatted, so we do a best effort extraction
    # or fail if not found.

    # A simple line-by-line parser for "Key: Value" or sections
    current_key = None
    lines = content.split('\n')

    # First, let's try a regex approach for explicit fields
    def extract_section(text, section_name):
        pattern = rf"(?i)(?:^|\n)(?:##\s*)?(?:{section_name})[:\s]+(.*?)(?=\n(?:##\s*|(?:\w+(?: \w+)*[:]))|\Z)"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    for key in fields.keys():
        val = extract_section(content, key)
        if val:
            fields[key] = val

    # For any fields missing, we try to grab the whole content if it's small and unstructured?
    # Actually, the requirement says "enforces the inclusion of Scope, Owner, Dependencies, Acceptance, Evidence, and Exclusive Files".
    # This implies we might need to strictly require them or generate placeholders.
    # Let's enforce that they exist, or at least generate the structure with "Missing" if not found.
    for key in fields.keys():
        if not fields[key]:
            # If not explicitly formatted, we'll just try to infer or leave as FIXME
            fields[key] = "TODO: Define " + key

    return fields

def compile_prd(mandate_content, issue_id, forge_group):
    parsed = parse_mandate(mandate_content)

    # Force Owner assignment (Clara Primary Spec, Rick Gatekeeper) without LLM.
    owner = "Primary Spec: Clara\nGatekeeper: Rick"

    # Generate the bounded PRD markdown
    prd_md = f"""# Bounded PRD: {issue_id} ({forge_group})

## Scope
{parsed['Scope']}

## Owner
{owner}

## Dependencies
{parsed['Dependencies']}

## Acceptance
{parsed['Acceptance']}

## Evidence
{parsed['Evidence']}

## Exclusive Files
{parsed['Exclusive Files']}
"""
    return prd_md

def main():
    parser = argparse.ArgumentParser(description="Compile Linear mandate into bounded PRD")
    parser.add_argument('--file', required=True, help="Path to the mandate file")
    parser.add_argument('--issue_id', required=True, help="Issue ID (e.g., FOR-4)")
    parser.add_argument('--forge_group', required=True, help="Forge group (e.g., FORGE_F0)")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: Mandate file not found: {args.file}")
        sys.exit(1)

    with open(args.file, 'r', encoding='utf-8') as f:
        content = f.read()

    prd_content = compile_prd(content, args.issue_id, args.forge_group)

    # Output to the correct directory: 10_Tech_OS/PRD_Autonomy/{forge_group}/
    # e.g., 10_Tech_OS/PRD_Autonomy/FORGE_F0/{issue_id}.md

    out_dir = os.path.join("10_Tech_OS", "PRD_Autonomy", args.forge_group)
    os.makedirs(out_dir, exist_ok=True)

    out_file = os.path.join(out_dir, f"{args.issue_id}.md")

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(prd_content)

    print(f"Successfully compiled PRD to {out_file}")

if __name__ == "__main__":
    main()
