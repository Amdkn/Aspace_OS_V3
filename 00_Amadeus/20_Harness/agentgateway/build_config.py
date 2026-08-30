"""Genere la config agentgateway a partir des MCP deja declares.

Lit les serveurs stdio de mcp_sources.json — la SOURCE DE VERITE — et emet
config.yaml avec une cible MCP par serveur.

Ne PAS le faire lire ~/.mcp.json : ce fichier ne contient plus que l'entree
`gateway` qui pointe vers ce service. Le lire ferait boucler le gateway sur
lui-meme.

Usage :  python build_config.py [--dry-run]
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HOME = Path.home()
SOURCE = Path(__file__).parent / "mcp_sources.json"
OUT = Path(__file__).parent / "config.yaml"
PORT = 3300

# Serveurs a NE PAS router : ils parlent deja HTTP, ou ils sont fournis par
# l'application elle-meme et ne vivent pas dans un fichier.
SKIP = {"posthog", "transcript-api", "gateway"}


def collect() -> dict[str, dict]:
    """Lit la source de verite.

    ATTENTION : ce n'est PAS ~/.mcp.json. Ce dernier ne contient plus que
    l'entree `gateway` qui pointe vers ce service — le lire reviendrait a
    demander au gateway de se router vers lui-meme. La liste des serveurs
    agreges vit dans mcp_sources.json, a cote de ce script.
    """
    if not SOURCE.is_file():
        raise SystemExit(
            f"source introuvable : {SOURCE}\n"
            "Elle porte la liste des MCP agreges. La restaurer depuis une "
            "sauvegarde ~/.mcp.json.bak_* avant de regenerer.")

    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    servers: dict[str, dict] = dict(data.get("mcpServers", {}) or {})

    keep = {}
    for name, spec in servers.items():
        if name in SKIP:
            continue
        # stdio uniquement : un serveur HTTP distant n'a pas besoin d'etre
        # relance par le gateway, il serait proxifie autrement.
        if not spec.get("command"):
            continue
        keep[name] = spec
    return keep


def reachable(spec: dict) -> str | None:
    """Rend le motif du rejet, ou None si la cible est lancable.

    Controle indispensable : agentgateway fait echouer l'`initialize` COMPLET
    si une seule cible meurt au demarrage. Un serveur casse ne degrade pas le
    service, il l'abat. Mieux vaut l'ecarter a la generation.
    """
    cmd = spec["command"]
    if not (shutil.which(cmd) or os.path.isfile(cmd)):
        return f"commande introuvable : {cmd}"
    for arg in spec.get("args") or []:
        text = str(arg)
        if text.endswith((".py", ".js", ".mjs", ".cjs")) and not os.path.isfile(text):
            return f"fichier manquant : {text}"
    return None


def identifiants_morts() -> dict[str, str]:
    """Les serveurs dont l'identifiant est refuse, d'apres `sonde_identifiants.py`.

    POURQUOI CE SECOND CONTROLE

    `reachable()` teste que le BINAIRE existe. C'est necessaire et insuffisant :
    un serveur dont le jeton est revoque demarre parfaitement, puis bloque sur sa
    poignee de main d'authentification. Comme l'`initialize` d'agentgateway est
    tout-ou-rien, **toute la passerelle pend** — pas d'erreur, pas de log, juste
    un `/mcp` qui n'a jamais repondu.

    Constate le 2026-08-13 : gateway relance, `/` rend 406, l'admin rend 308,
    et `POST /mcp` reste muet au-dela de 60 s. Les deux jetons Vercel etaient
    refuses (`HTTP 403 invalidToken`) alors que leurs binaires existaient.

    Un echec se voit. Une attente ressemble a un reseau lent. C'est pire.

    En cas de panne de la sonde, on rend un dict vide : ce controle ne doit
    JAMAIS empecher une generation. Un garde-fou qui bloque la chaine quand il
    tombe lui-meme est un garde-fou qui coute plus qu'il ne rapporte.
    """
    sonde = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sonde_identifiants.py")
    if not os.path.isfile(sonde):
        return {}
    try:
        r = subprocess.run([sys.executable, sonde, "--json"],
                           capture_output=True, text=True, timeout=300)
        return {l["serveur"]: l["detail"] for l in json.loads(r.stdout) if l.get("etat") == "MORT"}
    except Exception:
        return {}


PLACEHOLDER = re.compile(r"^\$\{env:([A-Za-z_][A-Za-z0-9_]*)\}$")


def resolve_env(env: dict) -> tuple[dict, list[str]]:
    """Aplatit les valeurs `${env:VAR}`.

    agentgateway lit `${env:...}` comme SA propre syntaxe de substitution et
    refuse de demarrer si la variable manque a SON environnement. Claude Code,
    lui, les resolvait au niveau de son propre process. On resout donc ici, et
    on ecarte ce qui n'existe pas plutot que de laisser un placeholder mort.
    """
    out, dropped = {}, []
    for key, value in env.items():
        match = PLACEHOLDER.match(str(value).strip())
        if match:
            actual = os.environ.get(match.group(1))
            if actual:
                out[key] = actual
            else:
                dropped.append(key)
            continue
        # Une valeur litterale contenant "${" serait aussi interpretee.
        out[key] = str(value).replace("${", "$${")
    return out, dropped


def to_targets(servers: dict[str, dict]) -> tuple[list[dict], dict[str, list[str]], dict[str, str]]:
    targets, all_dropped, rejected = [], {}, {}
    morts = identifiants_morts()
    for name, spec in sorted(servers.items()):
        why = reachable(spec) or (f"identifiant refuse — {morts[name]}" if name in morts else None)
        if why:
            rejected[name] = why
            continue
        stdio = {"cmd": spec["command"]}
        if spec.get("args"):
            stdio["args"] = list(spec["args"])
        if spec.get("env"):
            env, dropped = resolve_env(spec["env"])
            if env:
                stdio["env"] = env
            if dropped:
                all_dropped[name] = dropped
        targets.append({"name": name, "stdio": stdio})
    return targets, all_dropped, rejected


def emit(targets: list[dict]) -> str:
    """Ecrit le YAML a la main : pas de dependance externe, et on controle
    exactement la citation des valeurs (les secrets contiennent des ':')."""
    def q(v: str) -> str:
        return json.dumps(str(v))  # JSON est un sous-ensemble valide de YAML

    lines = [
        "# yaml-language-server: $schema=https://agentgateway.dev/schema/config",
        "#",
        "# GENERE PAR build_config.py — ne pas editer a la main.",
        "# Source : mcp_sources.json — editer LA, jamais ce fichier-ci.",
        f"# {len(targets)} serveurs MCP agreges derriere un seul endpoint.",
        "",
        "binds:",
        f"  - port: {PORT}",
        "    listeners:",
        "      - routes:",
        "          - backends:",
        "              - mcp:",
        "                  targets:",
    ]
    for t in targets:
        lines.append(f"                    - name: {q(t['name'])}")
        lines.append("                      stdio:")
        lines.append(f"                        cmd: {q(t['stdio']['cmd'])}")
        if t["stdio"].get("args"):
            lines.append("                        args:")
            for a in t["stdio"]["args"]:
                lines.append(f"                          - {q(a)}")
        if t["stdio"].get("env"):
            lines.append("                        env:")
            for k, v in t["stdio"]["env"].items():
                lines.append(f"                          {k}: {q(v)}")
    return "\n".join(lines) + "\n"


def main() -> int:
    servers = collect()
    targets, dropped, rejected = to_targets(servers)
    text = emit(targets)

    print(f"{len(targets)} cibles MCP :")
    for t in targets:
        n_env = len(t["stdio"].get("env", {}))
        print(f"  {t['name']:20} env={n_env}")

    if rejected:
        print("\ncibles ECARTEES (une seule cible morte abat tout l'initialize) :")
        for name, why in rejected.items():
            print(f"  {name:20} {why}")

    if dropped:
        print("\nvariables non resolues, ecartees :")
        for name, keys in dropped.items():
            print(f"  {name:20} {', '.join(keys)}")

    if "--dry-run" in sys.argv:
        print("\n(dry-run, rien ecrit)")
        return 0

    OUT.write_text(text, encoding="utf-8")
    print(f"\necrit : {OUT}  ({len(text)} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
