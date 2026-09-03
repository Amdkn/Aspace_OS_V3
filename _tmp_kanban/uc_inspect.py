import sqlite3, json
c = sqlite3.connect('10_Tech_OS/kernel/uc.db'); c.row_factory = sqlite3.Row
print([r[0] for r in c.execute("select name from sqlite_master where type='table'")])
cols = [r[1] for r in c.execute("pragma table_info(work)")]
print("cols:", cols)
for r in c.execute("select * from work order by id"):
    d = dict(r)
    print({k: d.get(k) for k in d if k in ('id','title','status','layer','priority','source','origin','created_at','assignee')})
