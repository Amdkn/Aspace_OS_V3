import sqlite3
conn = sqlite3.connect('C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db')
cur = conn.cursor()
cur.execute("SELECT work_id, session_key, harness, status, started_at, ended_at FROM session_binding WHERE status!='closed'")
for row in cur.fetchall():
    print(row)
