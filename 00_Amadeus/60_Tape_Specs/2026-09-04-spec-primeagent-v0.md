---
id: spec-primeagent-v0
date: 2026-09-04
layer: L2
owner: doctor12_l2
status: active
type: ruban-phi
os: 30_Business_OS
target: 30_Business_OS/02_Meta_Factory/primeagent/
---

# SPEC PrimeAgent v0 - prototype d'agents franchises

> Ruban phi. Test du ruban : GO permanent, aucune question a l'operateur.
> Chemin : `C:/Users/amado/ASpace_OS_V3/00_Amadeus/60_Tape_Specs/2026-09-04-spec-primeagent-v0.md`
> Pattern V3 mesure (lecture directe) : `30_Business_OS/00_Jerry_Business_Pulse/verifier.py`
> (python stdlib uniquement, francais ASCII sans accents, sortie OK/KO, rc 0/1)
> et `30_Business_OS/00_Jerry_Business_Pulse/01_Prime/pulse.json` (JSON plat,
> indent=2, encodage UTF-8). Base : `30_Business_OS/02_Meta_Factory/primeagent/README.md`
> existe (role, entree, sortie, invariant : le prototype derive du modele source,
> jamais l'inverse).

## 1. Objectif

Creer le premier prototype d'agents franchises dans `02_Meta_Factory/primeagent/` :
un generateur CLI (`agent-template.py`) qui construit l'arborescence complete
d'une franchise a partir d'un nom, sur les 8 domaines B2 (Growth / Sales /
Product / Ops / IT / Finance / People / Legal, SDD-006), et un verifier
(`verifier.py`) qui teste la generation dans un tmpdir et affiche
`PRIMEAGENT_OK` (rc=0) ou `PRIMEAGENT_KO` (rc=1).

## 2. Livrables (chemins exacts)

```
30_Business_OS/02_Meta_Factory/primeagent/
├── README.md            (EXISTANT, non modifie)
├── agent-template.py    (NOUVEAU - generateur CLI)
└── verifier.py          (NOUVEAU - verificateur)
```

## 3. Etapes executable

### 3.1 agent-template.py - comportement exact

- Shebang `#!/usr/bin/env python3`, coding `# -*- coding: ascii -*-`,
  docstring en francais ASCII annoncant le role, la spec (ce chemin), et
  l'usage.
- CLI : `python agent-template.py <nom_franchise> <repertoire_cible>`
  - `<nom_franchise>` : chaine non vide, sans separateur de chemin.
  - `<repertoire_cible>` : dossier de sortie (cree si absent).
  - Sans les 2 arguments ou `-h/--help` : affiche l'usage sur stdout et
    retourne rc=2 (usage incorrect, distinct de l'echec rc=1).
- Genere dans `<repertoire_cible>/<slug>/` ou `<slug>` = nom en minuscules,
  espaces remplaces par tirets :
  - `README.md` : titre `# <nom_franchise>`, ligne `statut: v0-initialise`,
    date de creation ISO (AAAAMMJJ, derivee de `datetime.now()`), section par
    domaine.
  - Un dossier par domaine, dans cet ordre exact :
    `01_Growth`, `02_Sales`, `03_Product`, `04_Ops`, `05_IT`,
    `06_Finance`, `07_People`, `08_Legal`.
  - Dans chaque dossier de domaine : `README.md` non vide portant le titre
    `# <nom_franchise> - <Domaine>` (ex. `# Ma Franchise - Growth`).
  - `franchise.json` a la racine du slug :
    ```json
    {
      "nom": "<nom_franchise>",
      "slug": "<slug>",
      "domaines": ["growth", "sales", "product", "ops", "it",
                    "finance", "people", "legal"],
      "cree": "<AAAA-MM-JJ>",
      "statut": "v0-initialise"
    }
    ```
    ecrit avec `json.dump(..., indent=2)` + saut de ligne final, encodage UTF-8.
- Idempotence : si le dossier `<slug>` existe deja, le script echoue proprement
  (message sur stderr, rc=1) et ne modifie rien - l'invariant du README
  (derive du modele, jamais l'inverse) interdit d'ecraser une franchise existante.
- Succes : message une ligne sur stdout (`franchise generee: <slug>`), rc=0.
- Stdlib uniquement : `sys`, `os`, `json`, `re` (eventuel), `datetime`.
- Aucun accent dans le code, les commentaires, les contenus generes.

### 3.2 verifier.py - comportement exact

- Meme entete (shebang, coding ascii, docstring francais ASCII citant la spec).
- Stdlib uniquement : `sys`, `os`, `json`, `tempfile`, `shutil`, `subprocess`.
- Sequences de test, toutes dans un `tempfile.mkdtemp()` nettoyé avec
  `shutil.rmtree(..., ignore_errors=True)` dans un bloc `finally` :
  1. Localise `agent-template.py` a cote de lui (`os.path.dirname(__file__)`),
     echec s'il est absent.
  2. Genere une franchise `Franchise Test` via `subprocess.run([sys.executable,
     "agent-template.py", "Franchise Test", tmpdir])` : rc attendu 0.
  3. Verifie l'arborescence : dossier `franchise-test/` present, les 8 dossiers
     de domaine dans l'ordre, `franchise.json` present et JSON valide (nom ==
     "Franchise Test", slug == "franchise-test", 8 domaines dans l'ordre,
     statut == "v0-initialise", `cree` non vide), README racine du slug non
     vide avec titre et `statut: v0-initialise`, README de chaque domaine non
     vide avec titre `# Franchise Test - <Domaine>`.
  4. Test d'echec propre : re-invoque le generateur sur le meme tmpdir ; rc
     attendu != 0 (idempotence protectrice), et le `franchise.json` existant
     doit rester identique (relit et compare).
  5. Test usage : invocation sans argument, rc attendu 2.
- Sortie : `PRIMEAGENT_OK` + rc=0 si tout passe ; sinon `PRIMEAGENT_KO` + une
  ligne `  ERREUR: <detail>` par echec + rc=1. Meme style que le verifier du
  pulse B1 (mesure : `00_Jerry_Business_Pulse/verifier.py`, lignes 226-233).

### 3.3 Ordre d'execution

1. Ecrire `agent-template.py`.
2. Ecrire `verifier.py`.
3. Executer le verifier (section 4). Aucune autre modification autorisee dans
   `primeagent/` (README.md existant untouched).

## 4. Verification (commande + sortie attendue)

```
python C:/Users/amado/ASpace_OS_V3/30_Business_OS/02_Meta_Factory/primeagent/verifier.py
```

Sortie attendue : `PRIMEAGENT_OK` sur stdout, rc=0.
Contre-epreuve (environnent) : `echo $?` → `0`.
En cas d'echec : `PRIMEAGENT_KO`, rc=1, erreurs detaillees ligne par ligne.

## 5. Prediction a pre-enregistrer (avant execution)

Texte : "Le 2026-09-04, apres ecriture des deux scripts, `python
verifier.py` dans `30_Business_OS/02_Meta_Factory/primeagent/` affiche
`PRIMEAGENT_OK` avec rc=0 au premier tir, et la contre-epreuve d'echec
(renommer temporairement `agent-template.py` puis relancer) affiche
`PRIMEAGENT_KO` avec rc=1."

Seuil : les deux sorts doivent passer tels quels. Un seul tir de correction
autorise si KO ; au-dela, retour a la file (`kernel/uc.db`), 3 echecs → Donna.

## 6. Contraintes

- Python stdlib uniquement (aucun pip install, aucune dependance externe).
- Francais ASCII sans accents dans tout code, commentaire et contenu genere.
- Artefact executable + verifier a sortie OK/KO et rc 0/1 (pattern V3 du
  pulse B1, mesure le 2026-09-03).
- `README.md` existant de `primeagent/` non modifie (append-only D4 sur le
  reste du dossier).
- Invariant du modele source : le generateur ne cree aucune capacite non
  declaree dans son modele (8 domaines B2 fixes, aucune option cachee).
- Pyramide L0 >= L1 > L2 : ce ruban L2 ne touche ni `10_Tech_OS/kernel/` ni
  `00_Amadeus/40_Predictions/` (l'enregistrement de la prediction se fait par
  l'operateur ou le controleur C, pas par le constructeur).
- Rollback : supprimer `agent-template.py` et `verifier.py` (deux fichiers
  nouveaux, rien d'existant n'est modifie).
