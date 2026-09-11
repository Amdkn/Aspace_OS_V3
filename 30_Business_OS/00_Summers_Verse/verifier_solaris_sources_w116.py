"""Verifier Solaris sources v+2 - work 116, Summers Verse ingestion.

Verifie le registre des sources Solaris (registre_solaris_sources_w116.json)
dans 00_Summers_Verse. Retourne rc=0 si au moins 1 critere OK.
"""
import json
import subprocess
import sys
import hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
REGISTRE = BASE / "registre_solaris_sources_w116.json"

resultats = []

def critere(nom, cond, detail=""):
    resultats.append((nom, bool(cond), detail))

def main():
    # C1: le registre existe
    critere("C1_registre_existe", REGISTRE.is_file(), str(REGISTRE))

    # C2: JSON lisible par python -m json.tool (rc=0) - DoD ruban
    rc = subprocess.run(
        [sys.executable, "-m", "json.tool", str(REGISTRE)],
        capture_output=True,
    ).returncode
    critere("C2_json_tool_rc0", rc == 0, f"python -m json.tool rc={rc}")

    data = None
    try:
        data = json.loads(REGISTRE.read_text(encoding="utf-8"))
    except Exception as e:
        critere("C3_structure_registre", False, str(e))
    if data is not None:
        ok = (
            isinstance(data, dict)
            and data.get("verse") == "Summers Verse"
            and isinstance(data.get("sources"), list)
            and len(data["sources"]) >= 1
        )
        critere(
            "C3_structure_registre", ok,
            f"verse={data.get('verse')!r} sources={len(data.get('sources', []))}",
        )
        srcs = data.get("sources", [])
        complet = all(
            isinstance(s, dict) and s.get("id") and s.get("chemin") and s.get("type")
            for s in srcs
        )
        critere("C4_sources_completes", complet and bool(srcs), f"{len(srcs)} source(s)")

        tape = (BASE.parent.parent / data.get("tape", "")).resolve()
        critere("C5_ruban_existe", tape.is_file(), str(tape))

        sha = hashlib.sha256(tape.read_bytes()).hexdigest()
        critere(
            "C6_sha_ruban_verifie",
            sha == data.get("tape_sha256"),
            sha[:16] + "...",
        )

        sig = data.get("origin", {})
        critere(
            "C7_signal_wheel",
            "LD01" in sig.get("signal", "") and sig.get("beth_action") == "none",
            f"signal={sig.get('signal', '')[:60]}",
        )

        routes = sig.get("wheel_routes_mesurees", {})
        critere(
            "C8_routes_mesurees",
            routes.get("LD03") == "PROTOSTAR_DEAL",
            str(routes),
        )

    n_ok = sum(1 for _, ok, _ in resultats if ok)
    for nom, ok, detail in resultats:
        print(f"[{'OK' if ok else 'FAIL'}] {nom} - {detail}")
    print("SOLARIS_W116_OK" if n_ok >= 1 else "SOLARIS_W116_FAIL")
    print(f"Total: {n_ok}/{len(resultats)} criteres OK")
    return 0 if n_ok >= 1 else 1

if __name__ == "__main__":
    sys.exit(main())
