# Spec — Jerry Business Pulse v1 : fichiers pulse.json par variante + verifier v1

- Rôle : Spec (ruban φ), L2 Buzz Core — pour 30_Business_OS (B1).
- Date : 2026-09-03 · Statut : executable, aucune question requise par le constructeur (test du ruban OK).
- Portée : évolution de `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/` de v0 vers v1. v0 est DÉJÀ EN PLACE (vérifié le 2026-09-01 : `00_Registre/registre.json` version "v0", 4 dossiers `01_Prime/ 02_Bio/ 03_Nexus/ 04_Solarpunk/` avec README.md, `verifier.py` 116 lignes). Cette spec n'ajoute rien hors de ce dossier.
- Spec amont : `C:/Users/amado/ASpace_OS_V3/00_Amadeus/60_Tape_Specs/2026-09-03-spec-jerry-business-pulse-v0.md` (conservée, non modifiée).

## Contexte

v0 = squelette : dossiers, README par variante, registre central, verifier v0.
v1 = premier état mesurable : chaque variante Jerry porte un `pulse.json` avec
trois métriques métier initialisées à zéro, et le verifier vérifie en PLUS des
checks v0 la validité de ces 4 fichiers. Aucun fichier v0 n'est supprimé ;
`registre.json` passe de `"version": "v0"` à `"version": "v1"` (seul champ modifié).
Python stdlib uniquement, ASCII sans accents dans tout le code, contenus en français.

## Quoi batir — OU (chemins absolus exacts)

Base : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/`

### 1. Quatre fichiers pulse.json — contenu EXACT, octet pour octet

Fichier `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/01_Prime/pulse.json` :

```json
{
  "id": "prime",
  "nom": "Jerry Prime",
  "domaine": "business classique",
  "metriques": {
    "revenus_mois": 0,
    "clients_actifs": 0,
    "offres_lancees": 0
  },
  "statut": "v1-initialise"
}
```

Fichier `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/02_Bio/pulse.json` :

```json
{
  "id": "bio",
  "nom": "Jerry Bio",
  "domaine": "bio/health",
  "metriques": {
    "revenus_mois": 0,
    "clients_actifs": 0,
    "offres_lancees": 0
  },
  "statut": "v1-initialise"
}
```

Fichier `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/03_Nexus/pulse.json` :

```json
{
  "id": "nexus",
  "nom": "Jerry Nexus",
  "domaine": "tech/plateforme",
  "metriques": {
    "revenus_mois": 0,
    "clients_actifs": 0,
    "offres_lancees": 0
  },
  "statut": "v1-initialise"
}
```

Fichier `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/04_Solarpunk/pulse.json` :

```json
{
  "id": "solarpunk",
  "nom": "Jerry Solarpunk",
  "domaine": "solaire/durabilite",
  "metriques": {
    "revenus_mois": 0,
    "clients_actifs": 0,
    "offres_lancees": 0
  },
  "statut": "v1-initialise"
}
```

Convention : encodage UTF-8 sans BOM, fin de ligne LF, une indentation de 2
espaces, aucune clé supplémentaire, aucune clé manquante.

### 2. registre.json — une seule modification

Dans `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/00_Registre/registre.json`,
remplacer la ligne `  "version": "v0",` par `  "version": "v1",`. Tout le reste
du fichier (`date_init`, les 4 variantes avec id/nom/dossier/cree) reste
strictement identique. Résultat attendu complet :

```json
{
  "version": "v1",
  "date_init": "2026-09-03",
  "variantes": [
    {
      "id": "prime",
      "nom": "Jerry Prime",
      "dossier": "01_Prime",
      "cree": "2026-09-03"
    },
    {
      "id": "bio",
      "nom": "Jerry Bio",
      "dossier": "02_Bio",
      "cree": "2026-09-03"
    },
    {
      "id": "nexus",
      "nom": "Jerry Nexus",
      "dossier": "03_Nexus",
      "cree": "2026-09-03"
    },
    {
      "id": "solarpunk",
      "nom": "Jerry Solarpunk",
      "dossier": "04_Solarpunk",
      "cree": "2026-09-03"
    }
  ]
}
```

### 3. verifier.py — REMPLACER intégralement par ce source v1

Fichier `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/verifier.py`
(source complet ci-dessous ; garde TOUS les checks v0, ajoute les checks v1) :

```python
#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verifier.py - Jerry Business Pulse v1.

