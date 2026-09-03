#!/usr/bin/env python3
"""wheel_consumer.py — consommateur du bus Wheel Discovery -> mandats L2.

Boucle metabolique : lit `20_Life_OS/22_Wheel_Discovery/state.json` (bus produit
par work 35). Si au moins un LD est GREEN avec load_signal=low et que Beth n'est
pas en HALT (beth_action != halt* sur tous les LD, aucun HALT_* dans le log),
genere un INTENT de production de valeur L2 dans `_INBOX/B1_Jerry_Summers/`
(-> gate.py -> Clara spec -> Nardole build -> Doctor12 review).

Anti-doublon : un intent n'est genere que si aucun work `pending` ne porte deja
son titre (uc.db) et si le fichier intent n'existe pas deja.

    python 10_Tech_OS/kernel/wheel_consumer.py run [--dry]
"""
from __future__ import annotations
import argparse, json, os, sqlite3, sys
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.abspath(os.path.join(HERE, "..", ".."))
DB = os.path.join(HERE, "uc.db")
STATE = os.path.join(V3, "20_Life_OS", "22_Wheel_Discovery", "state.json")
INBOX = os.path.join(V3, "_INBOX", "B1_Jerry_Summers")
LOG = os.path.join(V3, "20_Life_OS", "22_Wheel_Discovery", "consumer_log.jsonl")

# Rotation des mandats L2 (morty_route -> livrable cible dans 30_Business_OS)
ROTATION = [
    ("ENTERPRISE_PARA", "Summers Verse v+1: prochaine franchise coach-os-app "
     "(registre + verifier) dans 00_Summers_Verse"),
    ("PROTOSTAR_DEAL", "Summers Verse: ingestion Solaris (registre des sources "
     "+ verifier) dans 00_Summers_Verse"),
    ("SNW_12WY", "Summers Verse: horizon 12WY pour le prochain projet "
     "(registre + verifier) dans 00_Summers_Verse"),
    ("CERRITOS_GTD", "Summers Verse: boucle GTD Cerritos appliquee au projet "
     "actif (registre + verifier) dans 00_Summers_Verse"),
    ("ORVILLE_IKIGAI", "Summers Verse: matrice Ikigai Orville du prochain "
     "projet (registre + verifier) dans 00_Summers_Verse"),
]

INTENT_TEMPLATE = """---
title: "{titre}"
layer: L2
originator: wheel_consumer (cron metabolique)
source: 20_Life_OS/22_Wheel_Discovery/state.json
statut: FROZEN
date: {date}
---

## Irritant

Le bus Wheel Discovery (work 35) signale `{ld}` GREEN, load low, route
`{route}` — Beth verte (beth_action: none). Ce signal n'avait aucun
consommateur : aucune traduction en work L2 de production de valeur.

## Résultat visé

{titre}

## Contraintes

- Passer par le portier `_INBOX/B1_Jerry_Summers/` -> `gate.py run` (L2).
- Pyramide L0 >= L1 > L2 : Beth a le veto, respecter `30_Business_OS/AGENTS.md`.
- Ne pas toucher `10_Tech_OS/kernel/` ni `20_Life_OS/`.

## Definition of Done

- [ ] `30_Business_OS/00_Summers_Verse/` contient le livrable cite dans
      l'objectif, avec un registre JSON lisible par `python -m json.tool` (rc=0).
- [ ] Un verifier executé (`python <verifier>.py`) retourne rc=0 et imprime
      au moins 1 critere OK.
- [ ] Le work uc.db correspondant porte une prediction pre-enregistree AVANT
      la premiere evidence (loi de prediction, schema.sql).
"""


def beth_verte(state: dict) -> tuple[bool, str]:
    """Beth a le veto (20_Life_OS/AGENTS.md regle 1). Vert = aucun HALT."""
    for ld, d in state.get("domains", {}).items():
        act = (d.get("beth_action") or "").lower()
        if "halt" in act:
            return False, f"{ld} beth_action={act}"
        if d.get("zora_state", "").upper() == "HALT":
            return False, f"{ld} zora_state=HALT"
    return True, "aucun HALT declare"


def work_existe(titre: str) -> bool:
    c = sqlite3.connect(DB, timeout=10)
    r = c.execute("SELECT 1 FROM work WHERE title=? AND status IN "
                  "('pending','claimed','review') LIMIT 1", (titre,)).fetchone()
    c.close()
    return r is not None


def prochain_mandat() -> tuple[str, str]:
    """Round-robin base sur le nombre d'intents deja emis (log jsonl)."""
    n = 0
    if os.path.exists(LOG):
        with open(LOG, encoding="utf-8") as f:
            n = sum(1 for _ in f)
    return ROTATION[n % len(ROTATION)]


def cmd_run(a) -> None:
    state = json.load(open(STATE, encoding="utf-8"))
    ok, motif = beth_verte(state)
    if not ok:
        print(json.dumps({"action": "skip", "raison": f"Beth HALT: {motif}"},
                         ensure_ascii=False))
        return
    verts = [ld for ld, d in state["domains"].items()
             if d.get("zora_state") == "GREEN" and d.get("load_signal") == "low"]
    if not verts:
        print(json.dumps({"action": "skip", "raison": "aucun LD GREEN low"},
                         ensure_ascii=False))
        return

    route, titre = prochain_mandat()
    if work_existe(titre):
        print(json.dumps({"action": "skip", "raison": "work actif existe deja",
                          "titre": titre}, ensure_ascii=False))
        return

    ld = verts[0]
    os.makedirs(INBOX, exist_ok=True)
    dest = os.path.join(INBOX, f"intent-wheel-{date.today().isoformat()}-{route.lower()}.md")
    if os.path.exists(dest):
        print(json.dumps({"action": "skip", "raison": "intent deja depose",
                          "intent": dest}, ensure_ascii=False))
        return
    if a.dry:
        print(json.dumps({"action": "dry", "intent": dest, "titre": titre},
                         ensure_ascii=False))
        return
    with open(dest, "w", encoding="utf-8") as f:
        f.write(INTENT_TEMPLATE.format(titre=titre, route=route, ld=ld,
                                       date=date.today().isoformat()))
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps({"at": datetime.now().isoformat(timespec="seconds"),
                            "intent": os.path.relpath(dest, V3),
                            "titre": titre, "ld": ld, "route": route}) + "\n")
    print(json.dumps({"action": "emis", "intent": dest, "titre": titre,
                      "ld": ld, "route": route}, ensure_ascii=False))


P = argparse.ArgumentParser(description="consommateur du bus Wheel -> L2")
S = P.add_subparsers(dest="cmd", required=True)
p = S.add_parser("run"); p.add_argument("--dry", action="store_true")
p.set_defaults(f=cmd_run, d=None)

if __name__ == "__main__":
    a = P.parse_args(); a.f(a)
