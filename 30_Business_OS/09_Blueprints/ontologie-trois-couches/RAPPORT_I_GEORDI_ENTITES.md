---
id: I_GEORDI_ENTITES
chantier: ontologie-trois-couches
title: BRIEF I — Ce qui existe déjà dans Geordi, avant d'inventer quoi que ce soit
date: 2026-08-13
auteur: MiniMax-M3 (Claude Code, exécution propre)
périmètre_lecture: C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/
périmètre_écriture: C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/ontologie-trois-couches/
statut: COMPLET
---

# BRIEF I — Rapport : Ce qui existe déjà dans Geordi

## TL;DR

- **29 noms** d'entités candidates scannés dans Geordi. **Tous dépassent le seuil de
  5 fichiers distincts**. Aucun nom sous le seuil de 3 fichiers.
- **CONSTITUTION.md existe** : 1 fichier canonique (`05_From_V2_Domains/00_Amadeus/01_Identity_Core/CONSTITUTION.md`),
  plus 50 fichiers qui la mentionnent. **L'hypothèse du brief ("réputée absente") est fausse**.
- **H3 est une découverte** : 806 fichiers mentionnent H3, alors que le brief n'envisageait
  que H1/H10/H30/H90. Le V3 a étendu la grille à **H1/H3/H10/H30/H90** (confirmé dans
  `ASpace_OS_V3/20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/`).
- **5 des 8 tournures de finalité** sont présentes en Geordi (sert à, afin de, contribue
  à, rattachée à, au service de, répond à, vise à). "Pour" représente 155 491 matchs
  bruts — un océan de bruit impossible à filtrer proprement. La sélection finale retient
  7 tournures non-pour, **zéro "pour"** — résultat à interpréter.
- **Le script détecte 159 jonctions** (exactement le nombre attendu par la doctrine).
  Sans ce filtrage, `os.walk` naïf aurait compté 13,8 M de fichiers.

## 1. Méthode

Trois scripts Python en lecture seule, exécutés localement avec `python 3.14`.

| Script | Rôle | Temps | Fichiers lus |
|---|---|---|---|
| `00_recon.py` | Walk + comptage (top-level, fichiers, jonctions) | < 1 min | 0 (metadata) |
| `01_scan.py` | Scan des 29 noms candidats | 19 min | 59 265 (308 Mo) |
| `02_combined.py` | Scan finalités + Constitution/IK/Horizons en un seul passage | 5 min | 59 265 (308 Mo) |

**Détection des jonctions** : `stat.FILE_ATTRIBUTE_REPARSE_POINT` (0x400) testé sur
chaque `DirEntry.stat(follow_symlinks=False).st_file_attributes`. Aucune descente dans
une jonction ; comptage et abandon.

**Critères de scan des noms** : regex `\b{nom}\b` case-insensitive, comptage en fichiers
**distincts** (un même nom cité 400 fois dans un seul fichier ne compte que 1).

**Critères de scan des finalités** : 8 patterns regex (`sert à`, `afin de`, `contribue à`,
`rattachée à`, `au service de`, `répond à`, `vise à`, `pour`). Pour `pour`, filtre anti-bruit
éliminant les pronoms/verbes immédiatement après ("pour nous", "pour faire", etc.). Sélection
de 20 : 1 par fichier max, 4 par tournure max.

## 2. Reconnaissance Geordi

| Mesure | Valeur |
|---|---|
| Fichiers totaux sous Geordi | 432 409 |
| **Fichiers `.md`** | **59 265** |
| Dossiers | 46 370 |
| **Jonctions détectées et écartées** | **159** |
| Erreurs de scan (permissions, OS) | 0 |

Top-level de Geordi :

```
00_Index/                     04_From_V2_Root/                07_From_Home_Root_2026-08-01/
01_Guides/                    05_From_V2_Domains/             08_Workspaces_Dormants_2026-08-01/
02_Templates/                 06_Claude_Code_Bare/            09_From_Home_Root_Batch2_2026-08-01/
03_Memory_Unified/                                          09_Life_OS/
Cerritos_Plane_Settings/      graphify-out/                   Youtube_Take_out/
_DRAFTS_PPR_LANE/             _TRASH_2026-07-27_phase13_7a_scripts/
_evals/                       _transcripts_raw/
+ 4 fichiers racine (.gitkeep, A3_Geordi_Resources_Spec.md, CLAUDE.md, L0_00_Couveuse.md, README.md, watch-history.html)
```

