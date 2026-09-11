#!/usr/bin/env python3
"""
controleur.py — le battement qui manquait.

CE QUE L'AUDIT A ETABLI (verdent-gpt-5.6-sol, 2026-08-30, verifie ici)
    « V3 possede un genome, une anatomie decrite et plusieurs systemes nerveux
    experimentaux. Il ne possede pas encore de metabolisme ferme. »

    Verifie independamment le 2026-08-30 :
      - dernier evenement de uc.db : 2026-08-03 17:18 (27 jours d'arret)
      - 6 work sur 11 en `failed`, 2 en `claimed` depuis 27 jours
      - AUCUNE tache planifiee ne pilote le kernel
      - worker_example.py fait `time.sleep(0.2)` au lieu de construire

    Les organes existent : gate, claim atomique, reap, prediction, review, DLQ.
    Rien ne les APPELLE. C'est un coeur complet sans systole.

CE QUE CE SCRIPT FAIT, ET NE FAIT PAS
    Il fait battre : a chaque tour il recupere les baux expires, relance le
    travail recuperable, et rend un etat. C'est la boucle 6 -> 2 de la
    definition falsifiable de l'audit -- « survivre a la mort d'un worker »
    puis « reclamer a nouveau ».

    Il NE construit pas. Le constructeur reel est un harness (cc, glm, hermes)
    et ce script ne pretend pas en etre un : il ordonnance, il ne batit pas.
    Confondre les deux est exactement ce que l'audit reproche au worker de
    reference, qui simule la construction par un sleep.

USAGE
    python controleur.py --etat              # diagnostic, n'ecrit rien
    python controleur.py --battre --tours 1  # un tour, effets reels
    python controleur.py --auto-test         # verifie que le battement bat
"""

from __future__ import annotations
import argparse
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ICI = Path(__file__).resolve().parent
DB = ICI / "uc.db"
UC = ICI / "uc.py"

try:
    from engram.beth_filter import BethFilter
    _beth_filter = BethFilter()
except Exception:
    _beth_filter = None

# Un bail de plus de 15 min sans battement est considere mort. Les deux `claimed`
# du 3 aout le sont depuis 27 jours : sans reaper, un worker mort retient son
# travail pour toujours.
BAIL_MORT = timedelta(minutes=15)

# Au-dela, on cesse de relancer. Un echec rejoue a l'infini n'est pas de la
# resilience, c'est P1 au niveau du runtime : la boucle du rejeu.
MAX_TENTATIVES = 3


def cx() -> sqlite3.Connection:
    c = sqlite3.connect(str(DB))
    c.row_factory = sqlite3.Row
    return c


def maintenant() -> datetime:
    return datetime.now(timezone.utc)


