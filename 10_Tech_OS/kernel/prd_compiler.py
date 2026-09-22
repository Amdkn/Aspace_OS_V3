import re
import os
import argparse
import sys

REQUIRED_SECTIONS = [
    "Scope",
    "Owner",
    "Dependencies",
    "Acceptance",
    "Evidence",
    "Exclusive Files"
]

class PRDCompiler:
    @staticmethod
    def compile(raw_text: str, issue_id: str = "UNKNOWN", forge_group: str = "UNKNOWN") -> str:
        sections = {}
        for key in REQUIRED_SECTIONS:
            other_keys = [k for k in REQUIRED_SECTIONS if k != key]
            stop_pattern = "|".join([fr"\n{re.escape(k)}:" for k in other_keys])
            pattern = fr"{re.escape(key)}:\s*(.*?)(?={stop_pattern}|$)"
            match = re.search(pattern, raw_text, re.DOTALL | re.IGNORECASE)
            if match:
                sections[key] = match.group(1).strip()
            else:
                raise ValueError(f"Missing required section: {key}")

        lines = []
        lines.append(f"# PRD: {issue_id} ({forge_group})")
        lines.append("")
        lines.append("**Primary Spec**: Clara")
        lines.append("**Gatekeeper**: Rick")
        lines.append("")

        for key in REQUIRED_SECTIONS:
            lines.append(f"## {key}")
            lines.append(sections[key])
            lines.append("")

        return "\n".join(lines).strip() + "\n"

    @staticmethod
    def write_prd(compiled_md: str, issue_id: str, forge_group: str, base_dir: str = "10_Tech_OS/PRD_Autonomy"):
        out_dir = os.path.join(base_dir, forge_group)
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, f"{issue_id}.md")
        with open(out_file, "w") as f:
            f.write(compiled_md)
        return out_file

def main():
    parser = argparse.ArgumentParser(description="Compile Linear mandate into bounded PRD.")
    parser.add_argument("--file", help="Path to raw mandate file", type=str)
    parser.add_argument("--issue_id", help="Issue ID (e.g., FPRD-001_FOR-4)", type=str, required=True)
    parser.add_argument("--forge_group", help="Forge Group (e.g., FORGE_F0)", type=str, required=True)
    parser.add_argument("--base_dir", help="Base directory for output", type=str, default="10_Tech_OS/PRD_Autonomy")
    parser.add_argument("--text", help="Raw mandate text", type=str)

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            raw_text = f.read()
    elif args.text:
        raw_text = args.text
    else:
        raw_text = sys.stdin.read()

    try:
        compiled_md = PRDCompiler.compile(raw_text, issue_id=args.issue_id, forge_group=args.forge_group)
        out_file = PRDCompiler.write_prd(compiled_md, args.issue_id, args.forge_group, args.base_dir)
        print(f"Successfully compiled PRD to {out_file}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
