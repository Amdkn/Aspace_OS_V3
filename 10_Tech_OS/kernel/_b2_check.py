import sqlite3
# contenu du checkpoint : status de 67 ?
c = sqlite3.connect("checkpoints/20260904_074957/uc.db")
print("ckpt status 67:", c.execute("SELECT status, attempts FROM work WHERE id=67").fetchall())
c.close()
c = sqlite3.connect("uc.db")
print("live status 67:", c.execute("SELECT status, attempts FROM work WHERE id=67").fetchall())
c.close()
