#!/usr/bin/env python3
"""Verifier work 38 - Summers Verse horizon 12WY (route SNW_12WY)."""
import json
import subprocess
import sys

REGISTRE = "registre_solaris_12wy.json"
STATE = "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/state.json"

ok = 0


def critere(nom, cond):
    global ok
    print(("OK" if cond else "FAIL") + " - " + nom)
    if cond:
        ok += 1


with open(REGISTRE, encoding="utf-8") as f:
    reg = json.load(f)

critere("registre JSON charge et route SNW_12WY", reg["prochain_projet"]["route"] == "SNW_12WY")
critere("horizons 12WY H1/H3/H10/H30/H90",
        set(reg["prochain_projet"]["horizons"]) == {"H1", "H3", "H10", "H30", "H90"})
critere("signal LD01 GREEN load low",
        reg["source"]["signal"] == "LD01 GREEN load low")

with open(STATE, encoding="utf-8") as f:
    state = json.load(f)
critere("state.json confirme LD01 GREEN/low, beth_action none",
        state["domains"]["LD01"]["zora_state"] == "GREEN"
        and state["domains"]["LD01"]["load_signal"] == "low"
        and state["domains"]["LD01"]["beth_action"] == "none")

r = subprocess.run([sys.executable, "-m", "json.tool", REGISTRE],
                   capture_output=True)
critere("python -m json.tool rc=0 sur le registre", r.returncode == 0)

print("criteres OK: %d" % ok)
sys.exit(0 if ok >= 1 and ok == 5 else 1)
