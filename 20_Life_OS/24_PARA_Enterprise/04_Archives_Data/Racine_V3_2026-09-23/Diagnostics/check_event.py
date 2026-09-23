import sqlite3
conn = sqlite3.connect('C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db')
cur = conn.cursor()
cur.execute("SELECT MAX(at) FROM event")
print('max at', cur.fetchone())
cur.execute("SELECT work_id, status FROM work WHERE status!='done' AND status!='failed'")
rows = cur.fetchall()
print('non-done/failed', rows)
