#!/usr/bin/env python
"""
sonde_identifiants.py — le garde-fou qui manquait a build_config.py.

POURQUOI CE FICHIER EXISTE

`build_config.py` ecarte les cibles injoignables. Sa verification, ligne 69 :

    if not (shutil.which(cmd) or os.path.isfile(cmd)):

Elle teste que **le binaire existe sur le disque**. Rien d'autre.

Un serveur dont le jeton est revoque passe ce test au vert et meurt au premier
appel. Mesure du 2026-08-13 : les trois serveurs Supabase repondent **403** sur
`api.supabase.com/v1/projects`. `build_config.py` les declare joignables. Ils
sont morts depuis des semaines, et rien ne l'avait dit.

C'est la meme famille de defaut que les sept faux verdicts de la campagne du
12-13 aout : **un feu vert qui mesure un proxy.** Le binaire existe n'implique
pas le serveur repond, exactement comme le journal est vide n'implique pas
l'agent est mort.

Cette sonde teste ce que build_config.py ne peut pas voir : l'identifiant
lui-meme, par un appel reel a l'API du fournisseur.

CE QU'ELLE NE FAIT PAS

Elle n'ecrit rien, ne corrige rien, ne relance rien. Elle mesure et elle dit.
Un jeton mort reste declare : c'est a l'humain de le faire tourner. Un outil
qui reecrit `mcp_sources.json` tout seul serait un outil qui cache ses propres
degats.

Aucune valeur de jeton n'est affichee ni journalisee — seulement sa longueur.

USAGE

    python sonde_identifiants.py            # tableau
    python sonde_identifiants.py --json     # sortie machine, pour le watchdog
"""

from __future__ import annotations
import json, os, re, shutil, sys, urllib.error, urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent
SOURCES = RACINE / "mcp_sources.json"
DELAI = 20

# Une sonde par fournisseur : (variables acceptees, fabrique de requete).
# L'endpoint choisi est toujours le moins couteux qui prouve l'identite —
# « qui suis-je », jamais une liste large.
def _req(url: str, entetes: dict[str, str]) -> urllib.request.Request:
    return urllib.request.Request(url, headers={"User-Agent": "aspace-sonde/1", **entetes})

SONDES = {
    "supabase":  (["SUPABASE_ACCESS_TOKEN"],
                  lambda v: _req("https://api.supabase.com/v1/projects",
                                 {"Authorization": f"Bearer {v[0]}"})),
    "vercel":    (["VERCEL_TOKEN"],
                  lambda v: _req("https://api.vercel.com/v2/user",
                                 {"Authorization": f"Bearer {v[0]}"})),
    "github":    (["GITHUB_PERSONAL_ACCESS_TOKEN"],
                  lambda v: _req("https://api.github.com/user",
                                 {"Authorization": f"Bearer {v[0]}",
                                  "Accept": "application/vnd.github+json"})),
    "airtable":  (["AIRTABLE_API_KEY", "AIRTABLE_TOKEN", "AIRTABLE_PAT"],
                  lambda v: _req("https://api.airtable.com/v0/meta/whoami",
                                 {"Authorization": f"Bearer {v[0]}"})),
    "clickup":   (["CLICKUP_API_TOKEN", "CLICKUP_API_KEY"],
                  lambda v: _req("https://api.clickup.com/api/v2/user",
                                 {"Authorization": v[0]})),
    "notion":    (["OPENAPI_MCP_HEADERS"],
                  lambda v: _req("https://api.notion.com/v1/users/me",
                                 {**_entetes_notion(v[0]), "Notion-Version": "2022-06-28"})),
    "hostinger": (["HOSTINGER_API_TOKEN"],
                  lambda v: _req("https://developers.hostinger.com/api/dns/v1/zones",
                                 {"Authorization": f"Bearer {v[0]}"})),
    "coolify":   (["COOLIFY_URL", "COOLIFY_TOKEN"],
                  lambda v: _req(f"{v[0].rstrip('/')}/api/v1/version",
                                 {"Authorization": f"Bearer {v[1]}"})),
}

def _entetes_notion(brut: str) -> dict[str, str]:
    """OPENAPI_MCP_HEADERS porte un JSON d'en-tetes, pas un jeton nu."""
    try:
        return {k: v for k, v in json.loads(brut).items()}
    except Exception:
        return {"Authorization": f"Bearer {brut}"}

PLACEHOLDER = re.compile(r"^\$\{env:([A-Za-z_][A-Za-z0-9_]*)\}$")