def lire_ts(v) -> datetime | None:
    if not v:
        return None
    try:
        d = datetime.fromisoformat(str(v).replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def etat() -> dict:
    if not DB.exists():
        return {"erreur": f"uc.db absent : {DB}"}
    c = cx()
    par_statut = {r["status"]: r["n"] for r in
                  c.execute("SELECT status, COUNT(*) n FROM work GROUP BY status")}
    dernier = c.execute("SELECT MAX(at) a FROM event").fetchone()["a"]
    d = lire_ts(dernier)
    silence = (maintenant() - d) if d else None

    # Les baux morts : reclames et sans battement recent.
    morts = []
    for r in c.execute("SELECT id, title, updated_at FROM work WHERE status='claimed'"):
        u = lire_ts(r["updated_at"])
        if u and maintenant() - u > BAIL_MORT:
            morts.append({"id": r["id"], "titre": r["title"],
                          "depuis_h": round((maintenant() - u).total_seconds() / 3600, 1)})

    # Requeue selective : un work porte une qualification terminale (escalade
    # Donna ou arbitrage Rick) n'est PAS du travail dormant, c'est du dechet
    # tranche. Relancer un tranche, c'est annuler l'arbitrage — le parasite
    # du 2026-09-04. dlq.py rendre exige --autorise ; l'UPDATE direct ne doit
    # jamais le contourner.
    relancables = [dict(r) for r in c.execute(
        "SELECT id, title, attempts FROM work WHERE status='failed' AND attempts < ? "
        "AND NOT EXISTS (SELECT 1 FROM event e WHERE e.work_id=work.id "
        "                AND e.kind IN ('escalade','arbitrage'))",
        (MAX_TENTATIVES,))]
    epuises = c.execute(
        "SELECT COUNT(*) n FROM work WHERE status='failed' AND attempts >= ? "
        "AND NOT EXISTS (SELECT 1 FROM event e WHERE e.work_id=work.id "
        "                AND e.kind IN ('escalade','arbitrage'))",
        (MAX_TENTATIVES,)).fetchone()["n"]

    # Le test de vivance : un runtime silencieux depuis plus d'une heure
    # avec du travail en attente n'est pas au repos, il est arrete.
    # En revanche, sans travail pending/claimed et sans echecs orphelins,
    # il est en veille nominale, pret pour la prochaine vague.
    a_du_travail_en_souffrance = (par_statut.get("pending", 0) > 0 or
                                  par_statut.get("claimed", 0) > 0 or
                                  epuises > 0 or
                                  len(morts) > 0)
    vivant = bool((silence and silence < timedelta(hours=1)) or not a_du_travail_en_souffrance)

    return {
        "par_statut": par_statut,
        "dernier_evenement": dernier,
        "silence_h": round(silence.total_seconds() / 3600, 1) if silence else None,
        "baux_morts": morts,
        "relancables": relancables,
        "epuises": epuises,
        "vivant": vivant,
    }


def afficher(e: dict) -> int:
    if "erreur" in e:
        print(f"  {e['erreur']}")
        return 2
    print("  Etat du runtime\n")
    for s, n in sorted(e["par_statut"].items()):
        print(f"    {n:>4}  {s}")
    print(f"\n  dernier evenement : {e['dernier_evenement']}")
    if e["silence_h"] is not None:
        j = e["silence_h"] / 24
        print(f"  silence           : {e['silence_h']} h ({j:.1f} jours)")
    print(f"  vivant            : {'oui' if e['vivant'] else 'NON'}")

    if e["baux_morts"]:
        print(f"\n  {len(e['baux_morts'])} bail(s) mort(s) — travail retenu par un worker disparu :")
        for m in e["baux_morts"]:
            print(f"    #{m['id']}  depuis {m['depuis_h']} h  {str(m['titre'])[:44]}")
        print("  Sans reaper, ce travail n'est jamais rendu a la file.")

    if e["relancables"]:
        print(f"\n  {len(e['relancables'])} echec(s) relancable(s) (< {MAX_TENTATIVES} tentatives) :")
        for r in e["relancables"]:
            print(f"    #{r['id']}  tent={r['attempts']}  {str(r['title'])[:44]}")
    if e["epuises"]:
        print(f"\n  {e['epuises']} echec(s) epuise(s) — relancer n'est plus de la")
        print("  resilience, c'est du rejeu. Ils demandent un diagnostic humain.")
    return 0 if e["vivant"] else 1


def battre(tours: int, pause: float) -> int:
    """Un tour = recuperer les baux morts, relancer ce qui est recuperable.

    Ce n'est pas de la construction : c'est le systole qui rend le travail
    disponible pour un harness. Sans lui, la file est un cimetiere."""
    if not DB.exists():
        print(f"  uc.db absent : {DB}")
        return 2

    total_reap = total_relance = 0
    for t in range(1, tours + 1):
        e = etat()

        # 1. Recuperer les baux morts. On passe par uc.py reap plutot que par
        #    un UPDATE direct : la CLI est l'autorite, et elle journalise.
        if e["baux_morts"]:
            r = subprocess.run([sys.executable, str(UC), "reap"],
                               capture_output=True, text=True, timeout=60)
            if r.returncode == 0:
                total_reap += len(e["baux_morts"])
                print(f"  tour {t} : {len(e['baux_morts'])} bail(s) recupere(s)")
            else:
                print(f"  tour {t} : reap a echoue — {r.stderr.strip()[:120]}")

        # 2. Rendre les echecs recuperables a la file. Un `failed` sous le
        #    plafond de tentatives est du travail dormant, pas du dechet.
        if e["relancables"]:
            c = cx()
            # Garde-fou en profondeur : re-verifier la qualification terminale
            # a l'instant du write (une qualification peut tomber entre etat()
            # et l'UPDATE). Un id qualifie est retire, jamais relance.
            valid_items = []
            for r in e["relancables"]:
                i = r["id"]
                titre = r.get("title", "")
                if c.execute(
                    "SELECT COUNT(*) n FROM event WHERE work_id=? "
                    "AND kind IN ('escalade','arbitrage')", (i,)).fetchone()["n"] > 0:
                    continue
                # Évaluation Engram Gatekeeper A1 Beth
                if _beth_filter and titre:
                    eval_b = _beth_filter.evaluate_intent(titre)
                    if eval_b.get("veto"):
                        c.execute(
                            "INSERT INTO event(work_id, harness, kind, payload, at) VALUES(?,?,?,?,?)",
                            (i, "beth_gatekeeper", "veto", eval_b.get("reason"),
                             maintenant().isoformat(timespec="seconds")))
                        c.commit()
                        print(f"  tour {t} : veto Beth A1 sur #{i} ({titre[:30]}) -> non relancé")
                        continue
                valid_items.append(i)

            ids = valid_items
            c.executemany(
                "UPDATE work SET status='pending', updated_at=? WHERE id=? AND status='failed'",
                [(maintenant().isoformat(timespec="seconds"), i) for i in ids])
            for i in ids:
                c.execute(
                    "INSERT INTO event(work_id, harness, kind, payload, at) VALUES(?,?,?,?,?)",
                    (i, "controleur", "requeue", "relance apres echec recuperable",
                     maintenant().isoformat(timespec="seconds")))
            c.commit()
            total_relance += len(ids)
            print(f"  tour {t} : {len(ids)} echec(s) rendu(s) a la file")

        if not e["baux_morts"] and not e["relancables"]:
            print(f"  tour {t} : rien a faire")
        if t < tours:
            time.sleep(pause)

    print(f"\n  {total_reap} bail(s) recupere(s), {total_relance} relance(s)")
    print("  Le controleur ORDONNANCE. Il ne construit pas : le constructeur")
    print("  est un harness, et confondre les deux est ce que l'audit reproche")
    print("  au worker de reference qui simule le travail par un sleep.")
    return 0


def auto_test() -> int:
    """Verifie que le battement bat vraiment, sur une base jetable."""
    global DB
    import shutil
    import tempfile
    print("  Auto-test du controleur\n")
    if not DB.exists():
        print("  ECHEC : uc.db absent, rien a tester")
        return 1

    tmp = Path(tempfile.mkdtemp()) / "uc.db"
    shutil.copy2(DB, tmp)
    vraie, DB = DB, tmp
    try:
        avant = etat()
        n_recuperable = len(avant["relancables"])
        if n_recuperable == 0:
            print("  aucun echec recuperable dans la copie — on en fabrique un")
            c = cx()
            c.execute("UPDATE work SET status='failed', attempts=0 "
                      "WHERE id=(SELECT id FROM work LIMIT 1)")
            c.commit()
            n_recuperable = len(etat()["relancables"])

        battre(tours=1, pause=0)
        apres = etat()
        if len(apres["relancables"]) >= n_recuperable and n_recuperable > 0:
            print("\n  ECHEC : les echecs recuperables n'ont pas ete rendus a la file.")
            return 1
        print("\n  OK : le battement rend le travail dormant a la file.")
        print("  (execute sur une COPIE — la base de production n'a pas bouge)")
        return 0
    finally:
        DB = vraie
        shutil.rmtree(tmp.parent, ignore_errors=True)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--etat", action="store_true", help="diagnostic seul, n'ecrit rien")
    p.add_argument("--battre", action="store_true", help="effets reels sur uc.db")
    p.add_argument("--tours", type=int, default=1)
    p.add_argument("--pause", type=float, default=5.0)
    p.add_argument("--auto-test", action="store_true")
    a = p.parse_args()

    if a.auto_test:
        return auto_test()
    if a.battre:
        return battre(a.tours, a.pause)
    return afficher(etat())


if __name__ == "__main__":
    raise SystemExit(main())
