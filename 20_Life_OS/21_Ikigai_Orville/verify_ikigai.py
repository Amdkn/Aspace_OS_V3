#!/usr/bin/env python3
# -*- coding: ascii -*-
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
PULSE_PATH = os.path.join(BASE, "pulse.json")

def main():
    errors = []

    if not os.path.isfile(PULSE_PATH):
        errors.append("pulse.json manquant")
        print("IKIGAI_KO")
        for e in errors:
            print("  ERREUR: " + e)
        return 1

    try:
        with open(PULSE_PATH, "r", encoding="utf-8") as f:
            pulse = json.load(f)
    except Exception as e:
        errors.append("pulse.json illisible: " + str(e))
        print("IKIGAI_KO")
        for e in errors:
            print("  ERREUR: " + e)
        return 1

    if pulse.get("version") not in ["v0", "v1"]:
        errors.append("pulse.json: version is not v0 or v1")

    if "date_pulse" not in pulse:
        errors.append("pulse.json: date_pulse absent")

    if "date_init" not in pulse:
        errors.append("pulse.json: date_init absent")

    if pulse.get("framework") != "Ikigai Orville":
        errors.append("pulse.json: framework != Ikigai Orville")

    if errors:
        print("IKIGAI_KO")
        for e in errors:
            print("  ERREUR: " + e)
        return 1

    print("IKIGAI_OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
