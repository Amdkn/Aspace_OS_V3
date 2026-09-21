def compile_mandate(text: str) -> str:
    """
    Deterministically parses raw Linear mandate text into a structured, bounded Markdown PRD.
    Enforces the inclusion of Scope, Owner, Dependencies, Acceptance, Evidence, and Exclusive Files.
    Automatically assigns Clara as Primary Spec and Rick as Gatekeeper.
    """
    fields = {
        "Scope": "Not specified.",
        "Dependencies": "None",
        "Acceptance": "Not specified.",
        "Evidence": "Not specified.",
        "Exclusive Files": "None"
    }

    lines = text.split('\n')
    current_field = None
    field_content = {f: [] for f in fields.keys()}

    keywords = {
        "scope": "Scope",
        "dependencies": "Dependencies",
        "acceptance": "Acceptance",
        "evidence": "Evidence",
        "exclusive files": "Exclusive Files"
    }

    has_any_field = False

    for line in lines:
        stripped_line = line.strip()
        lower_line = stripped_line.lower()
        matched = False
        for kw, field_name in keywords.items():
            if lower_line.startswith(kw + ":") or lower_line == kw + ":":
                current_field = field_name
                # Properly extract content after the keyword and colon
                # We know lower_line starts with kw+":" (length: len(kw)+1)
                # or is exactly kw+":"
                content = stripped_line[len(kw)+1:].strip()
                if content:
                    field_content[current_field].append(content)
                matched = True
                has_any_field = True
                break

        if not matched and current_field:
            field_content[current_field].append(stripped_line)
        elif not matched and not current_field and stripped_line:
            # If we haven't matched any field yet, treat as Scope
            field_content["Scope"].append(stripped_line)

    for f in fields.keys():
        if field_content[f]:
            fields[f] = "\n".join(field_content[f]).strip()

    if not has_any_field and field_content["Scope"]:
        fields["Scope"] = "\n".join(field_content["Scope"]).strip()

    prd = f"""# Bounded PRD

## Scope
{fields['Scope']}

## Owner
Clara (Primary Spec), Rick (Gatekeeper)

## Dependencies
{fields['Dependencies']}

## Acceptance
{fields['Acceptance']}

## Evidence
{fields['Evidence']}

## Exclusive Files
{fields['Exclusive Files']}
"""
    return prd
