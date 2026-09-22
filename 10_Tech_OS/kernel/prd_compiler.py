import sys
import re

def compile_prd(raw_text: str) -> str:
    """
    Compiles a raw text mandate into a bounded PRD markdown format.
    Does not use LLMs, only string parsing.
    """
    # Define expected sections
    sections = {
        "Scope": "TBD",
        "Owner": "Clara (Primary Spec) / Rick (Gatekeeper)",
        "Dependencies": "None",
        "Acceptance": "TBD",
        "Evidence": "TBD",
        "Exclusive Files": "None"
    }

    # Try to extract sections if the text is somewhat structured.
    # We look for simple patterns like "Scope: ...", "Dependencies: ...", etc.
    # If not found, we will put the whole raw text in Scope.

    # First, let's normalize headers if any
    text = raw_text.strip()

    # If the text does not contain any obvious section markers, treat it all as Scope.
    # We consider markers as words followed by a colon at the start of a line or paragraph.
    markers = [r'(?i)^\s*(Scope)\s*:', r'(?i)^\s*(Owner)\s*:', r'(?i)^\s*(Dependencies)\s*:',
               r'(?i)^\s*(Acceptance)\s*:', r'(?i)^\s*(Evidence)\s*:', r'(?i)^\s*(Exclusive Files)\s*:']

    has_markers = any(re.search(m, text, re.MULTILINE) for m in markers)

    if not has_markers:
        if text:
            sections["Scope"] = text
    else:
        # We need a robust way to extract between markers.
        # Let's find all occurrences of markers.
        # A simpler way is to split by markers and capture them.
        pattern = r'(?i)^\s*(Scope|Owner|Dependencies|Acceptance|Evidence|Exclusive Files)\s*:'
        parts = re.split(pattern, text, flags=re.MULTILINE)

        # parts will be [preamble, Header, Content, Header, Content, ...]
        if parts and parts[0].strip():
            sections["Scope"] = parts[0].strip()

        for i in range(1, len(parts), 2):
            header = parts[i].strip().title()
            # Handle "Exclusive Files" capitalization
            if header.lower() == "exclusive files":
                header = "Exclusive Files"

            content = parts[i+1].strip()
            if content:
                # We always force the owner to Clara/Rick if we are auto-assigning without LLM.
                # However, PRD says: "If the owner is missing in the raw text, it defaults to: Clara (Primary Spec) / Rick (Gatekeeper)."
                # And "automatically assigning Clara as Primary Spec and Rick as Gatekeeper without relying on LLMs."
                # It means we should always use this default or enforce it. Let's just always enforce it or use it if missing.
                # Memory: "automatically assigning Clara as Primary Spec and Rick as Gatekeeper without relying on LLMs."
                if header == "Owner":
                    pass # We ignore extracted owner and use the forced one, or keep the default
                else:
                    sections[header] = content

    # Always enforce Owner as required by memory
    sections["Owner"] = "Clara (Primary Spec) / Rick (Gatekeeper)"

    prd_parts = []
    prd_parts.append(f"## Scope\n{sections['Scope']}\n")
    prd_parts.append(f"## Owner\n{sections['Owner']}\n")
    prd_parts.append(f"## Dependencies\n{sections['Dependencies']}\n")
    prd_parts.append(f"## Acceptance\n{sections['Acceptance']}\n")
    prd_parts.append(f"## Evidence\n{sections['Evidence']}\n")
    prd_parts.append(f"## Exclusive Files\n{sections['Exclusive Files']}")

    return "\n".join(prd_parts)

if __name__ == "__main__":
    raw_text = sys.stdin.read()
    print(compile_prd(raw_text))
