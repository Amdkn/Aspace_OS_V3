import pathlib, sqlite3
k=pathlib.Path(r"C:\Users\amado\ASpace_OS_V3\10_Tech_OS\kernel")
db=k/"backups"/"uc-workgraph-v2-shadow.db"
c=sqlite3.connect(db)
c.execute("PRAGMA foreign_keys=ON")
c.executescript((k/"workgraph_v2_goal_capability.sql").read_text(encoding="utf-8"))
print("fk", c.execute("PRAGMA foreign_key_check").fetchall())
print("tables", [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name") if r[0] in {"goal","goal_round","round_work","work_wait","harness_capability"}])
c.execute("INSERT INTO harness_capability(harness,capability,evidence_level,status,evidence_ref) VALUES(?,?,?,?,?)", ("antigravity","AUTH","CANARY","pass","incident-2026-09-19"))
print("cap", c.execute("SELECT harness,capability,evidence_level,status FROM harness_capability").fetchall())
c.commit()
