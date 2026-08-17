---
type: Event
title: Graphify-out — pipeline parallèle avec 11 chunks échoués sur 25
description: Le dossier `graphify-out/` contient les sorties d'un run Graphify (25 chunks, 8 workers max) qui a réussi 14 chunks sur 25, produit 1006 nœuds uniques et 1666 arêtes, avec 17 communautés détectées (long tail).
tags: [graphify, pipeline, parallel, chunks, failure, partial-run, 2026-06-16, 421-files]
generated: { by: minimax-m3, at: 2026-08-17T23:20:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:20:00Z }
sources:
  - id: graph-report
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/graphify-out/GRAPH_REPORT.json"
    title: GRAPH_REPORT.json (1006 nœuds, 1666 arêtes, 17 communautés)
    last_modified: 2026-06-16
  - id: swarm-summary
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/graphify-out/swarm_summary.json"
    title: swarm_summary.json (25 chunks, 14 ok, 11 failed, 803.2 s total)
    last_modified: 2026-06-16
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl"
    title: Substrat — 387 fichiers .md dans graphify-out (chunks + index files)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Graphify-out — pipeline parallèle avec 11 chunks échoués sur 25

## Mesure du run (verbatim `swarm_summary.json`)

| Champ | Valeur |
|---|---|
| Cible | `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\04_Archives_Data` |
| Out root | `…\04_Archives_Data\graphify-out` |
| **n_chunks** | **25** |
| **max_workers** | **8** |
| **ok** | **14** (56%) |
| **failed** | **11** (44%) |
| elapsed_s | 803,2 s (~13 min) |
| total_files | 421 |

## Le succès (verbatim `GRAPH_REPORT.json`)

| Champ | Valeur |
|---|---|
| merged_at | 2026-06-16 |
| chunk_count | 14 |
| **unique_nodes** | **1006** |
| **unique_edges** | **1666** |
| communautés | **17** au total |

Distribution des communautés :

| Communauté | Taille |
|---|---|
| 0 | 194 |
| 1 | 171 |
| 2 | 146 |
| 3 | 122 |
| 4 | 101 |
| 5 | 87 |
| 6 | 65 |
| 7 | 56 |
| 8 | 32 |
| 9 | 17 |
| 10 | 8 |
| 11-16 | 1 chacune (long tail) |

C'est une **distribution en power-law** classique de communautés
détectées par Louvain / Label Propagation : quelques hubs massifs et un
long tail de singletons.

## Périmètre mesuré du dossier

- **387 fichiers `.md`** dans `graphify-out/` selon le substrat.
- **25 dossiers `chunk_000` à `chunk_024`**, dont :
  - **chunk_000 à chunk_015** : **16 fichiers par chunk** (cohérent avec
    `~17 fichiers / chunk` annoncé dans le swarm summary)
  - **chunk_016 à chunk_024** : 15 fichiers par chunk (un peu moins)
- **2 fichiers `.json` racine** : `GRAPH_REPORT.json`, `swarm_summary.json`
- **1 fichier `graph.json`** (le graphe fusionné)

## Pourquoi 11 chunks ont échoué

Le `swarm_summary.json` liste les chunks réussis (0, 1, 2, 4, 5, 6, 7, 8,
9, 10, 11, 12, 13, 14…) et laisse les autres sans `ok:true` — **la raison
exacte des échecs n'est pas documentée dans le run** :

- Pas de log d'erreur préservé
- Pas de `error_message` dans la sortie swarm_summary
- Pas de re-run documenté

L'opérateur qui voudrait rejouer le pipeline devrait :
1. Identifier les 11 chunks sans `ok:true` (la liste n'est pas dans le
   swarm_summary complet, c'est une lecture exhaustive à faire).
2. Relancer manuellement.
3. Re-merger avec un nouveau `GRAPH_REPORT.json`.

## Le graphe fusionné — mérites et limites

- **1006 nœuds uniques** : cohérent avec 421 fichiers et un facteur
  d'extraction ~2,4 (chaque fichier génère ~2-3 nœuds en moyenne).
- **1666 arêtes** : densité ~3,3 arêtes/nœud — un graphe modérément
  connecté, **pas** un graphe pathologique full-connected.
- **17 communautés** : signal de **modularité** réelle, le corpus n'est
  pas un blob.

## Le sens de cette archive

C'est **un run de pipeline**, pas un livrable canonique :

- Le run a **réussi** au sens « artefacts produits » (1006 nœuds, 1666
  arêtes, 17 communautés).
- Le run a **échoué partiellement** au sens « 11 chunks sur 25 » — c'est
  un **état partiel** qu'il faut comprendre comme tel.
- Le **nœud RDF canonique** reste `03_Resources_Geordi/wiki/`, pas
  `graphify-out/graph.json`.

## Concepts liés

- [[graphify-burst-chunk-duplication-pattern]] — la duplication de fichiers entre chunks et 03_Resources_Geordi.
- [[archive-as-source-of-truth-decision]] — pourquoi Geordi et pas graphify-out.
