---
name: guide-domain-stats
description: |
  Generate observability metrics + reports for Geordi Resources guides per
  Business domain. Tracks count, char/token size, distribution (SMALL/MEDIUM/LARGE),
  top-5 largest guides, growth delta (vs previous run), anti-blowup D6 #NEW #3
  metrics. Use to monitor context bleed risk over time.

  Triggers:
    - "guide stats", "domain metrics", "geordi observability"
    - "guide distribution", "size analysis", "growth delta"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
---

# /guide-domain-stats — Geordi Resources Observability + Metrics

## Why

**D6 root cause closed 2026-06-22** : 1067 guides × 3.08M tokens = context blowup. **Observability** = monitor size distribution over time, detect regressions, validate `/guide-trim-large` savings.

## Inputs

- `target` (default "all") : `"all"`, `"global"`, `"domain:XX"`
- `compare_to_previous` (default false) : if true, compute growth delta
- `format` (default `"table"`) : `"table"`, `"json"`, `"markdown"`

## Output

```
=== GEORDI STATS — 2026-06-22 ===

| Domain | Guides | Chars | Tokens | SMALL | MEDIUM | LARGE | Status |
|---|---|---|---|---|---|---|---|
| 00_KERNEL_OS | 0 | 0 | 0 | 0 | 0 | 0 | 🟢 |
| 01_Product | 10 | 134K | 33K | 2 | 7 | 1 | 🟢 |
| 02_Ops | 28 | 214K | 53K | 5 | 20 | 3 | 🟢 |
| 03_IT | 344 | 2.67M | 666K | 22 | 234 | 88 | 🔴 BLOATED |
| 04_Finance | 43 | 609K | 152K | 4 | 30 | 9 | 🟡 |
| 05_Legal | 10 | 144K | 36K | 1 | 7 | 2 | 🟢 |
| 06_Sales | 37 | 554K | 138K | 6 | 23 | 8 | 🟡 |
| 07_Growth | 74 | 917K | 229K | 8 | 51 | 15 | 🟡 |
| 08_People | 36 | 311K | 78K | 5 | 25 | 6 | 🟢 |
| 09_Life_OS | 32 | 231K | 58K | 4 | 22 | 6 | 🟢 |
| _TRASH (archive) | 13 | 35K | 9K | - | - | - | ⚪ ARCHIVE |
| **TOTAL** | **1067** | **12.3M** | **3.08M** | **57** | **739** | **189** | - |

Top 5 LARGE guides:
1. `affine_deal_drafts.md` — 570K chars (142K tokens)
2. `YANN_CORPUS_INDEX.md` — 142K chars (35K tokens)
3. `affine_deal_drafts.md` (Yann_Leonardi/) — 93K chars (23K tokens)
4. `IT_CHANNELS_BULK_AUDIT.md` — 64K chars (16K tokens)
5. `resource_gaza_guerre_information_blast_2024.md` — 30K chars (7.5K tokens)

Distribution:
- SMALL (< 6K chars): 57 guides (5.3%) — SAFE
- MEDIUM (6K-16K): 739 guides (69.3%) — MODERATE risk
- LARGE (> 16K): 189 guides (17.7%) — DANGER (use /guide-trim-large)
- > 100K (outliers): 4 guides — CRITICAL

Growth delta (vs 2026-06-15):
- Total chars: +8.2% (12.3M vs 11.4M)
- Total guides: +12 (1067 vs 1055)
- New domain: (none)
- New LARGE guides: +7 (>16K threshold)

D6 #NEW #3 anti-blowup recommendations:
- 189 LARGE guides → run `/guide-trim-large` to reduce by 80% (770K tokens → 154K)
- After trim: total tokens 3.08M → 2.46M (potential 20% reduction)
- For acute blowup risk: trim top 10 first (largest tokens saved)
```

## Workflow

### Step 1 — D1 verify scope (cheap)

```bash
find "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides" -maxdepth 1 -type d
```

D1 receipts : 9 domain subdirs canon + 1 archives + 1 transcripts_raw

### Step 2 — Per-domain stats (D1 receipts)

For each domain, compute:
- Count of guides (excluding _transcripts_raw + _TRASH)
- Total chars
- Token estimate (chars / 4)
- Distribution buckets: SMALL (< 6K), MEDIUM (6K-16K), LARGE (> 16K)

### Step 3 — Top 5 LARGE guides (outliers)

```bash
find "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides" -name "*.md" -not -path "*_transcripts_raw*" -exec wc -c {} \; | sort -rn | head -5
```

### Step 4 — Growth delta (optional)

If `compare_to_previous=true`, load previous stats from `wiki/hand_offs/geordi_stats_<PREV_DATE>.json` and compute delta.

### Step 5 — D6 recommendations

Based on distribution, suggest actions:
- 189 LARGE guides → run `/guide-trim-large`
- 03_IT domain BLOATED (666K tokens) → consider sub-categorization
- _TRASH archives → consider hard delete (D7 cost-of-escalation : A0 HITL)

## Acceptance Criteria

| Test | Expected |
|---|---|
| `target="all"` | Report covers all 11 subdirs + total |
| Char count per domain | ≥ 0, sum matches TOTAL |
| Bucket distribution | SMALL + MEDIUM + LARGE = TOTAL guides |
| Top 5 LARGE | sorted by char count desc, top 5 listed |
| Growth delta | computed vs previous run if available |
| Output format | table (default), json, markdown |

## Anti-patterns interdits

- ❌ Hardcode domain list (D3 nuance: read dynamically from disk)
- ❌ Include `_transcripts_raw/` in stats (these are raw, not guides)
- ❌ Skip LARGE guides distribution (D6 #NEW #3 anti-blowup metric)
- ❌ Auto-archive LARGE guides without A0 HITL (D7 cost-of-escalation)
- ❌ Suggest `/guide-trim-large` batch without confirmation (189 files = significant change)

## Doctrine ancrage

- **D1 verify-before-assert** : real-time wc -c + bucket count, no estimation
- **D2 research-first** : Karpathy observability pattern (periodic metrics snapshots)
- **D3 nuance over literal** : 9 domain subdirs + 1 archives (pas 8 — 00_KERNEL_OS vide)
- **D4 append-only** : stats report saved as `<DATE>_geordi_stats.md` (no overwrite)
- **D5 proof not narrative** : receipts chars + tokens + bucket counts
- **D6 root-cause** : D6 #NEW #3 — anti-blowup metrics tracking
- **D7 cost-of-escalation** : A0 HITL before any `/guide-trim-large` batch
- **D8 cross-agent** : worktree-isolated stats computation

## Cross-refs

- `/guide-search` (consumes stats for context-aware queries)
- `/guide-index-builder` (uses stats for INDEX size estimate)
- `/guide-trim-large` (recommended by stats for LARGE guides)
- `/guide-cross-search` (uses stats for cross-domain distribution)
- `/context-bloat-detector` (parent skill, anti-blowup canon)
- `wiki/hand_offs/geordi_stats_<DATE>.md` (historical snapshots)

---

**Created by** : A2 Claude Code orchestrator (Phase 2 batch, 2026-06-22)
**Cycle** : 12WY Q3 2026 W3
**Doctrine** : D6 #NEW #3 anti-blowup observability canon