---
type: Concept
title: Compounding Knowledge — pourquoi un wiki LLM bat RAG
description: Le wiki LLM produit un effet composé (chaque interaction augmente la valeur), contrairement à RAG extractif qui repart de zéro. Trois conditions : le principal reste, les rendements sont réinvestis, le temps amplifie la base. Le LLM élimine le goulot de maintenance.
tags: [compounding-knowledge, wiki, rag, maintenance, llm-pattern, knowledge-system]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:00:00Z }
sources:
  - id: concept-compounding
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_compounding_knowledge.md"
    title: "Concept: Compounding Knowledge"
    last_modified: 2026-05-11
  - id: llm-wiki-pattern-source
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/sources/source_llm-wiki-pattern.md"
    title: "LLM Wiki Pattern (source canon)"
    last_modified: 2026-05-11
  - id: wiki-schema
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/schema.md"
    title: "LLM Wiki — Schema (CLAUDE.md Companion)"
    last_modified: 2026-05-10
okf_version: "0.2"
---

# Compounding Knowledge — pourquoi un wiki LLM bat RAG

> *Related terms* : persistent wiki, knowledge compilation, RAG vs curated memory.
> *See also* : [[sources/source_llm-wiki-pattern]]

## 1. Définition

Un **système de connaissance** où chaque interaction **augmente la valeur** (au lieu de
la laisser plate ou de la dégrader). L'artefact produit — le wiki — **compose** dans le
temps comme un investissement bien géré. Chaque source ingérée, chaque query répondue,
chaque lint pass ajoute à un tout grandissant, cross-référencé, maintenu de façon cohérente.

**Contraste avec RAG extractif** : chaque query repart de zéro. Le système ne construit
**jamais** sur lui-même. Pas d'accumulation, pas de synthèse, pas de compounding.

## 2. Pourquoi « compounding » est la bonne métaphore

L'intérêt composé fonctionne parce que :
1. Le principal (connaissance) reste dans le système
2. Les rendements (insights, connections) sont **réinvestis**, pas consommés
3. Le temps amplifie la base

Le LLM Wiki applique les trois :
1. **Principal reste** : raw sources → wiki summaries sont des ajouts permanents
2. **Rendements réinvestis** : les bonnes réponses deviennent de nouvelles pages wiki ;
   les lint fixes mettent à jour les pages existantes
3. **Le temps amplifie** : un wiki de 100 sources est plus utile qu'un de 10 ;
   un wiki de 10 000 pages est une thèse vivante

## 3. Le coût de maintenance est la variable

La raison pour laquelle la plupart des wikis personnels échouent à composer : le coût de
maintenance **augmente plus vite que la valeur**. Les mainteneurs humains abandonnent.
Les cross-références deviennent périmées. Les synthèses se contredisent.

Le LLM **élimine le goulot de maintenance**. Il touche 15 fichiers par ingest, met à
jour les cross-references à chaque update, flagge les contradictions automatiquement.
La courbe de compounding reste positive indéfiniment.

## 4. Application à A'Space OS

| Stage | Système | Compose ? |
|---|---|---|
| Conversations brutes | `Gemini_Takeout_2026/*.md` | Non (archive statique) |
| Summaries LLM-extraits | `LLM_Wiki/wiki/sources/` | Oui |
| Pages entité | `LLM_Wiki/wiki/entities/` | Oui |
| Pages synthèse | `LLM_Wiki/wiki/syntheses/` | Oui |
| Réponses filées | `LLM_Wiki/wiki/sources/` + `comparisons/` | Oui |

Le Takeout est le corpus seed. Le wiki est l'intérêt composé.

## 5. Garde-fous (le contraire de compounding)

- **Perdre le LLM** = la valeur composée se fige ; un wiki sans maintenance devient cimetière.
- **Changer de modèle** = risque de dérive dans la qualité des résumés.
- **Indexer sans curarisation** = duplications, contradictions, halitose.

## 6. Loi du harvest (W22 M5, 2026-07-13)

> Une page evergreen (concepts/, entities/) n'est créée QUE depuis un artefact shippé.
> Anti-pattern : créer une page SANS artefact shippé = bloquer, exiger source canon.

C'est le **mécanisme anti-pollution** du compounding : le wiki ne dérive pas.

## Liens entrants

- `wiki-schema-llm-wiki.md` — la mise en œuvre qui produit le compounding
- `geordi-kb-quatre-piliers.md` — où loge le wiki dans la KB
- `okf-v0-1-format-standard.md` — le format qui rend le wiki bundle-stable
