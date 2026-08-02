# A'Space OS V3

> **Loi L0 — Rick.** *Un système qui ne sait pas se répliquer n'est pas un système,
> c'est un document.* Von Neumann : ruban + constructeur + copieur + contrôleur.
> Conway : trois règles suffisent, la complexité émerge, jamais déclarée.

V3 n'est pas une copie de V2. **V2 est la mémoire, V3 est le runtime.**

---

## État au 2026-08-02

**84 dossiers, 50 fichiers réels.** Tout ce qui existe ici sert au fonctionnement.

Les 17 665 fichiers de l'ancienne structuration sont archivés, intacts et réversibles, dans
`ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\_V3_STRUCTURE_2026-08-02\`
(manifeste de 471 entrées).

Les 1 576 dossiers vides qui reproduisaient l'imbrication V2 ont été supprimés le 2026-08-02 :
un dossier vide n'est pas une structure, c'est une règle en plus qui fige la capacité sans
rien produire. La structure d'origine reste lisible dans l'archive.

## Arborescence

| Chemin | Contenu |
|---|---|
| `_INBOX/` | admission — portiers `S1_Rick`, `A1_Beth_Morty`, `B1_Jerry_Summer` |
| `00_Amadeus/` | A0 — Observateur Méta : observateurs, harness, shadow, prédictions, bench, rubans, skills, doctrine |
| `10_Tech_OS/00_Governance_Rick/` | la loi et le **réplicateur** — gabarit de Core + `spawn.py` |
| `10_Tech_OS/kernel/` | les organes : `uc.py`, `harness.py`, `gate.py`, `review.py`, `dlq.py` |
| `10_Tech_OS/11_Kernel_Core_13th/` | 13e Docteur — maître de `10_Tech_OS` *(engendré)* |
| `10_Tech_OS/12_Life_Core_11th/` | 11e Docteur — maître de `20_Life_OS` *(engendré)* |
| `10_Tech_OS/13_Buzz_Core_12th/` | 12e Docteur — maître de `30_Business_OS` *(engendré)* |
| `20_Life_OS/` · `30_Business_OS/` | les couches maîtrisées — le travail y atterrit, pas les Cores |
| `scripts/` · `AGENTS.md` · `LICENSE` · `.gitignore` · `README.md` | amorçage et identité |

**Rien ne se crée à la racine.** Tout fichier qui n'appartient ni à Tech, ni à Life, ni à
Business va dans `00_Amadeus/`.

## Les quatre organes

| Organe | Où | Fait quoi |
|---|---|---|
| Ruban φ | `00_Amadeus/60_Tape_Specs/` | la description — `/spec-loop`, `/bmad` |
| Constructeur A | `10/20/30_*_OS/` | bâtit depuis le ruban |
| Copieur B | `00_Governance_Rick/replicator/` | duplique sans interpréter — engendre les Cores |
| Contrôleur C | `_INBOX/` + `kernel/uc.db` | ordonne, puis **détache** |

## Le cycle, de bout en bout

```bash
python 10_Tech_OS/kernel/gate.py run        # le portier admet ou refuse
python 10_Tech_OS/kernel/worker_example.py --harness cc --layer L2 --max 1
python 10_Tech_OS/kernel/review.py run      # exige les preuves, score, détache
python 10_Tech_OS/kernel/dlq.py rapport     # ce qui attend Rick
```

## Hiérarchie

`ORG.json` fait foi. S1 Rick gouverne le mécanisme et ne réclame jamais de travail.
S2 les trois Docteurs maîtrisent une couche et **détachent**. S3 les neuf compagnons
exécutent — Spec, Build, Spawn. Donna reçoit les échecs répétés et escalade à Rick.

Harness : Multica (L0) · Buzz (L1) · Paperclip (L2). Contrat commun :
`00_Amadeus/20_Harness/ADAPTER.md`.

## La mémoire est dans V2

```
ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\
```

Point d'entrée `03_Resources_Geordi/CLAUDE.md`. Les 4 piliers : **OKF** · **Wiki** ·
**Graphify** · **Dox**. Un fichier qui n'exécute rien et contre lequel rien ne s'exécute
appartient à Geordi, pas ici.

## ⚠ Secrets publiés

Ce dépôt a un remote GitHub et son historique contient au moins 11 fichiers porteurs de
credentials, poussés via le commit `41c19a5`. **Faire tourner ces clés** est prioritaire sur
toute réécriture d'historique — celle-ci ne révoque rien.

Licence : **MIT**.
