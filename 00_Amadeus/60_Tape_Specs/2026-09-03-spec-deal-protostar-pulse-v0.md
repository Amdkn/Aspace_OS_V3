# Spec — DEAL Protostar Pulse v0 : pulse.json + verify_deal.py (registre + verifier, pattern prouve)

- Role : Spec (ruban φ), L1 Life Core (11e Docteur) — pour 20_Life_OS/26_DEAL_Protostar.
- Date : 2026-09-03 · Statut : executable, aucune question requise par le constructeur (test du ruban OK).
- Modele exact : `2026-09-03-spec-gtd-cerritos-pulse-v0.md` et sa realisation dans
  `25_GTD_Cerritos/` (`pulse.json` + `verify_gtd.py`, work #39 status done).

## Contexte — etat mesure au 2026-09-03

Mesure directe de `C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/` :
- La racine porte : `A2_HoloJaneway_Protostar_Spec.md`, `A3_Protostar_References_Index.md`,
  `AGENTS.md`, `README.md`, `SOUL.md`.
- Les 4 dossiers de stage existent, chacun avec exactement 4 fichiers :
  - `01_Definition_Dal/` — `A3_Dal_Definition_Spec.md`, `AGENT.md`, `README.md`, `SOUL.md`
  - `02_Elimination_RokTahk/` — `A3_RokTahk_Elimination_Spec.md`, `AGENT.md`, `README.md`, `SOUL.md`
  - `03_Automation_Zero/` — `A3_Zero_Automation_Spec.md`, `AGENT.md`, `README.md`, `SOUL.md`
  - `04_Liberation_Gwyn/` — `A3_Gwyn_Liberation_Spec.md`, `AGENT.md`, `README.md`, `SOUL.md`
- **Aucun artefact de donnees** n'existe dans les 4 dossiers (mesure `ls -a` :
  aucun fichier hors des 4 ci-dessus, pas de `__pycache__`, pas de `.json`, pas de `.md`
  de donnees). Tous les `artefact` sont donc `null` en v0.
- **Aucun verifier ni pulse.json n'existe** dans ce framework. Le pattern est prouve
  dans `25_GTD_Cerritos/` (`verify_gtd.py` affiche `GTD_OK`/`GTD_KO`, rc 0/1, stdlib).

## Objectif

Ajouter a `26_DEAL_Protostar/` son premier etat mesurable, sur le pattern deja prouve :

1. `pulse.json` a la racine du framework : le registre-pulse DEAL (4 etapes,
   leurs personas canon actif, chemins des specs, version v0).
2. `verify_deal.py` a la racine du framework : verifier stdlib qui valide la
   structure des 4 etapes, le frontmatter/nom des specs A3, et le pulse.json.

Python stdlib uniquement (json, os, sys), ASCII sans accents dans le code,
contenus en francais. Aucune dependance pip.

## Quoi batir — OU (chemins absolus exacts)

Base : `C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/`

### 1. Fichier `C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/pulse.json` — contenu EXACT

```json
{
  "version": "v0",
  "date_init": "2026-09-03",
  "framework": "DEAL Protostar",
  "canon_4_stages": [
    {
      "stage": "definition",
      "dossier": "01_Definition_Dal",
      "persona": "Dal",
      "spec": "A3_Dal_Definition_Spec.md",
      "artefact": null
    },
    {
      "stage": "elimination",
      "dossier": "02_Elimination_RokTahk",
      "persona": "RokTahk",
      "spec": "A3_RokTahk_Elimination_Spec.md",
      "artefact": null
    },
    {
      "stage": "automation",
      "dossier": "03_Automation_Zero",
      "persona": "Zero",
      "spec": "A3_Zero_Automation_Spec.md",
      "artefact": null
    },
    {
      "stage": "liberation",
      "dossier": "04_Liberation_Gwyn",
      "persona": "Gwyn",
      "spec": "A3_Gwyn_Liberation_Spec.md",
      "artefact": null
    }
  ]
}
```

Convention : encodage UTF-8 sans BOM, fin de ligne LF, indentation 2 espaces,
aucune cle supplementaire, aucune cle manquante. `artefact: null` signifie
"aucun artefact de donnees encore produit a ce stage" — verifie comme `null`.

### 2. Fichier `C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/verify_deal.py` — source complet

