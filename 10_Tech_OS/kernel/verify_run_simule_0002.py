# verify_run_simule_0002.py -- preuve de la loi du bail (work 9)
# Verifie, dans l'ordre :
#  [1] etat pre-reap admissible (pending, ou claimed avec bail expire)
#  [2] apres reap : status=pending, aucune claim active (expires_at future)
#  [3] au moins un event de kind 'reap' horodate pour ce work_id
# Puis rend le work de test a l'etat neutre via dlq.py rendre (Donna).
import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timedelta

KERNEL = os.path.dirname(os.path.abspath(__file__))
UC = os.path.join(KERNEL, "uc.py")
DLQ = os.path.join(KERNEL, "dlq.py")
DB = os.path.join(KERNEL, "uc.db")

erreurs = []


def uc(*args):
    p = subprocess.run([sys.executable, UC] + list(args),
                       capture_output=True, text=True, cwd=KERNEL)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def work_status(wid):
    c = sqlite3.connect(DB)
    row = c.execute("select status from work where id=?", (wid,)).fetchone()
    c.close()
    return row[0] if row else None


def claim_active(wid):
    c = sqlite3.connect(DB)
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    rows = list(c.execute(
        "select expires_at from claim where work_id=? and expires_at > ?",
        (wid, now)))
    c.close()
    return rows


def events_reap(wid):
    c = sqlite3.connect(DB)
    rows = list(c.execute(
        "select kind, at from event where work_id=? and kind like '%reap%'",
        (wid,)))
    c.close()
    return rows


def main():
    sp = os.path.join(KERNEL, "run_simule_0002_state.json")
    if not os.path.exists(sp):
        print("SIM0002_KO state absent, lancer run_simule_0002.py d'abord")
        return 1
    with open(sp) as f:
        state = json.load(f)
    wid = state["work_id"]

    # [1] etat pre-reap : attendre l'expiration du bail
    wait = state.get("expire_wait_s", 130)
    print("[1] attente expiration du bail (%ss)..." % wait)
    time.sleep(wait)
    st = work_status(wid)
    expires = claim_active(wid)
    if st == "pending":
        ok1 = True
    elif st == "claimed" and not expires:
        ok1 = True  # bail expire, reap pas encore tourne : admissible
    else:
        ok1 = False
        erreurs.append("[1] status=%s claims_actives=%s" % (st, expires))
    print("[1] pre-reap status=%s claims_actives=%s -> %s"
          % (st, bool(expires), "OK" if ok1 else "KO"))

    # [2] reap puis verification
    rc, out, err = uc("reap")
    print("[2] reap rc=%s out=%s err=%s" % (rc, out, err))
    if rc != 0:
        erreurs.append("[2] reap rc=%s %s" % (rc, err))
    st2 = work_status(wid)
    actives = claim_active(wid)
    if st2 == "pending" and not actives:
        print("[2] post-reap status=%s claims_actives=0 -> OK" % st2)
    else:
        erreurs.append("[2] post-reap status=%s claims_actives=%s"
                       % (st2, actives))

    # [3] event reap horodate
    evs = events_reap(wid)
    if evs:
        print("[3] events reap: %s -> OK" % evs)
    else:
        erreurs.append("[3] aucun event kind reap pour work %s" % wid)

    # 4. rendre proprement a l'etat neutre (Donna), journaliser l'etat final
    rc, out, err = subprocess.run(
        [sys.executable, DLQ, "rendre", "--work", str(wid)],
        capture_output=True, text=True, cwd=KERNEL).returncode, None, None
    p = subprocess.run([sys.executable, DLQ, "rendre", "--work", str(wid)],
                       capture_output=True, text=True, cwd=KERNEL)
    final = work_status(wid)
    print("[4] dlq rendre rc=%s out=%s etat_final_mesure=%s"
          % (p.returncode, p.stdout.strip(), final))
    if final not in ("pending", "failed"):
        erreurs.append("[4] etat final inattendu: %s" % final)

    if erreurs:
        print("SIM0002_KO")
        for e in erreurs:
            print("  - " + e)
        return 1
    print("SIM0002_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
