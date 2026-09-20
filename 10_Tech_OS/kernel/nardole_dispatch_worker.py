import sqlite3
import json
import os
import datetime

db_path = r"c:\Users\amado\ASpace_OS_V3\10_Tech_OS\kernel\uc.db"
report = {
    "timestamp": datetime.datetime.now().isoformat(),
    "db_found": False,
    "counts": {},
    "pending_tasks": [],
    "active_leases": [],
    "status": "balanced"
}

if os.path.exists(db_path):
    report["db_found"] = True
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [r[0] for r in cur.fetchall()]
    report["tables"] = tables
    
    if "work" in tables:
        cur.execute("SELECT status, count(*) FROM work GROUP BY status;")
        report["counts"] = dict(cur.fetchall())
        
        cur.execute("SELECT id, tape_id, layer, title, status, priority, attempts, updated_at FROM work WHERE status='pending' LIMIT 10;")
        report["pending_tasks"] = [
            {"id": r[0], "tape_id": r[1], "layer": r[2], "title": r[3], "status": r[4], "priority": r[5], "attempts": r[6], "updated_at": r[7]}
            for r in cur.fetchall()
        ]
        
    if "lease" in tables:
        cur.execute("SELECT work_id, worker_id, expires_at, heartbeat_at FROM lease LIMIT 10;")
        report["active_leases"] = [
            {"work_id": r[0], "worker_id": r[1], "expires_at": r[2], "heartbeat_at": r[3]}
            for r in cur.fetchall()
        ]
        
    conn.close()

out_dir = r"c:\Users\amado\ASpace_OS_V3\10_Tech_OS\reports"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "nardole_kanban_dispatch.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Nardole dispatch audit complete. File: {out_file}")
print("Work summary:", report.get("counts"))
print(f"Pending tasks count: {len(report['pending_tasks'])}, Active leases: {len(report.get('active_leases', []))}")
