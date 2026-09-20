import json, sqlite3, subprocess, sys

def run(*args):
    r = subprocess.run([sys.executable, "graham_checkpoint.py", *args],
                       capture_output=True, text=True)
    print(args[0], "rc:", r.returncode, r.stdout.strip()[:160], r.stderr.strip()[:160])
    return r

def q(sql):
    c = sqlite3.connect("uc.db")
    r = c.execute(sql).fetchall()
    c.close()
    return r

# 0. etat initial : remettre 67 en claimed via SQL direct (comme un claim ferait)
c = sqlite3.connect("uc.db")
c.execute("UPDATE work SET status='claimed', attempts=1 WHERE id=67")
c.commit(); c.close()

# 1. checkpoint AVANT la carte
r = run("save", "--work", "67")
ckpt = json.loads(r.stdout)["checkpoint"]

# 2. la carte casse : mutation destructive
c = sqlite3.connect("uc.db")
c.execute("UPDATE work SET status='failed', attempts=9 WHERE id=67")
c.commit(); c.close()
print("after break:", q("SELECT status,attempts FROM work WHERE id=67"))

# 3. restore
run("restore", "--work", "67")

# 4. verifier
st, at = q("SELECT status,attempts FROM work WHERE id=67")[0]
ev = [e[0] for e in q("SELECT kind FROM event WHERE work_id=67 AND harness='graham_checkpoint' AND kind IN ('checkpoint_save','checkpoint_restore') ORDER BY id")]
print("after restore:", st, at, "| events:", ev)
ok = st == "claimed" and at == 1 and ev.count("checkpoint_save") >= 1 and "checkpoint_restore" in ev
print("TEST_B2:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
