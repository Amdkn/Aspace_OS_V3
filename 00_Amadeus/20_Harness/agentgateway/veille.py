#!/usr/bin/env python
"""
veille.py — la sonde externe qui annonce la mort du gateway.

POURQUOI CE FICHIER EXISTE

Le 2026-08-13, le gateway est reste mort toute une session sans que rien ne le
dise. Decouvert par accident, en cherchant a joindre Supabase. Entre le
redemarrage et la decouverte, **toutes les capacites MCP etaient absentes en
silence**.

`WATCHDOG.md` §1 pose la regle qui gouverne ce fichier :

> A0 orchestre Life OS ; il ne se surveille pas lui-meme. Un orchestrateur qui
> juge sa propre sante est exactement le defaut que la boucle gauntlet existe
> pour corriger, transpose a l'infrastructure.

Meme chose ici : le gateway ne peut pas etre son propre veilleur. Cette sonde
tourne **a cote**, pas dedans.

TROIS PALIERS, DU MOINS CHER AU PLUS CHER

  1. le port 3300 ecoute-t-il ?          (socket, instantane)
  2. le serveur HTTP repond-il ?         (racine, ~1 s)
  3. les identifiants sont-ils acceptes ? (sonde_identifiants.py, ~20 s)

Le palier 3 ne tourne qu'a la demande (`--complet`) : il fait 23 appels reseau,
il n'a rien a faire dans une veille a la minute.

CE QU'ELLE FAIT QUAND CA TOMBE

Elle **ecrit dans le journal** — c'est le minimum, et c'est ce qui manquait.
Avec `--relancer`, elle relance le `.vbs` de demarrage. Sans l'option, elle
constate et se tait : un veilleur qui redemarre en boucle un service casse
fabrique des processus fantomes, et ce poste en a deja paye.

USAGE

    python veille.py                 # 2 paliers, une ligne au journal
    python veille.py --complet       # + sonde des identifiants
    python veille.py --relancer      # + relance si mort
"""

from __future__ import annotations
import json, socket, subprocess, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent
JOURNAL = RACINE / "veille.log"
ETAT = RACINE / "veille_etat.json"
VBS = Path("C:/Users/amado/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/agentgateway.vbs")
HOTE, PORT = "127.0.0.1", 3300

def dire(msg: str) -> None:
    ligne = f"[{datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(ligne)
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(ligne + "\n")

def palier_port() -> bool:
    with socket.socket() as s:
        s.settimeout(2)
        return s.connect_ex((HOTE, PORT)) == 0

def palier_http() -> tuple[bool, str]:
    """
    Le serveur HTTP repond-il ? On interroge la RACINE, pas `/mcp`.

    POURQUOI PAS `/mcp`

    Une premiere version postait un `initialize` JSON-RPC sur `/mcp`. Elle rendait
    `TimeoutError` de facon reproductible — y compris avec un gateway dont la
    racine repondait 406 et l'admin 308, donc parfaitement vivant. Verifie a
    curl : meme silence, 25 s, HTTP 000.

    Je n'ai pas pu etablir si `/mcp` etait reellement casse ou si ma requete
    etait mal formee pour ce transport (le streamable HTTP de MCP attend
    peut-etre une session prealable). **Dans le doute, une sonde ne rend pas de
    verdict.** Le 2026-08-13 a produit dix faux rouges ; le onzieme aurait ete
    celui-ci, ecrit chaque minute dans un journal que quelqu'un finit par croire.

    Ce qu'on teste ici est donc plus modeste et parfaitement fiable : **le port
    ecoute et le serveur parle HTTP**. Le seul juge competent de la sante MCP est
    un vrai client MCP — si Claude Code voit ses outils, ca marche.

    Un 406 est un SUCCES : le serveur a compris la requete et refuse le type de
    contenu. Un serveur mort ne rend pas 406, il ne rend rien.
    """
    req = urllib.request.Request(f"http://{HOTE}:{PORT}/",
                                 headers={"User-Agent": "aspace-veille/1"})
    try:
        with urllib.request.urlopen(req, timeout=6) as r:
            return True, f"HTTP {r.status}"
    except urllib.error.HTTPError as e:
        return True, f"HTTP {e.code} (le serveur repond)"
    except Exception as e:
        return False, type(e).__name__

def relancer() -> str:
    if not VBS.exists():
        return f"ECHEC — {VBS.name} introuvable"
    try:
        subprocess.Popen(["wscript.exe", str(VBS)], close_fds=True)
        time.sleep(12)
        return "relance — port " + ("OUVERT" if palier_port() else "TOUJOURS FERME")
    except Exception as e:
        return f"ECHEC relance — {type(e).__name__}"

def main() -> int:
    vivant = palier_port()
    detail = "port ferme"
    if vivant:
        ok, detail = palier_http()
        vivant = ok

    etat = {"quand": datetime.now(timezone.utc).isoformat(), "vivant": vivant, "detail": detail}

    if vivant:
        # Une ligne par passage rendrait le journal illisible. On n'ecrit que les
        # transitions : c'est le changement qui informe, pas la repetition.
        precedent = None
        if ETAT.exists():
            try: precedent = json.loads(ETAT.read_text(encoding="utf-8")).get("vivant")
            except Exception: pass
        if precedent is False:
            dire(f"gateway REVENU ({detail})")
    else:
        dire(f"gateway MORT — {detail}")
        if "--relancer" in sys.argv:
            dire("  " + relancer())

    ETAT.write_text(json.dumps(etat, ensure_ascii=False), encoding="utf-8")

    if "--complet" in sys.argv:
        r = subprocess.run([sys.executable, str(RACINE / "sonde_identifiants.py"), "--json"],
                           capture_output=True, text=True, timeout=300)
        try:
            morts = [l["serveur"] for l in json.loads(r.stdout) if l["etat"] == "MORT"]
            dire(f"identifiants refuses : {', '.join(morts) if morts else 'aucun'}")
        except Exception:
            dire("sonde_identifiants : sortie illisible")

    print(f"\n  gateway : {'VIVANT' if vivant else 'MORT'} · {detail}")
    return 0 if vivant else 1

if __name__ == "__main__":
    raise SystemExit(main())
