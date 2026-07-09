---
source: LLM_Wiki_A0
date: 2026-05-10
type: summary
domain: LLM_Wiki_Pattern / Knowledge_Architecture
tags: [#LLM_Wiki #RAG #Knowledge_Base #Persistent_Wiki #Compounding_Knowledge]
---

# LLM Wiki Pattern

**Source:** Personal document shared by A0 Amadeus, 2026-05-10.
**Public provenance (confirmed 2026-05-17):** Andrej Karpathy — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**Type:** Pattern / Architecture Note.
**Slug:** `llm-wiki-pattern`
**Companion source:** [[source_karpathy-autoresearch]] (autonomous research loop — sibling pattern by same author)

---

## Core Thesis

Most RAG systems re-derive knowledge from scratch on every query. The LLM Wiki pattern solves this by having the LLM **incrementally build and maintain a persistent wiki** — a structured, interlinked markdown collection that sits between the user and raw sources. Knowledge is compiled once and kept current. The cross-references are already there. The contradictions are flagged. The synthesis already reflects everything read.

> *"The wiki is a persistent, compounding artifact."*

---

## The Three Layers

| Layer | Role | Owner |
|-------|------|-------|
| **Raw sources** | Immutable curated documents | Human |
| **Wiki** | LLM-generated markdown pages (summaries, entities, concepts, syntheses) | LLM |
| **Schema** | CLAUDE.md-style instructions telling the LLM how to behave as wiki maintainer | Co-evolved |

---

## Key Differentiator: Maintenance by LLM

Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored, don't forget cross-references, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

**Human's job:** Curate sources, direct analysis, ask good questions, think about meaning.
**LLM's job:** Summarize, cross-reference, file, update, flag contradictions.

---

## Operations

### Ingest
Drop source → LLM reads → writes summary → updates index → updates entity/concept pages → flags contradictions → logs.

### Query
User asks → LLM reads index → drills into pages → synthesizes answer → cites with wikilinks → files valuable answers back as new wiki pages.

### Lint
Periodic health-check: contradictions, stale claims, orphans, missing cross-references, data gaps. LLM suggests new questions and sources.

---

## Index vs Log

- **index.md** — content-oriented catalog. Updated on every ingest. LLM reads it first on every query.
- **log.md** — chronological append-only record. Each entry starts with `## [YYYY-MM-DD]` for Unix-parsability.

---

## Optional Tools

| Tool | Purpose |
|------|---------|
| Obsidian | Wiki IDE — graph view, Dataview, frontmatter queries |
| qmd | Local BM25+vector search over markdown (CLI + MCP) |
| Marp | Slide deck from markdown |
| Obsidian Web Clipper | Browser → markdown for raw sources |
| Download images locally | LLM can view images directly |

---

## Why This Works

Vannevar Bush's Memex (1945) envisioned a personal, curated knowledge store with associative trails. The part he couldn't solve: who does the maintenance? LLMs handle that now.

Related: [[concept_sovereignty]] — the wiki as a sovereign knowledge layer, distinct from the raw sources that feed it.


---

## Inbounds

- [[sources/source_llm-wiki-pattern]]

---

## Context for A'Space OS

This pattern maps directly onto A0's memory architecture:

| LLM Wiki Concept | A'Space Equivalent |
|------------------|-------------------|
| Raw sources | `Gemini_Takeout_2026/` conversations |
| Wiki | `LLM_Wiki/wiki/` (entities, concepts, syntheses) |
| Schema | `LLM_Wiki/wiki/schema.md` (this file governs Claude Code as wiki maintainer) |
| Index | `LLM_Wiki/wiki/index.md` |
| Log | `LLM_Wiki/wiki/log.md` |
| Obsidian IDE | `ASpace_OS_V2/` opened in Obsidian |

**The Takeout conversations are the first raw source corpus.** Ingesting them selectively — one month at a time — is the natural first use of this wiki inside A'Space OS.