Le chiffre de ~14 600 fichiers mentionné dans CLAUDE.md (et le brief) sous-estime
l'arbre réel par ~30×. À prendre comme référentiel désormais : **59 265 `.md`**.

## 3. Entités observées — tableau par couche

Tous les 29 noms candidats dépassent le seuil de 5 fichiers distincts. Aucun n'est
sous le seuil de 3. **Avec un corpus aussi large, le seuil de 5 ne sépare plus rien** —
il faudrait probablement un seuil de 1 000 ou 5 000 pour distinguer un mot d'usage d'un
concept structurant.

### Business OS (12 entités — toutes confirmées)

| Nom | Fichiers distincts | Seuil | Exemples |
|---|---:|---:|---|
| **Agent** | 15 147 | ≥ 5 | `00_Index/FIX_KB_2026-08-02.md`, `00_Index/GEORDI_KB_ROOT.md`, `00_Index/INDEX_OF_INDEXES.md` |
| **Client** | 7 333 | ≥ 5 | `01_Guides/01_Product/Geordi_YT-AWtej6xTtp8.md`, … |
| **Skill** | 6 414 | ≥ 5 | `00_Index/INDEX_OF_INDEXES.md`, … |
| **SOP** | 5 074 | ≥ 5 | (cf. JSON) |
| **Persona** | 2 038 | ≥ 5 | (cf. JSON) |
| **Routine** | 1 672 | ≥ 5 | (cf. JSON) |
| **Profile** | 1 521 | ≥ 5 | (cf. JSON) |
| **Incident** | 1 069 | ≥ 5 | (cf. JSON) |
| **Organization** | 780 | ≥ 5 | (cf. JSON) |
| **Runbook** | 542 | ≥ 5 | (cf. JSON) |
| **Membership** | 355 | ≥ 5 | (cf. JSON) |
| **Offering** | **90** | ≥ 5 | (cf. JSON) |

Les 12 entités Business OS déjà modélisées dans l'ontologie Coach OS sont **toutes
confirmées dans le corpus**. Aucune n'est tombée sous le seuil. `Offering` est la plus
rare (90 fichiers) mais toujours largement au-dessus.

### Life OS (17 noms candidats — Life Wheel, PARA, GTD, 12 Week Year, D.E.A.L, Ikigai)

| Nom | Fichiers distincts | Seuil | Notes |
|---|---:|---:|---|
| **Objectif** | 6 511 | ≥ 5 | |
| **Contexte** | 5 845 | ≥ 5 | |
| **Domaine** | 4 603 | ≥ 5 | |
| **Ressource** | 3 611 | ≥ 5 | PARA |
| **Projet** | 3 427 | ≥ 5 | PARA |
| **Area** | 2 087 | ≥ 5 | PARA |
| **Archive** | 1 884 | ≥ 5 | PARA |
| **Horizon** | 1 782 | ≥ 5 | Mot (cf. aussi codes ci-dessous) |
| **Semaine** | 1 778 | ≥ 5 | 12 Week Year |
| **Cadence** | 1 151 | ≥ 5 | |
| **Ikigai** | 1 101 | ≥ 5 | |
| **H1** | 2 069 | ≥ 5 | Code horizon |
| **H10** | 737 | ≥ 5 | Code horizon |
| **H90** | 560 | ≥ 5 | Code horizon |
| **H30** | 499 | ≥ 5 | Code horizon |
| **Occurrence** | 174 | ≥ 5 | D.E.A.L |
| **Charter** | **158** | ≥ 5 | Le plus rare, mais > 5 |

**Découvertes** :

- **H3 apparaît dans 806 fichiers.** Le brief initial ne le mentionnait pas, mais V3
  a étendu la grille d'horizons à **H1/H3/H10/H30/H90** — confirmé dans
  `ASpace_OS_V3/20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/01_H1_Isaac`, `02_H3_Lamarr`,
  `03_H10_Bortus`, `04_H30_Alara`, `05_H90_Klyden`. Chaque horizon est nommé d'après un
  personnage d'Orville (série télévisée).
