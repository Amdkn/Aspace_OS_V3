#!/usr/bin/env python3
"""gate.py — le portier.

Prend une note deposee dans `_INBOX/<portier>/`, lui applique le test du ruban
(AGENTS.md §3), et soit la promeut en ruban + item de file, soit la refuse en
disant ce qui manque.

Un portier ne travaille pas : il **admet ou refuse**. C'est du controle
d'admission.

    python gate.py template            # le gabarit de note
    python gate.py check note.md       # test du ruban, sans effet de bord
    python gate.py run [--dry]         # scanne _INBOX et tranche
"""
from __future__ import annotations
import argparse, json, os, re, shutil, subprocess, sys, unicodedata
from datetime import date

sys.path.insert(0, os.path.expanduser("~/agentpulse"))
sys.path.insert(0, os.path.expanduser("~"))
from agentpulse.sdk import instrument

instrument(
    task_type="gate-eval",
    prompt_version=1,
    db_name="kernel-gate",
)

HERE  = os.path.dirname(os.path.abspath(__file__))
V3    = os.path.abspath(os.path.join(HERE, "..", ".."))
INBOX = os.path.join(V3, "_INBOX")
TAPES = os.path.join(V3, "00_Amadeus", "60_Tape_Specs")
UC    = os.path.join(HERE, "uc.py")

# Un portier par couche. Le dossier decide de la couche : pas d'ambiguite.
PORTIERS = {
    "S1_Rick":         "L0",   # noyau, infra, harness
    "A1_Beth_Morty":   "L1",   # identite, observation, vie
    "B1_Jerry_Summer": "L2",   # valeur externe
}

SECTIONS = ["Objectif", "Critère d'acceptation", "Périmètre", "Interdits"]

# Marqueurs de question non resolue : ce sont eux que le test du ruban traque.
BLOQUANTS = re.compile(
    r"\bTODO\b|\bTBD\b|\bFIXME\b|\bXXX\b|à définir|a definir|à confirmer|a confirmer"
    r"|à préciser|a preciser|à voir|a voir|je ne sais pas|on verra|\?\?", re.I)

# Un critere verifiable porte un chiffre, une comparaison, une commande ou une case.
VERIFIABLE = re.compile(r"\d|[<>=]|`[^`]+`|^\s*-\s*\[ \]", re.M)


def slug(s: str, n: int = 48) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return (s or "note")[:n]


def parse(txt: str) -> tuple[dict, dict]:
    """Rend (frontmatter, {section: corps})."""
    fm = {}
    if txt.lstrip().startswith("---"):
        bloc = txt.split("---", 2)
        if len(bloc) >= 3:
            for line in bloc[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip("\"'")
            txt = bloc[2]
    secs, cur = {}, None
    for line in txt.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip()
            secs[cur] = []
        elif cur:
            secs[cur].append(line)
    return fm, {k: "\n".join(v).strip() for k, v in secs.items()}


def test_du_ruban(path: str) -> dict:
    """Le ruban est-il complet ? Binaire, avec la liste de ce qui manque."""
    txt = open(path, encoding="utf-8", errors="ignore").read()
    fm, secs = parse(txt)
    manques: list[str] = []

    if not fm.get("title"):
        manques.append("frontmatter `title:` absent")

    for s in SECTIONS:
        corps = next((v for k, v in secs.items() if k.lower() == s.lower()), None)
        if corps is None:
            manques.append(f"section `## {s}` absente")
        elif len(corps) < 12:
            manques.append(f"section `## {s}` vide ou trop courte")

    acc = next((v for k, v in secs.items() if k.lower().startswith("critère d'acc")
                or k.lower().startswith("critere d'acc")), "")
    if acc and not VERIFIABLE.search(acc):
        manques.append("critère d'acceptation non vérifiable : "
                       "aucun chiffre, comparaison, commande ni case à cocher")

    for m in set(x.group(0) for x in BLOQUANTS.finditer(txt)):
        manques.append(f"question non résolue dans le texte : « {m} »")

    return {"complet": not manques, "manques": manques,
            "title": fm.get("title"), "layer": fm.get("layer")}


def uc(*args) -> dict:
    p = subprocess.run([sys.executable, UC] + [str(a) for a in args],
                       capture_output=True, text=True, timeout=60)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"uc.py illisible: {p.stdout[:150]} {p.stderr[:150]}")


