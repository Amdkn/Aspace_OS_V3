#!/usr/bin/env python3
"""Verifier Wheel Discovery — bus d'etat + 8 jauges LD01-LD08 (tape 27)."""
import json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PERSONAS = {"LD01": "Book", "LD02": "Saru", "LD03": "Culber", "LD04": "Tilly",
            "LD05": "Stamets", "LD06": "Burnham", "LD07": "Reno", "LD08": "Georgiou"}
FOLDERS = {"LD01": "LD01_Business_Book", "LD02": "LD02_Finance_Saru", "LD03": "LD03_Health_Culber",
           "LD04": "LD04_Cognition_Tilly", "LD05": "LD05_Social_Stamets", "LD06": "LD06_Family_Burnham",
           "LD07": "LD07_Creativity_Reno", "LD08": "LD08_Impact_Georgiou"}
ZORA = {"GREEN", "YELLOW", "RED"}
LOAD = {"low", "medium", "high", "critical"}
ROUTES = {"ORVILLE_IKIGAI", "SNW_12WY", "ENTERPRISE_PARA", "CERRITOS_GTD", "PROTOSTAR_DEAL"}

ok = True

def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

bus_path = os.path.join(ROOT, "state.json")
bus = load(bus_path)

schema_valid = (bus.get("ship") == "DISCOVERY"
                and bus.get("framework") == "Life Wheel / ZORA"
                and "updated" in bus
                and isinstance(bus.get("domains"), dict)
                and set(bus["domains"]) == set(PERSONAS)
                and bus.get("evidence_paths") == [])
if not schema_valid:
    fail("bus state.json schema")

n_ok = 0
for ld, persona in PERSONAS.items():
    d = bus["domains"].get(ld, {})
    good = (d.get("persona") == persona
            and d.get("zora_state") in ZORA
            and d.get("load_signal") in LOAD
            and d.get("beth_action") is not None
            and d.get("morty_route") in ROUTES)
    if not good:
        fail("bus domain %s" % ld)
        continue
    fpath = os.path.join(ROOT, FOLDERS[ld], "state.json")
    try:
        s = load(fpath)
        coh = (s.get("domain") == ld and s.get("persona") == persona
               and s.get("zora_state") == d["zora_state"]
               and s.get("load_signal") == d["load_signal"]
               and s.get("zora_state") in ZORA and s.get("load_signal") in LOAD)
    except Exception as e:
        fail("domain file %s: %s" % (ld, e))
        continue
    if not coh:
        fail("domain %s incoherent with bus" % ld)
        continue
    n_ok += 1

size_ok = os.path.getsize(bus_path) < 10240
if not size_ok:
    fail("bus size >= 10240")

print("domains_ok=%d/8" % n_ok)
print("schema_valid=%s" % str(schema_valid).lower())
print("bus_size_ok=%s" % str(size_ok).lower())
sys.exit(0 if (ok and n_ok == 8 and schema_valid) else 1)
