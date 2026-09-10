#!/usr/bin/env python3
"""dlq.py — Donna, réceptionniste des erreurs.

Donna siège sous Rick. Elle reçoit ce que l'uplink des compagnons n'a pas résolu
et que le Docteur de la couche n'a pas su corriger. Elle ne répare rien : elle
**qualifie** et **escalade** au Super Uplink de Rick.

Sans elle, un échec répété reste `failed` dans un coin et personne ne le voit —
c'est exactement comme ça qu'un système autonome s'arrête sans prévenir.

    python dlq.py run [--seuil 3]     # échecs répétés -> blocked, escaladés à Rick
    python dlq.py rapport             # ce qu'il y a sur le bureau de Rick
    python dlq.py rendre --work N     # Rick a tranché : retour en file
"""
from __future__ import annotations
import argparse, json, os, re, sqlite3, subprocess, sys
from datetime import date
from collections import Counter

sys.path.insert(0, os.path.expanduser("~/agentpulse"))
sys.path.insert(0, os.path.expanduser("~"))
try:
    from agentpulse.sdk import instrument
    instrument(
        task_type="dlq-triage",
        prompt_version=1,
        db_name="kernel-dlq",
    )
except ImportError:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
UC   = os.path.join(HERE, "uc.py")
DB   = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))


def cx():
    c = sqlite3.connect(DB, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    return c


def uc(*args) -> dict:
    p = subprocess.run([sys.executable, UC] + [str(a) for a in args],
                       capture_output=True, text=True, timeout=60)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"uc.py illisible: {p.stdout[:150]}")


def dernier_motif(c, work_id: int) -> str:
    r = c.execute("SELECT payload FROM event WHERE work_id=? AND kind='failed' "
                  "ORDER BY id DESC LIMIT 1", (work_id,)).fetchone()
    if not r or not r["payload"]:
        return "motif non enregistré"
    return (json.loads(r["payload"]).get("reason") or "motif vide").strip()


def famille(motif: str) -> str:
    """Regroupe les motifs : Rick doit voir des causes, pas des lignes."""
    m = motif.lower()
    if "sans preuve" in m or "attestation" in m:      return "preuve manquante"
    if "aucun critère" in m or "aucun critere" in m:  return "ruban sans critère"
    if "exécuté en échec" in m or "execute en echec" in m: return "critère exécuté en échec"
    if "attesté en échec" in m or "atteste en echec" in m: return "critère attesté en échec"
    if "sorti sans rendre" in m:                      return "harness disparu"
    if re.search(r"error|exception|traceback", m):    return "plantage harness"
    return "autre"


def est_terminal(c, work_id: int) -> bool:
    """Vrai si Rick a pose une cloture terminale sur ce work (event arbitrage
    avec terminal=true). Un failed arbitre terminal n'est plus une DLQ."""
    r = c.execute("SELECT payload FROM event WHERE work_id=? AND kind='arbitrage' "
                  "ORDER BY id DESC LIMIT 1", (work_id,)).fetchone()
    if not r or not r["payload"]:
        return False
    try:
        return bool(json.loads(r["payload"]).get("terminal"))
    except json.JSONDecodeError:
        return False


def cmd_run(a):
    c = cx()
    pris = []
    for r in c.execute("SELECT id, title, layer, attempts FROM work "
                       "WHERE status='failed' AND attempts >= ? ORDER BY id", (a.seuil,)):
        if est_terminal(c, r["id"]):
            continue
        motif = dernier_motif(c, r["id"])
        c.execute("UPDATE work SET status='blocked' WHERE id=?", (r["id"],))
        c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
                  (r["id"], "donna", "escalade",
                   json.dumps({"vers": "rick", "tentatives": r["attempts"],
                               "famille": famille(motif), "motif": motif},
                              ensure_ascii=False)))
        pris.append({"work_id": r["id"], "title": r["title"], "layer": r["layer"],
                     "tentatives": r["attempts"], "famille": famille(motif)})
    print(json.dumps({"seuil": a.seuil, "escalades": pris}, ensure_ascii=False, indent=1))