# ------------------------------------------------------------------ commandes
GABARIT = """---
title: "<une phrase, ce qui doit exister a la fin>"
---

## Objectif

<Ce qu'il faut batir. Pas pourquoi : quoi.>

## Critère d'acceptation

Doit contenir au moins un chiffre, une comparaison, une commande ou une case.
- [ ] `commande` retourne 0
- [ ] la page charge en < 2 s

## Périmètre

<Ce qui est dedans. Ce qui est dehors. Le chemin cible.>

## Interdits

<Ce qui ne doit surtout pas arriver. Fichiers a ne pas toucher, actions bannies.>
"""


def cmd_template(a):
    print(GABARIT)


def cmd_check(a):
    r = test_du_ruban(a.fichier)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(0 if r["complet"] else 1)


def cmd_run(a):
    os.makedirs(TAPES, exist_ok=True)
    bilan = {"admis": [], "refuses": []}
    for portier, couche in PORTIERS.items():
        d = os.path.join(INBOX, portier)
        if not os.path.isdir(d):
            continue
        for nom in sorted(os.listdir(d)):
            if not nom.lower().endswith(".md") or nom.startswith("_"):
                continue
            src = os.path.join(d, nom)
            r = test_du_ruban(src)
            layer = r["layer"] if r["layer"] in ("A0", "L0", "L1", "L2") else couche

            if not r["complet"]:
                bilan["refuses"].append({"note": f"{portier}/{nom}", "manques": r["manques"]})
                if a.dry:
                    continue
                rej = os.path.join(INBOX, "_refuses", portier)
                os.makedirs(rej, exist_ok=True)
                with open(os.path.join(rej, nom.replace(".md", ".REFUS.md")), "w",
                          encoding="utf-8") as f:
                    f.write(f"# Refus — {nom}\n\nPortier `{portier}`, {date.today()}.\n\n"
                            "Le ruban est incomplet. Un constructeur devrait te poser une "
                            "question, donc il retourne à l'expéditeur.\n\n"
                            + "".join(f"- {m}\n" for m in r["manques"])
                            + "\nCorrige et redépose dans `_INBOX/" + portier + "/`.\n")
                shutil.move(src, os.path.join(rej, nom))
                continue

            titre = r["title"]
            if a.dry:
                bilan["admis"].append({"note": f"{portier}/{nom}", "layer": layer,
                                       "title": titre, "dry": True})
                continue
            ruban = os.path.join(TAPES, f"{date.today()}-{slug(titre)}.md")
            i = 2
            while os.path.exists(ruban):
                ruban = os.path.join(TAPES, f"{date.today()}-{slug(titre)}-{i}.md"); i += 1
            shutil.copy2(src, ruban)
            res = uc("submit", "--layer", layer, "--title", titre, "--tape", ruban)
            adm = os.path.join(INBOX, "_admis", portier)
            os.makedirs(adm, exist_ok=True)
            shutil.move(src, os.path.join(adm, nom))
            bilan["admis"].append({"note": f"{portier}/{nom}", "layer": layer,
                                   "work_id": res.get("work_id"),
                                   "ruban": os.path.relpath(ruban, V3).replace("\\", "/")})
    print(json.dumps(bilan, ensure_ascii=False, indent=1))


P = argparse.ArgumentParser(description="portier d'admission A'Space V3")
S = P.add_subparsers(dest="cmd", required=True)
S.add_parser("template").set_defaults(f=cmd_template)
p = S.add_parser("check"); p.add_argument("fichier"); p.set_defaults(f=cmd_check)
p = S.add_parser("run"); p.add_argument("--dry", action="store_true"); p.set_defaults(f=cmd_run)

if __name__ == "__main__":
    a = P.parse_args(); a.f(a)
