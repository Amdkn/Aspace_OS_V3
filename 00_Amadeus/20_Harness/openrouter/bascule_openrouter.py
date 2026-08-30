#!/usr/bin/env python3
"""Bascule Claude Code de MiniMax vers OpenRouter (Anthropic Skin).

A LANCER CLAUDE CODE FERME. CC reecrit settings.json en fin de session :
une edition a chaud est perdue sans avertissement.

    python bascule_openrouter.py            # applique
    python bascule_openrouter.py --revert   # revient au dernier backup

La cle OpenRouter est demandee en saisie masquee. Elle n'est jamais passee
en argument, jamais ecrite dans un log, jamais affichee.
"""

import json
import getpass
import shutil
import sys
import os
from datetime import datetime

SETTINGS = os.path.expanduser(r"~/.claude/settings.json")
BACKUP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backups")

# Profil CACHE — arrete le 2026-08-21 apres mesure au banc.
#
# `banc_outils.py` a rendu 3/3 pour xiaomi/mimo-v2.5 ET deepseek/deepseek-v4-flash
# sur l'Anthropic Skin : emission de tool_use valide, boucle tool_result
# coherente, cache lu observe au second appel. MiMo est donc promu principal —
# son cache lu x50 le rend le moins cher des ~95 % de reutilisation, ce qui est
# le regime normal d'une session Claude Code.
#
#   slot principal : xiaomi/mimo-v2.5
#     in $0.140  cache lu $0.0028 (x50)  out $0.28  contexte 1 050 000
#   slot small/fast : inclusionai/ling-3.0-flash
#     in $0.021  cache lu $0.0042 (x5)   out $0.06  contexte   262 144
#
# Repli eprouve, si MiMo deraille en usage reel : deepseek/deepseek-v4-flash
#     in $0.081  cache lu $0.0162 (x5)   out $0.16  contexte 1 048 576
# Il a passe le meme banc 3/3 et a tourne en session. Remplacer les trois
# premieres lignes ci-dessous, relancer le script, relancer CC.
#
# Ecarte : openai/gpt-oss-120b — son cache lu coute le prix de l'entree
# ($0.030 = $0.030), benefice nul. Le prix d'entree seul est un mauvais critere.
MODELES = {
    # Durable — raisonnement lourd, arbitrage.
    #   in $0.966  cache $0.1932 (x5)  out $3.04  ctx 1 048 576
    "ANTHROPIC_DEFAULT_OPUS_MODEL":   "z-ai/glm-5.2",
    # Persistant — le cheval de trait, contexte le plus large du profil.
    #   in $0.065  cache $0.0200 (x3)  out $0.18  ctx 1 310 720
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "~deepseek/deepseek-v4-flash-latest",
    # Idempotence — gratuit. Voir l'avertissement de debit ci-dessous.
    #   in $0  cache $0  out $0  ctx 200 000
    "ANTHROPIC_DEFAULT_HAIKU_MODEL":  "openrouter/free",
    # Trafic de fond (resumes, WebFetch, titres). VOLONTAIREMENT PAS `openrouter/free`.
    # Le palier gratuit plafonne a 20 req/min ; le trafic de fond de CC est
    # frequent et automatique, donc le premier a declencher un 429 — exactement
    # ce qui a abattu la vague de revue du 2026-08-21 au matin.
    # Pour l'aligner quand meme sur Haiku : remplacer par "openrouter/free".
    "ANTHROPIC_SMALL_FAST_MODEL":     "inclusionai/ling-3.0-flash",
}

# Antifragile — Kimi. `ANTHROPIC_DEFAULT_FABLE_MODEL` N'EXISTE PAS : le binaire
# CC v2.1.143 ne connait que les slots OPUS, SONNET, HAIKU (verifie par lecture
# du binaire, 218 Mo, le 2026-08-21). Le mecanisme reel pour ajouter une entree
# nommee au selecteur /model est ce quatuor, qui alimente
# `additionalModelOptionsCache` dans le binaire.
#   in $0.580  cache $0.0976 (x6)  out $2.44  ctx 262 144
OPTION_SUP = {
    "ANTHROPIC_CUSTOM_MODEL_OPTION":             "moonshotai/kimi-k2.6",
    "ANTHROPIC_CUSTOM_MODEL_OPTION_NAME":        "Antifragile",
    "ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION": "Kimi K2.6 - 262k ctx, cache x6",
}

