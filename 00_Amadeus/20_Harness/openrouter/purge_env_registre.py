#!/usr/bin/env python3
"""Retire les ANTHROPIC_* permanents de HKCU:\\Environment.

POURQUOI CE SCRIPT EXISTE
-------------------------
Les variables d'environnement utilisateur du registre ont **precedence sur
`settings.json`**. Tant qu'elles pointent MiniMax, la bascule OpenRouter est
ecrite correctement dans le fichier et sans aucun effet : la banniere de CC
affiche `MiniMax-M3`, et `ANTHROPIC_AUTH_TOKEN = sk-cp-...` ecrase meme la
cle OpenRouter.

CE QUE CA CASSE — a lire avant de lancer
----------------------------------------
Ces variables avaient ete posees dans le registre **exprès** : c'est ce qui
faisait fonctionner la delegation MiniMax depuis PowerShell sans reexporter
a chaque shell (canon §1, « Terminal PowerShell »). Les retirer arrete ce
chemin-la. Si l'on veut le garder, l'enrober dans un `lance.sh` / `lance.ps1`
qui exporte les variables pour ce seul processus, au lieu de les rendre
globales.

    python purge_env_registre.py              # montre, ne touche a rien
    python purge_env_registre.py --appliquer  # sauvegarde puis retire
    python purge_env_registre.py --restaurer  # remet depuis la sauvegarde

La sauvegarde est un .json a cote de ce script. Les valeurs y sont ecrites en
clair — c'est le seul moyen de pouvoir restaurer — donc le dossier `backups/`
ne doit jamais partir dans un depot.
"""

import ctypes
import json
import os
import sys
import winreg

CIBLES = [
    "ANTHROPIC_BASE_URL",
    "ANTHROPIC_API_KEY",
    "ANTHROPIC_AUTH_TOKEN",
    "ANTHROPIC_MODEL",
    "ANTHROPIC_SMALL_FAST_MODEL",
]

ICI = os.path.dirname(os.path.abspath(__file__))
SAUVE = os.path.join(ICI, "backups", "env_registre.json")


def lire():
    trouve = {}
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
        for nom in CIBLES:
            try:
                val, typ = winreg.QueryValueEx(k, nom)
                trouve[nom] = {"valeur": val, "type": typ}
            except FileNotFoundError:
                pass
    return trouve


def masque(v):
    return v[:14] + "...(masque)" if len(v) > 18 else v


def diffuser():
    """Previent les applications que l'environnement a change.

    Sans ca, seuls les processus lances apres une reouverture de session
    verraient la modification.
    """
    HWND_BROADCAST, WM_SETTINGCHANGE, SMTO_ABORTIFHUNG = 0xFFFF, 0x1A, 0x0002
    res = ctypes.c_ulong()
    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_SETTINGCHANGE, 0,
        ctypes.c_wchar_p("Environment"), SMTO_ABORTIFHUNG, 5000,
        ctypes.byref(res))


def montrer():
    t = lire()
    if not t:
        print("Aucune ANTHROPIC_* dans HKCU:\\Environment. Rien a faire.")
        return 0
    print(f"{len(t)} variable(s) permanente(s) trouvee(s) — elles ECRASENT settings.json :\n")
    for nom, d in t.items():
        print(f"  {nom:28} = {masque(str(d['valeur']))}")
    print("\nAucune modification. Pour appliquer : --appliquer")
    return 0


def appliquer():
    t = lire()
    if not t:
        print("Aucune ANTHROPIC_* a retirer.")
        return 0
    os.makedirs(os.path.dirname(SAUVE), exist_ok=True)
    with open(SAUVE, "w", encoding="utf-8") as f:
        json.dump(t, f, indent=2, ensure_ascii=False)
    print(f"Sauvegarde : {SAUVE}  ({len(t)} variables, valeurs en clair)")

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0,
                        winreg.KEY_SET_VALUE) as k:
        for nom in t:
            winreg.DeleteValue(k, nom)
            print(f"  retire : {nom}")
    diffuser()

    restant = lire()
    print(f"\nVerification : {len(restant)} ANTHROPIC_* restante(s) — "
          f"{'OK' if not restant else 'ECHEC, voir ci-dessus'}")
    print("\nOuvrir un NOUVEAU terminal, puis relancer Claude Code.")
    print("Le terminal courant garde l'ancien environnement : il ne prouve rien.")
    return 0 if not restant else 1


def restaurer():
    if not os.path.exists(SAUVE):
        print(f"Pas de sauvegarde : {SAUVE}")
        return 1
    t = json.load(open(SAUVE, encoding="utf-8"))
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0,
                        winreg.KEY_SET_VALUE) as k:
        for nom, d in t.items():
            winreg.SetValueEx(k, nom, 0, d["type"], d["valeur"])
            print(f"  remis : {nom}")
    diffuser()
    print("\nOuvrir un nouveau terminal pour que ca prenne.")
    return 0


if __name__ == "__main__":
    if "--appliquer" in sys.argv:
        sys.exit(appliquer())
    if "--restaurer" in sys.argv:
        sys.exit(restaurer())
    sys.exit(montrer())
