---
source: LLM_Wiki_A0
date: 2026-05-10
type: schema
domain: A0_Sovereign / LLM_Wiki_Pattern
tags: [#LLM_Wiki #Knowledge_Base #A0_Amadeus #CLAUDE.md #CLAUDE_Agent]
---

# LLM Wiki — Schema (CLAUDE.md Companion)

> *"The LLM is the programmer; the wiki is the codebase."*
> — adapted from A'Space OS / LLM Wiki Pattern

This document is the **schema** that tells Claude Code how to build, maintain, and query the LLM Wiki sitting inside `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/`.

It is the counterpart to this repository's `CLAUDE.md`. While `CLAUDE.md` governs how Claude Code operates in this codebase, this schema governs how it operates as a **wiki maintainer**.

---

## The Three Layers

```
raw/          → Immutables sources (articles, PDFs, transcripts, Gemini conversations)
wiki/         → LLM-owned, LLM-written markdown pages
schema.md     → This file (CLAUDE.md companion, tells the LLM how to behave)
```

**Raw sources are sacred.** Claude Code reads them but never modifies them.

---

## Wiki Page Types

| Type | Folder | Content |
|------|--------|---------|
| **Summary** | `sources/` | One page per ingested source — key takeaways, quotes, synthesis |
| **Entity** | `entities/` | Pages for recurring actors, tools, projects, concepts |
| **Concept** | `concepts/` | Pages for cross-domain ideas, patterns, frameworks |
| **Synthesis** | `syntheses/` | Long-form pages that fuse multiple sources into a thesis |
| **Comparison** | `comparisons/` | Tables, matrices, side-by-side analyses |
| **Overview** | `wiki/index.md` | Catalog of all pages with summaries |
| **Log** | `wiki/log.md` | Chronological append-only record of ingests and queries |

---

## Workflows

### Ingest (Process a New Source)

Trigger: a new file appears in `raw/` or user asks to process a source.

```
1. Read the source in full
2. Extract key entities (people, tools, projects, concepts)
3. Write a summary page in sources/[slug].md
4. Update wiki/index.md with the new entry
5. Update or create entity pages in entities/
6. Update or create concept pages in concepts/
7. Check for contradictions with existing pages → flag in log.md
8. Append entry to wiki/log.md
9. Notify user what changed
```

A single ingest may touch 10–15 wiki pages. The LLM owns all of it.

### Query (Answer a Question)

Trigger: user asks a question.

```
1. Read wiki/index.md to find relevant pages
2. Drill into relevant pages
3. Synthesize answer
4. If answer is valuable (comparison, analysis, discovery) → file as a new wiki page
5. Cite wiki pages in answer with `wikilinks`
6. Append query + answer summary to wiki/log.md
```

### Lint (Health Check)

Trigger: user asks "run a wiki lint" or "audit the wiki".

```
1. Check for contradictions between pages
2. Flag stale claims superseded by newer sources
3. Find orphan pages (no inbound links)
4. Find important concepts with no dedicated page
5. Suggest missing cross-references
6. Report data gaps that could be filled with web search
7. Append lint report to wiki/log.md
```

---

## Naming Conventions

- **Source summaries**: `YYYY-MM-DD_slug-source-title.md`
- **Entity pages**: `entity_[name].md` (kebab-case, lowercase)
- **Concept pages**: `concept_[topic].md` (kebab-case, lowercase)
- **Syntheses**: `synthesis_[thesis-title].md`
- **Comparisons**: `compare_[A]-vs-[B].md`
- **Log entries**: `## [YYYY-MM-DD] action | Title`

Frontmatter required on every page:
```yaml
---
source: LLM_Wiki_A0
date: YYYY-MM-DD
type: summary|entity|concept|synthesis|comparison
domain: <relevant domain tag>
tags: [#relevant #tags]
---
```

---

## Cross-Referencing

Use Obsidian `wikilinks` for all cross-references. This enables the graph view and makes the wiki navigable.

- From entity to entity: `[[entity_rick]]`
- From summary to concept: `[[concept_sovereignty]]`
- From synthesis to source: `[[sources/source_gemini-takeout-2026-05]]`

---

## Log Format

Each entry in `wiki/log.md` starts with a consistent prefix for Unix-parsability:

```
## [YYYY-MM-DD] ingest    | Source Title
## [YYYY-MM-DD] query    | Question summary
## [YYYY-MM-DD] lint     | Issues found: X orphans, Y stale claims
## [YYYY-MM-DD] update   | Revised entity_X after source Y
```

Quick Unix navigation:
```bash
grep "^## \[" wiki/log.md | tail -10   # last 10 entries
grep "^## \[" wiki/log.md | grep ingest   # all ingests
```

---

## Index Format

`wiki/index.md` lists every page, organized by category:

```markdown
# LLM Wiki Index

## Sources (ingested documents)
| Date | Page | Summary | Tags |
|------|------|---------|------|
| 2026-05-10 | sources/... | One-line description | #tag |

## Entities (recurring actors, tools, projects)
| Page | Summary | Last Updated | Inbound Links |
|------|---------|-------------|-------------|
| entity_rick.md | Guardian of L0 sovereignty | 2026-05-10 | 3 |

## Concepts (cross-domain patterns)
...

## Syntheses (theses integrating multiple sources)
...

## Comparisons (matrices, tables)
...
```

---

## Tools & Integration

| Tool | Purpose |
|------|---------|
| **Obsidian** | IDE for browsing the wiki — graph view, Dataview, frontmatter queries |
| **qmd** | Local search engine (BM25 + vector) over wiki markdown files — MCP available |
| **Marp** | Slide deck generation from markdown |
| **Context7 MCP** | Web search for filling data gaps during lint |
| **Supabase MCP** | (future) pgvector semantic search over wiki content |

---

## Tips

- **Obsidian Web Clipper** converts web articles to markdown → drop in `raw/`
- Download images locally via Obsidian hotkey (Ctrl+Shift+D) → LLM can view them directly
- Good answers filed back into the wiki compound just like ingested sources
- The wiki is a git repo → version history, branching, collaboration for free
- The LLM writes and maintains all pages. You source, explore, and ask.
