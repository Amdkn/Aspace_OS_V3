import sqlite3, json
c = sqlite3.connect('10_Tech_OS/kernel/uc.db'); c.row_factory = sqlite3.Row
r = c.execute("select * from work where id=38").fetchone()
print(json.dumps(dict(r), indent=1, default=str))
r = c.execute("select * from tape order by id desc limit 1").fetchone()
print(json.dumps(dict(r), default=str))
# works 30-32
for i in (30,31,32):
    print(dict(c.execute("select id,status from work where id=?", (i,)).fetchone()))
print("events:", c.execute("select count(*) from event where kind in ('purge_doublon','qualification_mort')").fetchone()[0])
