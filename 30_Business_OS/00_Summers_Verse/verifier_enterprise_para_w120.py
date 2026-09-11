#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifier franchise ENTERPRISE_PARA v+1 (work 120, tape 91).

Lit le signal Wheel (state.json, non modifie), valide le registre
registre_enterprise_para_w120.json et la coherence canon PARA
(verify_para.py rc=0). Sortie PARA120_OK (rc=0) ou PARA120_KO (rc=1).
"""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))  # 00_Summers_Verse
RACINE = os.path.dirname(os.path.dirname(BASE))    # depot ASpace_OS_V3

erreurs = []
ok = 0


def critere(label, cond):
    global ok
    print(("OK" if cond else "FAIL") + ": " + label)
    if cond:
        ok += 1
    else:
        erreurs.append(label)


# [1] Signal Wheel lu, route ENTERPRISE_PARA, non modifie
try:
    with open(os.path.join(RACINE, "20_Life_OS", "22_Wheel_Discovery", "state.json"),
              encoding="utf-8") as f:
        state = json.load(f)
    ld01 = state["domains"]["LD01"]
    critere("[1] signal Wheel LD01 GREEN/low, route ENTERPRISE_PARA, beth_action none",
            ld01["morty_route"] == "ENTERPRISE_PARA"
            and ld01["zora_state"] == "GREEN"
            and ld01["load_signal"] == "low"
            and ld01["beth_action"] == "none")
except Exception as e:
    erreurs.append("[1] state.json illisible: %s" % e)
    print("FAIL: [1] state.json illisible: %s" % e)

# [2] registre_enterprise_para_w120.json valide (json.tool rc=0) et champs cles
reg = None
reg_path = os.path.join(BASE, "registre_enterprise_para_w120.json")
try:
    p = subprocess.run([sys.executable, "-m", "json.tool", reg_path],
                       capture_output=True)
    critere("[2] json.tool rc=0 sur registre_enterprise_para_w120.json",
            p.returncode == 0)
    if p.returncode == 0:
        with open(reg_path, encoding="utf-8") as f:
            reg = json.load(f)
except Exception as e:
    erreurs.append("[2] %s" % e)
    print("FAIL: [2] %s" % e)

if reg is not None:
    critere("[3] registre porte tape_id 91, work_id 120, route ENTERPRISE_PARA",
            reg.get("tape_id") == 91
            and reg.get("work_id") == 120
            and reg.get("franchise", {}).get("route") == "ENTERPRISE_PARA")
    critere("[4] prediction_id 150 portee par le registre",
            reg.get("prediction_id") == 150)
else:
    critere("[3] registre inexistant", False)
    critere("[4] prediction_id absente", False)

# [5] verify_para.py canon retourne rc=0 (PARA_OK)
try:
    para_v = os.path.join(RACINE, "20_Life_OS", "24_PARA_Enterprise", "verify_para.py")
    p_para = subprocess.run([sys.executable, para_v],
                            capture_output=True, text=True)
    critere("[5] verify_para.py rc=0 (PARA_OK)",
            p_para.returncode == 0 and "PARA_OK" in p_para.stdout)
except Exception as e:
    erreurs.append("[5] verify_para.py: %s" % e)
    print("FAIL: [5] verify_para.py: %s" % e)

# [6] Projet coach-os-app present
proj = os.path.join(BASE, "projects", "coach-os-app", "registre.json")
critere("[6] projects/coach-os-app/registre.json present", os.path.isfile(proj))

print("\nBilan : %d/6 criteres OK" % ok)
if erreurs:
    print("Erreurs : " + "; ".join(erreurs))
    print("PARA120_KO")
    sys.exit(1)
else:
    print("PARA120_OK")
    sys.exit(0)
