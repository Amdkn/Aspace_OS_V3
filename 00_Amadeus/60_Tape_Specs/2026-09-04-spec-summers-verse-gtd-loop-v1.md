---
id: spec-summers-verse-gtd-loop-v1
date: 2026-09-04
layer: L2
owner: doctor12_l2
status: active
type: ruban-phi
os: 30_Business_OS
target: 30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd/
work: 43
tape_source: 00_Amadeus/60_Tape_Specs/2026-09-03-summers-verse-boucle-gtd-cerritos-appliquee-au-p.md
---

# SPEC Summers Verse - boucle GTD Cerritos sur le projet actif v1

> Ruban phi detaille du work 43 (`10_Tech_OS/kernel/uc.db`, table `work`,
> tape 35 FROZEN : "Summers Verse: boucle GTD Cerritos appliquee au projet
> actif (registre + verifier)"). Le tape FROZEN est trop generique : ce
> fichier en est la version executable, aucun constructeur ne doit poser une
> question a l'operateur (test du ruban, `AGENTS.md` racine, §3).
> Chemin : `C:/Users/amado/ASpace_OS_V3/00_Amadeus/60_Tape_Specs/2026-09-04-spec-summers-verse-gtd-loop-v1.md`
> Pattern V3 mesure (lecture directe) : `20_Life_OS/25_GTD_Cerritos/verify_gtd.py`
> (python stdlib uniquement, francais ASCII sans accents, criteres numerotes,
> sortie OK/KO, rc 0/1) et `20_Life_OS/25_GTD_Cerritos/pulse.json`
> (registre JSON plat, indent=2, UTF-8, canon 5 stages).
> Contexte cible mesure (listing du 2026-09-04) : `30_Business_OS/00_Summers_Verse/`
> existe avec `registre_solaris.json`, `verifier.py`, `verifier_solaris.py`,
> `verifier_solaris_12wy.py`, `registre_solaris_12wy.json`, `00_Registre/registre.json`,
> `projects/coach-os-app/` (contient `README.md`). Projet actif :
> `projects/coach-os-app`.

## 1. Objectif

Creer la boucle GTD Cerritos appliquee au projet actif `coach-os-app` dans le
dossier NOUVEAU `30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd/` :

- un registre `gtd.json` (JSON plat, indent=2, lisible par
  `python -m json.tool`, rc=0) declarant le verse, le projet et les 5 stages ;
- `apply_gtd.py` qui fait tourner les 5 stages GTD Cerritos
  (capture / clarify / organize / review / engage) sur le projet actif, en
  lecture de l'inbox graine et en ecriture d'un fichier JSON par stage ;
- `verifier.py` qui teste le tout, criteres numerotes `[1]`-`[6]`, et affiche
  `GTDLOOP_OK` (rc=0) ou `GTDLOOP_KO` (rc=1).

Le tape FROZEN (tape 35) ne fixait ni chemin exact, ni format de registre, ni
regles de stages : tout est fixe ici.

## 2. Livrables (chemins exacts)

```
30_Business_OS/00_Summers_Verse/projects/coach-os-app/
├── README.md                        (EXISTANT, non modifie)
└── gtd/                             (NOUVEAU - tout le livrable)
    ├── gtd.json                     (NOUVEAU - registre, section 3.1)
    ├── apply_gtd.py                 (NOUVEAU - moteur 5 stages, section 3.3)
    ├── verifier.py                  (NOUVEAU - verificateur, section 3.4)
    └── 01_Capture_Mariner/
        └── inbox.md                 (NOUVEAU - inbox graine, section 3.2)
```

Les dossiers `02_Clarify_Boimler/`, `03_Organize_Rutherford/`,
`04_Review_Tendi/`, `05_Engage_Freeman/` et leurs fichiers `*.json` sont
CREES PAR `apply_gtd.py` a l'execution (pas par le constructeur). A la
livraison, `gtd/` ne contient que les 4 fichiers ci-dessus.

## 3. Etapes executable

### 3.1 gtd.json - contenu exact

Ecrit avec `json.dump(..., indent=2)` + saut de ligne final, encodage UTF-8.
Contenu verbatim :

```json
{
  "version": "v1",
  "date_init": "2026-09-04",
  "framework": "GTD Cerritos",
  "verse": "Summers Verse",
  "projet": "coach-os-app",
  "source_tape": "00_Amadeus/60_Tape_Specs/2026-09-04-spec-summers-verse-gtd-loop-v1.md",
  "source_pulse": "20_Life_OS/25_GTD_Cerritos/pulse.json",
  "stages": ["capture", "clarify", "organize", "review", "engage"]
}
```

### 3.2 01_Capture_Mariner/inbox.md - contenu exact

Donnee d'entree graine de la boucle. Contenu verbatim (UTF-8, sans accents) :

```
# Inbox - Mariner (Capture)

## Items
- [ ] ACTION: ecrire la page Plan du coach-os-app
- [ ] INFO: pattern verifier V3 mesure dans 00_Jerry_Business_Pulse
- [ ] QUESTION: quel domaine B2 porte la version payante?
```

Ces 3 items rendent toutes les valeurs de sortie deterministes (section 3.4,
critere [5]). Le fichier est dans `gtd/` : aucun fichier existant de
`00_Summers_Verse/` n'est touche.

### 3.3 apply_gtd.py - comportement exact

- Shebang `#!/usr/bin/env python3`, coding `# -*- coding: ascii -*-`,
  docstring francais ASCII citant cette spec, le projet actif et l'usage.
- Stdlib uniquement : `sys`, `os`, `json`, `datetime`.
- CLI : `python apply_gtd.py`, sans argument requis ; la racine de la boucle
  est `os.path.dirname(os.path.abspath(__file__))`.
  - `-h/--help` : usage sur stdout, rc=2 (usage incorrect, distinct de
    l'echec rc=1).
- Lecture de `gtd/gtd.json` : s'il est absent, illisible, ou si `stages` !=
  `["capture", "clarify", "organize", "review", "engage"]`, affiche
  `GTDLOOP_APPLY_KO` + une ligne `  ERREUR: <detail>` sur stdout et rc=1.
- Les 5 stages tournent en sequence sur l'inbox, chaque stage cree son
  dossier si absent (`os.makedirs(..., exist_ok=True)`) et ecrit son JSON
  avec `json.dump(..., indent=2)` + saut de ligne final, UTF-8 :

  1. **capture** : lit `01_Capture_Mariner/inbox.md` ; items = lignes
     commencant par `- [ ] ` sous la section `## Items`, prefixes enleves.
     Ecrit `01_Capture_Mariner/capture.json` :
     ```json
     {"stage": "capture", "source": "01_Capture_Mariner/inbox.md",
      "items": ["ACTION: ecrire la page Plan du coach-os-app",
                "INFO: pattern verifier V3 mesure dans 00_Jerry_Business_Pulse",
                "QUESTION: quel domaine B2 porte la version payante?"]}
     ```
     (champs `stage` et `source` d'abord, `items` ensuite, dans cet ordre de
     cle). Inbox absent ou sans item : `items: []` et les stages suivants
     produisent des listes vides - ce n'est pas une erreur.
  2. **clarify** : classe chaque item par prefixe (sensible a la casse, le
     reste de la ligne apres le prefixe, `.strip()` = texte de l'item) :
     prefixe `ACTION:` -> type `action` ; `INFO:` -> type `info` ;
     `QUESTION:` -> type `question` ; prefixe inconnu -> type `action`
     (regle par defaut fixee ici, aucune question a poser).
     Ecrit `02_Clarify_Boimler/clarify.json` :
     ```json
     {"stage": "clarify",
      "decisions": [
        {"item": "ecrire la page Plan du coach-os-app", "type": "action"},
        {"item": "pattern verifier V3 mesure dans 00_Jerry_Business_Pulse", "type": "info"},
        {"item": "quel domaine B2 porte la version payante?", "type": "question"}]}
     ```
  3. **organize** : repartit les decisions par type. Ecrit
     `03_Organize_Rutherford/organize.json` :
     ```json
     {"stage": "organize",
      "prochaines_actions": ["ecrire la page Plan du coach-os-app"],
      "references": ["pattern verifier V3 mesure dans 00_Jerry_Business_Pulse"],
      "questions": ["quel domaine B2 porte la version payante?"]}
     ```
  4. **review** : compte. `date_revu` = `datetime.now().strftime("%Y-%m-%d")`
     (date seule). Ecrit `04_Review_Tendi/review.json` :
     ```json
     {"stage": "review", "date_revu": "<AAAA-MM-JJ du tir>",
      "total_captures": 3, "actions": 1, "references": 1, "questions": 1}
     ```
  5. **engage** : engage la premiere action. Ecrit
     `05_Engage_Freeman/engage.json` :
     ```json
     {"stage": "engage",
      "action_engagee": "ecrire la page Plan du coach-os-app",
      "statut": "pret"}
     ```
     (`action_engagee: null` et `statut: "vide"` si aucune action ; champ
     `action_engagee` toujours present).
- `apply_gtd.py` n'accede a AUCUN fichier en dehors de `gtd/` (ni lecture ni
  ecriture). Il ne lit pas `20_Life_OS/` - le canon 5 stages est cite dans
  `gtd.json`, pas importe.
- Idempotence : relancer le script le meme jour calendaire reecrit les 6
  fichiers JSON a l'identique octet pour octet (meme valeurs, meme ordre de
  cles, meme indent). Aucun dossier n'est supprime, aucun fichier existant
  hors `gtd/` n'est touche.
- Succes : affiche `GTDLOOP_APPLY_OK` + une ligne `stage OK: <stage>` par
  stage tourne, rc=0.

### 3.4 verifier.py - criteres [1]-[6]

- Meme entete (shebang, coding ascii, docstring francais ASCII citant la
  spec). Stdlib uniquement : `sys`, `os`, `json`, `subprocess`.
- Racine de la boucle : `os.path.dirname(os.path.abspath(__file__))`.
- Criteres numerotes, chacun imprime une ligne `OK: [n] <resume>` des qu'il
  passe, et une ligne `  ERREUR: <detail>` par echec accumule :
  - `[1]` `gtd/gtd.json` present, JSON valide via `json.load`, ET lisible par
    `subprocess.run([sys.executable, "-m", "json.tool", <chemin>])` rc=0
    (DoD du tape 35) ; champs : `version == "v1"`, `date_init == "2026-09-04"`,
    `framework == "GTD Cerritos"`, `verse == "Summers Verse"`,
    `projet == "coach-os-app"`, `stages == ["capture", "clarify", "organize",
    "review", "engage"]`, `source_tape` == chemin de cette spec, `source_pulse`
    == `20_Life_OS/25_GTD_Cerritos/pulse.json`.
  - `[2]` `apply_gtd.py` present, non vide, premiere ligne shebang
    `#!/usr/bin/env python3`, deuxieme ligne coding ascii.
  - `[3]` `01_Capture_Mariner/inbox.md` present, non vide, contient le titre
    `# Inbox - Mariner (Capture)` et une section `## Items` avec au moins
    1 ligne item `- [ ] `.
  - `[4]` `subprocess.run([sys.executable, "apply_gtd.py"])` : rc=0 et stdout
    contient `GTDLOOP_APPLY_OK`.
  - `[5]` apres le tir de `[4]`, les 5 dossiers de stage existent et leurs
    JSON sont valides avec les valeurs exactes attendues (deterministes via
    l'inbox de la section 3.2) :
    - `capture.json` : 3 items, premier == `ACTION: ecrire la page Plan du
      coach-os-app` ;
    - `clarify.json` : 3 decisions, types dans l'ordre
      `["action", "info", "question"]` ;
    - `organize.json` : `prochaines_actions == ["ecrire la page Plan du
      coach-os-app"]`, `references` de longueur 1, `questions` de longueur 1 ;
    - `review.json` : `total_captures == 3`, `actions == 1`,
      `references == 1`, `questions == 1`, `date_revu` au format
      `AAAA-MM-JJ` (parse par `datetime.strptime`) ;
    - `engage.json` : `action_engagee == "ecrire la page Plan du
      coach-os-app"`, `statut == "pret"`.
  - `[6]` idempotence : relance `apply_gtd.py` une seconde fois (rc=0), puis
    compare les 6 JSON (`capture`, `clarify`, `organize`, `review`, `engage`
    + `gtd.json` non modifie) octet pour octet entre les deux tirs - tous
    identiques (meme jour calendaire, `date_revu` compris).
- Ne modifie rien : il ne fait que lire, executer `apply_gtd.py` et comparer.
- Sortie finale : `GTDLOOP_OK` + rc=0 si les 6 criteres passent ; sinon
  `GTDLOOP_KO` + rc=1 (meme style que `verify_gtd.py` du pulse Cerritos,
  mesure : lignes 131-138 - bloc erreurs puis statut final).

### 3.5 Ordre d'execution

1. Ecrire `gtd/gtd.json` et `gtd/01_Capture_Mariner/inbox.md` (sections 3.1
   et 3.2, verbatim).
2. Ecrire `gtd/apply_gtd.py` (section 3.3).
3. Ecrire `gtd/verifier.py` (section 3.4).
4. Executer le verifier (section 4). Aucune autre modification autorisee :
   rien hors `gtd/`, rien d'existant.

## 4. Verification (commande + sortie attendue)

```
python C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd/verifier.py
```

Sortie attendue : 6 lignes `OK: [n] ...`, puis `GTDLOOP_OK`, rc=0.
Contre-epreuve (environnement) : `echo $?` -> `0`.
DoD du tape 35 re-covers : `python -m json.tool gtd.json` rc=0 (critere [1]),
verifier rc=0 imprimant au moins 1 critere OK (criteres [1]-[6]).
En cas d'echec : `GTDLOOP_KO`, rc=1, une ligne `  ERREUR: <detail>` par
critere en echec, aucun fichier modifie par le verifier lui-meme.

## 5. Prediction a pre-enregistrer (avant execution)

Texte : "Le 2026-09-04, apres ecriture des 4 fichiers de `gtd/`,
`python verifier.py` dans
`30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd/` affiche
`GTDLOOP_OK` avec rc=0 au premier tir, les 6 criteres `[1]`-`[6]` passent
dont le critere [6] d'idempotence (deux tirs d'`apply_gtd.py` a fichiers
identiques octet pour octet), et `python -m json.tool gtd.json` retourne
rc=0. La contre-epreuve (renommer temporairement `apply_gtd.py` puis
relancer) affiche `GTDLOOP_KO` avec rc=1 au critere [4]."

Seuil : les deux sorts doivent passer tels quels. Un seul tir de correction
autorise si KO ; au-dela, retour a la file (`kernel/uc.db`), 3 echecs ->
Donna (`10_Tech_OS/kernel/dlq.py`) -> Rick.
L'enregistrement de la prediction dans uc.db (loi de prediction, schema.sql)
se fait par le constructeur AVANT la premiere evidence, via les commandes
kernel existantes ; le constructeur ne modifie ni `schema.sql` ni aucun
fichier du kernel.

## 6. Contraintes

- Python stdlib uniquement (aucun pip install, aucune dependance externe).
- Francais ASCII sans accents dans tout code, commentaire et contenu genere
  (l'inbox graine de la section 3.2 est sans accent).
- Fichiers NOUVEAUX uniquement, tous dans
  `30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd/`. Liste exacte
  des fichiers existants INTOUCHABLES de `00_Summers_Verse/` (mesure du
  listing du 2026-09-04) : `registre_solaris.json`,
  `registre_solaris_12wy.json`, `verifier.py`, `verifier_solaris.py`,
  `verifier_solaris_12wy.py`, `00_Registre/registre.json`,
  `projects/coach-os-app/README.md`, et tout fichier cree a l'avenir hors
  `projects/coach-os-app/gtd/`.
- Ne pas toucher `10_Tech_OS/` (kernel `uc.db` compris - seules les commandes
  `gate.py` / `review.py` / prediction y sont executees, jamais ecrites),
  `20_Life_OS/` (`25_GTD_Cerritos/` sert de modele lu, jamais modifie), ni
  aucun autre framework - passer par son portier.
- Pyramide L0 >= L1 > L2 : Beth a le veto, respecter
  `30_Business_OS/AGENTS.md` ; ce ruban L2 n'ecrit ni dans
  `00_Amadeus/40_Predictions/` ni dans `00_Amadeus/60_Tape_Specs/` hors ce
  fichier lui-meme.
- Idempotence : `apply_gtd.py` et `verifier.py` sont relanceables, meme
  resultat a chaque tir (meme jour calendaire) ; aucun fichier existant hors
  `gtd/` n'est modifie par aucun des deux.
- Rollback : supprimer le dossier
  `30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd/` entier
  (uniquement des fichiers nouveaux, rien d'existant n'est modifie).
  Commande : `rm -rf C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Summers_Verse/projects/coach-os-app/gtd`.
- Append-only D4 : ce fichier est une tape NOUVELLE de `60_Tape_Specs/` ;
  aucune tape existante n'est reecrite (le tape 35 FROZEN reste tel quel,
  ce fichier en est le raffinement pointe par `work: 43`).
- Test du ruban (critere binaire, `AGENTS.md` racine §3) : aucun constructeur
  n'a besoin de poser une question - chemin exact, contenu verbatim, regles
  de classification, valeurs attendues, commande de verification, seuil de
  prediction et rollback sont tous fixes dans ce fichier.
