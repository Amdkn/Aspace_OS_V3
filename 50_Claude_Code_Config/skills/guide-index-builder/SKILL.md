---
name: guide-index-builder
description: |
  Generate canonical INDEX.md per domain (8 Business subdirs) + INDEX.md global
  cross-domain. Each guide = 1-line hook (title + path + summary + tags).
  Lazy-load pattern: agents read INDEX instead of full 1067 guides. Prevents
  context bleed by reducing pre-load from 3M tokens to ~50K (INDEX-only).

  Triggers:
    - "build guide index", "INDEX.md guides", "geordi index"
    - "lazy-load guides", "geordi index rebuild", "/INDEX.md creation"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
---

# /guide-index-builder — Geordi Resources INDEX Generator

## Why

**D6 root cause closed 2026-06-22** : 1067 guides × 3.08M tokens = context blowup. **INDEX-ONLY pattern** : un fichier INDEX.md par domain avec 1-line hooks → agent lit l'INDEX (50K tokens) au lieu de full guides (3M tokens).

**Réduction** : **3.08M → ~50K tokens = -98.4%** (par lazy-load canon).

## Inputs

- `target` (default "all") : `"all"` (8 INDEX.md), `"global"` (1 INDEX global), `"domain:XX"` (1 INDEX domain spécifique)
- `force_rebuild` (default false) : si true, écrase les INDEX existants

## Output

Pour chaque domain target :
- `01_Guides/<DOMAIN>/INDEX.md` avec table 1-line hooks
- Format : `| # | Path | Title | Tags | Date | Chars |`

Pour global :
- `01_Guides/INDEX.md` avec table cross-domain summary

## Workflow

### Step 1 — D1 verify scope (cheap)

```bash
find "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides" -maxdepth 1 -type d -not -path "*_transcripts_raw*" -not -path "*_TRASH*"
```

D1 receipts :
- 9 domain subdirs canon : 00_KERNEL_OS (vide), 01_Product, 02_Ops, 03_IT, 04_Finance, 05_Legal, 06_Sales, 07_Growth, 08_People, 09_Life_OS

### Step 2 — Per-domain extraction (cheap)

Pour chaque domain, extraire frontmatter de tous les guides :
```bash
for f in 01_Guides/<DOMAIN>/*.md; do
  frontmatter=$(awk '/^---$/{c++; if(c==2) exit} c>=1' "$f")
  title=$(echo "$frontmatter" | grep "^title:" | head -1)
  tags=$(echo "$frontmatter" | grep "^tags:")
  ...
done
```

### Step 3 — Generate INDEX.md per domain

```markdown
# INDEX — 04_Finance/

> Generated 2026-06-22 by `/guide-index-builder`. Total: 43 guides, 152K chars.

| # | Path | Title | Tags | Date | Chars |
|---|---|---|---|---|---|
| 1 | `saru_finance_strategy.md` | Saru quarterly runway review H3 | saru, h3, ld02 | 2026-06-15 | 8K |
| 2 | `saru_antipaperclip_doctrine.md` | Anti-paperclip maximizer doctrine | saru, rick, anti-paperclip | 2026-06-21 | 12K |
| ... |
```

### Step 4 — Generate global INDEX.md (cross-domain)

```markdown
# INDEX — Geordi Resources (Global)

> Generated 2026-06-22. Total: 1067 guides, 3.08M chars ≈ 770K tokens.

| Domain | Guides | Chars | Tokens | INDEX path |
|---|---|---|---|---|
| 01_Product | 10 | 134K | 33K | 01_Product/INDEX.md |
| 02_Ops | 28 | 214K | 53K | 02_Ops/INDEX.md |
| 03_IT | 344 | 2.67M | 666K | 03_IT/INDEX.md |
| ... |
| **TOTAL** | **1067** | **12.3M** | **3.08M** | 10 INDEX.md |
```

### Step 5 — D1 verify INDEX size

```bash
wc -l 01_Guides/INDEX.md 01_Guides/04_Finance/INDEX.md ...
```

D1 receipts :
- Global INDEX : ~50 lines ≈ 1.5K tokens (vs 3.08M full = -99.95% reduction)
- Per-domain INDEX : ~30-200 lines ≈ 1K-5K tokens each

## Acceptance Criteria

| Test | Expected |
|---|---|
| `target="all"` | 10 INDEX.md created (1 global + 9 domain) |
| Global INDEX size | ≤ 2K tokens (vs 3.08M full = -99.95%) |
| Per-domain INDEX size | ≤ 5K tokens each |
| INDEX.md format | table canon 1-line hooks |
| Build time | < 30 sec for all 1067 guides |
| D4 append-only | 0 modification of original guides |

## Anti-patterns interdits

- ❌ Include full guide content in INDEX (defeats purpose, blowup)
- ❌ Modify original guides during INDEX build (D4 violation)
- ❌ Skip domain directories (incomplete coverage)
- ❌ Hardcode guides list (D3 nuance: read dynamically from disk)
- ❌ Build INDEX without `awk` frontmatter extraction (would read full files = blowup)

## Doctrine ancrage

- **D1 verify-before-assert** : char count after INDEX build (sanity check)
- **D2 research-first** : Karpathy INDEX-ONLY pattern (same as CLAUDE_INDEX.md / MEMORY_INDEX.md)
- **D3 nuance over literal** : 9 domain subdirs canon (pas 8 — 00_KERNEL_OS vide mais existe)
- **D4 append-only** : INDEX files créés, guides originaux intacts
- **D5 proof not narrative** : receipt `wc -l INDEX.md` = canon size
- **D6 root-cause** : D6 #NEW #3 — blowup prevention via lazy-load
- **D7 cost-of-escalation** : A0 HITL for `force_rebuild=true` (D4 append-only risk)
- **D8 cross-agent** : worktree-isolated INDEX build, no concurrent edits

## Cross-refs

- `/guide-search` (uses INDEX for fast queries)
- `/guide-trim-large` (split LARGE guides before INDEX)
- `/guide-cross-search` (compound cross-domain search)
- `/guide-domain-stats` (observability + size metrics)
- `CLAUDE_INDEX.md` + `MEMORY_INDEX.md` (sister INDEX-ONLY siblings)

---

**Created by** : A2 Claude Code orchestrator (Phase 2 batch, 2026-06-22)
**Cycle** : 12WY Q3 2026 W3
**Doctrine** : D6 #NEW #3 anti-blowup canon