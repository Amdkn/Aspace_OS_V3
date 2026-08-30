#!/usr/bin/env python3
"""Banc d'essai : un modele OpenRouter tient-il l'usage d'outils de Claude Code ?

Tache jetable, aucune ecriture, aucune modification de settings.json.
Frappe l'endpoint **Anthropic Skin** — exactement le chemin que CC utilisera,
donc un succes ici vaut preuve pour CC. Un test via /chat/completions ne
prouverait rien.

    python banc_outils.py                          # xiaomi/mimo-v2.5
    python banc_outils.py deepseek/deepseek-v4-flash
    python banc_outils.py xiaomi/mimo-v2.5 deepseek/deepseek-v4-flash

La cle est lue dans OPENROUTER_API_KEY si presente, sinon demandee en saisie
masquee. Elle n'est jamais affichee ni ecrite.

Trois epreuves, dans l'ordre ou elles cassent :
  1. Emission — le modele produit-il un tool_use valide plutot que du texte ?
  2. Boucle   — accepte-t-il un tool_result et poursuit-il correctement ?
  3. Cache    — un second appel identique est-il facture en cache lu ?
"""

import json
import os
import sys
import getpass
import urllib.request
import urllib.error

URL = "https://openrouter.ai/api/v1/messages"

OUTIL = [{
    "name": "lire_fichier",
    "description": "Lit un fichier du disque et rend son contenu.",
    "input_schema": {
        "type": "object",
        "properties": {
            "chemin": {"type": "string", "description": "Chemin absolu du fichier"},
            "lignes": {"type": "integer", "description": "Nombre de lignes a lire"},
        },
        "required": ["chemin"],
    },
}]

# Prefixe volumineux et stable : c'est lui qui doit tomber en cache au 2e appel.
# ~10 000 tokens, l'ordre de grandeur du prefixe reel de Claude Code sur ce poste.
PREFIXE = ("Contexte de gouvernance A'Space. " * 40 + "\n") * 60


def appel(cle, modele, messages, outils=True, prefixe=False):
    corps = {
        "model": modele,
        "max_tokens": 512,
        "messages": messages,
    }
    if outils:
        corps["tools"] = OUTIL
    if prefixe:
        corps["system"] = PREFIXE
    req = urllib.request.Request(
        URL,
        data=json.dumps(corps).encode(),
        headers={
            "Authorization": f"Bearer {cle}",
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read()), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code} — {e.read().decode()[:300]}"
    except Exception as e:
        return None, f"{type(e).__name__} — {e}"


def bloc(rep, genre):
    return [b for b in (rep.get("content") or []) if b.get("type") == genre]


def tester(cle, modele):
    print(f"\n{'='*66}\n  {modele}\n{'='*66}")
    score = 0

    # --- 1 : emission d'un tool_use ---
    msgs = [{"role": "user", "content":
             "Lis les 20 premieres lignes de C:/Users/amado/CLAUDE.md. "
             "Utilise l'outil, ne reponds pas en texte."}]
    rep, err = appel(cle, modele, msgs)
    if err:
        print(f"  1. emission ....... ECHEC — {err}")
        return score
    uses = bloc(rep, "tool_use")
    if not uses:
        txt = (bloc(rep, "text") or [{}])[0].get("text", "")[:90]
        print(f"  1. emission ....... ECHEC — texte au lieu d'un outil : {txt!r}")
        return score
    arg = uses[0].get("input") or {}
    if "chemin" not in arg:
        print(f"  1. emission ....... ECHEC — champ requis absent : {arg}")
        return score
    print(f"  1. emission ....... OK — chemin={arg['chemin']!r}")
    score += 1

    # --- 2 : boucle tool_result ---
    msgs.append({"role": "assistant", "content": rep["content"]})
    msgs.append({"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": uses[0]["id"],
        "content": "# C:\\Users\\amado — racine du profil\n\nCe dossier est un profil utilisateur.",
    }]})
    rep2, err = appel(cle, modele, msgs)
    if err:
        print(f"  2. boucle ......... ECHEC — {err}")
        return score
    txt = " ".join(b.get("text", "") for b in bloc(rep2, "text"))
    if not txt.strip():
        print("  2. boucle ......... ECHEC — aucune reponse texte apres le tool_result")
        return score
    coherent = "profil" in txt.lower() or "racine" in txt.lower()
    print(f"  2. boucle ......... {'OK' if coherent else 'DOUTEUX'} — {txt.strip()[:80]!r}")
    score += 1 if coherent else 0

    # --- 3 : cache lu au second appel identique ---
    m3 = [{"role": "user", "content": "Reponds uniquement: PONG"}]
    a, err = appel(cle, modele, m3, outils=False, prefixe=True)
    if err:
        print(f"  3. cache .......... indeterminable — {err}")
        return score
    b, err = appel(cle, modele, m3, outils=False, prefixe=True)
    if err:
        print(f"  3. cache .......... indeterminable — {err}")
        return score
    u1, u2 = a.get("usage", {}), b.get("usage", {})
    lu = u2.get("cache_read_input_tokens") or 0
    if lu:
        print(f"  3. cache .......... OK — {lu:,} tokens relus en cache au 2e appel")
        score += 1
    else:
        print(f"  3. cache .......... pas de cache observe (appel 1 : {u1}, appel 2 : {u2})")
    return score


if __name__ == "__main__":
    modeles = sys.argv[1:] or ["xiaomi/mimo-v2.5"]
    cle = os.environ.get("OPENROUTER_API_KEY") or getpass.getpass(
        "Cle OpenRouter (sk-or-v1-..., saisie masquee) : ").strip()
    if not cle.startswith("sk-or-v1-"):
        print("ERREUR : une cle OpenRouter commence par 'sk-or-v1-'.")
        sys.exit(1)

    resultats = {m: tester(cle, m) for m in modeles}
    print(f"\n{'='*66}\n  VERDICT  (3 = utilisable par Claude Code)\n{'='*66}")
    for m, s in resultats.items():
        etat = "utilisable" if s == 3 else ("partiel" if s >= 2 else "INAPTE")
        print(f"  {s}/3  {etat:12} {m}")
    print("\nUn modele qui echoue l'epreuve 1 ou 2 ne peut pas piloter Claude Code,")
    print("quel que soit son prix.")