# `ANTHROPIC_MODEL` epingle un modele unique et court-circuite les trois slots :
# /model n'aurait plus aucun effet. Il est donc RETIRE, pas remplace.
A_RETIRER = ["ANTHROPIC_MODEL"]


def charger():
    with open(SETTINGS, encoding="utf-8") as f:
        return json.load(f)


def ecrire(cfg):
    with open(SETTINGS, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")


def sauvegarder():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    horo = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    dst = os.path.join(BACKUP_DIR, f"settings.{horo}.json")
    shutil.copy2(SETTINGS, dst)
    return dst


def lister_backups():
    if not os.path.isdir(BACKUP_DIR):
        return []
    return sorted(f for f in os.listdir(BACKUP_DIR) if f.startswith("settings."))


def revert(choix=None):
    """Restaure un backup.

    Le plus recent n'est PAS forcement celui qu'on veut : apres plusieurs
    bascules, c'est deja une config OpenRouter. On affiche donc le fournisseur
    de chaque backup et on demande lequel restaurer.
    """
    fichiers = lister_backups()
    if not fichiers:
        print("Aucun backup. Rien a restaurer.")
        return 1

    print("Backups disponibles :\n")
    for n, f in enumerate(fichiers, 1):
        try:
            env = json.load(open(os.path.join(BACKUP_DIR, f), encoding="utf-8")).get("env", {})
            url = env.get("ANTHROPIC_BASE_URL", "?")
            mod = env.get("ANTHROPIC_MODEL", "?")
        except Exception:
            url = mod = "(illisible)"
        print(f"  [{n}] {f}\n      {url}\n      {mod}\n")

    if choix is None:
        rep = input(f"Numero a restaurer (1-{len(fichiers)}, vide = annuler) : ").strip()
        if not rep:
            print("Annule. Rien n'a ete modifie.")
            return 0
        choix = rep
    try:
        idx = int(choix)
        assert 1 <= idx <= len(fichiers)
    except (ValueError, AssertionError):
        print("Numero invalide. Rien n'a ete modifie.")
        return 1

    src = os.path.join(BACKUP_DIR, fichiers[idx - 1])
    shutil.copy2(src, SETTINGS)
    print(f"\nRestaure depuis {src}")
    print("Relancer Claude Code pour que la config reprenne.")
    return 0


def vers_anthropic():
    """Retire toute configuration ANTHROPIC_* pour retomber sur le plan Pro.

    POURQUOI CE MODE EXISTE
    -----------------------
    Les sous-agents de Claude Code heritent de la configuration de la session.
    Demander `model: sonnet` ne resout PAS vers Sonnet 5 d'Anthropic : il passe
    par `ANTHROPIC_DEFAULT_SONNET_MODEL`, donc vers le modele OpenRouter du
    slot. Mesure du 2026-08-21 : des agents lances sur `sonnet` sont morts sur
    « There's an issue with the selected model (~deepseek/...) ».

    Desactiver les variables d'environnement ne suffit pas non plus : le
    fichier est lu apres, et gagne. Verifie le meme jour par compteur d'usage
    OpenRouter — un `claude -p --model sonnet` avec toutes les ANTHROPIC_*
    unset a quand meme fait monter la facture OpenRouter.

    Le seul etat qui donne du vrai Sonnet 5 est l'absence totale de ces cles.
    """
    cfg = charger()
    env = cfg.setdefault("env", {})
    bak = sauvegarder()
    print(f"Backup : {bak}")

    retires = [c for c in list(env) if c.startswith("ANTHROPIC_")]
    for c in retires:
        env.pop(c)

    ecrire(cfg)
    print(f"\n{len(retires)} cle(s) ANTHROPIC_* retiree(s) de settings.json :")
    for c in retires:
        print(f"  - {c}")
    print("\nL'authentification retombe sur les credentials OAuth du plan Pro.")
    print("\nEtapes suivantes :")
    print("  1. Fermer et relancer Claude Code.")
    print("  2. La banniere doit montrer un modele Anthropic, pas un slug OpenRouter.")
    print("  3. Les sous-agents `model: sonnet` atteindront alors Sonnet 5.")
    print("\nATTENTION QUOTA : ce mode consomme le forfait Pro, pas OpenRouter.")
    print(f"\nPour revenir a OpenRouter : python {os.path.basename(__file__)}")
    return 0


def appliquer():
    cfg = charger()
    env = cfg.setdefault("env", {})

    bak = sauvegarder()
    print(f"Backup : {bak}")

    cle = getpass.getpass("Cle OpenRouter (sk-or-v1-..., saisie masquee) : ").strip()
    if not cle.startswith("sk-or-v1-"):
        print("ERREUR : une cle OpenRouter commence par 'sk-or-v1-'. Rien n'a ete modifie.")
        return 1

    # --- endpoint ---
    # L'URL est SANS /v1 : Claude Code ajoute /v1/messages lui-meme.
    # Mettre https://openrouter.ai/api/v1 produit un 404 sur /api/v1/v1/messages.
    env["ANTHROPIC_BASE_URL"] = "https://openrouter.ai/api"

    # OpenRouter authentifie par bearer -> ANTHROPIC_AUTH_TOKEN.
    # ANTHROPIC_API_KEY part en header x-api-key et serait traite comme une
    # credential Anthropic directe : il DOIT etre vide, pas absent.
    env["ANTHROPIC_AUTH_TOKEN"] = cle
    env["ANTHROPIC_API_KEY"] = ""

    # --- modeles ---
    for slot, ident in MODELES.items():
        env[slot] = ident
    for slot, val in OPTION_SUP.items():
        env[slot] = val
    for slot in A_RETIRER:
        env.pop(slot, None)

    # Le picker de modeles derriere une gateway est opt-in.
    env["CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY"] = "1"

    # deepseek-v4-flash porte 1 048 576 tokens : la fenetre de compaction tient.
    env["CLAUDE_CODE_AUTO_COMPACT_WINDOW"] = "1000000"

    ecrire(cfg)

    print("\nApplique. Recapitulatif (cle masquee) :")
    print(f"  ANTHROPIC_BASE_URL   = {env['ANTHROPIC_BASE_URL']}")
    print(f"  ANTHROPIC_AUTH_TOKEN = {cle[:12]}...(masque)")
    print(f"  ANTHROPIC_API_KEY    = (vide, volontairement)")
    for slot, ident in MODELES.items():
        print(f"  {slot:34} = {ident}")
    for slot, val in OPTION_SUP.items():
        print(f"  {slot:34} = {val}")
    for slot in A_RETIRER:
        print(f"  {slot:34} = (retire : il epinglerait un modele unique)")
    print("\nEtapes suivantes :")
    print("  1. Relancer Claude Code.")
    print("  2. Si un compte Anthropic a deja ete utilise ici : /logout puis relancer,")
    print("     sinon le login en cache ecrase ces variables (erreurs 'model not found').")
    print("  3. /status doit montrer la base URL OpenRouter et la source du token.")
    print(f"\nPour revenir en arriere : python {os.path.basename(__file__)} --revert")
    return 0


if __name__ == "__main__":
    if not os.path.exists(SETTINGS):
        print(f"Introuvable : {SETTINGS}")
        sys.exit(1)
    if "--anthropic" in sys.argv:
        sys.exit(vers_anthropic())
    if "--revert" in sys.argv:
        rest = [a for a in sys.argv[1:] if a != "--revert"]
        sys.exit(revert(rest[0] if rest else None))
    sys.exit(appliquer())
