---
type: Pattern
title: Graphify-burst chunks — la duplication de fichiers massifs entre chunks et Geordi
description: Le pipeline Graphify produit des dossiers `graphify-burst/chunks/chunk_NNN/` dupliquant le contenu d'autres chemins du seau ; un même fichier (ex. `affine_deal_drafts.md` 60 001 mots, `REBUILD_PROMPT_V2.md` 15 627 mots) peut apparaître dans 4 chunks distincts et dans `03_Resources_Geordi/`.
tags: [graphify, burst, chunks, duplication, pipeline, 60001-mots]
generated: { by: minimax-m3, at: 2026-08-17T23:45:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:45:00Z }
sources:
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl"
    title: Substrat — comptage des chemins, top docs par mots
    last_modified: 2026-08-17
  - id: archive-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/README.md"
    title: Origine V3 du snapshot
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Graphify-burst chunks — la duplication de fichiers massifs entre chunks et Geordi

## Le constat (substrat)

Le substrat d'extraction a révélé que **plusieurs fichiers apparaissent à
plusieurs endroits** avec exactement le **même nombre de mots** — un
proxy fiable de duplication littérale.

### Exemple 1 — `affine_deal_drafts.md` (60 001 mots)

| # | Chemin | Mots |
|---|---|---|
| 1 | `_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_019/affine_deal_drafts.md` | 60 001 |
| 2 | `_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_018/affine_deal_drafts.md` | 60 001 |
| 3 | `_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_001/affine_deal_drafts.md` | 60 001 |
| 4 | `_V3_STRUCTURE_2026-08-02/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/affine_deal_drafts.md` | 60 001 |

**4 occurrences** du même fichier dans 4 chunks + 1 dans Geordi.

### Exemple 2 — `REBUILD_PROMPT_V2.md` (15 627 mots)

| # | Chemin | Mots |
|---|---|---|
| 1 | `_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_004/REBUILD_PROMPT_V2.md` | 15 627 |
| 2 | `_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_001/REBUILD_PROMPT_V2.md` | 15 627 |
| 3 | `_V3_STRUCTURE_2026-08-02/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw OS Blueprint Kit/REBUILD_PROMPT_V2.md` | 15 627 |

**3 occurrences** du même fichier.

## Le pattern `graphify-burst/chunks/`

Le chemin typique d'un fichier dupliqué est :

```
…/graphify-burst/chunks/chunk_NNN/<nom_de_fichier>.md
```

Plusieurs dossiers `graphify-burst` existent :

- `30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/`
- (probablement d'autres : `00_Amadeus/.../graphify-burst`, `20_Life_OS/.../graphify-burst`)

Le **mot `burst`** est un indice : c'est un run **explosif** où le
pipeline a **injecté** un grand nombre de fichiers en peu de temps. Le
résultat, c'est que le même fichier peut atterrir dans plusieurs chunks
si l'injection s'est faite en plusieurs passes sans déduplication.

## Pourquoi cette duplication existe

**Hypothèse 1 — déduplication non implémentée dans le pipeline**. Si
chaque chunk est traité indépendamment et qu'un même fichier source est
présent dans plusieurs sources d'entrée, il sera répliqué dans chaque
chunk.

**Hypothèse 2 — intentionnel, pour redondance**. Le pipeline peut avoir
voulu **dupliquer** pour assurer qu'un fichier volumineux n'est pas
perdu en cas d'échec d'un chunk. C'est le pattern « write-many-read-one »
des stockages objet.

**Hypothèse 3 — run partiel + rattrapage**. Le run Graphify qui a
produit 14/25 chunks réussis a peut-être été **relancé** plusieurs fois
en mode « rattrapage », et chaque rattrapage a ajouté une copie dans un
nouveau chunk.

**Le substrat ne tranche pas.** Le brief demande de **nommer sans
arbitrer**.

## L'impact sur la distillation

Pour un graphe RDF, ces 4 occurrences de `affine_deal_drafts.md`
représentent **un seul nœud** (l'entité `affine_deal_drafts`) avec
**plusieurs `aspace:archivePath`** :

```turtle
<aspace:entity/affine_deal_drafts>
    a aspace:Document ;
    aspace:wordCount 60001 ;
    aspace:archivePath "_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_019/affine_deal_drafts.md" ;
    aspace:archivePath "_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_018/affine_deal_drafts.md" ;
    aspace:archivePath "_V3_STRUCTURE_2026-08-02/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_001/affine_deal_drafts.md" ;
    aspace:canonicalPath "_V3_STRUCTURE_2026-08-02/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/affine_deal_drafts.md" .
```

**Une entité, plusieurs chemins**, et un **chemin canonique** est le
`03_Resources_Geordi/01_Guides/...` — c'est la **Living Source** désignée
par le README d'archive.

## Concepts liés

- [[graphify-out-pipeline-partial-run]] — la course partielle qui a généré ces chunks.
- [[archive-as-source-of-truth-decision]] — pourquoi Geordi est désigné comme chemin canonique.
