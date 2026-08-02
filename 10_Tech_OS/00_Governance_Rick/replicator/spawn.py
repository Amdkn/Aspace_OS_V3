#!/usr/bin/env python3
"""spawn.py — le mécanisme de reproduction des trois OS.

C'est l'organe que V2 n'a jamais eu : le **copieur**. Il duplique le gabarit d'un
Core sans l'interpréter, en substituant seulement les paramètres de couche, puis
matérialise un dossier par compagnon.

Le gabarit est le ruban φ d'un Core. Le même gabarit produit le Kernel Core du
13e, le Life Core du 11e et le Buzz Core du 12e — c'est ce qui fait du Tech OS un
constructeur *universel* et non trois constructions séparées.

    python spawn.py --list
    python spawn.py --core 13
    python spawn.py --all [--force]
"""
from __future__ import annotations
import argparse, json, os, shutil, sys

HERE  = os.path.dirname(os.path.abspath(__file__))
V3    = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TPL   = os.path.join(HERE, "core.template")
CORES = os.path.join(HERE, "cores.json")

DEVOIRS = {
    "Spec": (
        "- rédige le ruban, le dépose au portier de la couche\n"
        "- le corrige tant qu'il échoue au test du ruban\n"
        "- **n'a pas le droit** de bâtir ni de détacher\n"
    ),
    "Build": (
        "- `claim` → `predict` → bâtit → `attest` chaque critère → `review`\n"
        "- **n'a pas le droit** de prononcer `done`\n"
    ),
    "Spawn": (
        "- duplique un ruban éprouvé **en aveugle**, sans le réinterpréter\n"
        "- soumet la descendance à la file\n"
        "- **n'a pas le droit** de modifier le ruban qu'il copie\n"
    ),
}


def charge() -> dict:
    with open(CORES, encoding="utf-8") as f:
        return json.load(f)


def substitue(txt: str, c: dict) -> str:
    """Substitution aveugle : le copieur ne comprend pas ce qu'il copie."""
    v = {
        "{{DOCTOR}}": c["doctor"], "{{CORE}}": c["core"], "{{LAYER}}": c["layer"],
        "{{OS}}": c["os"], "{{DEST}}": c["dest"], "{{MISSION}}": c["mission"],
        "{{MAITRISE}}": c.get("maitrise", c["os"]),
        "{{R_SPEC}}": c["roles"]["spec"], "{{R_BUILD}}": c["roles"]["build"],
        "{{R_SPAWN}}": c["roles"]["spawn"], "{{R_REVIEW}}": c["roles"]["review"],
    }
    for k, val in v.items():
        txt = txt.replace(k, val)
    return txt


def fiche_compagnon(k: dict, c: dict) -> str:
    return (
        f"# {k['nom']} — {k['specialite']}\n\n"
        f"> Compagnon du {c['doctor']} · couche `{c['layer']}` · organe **{k['organe']}**\n\n"
        "**Fichier engendré.** Source : `10_Tech_OS/00_Governance_Rick/replicator/`.\n"
        "Toute modification directe sera écrasée au prochain `spawn.py --force`.\n\n"
        "## Spécialité\n\n"
        f"`{k['specialite']}` — héritée de la structure V2, conservée parce qu'elle porte un\n"
        "savoir de domaine que le seul nom d'organe ne porte pas.\n\n"
        "## Organe\n\n"
        f"**{k['organe']}** dans le constructeur universel. Verbes du contrat\n"
        "(`00_Amadeus/20_Harness/ADAPTER.md`) :\n\n"
        + DEVOIRS[k["organe"]]
        + "\n## Escalade\n\n"
        f"Échec simple → {c['doctor']}. Échec répété (3 tentatives) → Donna\n"
        "(`10_Tech_OS/kernel/dlq.py`) → Rick, en Super Uplink.\n"
    )


def engendre(cle: str, c: dict, force: bool) -> dict:
    dest = os.path.join(V3, c["dest"].replace("/", os.sep))
    if os.path.exists(dest) and not force:
        return {"core": cle, "etat": "existe deja", "dest": c["dest"]}

    ecrits = []
    for racine, _, fichiers in os.walk(TPL):
        rel = os.path.relpath(racine, TPL)
        cible = dest if rel == "." else os.path.join(dest, rel)
        os.makedirs(cible, exist_ok=True)
        for f in fichiers:
            src, dst = os.path.join(racine, f), os.path.join(cible, f)
            if f.endswith(".md"):
                with open(src, encoding="utf-8") as fh:
                    contenu = substitue(fh.read(), c)
                with open(dst, "w", encoding="utf-8") as fh:
                    fh.write(contenu)
            else:
                shutil.copy2(src, dst)
            ecrits.append(os.path.relpath(dst, V3).replace(os.sep, "/"))

    os.makedirs(os.path.join(dest, "tapes"), exist_ok=True)
    open(os.path.join(dest, "tapes", ".gitkeep"), "w").close()

    # --force doit purger les compagnons obsoletes, sinon un ancien roster survit.
    cdir = os.path.join(dest, "compagnons")
    if force and os.path.isdir(cdir):
        shutil.rmtree(cdir)

    # Un dossier par compagnon : sa spécialité héritée, son organe von Neumann.
    comp = []
    for k in c.get("compagnons", []):
        for rel in k.get("dossiers", [f"{k['n']}_{k['nom']}_{k['specialite']}"]):
            d = os.path.join(dest, "compagnons", *rel.split("/"))
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "AGENT.md"), "w", encoding="utf-8") as fh:
                fh.write(fiche_compagnon(k, c))
            comp.append(rel)

    return {"core": cle, "etat": "engendre", "dest": c["dest"],
            "fichiers": len(ecrits), "compagnons": comp}


P = argparse.ArgumentParser(description="réplicateur des Cores A'Space V3")
P.add_argument("--core", help="clé du Core à engendrer (13, 11, 12)")
P.add_argument("--all", action="store_true")
P.add_argument("--list", action="store_true")
P.add_argument("--force", action="store_true", help="réécrire un Core existant")
a = P.parse_args()

cores = charge()
if a.list:
    print(json.dumps({k: {"doctor": v["doctor"], "core": v["core"], "layer": v["layer"],
                          "dest": v["dest"], "harness": v.get("harness"),
                          "compagnons": [f"{x['nom']} ({x['specialite']}/{x['organe']})"
                                         for x in v.get("compagnons", [])]}
                      for k, v in cores.items()}, ensure_ascii=False, indent=1))
    sys.exit(0)

cibles = list(cores) if a.all else ([a.core] if a.core else [])
if not cibles:
    P.error("préciser --core CLE, ou --all, ou --list")
print(json.dumps([engendre(k, cores[k], a.force) for k in cibles],
                 ensure_ascii=False, indent=1))
