import argparse
import os
import re

def parse_linear_mandate(text: str) -> dict:
    """Parses a linear mandate string into a dictionary of fields."""

    fields = {
        "Scope": "Not provided",
        "Owner": "Not provided",
        "Dependencies": "Not provided",
        "Acceptance": "Not provided",
        "Evidence": "Not provided",
        "Exclusive Files": "Not provided"
    }

    # We look for lines containing these keywords or markdown headings for these
    # e.g. "Scope: ...", "## Scope", "- Scope: "

    patterns = {
        "Scope": re.compile(r'^\s*(?:\#+\s*)?(?:\-\s*)?Scope(?:\:)?\s*(.*?)(?=^\s*(?:\#+\s*)?(?:\-\s*)?(?:Owner|Dependencies|Acceptance|Evidence|Exclusive Files)(?:\:)?\s*|\Z)', re.IGNORECASE | re.DOTALL | re.MULTILINE),
        "Owner": re.compile(r'^\s*(?:\#+\s*)?(?:\-\s*)?Owner(?:\:)?\s*(.*?)(?=^\s*(?:\#+\s*)?(?:\-\s*)?(?:Scope|Dependencies|Acceptance|Evidence|Exclusive Files)(?:\:)?\s*|\Z)', re.IGNORECASE | re.DOTALL | re.MULTILINE),
        "Dependencies": re.compile(r'^\s*(?:\#+\s*)?(?:\-\s*)?Dependencies(?:\:)?\s*(.*?)(?=^\s*(?:\#+\s*)?(?:\-\s*)?(?:Scope|Owner|Acceptance|Evidence|Exclusive Files)(?:\:)?\s*|\Z)', re.IGNORECASE | re.DOTALL | re.MULTILINE),
        "Acceptance": re.compile(r'^\s*(?:\#+\s*)?(?:\-\s*)?Acceptance(?:\:)?\s*(.*?)(?=^\s*(?:\#+\s*)?(?:\-\s*)?(?:Scope|Owner|Dependencies|Evidence|Exclusive Files)(?:\:)?\s*|\Z)', re.IGNORECASE | re.DOTALL | re.MULTILINE),
        "Evidence": re.compile(r'^\s*(?:\#+\s*)?(?:\-\s*)?Evidence(?:\:)?\s*(.*?)(?=^\s*(?:\#+\s*)?(?:\-\s*)?(?:Scope|Owner|Dependencies|Acceptance|Exclusive Files)(?:\:)?\s*|\Z)', re.IGNORECASE | re.DOTALL | re.MULTILINE),
        "Exclusive Files": re.compile(r'^\s*(?:\#+\s*)?(?:\-\s*)?Exclusive Files(?:\:)?\s*(.*?)(?=^\s*(?:\#+\s*)?(?:\-\s*)?(?:Scope|Owner|Dependencies|Acceptance|Evidence)(?:\:)?\s*|\Z)', re.IGNORECASE | re.DOTALL | re.MULTILINE)
    }

    for key, pattern in patterns.items():
        match = pattern.search(text)
        if match:
            extracted = match.group(1).strip()
            if extracted:
                fields[key] = extracted

    return fields

def compile_prd(fields: dict) -> str:
    """Compiles the extracted fields into a formatted PRD markdown string."""
    prd = []
    prd.append("# Bounded PRD\n")

    prd.append("## Roles")
    prd.append("- **Primary Spec:** Clara")
    prd.append("- **Gatekeeper:** Rick\n")

    for key in ["Scope", "Owner", "Dependencies", "Acceptance", "Evidence", "Exclusive Files"]:
        prd.append(f"## {key}")
        prd.append(f"{fields[key]}\n")

    return "\n".join(prd)

def main():
    parser = argparse.ArgumentParser(description="Compile a Linear mandate into a bounded PRD.")
    parser.add_argument("--input", required=True, help="Path to the input text file containing the Linear mandate.")
    parser.add_argument("--output", required=True, help="Path to save the compiled PRD markdown file.")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found at {args.input}")
        return

    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()

    fields = parse_linear_mandate(text)
    prd_markdown = compile_prd(fields)

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(prd_markdown)

    print(f"Successfully compiled PRD to {args.output}")

if __name__ == "__main__":
    main()
