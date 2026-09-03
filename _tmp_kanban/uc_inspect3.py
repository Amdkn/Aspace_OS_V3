import sqlite3, json
c = sqlite3.connect('10_Tech_OS/kernel/uc.db'); c.row_factory = sqlite3.Row
cols = [r[1] for r in c.execute("pragma table_info(tape)")]
print("tape cols:", cols)
for t in (24, 28, 29):
    r = c.execute("select * from tape where id=?", (t,)).fetchone()
    print(json.dumps(dict(r), default=str)[:800] if r else "none")
# doublons 30-32
print("--- works 30/31/32 pre-purge:")
for i in (30,31,32):
    r = c.execute("select id,status,tape_id from work where id=?", (i,)).fetchone()
    print(dict(r))
