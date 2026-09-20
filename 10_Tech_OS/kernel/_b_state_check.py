import sqlite3, os
c = sqlite3.connect(r'C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db')
print('tables:', [r[0] for r in c.execute("select name from sqlite_master where type='table'")])
print('cols prompt_blueprints:', [r[1] for r in c.execute("pragma table_info(prompt_blueprints)")])
print('blueprints:', list(c.execute("select slug,version,sha256 from prompt_blueprints")))
print('cols events:', [r[1] for r in c.execute("pragma table_info(events)")])
print('work:', list(c.execute("select id,status,substr(title,1,60) from work order by rowid desc limit 15")))
print('recent events:', list(c.execute("select kind,substr(coalesce(payload,''),1,100) from event order by rowid desc limit 10")))
for d in ['50_Distillation','60_Implementation_Meth','70_Onthologies']:
    for root in [r'C:/Users/amado/ASpace_OS_V3', r'C:/Users/amado/ASpace_OS_V3/10_Tech_OS']:
        p = os.path.join(root, d)
        print(d, '->', p, os.path.isdir(p) and os.listdir(p))
