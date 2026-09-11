#!/usr/bin/env python
"""Verifier 30_Business_OS — pattern Coach OS (pulse.json + verifier).

Preuve Gate 2 (ruban _INBOX/S1_Rick/intent-migration-v2-v3-gates-20260903.md) :
registre présent + pulse présent + projets distillés référencés + template
Coach OS intact. Sortie BUSINESS_OS_OK + rc=0 en cas de succès.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FAILS = []


def check(label, cond):
    print(("OK  " if cond else "FAIL") + " " + label)
    if not cond:
        FAILS.append(label)


# 1. Registre Coach OS-style
reg = ROOT / "00_Registre" / "registre.json"
check("registre present: 00_Registre/registre.json", reg.is_file())
d = json.loads(reg.read_text(encoding="utf-8")) if reg.is_file() else {}
check("registre has template=Coach OS", d.get("template", "").startswith("Coach OS"))
check("registre lists 6 domains", len(d.get("domains", [])) == 6)
for dom in d.get("domains", []):
    check("domain dir exists: " + dom["path"], (ROOT / dom["path"]).is_dir())

# 2. Pulse — pattern Coach OS
pulse = ROOT / "00_Registre" / "pulse.json"
check("pulse present: 00_Registre/pulse.json", pulse.is_file())

# 3. Projets distillés V2 (Gate 1 preuve croisée)
dp = d.get("projects_distilled_v2", [])
check("6 projets V2 distillés listés", len(dp) == 6)

# 4. Template Coach OS intact
coach = ROOT / "10_Projects" / "coach-os-app"
check("coach-os-app present (template)", coach.is_dir())
check("coach-os-app _runtime exists", (coach / "_runtime").is_dir())

# 5. registre_para coherent canon (verify_para rc=0)
rp = ROOT.parent / "20_Life_OS" / "24_PARA_Enterprise" / "registre_para.json"
vp = ROOT.parent / "20_Life_OS" / "24_PARA_Enterprise" / "verify_para.py"
if not rp.is_file():
    check("registre_para.json present", False)
elif not vp.is_file():
    check("verify_para.py present (canon verifier)", False)
else:
    import subprocess
    r = subprocess.run(
        [sys.executable, str(vp)],
        capture_output=True, text=True,
        cwd=str(vp.parent),
    )
    check("registre_para coherent canon (verify_para rc=0)", r.returncode == 0)

if FAILS:
    print("FAILED: " + str(len(FAILS)))
    sys.exit(1)
print("BUSINESS_OS_OK")
sys.exit(0)