def resoudre(env: dict[str, str]) -> tuple[dict[str, str], list[str]]:
    """
    Resout les `${env:VAR}` comme le fait `build_config.py:resolve_env()`.

    Sans ca, la sonde teste la CHAINE `${env:AIRTABLE_API_KEY}` comme si c'etait
    un jeton, recolte un 401, et declare mort un identifiant qui n'a jamais ete
    lu. Constate le 2026-08-13 sur `airtable` et `clickup` : quatre variables,
    quatre faux morts.

    C'est le piege 2 de CLAUDE.md §3bis, retrouve depuis l'autre bout : le
    gateway resout ces placeholders, un outil qui lit `mcp_sources.json` a cru
    doit les resoudre aussi — sinon il n'observe pas le meme systeme.
    """
    clair, manquantes = {}, []
    for k, v in env.items():
        m = PLACEHOLDER.match(str(v))
        if not m:
            clair[k] = v
            continue
        reel = os.environ.get(m.group(1))
        if reel:
            clair[k] = reel
        else:
            manquantes.append(m.group(1))
    return clair, manquantes

def famille(nom: str) -> str | None:
    for f in SONDES:
        if nom == f or nom.startswith(f + "-"):
            return f
    return None

def sonder(f: str, env: dict[str, str]) -> tuple[str, str]:
    """Rend (etat, detail). Etats : OK · MORT · SANS_JETON · INJOIGNABLE."""
    cles, fabrique = SONDES[f]
    vals = []
    for c in cles:
        if env.get(c):
            vals.append(env[c])
            if f != "coolify":
                break
    if f == "coolify":
        vals = [env.get(c, "") for c in cles]
        if not all(vals):
            return "SANS_JETON", "COOLIFY_URL ou COOLIFY_TOKEN manque"
    if not vals or not vals[0]:
        return "SANS_JETON", f"aucune de {cles} n'est renseignee"
    try:
        with urllib.request.urlopen(fabrique(vals), timeout=DELAI) as r:
            return "OK", f"HTTP {r.status}"
    except urllib.error.HTTPError as e:
        # 401/403 = l'identifiant est refuse. C'est le cas que build_config.py rate.
        etat = "MORT" if e.code in (401, 403) else "INJOIGNABLE"
        try:
            corps = " ".join(e.read()[:110].decode("utf8", "replace").split())
        except Exception:
            corps = ""
        return etat, f"HTTP {e.code} {corps}"
    except Exception as e:
        return "INJOIGNABLE", type(e).__name__

def main() -> int:
    srv = json.loads(SOURCES.read_text(encoding="utf-8"))
    srv = srv.get("mcpServers", srv)
    lignes = []
    for nom, spec in sorted(srv.items()):
        env, manquantes = resoudre(spec.get("env") or {})
        cmd = spec.get("command", "")
        binaire = "oui" if (cmd and (shutil.which(cmd) or os.path.isfile(cmd))) else "NON"
        f = famille(nom)
        if f is None:
            etat, detail = "NON_TESTABLE", "aucune sonde pour ce fournisseur"
        else:
            etat, detail = sonder(f, env)
            if manquantes and etat != "OK":
                etat, detail = "NON_RESOLU", f"${{env:{'/'.join(manquantes)}}} absente(s) de l'environnement"
        lignes.append({"serveur": nom, "binaire": binaire, "etat": etat, "detail": detail})

    if "--json" in sys.argv:
        print(json.dumps(lignes, ensure_ascii=False, indent=1))
    else:
        print(f"\n  {'serveur':<20} {'binaire':<8} {'identifiant':<14} detail")
        print("  " + "-" * 62)
        for l in lignes:
            print(f"  {l['serveur']:<20} {l['binaire']:<8} {l['etat']:<14} {l['detail']}")
        morts = [l["serveur"] for l in lignes if l["etat"] == "MORT"]
        vert_trompeur = [l["serveur"] for l in lignes if l["etat"] == "MORT" and l["binaire"] == "oui"]
        print(f"\n  {len(lignes)} serveurs · {len(morts)} identifiant(s) refuse(s)")
        if vert_trompeur:
            print(f"  {len(vert_trompeur)} passe(nt) le test de build_config.py et sont morts :")
            print("     " + ", ".join(vert_trompeur))
            print("  C'est exactement le faux vert que cette sonde existe pour nommer.")
    return 1 if any(l["etat"] == "MORT" for l in lignes) else 0

if __name__ == "__main__":
    raise SystemExit(main())
