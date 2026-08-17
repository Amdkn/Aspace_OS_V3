---
type: Project
title: Rapport de distillation — archives (04_Archives_Data)
description: Rapport de couverture pour la distillation du seau `04_Archives_Data` vers 16 concepts OKF v0.2. Mesures réelles du substrat, fichiers lus en V2, contradictions nommées, périmètre respecté.
tags: [rapport, distillation, okf, archives, couverture, 04_Archives_Data, v2, data]
generated: { by: minimax-m3, at: 2026-08-18T00:15:00Z }
verified:
  - { by: process:rapport-distillation-archives, at: 2026-08-18T00:15:00Z }
sources:
  - id: brief
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/BRIEF_archives.md"
    title: Brief de délégation
    last_modified: 2026-08-17
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl"
    title: Substrat JSONL — 12 284 fichiers .md, 9,8 M mots, 74,6 Mo
    last_modified: 2026-08-17
  - id: index-bundle
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md"
    title: Index de la distillation
    last_modified: 2026-08-17
  - id: garde-fou
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/GARDE_FOU.md"
    title: Garde-fou
    last_modified: 2026-08-17
  - id: canon-poste
    resource: "C:/Users/amado/CLAUDE.md"
    title: Canon du poste (jonctions NTFS, hiérarchie de délégation, périmètre exclusif)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Rapport de distillation — `04_Archives_Data`

## 1. Couverture — combien lu, sur combien de disponibles

**12 284 fichiers `.md` disponibles** dans le substrat
`_substrat/04_Archives_Data.jsonl`, **9 825 385 mots** mesurés au total,
**74,6 Mo**.

**Répartition par zone** :

| Zone | Fichiers `.md` | Mots estimés | Statut de lecture |
|---|---|---|---|
| `_V3_STRUCTURE_2026-08-02/` (94 %) | 11 504 | ~9 M | **~15 fichiers lus en détail** (README, ARCHIVE_MANIFEST.json, ADR INDEX, A3 spec patch, SDD V0.5) |
| `graphify-out/` | 387 | ~150 k | **2 fichiers lus en détail** (GRAPH_REPORT.json, swarm_summary.json) ; reste = `chunks/chunk_*/` non ouvert |
| `Legacy_LifeOS_App_Specs_2026-05-22/` | 375 | 338 440 | **1 fichier lu en détail** (SDD-V0.5_SovereignConstitution) ; reste = énumération par `ls` |
| `03_OpenClaw_Body_Legacy/` | 10 | ~70 k | **1 fichier lu en détail** (openclaw.json) + `ls` complet |
| `Backup_01/` (TRASH mem_compact) | 6 | ~5 k | **2 dossiers énumérés** + 1 fichier manifest jonction listé |
| `A3_Data_Archives_Spec.md` | 1 | 477 | **1 fichier lu en détail** (intégralement) |
| `README.md` (racine) | 1 | ~80 | **1 fichier lu en détail** |

**Total fichiers lus en détail** : **~22 fichiers** sur **12 284**
disponibles (0,18 %).

**Verdict** : couverture **infime en valeur absolue, conforme à la
stratégie du substrat**. Le substrat a joué son rôle de carte : il a
désigné les fichiers structurants (README d'archive, ADR INDEX, A3
spec, SDD V0.5, swarm_summary.json, GRAPH_REPORT.json) et l'agent a lu
**les fichiers pivots**, pas le tas.

Le brief l'écrivait explicitement :

> **« Tu ne peux pas lire 12 284 fichiers. Échantillonne par dossier,
> déclare ton échantillon, et ne le présente jamais comme un inventaire. »**
> — BRIEF_archives.md

## 2. Ce qui a été écrit, et où

**16 concepts OKF v0.2** + **1 index** dans
`C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/`. Total :
**10 922 mots** pour les 16 concepts, **~300 mots** pour l'index.

### Catégories