```python
#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verify_deal.py - DEAL Protostar Pulse v0.

Verifie la structure du framework DEAL Protostar :
  [1] pulse.json present, JSON valide, version v0, date_init, 4 etapes dans l'ordre
  [2] les 4 dossiers de stage existent
  [3] chaque stage porte sa spec A3_*_Spec.md non vide, son AGENT.md, son README.md, son SOUL.md
  [4] la racine porte A2_HoloJaneway_Protostar_Spec.md non vide (spec A2 fait foi)

Affiche DEAL_OK et retourne rc=0 si tout passe, sinon DEAL_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-03-spec-deal-protostar-pulse-v0.md
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

STAGES = ["definition", "elimination", "automation", "liberation"]
DOSSIERS = {
    "definition": "01_Definition_Dal",
    "elimination": "02_Elimination_RokTahk",
    "automation": "03_Automation_Zero",
    "liberation": "04_Liberation_Gwyn",
}
PERSONAS = {
    "definition": "Dal",
    "elimination": "RokTahk",
    "automation": "Zero",
    "liberation": "Gwyn",
}
SPECS = {
    "definition": "A3_Dal_Definition_Spec.md",
    "elimination": "A3_RokTahk_Elimination_Spec.md",
    "automation": "A3_Zero_Automation_Spec.md",
    "liberation": "A3_Gwyn_Liberation_Spec.md",
}
ARTEFACTS = {
    "definition": None,
    "elimination": None,
    "automation": None,
    "liberation": None,
}
A2_SPEC = "A2_HoloJaneway_Protostar_Spec.md"


def main():
    erreurs = []

    # 1. pulse.json
    pulse_path = os.path.join(BASE, "pulse.json")
    if not os.path.isfile(pulse_path):
        erreurs.append("pulse.json manquant")
    else:
        try:
            pulse = json.load(open(pulse_path, "r", encoding="utf-8"))
        except (ValueError, OSError) as e:
            pulse = None
            erreurs.append("pulse.json illisible: " + str(e))
        if pulse is not None:
            if pulse.get("version") != "v0":
                erreurs.append("pulse.json: version != v0 (trouve " + repr(pulse.get("version")) + ")")
            if pulse.get("date_init") != "2026-09-03":
                erreurs.append("pulse.json: date_init != 2026-09-03")
            if pulse.get("framework") != "DEAL Protostar":
                erreurs.append("pulse.json: framework != DEAL Protostar")
            stages = [s.get("stage") for s in pulse.get("canon_4_stages", [])]
            if stages != STAGES:
                erreurs.append("pulse.json: stages != " + str(STAGES) + " (trouve " + str(stages) + ")")
            for s in pulse.get("canon_4_stages", []):
                st = s.get("stage")
                if st not in STAGES:
                    erreurs.append("pulse.json: stage inconnu " + repr(st))
                    continue
                if s.get("dossier") != DOSSIERS[st]:
                    erreurs.append("pulse.json: " + st + " dossier != " + DOSSIERS[st])
                if s.get("persona") != PERSONAS[st]:
                    erreurs.append("pulse.json: " + st + " persona != " + PERSONAS[st])
                if s.get("spec") != SPECS[st]:
                    erreurs.append("pulse.json: " + st + " spec != " + SPECS[st])
                if s.get("artefact") != ARTEFACTS[st]:
                    erreurs.append("pulse.json: " + st + " artefact != " + repr(ARTEFACTS[st]))

    # 2 + 3. dossiers, specs, AGENT/README/SOUL
    for st in STAGES:
        d = os.path.join(BASE, DOSSIERS[st])
        if not os.path.isdir(d):
            erreurs.append("dossier manquant: " + DOSSIERS[st])
            continue
        for nom in [SPECS[st], "AGENT.md", "README.md", "SOUL.md"]:
            p = os.path.join(d, nom)
            if not os.path.isfile(p):
                erreurs.append(DOSSIERS[st] + "/" + nom + " manquant")
            elif os.path.getsize(p) == 0:
                erreurs.append(DOSSIERS[st] + "/" + nom + " vide")

    # 4. spec A2 racine fait foi
    a2 = os.path.join(BASE, A2_SPEC)
    if not os.path.isfile(a2):
        erreurs.append(A2_SPEC + " manquant")
    elif os.path.getsize(a2) == 0:
        erreurs.append(A2_SPEC + " vide")

    if erreurs:
        print("DEAL_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("DEAL_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### 3. Ce qui ne change PAS

- Aucun fichier existant de `26_DEAL_Protostar/` n'est modifie ni supprime.
- Aucun nouveau dossier. Aucun fichier hors de `26_DEAL_Protostar/`.
- `10_Tech_OS/kernel/uc.db` : non touche par le constructeur (l'INSERT est fait
  par le Spec au depot du ruban). Rubans amont : non modifies.

## Etapes executables sans question

1. Ecrire `pulse.json` avec le contenu exact du bloc 1.
2. Ecrire `verify_deal.py` avec le source exact du bloc 2 (UTF-8, LF).
3. Lancer le verifier ; si `DEAL_KO`, corriger l'objet nomme par l'erreur
   (jamais le verifier) et relancer.
4. Test negatif une fois, puis retablissement :
   - renommer `pulse.json` en `pulse.json.bak` → verifier doit afficher `DEAL_KO` rc=1
     avec exactement 1 ligne `ERREUR:` mentionnant `pulse.json` ;
   - renommer en arriere → `DEAL_OK` rc=0.

## Criteres de verification (commande + rc attendu)

```
python C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/verify_deal.py
```
Attendu : `DEAL_OK` sur stdout, rc=0.

```
python -c "import json;d=json.load(open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/pulse.json',encoding='utf-8'));assert d['version']=='v0' and len(d['canon_4_stages'])==4"
```
Attendu : rc=0.

```
python -c "import py_compile;py_compile.compile(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/verify_deal.py',doraise=True)"
```
Attendu : rc=0.

## Prediction verifiable (loi de prediction — enregistrer AVANT execution)

- Prediction P1 : le verifier v0 affiche `DEAL_OK` et retourne rc=0 au premier
  lancement apres ecriture des 2 fichiers, sans modification d'un fichier
  existant. Verifiable par la commande ci-dessus.
- Prediction P2 : le test negatif (renommer pulse.json) produit `DEAL_KO` rc=1 avec
  exactement 1 ligne `ERREUR:` mentionnant `pulse.json`. Verifiable par l'etape 4.
- Si P1 echoue, la prediction est marquee `FALSIFIEE` dans le retour de review —
  pas de reecriture retroactive.

## Contraintes

- Ne rien ecrire hors `C:/Users/amado/ASpace_OS_V3/20_Life_OS/26_DEAL_Protostar/`.
- Python stdlib uniquement (json, os, sys) — aucune dependance pip.
- Tout le code Python en ASCII sans accents (coding: ascii), contenus en francais.
- Ne pas prononcer `done` : detache par le 11e Docteur depuis `review` seulement.
