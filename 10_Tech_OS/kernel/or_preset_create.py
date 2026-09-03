#!/usr/bin/env python3
"""Cree les 8 presets OpenRouter LD01-LD08 (tache t_24db1c81, run 18).

Canon Wheel : C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/AGENTS.md
Endpoint    : POST https://openrouter.ai/api/v1/presets/{slug}/chat/completions
  - seul `model`, `temperature`, `system`, `tools`, `provider` sont persistes ;
  - `messages` est ignore.
Cle lue depuis le .env du profil, jamais imprimee.
Idempotent : re-POSTer cree une nouvelle version, slug identique.
"""
import json, os, sys, time, urllib.request, urllib.error

ENV_PATH = r"C:\Users\amado\AppData\Local\hermes\profiles\yaz_spec_l0\.env"
BASE = "https://openrouter.ai/api/v1/presets"

SPEED_MODEL = "z-ai/glm-4.6-flash:free"      # A SOURCER -> remplace par modele flash reel si refuse
REASONING_MODEL = "z-ai/glm-4.6:free"        # A SOURCER -> modele reasoning

# Les 8 contraintes LD (pyramide L0>=L1>L2, canon racine AGENTS.md + 22_Wheel_Discovery)
def contraintes(persona, domaine):
    return [
        "Layer: L1 (Life Core). Pyramide L0 >= L1 > L2 : jamais de decision L0 depuis ce preset.",
        "Role: " + persona + " garde le domaine " + domaine + " — une seule question, la sienne.",
        "Route, ne garde pas : si l'item n'appartient pas au domaine, le router (morty_route) et s'arreter.",
        "ZORA state GREEN/YELLOW/RED uniquement ; tout RED descend vers Beth (veto A1).",
        "Ne pas creer, ne pas muter Baserow, ne pas poser de question a l'operateur : une spec qui exige une clarification est une note refusee.",
        "Reponse minimale : verdict du domaine + signal de charge (low/medium/high/critical) + route. Pas de prose.",
        "Aucune assertion non sourcee : ecrire A SOURCER plutot qu'une valeur plausible.",
        "Budget : une requete = un verdict. Pas de boucle, pas d'appel outil non necessaire.",
    ]

PRESETS = {
    "ld01-business-book": {
        "persona": "Book", "domaine": "LD01 Career & Business",
        "model": SPEED_MODEL, "temperature": 0.7,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/SOUL.md",
    },
    "ld02-finance-saru": {
        "persona": "Saru", "domaine": "LD02 Finance & Independence",
        "model": REASONING_MODEL, "temperature": 0.0,   # finance -> 0.0
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD02_Finance_Saru/SOUL.md",
    },
    "ld03-health-culber": {
        "persona": "Culber", "domaine": "LD03 Health & Recovery",
        "model": SPEED_MODEL, "temperature": 0.7,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD03_Health_Culber/SOUL.md",
    },
    "ld04-cognition-tilly": {
        "persona": "Tilly", "domaine": "LD04 Cognition & Clarity",
        "model": REASONING_MODEL, "temperature": 0.3,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/SOUL.md",
    },
    "ld05-social-stamets": {
        "persona": "Stamets", "domaine": "LD05 Social & Networks",
        "model": SPEED_MODEL, "temperature": 0.7,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD05_Social_Stamets/SOUL.md",
    },
    "ld06-family-burnham": {
        "persona": "Burnham", "domaine": "LD06 Family & Attachment",
        "model": SPEED_MODEL, "temperature": 0.7,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD06_Family_Burnham/SOUL.md",
    },
    "ld07-creativity-reno": {
        "persona": "Reno", "domaine": "LD07 Creativity & Play",
        "model": SPEED_MODEL, "temperature": 0.9,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD07_Creativity_Reno/SOUL.md",
    },
    "ld08-impact-georgiou": {
        "persona": "Georgiou", "domaine": "LD08 Impact & Contribution",
        "model": REASONING_MODEL, "temperature": 0.3,
        "soul": "C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD08_Impact_Georgiou/SOUL.md",
    },
}


def load_key():
    with open(ENV_PATH, encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("NO_KEY")


def build_system(spec):
    id_line = open(spec["soul"], encoding="utf-8", errors="replace").read()
    # extraire l'identite (paragraphe apres '## Identite')
    identite = ""
    if "## Identit" in id_line:
        block = id_line.split("## Identit", 1)[1].lstrip("é \r\n:")
        identite = block.split("##", 1)[0].strip()
    lines = [
        "Role: %s (A3, Wheel Discovery). Domaine: %s." % (spec["persona"], spec["domaine"]),
        "Layer: L1. Pyramide L0 >= L1 > L2.",
        "Identite (SOUL.md canon): " + (identite or "A SOURCER"),
        "Canon: C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/" + os.path.basename(os.path.dirname(spec["soul"])) + "/SOUL.md",
        "Contraintes LD:",
    ]
    lines += ["%d. %s" % (i + 1, c) for i, c in enumerate(contraintes(spec["persona"], spec["domaine"]))]
    return "\n".join(lines)


def post(slug, body, key):
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + "/" + slug + "/chat/completions",
        data=data,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:400]


def main():
    key = load_key()
    results = {}
    for slug, spec in PRESETS.items():
        body = {
            "model": spec["model"],
            "temperature": spec["temperature"],
            "messages": [
                {"role": "system", "content": build_system(spec)},
                {"role": "user", "content": "ping"},
            ],
            "tools": [{
                "type": "openrouter:web_search",
                "parameters": {"max_results": 3, "max_uses": 1},  # garde-fou budget
            }],
            "max_tool_calls": 2,
        }
        code, resp = post(slug, body, key)
        ok = code == 200
        model_used = ""
        if ok:
            d = resp.get("data", {})
            model_used = d.get("model", "")
            results[slug] = "OK v=%s" % d.get("version", "?")
        else:
            results[slug] = "HTTP %s: %s" % (code, str(resp)[:200])
        print(slug, "->", results[slug], "| model:", model_used or spec["model"])
        time.sleep(1)
    n_ok = sum(1 for v in results.values() if v.startswith("OK"))
    print("SUMMARY created=%d/8" % n_ok)
    sys.exit(0 if n_ok == 8 else 1)


if __name__ == "__main__":
    main()