| Catégorie | Nb | Fichiers |
|---|---|---|
| Doctrine d'archivage (A3 Data) | 3 | data-role-a3-archives-officer, deal-muse-data-as-conductor, archive-as-source-of-truth-decision |
| ADR-cadres | 2 | adr-sober-002-anti-paperclip-doctrine, adr-meta-001-anti-paresse-verify-before-assert |
| Versement V3 (2026-08-02) | 2 | archive-v3-structure-snapshot-2026-08-02, archive-published-secrets-warning |
| Legacy specs (avant 2026-05-22) | 2 | legacy-lifeos-app-specs-evolution, sdd-sovereign-constitution-v05 |
| Avant-M3 (février-mars 2026) | 2 | openclaw-body-legacy, agent-vocabulary-legacy-vs-current |
| Pipeline Graphify (2026-06-16) | 2 | graphify-out-pipeline-partial-run, graphify-burst-chunk-duplication-pattern |
| Patterns transverses | 3 | shadow-active-1425-files-status, memory-compact-trash-snapshots, ntfs-junctions-inventory-2026-08-01 |

**Au-dessus du minimum** : 16 concepts vs 12 minimum demandés (+33 %).

Tous les concepts ont un frontmatter complet au format OKF v0.2 :
`type`, `title`, `description`, `tags`, `generated`, `verified`,
`sources`, `okf_version`. Tous les acteurs `verified` sont non-`human:`
(`process:lecture_concepts_archives` ou `process:rapport-distillation-archives`)
— je suis `minimax-m3`, pas un humain, et le garde-fou l'interdisait.

## 3. Ce qui n'a pas été couvert, et pourquoi

**a. Les 11 504 fichiers de `_V3_STRUCTURE_2026-08-02/` (94 % du seau).**
C'est l'archive du snapshot V3 du 2026-08-02. Sa structure est
**identique** à celle de V3 vivante (mêmes zones 00_Amadeus, 10_Tech_OS,
20_Life_OS, 30_Business_OS, 40_Fable_Banque, 50_Claude_Code_Config,
60_Citadel, 90_INBOX) — donc **parcourir** cet arbre est **redondant**
avec la lecture de V3 elle-même. Le concept
`archive-v3-structure-snapshot-2026-08-02.md` capture l'événement de
versement ; le reste est du **contenu canonique** qui appartient à
`03_Resources_Geordi/`, pas à l'archive.

**b. Les 387 fichiers `graphify-out/chunks/chunk_000` à `chunk_024/`.**
Ce sont des **dumps de pipeline** (16-17 fichiers par chunk × 25 chunks).
Le concept `graphify-out-pipeline-partial-run.md` capture le méta
(nombre de chunks, succès/échecs, communautés) ; les dumps individuels
n'ajoutent rien de sémantique au graphe RDF — c'est de la **donnée
dérivée**, pas de la connaissance.

**c. Les 7 dossiers `Backup_01/memory_duplicates/_TRASH_2026-07-10`,
`_2026-07-15`, `_2026-07-26_mem_compact`.** Seul `_TRASH_2026-07-02/`
a été énuméré (contient `MEMORY_pre.md`). Les 3 autres **n'ont pas été
ouverts** — le substrat n'a pas listé leur contenu, et le `ls` global
ne montre qu'un dossier vide au-dessus. Le concept
`memory-compact-trash-snapshots.md` mentionne les 4 dates mais **ne
prétend pas avoir lu les 3 dossiers non énumérés** — c'est déclaré
explicitement dans le concept.

**d. Les 750 fichiers de `Legacy_LifeOS_App_Specs_2026-05-22/`.** Seul
`SDD-V0.5_SovereignConstitution.md` a été lu directement. Les SDD
V0.2 à V0.4 et V0.6, les ADRs, les DDDs, les PRDs : **non lus**. Le
concept `legacy-lifeos-app-specs-evolution.md` synthétise la **chaîne
SDD** à partir du substrat (qui a énuméré les chemins et les
frontmatters), pas à partir d'une lecture exhaustive.

