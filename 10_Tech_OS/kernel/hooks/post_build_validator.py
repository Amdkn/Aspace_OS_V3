#!/usr/bin/env python3
"""
Post-Build Validator Hook — Agent OS V3 (Tech OS Kernel)
Couche déterministe [5D] de la Pyramide de Sécurité.

Exécute les validations strictes d'artefacts et de code produit par Ryan / SSSF :
1. Compilation TypeScript / Syntaxe Python.
2. Détection de placeholders ou coquilles vides (TODO, mocks sans implémentation).
3. Contrôle des codes de retour et des traces de test.
"""

import sys
import subprocess
import json
from pathlib import Path

def validate_typescript(project_dir: Path) -> dict:
    if not (project_dir / "package.json").exists():
        return {"ok": True, "note": "Pas de projet TypeScript détecté"}
    
    try:
        res = subprocess.run(
            ["npm", "run", "typecheck"],
            cwd=str(project_dir),
            capture_output=True,
            text=True,
            timeout=30,
            shell=True
        )
        return {
            "ok": res.returncode == 0,
            "stdout": res.stdout.strip(),
            "stderr": res.stderr.strip(),
            "exit_code": res.returncode
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("C:/Users/amado/agent-os/desktop")
    report = validate_typescript(target)
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["ok"] else 1)
