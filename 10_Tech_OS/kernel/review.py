#!/usr/bin/env python3
"""review.py — le reviewer. Détache, ou refuse.

Consomme les items en `review`. Pour chacun : relit le critère d'acceptation du
ruban, exige une **preuve** par critère, score la prédiction, et détache
seulement si tout est prouvé.

Le principe : un reviewer ne peut pas savoir si le travail est fait. Il ne
constate pas, il **exige des preuves**. Un critère sans attestation vaut faux.

    python review.py run [--exec] [--max N]
    python review.py show --work N
"""
from __future__ import annotations
import argparse, json, os, re, shlex, subprocess, sys, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
UC   = os.path.join(HERE, "uc.py")
DB   = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))

# Un critère exécutable : une case à cocher qui contient une commande entre accents graves.
CMD = re.compile(r"`([^`]+)`")


def uc(*args) -> dict:
    p = subprocess.run([sys.executable, UC] + [str(a) for a in args],
                       capture_output=True, text=True, timeout=120)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"uc.py illisible: {p.stdout[:150]}{p.stderr[:150]}")


def cx():
    c = sqlite3.connect(DB, timeout=10)
    c.row_factory = sqlite3.Row
    return c


def criteres(tape_path: str | None) -> list[str]:
    """Extrait les lignes du bloc `## Critère d'acceptation`."""
    if not tape_path or not os.path.exists(tape_path):
        return []
    txt = open(tape_path, encoding="utf-8", errors="ignore").read()
    out, dedans = [], False
    for line in txt.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            t = m.group(1).lower()
            dedans = t.startswith("critère d'acc") or t.startswith("critere d'acc")
            continue
        if dedans and line.strip():
            out.append(line.strip())
    return out


def preuves(work_id: int) -> dict[int, dict]:
    c = cx()
    d: dict[int, dict] = {}
    for r in c.execute("SELECT payload FROM event WHERE work_id=? AND kind='evidence' ORDER BY id",
                       (work_id,)):
        p = json.loads(r["payload"])
        d[int(p["criterion"])] = p          # la dernière attestation gagne
    return d


def executer(ligne: str, cwd: str) -> tuple[bool, str] | None:
    """Si le critère porte une commande, l'exécuter et en faire une preuve."""
    m = CMD.search(ligne)
    if not m:
        return None
    cmd = m.group(1).strip()
    try:
        p = subprocess.run(shlex.split(cmd), cwd=cwd, capture_output=True,
                           text=True, timeout=300)
        return p.returncode == 0, f"exit={p.returncode} {(p.stderr or p.stdout).strip()[:160]}"
    except Exception as e:
        return False, f"{type(e).__name__}: {str(e)[:160]}"


def cmd_show(a):
    c = cx()
    w = c.execute("SELECT w.*, t.path tape FROM work w LEFT JOIN tape t ON t.id=w.tape_id "
                  "WHERE w.id=?", (a.work,)).fetchone()
    if not w:
        print(json.dumps({"err": "item inconnu"})); return
    cs = criteres(w["tape"]); pv = preuves(a.work)
    print(json.dumps({"work": dict(w), "criteres": cs,
                      "preuves": {str(k): v for k, v in pv.items()}},
                     ensure_ascii=False, indent=1))


def cmd_run(a):
    c = cx()
    items = [dict(r) for r in c.execute(
        "SELECT w.id, w.title, w.layer, t.path tape FROM work w "
        "LEFT JOIN tape t ON t.id=w.tape_id WHERE w.status='review' ORDER BY w.id")]
    if a.max:
        items = items[:a.max]
    bilan = {"detaches": [], "refuses": []}

    for it in items:
        cs = criteres(it["tape"])
        pv = preuves(it["id"])
        detail, manquants = [], []

        if not cs:
            manquants.append("le ruban ne porte aucun critère d'acceptation lisible")

        for i, ligne in enumerate(cs):
            if i in pv:
                ok = bool(pv[i]["ok"])
                detail.append({"i": i, "critere": ligne, "ok": ok,
                               "source": "attestation", "note": pv[i].get("note")})
                if not ok:
                    manquants.append(f"critère {i} attesté en échec : {ligne}")
                continue
            r = executer(ligne, os.path.dirname(it["tape"] or HERE)) if a.exec else None
            if r is None:
                manquants.append(f"critère {i} sans preuve : {ligne}")
                detail.append({"i": i, "critere": ligne, "ok": None, "source": "aucune"})
            else:
                ok, note = r
                uc("attest", "--work", it["id"], "--criterion", i,
                   "--ok", 1 if ok else 0, "--harness", "reviewer", "--note", note)
                detail.append({"i": i, "critere": ligne, "ok": ok,
                               "source": "execution", "note": note})
                if not ok:
                    manquants.append(f"critère {i} exécuté en échec : {ligne} → {note}")

        passe = not manquants

        # La prédiction est scorée dans les deux cas : c'est ce qui alimente la calibration.
        for r in c.execute("SELECT id FROM prediction WHERE work_id=? AND outcome IS NULL",
                           (it["id"],)):
            uc("score", "--prediction", r["id"], "--outcome", 1 if passe else 0)

        if passe:
            uc("done", "--work", it["id"])
            bilan["detaches"].append({"work_id": it["id"], "title": it["title"],
                                      "criteres": len(cs)})
        else:
            uc("fail", "--work", it["id"], "--reason", " | ".join(manquants)[:400])
            bilan["refuses"].append({"work_id": it["id"], "title": it["title"],
                                     "manques": manquants, "detail": detail})

    print(json.dumps(bilan, ensure_ascii=False, indent=1))


P = argparse.ArgumentParser(description="reviewer A'Space V3 — détache ou refuse")
S = P.add_subparsers(dest="cmd", required=True)
p = S.add_parser("run")
p.add_argument("--exec", action="store_true",
               help="exécuter les critères qui portent une commande entre accents graves")
p.add_argument("--max", type=int); p.set_defaults(f=cmd_run)
p = S.add_parser("show"); p.add_argument("--work", type=int, required=True); p.set_defaults(f=cmd_show)

if __name__ == "__main__":
    a = P.parse_args(); a.f(a)
