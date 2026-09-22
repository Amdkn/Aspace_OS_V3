import argparse
import os
import re

def parse_mandate(content):
    sections = {
        "Scope": "",
        "Dependencies": "",
        "Acceptance": "",
        "Evidence": "",
        "Exclusive Files": ""
    }

    current_section = "Scope"

    for line in content.split("\n"):
        # For section matching, normalize the line heavily
        line_normalized = line.strip().lower()
        line_normalized = re.sub(r'[^a-z ]', '', line_normalized).strip()

        if line_normalized == "scope":
            current_section = "Scope"
            continue
        elif line_normalized == "dependencies":
            current_section = "Dependencies"
            continue
        elif line_normalized == "acceptance" or line_normalized == "acceptance criteria":
            current_section = "Acceptance"
            continue
        elif line_normalized == "evidence":
            current_section = "Evidence"
            continue
        elif line_normalized == "exclusive files":
            current_section = "Exclusive Files"
            continue

        sections[current_section] += line + "\n"

    # Clean up whitespace
    for key in sections:
        sections[key] = sections[key].strip()
        if not sections[key]:
            sections[key] = "TBD"

    return sections

def compile_prd(file_path, issue_id, forge_group):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    sections = parse_mandate(content)

    prd_content = f"""# PRD: {issue_id}

## Scope
{sections['Scope']}

## Owner
- **Primary Spec:** Clara
- **Gatekeeper:** Rick

## Dependencies
{sections['Dependencies']}

## Acceptance
{sections['Acceptance']}

## Evidence
{sections['Evidence']}

## Exclusive Files
{sections['Exclusive Files']}
"""

    output_dir = f"10_Tech_OS/PRD_Autonomy/FORGE_{forge_group}"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{issue_id}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(prd_content)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile a bounded PRD from a raw Linear mandate.")
    parser.add_argument("--file", required=True, help="Path to the raw mandate file")
    parser.add_argument("--issue_id", required=True, help="Linear Issue ID")
    parser.add_argument("--forge_group", required=True, help="Forge group (e.g., F0, F1)")

    args = parser.parse_args()
    output_path = compile_prd(args.file, args.issue_id, args.forge_group)
    print(f"Compiled PRD successfully: {output_path}")
