---
source: LLM_Wiki_A0
date: 2026-05-10
type: concept
domain: Knowledge_Architecture / Memory_Systems
tags: [#LLM_Wiki #Knowledge_Architecture #Compounding_Knowledge #Memory_System]
---

# Concept: Compounding Knowledge

**Related terms:** persistent wiki, knowledge compilation, RAG vs. curated memory.
**See also:** [[sources/source_llm-wiki-pattern]]

---

## Definition

A knowledge system where each interaction with the system increases its value, rather than leaving it flat or degrading it. The artifact being built — the wiki — compounds over time the way a well-managed investment compounds. Every source ingested, every query answered, every lint pass run adds to a growing, cross-referenced, consistently-maintained whole.

Contrast with **extractive RAG**: each query starts from scratch. The system never builds on itself. No accumulation, no synthesis, no compounding.

---

## Why "Compounding" Is the Right Metaphor

Compound interest works because:
1. The principal (knowledge) stays in the system
2. Returns (insights, connections) are reinvested, not consumed
3. Time amplifies the base

The LLM Wiki applies all three:
1. **Principal stays:** raw sources → wiki summaries are permanent additions
2. **Returns reinvested:** good answers become new wiki pages; lint fixes update existing pages
3. **Time amplifies:** a wiki of 100 sources is more useful than 10; a wiki of 10,000 pages is a living thesis

---

## Maintenance Cost Is the Variable

The reason most personal wikis fail to compound: maintenance cost increases faster than value. Human maintainers drop off. Cross-references go stale. Syntheses contradict each other.

The LLM removes the maintenance bottleneck. It touches 15 files per ingest, updates cross-references on every update, flags contradictions automatically. The compounding curve stays positive indefinitely.


---

## Inbounds

- [[concept_compounding_knowledge]]

---

## Application to A'Space OS

| Stage | System | Compounds? |
|-------|--------|-----------|
| Raw conversation history | `Gemini_Takeout_2026/*.md` | No (static archive) |
| LLM-extracted summaries | `LLM_Wiki/wiki/sources/` | Yes |
| Entity pages | `LLM_Wiki/wiki/entities/` | Yes |
| Synthesis pages | `LLM_Wiki/wiki/syntheses/` | Yes |
| Answers filed back | `LLM_Wiki/wiki/sources/` + `comparisons/` | Yes |

The Takeout is the seed corpus. The wiki is the compound interest.