Verifie la structure du pulse B1 :
  [v0] dossiers des 4 variantes presents
  [v0] registre.json valide (version, ordre des variantes)
  [v0] README de chaque variante non vide et portant "statut: v0-initialise"
  [v1] registre.json version == "v1"
  [v1] pulse.json de chaque variante : existe, JSON valide, id/nom/domaine
       corrects, 3 metriques a zero, statut == "v1-initialise"

Affiche PULSE_OK et retourne rc=0 si tout passe, sinon PULSE_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-03-spec-jerry-business-pulse-v1.md
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

VARIANTES = ["prime", "bio", "nexus", "solarpunk"]
DOSSIERS = {
    "prime": "01_Prime",
    "bio": "02_Bio",
    "nexus": "03_Nexus",
    "solarpunk": "04_Solarpunk",
}
NOMS = {
    "prime": "Jerry Prime",
    "bio": "Jerry Bio",
    "nexus": "Jerry Nexus",
    "solarpunk": "Jerry Solarpunk",
}
DOMAINES = {
    "prime": "business classique",
    "bio": "bio/health",
    "nexus": "tech/plateforme",
    "solarpunk": "solaire/durabilite",
}
STATUT = "statut: v0-initialise"
PULSE_STATUT = "v1-initialise"
METRIQUES = ["revenus_mois", "clients_actifs", "offres_lancees"]


