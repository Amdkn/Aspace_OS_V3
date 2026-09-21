import argparse
import sys
import re

def parse_mandate(text: str) -> dict:
    sections = {
        "scope": "",
        "dependencies": "",
        "acceptance": "",
        "evidence": "",
        "exclusive_files": ""
    }

    current_section = "scope"

    for line in text.split('\n'):
        lower_line = line.lower().strip()
        if lower_line.startswith("scope:"):
            current_section = "scope"
            sections[current_section] += line[6:].strip() + "\n"
        elif lower_line.startswith("dependencies:"):
            current_section = "dependencies"
            sections[current_section] += line[13:].strip() + "\n"
        elif lower_line.startswith("acceptance:"):
            current_section = "acceptance"
            sections[current_section] += line[11:].strip() + "\n"
        elif lower_line.startswith("evidence:"):
            current_section = "evidence"
            sections[current_section] += line[9:].strip() + "\n"
        elif lower_line.startswith("exclusive files:"):
            current_section = "exclusive_files"
            sections[current_section] += line[16:].strip() + "\n"
        else:
            sections[current_section] += line + "\n"

    for k in sections:
        sections[k] = sections[k].strip()
        if not sections[k]:
            if k == "scope":
                sections[k] = "No scope provided."
            else:
                sections[k] = "None specified."

    return sections

def compile_prd(mandate_text: str, title: str = "Bounded PRD") -> str:
    parsed = parse_mandate(mandate_text)

    prd = f"""# {title}

## 1. Scope
{parsed['scope']}

## 2. Owner
- Primary Spec: Clara
- Gatekeeper: Rick

## 3. Dependencies
{parsed['dependencies']}

## 4. Acceptance
{parsed['acceptance']}

## 5. Evidence
{parsed['evidence']}

## 6. Exclusive Files
{parsed['exclusive_files']}
"""
    return prd

def main():
    parser = argparse.ArgumentParser(description="Compile Linear mandate into bounded PRD.")
    parser.add_argument("--mandate", type=str, help="Raw mandate text or path to mandate file.")
    parser.add_argument("--title", type=str, default="Bounded PRD", help="Title of the PRD.")
    parser.add_argument("--out", type=str, help="Output file path.")

    args = parser.parse_args()

    if args.mandate:
        import os
        if os.path.exists(args.mandate):
            with open(args.mandate, "r") as f:
                mandate_text = f.read()
        else:
            mandate_text = args.mandate
    else:
        mandate_text = sys.stdin.read()

    prd = compile_prd(mandate_text, title=args.title)

    if args.out:
        with open(args.out, "w") as f:
            f.write(prd)
        print(f"PRD successfully compiled to {args.out}")
    else:
        print(prd)

if __name__ == "__main__":
    main()
