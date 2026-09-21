import re
from typing import Dict

def parse_mandate(text: str) -> Dict[str, str]:
    """
    Parses a raw Linear mandate text and extracts the bounded fields:
    Scope, Owner, Dependencies, Acceptance, Evidence, Exclusive Files.
    """
    fields = [
        "Scope",
        "Owner",
        "Dependencies",
        "Acceptance",
        "Evidence",
        "Exclusive Files"
    ]

    data = {}

    # Simple regex to extract Field: ... until next field or end of text.
    for field in fields:
        # Match 'Field:' followed by anything (non-greedy) until we see another valid 'Field:' or EOF
        pattern = re.compile(rf"(?i)^{field}:\s*(.*?)(?=\n(?:{ '|'.join(fields) }):|\Z)", re.MULTILINE | re.DOTALL)
        match = pattern.search(text)
        if match:
            data[field] = match.group(1).strip()
        else:
            data[field] = "UNKNOWN"

    return data

def format_prd(data: Dict[str, str]) -> str:
    """
    Formats the extracted fields into a bounded Markdown PRD.
    Automatically assigns Clara as Primary Spec and Rick as Gatekeeper.
    """
    prd = []
    prd.append("# Bounded PRD")
    prd.append("")
    prd.append("## Automated Assignments")
    prd.append("- **Primary Spec:** Clara")
    prd.append("- **Gatekeeper:** Rick")
    prd.append("")

    fields = [
        "Scope",
        "Owner",
        "Dependencies",
        "Acceptance",
        "Evidence",
        "Exclusive Files"
    ]

    for field in fields:
        prd.append(f"## {field}")
        prd.append(data.get(field, "UNKNOWN"))
        prd.append("")

    return "\n".join(prd).strip()

def compile_mandate_to_prd(text: str) -> str:
    """
    Main function to compile a mandate to a bounded PRD.
    """
    data = parse_mandate(text)
    return format_prd(data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            text = f.read()
            print(compile_mandate_to_prd(text))
