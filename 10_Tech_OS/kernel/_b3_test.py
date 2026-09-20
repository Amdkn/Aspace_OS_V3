import json, shutil, sqlite3, subprocess, sys, os, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

# 1. copie de travail de uc.db (jamais la prod pour le test brut)
tmp = os.path.join(tempfile.mkdtemp(), "test.db")
shutil.copy2(os.path.join(HERE, "uc.db"), tmp)

c = sqlite3.connect(tmp)
c.executescript(open(os.path.join(HERE, "schema.sql"), encoding="utf-8").read())
c.commit()
tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
c.close()
need = ["prompt_blueprints", "domain_rules_b2", "marvel_personas_b3"]
print("tables:", tables)
ok1 = all(t in tables for t in need)

# 2. migration de la prod via uc.py init (schema idempotent, ADR-0007)
r = subprocess.run([sys.executable, "uc.py", "init"], cwd=HERE, capture_output=True, text=True)
print("uc.py init rc:", r.returncode)
init = json.loads(r.stdout)
ok2 = all(t in init["tables"] for t in need)
print("init tables:", init["tables"])

print("TEST_B3:", "PASS" if ok1 and ok2 else "FAIL")
sys.exit(0 if ok1 and ok2 else 1)
