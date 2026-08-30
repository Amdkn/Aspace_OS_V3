---
okf_version: "0.1"
type: brief-delegation
title: BRIEF M3 — Distillation des guides YouTube en 8 domaines Business
description: Brief de délégation à MiniMax-M3. Distille le corpus de guides YouTube épars de Geordi en 8 distillations de domaine, déposées dans LD01_Business_Book/01_Guides_Business/.
timestamp: 2026-08-02T13:45:00-04:00
domain: LD01_Career_Business
agent: A3_Book
executor: MiniMax-M3[1m]
---

# BRIEF — Distillation 8 domaines · guides YouTube Geordi → LD01 Book

Tu es l'exécutant délégué. Ce fichier est ton seul ordre de mission. Tu ne demandes rien :
tu mesures, tu écris, tu rends compte.

---

## 1. Faits déjà mesurés — ne les recompte pas

Corpus source : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\`

Comptes `.md` récursifs relevés le 2026-08-02 (hors `_TRASH_*` et `_SKIP_*`) :

| Dossier legacy | `.md` | Domaine cible |
|---|---:|---|
| *(racine de `01_Guides`)* | 426 | à classer par contenu |
| `00_KERNEL_OS` | 199 | 1 · RH & Méta Gouvernance |
| `01_Product` + `01_Product_Product` | 900 | 3 · Productization des Besoins |
| `02_Ops` + `02_Ops_Ops` | 287 | 2 · Opérations en Loops |
| `03_IT` | 10 524 | 7 · R&D & IT |
| `03_IT_IT` | 123 | 7 · R&D & IT |
| `04_Finance` + `04_Finance_Finance` | 370 | 6 · Finance & ROI |
| `05_Legal` + `08_Legal` + `08_Legal_Legal` | 63 | 8 · Legal & Compliance |
| `05_People` + `05_People_People` + `08_People` | 253 | 1 · RH & Méta Gouvernance |
| `06_Sales` + `06_Sales_Sales` | 118 | 4 · Sales & Cognition |
| `07_Growth` + `07_Growth_Growth` | 555 | 5 · People & Brand |
| `09_Life_OS` + `09_Life_OS_Life_OS` | 1 607 | à classer — **ne retenir que business ou IA** |
| `_DRAFTS_PPR_LANE` | 107 | à classer par contenu |

**Total ordre de grandeur : ~15 500 fichiers.** À la racine de `01_Guides` : 35 `Geordi_YT-*.md`
et 2 `Geordi_Guide_Premium_Batch_*.md`.

Le doublonnage `01_Product` / `01_Product_Product` est un artefact d'une reclassification
antérieure. Traite les deux comme un seul domaine, et **signale les doublons de contenu**
plutôt que de les fusionner toi-même.

## 2. Les 8 domaines — nomenclature arrêtée par A0 le 2026-08-02

Cette liste fait foi. Elle ne se renomme pas, ne se réordonne pas, ne s'augmente pas.

| # | Domaine | VP (DC) | Squad technicienne (Marvel) |
|---|---|---|---|
| 1 | **RH & Méta Gouvernance** | Green Lantern | X-Men |
| 2 | **Opérations en Loops** | Batman | Fantastic Four |
| 3 | **Productization des Besoins** | Flash | Avengers |
| 4 | **Sales & Cognition** | Martian Manhunter | Illuminati |
| 5 | **People & Brand** | Superman | Guardians |
| 6 | **Finance & ROI** | Wonder Woman | Thunderbolts |
| 7 | **R&D & IT** | Cyborg | Kang Dynasty |
| 8 | **Legal & Compliance** | Aquaman | Eternals |

Canon de rattachement : `ADR-CANON-001` (8 B2 + 8 squads + 53 B3).
Le domaine 7 R&D & IT **porte le pipeline de veille** (`/youtube-to-guide` → Last30days),
c'est donc lui qui hérite du plus gros volume : c'est normal, pas une anomalie de classement.

## 3. Périmètre exact

**Retenir** : tout guide dont le sujet est le **business** ou l'**IA / les agents / le harness
engineering**.

**Écarter** : ce qui est purement personnel (santé, famille, spiritualité) sans angle business
ni IA. Ces fichiers ne se suppriment pas — ils vont dans une ligne `hors_perimetre` du manifeste.

## 4. Livrables — et rien d'autre

Tout est déposé dans :
`C:\Users\amado\ASpace_OS_V3\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\01_Guides_Business\`

### 4.1 — Passe 1 : l'index mécanique (aucune lecture LLM)

`_INDEX_GUIDES.tsv` — une ligne par fichier, colonnes exactement dans cet ordre :

```
chemin_relatif	titre	domaine	confiance	signal	octets	mtime
```

- `domaine` : entier 1-8, ou `0` si hors périmètre.
- `confiance` : `haute` (le dossier legacy donne le domaine) · `moyenne` (titre explicite) ·
  `basse` (deviné).
- `signal` : le mot ou la locution du titre/frontmatter qui a décidé du classement. Vide interdit.

Cette passe est **scriptée en Python**, pas lue fichier par fichier par toi. Un script qui lit
le nom, le frontmatter YAML et les 40 premières lignes suffit. Il doit tourner en une fois sur
les ~15 500 fichiers.

### 4.2 — Passe 2 : les 8 distillations

Un fichier par domaine, nommé `0N_<Domaine_Snake>.md` — donc exactement :

```
01_RH_Meta_Gouvernance.md
02_Operations_en_Loops.md
03_Productization_des_Besoins.md
04_Sales_et_Cognition.md
05_People_et_Brand.md
06_Finance_et_ROI.md
07_RD_et_IT.md
08_Legal_et_Compliance.md
```

Chacun porte un frontmatter OKF v0.1 (`okf_version`, `type: guide-distillation`, `title`,
`description`, `timestamp`, `domain: LD01_Career_Business`, `agent: A3_Book`) puis, dans cet
ordre :

1. **Ce que le corpus dit** — 5 à 12 thèses, chacune adossée à ≥2 guides cités par chemin.
   Une thèse sans deux sources est une opinion : elle ne rentre pas.
2. **Ce qui est actionnable maintenant** — cases à cocher `- [ ]`, chacune vérifiable
   (un nombre, un fichier, une commande). Pas de « améliorer X ».
3. **Ce que le corpus contredit** — les désaccords entre guides. Ne les arbitre pas : expose-les.
4. **Les 10 guides de tête** — tableau `chemin · titre · pourquoi celui-ci`.
5. **Angles morts** — ce que le domaine ne couvre pas et qui manque.

Taille visée : 150 à 400 lignes. Un fichier de 40 lignes est un échec ; un de 1 500 est un dump.

### 4.3 — Le manifeste

`_MANIFEST_DISTILLATION.json` :

```json
{
  "date": "2026-08-02",
  "executeur": "MiniMax-M3[1m]",
  "fichiers_indexes": 0,
  "par_domaine": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0},
  "hors_perimetre": 0,
  "confiance": {"haute": 0, "moyenne": 0, "basse": 0},
  "doublons_suspects": [],
  "distillations_ecrites": [],
  "non_traite": []
}
```

## 5. Interdits

- **Ne rien déplacer, ne rien supprimer, ne rien renommer** dans `03_Resources_Geordi/`.
  Le corpus source est en lecture seule. Tu produis à côté, tu ne touches pas à l'original.
- **Ne rien écrire à la racine** de `C:\Users\amado` ni de `ASpace_OS_V3`.
  Les fichiers de travail vont dans `%TEMP%`.
- **Ne pas suivre les jonctions NTFS.** 47 recensées sur ce disque. `os.path.islink()` ne les
  voit pas. Un `os.walk` naïf a déjà compté 13,8 millions de fichiers là où il y en avait 14 613.
  Détection obligatoire :

  ```python
  RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
  bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
  ```

- **Ne pas inventer de source.** Un chemin cité dans une distillation doit exister. Si tu ne
  peux pas citer, tu n'affirmes pas.
- **Ne pas réécrire** `00_index.md`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `A3_Book_LD01_Spec.md`,
  `BIBLIOGRAPHY.md`. Posture additive stricte : tu ajoutes des fichiers, tu n'en modifies aucun.
- **Ne pas toucher** aux 3 guides déjà présents dans `01_Guides_Business/`.
- Aucun secret dans les livrables — motifs `sk-`, `sbp_`, `vcp_`, `ghp_`, JWT, clés PEM.

## 6. Si tu t'arrêtes

Arrêt pour quelque raison que ce soit — budget, erreur, corpus plus gros que prévu :
tu écris `_RAPPORT_PARTIEL.md` dans le même dossier, avec

- ce qui est fait, chiffré ;
- ce qui ne l'est pas, nommé ;
- la cause de l'arrêt ;
- la commande exacte pour reprendre.

Un arrêt documenté vaut mieux qu'un livrable inventé. **Ne complète jamais un manque par une
supposition présentée comme un fait.**

## 7. Ordre d'exécution

1. Écris et lance le script d'index (passe 1). Vérifie que le total indexé est du bon ordre
   de grandeur (~15 500) — s'il est à 13 millions, tu as suivi une jonction : arrête et corrige.
2. Écris `_MANIFEST_DISTILLATION.json` avec les compteurs de la passe 1.
3. Distille domaine par domaine, **du plus petit au plus grand** (8, 4, 1, 2, 6, 5, 3, 7).
   Écris chaque fichier dès qu'il est fini — ne garde rien en mémoire pour la fin.
4. Mets le manifeste à jour après chaque distillation écrite.
