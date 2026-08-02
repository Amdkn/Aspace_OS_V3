#!/usr/bin/env python3
"""tri.py — applique la regle runs>=5 OU last_active<14j sur les 112 agents.

Source: agents.json + multica agent tasks <id>.
Sortie: tri.csv (id, name, runs, last_active, decision).
"""
import json, csv, subprocess, sys, io
from pathlib import Path

HERE = Path(__file__).parent
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ag = json.loads((HERE / "agents.json").read_text(encoding="utf-8"))

CUTOFF_DAYS = 14
TODAY = "2026-08-02"

rows = []
for i, a in enumerate(ag):
    aid = a["id"]; name = a["name"]
    try:
        r = subprocess.run(
            ["multica", "agent", "tasks", aid, "--output", "json"],
            capture_output=True, timeout=20,
        )
        text = r.stdout.decode("utf-8", errors="replace")
        tasks = json.loads(text) if text.strip() else []
    except Exception as e:
        print(f"  ERR {name}: {e}", file=sys.stderr)
        tasks = []

    runs = len(tasks)
    if tasks:
        last_active = max(
            (t.get("completed_at") or t.get("dispatched_at") or t.get("created_at") or "")
            for t in tasks
        )
    else:
        last_active = ""

    # decision
    active_recent = False
    if last_active and last_active >= "2026-07-19":
        active_recent = True
    keep = runs >= 5 or active_recent
    decision = "KEEP" if keep else "ARCHIVE"

    rows.append({
        "id": aid, "name": name, "runs": runs,
        "last_active": last_active, "decision": decision,
    })
    print(f"  [{i+1:3}/112] {decision:6} runs={runs:4}  last={last_active:20}  {name}")

with (HERE / "tri.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id","name","runs","last_active","decision"])
    w.writeheader(); w.writerows(rows)

keep = sum(1 for r in rows if r["decision"]=="KEEP")
arch = sum(1 for r in rows if r["decision"]=="ARCHIVE")
print(f"\nTOTAL: {len(rows)}  KEEP: {keep}  ARCHIVE: {arch}")
