# verify_run_simule_0002.py -- Verificateur de la loi du bail (ruban v1).
# Prouve que le reap rend le work de test a la file apres expiration du bail.
# stdlib uniquement : json/os/subprocess/sys/time.

import json
import os
import subprocess
import sys
import time

KERNEL = os.path.dirname(os.path.abspath(__file__))
UC = os.path.join(KERNEL, "uc.py")
DLQ = os.path.join(KERNEL, "dlq.py")
STATE = os.path.join(KERNEL, "run_simule_0002_state.json")
GRACE = 5  # marge de securite sur l'expiration


def run(args, cwd=KERNEL):
    p = subprocess.run([sys.executable] + list(args),
                       capture_output=True, text=True, cwd=cwd)
    return p.returncode, p.stdout, p.stderr


def query_scalar(sql):
    """select count(...) / valeur simple via sqlite3 en sous-processus."""
    code = ("import sqlite3;c=sqlite3.connect('uc.db');"
            "print([tuple(r) for r in c.execute(__import__('sys').argv[1])][0])")
    rc, out, err = run([sys.executable, "-c", code, sql] if False else
                       ["-c", code, sql])
    # note: sys.executable passed via first list element below
    return out.strip(), err


def main():
    errors = []
    if not os.path.exists(STATE):
        print("SIM0002_KO etat de simulation absent: " + STATE)
        return 1
    with open(STATE) as f:
        st = json.load(f)
    wid = st["work_id"]
    print("work de test: id=%d harness=%s lease=%ds" %
          (wid, st["harness"], st["lease_s"]))

    code = ("import sqlite3,sys;c=sqlite3.connect('uc.db');"
            "print([tuple(r) for r in c.execute(sys.argv[1])])")

    def q(sql):
        p = subprocess.run([sys.executable, "-c", code, sql],
                           capture_output=True, text=True, cwd=KERNEL)
        return p.stdout.strip(), p.stderr

    # [1] Etat pre-reap admissible : claimed (bail pose, non encore expiré
    #     au sens reap) OU pending. Mesure directe dans uc.db (lecture seule).
    out, err = q("select status from work where id=%d" % wid)
    status_pre = None
    try:
        status_pre = eval(out)[0][0]
    except Exception as e:
        errors.append("[1] lecture status impossible: %s (%s)" % (out, e))
    ok1 = status_pre in ("pending", "claimed")
    if not ok1:
        errors.append("[1] etat pre-reap non admissible: %s" % status_pre)
    print("[1] pre-reap: status=%s" % status_pre)

    # attendre l'expiration du bail (120 s) puis lancer le reap
    print("attente d'expiration du bail (%d s + %d s de marge)..." %
          (st["lease_s"], GRACE))
    time.sleep(st["lease_s"] + GRACE)
    rc, out, err = run(["-c", "print(1)"])  # no-op sanitaire
    rc, out, err = run([UC, "reap"])
    if rc != 0:
        errors.append("reap rc=%d %s" % (rc, err))
    else:
        print("reap: " + out.strip())

    # [2] apres reap : status=pending, aucune claim active (expires_at future)
    out, err = q("select status from work where id=%d" % wid)
    status_post = None
    try:
        status_post = eval(out)[0][0]
    except Exception as e:
        errors.append("[2] lecture status impossible: %s (%s)" % (out, e))
    if status_post != "pending":
        errors.append("[2] status apres reap = %s (attendu pending)" % status_post)
    c_out, _ = q("select expires_at from claim where work_id=%d" % wid)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        rows = eval(c_out)
    except Exception:
        rows = []
    for row in rows:
        if row and row[0] and row[0] > now:
            errors.append("[2] claim active subsiste: %s" % (row,))
    print("[2] post-reap: status=%s claims=%s" % (status_post, rows))

    # [3] au moins un evenement kind='reap' horodate pour ce work_id
    e_out, _ = q("select at from event where work_id=%d and kind='reap'" % wid)
    try:
        ev_rows = eval(e_out)
    except Exception:
        ev_rows = []
    if not ev_rows:
        errors.append("[3] aucun event 'reap' pour work %d" % wid)
    print("[3] events reap: %s" % (ev_rows,))

    # [4] rendre le work de test a Donna (etat final pending ou failed accepte)
    rc, out, err = run([DLQ, "rendre", "--work", str(wid)])
    print("[4] dlq rendre rc=%d out=%s err=%s" % (rc, out.strip(), err.strip()))
    f_out, _ = q("select status from work where id=%d" % wid)
    try:
        final_status = eval(f_out)[0][0]
    except Exception:
        final_status = None
    if final_status not in ("pending", "failed"):
        errors.append("[4] etat final = %s (attendu pending ou failed)"
                      % final_status)
    print("[4] etat final mesure=%s" % final_status)

    if errors:
        print("SIM0002_KO")
        for e in errors:
            print(" - " + e)
        return 1
    print("SIM0002_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
