import sqlite3, sys
db = sys.argv[1]
c = sqlite3.connect(db)
c.row_factory = None
print("work sql:", c.execute("SELECT sql FROM sqlite_master WHERE name='work'").fetchone())
print("work cols:", c.execute("PRAGMA table_info(work)").fetchall())
print("work_wait sql:", c.execute("SELECT sql FROM sqlite_master WHERE name='work_wait'").fetchone())
print("work 198:", c.execute("SELECT * FROM work WHERE id=198").fetchone())
print("work_wait 198:", c.execute("SELECT * FROM work_wait WHERE work_id=198").fetchone())
c.close()