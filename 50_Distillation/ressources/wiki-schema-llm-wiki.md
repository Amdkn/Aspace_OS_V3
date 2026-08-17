---
type: Backend
title: Schema LLM Wiki — trois couches raw/wiki/schema.md
description: Le schéma de construction et maintenance du wiki LLM_Wiki : trois couches physiques, six types de pages, trois workflows (ingest/query/lint), conventions de nommage et formatage.
tags: [llm-wiki, schema, pattern, maintenance, ingest, lint, geordi]
generated: { by: minimax-m3, at: 2026-08-17T20:32:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:32:00Z }
sources:
  - id: schema-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/schema.md"
    title: "LLM Wiki — Schema (CLAUDE.md Companion)"
    last_modified: 2026-05-10
  - id: plan-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/CARTOGRAPHIE_MEMOIRE_UNIFIEE.md"
    title: "Cartographie — Mémoire Unifiée (Ressources de Geordi)"
    last_modified: 2026-08-01
  - id: llm-wiki-pattern-source
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/sources/source_llm-wiki-pattern.md"
    title: "LLM Wiki Pattern (source canon)"
    last_modified: 2026-05-11
okf_version: "0.2"
---

# Schema LLM Wiki — trois couches raw/wiki/schema.md

> *"The LLM is the programmer; the wiki is the codebase."*
> — adapté de LLM Wiki Pattern

## 1. Trois couches physiques

```
raw/      → Immuables (articles, PDFs, transcripts, exports Gemini)
wiki/     → Propriétaire LLM, écrit par le LLM
schema.md → Compagnon CLAUDE.md qui dit au LLM comment se comporter
```

**Les sources brutes sont sacrées.** Le LLM les lit, ne les modifie jamais.

## 2. Six types de pages

| Type | Dossier | Rôle |
|---|---|---|
| **Summary** | `sources/` | Une page par source ingérée — points clés, citations, synthèse |
| **Entity** | `entities/` | Acteurs récurrents, outils, projets, concepts |
| **Concept** | `concepts/` | Idées transverses, patterns, frameworks |
| **Synthesis** | `syntheses/` | Thèse longue fusionnant plusieurs sources |
| **Comparison** | `comparisons/` | Tables, matrices, side-by-side |
| **Overview** | `wiki/index.md` | Catalogue de toutes les pages avec résumés |
| **Log** | `wiki/log.md` | Chronologique append-only des ingests/queries/lints |

## 3. Trois workflows

### Ingest (traiter une nouvelle source)

```
1. Lire la source en entier
2. Extraire les entités clés (personnes, outils, projets, concepts)
3. Écrire une page summary dans sources/[slug].md
4. Mettre à jour wiki/index.md
5. Mettre à jour ou créer les pages entities/
6. Mettre à jour ou créer les pages concepts/
7. Chercher les contradictions → flagger dans log.md
8. Append dans wiki/log.md
```

Un seul ingest peut toucher 10–15 pages. Le LLM possède tout.

### Query (répondre à une question)

```
1. Lire wiki/index.md
2. Descendre dans les pages pertinentes
3. Synthétiser
4. Si la réponse a valeur (comparison, discovery) → la verser comme nouvelle page
5. Citer les pages avec wikilinks
6. Append dans log.md
```

### Lint (health check)

```
1. Vérifier les contradictions entre pages
2. Flagger les claims périmés supersédés par sources plus récentes
3. Trouver les pages orphelines (pas de lien entrant)
4. Trouver les concepts importants sans page dédiée
5. Suggérer des cross-refs manquantes
6. Reporter les data gaps qui pourraient être remplis par web search
```

## 4. Conventions de nommage

- `sources/` : `YYYY-MM-DD_slug-source-title.md`
- `entities/` : `entity_[name].md` (kebab-case, lowercase)
- `concepts/` : `concept_[topic].md`
- `syntheses/` : `synthesis_[thesis-title].md`
- `comparisons/` : `comparison_[A]-vs-[B].md`
- `log.md` : `## [YYYY-MM-DD] action | Title`

## 5. Frontmatter obligatoire

```yaml
---
source: LLM_Wiki_A0
date: YYYY-MM-DD
type: summary|entity|concept|synthesis|comparison
domain: <tag domaine>
tags: [#tag1 #tag2]
---
```

## 6. Cross-référencement avec wikilinks

`[[entity_rick]]`, `[[concept_sovereignty]]`, `[[sources/source_gemini-takeout-2026-05]]`.
L'Obsidian graph view naît de ces liens. Navigation manuelle rapide en Bash :

```bash
grep "^## \[" wiki/log.md | tail -10   # 10 dernières entrées
grep "^## \[" wiki/log.md | grep ingest # tous les ingests
```

## 7. Outils attendus

- **Obsidian** : IDE de lecture (graph view, Dataview, requêtes frontmatter)
- **qmd** : moteur de recherche local (BM25 + vector) sur les `.md` du wiki
- **Marp** : génération de slides depuis markdown
- **Context7 MCP** : web search pour gaps pendant le lint

## 8. Loi du harvest (W22 M5, 2026-07-13)

> Une page evergreen (concepts/, entities/) n'est créée QUE depuis un artefact shippé
> (handoff, wargame exécuté, projet clos). Skill canon `/harvest`. Anti-pattern : créer une
> page SANS artefact shippé = bloquer, exiger source canon (D4 append-only).

## Liens entrants

- `okf-v0-1-format-standard.md` — OKF est la forme ; ce schema en est la chair
- `geordi-kb-quatre-piliers.md` — où loge ce schema dans la KB
- `compounding-knowledge-wiki.md` — pourquoi ce schema produit un effet composé
