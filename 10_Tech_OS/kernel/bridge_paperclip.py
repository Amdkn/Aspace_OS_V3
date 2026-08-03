#!/usr/bin/env python3
"""bridge_paperclip.py — le watchdog Paperclip parle enfin à Donna.

Sans ce pont, un agent L2 qui échoue en boucle dans Paperclip n'est vu par
personne : il ne remonte ni au 12e Docteur, ni à Donna, ni à Rick. C'est le
garde-fou n°4, et c'était le dernier trou de la chaîne.

Ce que fait le pont, à chaque passage :

  1. lit les runs Paperclip (`paperclipai run list`) ;
  2. pour chaque run en échec ou bloqué, trouve — ou crée — l'item L2
     correspondant dans la file du noyau, identifié par `pc:<runId>` ;
  3. le marque `fail` avec le motif réel ;
  4. laisse `dlq.py` faire son travail : à la 3e tentative, Donna escalade
     vers Rick, qui route vers le 12e Docteur.

Il n'annule rien côté Paperclip et ne décide rien : il transporte l'échec
jusqu'à l'organe qui sait quoi en faire.

    python bridge_paperclip.py scan [--seuil 3] [--limit 50]
    python bridge_paperclip.py boucle [--intervalle 300]
    python bridge_paperclip.py etat
"""
from __future__ import annotations
import argparse, json, os, re, sqlite3, subprocess, sys, time

sys.path.insert(0, os.path.expanduser("~/agentpulse"))
sys.path.insert(0, os.path.expanduser("~"))
from agentpulse.sdk import instrument

instrument(
    task_type="bridge-sync",
    prompt_version=1,
    db_name="kernel-bridge",
)

HERE = os.path.dirname(os.path.abspath(__file__))
UC = os.path.join(HERE, "uc.py")
DLQ = os.path.join(HERE, "dlq.py")
DB = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))
COMPANY = os.environ.get("PAPERCLIP_COMPANY_ID", "7beec325-965f-41b8-b5aa-786deea04bc3")

# Statuts Paperclip qui valent un echec pour nous.
ECHEC = {"failed", "error", "errored", "cancelled", "canceled", "timeout", "timed_out"}
COINCE = {"stuck", "stalled", "blocked"}


def uc(*args) -> dict:
    p = subprocess.run([sys.executable, UC] + [str(a) for a in args],
                       capture_output=True, text=True, timeout=120)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        raise RuntimeError("uc.py illisible: " + (p.stdout or p.stderr)[:160])


def pc(*args, t=120):
    """Appelle paperclipai. Rend (ok, sortie)."""
    exe = "paperclipai"
    npm = "C:/Users/amado/AppData/Roaming/npm/paperclipai.cmd"
    if os.path.exists(npm):
        exe = npm
    p = subprocess.run([exe] + list(args), capture_output=True, text=True,
                       timeout=t, encoding="utf-8", errors="replace")
    return p.returncode == 0, (p.stdout or "") + (p.stderr or "")


def runs(limit: int) -> list[dict]:
    ok, out = pc("run", "list", "--company-id", COMPANY, "--limit", str(limit), "--json")
    if not ok:
        # Le serveur peut etre eteint : ce n'est pas une erreur du pont.
        return []
    try:
        d = json.loads(out)
    except json.JSONDecodeError:
        return []
    return d if isinstance(d, list) else d.get("runs", d.get("data", []))


def work_pour(run_id: str, titre: str) -> int:
    """Un item L2 par run Paperclip, cree une seule fois."""
    c = sqlite3.connect(DB, timeout=10)
    c.row_factory = sqlite3.Row
    marque = "pc:" + run_id
    r = c.execute("SELECT id FROM work WHERE title LIKE ?", (marque + "%",)).fetchone()
    if r:
        return r["id"]
    return uc("submit", "--layer", "L2", "--title", marque + " " + titre[:60])["work_id"]


