import sqlite3, json
c = sqlite3.connect('10_Tech_OS/kernel/uc.db'); c.row_factory = sqlite3.Row
cols = [r[1] for r in c.execute("pragma table_info(work)")]
print("cols:", cols)
for i in (36, 37):
    r = c.execute("select * from work where id=?", (i,)).fetchone()
    if r: print(json.dumps(dict(r), default=str))
for i in (30, 31, 32):
    r = c.execute("select * from work where id=?", (i,)).fetchone()
    print(json.dumps(dict(r), default=str))
