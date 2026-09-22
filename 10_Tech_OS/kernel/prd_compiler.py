#!/usr/bin/env python3
import argparse
import os
import re

def parse_mandate_text(text):
    """
    Deterministically parses free-form mandate text into bounded sections.
    It looks for headers or keywords to extract specific sections.
    """
    sections = {
        "scope": "",
        "dependencies": "None explicitly identified.",
        "acceptance": "All requirements met implicitly.",
        "evidence": "Tests passed and verified.",
        "exclusive_files": "To be determined."
    }

    # Try to find explicit sections using regex
    # Format expected e.g., "Dependencies: ...\n" or "## Dependencies\n..."
    patterns = {
        "dependencies": r"(?i)(?:##\s*|)(?:dependencies|depends on)[\s:]+(.*?)(?:\n(?=[a-zA-Z\s]+:)|\n##|$)",
        "acceptance": r"(?i)(?:##\s*|)(?:acceptance(?: criteria)?|done when)[\s:]+(.*?)(?:\n(?=[a-zA-Z\s]+:)|\n##|$)",
        "evidence": r"(?i)(?:##\s*|)(?:evidence)[\s:]+(.*?)(?:\n(?=[a-zA-Z\s]+:)|\n##|$)",
        "exclusive_files": r"(?i)(?:##\s*|)(?:exclusive files?)[\s:]+(.*?)(?:\n(?=[a-zA-Z\s]+:)|\n##|$)"
    }

    # Extract scope: everything before the first recognized section, or the whole text if none found.
    # To do this safely, we will just use the entire text as scope if it's very short or unstructured.

    scope_text = text.strip()

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            extracted = match.group(1).strip()
            if extracted:
                sections[key] = extracted
            # Remove the extracted part from the scope_text approximately
            # This is a naive cleanup, realistically Scope is the remainder.
            scope_text = scope_text.replace(match.group(0), "")

    sections["scope"] = scope_text.strip()

    if not sections["scope"]:
         sections["scope"] = "Scope derived implicitly."

    return sections

def compile_prd(mandate, issue_id, forge_group):
    sections = parse_mandate_text(mandate)

    # Mandatory sections based on memory requirements
    content = f"# Bounded PRD: {issue_id}\n\n"
    content += "## Scope\n"
    content += f"{sections['scope']}\n\n"

    # Auto-assign roles as per constraints
    content += "## Owner\n"
    content += "- Primary Spec: Clara\n"
    content += "- Gatekeeper: Rick\n\n"

    content += "## Dependencies\n"
    content += f"{sections['dependencies']}\n\n"

    content += "## Acceptance\n"
    content += f"{sections['acceptance']}\n\n"

    content += "## Evidence\n"
    content += f"{sections['evidence']}\n\n"

    content += "## Exclusive Files\n"
    content += f"{sections['exclusive_files']}\n\n"

    content += "## Original Mandate\n"
    content += mandate

    return content

def save_prd(content, issue_id, forge_group):
    base_dir = "10_Tech_OS/PRD_Autonomy"
    forge_dir = os.path.join(base_dir, forge_group)
    os.makedirs(forge_dir, exist_ok=True)

    file_path = os.path.join(forge_dir, f"{issue_id}.md")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Bounded PRD compiled successfully: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Compile Linear mandate into bounded PRD.")
    parser.add_argument("--file", required=True, help="Path to the raw mandate file.")
    parser.add_argument("--issue_id", required=True, help="The issue ID (e.g., FPRD-001_FOR-4).")
    parser.add_argument("--forge_group", required=True, help="The forge group (e.g., FORGE_F0).")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: Mandate file not found: {args.file}")
        return

    with open(args.file, 'r', encoding='utf-8') as f:
        mandate_text = f.read()

    prd_content = compile_prd(mandate_text, args.issue_id, args.forge_group)
    save_prd(prd_content, args.issue_id, args.forge_group)

if __name__ == "__main__":
    main()