def deja_signale(work_id: int, run_id: str) -> bool:
    """Ne pas compter deux fois le meme echec du meme run."""
    c = sqlite3.connect(DB, timeout=10)
    for (p,) in c.execute("SELECT payload FROM event WHERE work_id=? AND kind='failed'",
                          (work_id,)):
        if p and run_id in p:
            return True
    return False


def cmd_scan(a):
    lot = runs(a.limit)
    if not lot:
        print(json.dumps({"ok": True, "runs": 0,
                          "note": "aucun run lisible — serveur Paperclip eteint ou file vide"},
                         ensure_ascii=False, indent=1))
        return

    bilan = {"vus": len(lot), "echecs": [], "ignores": 0}
    for r in lot:
        rid = str(r.get("id") or r.get("runId") or "")
        statut = str(r.get("status") or r.get("state") or "").lower()
        titre = str(r.get("title") or r.get("agentName") or r.get("agentId") or "run Paperclip")
        if not rid:
            continue
        if statut not in ECHEC and statut not in COINCE:
            bilan["ignores"] += 1
            continue

        wid = work_pour(rid, titre)
        if deja_signale(wid, rid):
            bilan["ignores"] += 1
            continue

        motif = ("paperclip run " + rid + " statut=" + statut + " : "
                 + str(r.get("error") or r.get("failureReason") or "sans motif fourni")[:180])
        # Reclamation CIBLEE : sans --work, on incrementerait les tentatives d'un autre item.
        uc("claim", "--harness", "paperclip-bridge", "--work", wid, "--lease", "60")
        uc("fail", "--work", wid, "--reason", motif)
        bilan["echecs"].append({"run": rid, "work_id": wid, "statut": statut})

    # Donna qualifie et escalade ce qui a franchi le seuil.
    d = subprocess.run([sys.executable, DLQ, "run", "--seuil", str(a.seuil)],
                       capture_output=True, text=True, timeout=180)
    try:
        bilan["escalade_donna"] = json.loads(d.stdout).get("escalades", [])
    except json.JSONDecodeError:
        bilan["escalade_donna"] = []
    print(json.dumps(bilan, ensure_ascii=False, indent=1))


def cmd_boucle(a):
    print("pont actif, intervalle " + str(a.intervalle) + "s — Ctrl+C pour arreter")
    while True:
        try:
            cmd_scan(a)
        except Exception as e:
            print(json.dumps({"erreur": type(e).__name__ + ": " + str(e)[:160]}))
        time.sleep(a.intervalle)


def cmd_etat(a):
    ok, out = pc("run", "list", "--company-id", COMPANY, "--limit", "1", "--json", t=60)
    c = sqlite3.connect(DB, timeout=10)
    n = c.execute("SELECT count(*) FROM work WHERE title LIKE 'pc:%'").fetchone()[0]
    b = c.execute("SELECT count(*) FROM work WHERE title LIKE 'pc:%' AND status='blocked'").fetchone()[0]
    print(json.dumps({"paperclip_joignable": ok, "items_ponts": n,
                      "escalades_chez_rick": b, "db": DB, "company": COMPANY},
                     ensure_ascii=False, indent=1))


P = argparse.ArgumentParser(description="pont watchdog Paperclip -> Donna -> Rick")
S = P.add_subparsers(dest="cmd", required=True)
p = S.add_parser("scan"); p.add_argument("--seuil", type=int, default=3)
p.add_argument("--limit", type=int, default=50); p.set_defaults(f=cmd_scan)
p = S.add_parser("boucle"); p.add_argument("--intervalle", type=int, default=300)
p.add_argument("--seuil", type=int, default=3); p.add_argument("--limit", type=int, default=50)
p.set_defaults(f=cmd_boucle)
S.add_parser("etat").set_defaults(f=cmd_etat)

if __name__ == "__main__":
    a = P.parse_args(); a.f(a)
