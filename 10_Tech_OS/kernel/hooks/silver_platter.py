#!/usr/bin/env python3
"""
Silver Platter Context Injector — Agent OS V3 (Tech OS Kernel)
Couche déterministe [Pantry / 6D] de la Pyramide de Sécurité.

Fournit à la volée aux agents (Ryan, Yaz, Antigravity) un "plateau d'argent"
contenant uniquement le sous-contexte strict nécessaire :
- Invariants D1-D4 résumés
- Schéma cible
- Status des derniers commits et validation gates
- Évite l'empoisonnement du contexte et économise 80% de tokens.
"""

import sys
import json
import sqlite3
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parent.parent
UC_DB = KERNEL_DIR / "uc.db"
SSSF_DB = Path("C:/Users/amado/super-simple-software-factory/adws/adw_data/sssf.db")

def get_silver_platter(domain: str = "l0-tech") -> dict:
    platter = {
        "domain": domain,
        "invariants": {
            "L0": "Un système qui ne sait pas se répliquer est un document, pas un système.",
            "D1": "Jumeau numérique autonome et résilient.",
            "D2": "Frontière certifiée vs supposée (verified: by: human:amdkn).",
            "D3": "Le disque est l'unique source de vérité.",
            "D4": "Reproduire sans réexpliquer (Ownerbooks & SOPs vivantes)."
        },
        "system_status": {
            "uc_db_connected": UC_DB.exists(),
            "sssf_db_connected": SSSF_DB.exists(),
        },
        "gates_required": [
            "tsc_zero_error",
            "artifacts_non_empty",
            "json_parses",
            "rot_rate_fresh"
        ]
    }

    if SSSF_DB.exists():
        try:
            conn = sqlite3.connect(SSSF_DB)
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM sessions")
            platter["system_status"]["sssf_sessions_count"] = cur.fetchone()[0]
            conn.close()
        except Exception as e:
            platter["system_status"]["sssf_error"] = str(e)

    return platter

if __name__ == "__main__":
    dom = sys.argv[1] if len(sys.argv) > 1 else "l0-tech"
    print(json.dumps(get_silver_platter(dom), indent=2))
