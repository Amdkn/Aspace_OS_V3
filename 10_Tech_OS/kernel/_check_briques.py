import sqlite3, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
c = sqlite3.connect('uc.db'); c.row_factory = sqlite3.Row
print("blueprints:", [dict(r) for r in c.execute("select id,slug,version from prompt_blueprints")])
print("works:", [tuple(r) for r in c.execute("select id,status from work where id in (67,68,69,70)")])
print("events:", [tuple(r) for r in c.execute("select kind,count(*) from event group by kind")])