#!/usr/bin/env python3
"""Verifier Meta_Factory v0 — stdlib only, cwd-independent."""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
VALID_IDS = {"autolab", "primeagent", "jcode"}


def fail(msg):
    print(f"meta-factory v0: FAIL - {msg}")
    sys.exit(1)


def main():
    reg_path = BASE / "00_Registre" / "registre.json"
    try:
        data = json.loads(reg_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"registre introuvable: {reg_path}")
    except json.JSONDecodeError as e:
        fail(f"JSON invalide: {e}")

    units = data.get("units")
    if not isinstance(units, list) or len(units) != 3:
        fail(f"attendu 3 units, trouve {len(units) if isinstance(units, list) else 'autre'}")

    ids = []
    for u in units:
        if not isinstance(u, dict) or not u.get("id") or not u.get("role"):
            fail(f"unit sans id ou role: {u}")
        ids.append(u["id"])
    if set(ids) != VALID_IDS:
        fail(f"ids hors {sorted(VALID_IDS)}: {ids}")

    for uid in ids:
        readme = BASE / uid / "README.md"
        if not readme.is_file():
            fail(f"README manquant pour '{uid}': {readme}")

    print("meta-factory v0: OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
