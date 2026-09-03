"""Summers Verse v0 verifier — stdlib only.

Exit 1 si: JSON invalide, projects vide, id inconnu (hors registre), README manquant.
Exit 0 + 'summers-verse v0: OK' sinon. Paths relatifs a __file__ (cwd-free).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRE = ROOT / "00_Registre" / "registre.json"
PROJECTS = ROOT / "projects"

# Ids reconnus hors registre (miroirs autorises de 10_Projects/).
KNOWN_IDS = {"coach-os-app"}


def main() -> int:
    try:
        data = json.loads(REGISTRE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL: registre.json illisible/invalide: {e}", file=sys.stderr)
        return 1

    projects = data.get("projects")
    if not isinstance(projects, list) or not projects:
        print("FAIL: projects vide ou absent", file=sys.stderr)
        return 1

    for p in projects:
        pid = p.get("id")
        if pid not in KNOWN_IDS:
            print(f"FAIL: id inconnu: {pid!r}", file=sys.stderr)
            return 1
        readme = PROJECTS / pid / "README.md"
        if not readme.is_file():
            print(f"FAIL: README manquant pour {pid!r}", file=sys.stderr)
            return 1

    print("summers-verse v0: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
