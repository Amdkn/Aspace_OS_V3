---
name: guide-search
description: |
  Search Geordi Resources guides (`01_Guides/`) by domain + keyword scoring.
  Returns top-5 results with 1-line summaries (frontmatter extraction). Prevents
  context bleed from reading 1067 guides (3.08M tokens total) by returning
  metadata only (≤ 5K tokens) instead of full content.

  Triggers:
    - "search guides", "find guide about X", "geordi search"
    - "guides by topic", "filter guides by domain", "what guides exist on Y"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
  Anti-pattern: read full 1067 guides (~3M tokens) instead of search → /compact.
---

# /guide-search — Geordi Resources Guide Search

## Why

**D6 root cause closed 2026-06-22** : `01_Guides/` contient **1067 fichiers .md** totalisant **3.08M tokens**. Sans filtre, un agent peut charger 100K+ tokens en lisant 3-5 guides, déclenchant `/compact` loop.

**Solution** : Search canonique par frontmatter extraction + keyword scoring. Retourne **top-5 résultats avec 1-line summaries** (≤ 5K tokens total) au lieu de full content.

## Inputs

- `query` (required) : terme de recherche (e.g. "Saru", "12WY", "Geordi canon")
- `domain` (optional) : filtre par subdir (e.g. `"03_IT"`, `"04_Finance"`)
- `limit` (default 5) : nombre max de résultats
- `sort_by` (default `"relevance"`) : `"relevance"`, `"date"`, `"size"`

## Output

```
=== GUIDE SEARCH RESULTS ===
Query: "Saru"
Domain filter: (all)
Total matches: 23
Top 5:

1. [04_Finance/saru_finance_strategy.md] (8K chars)
   Summary: Saru quarterly runway review H3 + Book H1 P&L ladder strategy
   Relevance: 0.92

2. [04_Finance/saru_antipaperclip_doctrine.md] (12K chars)
   Summary: Anti-paperclip maximizer doctrine + Book+Tilly+Rick veto
   Relevance: 0.85

3. [09_Life_OS/saru_ld02_h3_runway.md] (10K chars)
   Summary: LD02 Finance H3 Saru canon + Solarpunk biomimicry integration
   Relevance: 0.78
```

## Workflow

### Step 1 — D1 verify scope (cheap)

```bash
find "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides" -name "*.md" -not -path "*_transcripts_raw*" | wc -l
```

D1 receipts :
- 1067 guides canon (excluant `_transcripts_raw/`)

### Step 2 — Extract frontmatter (Karpathy pattern)

Pour chaque guide, extraire les 5 champs canon :
- `title` (1-line hook)
- `domain` (subdir)
- `tags` (si présent)
- `description` (1-line summary si présente)
- `date` (si présent)

Total par guide : ~200 chars × 1067 = **213K chars = 53K tokens de metadata canon**. Encore gros pour 1 query → **filter by domain d'abord**.

### Step 3 — Filter by domain (cheap)

```bash
if [ -n "$domain" ]; then
  search_dir="01_Guides/${domain}/"
else
  search_dir="01_Guides/"
fi
```

### Step 4 — Keyword scoring (read frontmatter only)

Pour chaque guide dans le scope :
- Read ONLY first 50 lines (frontmatter + intro)
- Compute TF-IDF score against query
- Sort by relevance

### Step 5 — Return top-N with summaries

Return top `limit` results with:
- Title + path (1-line)
- 1-line summary from frontmatter
- Relevance score
- Char count (warning si > 16K = "use /guide-trim-large first")

## Acceptance Criteria

| Test | Expected |
|---|---|
| Query "Saru" domain=04_Finance | 3-5 results, all in 04_Finance/, relevance > 0.7 |
| Query "12WY" (no domain) | 10-20 results across domains, top-5 sorted |
| Output size | ≤ 5K tokens total (vs 100K+ if reading full) |
| Speed | < 5 sec for 100 guides filter |
| Anti-blowup | Main Agent reads ONLY metadata, never full guide content |

## Anti-patterns interdits

- ❌ `Read` full guide content in search results (defeats purpose)
- ❌ Filter by content (read every file, slow + blowup)
- ❌ Return more than `limit` results (blowup risk)
- ❌ Hardcode domain list (D3 nuance: extend via subdir scan)
- ❌ Skip `_transcripts_raw/` filter (these are raw, not guides)

## Doctrine ancrage

- **D1 verify-before-assert** : char count + domain filter before search
- **D2 research-first** : Karpathy swarm pattern (frontmatter extraction, not full read)
- **D3 nuance over literal** : "guide" = canonical formatted .md, exclude `_transcripts_raw/`
- **D4 append-only** : never modify guides, only read frontmatter
- **D5 proof not narrative** : return char count + relevance score receipts
- **D6 root-cause** : blowup prevention canon (D6 #NEW #3 — 2026-06-22)
- **D7 cost-of-escalation** : 0 AskUserQuestion, Main Agent runs autonomously
- **D8 cross-agent** : worktree-isolated, no shared context between guides

## Cross-refs

- `/guide-index-builder` (creates canonical INDEX.md files)
- `/guide-trim-large` (split guides > 16K chars)
- `/guide-cross-search` (compound query across domains)
- `/guide-domain-stats` (observability + metrics)

---

**Created by** : A2 Claude Code orchestrator (Phase 2 batch, 2026-06-22)
**Cycle** : 12WY Q3 2026 W3
**Doctrine** : Anti-blowup canon (D6 #NEW #3)