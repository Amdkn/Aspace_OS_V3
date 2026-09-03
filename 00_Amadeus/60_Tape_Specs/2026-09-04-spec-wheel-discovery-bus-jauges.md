---
title: "Wheel Discovery: bus d etat + jauges LD01-LD08 fonctionnelles"
layer: L1
---

## Objectif

Donner au framework `20_Life_OS/22_Wheel_Discovery/` (A2 Discovery/ZORA, spec `A2_Discovery_ZORA_Spec.md`) un **bus d'état machine** et des **jauges fonctionnelles** pour les 8 domaines LD01-LD08, sans toucher un seul fichier canon existant. Aujourd'hui l'état ZORA n'existe que comme YAML d'exemple dans la spec ; ce work le matérialise en fichiers JSON lisibles par machine, avec un vérificateur exécutable chiffré (contrat D1 receipt du `LD01_Business_Book/AGENTS.md`).

Les 8 personas LD (canon §Crew de la spec ZORA) : Book (LD01 Business), Saru (LD02 Finance), Culber (LD03 Health), Tilly (LD04 Cognition), Stamets (LD05 Social), Burnham (LD06 Family), Reno (LD07 Creativity), Georgiou (LD08 Impact).

## Périmètre

Tout est **nouveau** (création), sous `C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/` :

1. `state.json` — bus d'état central ZORA. JSON avec les clés (alignées §Outputs de la spec ZORA) :
   - `ship: "DISCOVERY"`, `framework: "Life Wheel / ZORA"`,
   - `updated` (date ISO de création),
   - `domains` : objet à 8 clés `LD01`…`LD08`, chacune `{ "persona": <nom canon>, "zora_state": "GREEN", "load_signal": "low", "beth_action": "none", "morty_route": <un de ORVILLE_IKIGAI|SNW_12WY|ENTERPRISE_PARA|CERRITOS_GTD|PROTOSTAR_DEAL> }`,
   - `evidence_paths: []` (liste vide, alimentée plus tard par Discovery).
   Taille < 10240 octets (garde-fou rotation, cf. modèle 23_12WY_SNW).
2. Un fichier d'état par domaine : `LD01_Business_Book/state.json`, `LD02_Finance_Saru/state.json`, `LD03_Health_Culber/state.json`, `LD04_Cognition_Tilly/state.json`, `LD05_Social_Stamets/state.json`, `LD06_Family_Burnham/state.json`, `LD07_Creativity_Reno/state.json`, `LD08_Impact_Georgiou/state.json`. Chacun : `{ "domain": "LDxx", "persona": <nom canon>, "zora_state": "GREEN|YELLOW|RED", "load_signal": "low|medium|high|critical", "notes": [], "updated": <ISO> }` — état initial GREEN/low (aucune donnée réelle inventée).
3. `LD01_Business_Book/state_okf_2026-09-04.md` … et l'équivalent dans les 7 autres dossiers LD — **non** : un seul fichier OKF par domaine, nommé `state_okf.md`, créé **seulement s'il n'existe pas déjà** (check avant création). Frontmatter YAML minimal conforme OKF 0.2 (au minimum `type: dox-state-jauge`, plus `domain`, `persona`, `parent`), corps ≤ 20 lignes décrivant la jauge. Si un `state_okf.md` existe déjà dans un dossier LD : ne pas le modifier, append seulement (additivité).
4. `verify_wheel.py` — vérificateur exécutable (nouveau fichier, à la racine du framework). Python 3 standard-library uniquement. Il :
   - charge `state.json`, valide le schéma (8 domaines, personas canon exacts, valeurs ZORA dans les enums de la spec),
   - charge les 8 `state.json` de domaine, vérifie la cohérence avec le bus,
   - imprime un rapport chiffré : `domains_ok=8/8`, `schema_valid=true`, et sort `rc=0` si tout passe, `rc=1` sinon.

## Périmètre (hors champ)

- `A2_Discovery_ZORA_Spec.md`, `A3_Discovery_References_Index.md`, `AGENTS.md`, `README.md`, `SOUL.md` à la racine du framework : **lecture seule**.
- Tout fichier canon existant dans les 8 dossiers LD (notamment `A3_Book_LD01_Spec.md`, `BIBLIOGRAPHY.md`, `README.md`, `01_Guides_Business/`, `00_index.md`, `30_decisions/`, `90_manifests/`, `99_meta/` de LD01) : **lecture seule**, additivité stricte (contrat 1 du `LD01_Business_Book/AGENTS.md`). Si un append est fait dans `99_meta/rot-rates.md` de LD01 pour déclarer la ROT du module (contrat 4), il est append-only.
- Tout autre framework 20_Life_OS (21, 23, 24, 25, 26) et `00_Gatekeepers_Beth_Morty/`.
- `10_Tech_OS/kernel/` (uc.db, gate.py, schema.sql) — noyau sacré.

## Critère d'acceptation

- [ ] `ls C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/` contient `state.json` et `verify_wheel.py` (2 nouvelles entrées racine au-delà des 14 existantes mesurées 2026-09-04, soit 16 entrées au total).
- [ ] `cat C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/state.json | python -m json.tool` retourne rc=0 et contient exactement 8 clés `LD01`…`LD08` dans `domains`, chacune avec `persona` ∈ {Book, Saru, Culber, Tilly, Stamets, Burnham, Reno, Georgiou} (1:1, aucune permutation).
- [ ] `ls C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/LD0*/state.json | wc -l` retourne **8**.
- [ ] `python C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/verify_wheel.py` sort `domains_ok=8/8` et `schema_valid=true`, et retourne **rc=0**.
- [ ] `python -c "import json,sys; d=json.load(open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/state.json')); import os; print(os.path.getsize(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/state.json')<10240)"` affiche `True` (garde-fou rotation).
- [ ] Chaque `LD0*/state_okf.md` existant ouvre par un frontmatter YAML contenant une ligne `^type:` (`grep -c "^type:" LD0*/state_okf.md` ≥ 1 par fichier) — contrat frontmatter OKF du `LD01_Business_Book/AGENTS.md`.
- [ ] `git -C C:/Users/amado/ASpace_OS_V3 status --porcelain` après le build ne montre **aucun fichier canon modifié** (uniquement des créations, prefixe double-point-interrogation de git) — additivité stricte.

## Interdits

- Ne pas écrire dans `20_Life_OS/00_Gatekeepers_Beth_Morty/` (veto A1 Beth).
- Ne pas modifier `10_Tech_OS/kernel/` — noyau sacré.
- Ne toucher à aucun fichier canon listé « dehors ». Toute mutation d'un fichier existant = append, jamais réécriture.
- Ne pas inventer de donnée d'état réelle : initialisation neutre GREEN/low uniquement ; les vraies valeurs viennent des observations Sunday Uplink / Baserow, pas du constructeur.
- Ne pas marquer `done` : seul le 11e Docteur détache depuis `review`.
- Ne pas écrire dans `~/.hermes/` (stub legacy) ni dans un profil Hermes autre que `amy_spec_l1`.

## Vérifieur (D1 receipt)

Commande unique, sortie chiffrée :

```bash
python C:/Users/amado/ASpace_OS_V3/20_Life_OS/22_Wheel_Discovery/verify_wheel.py
# attendu: domains_ok=8/8  schema_valid=true  (rc=0)
```
