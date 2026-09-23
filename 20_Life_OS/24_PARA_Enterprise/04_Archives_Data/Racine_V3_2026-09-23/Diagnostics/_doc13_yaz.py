# -*- coding: utf-8 -*-
"""Work 146 — Audit sha256 specs vs table tape (uc.db). Usage: python _doc13_yaz.py [audit|fix]"""
import hashlib, os, sqlite3, sys

ROOT = r"C:\Users\amado\ASpace_OS_V3"
SPECS = os.path.join(ROOT, "00_Amadeus", "60_Tape_Specs")
DB = os.path.join(ROOT, "10_Tech_OS", "kernel", "uc.db")

def norm(p):
    return p.replace("\\\\", "\\").replace("/", "\\").lower().strip()

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()

def load_tape():
    cx = sqlite3.connect(DB)
    return {norm(r[0]): (r[0], r[1]) for r in cx.execute("select path, sha256 from tape")}, cx

def audit():
    tape, _ = load_tape()
    matches, drift, unreg = [], [], []
    for fn in sorted(os.listdir(SPECS)):
        if not fn.endswith(".md"):
            continue
        full = os.path.join(SPECS, fn)
        s = sha(full)
        hit = tape.get(norm(full))
        if hit is None:
            unreg.append((fn, full, s))
        elif hit[1] == s:
            matches.append(fn)
        else:
            drift.append((fn, full, s, hit[1]))
    print("SPECS=%d MATCH=%d DRIFT=%d UNREGISTERED=%d TAPE_ROWS=%d" % (
        len(matches) + len(drift) + len(unreg), len(matches), len(drift), len(unreg), len(tape)))
    print("-- DRIFT --")
    for fn, full, s, old in drift:
        print("%s\n  db=%s\n  fs=%s" % (fn, old, s))
    print("-- UNREGISTERED --")
    for fn, full, s in unreg:
        print("%s  %s" % (fn, s))
    return matches, drift, unreg

def fix():
    tape, cx = load_tape()
    cur = cx.cursor()
    resub, inserted = 0, 0
    for fn in sorted(os.listdir(SPECS)):
        if not fn.endswith(".md"):
            continue
        full = os.path.join(SPECS, fn)
        s = sha(full)
        hit = tape.get(norm(full))
        if hit is None:
            cur.execute("insert into tape(path, sha256) values(?,?)", (full, s))
            inserted += 1
        elif hit[1] != s:
            cur.execute("update tape set sha256=? where path=?", (s, hit[0]))
            resub += 1
    cx.commit()
    print("INSERTED=%d RESUBMITTED(drift re-sealed)=%d" % (inserted, resub))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "fix":
        fix()
    else:
        audit()
