import sqlite3
conn = sqlite3.connect('C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db')
cur = conn.cursor()
cur.execute("SELECT work_id, status FROM session_binding WHERE status!='closed'")
print(cur.fetchall())
cur.execute("SELECT COUNT(*) FROM session_binding")
print('total', cur.fetchone()[0])
