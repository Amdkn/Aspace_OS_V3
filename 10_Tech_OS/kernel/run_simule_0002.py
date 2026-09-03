# run_simule_0002.py -- simulation de l'epreuve bail (work 9, Nardole)
# Un worker fantome (nardole_sim_l2) claim un work de test, bail 120 s,
# puis meurt sans rendre le travail : ni done, ni fail, ni abandon.
# Loi testee : la loi du bail doit rendre le work a la file tout seul.
import json
import os
import subprocess
import sys
import time

KERNEL = os.path.dirname(os.path.abspath(__file__))
UC = os.path.join(KERNEL, "uc.py")
HARNESS = "nardole_sim_l2"
LEASE = 120


def uc(*args):
    p = subprocess.run(
        [sys.executable, UC] + list(args),
        capture_output=True, text=True, cwd=KERNEL,
    )
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def main():
    # 1. submit du work de test, parent 9
    rc, out, err = uc("submit", "--layer", "L2",
                      "--title", "pc:run-simule-0002 nardole sim epreuve bail",
                      "--parent", "9")
    if rc != 0:
        print("SIM0002_KO submit rc=%s %s %s" % (rc, out, err))
        return 1
    data = json.loads(out)
    if not data.get("ok"):
        print("SIM0002_KO submit refuse: %s" % out)
        return 1
    work_id = data["work_id"]
    print("work de test cree: %s" % work_id)

    # 2. claim par le worker fantome, bail 120 s
    rc, out, err = uc("claim", "--harness", HARNESS,
                      "--work", str(work_id), "--lease", str(LEASE))
    if rc != 0:
        print("SIM0002_KO claim rc=%s %s %s" % (rc, out, err))
        return 1
    data = json.loads(out)
    if not data.get("ok"):
        print("SIM0002_KO claim refuse: %s" % out)
        return 1
    claimed_at = data["work"]["updated_at"]
    print("claim nardole_sim_l2 pose: %s (bail %ss)" % (claimed_at, LEASE))

    # 3. mort sans rendre le travail : aucune commande uc.py de plus.
    #    Ecrit l'etat de la simulation pour le verifier.
    state = {
        "work_id": work_id,
        "harness": HARNESS,
        "lease": LEASE,
        "claimed_at": claimed_at,
        "expire_wait_s": LEASE + 10,
    }
    with open(os.path.join(KERNEL, "run_simule_0002_state.json"), "w") as f:
        json.dump(state, f)
    print("worker mort sans rendre le travail (simulation de mort).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
