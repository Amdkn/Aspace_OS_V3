"""Verifier Solaris — work 37, Summers Verse ingestion.

Verifie le registre des sources Solaris dans 00_Summers_Verse.
Retourne rc=0 si au moins 1 critere OK, imprime chaque critere.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
REGISTRE = BASE / "registre_solaris.json"

resultats = []


def critere(nom, cond, detail=""):
    resultats.append((nom, bool(cond), detail))


def main():
    # C1: le registre existe
    critere("C1_registre_existe", REGISTRE.is_file(), str(REGISTRE))

    # C2: JSON valide et chargable
    data = None
    try:
        data = json.loads(REGISTRE.read_text(encoding="utf-8"))
        ok, detail = True, "json.loads rc=0"
    except Exception as e:  # noqa: BLE001
        ok, detail = False, str(e)
    critere("C2_json_valide", ok, detail)

    # C3: structure minimale du registre Solaris
    if data is not None:
        critere(
            "C3_structure_registre",
            isinstance(data, dict)
            and data.get("verse") == "Summers Verse"
            and isinstance(data.get("sources"), list)
            and len(data["sources"]) >= 1,
            f"verse={data.get('verse')!r} sources={len(data.get('sources', []))}",
        )
        # C4: chaque source a un id, un chemin et un type
        srcs = data.get("sources", [])
        complet = all(
            isinstance(s, dict) and s.get("id") and s.get("chemin") and s.get("type")
            for s in srcs
        )
        critere("C4_sources_completes", complet and bool(srcs), f"{len(srcs)} source(s)")
    else:
        critere("C3_structure_registre", False, "JSON illisible")
        critere("C4_sources_completes", False, "JSON illisible")

    n_ok = sum(1 for _, ok, _ in resultats if ok)
    for nom, ok, detail in resultats:
        print(f"[{'OK' if ok else 'FAIL'}] {nom} — {detail}")
    print(f"Total: {n_ok}/{len(resultats)} criteres OK")
    return 0 if n_ok >= 1 else 1


if __name__ == "__main__":
    sys.exit(main())