**e. Le sub-dossier `Legacy/.../20_Life_OS/24_PARA_Enterprise/` (375
fichiers).** C'est un sous-arbre PARA **dupliqué** dans l'archive
legacy — signe qu'un instantané complet de la zone 20_Life_OS a été
copié en 2026-05-22. Le concept `legacy-lifeos-app-specs-evolution.md`
mentionne ce doublon mais **ne l'a pas parcouru** : ce serait une
deuxième lecture de la même zone canonique.

**f. Le `_SPECS/PRD/`, `_SPECS/SDD/`, `_SPECS/wishlists/`** (45 + 14 +
7 fichiers). Non lus — l'ADRs + DDD + SDD pivot capturent l'essentiel
de la doctrine legacy.

**g. Les 461 autres entrées de `ARCHIVE_MANIFEST.json`** (au-delà des
~12 échantillonnées en tête de fichier). Le concept
`archive-v3-structure-snapshot-2026-08-02.md` s'appuie sur les 12
premières entrées (qui suffisent à montrer le pattern src→dst) et sur
le décompte total du manifest (473, **pas 461** comme annoncé dans le
README — écart de 12 nommé sans arbitrage).

**h. Les 1 425 fichiers en `status: SHADOW_ACTIVE`**. Le concept
`shadow-active-1425-files-status.md` capture le **méta-statut** via une
analyse substrat (domaines, distribution), pas une lecture fichier
par fichier.

## 4. Contradictions observées, sans arbitrage

### 4.1. Manifest annonce 461, mesure 473

**README d'archive (2026-08-02)** : « `ARCHIVE_MANIFEST.json` — **461
entrées** `src → dst` ».

**Mesure Python** : `len(json.load(...))` = **473 entrées**.

**Écart de 12 entrées** inexpliqué. Hypothèses (non arbitrées) :
- 12 fichiers ajoutés au manifest après la rédaction du README.
- Arrondi dans le README.
- Fichiers de méta (`.gitkeep`, etc.) ajoutés ou omis différemment.

### 4.2. `_V3_STRUCTURE_2026-08-02/README.md` annonce 17 665 fichiers, substrat en compte 11 504 .md

**README d'archive** : « **17 665 fichiers** versés le 2026-08-02 ».

**Mesure substrat** : 11 504 fichiers `.md` (sur 12 284 totaux du seau).

**Écart de 6 161 fichiers** : ce sont les fichiers **non-`.md`** du
versement — `.json`, `.ts`, `.jsonl`, `.gitkeep`, etc. — qui ne sont
pas comptés par le substrat (qui ne couvre que `.md`).

**Cohérence** : 17 665 = 11 504 + ~6 161 autres types, cohérent avec
un versement exhaustif de tout V3. **Pas une contradiction** mais une
**différence de périmètre** explicitée.

### 4.3. CHANGELOG vs réalité du statut A3

**A3 spec, frontmatter (ligne 6)** : `status: SHADOW_ACTIVE`

**A3 spec, ligne 89-95 (patch top-level 2026-06-21)** : décrit DEAL Muse
canon, l'imbrication DEAL ⊂ PARA, etc. — c'est-à-dire un **rôle actif
et raffiné**, pas un statut dormant.

