import argparse
import sys
import os

def compile_prd(linear_mandate_text):
    """
    Compiles a raw Linear mandate into a bounded PRD format.
    Enforces the inclusion of Scope, Owner, Dependencies, Acceptance, Evidence, and Exclusive Files.
    Automatically assigns Clara as Primary Spec and Rick as Gatekeeper.
    """
    # In a real scenario, this might extract specific sections from the raw text.
    # Here, we treat the raw text as the scope/objective description.
    scope_text = linear_mandate_text.strip()

    prd_content = f"""# Product Requirements Document (PRD)

## Scope
{scope_text}

## Owner
- **Primary Spec:** Clara
- **Mechanism Gatekeeper:** Rick

## Dependencies
- None identified by default. (To be populated as needed)

## Acceptance Criteria
- [ ] Requirements met as per scope.
- [ ] Code is deterministic and bounded.
- [ ] Output feeds Jules fleet without LLM technician work.

## Evidence
- Automated tests pass.
- Bounded scope verified by gatekeeper.

## Exclusive Files
- None identified by default. (To be populated as needed)
"""
    return prd_content

def main():
    parser = argparse.ArgumentParser(description="Compile Linear mandate to PRD")
    parser.add_argument("--mandate-file", required=True, help="Path to Linear mandate file")
    parser.add_argument("--out-file", required=True, help="Path to output PRD file")

    args = parser.parse_args()

    if not os.path.exists(args.mandate_file):
        print(f"Error: Mandate file '{args.mandate_file}' not found.")
        sys.exit(1)

    with open(args.mandate_file, 'r', encoding='utf-8') as f:
        mandate_text = f.read()

    prd = compile_prd(mandate_text)

    # Ensure directory exists
    os.makedirs(os.path.dirname(os.path.abspath(args.out_file)), exist_ok=True)

    with open(args.out_file, 'w', encoding='utf-8') as f:
        f.write(prd)

    print(f"Compiled PRD written to {args.out_file}")

if __name__ == "__main__":
    main()
