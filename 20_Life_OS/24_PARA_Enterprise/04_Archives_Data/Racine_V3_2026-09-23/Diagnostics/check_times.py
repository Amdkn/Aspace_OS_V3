import sqlite3
conn = sqlite3.connect('C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db')
cur = conn.cursor()
cur.execute("SELECT MAX(updated_at) FROM work")
print('max work updated', cur.fetchone())
cur.execute("SELECT MAX(created_at) FROM event")
print('max event', cur.fetchone())
cur.execute("SELECT MAX(at) FROM event")
print('max at', cur.fetchone())
