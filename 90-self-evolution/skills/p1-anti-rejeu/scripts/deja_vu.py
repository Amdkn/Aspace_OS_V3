#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ce brief a-t-il deja tourne ?

POURQUOI CE SCRIPT EXISTE
    Mesure du 2026-08-30 : l'unicite des intentions passe de 80,5 % en juillet
    a 32,3 % en aout. 978 sessions sur 2 307 rejouent un brief deja formule.
    Un systeme qui ne sait pas qu'il se repete ne peut pas s'arreter.

CE QU'IL NE FAIT PAS
    Il ne decide rien. Il rend un compte et des dates ; l'arbitrage appartient
    au proprietaire. Un rejeu conscient est une decision, un rejeu ignore est
    une panne -- la difference tient entierement a ce qui est montre avant.

LE SEUIL EST UN CHOIX, PAS UNE VERITE
    « Meme intention » = 120 premiers caracteres normalises identiques. Un
    brief reformule compte comme neuf. Le taux rendu est donc un PLANCHER.
"""

from __future__ import annotations
import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

# La console Windows est en cp1252 et leve sur le premier caractere hors table
# (« × », « — »). Un script qui meurt en affichant son resultat a mesure juste
# et n'a rien rendu : c'est un instrument qui ment par omission.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SUBSTRAT = Path("C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/05_Sessions.jsonl")
EMPREINTE = 120

# Mesure de reference, figee au 2026-08-30. Le test de verification echoue si
# la mesure s'en ecarte : c'est ce qui fait de ce script un instrument plutot
# qu'un affichage.
TAUX_REFERENCE = 42.4
TOLERANCE = 2.0


def norme(s: str) -> str:
    """Minuscules, accents retires, ponctuation reduite a l'espace.

    Sans le retrait des accents, « Genere » et « Génère » seraient deux
    intentions distinctes et le taux de rejeu serait sous-estime."""
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", " ", s).strip()


def charger() -> list[tuple[str, str]]:
    """(date, intention normalisee) pour chaque session exploitable."""
    if not SUBSTRAT.exists():
        print(f"  substrat introuvable : {SUBSTRAT}", file=sys.stderr)
        return []
    out = []
    for ligne in SUBSTRAT.read_text(encoding="utf-8", errors="ignore").splitlines():
        try:
            e = json.loads(ligne)
        except json.JSONDecodeError:
            continue
        titre = (e.get("titre") or "").strip()
        if len(titre) < 12:          # « ok », « /model » : du bruit, pas une intention
            continue
        out.append(((e.get("modifie") or "?")[:10], norme(titre)))
    return out


def chercher(brief: str) -> int:
    items = charger()
    if not items:
        return 2
    cible = norme(brief)[:EMPREINTE]
    if not cible:
        print("  brief vide apres normalisation", file=sys.stderr)
        return 2

    # DEFAUT PAYE LE 2026-08-30 : la comparaison exacte sur 120 caracteres
    # rendait « INEDIT » pour un GARDE-FOU present 65 fois dans le corpus. Un
    # brief retape a la main diverge toujours un peu du brief colle a
    # l'origine. Un detecteur de rejeu qui rate le brief le plus rejoue du
    # corpus n'est pas prudent, il est faux.
    #
    # On compare donc sur un prefixe court, puis on se replie sur le
    # recouvrement de mots. Mieux vaut signaler un rejeu de trop -- le
    # proprietaire tranche -- que de rater celui qui coute 96 sessions.
    PREFIXE = 45
    trouves = [(d, t) for d, t in items if t[:PREFIXE] == cible[:PREFIXE]]

    if not trouves:
        mots = set(cible.split())
        if len(mots) >= 4:
            proches = []
            for d, t in items:
                autres = set(t.split())
                if not autres:
                    continue
                # Jaccard : robuste a l'ordre et aux mots ajoutes.
                j = len(mots & autres) / len(mots | autres)
                if j >= 0.55:
                    proches.append((d, t))
            if proches:
                print(f"  VOISIN — {len(proches)} intentions tres proches "
                      f"(recouvrement >= 55 %), sans etre identiques.")
                for d, t in sorted(proches)[:5]:
                    print(f"    {d}  {t[:62]}")
                print("\n  Reformulation probable d'un brief existant.")
                print("  Verifier ce qu'il a produit avant de le relancer.")
                return 1

    n = len(trouves)

    if n == 0:
        print(f"  INEDIT — aucune des {len(items):,} intentions ne correspond.")
        print("  Executer normalement.")
        return 0

    dates = sorted(d for d, _ in trouves)
    print(f"  DEJA VU — ce brief a tourne {n} fois.")
    print(f"  premiere : {dates[0]}     derniere : {dates[-1]}")
    # Grouper par jour : lister 65 dates identiques a l'unite noie le signal
    # sous sa propre repetition -- exactement le defaut qu'on veut montrer.
    par_jour = collections.Counter(dates)
    if len(par_jour) > 1:
        print("  par jour :", "  ".join(f"{d}×{c}" for d, c in sorted(par_jour.items())))

    print()
    if n >= 5:
        print("  >= 5 occurrences — regle D.E.A.L. : ca REMBOURSE.")
        print("  La conversion en skill n'est plus une proposition, c'est une dette.")
    elif n >= 3:
        print("  >= 3 occurrences — regle D.E.A.L. : ca AUTOMATISE.")
        print("  Proposer la conversion en skill, et NOMMER ce qu'elle remplace.")
    else:
        print("  Montrer au proprietaire ce que les executions precedentes ont produit")
        print("  AVANT de proposer de relancer.")

    print()
    print("  Eliminer avant d'automatiser : D.E.A.L. commence par E. Si ce brief")
    print("  est rejoue, demander POURQUOI il ne tient pas. Figer un gaspillage")
    print("  en skill ne le retire pas.")
    return 1


def auto_test() -> int:
    """Rejoue la mesure du rapport. Echoue si l'instrument a derive."""
    items = charger()
    if not items:
        print("  ECHEC : substrat illisible")
        return 1

    cpt = collections.Counter(t[:EMPREINTE] for _, t in items)
    rejoues = sum(n for n in cpt.values() if n > 1)
    taux = 100 * rejoues / len(items)

    print(f"  sessions       : {len(items):,}")
    print(f"  intentions     : {len(cpt):,} uniques")
    print(f"  rejouees       : {rejoues:,}  ({taux:.1f} %)")
    print(f"  reference      : {TAUX_REFERENCE} %  (mesure du 2026-08-30)")

    ecart = abs(taux - TAUX_REFERENCE)
    if ecart > TOLERANCE:
        print(f"\n  ECHEC : ecart de {ecart:.1f} pts, tolerance {TOLERANCE}.")
        print("  Soit le corpus a bouge, soit ce script a cesse de mesurer ce")
        print("  qu'il pretend. Reparer l'instrument, jamais ajuster le chiffre.")
        return 1

    print(f"\n  OK : ecart {ecart:.1f} pt, dans la tolerance.")
    print("\n  Les 5 briefs les plus rejoues :")
    for t, n in cpt.most_common(5):
        print(f"    {n:>4}x  {t[:64]}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        print("  usage : deja_vu.py \"<debut du brief>\"")
        print("          deja_vu.py --auto-test")
        return 2
    if argv[1] == "--auto-test":
        return auto_test()
    return chercher(" ".join(argv[1:]))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
