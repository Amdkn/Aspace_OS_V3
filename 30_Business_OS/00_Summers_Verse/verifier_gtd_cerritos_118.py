#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Verifier boucle GTD Cerritos appliquee au projet actif (work 118, tape 89)."""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(BASE))

erreurs = []

try:
    with open(os.path.join(RACINE, "20_Life_OS", "22_Wheel_Discovery", "state.json"),
              encoding="utf-8") as f:
        state = json.load(f)
    txt = json.dumps(state)
    if "CERRITOS_GTD" not in txt:
        erreurs.append("[1] CERRITOS_GTD absent de state.json")
except Exception as e:
    erreurs.append("[1] state.json illisible: %s" % e)

if not erreurs:
    print("OK: [1] signal Wheel lu (CERRITOS_GTD), state.json non modifie")

reg = None
reg_path = os.path.join(BASE, "registre_gtd_cerritos_118.json")
if not erreurs:
    try:
        p = subprocess.run([sys.executable, "-m", "json.tool", reg_path],
                           capture_output=True)
        if p.returncode != 0:
            erreurs.append("[2] json.tool rc=%d: %s" % (p.returncode,
                           p.stderr.decode(errors="replace")[:200]))
        else:
            with open(reg_path, encoding="utf-8") as f:
                reg = json.load(f)
    except Exception as e:
        erreurs.append("[2] %s" % e)

if reg is not None:
    requis = {"registre": "summers_verse_cerritos_gtd_w118", "work_id": 118,
              "tape_id": 89, "harness": "nardole_build_l2", "prediction_id": 148}
    diffs = [k for k, v in requis.items() if reg.get(k) != v]
    if diffs:
        erreurs.append("[2] champs invalides: %s" % ", ".join(diffs))
    else:
        print("OK: [2] registre_gtd_cerritos_118.json valide (json.tool rc=0)")

if erreurs:
    for err in erreurs:
        print("FAIL: %s" % err)
    print("CERRITOS118_KO")
    sys.exit(1)
else:
    print("CERRITOS118_OK")
    sys.exit(0)
