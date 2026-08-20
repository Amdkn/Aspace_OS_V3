"""Appose le verdict humain sur un lot de concepts OKF.

POURQUOI CE SCRIPT EXISTE
C'est le seul verrou qu'aucun agent ne peut poser a la place du proprietaire
du produit : faire passer un concept de `confiance: machine` a
`confiance: humain`. Jusqu'ici ce geste n'avait aucun outil — il fallait
ouvrir 37 fichiers et editer du YAML a la main, ce qui est exactement la
raison pour laquelle la revue mourait apres l'ecoute du podcast.

Le niveau de confiance OKF v0.2 se DEDUIT de `verified` : au moins un acteur
`human:<id>` => revu par un humain. Ce script n'ecrit donc pas un champ
`confiance` — il ajoute l'acteur humain, et le niveau suit mecaniquement.
Ecrire les deux permettrait qu'ils divergent.

CE QU'IL REFUSE
- un fichier sans frontmatter : ce n'est pas un concept OKF ;
- un fichier deja tamponne par le meme humain : le geste est idempotent,
  relancer un lot ne cree pas de doublons ;
- d'ecrire quoi que ce soit sans --appliquer. Par defaut il montre.

Un tampon appose a tort est plus couteux qu'un tampon absent : il fait
passer une affirmation non verifiee pour une decision du proprietaire.
"""

import argparse
import io
import os
import re
import sys

V3 = r"C:\Users\amado\ASpace_OS_V3"


def decoupe(texte):
    """Rend (avant, frontmatter, apres) ou None si pas de frontmatter."""
    if not texte.startswith("---"):
        return None
    fin = texte.find("\n---", 3)
    if fin == -1:
        return None
    return texte[:3], texte[3:fin], texte[fin:]


def deja_humain(fm, acteur):
    """Vrai si cet acteur figure deja dans le bloc `verified`."""
    m = re.search(r"^verified:\s*$(.*?)(?=^\S|\Z)", fm, re.M | re.S)
    return bool(m) and acteur in m.group(1)


def niveau(fm):
    m = re.search(r"^verified:\s*$(.*?)(?=^\S|\Z)", fm, re.M | re.S)
    if not m or not m.group(1).strip():
        return "non verifie"
    return "humain" if "human:" in m.group(1) else "machine"


def tamponner(fm, acteur, quand, version, note):
    """Ajoute l'acteur humain au bloc `verified`, et la trace de la revue.

    Si `verified:` existe, on ajoute une entree a sa liste — jamais on ne la
    remplace : les verifications machine anterieures restent, elles disent
    quel processus a produit le concept.
    """
    entree = f"  - {{ by: {acteur}, at: {quand} }}"
    m = re.search(r"^verified:\s*$(.*?)(?=^\S|\Z)", fm, re.M | re.S)
    if m:
        bloc = m.group(1).rstrip("\n")
        fm = fm[:m.start(1)] + bloc + "\n" + entree + "\n" + fm[m.end(1):]
    else:
        # Pas de bloc : on l'insere juste apres `generated:`, qui est
        # toujours present dans OKF v0.2 et precede `verified` par convention.
        g = re.search(r"^generated:.*$", fm, re.M)
        pos = g.end() if g else len(fm.rstrip())
        fm = fm[:pos] + f"\nverified:\n{entree}" + fm[pos:]

    # La trace de la revue : quelle vague, quelle version, quel jugement.
    # Elle vit a cote de `verified` parce qu'elle en explique la provenance.
    if "review:" not in fm:
        trace = (f"\nreview:\n  version: {version}\n"
                 f"  by: {acteur}\n  at: {quand}\n  note: \"{note}\"")
        v = re.search(r"^verified:\s*$(.*?)(?=^\S|\Z)", fm, re.M | re.S)
        pos = v.end(1) if v else len(fm.rstrip())
        fm = fm[:pos].rstrip("\n") + trace + "\n" + fm[pos:]
    return fm


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("lots", nargs="+",
                   help="dossiers de concepts, relatifs a ASpace_OS_V3")
    p.add_argument("--acteur", default="human:amdkn")
    p.add_argument("--at", required=True, help="horodatage ISO 8601 (UTC)")
    p.add_argument("--version", default="V0")
    p.add_argument("--note", default="")
    p.add_argument("--appliquer", action="store_true",
                   help="sans ce drapeau, rien n'est ecrit")
    a = p.parse_args()

    total, tamponnes, sautes, refuses = 0, 0, 0, 0
    for lot in a.lots:
        d = lot if os.path.isabs(lot) else os.path.join(V3, lot)
        if not os.path.isdir(d):
            print(f"REFUS  dossier absent : {lot}", file=sys.stderr)
            refuses += 1
            continue
        fichiers = sorted(n for n in os.listdir(d)
                          if n.endswith(".md") and n != "index.md")
        print(f"\n=== {lot} — {len(fichiers)} concepts ===")
        for n in fichiers:
            chemin = os.path.join(d, n)
            texte = io.open(chemin, encoding="utf-8").read()
            total += 1
            parts = decoupe(texte)
            if not parts:
                print(f"  REFUS   {n} — pas de frontmatter OKF")
                refuses += 1
                continue
            tete, fm, queue = parts
            if deja_humain(fm, a.acteur):
                print(f"  saute   {n} — deja tamponne par {a.acteur}")
                sautes += 1
                continue
            avant = niveau(fm)
            neuf = tamponner(fm, a.acteur, a.at, a.version, a.note)
            print(f"  tampon  {n}  [{avant} -> humain]")
            tamponnes += 1
            if a.appliquer:
                io.open(chemin, "w", encoding="utf-8").write(tete + neuf + queue)

    mode = "APPLIQUE" if a.appliquer else "SIMULATION (ajouter --appliquer)"
    print(f"\n{mode}")
    print(f"  lus       : {total}")
    print(f"  tamponnes : {tamponnes}")
    print(f"  sautes    : {sautes}")
    print(f"  refuses   : {refuses}")
    if not a.appliquer and tamponnes:
        print("\nAucun fichier n'a ete modifie.")


if __name__ == "__main__":
    main()
