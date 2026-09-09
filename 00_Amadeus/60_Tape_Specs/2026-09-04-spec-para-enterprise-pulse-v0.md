---
id: spec-para-enterprise-pulse-v0
title: "PARA Enterprise pulse v0 : registre 4 categories PARA + verify_para.py dans 24_PARA_Enterprise"
date: 2026-09-04
layer: L1
status: active
type: ruban-phi
target: 20_Life_OS/24_PARA_Enterprise
framework: PARA Enterprise (A2, officier Enterprise)
persona_spec: A2_Computer_Enterprise_Spec.md
pattern_source:
  - 20_Life_OS/25_GTD_Cerritos/pulse.json
  - 20_Life_OS/25_GTD_Cerritos/verify_gtd.py
  - 20_Life_OS/26_DEAL_Protostar/verify_deal.py
version: v0
---

# Ruban φ — PARA Enterprise Pulse v0

## Objectif

Donner au framework `20_Life_OS/24_PARA_Enterprise/` son pulse v0 : un registre
machine (`registre_para.json`) des 4 categories PARA, peuple depuis les dossiers
existants, plus un verificateur executabable (`verify_para.py`, stdlib uniquement)
qui relit le registre et verifie sa coherence avec le disque. Pattern copie mesure
sur GTD Cerritos (pulse.json + verify_gtd.py) et DEAL Protostar (verify_deal.py) :
python stdlib uniquement, francais ASCII sans accents, criteres numerotes,
sortie OK/KO, rc 0/1.

## Critère d'acceptation

1. `C:/Users/amado/ASpace_OS_V3/20_Life_OS/24_PARA_Enterprise/registre_para.json`
   existe, est un JSON valide et porte exactement les 4 cles :
   `projects`, `areas`, `resources`, `archives`.
2. `registre_para.json` contient en tete : `"version": "v0"`,
   `"date_init": "2026-09-04"`, `"framework": "PARA Enterprise"`.
3. Chaque categorie liste les entrees mesurees sur le disque (noms de fichiers
   et sous-dossiers de premier niveau, hors `AGENT.md`, `A3_*_Spec.md`,
   `SOUL.md`) :
   - `projects` depuis `01_Projects_Picard/` (ce dossier ne porte que AGENT.md
     et SOUL.md aujourd'hui : liste vide `[]` est l'etat correct v0) ;
   - `areas` depuis `02_Areas_Spock/` ;
   - `resources` depuis `03_Resources_Geordi/` ;
   - `archives` depuis `04_Archives_Data/`.
   Si le disque evolue, c'est le registre qu'on met a jour — jamais l'inverse.
4. `C:/Users/amado/ASpace_OS_V3/20_Life_OS/24_PARA_Enterprise/verify_para.py`
   existe, execute par python 3 stdlib uniquement (imports limites a
   json/os/sys), francais ASCII sans accents, criteres numerotes en docstring,
   style identique a `verify_gtd.py`.
5. `verify_para.py` verifie, dans l'ordre numerote :
   [1] registre_para.json present, JSON valide, version v0, date_init
       2026-09-04, framework "PARA Enterprise", 4 cles exactes ;
   [2] les 4 dossiers `01_Projects_Picard`, `02_Areas_Spock`,
       `03_Resources_Geordi`, `04_Archives_Data` existent ;
   [3] pour chaque categorie, la liste du registre est exactement l'ensemble
       des entrees de premier niveau du dossier correspondant, hors les
       fichiers systeme exclus (AGENT.md, A3_*_Spec.md, SOUL.md) ;
       toute difference (manquant ou surplus) est une erreur nommee ;
   [4] la racine porte `A2_Computer_Enterprise_Spec.md` non vide
       (spec A2 fait foi).
6. `python verify_para.py` affiche `PARA_OK` et retourne rc=0 quand tout passe,
   `PARA_KO` avec la liste des erreurs et rc=1 sinon.

## Commandes de preuve

```bash
cd C:/Users/amado/ASpace_OS_V3/20_Life_OS/24_PARA_Enterprise
python verify_para.py ; echo "rc=$?"
python -c "import json;d=json.load(open('registre_para.json'));print(sorted(d.keys()))"
```

Preuve attendue : `PARA_OK`, `rc=0`, cles `['areas','archives','projects','resources']`.

## Périmètre

- Ce ruban ne cree que `registre_para.json` et `verify_para.py` a la racine du
  framework (admises par le portier). Aucun fichier existant n'est modifie.
- Test du ruban (AGENTS.md racine, §3) : un constructeur doit pouvoir executer
  sans poser une seule question a l'operateur.

## Interdits

- Pas de dependance hors stdlib. Pas d'accents ni de caracteres non ASCII
  dans le code et les donnees produites.