def cmd_rapport(a):
    c = cx()
    lignes = []
    for r in c.execute("SELECT id, title, layer, attempts FROM work "
                       "WHERE status='blocked' ORDER BY id"):
        e = c.execute("SELECT payload FROM event WHERE work_id=? AND kind='escalade' "
                      "ORDER BY id DESC LIMIT 1", (r["id"],)).fetchone()
        p = json.loads(e["payload"]) if e and e["payload"] else {}
        lignes.append({"work_id": r["id"], "layer": r["layer"], "title": r["title"],
                       "tentatives": r["attempts"], "famille": p.get("famille"),
                       "motif": (p.get("motif") or "")[:180]})
    fam = Counter(l["famille"] for l in lignes)
    couche = Counter(l["layer"] for l in lignes)
    print(json.dumps({"bureau_de_rick": lignes,
                      "par_famille": dict(fam.most_common()),
                      "par_couche": dict(couche.most_common()),
                      "verdict": ("rien a arbitrer" if not lignes else
                                  f"{len(lignes)} dossier(s) attendent Rick")},
                     ensure_ascii=False, indent=1))


def cmd_rendre(a):
    """Retour en file UNIQUEMENT si Rick l'autorise explicitement (--autorise).

    Sans --autorise, refus : c'est ce requeue silencieux qui a fait tourner le
    ping-pong failed/requeue des works fantomes 47/48/71/72/73 (2026-09-04).
    """
    c = cx()
    if not a.autorise:
        print(json.dumps({"ok": False,
                          "erreur": "requeue refuse: passer --autorise \"<justification Rick>\""},
                         ensure_ascii=False))
        sys.exit(3)
    c.execute("UPDATE work SET status='pending', attempts=0 WHERE id=? AND status='blocked'",
              (a.work,))
    ok = c.total_changes > 0
    if ok:
        c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
                  (a.work, "rick", "arbitrage",
                   json.dumps({"decision": "requeue autorise: " + (a.note or "remis en file"),
                               "autorise_par": "rick"}, ensure_ascii=False)))
    print(json.dumps({"ok": ok, "work_id": a.work}, ensure_ascii=False))


def cmd_cloturer(a):
    """Cloture TERMINALE d'un blocked: decision Rick, pas de requeue possible.

    Contourne loi_detachement (done exige review) parce que le verdict n'est pas
    une construction reussie mais un constat: doublon/vestige/fantome d'un
    objectif DEJA prouve par le parent. Statut 'failed' definitive (le seul
    etat terminal accessible depuis blocked), attempts fige, reason horodatee.
    """
    c = cx()
    r = c.execute("SELECT id, status FROM work WHERE id=?", (a.work,)).fetchone()
    if not r or r["status"] != "blocked":
        print(json.dumps({"ok": False,
                          "erreur": f"work {a.work} absent ou non blocked"}, ensure_ascii=False))
        sys.exit(3)
    c.execute("UPDATE work SET status='failed' WHERE id=?", (a.work,))
    c.execute("DELETE FROM claim WHERE work_id=?", (a.work,))
    c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
              (a.work, "rick", "arbitrage",
               json.dumps({"decision": "CLOTURE TERMINALE: " + a.motif,
                           "terminal": True, "autorise_par": "rick"},
                          ensure_ascii=False)))
    print(json.dumps({"ok": True, "work_id": a.work, "status": "failed (terminal)"},
                     ensure_ascii=False))


