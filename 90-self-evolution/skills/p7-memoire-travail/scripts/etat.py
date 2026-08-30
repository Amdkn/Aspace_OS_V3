#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
L'etat de travail verifie -- ce qui reste a faire, pas ce qui s'est passe.

RECURIS (arXiv 2608.24876), APPLIQUE
    « Prior harnesses retrieve against a growing chat history and lose track of
    unresolved goals. » C'est P2 decrit de l'exterieur.

    La regle centrale : « A checker evaluates the tool or environment result
    rather than the model's own claim that the action succeeded. Invoking a
    skill or attempting a tool call is not completion evidence. »

CE QUE CE SCRIPT REFUSE
    Marquer un objectif `fait` sans preuve. Ce n'est pas un avertissement,
    c'est un refus : un `done` sans preuve eteint la vigilance sur ce qui
    n'est pas fini, et c'est pire que de ne rien suivre.
"""

from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ETAT = Path("C:/Users/amado/ASpace_OS_V3/90-self-evolution/reports/etat_courant.json")

# Une preuve doit designer quelque chose d'observable. Ces marqueurs ne
# garantissent pas la verite, ils excluent « c'est fait » comme preuve.
MARQUEURS = ("rc=", "→", "->", "/", "\\", "http", ":", "ko", "octets", "lignes", "%")


def maintenant() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def charger() -> dict:
    try:
        return json.loads(ETAT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def sauver(d: dict) -> None:
    ETAT.parent.mkdir(parents=True, exist_ok=True)
    ETAT.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def ouvrir(tache: str, buts: list[str]) -> int:
    if not buts:
        print("  aucun objectif — un etat sans but ne sert a rien")
        return 2
    sauver({
        "tache": tache,
        "ouvert": maintenant(),
        "buts": [{"n": i + 1, "but": b, "statut": "pending",
                  "preuve": None, "bloqueur": None} for i, b in enumerate(buts)],
    })
    print(f"  {tache} — {len(buts)} objectifs")
    return voir()


def _trouver(d: dict, n: int) -> dict | None:
    return next((g for g in d.get("buts", []) if g["n"] == n), None)


def fait(n: int, preuve: str | None) -> int:
    d = charger()
    g = _trouver(d, n)
    if not g:
        print(f"  objectif {n} inconnu")
        return 2

    if not preuve or not preuve.strip():
        print(f"  REFUSE — objectif {n} : « {g['but']} »")
        print("  Aucune preuve fournie. Recuris : « Invoking a skill or")
        print("  attempting a tool call is not completion evidence. »")
        print("  Donner --preuve avec un resultat d'environnement observable :")
        print("    un chemin de fichier, un rc=, un code HTTP, une sortie reelle.")
        return 1

    if not any(m in preuve.lower() for m in MARQUEURS):
        print(f"  REFUSE — objectif {n} : la preuve ne designe rien d'observable.")
        print(f"    donnee : « {preuve} »")
        print("  Une preuve pointe vers un fichier, un code de retour, une sortie.")
        print("  « c'est fait » decrit une intention, pas un resultat.")
        return 1

    g["statut"] = "done"
    g["preuve"] = preuve
    g["bloqueur"] = None
    g["a"] = maintenant()
    sauver(d)
    print(f"  objectif {n} : done")
    return voir()


def bloque(n: int, raison: str | None) -> int:
    d = charger()
    g = _trouver(d, n)
    if not g:
        print(f"  objectif {n} inconnu")
        return 2
    if not raison:
        print("  un blocage sans raison est invisible a la reprise")
        return 2
    g["statut"] = "blocked"
    g["bloqueur"] = raison
    sauver(d)
    print(f"  objectif {n} : blocked")
    return voir()


def voir() -> int:
    d = charger()
    if not d:
        print("  aucun etat ouvert")
        return 0

    print(f"\n  {d.get('tache', '(sans titre)')}")
    reste = 0
    for g in d.get("buts", []):
        marque = {"done": "[x]", "blocked": "[!]", "pending": "[ ]"}.get(g["statut"], "[?]")
        print(f"    {marque} {g['n']}. {g['but']}")
        if g["statut"] == "done":
            print(f"          preuve : {g['preuve']}")
        elif g["statut"] == "blocked":
            print(f"          bloque : {g['bloqueur']}")
            reste += 1
        else:
            reste += 1

    print(f"\n  {reste} objectif(s) non resolu(s).")
    if reste == 0:
        print("  Tous les objectifs portent une preuve d'environnement.")
    else:
        print("  A relire APRES compaction — c'est cet etat qui fait foi,")
        print("  pas l'historique de conversation.")
    return 0


def auto_test() -> int:
    """Echoue si la regle de preuve peut etre contournee. C'est le seul
    comportement qui rendrait cette skill nuisible."""
    print("  Auto-test de la regle de preuve\n")
    sauvegarde = ETAT.read_text(encoding="utf-8") if ETAT.exists() else None
    echecs = 0
    try:
        ouvrir("auto-test", ["but temoin"])

        # 1. sans preuve → doit REFUSER
        if fait(1, None) == 0:
            print("  ECHEC : un `done` sans preuve a ete accepte.")
            echecs += 1

        # 2. preuve vide de sens → doit REFUSER
        if fait(1, "c'est fait") == 0:
            print("  ECHEC : « c'est fait » a ete accepte comme preuve.")
            echecs += 1

        # 3. preuve observable → doit ACCEPTER
        if fait(1, "portee.py --auto-test → rc=0") != 0:
            print("  ECHEC : une preuve observable a ete refusee.")
            echecs += 1

        # 4. persistance
        if charger().get("buts", [{}])[0].get("statut") != "done":
            print("  ECHEC : l'etat n'a pas survecu a la relecture.")
            echecs += 1
    finally:
        if sauvegarde is not None:
            ETAT.write_text(sauvegarde, encoding="utf-8")
        elif ETAT.exists():
            ETAT.unlink()

    print()
    if echecs:
        print(f"  {echecs} regle(s) contournable(s). La skill est nuisible en l'etat.")
        return 1
    print("  OK : sans preuve observable, aucun objectif ne passe a `done`.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        print("  usage : etat.py ouvrir \"<tache>\" \"<but>\" ...")
        print("          etat.py fait <n> --preuve \"<resultat observable>\"")
        print("          etat.py bloque <n> --raison \"<pourquoi>\"")
        print("          etat.py voir | --auto-test")
        return 2

    cmd = argv[1]
    if cmd == "--auto-test":
        return auto_test()
    if cmd == "voir":
        return voir()
    if cmd == "ouvrir":
        return ouvrir(argv[2] if len(argv) > 2 else "(sans titre)", argv[3:])
    if cmd in ("fait", "bloque"):
        if len(argv) < 3 or not argv[2].isdigit():
            print(f"  usage : etat.py {cmd} <n> --{'preuve' if cmd == 'fait' else 'raison'} \"...\"")
            return 2
        n = int(argv[2])
        drapeau = "--preuve" if cmd == "fait" else "--raison"
        val = argv[argv.index(drapeau) + 1] if drapeau in argv else None
        return fait(n, val) if cmd == "fait" else bloque(n, val)

    print(f"  commande inconnue : {cmd}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
