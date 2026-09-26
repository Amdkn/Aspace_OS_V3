#!/usr/bin/env python3
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_MAP_PATH = os.path.join(BASE, "20_Life_OS", "source_map.json")

def main():
    errors = []

    if not os.path.isfile(SOURCE_MAP_PATH):
        errors.append(f"source_map.json not found at {SOURCE_MAP_PATH}")
        print("SOURCE_MAP_KO")
        for e in errors:
            print(f"  ERREUR: {e}")
        return 1

    try:
        with open(SOURCE_MAP_PATH, "r", encoding="utf-8") as f:
            source_map = json.load(f)
    except Exception as e:
        errors.append(f"Could not parse source_map.json: {e}")
        print("SOURCE_MAP_KO")
        for e in errors:
            print(f"  ERREUR: {e}")
        return 1

    for category in ["frameworks", "provenance"]:
        if category not in source_map:
            errors.append(f"Missing category in source_map: {category}")
            continue

        for name, rel_path in source_map[category].items():
            full_path = os.path.join(BASE, rel_path)
            if not os.path.isfile(full_path):
                errors.append(f"Path not found: {rel_path} ({full_path})")

    script_path = source_map.get("drift_detection", {}).get("script")
    if script_path:
        full_path = os.path.join(BASE, script_path)
        if not os.path.isfile(full_path):
            errors.append(f"Script path not found: {script_path}")
    else:
        errors.append("drift_detection.script not defined in source_map.json")

    if errors:
        print("SOURCE_MAP_FAIL")
        for e in errors:
            print(f"  FAIL: {e}")
        return 1

    print("SOURCE_MAP_OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
