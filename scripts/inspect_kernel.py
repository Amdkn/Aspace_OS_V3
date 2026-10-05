import sqlite3, sys, json, os
db = sys.argv[1]
db = os.path.normpath(db)
c = sqlite3.connect(db)
c.row_factory = sqlite3.Row
print("=== tables ===")
for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
    print(r[0])
print("\n=== work cols ===")
print([r[0] for r in c.execute("PRAGMA table_info(work)")])
print("\n=== work 190-205 ===")
for r in c.execute("SELECT * FROM work WHERE id BETWEEN 190 AND 205 ORDER BY id"):
    print(dict(r))
print("\n=== prediction 220-226 ===")
for r in c.execute("SELECT * FROM prediction WHERE id BETWEEN 220 AND 226 ORDER BY id"):
    print(dict(r))
print("\n=== claim rows ===")
for r in c.execute("SELECT * FROM claim"):
    print(dict(r))
print("\n=== session_binding rows ===")
for r in c.execute("SELECT * FROM session_binding"):
    print(dict(r))
print("\n=== work_wait rows ===")
for r in c.execute("SELECT * FROM work_wait"):
    print(dict(r))
print("\n=== event kinds ===")
for r in c.execute("SELECT kind, count(*) FROM event GROUP BY kind"):
    print(r)
print("\n=== work 198 events ===")
for r in c.execute("SELECT id,kind,payload,at FROM event WHERE work_id=198 ORDER BY id"):
    print(r[0], r[1], r[2], r[3])
print("\n=== goals ===")
for r in c.execute("SELECT * FROM goal"):
    print(dict(r))
print("\n=== goal_rounds ===")
for r in c.execute("SELECT * FROM goal_round"):
    print(dict(r))
print("\n=== round_work ===")
for r in c.execute("SELECT * FROM round_work"):
    print(dict(r))
print("\n=== intent ===")
for r in c.execute("SELECT * FROM intent"):
    print(dict(r))
print("\n=== work_intent ===")
for r in c.execute("SELECT * FROM work_intent"):
    print(dict(r))
print("\n=== work_dependency ===")
for r in c.execute("SELECT * FROM work_dependency"):
    print(dict(r))
print("\n=== gate_decision ===")
for r in c.execute("SELECT * FROM gate_decision"):
    print(dict(r))
print("\n=== artifact ===")
for r in c.execute("SELECT * FROM artifact"):
    print(dict(r))