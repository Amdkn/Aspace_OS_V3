#!/usr/bin/env python3
import argparse
import os
import re

def parse_section(text, section_name):
    """
    Attempts to extract a section from the text based on common Markdown headings.
    Matches headings like `# Section`, `## Section`, `### Section`.
    Returns the content of the section, or an empty string if not found.
    """
    pattern = re.compile(rf'^#+\s*{section_name}\s*\n(.*?)(?=\n#+ |\Z)', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1).strip()
    return ""

def compile_prd(mandate_text, issue_id, forge_group):
    """
    Compiles a structured Bounded PRD from a raw mandate text.
    Enforces Clara as Primary Spec and Rick as Gatekeeper.
    """
    # Extract sections if they exist
    scope = parse_section(mandate_text, 'scope')
    if not scope:
        # If no explicit Scope section, assume the whole text (minus other found sections) might just be scope.
        # For simplicity, we just dump the mandate text if it's short, or a default.
        scope = mandate_text.strip() if mandate_text.strip() else "No scope provided."

    dependencies = parse_section(mandate_text, 'dependencies')
    if not dependencies:
        dependencies = "None specified."

    acceptance = parse_section(mandate_text, 'acceptance')
    if not acceptance:
        acceptance = "Tests pass."

    evidence = parse_section(mandate_text, 'evidence')
    if not evidence:
        evidence = "Logs and successful test runs."

    exclusive_files = parse_section(mandate_text, 'exclusive files')
    if not exclusive_files:
        exclusive_files = "None specified."

    # Build the structured PRD
    prd_lines = []
    prd_lines.append(f"# Bounded PRD: {issue_id}")
    prd_lines.append(f"Forge Group: {forge_group}")
    prd_lines.append("")
    prd_lines.append("## Scope")
    prd_lines.append(scope)
    prd_lines.append("")
    prd_lines.append("## Owner")
    prd_lines.append("- Primary Spec: Clara")
    prd_lines.append("- Mechanism Gatekeeper: Rick")
    prd_lines.append("")
    prd_lines.append("## Dependencies")
    prd_lines.append(dependencies)
    prd_lines.append("")
    prd_lines.append("## Acceptance")
    prd_lines.append(acceptance)
    prd_lines.append("")
    prd_lines.append("## Evidence")
    prd_lines.append(evidence)
    prd_lines.append("")
    prd_lines.append("## Exclusive Files")
    prd_lines.append(exclusive_files)
    prd_lines.append("")

    return "\n".join(prd_lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deterministic Linear mandate bounded PRD compiler")
    parser.add_argument("--file", help="Path to the input text file containing the raw mandate", default="")
    parser.add_argument("--issue_id", required=True, help="Linear issue ID (e.g., FPRD-001)")
    parser.add_argument("--forge_group", required=True, help="Forge group for categorization (e.g., FORGE_F0)")
    args = parser.parse_args()

    mandate_text = ""
    if args.file and os.path.exists(args.file):
        with open(args.file, 'r', encoding='utf-8') as f:
            mandate_text = f.read()

    prd_content = compile_prd(mandate_text, args.issue_id, args.forge_group)

    out_dir = os.path.join("10_Tech_OS", "PRD_Autonomy", args.forge_group)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"{args.issue_id}.md")

    with open(out_file, 'w', encoding='utf-8') as f:
         f.write(prd_content)

    print(f"Successfully compiled PRD to {out_file}")
