---
name: guide-trim-large
description: |
  Detect + split LARGE Geordi guides (> 16K chars) into head summary (≤ 5K chars)
  + body reference (path). Corrects D6 #NEW #3 context blowup. Target: reduce
  189 LARGE guides (> 16K chars, ~770K tokens combined) to manageable 5K-char
  heads + on-demand body loads.

  Triggers:
    - "trim large guides", "split guides", "compress guides"
    - "guides too big", "context blowup guide", "/guide-trim-large"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
---

# /guide-trim-large — Split LARGE Guides into Head + Body

## Why

**D6 root cause closed 2026-06-22** : 189 guides > 16K chars dans `01_Guides/`, certains jusqu'à **570K chars = 142K tokens** (`affine_deal_drafts.md`). Lecture unique = 70% du context window. **Solution** : split canonique en :
- **Head** (≤ 5K chars) : frontmatter + intro + key concepts + table of contents
- **Body** (full content, lazy-load sur demande)

## Inputs

- `target` (default "all") : `"all"` (tous les guides > 16K), `"domain:XX"`, `"path:relative/path"`
- `min_size_chars` (default 16000) : seuil pour considérer "LARGE"
- `head_size_chars` (default 5000) : taille max du head summary
- `dry_run` (default true) : si true, list candidats sans split

## Output

Pour chaque guide LARGE :
- `<guide>.head.md` (≤ 5K chars, summary canon)
- `<guide>.body.md` (full content, lazy-load)
- `<guide>.toc.md` (table of contents)

**OU** (mode dry_run) :
- Liste des guides > 16K chars avec char count + path

## Workflow

### Step 1 — D1 verify candidates (cheap)

```bash
find "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides" -name "*.md" -not -path "*_transcripts_raw*" -size +16k -exec wc -c {} \;
```

D1 receipts (2026-06-22) :
- **189 guides > 16K chars**
- Top 5 : `affine_deal_drafts.md` (570K), `YANN_CORPUS_INDEX.md` (142K), etc.

### Step 2 — Identify split points

Pour chaque guide LARGE :
- **Head** : frontmatter (YAML) + intro (1er `## ` heading) + TOC auto-généré
- **Body** : reste du contenu

### Step 3 — Generate head.md

```markdown
---
title: "[original title]"
domain: "[domain]"
original_path: "[relative path]"
original_size_chars: [N]
head_generated: 2026-06-22
status: TRIMMED_LARGE_HEAD
---

# [Title] (HEAD summary)

> Lazy-load body via `Read [original_path]` on demand.
> Original size: [N] chars ≈ [N/4] tokens.

## Key concepts

- [concept 1]: [50-100 word summary]
- [concept 2]: [50-100 word summary]
- ...

## Table of contents

- [Section 1]: line [N1]-[N2]
- [Section 2]: line [N3]-[N4]
- ...

## On-demand load

To read full content, invoke `/guide-search` or `Read <original_path>`.
```

### Step 4 — Generate body.md

```bash
cp <original> <original>.body.md
```

Body contains full content. Head contains summary.

### Step 5 — D1 verify split

```bash
wc -c <original>.head.md <original>.body.md
```

D1 receipts :
- head.md ≤ 5000 chars (per `head_size_chars` param)
- head.md + body.md ≈ original_size_chars (±100 chars for separators)

## Acceptance Criteria

| Test | Expected |
|---|---|
| `dry_run=true` | List 189 LARGE guides, no files modified |
| `target="all"` | 189 guides split, 378 new files (head + body each) |
| Head size | ≤ 5000 chars per guide |
| Original integrity | 0 modification of originals (D4 append-only) |
| Build time | ~30 min for 189 guides |
| Search via INDEX | Now shows head size instead of full body size |

## Anti-patterns interdits

- ❌ Modify original guide file (D4 violation)
- ❌ Hardcode split points (D3 nuance: derive from `## ` headings)
- ❌ Split guides < 16K chars (overhead > gain)
- ❌ Skip TOC generation (lazy-load path = user gets confused)
- ❌ Execute automatically on all LARGE guides (D7 cost-of-escalation : A0 HITL first)

## Doctrine ancrage

- **D1 verify-before-assert** : candidates list with char count, no surprises
- **D2 research-first** : Karpathy INDEX-ONLY pattern (same as CLAUDE_INDEX.md)
- **D3 nuance over literal** : head = summary NOT replacement (D4 respect)
- **D4 append-only** : original guide intact, head/body/toc as siblings
- **D5 proof not narrative** : receipt `head_size_chars ≤ 5000`
- **D6 root-cause** : D6 #NEW #3 — blowup prevention via split
- **D7 cost-of-escalation** : A0 HITL before batch split (189 files = significant change)
- **D8 cross-agent** : worktree-isolated (no concurrent edits during split)

## Cross-refs

- `/guide-search` (uses head.md for fast metadata display)
- `/guide-index-builder` (INDEX.md shows head size, not full body)
- `/guide-cross-search` (faster via head pre-filter)
- `/guide-domain-stats` (metrics reflect trim savings)
- `/context-bloat-detector` (parent skill, anti-blowup canon)

---

**Created by** : A2 Claude Code orchestrator (Phase 2 batch, 2026-06-22)
**Cycle** : 12WY Q3 2026 W3
**Doctrine** : D6 #NEW #3 anti-blowup canon