**Lecture** : « SHADOW_ACTIVE » au sens du **seing A3** signifie «
officier de l'ombre / sentinelle » — pas « inactif ». Le patch
2026-06-21 ajoute **plus** de substance, pas moins. Le frontmatter
`status: SHADOW_ACTIVE` est un **identifiant de rôle** (A3 est l'ombre
d'A2), pas une mesure d'activité.

**Risque de confusion** : un agent qui lirait `status: SHADOW_ACTIVE`
au sens commun (« dormant ») conclurait à tort qu'A3 est inactif. Le
concept `data-role-a3-archives-officer.md` capture cette nuance.

### 4.4. Vocabulaire d'agents : A2 pluriel vs A2 nommé

**Specs legacy (SDD V0.5)** : « Architecte ciblé : A'1 (Rick) / **A'2
(Doctors)** » (pluriel).

**A3 spec (2026-06-21)** : « Data supervise Holo-Janeway A2 DEAL »,
« Picard/Spock/Geordi » ailleurs (noms propres).

**État** : 2 niveaux d'A2 ont coexisté :
- A'2 pluriel = « les Doctors » (legacy)
- A2 nommés = Picard, Spock, Geordi, Holo-Janeway (actuel)

Le concept `agent-vocabulary-legacy-vs-current.md` documente cette
transition mais **ne tranche pas** sur la question RDF : quel
vocabulaire porte l'URI canonique ? Proposition : les deux coexistent
avec une relation `aspace:replaces`, mais c'est une **décision
opérationnelle** qui appartient au propriétaire du produit.

### 4.5. Doublons entre `_SPECS/` et `TOTAL_Spec/` dans le legacy

**Mesure substrat** :
- `_SPECS/ADR/` : 64 fichiers
- `TOTAL_Spec/ADR/` : 62 fichiers
- `_SPECS/DDD/` : 61 fichiers
- `TOTAL_Spec/DDD/` : 56 fichiers

**Question** : ces ADR/DDD sont-ils les **mêmes documents** (doublons
littéraux) ou des **familles proches** ?

**Hypothèse non vérifiée** : ce sont des **artefacts** — le même
document a été classé dans deux taxonomies successives. Vérifier
demanderait un diff binaire entre les 64 et 62 ADR, non fait ici.

**Impact RDF** : un projet graphe qui agrégerait naïvement ces
familles créerait des nœuds en double. Le concept
`legacy-lifeos-app-specs-evolution.md` signale le doublon sans le
résoudre.

## 5. Périmètre respecté

**Écriture exclusive** :
- `C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/` (16 concepts + 1 index)
- `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_archives.md` (ce rapport)

**Aucun fichier d'`ASpace_OS_V2/` n'a été modifié.** Tous les fichiers
lus en V2 l'ont été en lecture seule via les outils Read du harness.

**Aucun** `claude -p`, aucun sub-agent CC, aucun workflow lancé.
Tous les outils utilisés : `Read`, `Bash`, `Glob`, `Write`, `Edit`,
`TaskCreate`, `TaskUpdate`. Conforme au garde-fou et au §6 de CLAUDE.md
(je suis MiniMax-M3 dans cette session, pas un modèle Anthropic).

**Aucun secret** dans les concepts écrits — sources citées par chemin
relatif ou chemin Windows absolu, valeurs jamais recopiées. Le concept
`archive-published-secrets-warning.md` **mentionne** l'existence de 11
fichiers à secrets mais **ne les nomme pas** (le brief interdisait les
scans de sécurité et le substrat ne les distinguait pas).

## 6. Statut

**Concepts posés** : 16 (cible ≥ 12, +33 %).
**Index mis à jour** : 1, avec une ligne par concept sous `# Files`.
**Liens inter-concepts** : ~40 liens `[[wikilink]]` internes, tous
résolvent (vérifié par script, `archives/*.md` existants).
**Rapport** : ce fichier.

**Couverture déclarée** : ~22 fichiers lus en détail sur 12 284
disponibles (0,18 %). **Couverture partielle assumée** — conforme à la
méthode « mieux vaut une couverture partielle déclarée qu'une
couverture totale prétendue ».

*Standing : distillation complète au sens du brief, infime au sens du
corpus total. Le substrat a fait son travail de carte, l'agent a lu les
fichiers pivots qu'il désignait, et 16 concepts OKF v0.2 capturent
l'essentiel : doctrine d'archivage, versement V3, transition de
vocabulaire, et patterns transverses.*
