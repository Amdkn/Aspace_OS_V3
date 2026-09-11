#!/usr/bin/env python3
"""Verifier work 117 - Summers Verse horizon 12WY (registre + verifier)."""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
REGISTRE = str(BASE / "registre_summers_verse_12wy_w117.json")
STATE = str(BASE.parent.parent / "20_Life_OS/22_Wheel_Discovery/state.json")
TAPE_SHA = "88a0e834889172cf9cc810ddbc24ccf6bdcad352477b11b9705357ed20277204"

ok = 0

def critere(nom, cond):
    global ok
    print(("OK" if cond else "FAIL") + " - " + nom)
    if cond:
        ok += 1

with open(REGISTRE, encoding="utf-8") as f:
    reg = json.load(f)

critere("registre JSON charge et route SNW_12WY",
        reg["prochain_projet"]["route"] == "SNW_12WY")
critere("horizons 12WY H1/H3/H10/H30/H90",
        set(reg["prochain_projet"]["horizons"]) == {"H1", "H3", "H10", "H30", "H90"})
critere("work_id 117 et sha256 ruban conforme",
        reg["work_id"] == 117 and reg["tape_sha256"] == TAPE_SHA)
critere("Beth verte, veto non", reg["beth"]["veto"] == "non" and reg["beth"]["action"] == "none")

with open(STATE, encoding="utf-8") as f:
    state = json.load(f)
critere("state.json LD01 GREEN/low (lecture seule)",
        state["domains"]["LD01"]["zora_state"] == "GREEN"
        and state["domains"]["LD01"]["load_signal"] == "low")

r = subprocess.run([sys.executable, "-m", "json.tool", REGISTRE],
                   capture_output=True)
critere("python -m json.tool rc=0 sur le registre", r.returncode == 0)

print("criteres OK: %d" % ok)
sys.exit(0 if ok == 6 else 1)
