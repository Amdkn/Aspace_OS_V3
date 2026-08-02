#!/usr/bin/env python3
"""harness.py — adaptateur de harness, implementation de reference.

Le contrat est la CLI `uc.py`, pas ce fichier : n'importe quel langage peut
l'implementer en appelant les memes verbes et en lisant le JSON. Voir
`00_Amadeus/20_Harness/ADAPTER.md`.

Ce que l'adaptateur garantit, et qu'un appel manuel ne garantit pas :

  - le bail est prolonge tout seul tant que le travail dure ;
  - une exception rend le travail a la file au lieu de le retenir jusqu'a
    expiration — un agent qui plante ne bloque personne ;
  - on ne peut pas rendre un travail sans avoir predit avant.

Usage :

    from harness import Harness

    for item in Harness("cc", layer="L2").run(max_items=1):
        item.predict("lighthouse > 90", 0.7)
        ...  # le travail
        item.review()
"""
from __future__ import annotations
import json, os, subprocess, sys, threading, time

HERE = os.path.dirname(os.path.abspath(__file__))
UC   = os.path.join(HERE, "uc.py")


class HarnessError(RuntimeError):
    pass


class Item:
    """Un travail reclame. A utiliser comme context manager."""

    def __init__(self, h: "Harness", row: dict):
        self.h = h
        self.id = row["id"]
        self.layer = row["layer"]
        self.title = row["title"]
        self.tape_path = row.get("tape_path")
        self.attempts = row["attempts"]
        self._predicted = False
        self._reported = False
        self._stop = threading.Event()
        self._beat: threading.Thread | None = None

    # ---------------------------------------------------------------- bail
    def _pulse(self):
        while not self._stop.wait(self.h.beat_every):
            try:
                self.h._uc("beat", "--work", self.id, "--harness", self.h.name,
                           "--lease", self.h.lease)
            except Exception:
                pass  # le reap reprendra le travail, c'est le filet

    def __enter__(self) -> "Item":
        self._beat = threading.Thread(target=self._pulse, daemon=True)
        self._beat.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        self._stop.set()
        if not self._reported:
            # Un plantage ne doit jamais retenir un bail jusqu'a expiration.
            reason = f"{exc_type.__name__}: {exc}" if exc else "sorti sans rendre de verdict"
            try:
                self.fail(reason)
            except Exception:
                pass
        return False  # on ne masque pas l'exception

    # ------------------------------------------------------------- verdict
    def predict(self, claim: str, confidence: float) -> int:
        """Obligatoire avant tout verdict. Ecrite AVANT l'execution."""
        if not 0.0 < confidence < 1.0:
            raise ValueError("confiance attendue dans ]0,1[")
        r = self.h._uc("predict", "--work", self.id, "--claim", claim,
                       "--confidence", confidence)
        self._predicted = True
        return r["prediction_id"]

    def review(self):
        if not self._predicted:
            raise HarnessError(
                "loi_prediction: appeler predict() avant review() — une prediction "
                "posterieure a l'acte est une justification, pas une verification")
        self.h._uc("review", "--work", self.id)
        self._reported = True

    def fail(self, reason: str | None = None):
        args = ["fail", "--work", self.id]
        if reason:
            args += ["--reason", reason[:400]]
        self.h._uc(*args)
        self._reported = True

    def __repr__(self):
        return f"<Item {self.id} {self.layer} {self.title!r}>"


class Harness:
    """Un harness qui tire du travail de la file."""

    def __init__(self, name: str, layer: str | None = None, lease: int = 300,
                 beat_every: int | None = None, db: str | None = None,
                 python: str | None = None):
        self.name = name
        self.layer = layer
        self.lease = lease
        self.beat_every = beat_every or max(10, lease // 3)
        self.python = python or sys.executable
        self.env = dict(os.environ)
        if db:
            self.env["ASPACE_DB"] = db

    def _uc(self, *args) -> dict:
        cmd = [self.python, UC] + [str(a) for a in args]
        p = subprocess.run(cmd, capture_output=True, text=True, env=self.env, timeout=60)
        if p.returncode != 0 and not p.stdout.strip():
            raise HarnessError(f"uc.py {args[0]} a echoue: {p.stderr.strip()[:300]}")
        try:
            r = json.loads(p.stdout)
        except json.JSONDecodeError:
            raise HarnessError(f"reponse illisible de uc.py: {p.stdout[:200]}")
        if r.get("ok") is False:
            raise HarnessError(r.get("err", "erreur inconnue"))
        return r

    def claim(self) -> Item | None:
        args = ["claim", "--harness", self.name, "--lease", self.lease]
        if self.layer:
            args += ["--layer", self.layer]
        row = self._uc(*args).get("work")
        return Item(self, row) if row else None

    def reap(self) -> list[int]:
        return self._uc("reap")["reclames"]

    def run(self, max_items: int | None = None, poll: float = 5.0,
            idle_timeout: float | None = None):
        """Boucle : reap, claim, cede l'item, recommence.

        Chaque item est cede DANS son context manager : le bail bat tout seul et
        une exception dans le corps de la boucle rend le travail a la file.
        """
        seen, idle = 0, 0.0
        while max_items is None or seen < max_items:
            self.reap()
            item = self.claim()
            if item is None:
                if idle_timeout is not None and idle >= idle_timeout:
                    return
                time.sleep(poll)
                idle += poll
                continue
            idle = 0.0
            seen += 1
            with item:
                yield item


if __name__ == "__main__":
    h = Harness(sys.argv[1] if len(sys.argv) > 1 else "cc")
    print(json.dumps({"harness": h.name, "lease": h.lease,
                      "beat_every": h.beat_every, "uc": UC}, indent=1))
