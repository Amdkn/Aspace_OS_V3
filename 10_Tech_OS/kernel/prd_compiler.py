import re
import argparse
import sys

def compile_prd(raw_text: str) -> str:
    """
    Compiles a raw Linear mandate text into a deterministic bounded Markdown PRD.
    """
    # Extract sections using regex
    scope_match = re.search(r'(?i)(?:Scope|Objective)s?\s*:?\s*\n*(.*?)(?=\n*(?:Owner|Dependencies|Acceptance|Evidence|Exclusive Files|#|$))', raw_text, re.DOTALL)
    owner_match = re.search(r'(?i)Owner(?:s)?\s*:?\s*\n*(.*?)(?=\n*(?:Scope|Dependencies|Acceptance|Evidence|Exclusive Files|#|$))', raw_text, re.DOTALL)
    deps_match = re.search(r'(?i)Dependencies\s*:?\s*\n*(.*?)(?=\n*(?:Scope|Owner|Acceptance|Evidence|Exclusive Files|#|$))', raw_text, re.DOTALL)
    acc_match = re.search(r'(?i)Acceptance\s*(?:Criteria)?\s*:?\s*\n*(.*?)(?=\n*(?:Scope|Owner|Dependencies|Evidence|Exclusive Files|#|$))', raw_text, re.DOTALL)
    evi_match = re.search(r'(?i)Evidence\s*:?\s*\n*(.*?)(?=\n*(?:Scope|Owner|Dependencies|Acceptance|Exclusive Files|#|$))', raw_text, re.DOTALL)
    files_match = re.search(r'(?i)Exclusive Files\s*:?\s*\n*(.*?)(?=\n*(?:Scope|Owner|Dependencies|Acceptance|Evidence|#|$))', raw_text, re.DOTALL)

    scope = scope_match.group(1).strip() if scope_match else "No scope provided."
    owner_raw = owner_match.group(1).strip() if owner_match else ""
    dependencies = deps_match.group(1).strip() if deps_match else "None specified."
    acceptance = acc_match.group(1).strip() if acc_match else "No acceptance criteria specified."
    evidence = evi_match.group(1).strip() if evi_match else "No evidence criteria specified."
    exclusive_files = files_match.group(1).strip() if files_match else "None specified."

    # Parse specific owner assignments or default
    primary_spec = "Clara"
    mechanism_gate = "Rick"

    if owner_raw:
        spec_match = re.search(r'(?i)(?:Primary )?Spec\s*:?\s*([^\n]+)', owner_raw)
        gate_match = re.search(r'(?i)(?:Mechanism )?Gate(?:keeper)?\s*:?\s*([^\n]+)', owner_raw)

        if spec_match:
            primary_spec = spec_match.group(1).strip()
        elif "Primary Spec" not in owner_raw and "Spec" not in owner_raw and "\n" not in owner_raw:
            # Maybe just a list of names or one name
             primary_spec = owner_raw

        if gate_match:
            mechanism_gate = gate_match.group(1).strip()

    prd_md = f"""# Product Requirements Document (PRD)

## Scope
{scope}

## Owner
- Primary Spec: {primary_spec}
- Mechanism Gatekeeper: {mechanism_gate}

## Dependencies
{dependencies}

## Acceptance
{acceptance}

## Evidence
{evidence}

## Exclusive Files
{exclusive_files}
"""
    return prd_md

def main():
    parser = argparse.ArgumentParser(description="Compile a raw Linear mandate into a bounded PRD.")
    parser.add_argument("--input", type=str, required=True, help="Path to the raw mandate text file.")
    parser.add_argument("--output", type=str, required=True, help="Path to write the compiled PRD markdown file.")

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)

    prd_content = compile_prd(raw_text)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(prd_content)

    print(f"Successfully compiled PRD to '{args.output}'")

if __name__ == "__main__":
    main()