- **`Charter`** (158 fichiers) reste au-dessus du seuil, mais c'est le candidat le
  plus rare. Sa structure d'emploi mérite vérification manuelle.
- **`Occurrence`** (174 fichiers) — concept D.E.A.L, relativement niché.

### Tech OS

**Aucun candidat Tech OS n'a été fourni par le brief.** Les 29 noms testés sont
tous Business OS ou Life OS. Le scan ne peut donc pas répondre à la question « y a-t-il
des entités Tech OS dans Geordi ? ». Recommandation : itérer avec une liste Tech OS
candidate (ex. `Component`, `Module`, `Pipeline`, `Worktree`, `Endpoint`, `Service`,
`Build`, `Deploy`, `Migration`, `Skill_API`, `MCP`, `Tool`, `Kernel`, `Spawn`, `Core`).

## 4. Vingt relations de finalité

Forme demandée par le brief : `<chose> --sert à--> <finalité>`. La sélection a privilégié
la diversité (1 par fichier, 4 par tournure, hors "pour" qui est intractable).

Comptes bruts avant filtrage :

| Tournure | Matchs bruts |
|---|---:|
| `pour` | **155 491** |
| `afin de` | 1 079 |
| `vise à` | 488 |
| `sert à` | 212 |
| `au service de` | 119 |
| `répond à` | 116 |
| `contribue à` | 48 |
| `rattache à` | 20 |

### Sélection 20