def main():
    erreurs = []

    # 1. README racine non vide
    readme_racine = os.path.join(BASE, "README.md")
    if not os.path.isfile(readme_racine) or os.path.getsize(readme_racine) == 0:
        erreurs.append("README.md racine manquant ou vide")

    # 2. Dossiers des 4 variantes presents
    for vid in VARIANTES:
        d = os.path.join(BASE, DOSSIERS[vid])
        if not os.path.isdir(d):
            erreurs.append("dossier manquant: " + DOSSIERS[vid])

    # 3. Registre central
    reg_path = os.path.join(BASE, "00_Registre", "registre.json")
    if not os.path.isfile(reg_path):
        erreurs.append("00_Registre/registre.json manquant")
    else:
        try:
            with open(reg_path, "r", encoding="utf-8") as f:
                reg = json.load(f)
            if reg.get("version") != "v1":
                erreurs.append("registre.json: version != v1")
            if reg.get("date_init") != "2026-09-03":
                erreurs.append("registre.json: date_init != 2026-09-03")
            ids = [v.get("id") for v in reg.get("variantes", [])]
            if ids != VARIANTES:
                erreurs.append(
                    "registre.json: variantes != " + str(VARIANTES) + " (trouve " + str(ids) + ")"
                )
            for v in reg.get("variantes", []):
                vid = v.get("id")
                if vid not in VARIANTES:
                    erreurs.append("registre.json: id inconnu " + repr(vid))
                    continue
                attendu_dossier = DOSSIERS[vid]
                if v.get("dossier") != attendu_dossier:
                    erreurs.append(
                        "registre.json: " + vid + " dossier != " + attendu_dossier
                        + " (trouve " + repr(v.get("dossier")) + ")"
                    )
                if v.get("nom") != NOMS[vid]:
                    erreurs.append(
                        "registre.json: " + vid + " nom != " + NOMS[vid]
                        + " (trouve " + repr(v.get("nom")) + ")"
                    )
                if v.get("cree") != "2026-09-03":
                    erreurs.append("registre.json: " + vid + " cree != 2026-09-03")
        except (ValueError, OSError) as e:
            erreurs.append("registre.json illisible: " + str(e))

    # 4. README de chaque variante : non vide + statut present
    for vid in VARIANTES:
        p = os.path.join(BASE, DOSSIERS[vid], "README.md")
        if not os.path.isfile(p):
            erreurs.append(DOSSIERS[vid] + "/README.md manquant")
            continue
        if os.path.getsize(p) == 0:
            erreurs.append(DOSSIERS[vid] + "/README.md vide")
            continue
        with open(p, "r", encoding="utf-8") as f:
            contenu = f.read()
        if STATUT not in contenu:
            erreurs.append(DOSSIERS[vid] + "/README.md sans '" + STATUT + "'")
        titre = "# " + NOMS[vid]
        if titre not in contenu:
            erreurs.append(DOSSIERS[vid] + "/README.md sans titre '" + titre + "'")

    # 5. [v1] pulse.json de chaque variante
    for vid in VARIANTES:
        p = os.path.join(BASE, DOSSIERS[vid], "pulse.json")
        if not os.path.isfile(p):
            erreurs.append(DOSSIERS[vid] + "/pulse.json manquant")
            continue
        try:
            with open(p, "r", encoding="utf-8") as f:
                pulse = json.load(f)
        except (ValueError, OSError) as e:
            erreurs.append(DOSSIERS[vid] + "/pulse.json illisible: " + str(e))
            continue
        if pulse.get("id") != vid:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: id != " + vid
                + " (trouve " + repr(pulse.get("id")) + ")"
            )
        if pulse.get("nom") != NOMS[vid]:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: nom != " + NOMS[vid]
                + " (trouve " + repr(pulse.get("nom")) + ")"
            )
        if pulse.get("domaine") != DOMAINES[vid]:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: domaine != " + DOMAINES[vid]
                + " (trouve " + repr(pulse.get("domaine")) + ")"
            )
        met = pulse.get("metriques")
        if not isinstance(met, dict):
            erreurs.append(DOSSIERS[vid] + "/pulse.json: metriques absentes ou non objet")
        else:
            for m in METRIQUES:
                if m not in met:
                    erreurs.append(DOSSIERS[vid] + "/pulse.json: metrique manquante " + m)
                elif met[m] != 0:
                    erreurs.append(
                        DOSSIERS[vid] + "/pulse.json: metrique " + m
                        + " != 0 (trouve " + repr(met[m]) + ")"
                    )
        if pulse.get("statut") != PULSE_STATUT:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: statut != " + PULSE_STATUT
                + " (trouve " + repr(pulse.get("statut")) + ")"
            )

    if erreurs:
        print("PULSE_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("PULSE_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### 4. Ce qui ne change PAS

- `README.md` racine et les 4 `README.md` de variantes : inchangés (le check v0
  sur `statut: v0-initialise` est conservé).
- Aucun nouveau dossier. Aucun fichier hors de `00_Jerry_Business_Pulse/`.
- `10_Tech_OS/kernel/uc.db` : non touché.

## Critere d'acceptation

- [ ] `ls C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/0*/pulse.json` liste exactement 4 fichiers : `01_Prime/pulse.json`, `02_Bio/pulse.json`, `03_Nexus/pulse.json`, `04_Solarpunk/pulse.json`
- [ ] `python -c "import json;[json.load(open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/%s/pulse.json'%d,encoding='utf-8')) for d in ('01_Prime','02_Bio','03_Nexus','04_Solarpunk')]"` retourne rc=0
- [ ] `python -c "import json;assert json.load(open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/00_Registre/registre.json'))['version']=='v1'"` retourne rc=0
- [ ] `python C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/verifier.py` affiche `PULSE_OK` et retourne rc=0
- [ ] Test négatif (optionnel, après la vérification finale, puis rétablir) : renommer un `pulse.json` doit faire afficher `PULSE_KO` avec rc=1 ; renommer en arrière doit rétablir `PULSE_OK` rc=0

## Commande de verification finale

```
python C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/verifier.py
```

Résultat attendu : `PULSE_OK` sur stdout, code de retour 0.

## Contraintes

- Ne rien écrire hors `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/`.
- Ne pas modifier `10_Tech_OS/kernel/uc.db` ni `60_Tape_Specs/2026-09-03-spec-jerry-business-pulse-v0.md`.
- Python stdlib uniquement (json, os, sys) — aucune dépendance pip, aucune donnée business réelle (toutes les métriques à 0).
- Tout le code Python en ASCII sans accents (coding: ascii), contenus en français.
- Ne pas supprimer ni renommer de fichier v0 existant.
