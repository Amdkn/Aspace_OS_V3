---
name: guide-cross-search
description: |
  Compound cross-domain search across Geordi guides (multiple keywords + domain
  filters + semantic expansion). Returns ranked results with relevance score.
  Use when query spans multiple Business domains (e.g. "Saru + Book + 12WY"
  needs LD02 Finance + LD01 Business + 12WY frameworks).

  Triggers:
    - "cross-domain search", "compound query guides", "multi-domain search"
    - "Saru AND Book", "guides about X AND Y", "cross-search geordi"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
---

# /guide-cross-search — Compound Cross-Domain Guide Search

## Why

**D6 root cause closed 2026-06-22** : simple `/guide-search` uses single keyword + domain filter. Complex queries (e.g. "Saru + Book + 12WY integration") require multi-keyword semantic matching across multiple Business domains.

**Solution** : compound query parser + semantic expansion (synonyms, related concepts) + cross-domain scoring.

## Inputs

- `query` (required) : compound query string (e.g. `"Saru + Book + 12WY integration"`)
- `keywords` (optional, auto-parsed) : list of keywords extracted from query
- `semantic_expansion` (default true) : if true, expand keywords with related concepts
- `domain_filter` (default "all") : `"all"` or `"03_IT,04_Finance"` (comma-separated)
- `limit` (default 10) : max results
- `sort_by` (default `"compound_relevance"`) : `"compound_relevance"`, `"cross_domain_spread"`

## Output

```
=== CROSS-DOMAIN SEARCH RESULTS ===
Query: "Saru + Book + 12WY integration"
Keywords (auto-parsed): [saru, book, 12wy, integration]
Semantic expansion: [saru→ld02+finance+h3+runway+antipaperclip], [book→ld01+business+h1+pnl+trade], [12wy→12weekyear+w3+w6+rocks]
Domain filter: (all)
Cross-domain spread: 4/8 domains covered

Top 10:

1. [04_Finance/saru_book_h1pnl_integration.md] (10K chars)
   Score: 0.94 | Domains: 04_Finance, 01_Product
   Saru H3 quarterly runway + Book H1 weekly P&L integration strategy

2. [07_Growth/w3_w6_solarpunk_business.md] (12K chars)
   Score: 0.81 | Domains: 07_Growth, 04_Finance
   12WY Q3 2026 W3-W6 Solarpunk business model integration

3. [09_Life_OS/saru_book_12wy_doctrine.md] (8K chars)
   Score: 0.88 | Domains: 09_Life_OS, 04_Finance
   LD02 Saru + Book + 12WY doctrine convergence canon

... (7 more)
```

## Workflow

### Step 1 — Parse compound query

Extract keywords from query string (split on `+`, `,`, `and`, `&`).

```python
query = "Saru + Book + 12WY integration"
keywords = ["saru", "book", "12wy", "integration"]
```

### Step 2 — Semantic expansion (optional)

For each keyword, expand with related concepts from canon A'Space:

| Keyword | Expanded concepts |
|---|---|
| `saru` | ld02, finance, h3, quarterly, runway, antipaperclip |
| `book` | ld01, business, h1, weekly, pnl, trade, energy, economics |
| `12wy` | 12weekyear, w1-w12, rocks, tactics, pike, una, morty, snw, life-wheel |
| `integration` | bridge, sync, cerritos, morty, beth, alignment |

### Step 3 — Cross-domain filter (cheap)

```bash
if [ -n "$domain_filter" ]; then
  search_dirs=$(echo "$domain_filter" | tr ',' '\n' | xargs -I{} echo "01_Guides/{}")
else
  search_dirs="01_Guides/*/"
fi
```

### Step 4 — Score guides across all expanded keywords

For each guide in scope:
- Read ONLY frontmatter + first 100 lines
- Score = sum of keyword hits × domain spread bonus
- Rank by `score` desc

### Step 5 — Apply cross-domain spread bonus

Guide spanning multiple domains (e.g. mentioned in 04_Finance + 09_Life_OS) scores higher than single-domain guide.

### Step 6 — Return top-N

Return top `limit` results with:
- Title + path
- Score
- Domains covered
- 1-line summary

## Acceptance Criteria

| Test | Expected |
|---|---|
| Query "Saru + Book + 12WY" | Top results span 3-4 domains |
| Compound vs single | Cross-search score > 2× single-keyword score for matches |
| Semantic expansion | "saru" matches guides mentioning "LD02" or "Finance H3" |
| Cross-domain bonus | Multi-domain guide > single-domain guide at equal keyword hit |
| Output size | ≤ 10K tokens (vs 50K+ if reading full cross-domain guides) |

## Anti-patterns interdits

- ❌ Read full guide content in search results (blowup)
- ❌ Parse keywords without semantic expansion (misses related guides)
- ❌ Ignore domain spread bonus (defeats cross-domain purpose)
- ❌ Hardcode keyword mappings (D3 nuance: derive from canon)
- ❌ Skip frontmatter extraction (slow + inconsistent results)

## Doctrine ancrage

- **D1 verify-before-assert** : char count + cross-domain spread receipts
- **D2 research-first** : semantic expansion from canon A'Space (LDxx + twins + 12WY)
- **D3 nuance over literal** : "Saru" → also matches "LD02" + "Finance H3" + "antipaperclip"
- **D4 append-only** : never modify guides, only read frontmatter
- **D5 proof not narrative** : score + domain spread + char count receipts
- **D6 root-cause** : D6 #NEW #3 — blowup prevention via compound search
- **D7 cost-of-escalation** : A0 HITL if semantic expansion false positives
- **D8 cross-agent** : worktree-isolated search

## Cross-refs

- `/guide-search` (sister skill — single keyword search)
- `/guide-index-builder` (uses INDEX for fast metadata)
- `/guide-trim-large` (split LARGE guides before cross-search)
- `/guide-domain-stats` (observability + metrics)
- `/context-bloat-detector` (parent skill, anti-blowup canon)
- A'Space canon : AGENTS.md §"Layer 1 Life OS Fleet" (8 LDxx + twins)

---

**Created by** : A2 Claude Code orchestrator (Phase 2 batch, 2026-06-22)
**Cycle** : 12WY Q3 2026 W3
**Doctrine** : D6 #NEW #3 anti-blowup canon + cross-domain semantic expansion