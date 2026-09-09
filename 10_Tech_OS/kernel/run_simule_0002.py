# run_simule_0002.py -- Epreuve de la loi du bail (ruban v1, work 9).
# Un worker fantome (nardole_sim_l2) claim un work de test dedie, puis meurt
# sans jamais rendre le travail (aucun done, aucun abandon explicite).
# stdlib uniquement : json/os/subprocess/sys/time.

import json
import os
import subprocess
import sys
import time

HARNESS = "nardole_sim_l2"
LEASE = 120
KERNEL = os.path.dirname(os.path.abspath(__file__))
UC = os.path.join(KERNEL, "uc.py")


def run_uc(args):
    p = subprocess.run([sys.executable, UC] + args,
                       capture_output=True, text=True, cwd=KERNEL)
    return p.returncode, p.stdout, p.stderr


def main():
    # 1. Soumettre le work de test (le script cree lui-meme son item).
    rc, out, err = run_uc(["submit", "--layer", "L2",
                           "--title", "pc:run-simule-0002 nardole sim epreuve bail",
                           "--parent", "9"])
    if rc != 0:
        print("SIM0002_KO submit rc=%d %s %s" % (rc, out, err))
        return 1
    data = json.loads(out)
    if not data.get("ok") or "work_id" not in data:
        print("SIM0002_KO submit refuse: " + out)
        return 1
    wid = data["work_id"]
    print("work de test cree: id=%d" % wid)

    # 2. Claim par le worker fantome, bail 120 s.
    rc, out, err = run_uc(["claim", "--harness", HARNESS,
                           "--work", str(wid), "--lease", str(LEASE)])
    if rc != 0:
        print("SIM0002_KO claim rc=%d %s %s" % (rc, out, err))
        return 1
    data = json.loads(out)
    if not data.get("ok"):
        print("SIM0002_KO claim refuse: " + out)
        return 1
    expires = data.get("work", {}).get("updated_at") or data.get("expires_at")
    print("claim pose par %s, bail %d s (expires=%s)" % (HARNESS, LEASE, expires))

    # 3. Mort du worker : exit sans rendre le travail.
    state_path = os.path.join(KERNEL, "run_simule_0002_state.json")
    with open(state_path, "w", encoding="ascii") as f:
        json.dump({"work_id": wid, "harness": HARNESS,
                   "claimed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                   "lease_s": LEASE}, f)
    print("worker fantome mort sans rendre le travail (etat: %s)" % state_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
