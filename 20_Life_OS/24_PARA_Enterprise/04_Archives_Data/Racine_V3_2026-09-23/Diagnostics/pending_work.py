import sqlite3
conn = sqlite3.connect('C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db')
cur = conn.cursor()
cur.execute("SELECT id, layer, title, status FROM work WHERE status='pending' ORDER BY id")
rows = cur.fetchall()
for r in rows:
    print(r)
