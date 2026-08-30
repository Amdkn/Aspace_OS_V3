#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Le forum d'agents -- espace partage asynchrone, avec reservation.

POURQUOI IL EXISTE
    Lors de tests OpenAI, 1 200+ agents ont spontanement utilise un forum
    interne pour echanger 70 000+ messages et se repartir les taches. Ni
    chaine sequentielle, ni point-a-point : espace partage.

    Sur ce poste, l'absence de ce modele a coute deux fois :
      12 aout : 103 node.exe -> STATUS_COMMITMENT_LIMIT
      30 aout : deux boucles concurrentes, 4 tranches brulees en double

    Le second cas est exactement ce que `prendre` empeche.

SCHEMA
    channels / threads / messages / artifacts -- repris tel quel du plan
    Supabase, donc migrable. L'implementation est locale sur fichiers parce
    qu'aucune base n'est cablee ici : une implementation qui suppose une
    infrastructure absente ne tourne pas.
"""

from __future__ import annotations
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FORUM = Path("C:/Users/amado/ASpace_OS_V3/90-self-evolution/reports/forum")

# Une reservation sans peremption gele le fil si l'agent meurt. 45 min :
# au-dela, on considere l'agent perdu et le travail reprenable.
PEREMPTION = timedelta(minutes=45)


def maintenant() -> datetime:
    return datetime.now(timezone.utc)


def fichier(fil: str) -> Path:
    return FORUM / f"{fil}.json"


def charger(fil: str) -> dict:
    try:
        return json.loads(fichier(fil).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def sauver(fil: str, d: dict) -> None:
    FORUM.mkdir(parents=True, exist_ok=True)
    fichier(fil).write_text(json.dumps(d, ensure_ascii=False, indent=2),
                            encoding="utf-8")


def reservation_active(d: dict) -> tuple[str, datetime] | None:
    """Rend (agent, echeance) si une reservation tient encore."""
    r = d.get("reserve")
    if not r:
        return None
    try:
        pris = datetime.fromisoformat(r["a"])
    except (KeyError, ValueError):
        return None
    fin = pris + PEREMPTION
    return (r["agent"], fin) if fin > maintenant() else None


def fils() -> int:
    if not FORUM.is_dir():
        print("  aucun fil ouvert")
        return 0
    trouves = sorted(FORUM.glob("*.json"))
    if not trouves:
        print("  aucun fil ouvert")
        return 0
    print(f"  {len(trouves)} fil(s)\n")
    for f in trouves:
        d = charger(f.stem)
        act = reservation_active(d)
        etat = "CLOS" if d.get("clos") else ("PRIS " + act[0] if act else "libre")
        n = len(d.get("messages", []))
        print(f"    [{etat:>14}]  {f.stem:26} {n:>3} msg  "
              f"{d.get('canal', '?')}")
    return 0


def prendre(fil: str, agent: str) -> int:
    d = charger(fil) or {"fil": fil, "canal": "general", "messages": [],
                         "ouvert": maintenant().isoformat(timespec="seconds")}
    if d.get("clos"):
        print(f"  fil clos — rien a prendre")
        return 1

    act = reservation_active(d)
    if act and act[0] != agent:
        reste = int((act[1] - maintenant()).total_seconds() // 60)
        print(f"  REFUSE — « {fil} » est deja pris par {act[0]}")
        print(f"  (reservation valable encore {reste} min)")
        print("  C'est la garde qui manquait le 30 aout : deux boucles")
        print("  concurrentes avaient brule 4 tranches en double.")
        return 1

    d["reserve"] = {"agent": agent, "a": maintenant().isoformat(timespec="seconds")}
    sauver(fil, d)
    print(f"  « {fil} » reserve par {agent} pour {int(PEREMPTION.total_seconds() // 60)} min.")
    print("  Passe cette peremption, un autre agent peut reprendre :")
    print("  une reservation eternelle gele le fil si l'agent meurt.")
    return 0


def poster(fil: str, agent: str, texte: str, artefact: str | None) -> int:
    d = charger(fil) or {"fil": fil, "canal": "general", "messages": [],
                         "ouvert": maintenant().isoformat(timespec="seconds")}
    if d.get("clos"):
        print("  fil clos")
        return 1

    # Regle du resume contextuel : sans etat de fin, le fil devient un journal
    # que personne ne relit -- et le gain du forum disparait.
    lignes = [L for L in texte.strip().split("\n") if L.strip()]
    resume = bool(lignes) and len(lignes[-1]) < 200
    if not resume:
        print("  ATTENTION : pas de resume contextuel en derniere ligne.")
        print("  Chaque message doit finir par l'etat courant et l'action")
        print("  attendue. Sans ca, le fil se relit en entier — et le gain")
        print("  de contexte du forum est perdu.")

    d.setdefault("messages", []).append({
        "agent": agent,
        "a": maintenant().isoformat(timespec="seconds"),
        "texte": texte,
        "artefact": artefact,
        "resume_contextuel": resume,
    })
    sauver(fil, d)
    print(f"  poste dans « {fil} » par {agent}  ({len(d['messages'])} msg)")
    if artefact:
        existe = Path(artefact).exists()
        print(f"  artefact : {artefact}  {'(present)' if existe else '(INTROUVABLE)'}")
        if not existe:
            print("  Un artefact annonce et absent ment aux agents suivants.")
            return 1
    return 0


def lire(fil: str) -> int:
    d = charger(fil)
    if not d:
        print(f"  fil inconnu : {fil}")
        return 2
    act = reservation_active(d)
    print(f"\n  « {fil} »  canal={d.get('canal', '?')}"
          f"{'  [CLOS]' if d.get('clos') else ''}")
    if act:
        print(f"  pris par {act[0]}")
    print()
    for m in d.get("messages", []):
        print(f"    {m['a'][:16]}  {m['agent']}")
        for L in m["texte"].strip().split("\n"):
            print(f"      {L}")
        if m.get("artefact"):
            print(f"      → {m['artefact']}")
        if not m.get("resume_contextuel"):
            print("      (sans resume contextuel)")
        print()
    return 0


def clore(fil: str, synthese: str) -> int:
    d = charger(fil)
    if not d:
        print(f"  fil inconnu : {fil}")
        return 2
    d["clos"] = maintenant().isoformat(timespec="seconds")
    d["synthese"] = synthese
    d.pop("reserve", None)
    sauver(fil, d)
    print(f"  « {fil} » clos.")
    print("  Archiver la synthese en memoire longue : un forum qui n'archive")
    print("  jamais redevient un historique qui grossit.")
    return 0


def auto_test() -> int:
    """Echoue si la double reservation passe — la garde qui manquait le 30 aout."""
    print("  Auto-test du forum\n")
    fil = "_autotest"
    echecs = 0
    try:
        if fichier(fil).exists():
            fichier(fil).unlink()

        if prendre(fil, "alice") != 0:
            print("  ECHEC : premiere reservation refusee."); echecs += 1

        # LE test : bob ne doit pas pouvoir prendre ce qu'alice tient.
        if prendre(fil, "bob") == 0:
            print("  ECHEC : double reservation acceptee.")
            print("  C'est exactement le defaut du 30 aout.")
            echecs += 1

        # Le meme agent peut reprendre son propre fil.
        if prendre(fil, "alice") != 0:
            print("  ECHEC : l'agent proprietaire ne peut pas reprendre."); echecs += 1

        # Artefact introuvable → doit signaler.
        if poster(fil, "alice", "test\netat : en cours", "C:/inexistant_xyz.md") == 0:
            print("  ECHEC : un artefact absent a ete accepte en silence."); echecs += 1

        if poster(fil, "alice", "vrai message\netat : teste, action : clore",
                  str(fichier(fil))) != 0:
            print("  ECHEC : un artefact present a ete refuse."); echecs += 1

        if len(charger(fil).get("messages", [])) != 2:
            print("  ECHEC : les messages n'ont pas survecu."); echecs += 1
    finally:
        if fichier(fil).exists():
            fichier(fil).unlink()

    print()
    if echecs:
        print(f"  {echecs} regle(s) contournable(s).")
        return 1
    print("  OK : une tache prise ne peut pas etre prise deux fois.")
    return 0


def main(argv: list[str]) -> int:
    def opt(nom: str) -> str | None:
        return argv[argv.index(nom) + 1] if nom in argv and argv.index(nom) + 1 < len(argv) else None

    if len(argv) < 2:
        print(__doc__)
        print("  usage : forum.py fils")
        print("          forum.py prendre <fil> --agent <nom>")
        print("          forum.py poster <fil> --agent <nom> --texte \"...\" [--artefact <p>]")
        print("          forum.py lire <fil> | clore <fil> --synthese \"...\"")
        print("          forum.py --auto-test")
        return 2

    c = argv[1]
    if c == "--auto-test":
        return auto_test()
    if c == "fils":
        return fils()
    if len(argv) < 3:
        print(f"  « {c} » attend un nom de fil")
        return 2
    fil = argv[2]
    if c == "prendre":
        return prendre(fil, opt("--agent") or "anonyme")
    if c == "poster":
        return poster(fil, opt("--agent") or "anonyme",
                      opt("--texte") or "", opt("--artefact"))
    if c == "lire":
        return lire(fil)
    if c == "clore":
        return clore(fil, opt("--synthese") or "")
    print(f"  commande inconnue : {c}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