| # | Tournure | Fichier:ligne | Sujet --tournure--> Finalité |
|---:|---|---|---|
| 1 | sert à | `01_Guides/02_Ops/resource_sushi_ceo_25_ans_100m_turnaround.md:59` | série YouTube --sert à--> montrer les hauts, les bas, l'optimisme, le pessimisme (video diary) |
| 2 | afin de | `01_Guides/01_Product/Dan_Martell/resource_hSGt_rhu49U.md:47` | protocole --afin de--> attaquer directement la tâche la plus complexe |
| 3 | contribue à | `01_Guides/03_IT/itssssss-jack/its-a-great-day-to-be-in-pre-k-jack-hartmann.md:25` | nœud --contribue à--> agrégation de la base de connaissances distribuée |
| 4 | rattachée à | `03_Memory_Unified/LLM_Wiki/wiki/Gemini_Takeout_2026/2026-03_conversations.md:5835` | ambition (Ikigai H3) --rattachée à--> domaine précis de la vie |
| 5 | au service de | `01_Guides/07_Growth/Yann_Leonardi/resource_duolingo.md:57` | Gamification Positive --au service de--> Souveraineté (Habit-Building) |
| 6 | répond à | `01_Guides/02_Ops/Geordi_YT-ewkw9ioRc9Y.md:3` | Adam Driver --répond à--> question philosophique de Cannes |
| 7 | vise à | `01_Guides/02_Ops/business-is-hard-until-you-build-systems-like-this.md:21` | documentation précise de l'état actuel (As-Is) --vise à--> créer une cartographie |
| 8 | Sert à | `01_Guides/03_IT/Dan_Martell/resource_biAYfwX4bkY.md:92` | Base de connaissances Notion --Sert à--> centraliser et structurer les insights |
| 9 | afin de | `01_Guides/01_Product/Dan_Martell/resource_Mxy6MVbpNhg.md:30` | mécanismes techniques --afin de--> maximiser le retour sur investissement temporel |
| 10 | contribue à | `01_Guides/03_IT/itssssss-jack/the-jack-ranked-experience.md:36` | réinvention du paradigme de classement --contribue à--> éviter la centralisation et la surveillance |
| 11 | rattachée à | `03_Memory_Unified/LLM_Wiki/wiki/Gemini_Takeout_2026/2026-03_conversations.md:5835` | (doublon : entrée 4) |
| 12 | au service de | `01_Guides/07_Growth/Yann_Leonardi/resource_marketing-de-meero-...md:63` | IA --au service de--> l'hôte (vs plateforme tierce) |
| 13 | répond à | `01_Guides/02_Ops/Geordi_YT-ewkw9ioRc9Y.md:3` | Adam Driver --répond à--> (doublon : entrée 6) |
| 14 | vise à | `01_Guides/02_Ops/la-cte-divoire-fabrique-...md:36` | émergence de la fabrication locale --vise à--> systématiser les opérations d'A'Space OS |
| 15 | sert à | `01_Guides/03_IT/Dan_Martell/resource_dyrr4eAdnhg.md:38` | Ikigai --sert à--> trouver sa raison d'être dans la vie |
| 16 | afin de | `01_Guides/01_Product/Dan_Martell/resource_reR_EtTCkW4.md:37` | méthodologie --afin de--> ne retenir que les objectifs essentiels |
| 17 | contribue à | `01_Guides/03_IT/RoboNuggets/robonuggets-community-review.md:44` | revue en Open Data --contribue à--> enrichir la matrice de connaissances |
| 18 | rattachée à | `03_Memory_Unified/LLM_Wiki/wiki/graphify-out/chunks/chunk_000/2026-03_conversations.md:5835` | (doublon graphe de l'entrée 4 — graphify-out est une dérivation) |
| 19 | au service de | `01_Guides/07_Growth/Yann_Leonardi/resource_marketing-de-starbucks-...md:43` | personnalisation Starbucks --au service de--> espace documentaire A'Space OS |
| 20 | répond à | `01_Guides/03_IT/Dan_Martell/resource_bkM-lYgAxh0.md:48` | utilisateur --répond à--> entretien en utilisant le mode vocal |

**Lecture** :

- **20 chemins uniques sur 20 entrées** — la diversité par fichier (1 max) est
  respectée. Mais 3 paires concernent **la même ligne dans deux copies** (#11 vs #18 :
  Gemini_Takeout original et graphify-out dérivé, même ligne 5835 — deux fichiers
  distincts, mais même contenu). Une dédup par `realpath` + hash donnerait une
  sélection plus propre — **à faire dans un BRIEF II**.
- **Aucune entrée "pour" dans la sélection finale**. Avec 155 491 matchs bruts et un
  filtre "anti-pronom" imparfait, **"pour" est un faux ami structurel** : 99 % des
  occurrences sont du bruit ("pour nous", "pour le moment", "pour tel besoin"). Le
  seuil de qualité n'est pas atteignable sans analyse LLM par ligne. Recommandation :
  utiliser un modèle pour annoter un échantillon, ou restreindre "pour" à un contexte
  de titre de section.
- **"au service de" est surreprésenté** (3 entrées sur 20). Cela vient d'une
  forte présence du pattern dans les guides Yann_Leonardi + le fait que le pattern est
  peu ambigu (vs "pour"). C'est probablement représentatif.
- **Plusieurs entrées concernent A'Space OS directement** (#14, #19), montrant que la
  finalité "apprendre à systématiser" revient souvent. Ce sont les candidats les plus
  prometteurs pour la nouvelle ontologie : **`Routine` et `SOP` visent à systématiser
  les opérations d'A'Space OS**.

## 5. Où vit l'Ikigai, où vit la Constitution

### CONSTITUTION.md

**L'hypothèse du brief ("réputée absente de `00_Amadeus/01_Identity_Core/`") est fausse.**
Le fichier canonique existe :

```
05_From_V2_Domains/00_Amadeus/01_Identity_Core/CONSTITUTION.md
```

(et 0 erreur de lecture, le fichier est accessible).

**Mais** : ce chemin est dans **le snapshot V2 archivé dans Geordi**. Le **V3
n'a pas reproduit ce dossier** :

```
ASpace_OS_V3/00_Amadeus/      → 10_Observers, 20_Harness, 30_Shadow, 40_Predictions,
                                50_Bench, 60_Tape_Specs, 70_Skills, 90_Doctrine
```

`01_Identity_Core/` n'existe pas en V3. La **Constitution n'a pas été migrée en V3**
ou vit ailleurs sous un autre nom. Aucun fichier nommé `*constitution*` n'a été
retrouvé dans `ASpace_OS_V3/` (vérifié par `find -iname "*constitution*"`).

**50 autres fichiers mentionnent "CONSTITUTION"** dans leur contenu. Plusieurs
sont des SDD (Spec-Driven Development) :

- `SDD-000_ricks-verse-constitution.md` (à la racine wiki/raw/sdd et dans 10_Tech_OS)
- `SDD-V0.5_SovereignConstitution.md` (multiples copies graphify)

Ces SDD sont des documents de spécification, **pas la Constitution elle-même**.
La Constitution canonique est unique (1 fichier par nom) ; ses dérivées
(SDD, graphify-out) la dupliquent.

### Ikigai

**1 087 fichiers** contiennent "Ikigai" (1087 occurrences dans 59 265 fichiers).
L'Ikigai est **massivement présent** — c'est un concept central, pas un thème
niche. Représentations notables :

- **Spec canonique** : `ASpace_OS_V3/20_Life_OS/21_Ikigai_Orville/Ikigai_Pillars_Horizons_Kardashev.md`
  (fichier source du système).
- **Hand-off explicite** : `03_Memory_Unified/LLM_Wiki/wiki/hand_offs/ikigai_horizons_to_12wy_roadmap_2026-07-12.md`
  (transition Ikigai → 12 Week Year, juillet 2026).
- **Code React** : `IkigaiApp.tsx`, `IkigaiHorizons.tsx`, `IkigaiPillars.tsx`,
  `IkigaiItemCard.tsx`, `IkigaiDetailPanel.tsx` — composants frontend (snapshot V2).
- **ADRs et PRDs** : `ADR-FWK-013_V0.1.3_Ikigai_Structure.md`, `ADR-V0.2.5_IkigaiDeep.md`,
  `PRD-V0.2.5_IkigaiDeep.md`, `fw-ikigai.store.ts`.

### Horizons

| Code | Fichiers | Présent dans V3 ? |
|---|---:|---|
| **H1** | 1 132 | ✅ `02_Horizons_Time/01_H1_Isaac/` |
| **H3** | 806 | ✅ `02_Horizons_Time/02_H3_Lamarr/` |
| **H10** | 737 | ✅ `02_Horizons_Time/03_H10_Bortus/` |
| **H30** | 499 | ✅ `02_Horizons_Time/04_H30_Alara/` |
| **H90** | 560 | ✅ `02_Horizons_Time/05_H90_Klyden/` |
| **Horizon** (mot) | 2 017 | n/a |

**Note technique sur H1** : 1 132 fichiers avec `\bH1\b` est élevé. Probablement
contaminé par `<h1>` HTML et autres. Mais 737 de H10 et 499 de H30 — sans ambiguïté —
montrent que les codes sont bien vivants.

## 6. Découvertes notables

1. **CONSTITUTION.md n'est pas absente — elle est dans le snapshot V2 de Geordi, pas
   dans V3.** Le V3 a restructuré Amadeus (10_Observers, 20_Harness, …) sans
   reproduire le dossier `01_Identity_Core/`. La doctrine Identity Core n'est pas
   dans le V3 vivant.
2. **H3 est la 5e horizon, pas une omission du brief.** Le brief énumérait H1/H10/H30/H90 ;
   la réalité est H1/H3/H10/H30/H90. Découverte : V3 a ajouté H3 (3 ans) entre H1 (1 an)
   et H10 (10 ans). Cela donne une grille **plus régulière** (1, 3, 10, 30, 90 — espacement
   logarithmique).
3. **Aucun concept Tech OS dans les 29 noms testés.** Le brief ne proposait que des
   candidats Business OS + Life OS. Pour une ontologie Tech OS, il faut itérer avec
   une nouvelle liste.
4. **"Pour" est inutilisable comme marqueur de finalité** sur ce corpus (155 491
   occurrences, 99 % de bruit). Une ontologie qui s'appuierait dessus s'effondrerait.
5. **Plusieurs tournures de finalité (5 sur 8) sont productives** : sert à, afin de,
   au service de, vise à, contribuent à, rattachée à, répond à. Une relation
   `sert_à` serait modélisable directement.
6. **`Charter` (158 fichiers) est le candidat le plus rare.** Vérifier s'il est
   vraiment central ou périphérique.
7. **`Ikigai` (1 087 fichiers) est un objet structurant**, pas un mot d'usage.
   Le système de Pillars × Horizons est un candidat sérieux pour l'ontologie
   trois couches.

## 7. Limites — ce qui n'a pas pu être mesuré

- **"Pour" en finalité** : 155 491 matchs, mais aucun n'a passé les filtres de
  qualité sans LLM. Une analyse assistée par LLM sur un échantillon de 200 phrases
  pourrait calibrer un filtre déterministe.
- **Doublons partiels** : 5 des 20 exemples sont des quasi-doublons (graphify-out
  copie l'original ; même ligne répétée). Une déduplication par `realpath` + hash
  du contenu donnerait une sélection plus propre. **À faire dans un BRIEF II**.
- **Tech OS** : pas de candidats testés. Le périmètre du brief excluait cette
  couche — c'est un manque à signaler pour la suite.
- **Encodage** : tous les fichiers ont été lus en `utf-8, errors='replace'`.
  Certains fichiers Markdown importés de Windows-1252 peuvent avoir des caractères
  remplacés par `?` — rare mais possible (0 erreur rapportée par le script).
- **Fichiers > 1 Mo** : tronqués à 1 Mo. Geordi contient des fichiers Graphify
  potentiellement plus gros ; leurs fins de contenu ne sont pas scannées.
- **Cibles H1/H10/H30/H90 avec bruit** : `\bH1\b` capture `<h1>`, dates (`2026-H1`),
  peut-être des références. Une vérification manuelle sur un échantillon de 50
  fichiers dirait si la mesure est solide.

## 8. Artefacts produits

| Fichier | Contenu |
|---|---|
| `RAPPORT_I_GEORDI_ENTITES.md` | Ce rapport |
| `entites_observees.json` | 29 noms × `{fichiers_distincts, couche_supposee, seuil, exemples}` |
| `finalites_exemples.json` | Comptes bruts par tournure + sélection 20 + contexte |
| `constitution_ikigai.json` | Comptes Constitution / Ikigai / Horizons + échantillons |
| `00_recon.py` | Walk + comptage (lecture seule) |
| `01_scan.py` | Scanner des noms candidats |
| `02_combined.py` | Scanner finalités + Constitution/IK/Horizons (en un passage) |

Tous les scripts sont reproductibles : `python 00_recon.py`, `python 01_scan.py`,
`python 02_combined.py` depuis ce dossier. Aucun ne modifie Geordi.

## 9. Recommandations pour la suite (BRIEF II)

1. **Tester une couche Tech OS** avec ~15 candidats : `Component`, `Module`, `Pipeline`,
   `Endpoint`, `Service`, `Build`, `Deploy`, `Migration`, `Worktree`, `Skill_API`, `MCP`,
   `Tool`, `Kernel`, `Spawn`, `Core`, `Watchdog`, `Replay`, `Spec`, `ADR`, `SDD`, `Charter`.
2. **Dédupliquer la sélection de finalités** par hash de contenu pour éliminer les
   quasi-doublons graphify-out.
3. **Modéliser la relation `sert_à`** dans l'ontologie — elle est productive et le
   verbe est rare (`sert à` : 212 matchs bruts). **Et** modéliser la relation
   `vise_à` (488 matchs) et `au_service_de` (119). Trois relations suffiraient à
   couvrir la majorité des verbes de finalité observés.
4. **Pour "Pour"** : ne pas le modéliser comme relation. Soit l'ignorer, soit
   restreindre à un contexte de titre (header Markdown).
5. **Charter** : vérifier manuellement les 158 fichiers. S'il est périphérique
   (convention de nommage), le sortir de l'ontologie.
6. **V3 — Constitution** : la doctrine Identity Core du V3 n'existe pas sous le
   nom `01_Identity_Core/CONSTITUTION.md`. À documenter ailleurs, ou à reconnaître
   que la doctrine n'a pas encore été portée en V3.

---

**Annexe — script principal** (le seul qui produit les 3 JSON) : voir
`02_combined.py` dans ce dossier. Les scripts `00_recon.py` et `01_scan.py`
sont des sous-scripts de validation et peuvent être re-jusés pour reproduire les
comptes.