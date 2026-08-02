#!/usr/bin/env python3
"""archive_inaction.py — archive les agents ARCHIVE du tri.csv (les 103 inactifs).

Ne touche PAS les 9 KEEP — decision operateur requise.
"""
import csv, json, subprocess, sys, io
from pathlib import Path

HERE = Path(__file__).parent
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

rows = list(csv.DictReader((HERE / "tri.csv").open(encoding="utf-8")))
to_archive = [r for r in rows if r["decision"] == "ARCHIVE"]
kept       = [r for r in rows if r["decision"] == "KEEP"]

print(f"A archiver: {len(to_archive)}  Conserve (dec. operateur): {len(kept)}")
print("KEEP list:")
for r in kept:
    print(f"  {r['name']!r:40}  runs={r['runs']:>4}  last={r['last_active']}")

print("\n--- ARCHIVE en cours ---")
ok = err = 0
for i, r in enumerate(to_archive, 1):
    proc = subprocess.run(
        ["multica", "agent", "archive", r["id"]],
        capture_output=True, timeout=20,
    )
    if proc.returncode == 0 and b'"archived_at"' in proc.stdout:
        ok += 1
        if i % 10 == 0 or i == len(to_archive):
            print(f"  [{i:3}/{len(to_archive)}] ok={ok} err={err}")
    else:
        err += 1
        print(f"  ERR {r['name']}: rc={proc.returncode} out={proc.stdout[:200]} err={proc.stderr[:200]}")

print(f"\nRESULT: ok={ok}  err={err}")
