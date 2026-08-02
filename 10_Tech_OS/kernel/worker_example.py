#!/usr/bin/env python3
"""worker_example.py — worker de reference.

Le plus petit harness conforme au contrat. Tout harness reel (cc, hermes, orca,
codex, antigravity...) se ramene a cette forme : reclamer, predire, travailler,
rendre un verdict.

    python worker_example.py --harness cc --layer L2 --max 1
"""
import argparse, random, time
from harness import Harness

p = argparse.ArgumentParser()
p.add_argument("--harness", required=True)
p.add_argument("--layer", choices=["A0", "L0", "L1", "L2"])
p.add_argument("--max", type=int, default=1)
p.add_argument("--lease", type=int, default=60)
p.add_argument("--boom", action="store_true",
               help="lever une exception pendant le travail, pour prouver que le "
                    "travail retourne a la file au lieu d'etre retenu")
a = p.parse_args()

h = Harness(a.harness, layer=a.layer, lease=a.lease)

for item in h.run(max_items=a.max, idle_timeout=0):
    print(f"[{a.harness}] reclame {item}")

    # 1. Predire AVANT d'agir. La base refuse le verdict sans cette ligne.
    item.predict(f"{item.title} aboutit du premier coup", confidence=0.6)

    # 2. Le travail. Ici : un stub. Dans un vrai harness, c'est le constructeur
    #    qui lit le ruban (item.tape_path) et batit.
    if a.boom:
        raise RuntimeError("le harness plante en plein travail")
    time.sleep(0.2)

    # 3. Le verdict. review = pret a etre detache, fail = rendu a la file.
    if random.random() < 0.9:
        item.review()
        print(f"[{a.harness}] {item.id} -> review")
    else:
        item.fail("critere d'acceptation non atteint")
        print(f"[{a.harness}] {item.id} -> failed")