def cmd_intent(a):
    """Donna rédige l'intent.md de diagnostic d'un échec qualifié.

    Ne décide rien : elle documente (famille d'échec + preuve) et dépose dans
    _INBOX/S1_Rick/ en DRAFT. Rick tranche -> FROZEN -> Yaz spec -> cycle.
    """
    c = cx()
    r = c.execute("SELECT id, title, layer, attempts FROM work WHERE id=?",
                  (a.work,)).fetchone()
    if not r:
        print(json.dumps({"ok": False, "erreur": f"work {a.work} inexistant"},
                         ensure_ascii=False)); return
    e = c.execute("SELECT payload FROM event WHERE work_id=? AND kind='escalade' "
                  "ORDER BY id DESC LIMIT 1", (a.work,)).fetchone()
    p = json.loads(e["payload"]) if e and e["payload"] else {}
    motif = p.get("motif") or dernier_motif(c, a.work)
    fam = p.get("famille") or famille(motif)
    today = date.today().isoformat()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", r["title"])[:40].strip("-").lower()
    inbox = os.path.join(os.path.dirname(DB), "..", "..", "_INBOX", "S1_Rick")
    inbox = os.path.abspath(inbox)
    os.makedirs(inbox, exist_ok=True)
    dest = os.path.join(inbox, f"intent-diagnostic-work{a.work}-{today}.md")
    txt = f"""# INTENT: diagnostic-work{a.work}
**Layer:** {r["layer"] or "L0"}
**Originator:** Donna (dlq.py) — maintenance autonome
**Date:** {today}
**Statut:** DRAFT

## 1. Irritant réel

Échec répété (famille : {fam}) sur le work {a.work} « {r["title"]} »,
{r["attempts"]} tentative(s). Le work est en attente d'arbitrage Rick ; sans
tranche, il bloque la branche et l'opérateur redevient le superviseur.

Motif enregistré : {motif[:400]}

## 2. Résultat visé (mesurable)

Le work {a.work} ressort de l'arbitrage avec un statut terminal vérifiable :
soit `pending` (rendre) soit `done`, et plus aucun échec de la famille
« {fam} » n'atteint {a.seuil} tentatives au prochain passage de `dlq.py run`.

## 3. Contraintes non-négociables

- Blast radius : {a.blast}
- Aucun contournement de la preuve : les critères restent exécutables.
- La tranche appartient à Rick ; Donna ne modifie pas le statut elle-même.

## 4. Definition of Done

- [ ] `python 10_Tech_OS/kernel/dlq.py rapport` ne liste plus le work {a.work}
- [ ] `python 10_Tech_OS/kernel/uc.py status` rend `{r["layer"] or "L0"}` done/pending sans `blocked`
"""
    with open(dest, "w", encoding="utf-8") as f:
        f.write(txt)
    print(json.dumps({"ok": True, "intent": os.path.relpath(dest, os.path.dirname(DB)),
                      "famille": fam}, ensure_ascii=False))


P = argparse.ArgumentParser(description="Donna — DLQ et Super Uplink vers Rick")
S = P.add_subparsers(dest="cmd", required=True)
p = S.add_parser("run"); p.add_argument("--seuil", type=int, default=3); p.set_defaults(f=cmd_run)
S.add_parser("rapport").set_defaults(f=cmd_rapport)
p = S.add_parser("rendre"); p.add_argument("--work", type=int, required=True)
p.add_argument("--note")
p.add_argument("--autorise", help="justification Rick obligatoire pour tout requeue")
p.set_defaults(f=cmd_rendre)
p = S.add_parser("cloturer"); p.add_argument("--work", type=int, required=True)
p.add_argument("--motif", required=True)
p.set_defaults(f=cmd_cloturer)
p = S.add_parser("intent"); p.add_argument("--work", type=int, required=True)
p.add_argument("--seuil", type=int, default=3)
p.add_argument("--blast", default="dossiers touchés : aucun au-delà du work cité ; interdits : kernel/uc.db en écriture directe, 00_Amadeus/")
p.set_defaults(f=cmd_intent)


if __name__ == "__main__":
    a = P.parse_args(); a.f(a)
