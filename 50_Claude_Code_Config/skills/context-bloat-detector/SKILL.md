---
name: context-bloat-detector
description: |
  Measure pre-loading token cost at session start (CLAUDE.md + MEMORY.md + rules +
  ecc + skills SKILL.md descriptions). Detect blowup > 80K tokens and recommend
  archival/lazy-load/INDEX-ONLY strategies. D6 lesson shipped 2026-06-22.

  Triggers:
    - "context blowup", "pre-load too big", "tokens loaded at start"
    - "CLAUDE.md too long", "MEMORY.md bloated", "reduce pre-loading"
    - "context window full before user message", "/compact loop"
  Doctrine: A0 board observer, A1 Morty supervises, D4 append-only.
---

# /context-bloat-detector — Pre-Loading Token Cost Audit

## Why

**D6 root cause closed 2026-06-22** : Pre-loading at CC session start consumes **~139K tokens** before the first user message. This triggers `/compact` loops when the user adds any non-trivial request, because the context is already 70% full.

**Distribution measured** (2026-06-22 D1 receipts) :

| Source | Chars | Tokens (~4 c/t) | % du 200K |
|---|---|---|---|
| `MEMORY.md` | 87 458 | **21 864** | 10.9% |
| `rules/ecc/**` | 219 659 | **54 914** | 27.5% |
| Skills SKILL.md descriptions | ~188 000 | **~47 000** | 23.5% |
| `CLAUDE.md` | 35 084 | **8 771** | 4.4% |
| `rules/*.md` (racine) | 27 765 | **6 941** | 3.5% |
| **TOTAL** | **~557 966** | **~139 490** | **69.7%** |

## Inputs

None — this skill is read-only introspection.

## Output

```
=== CONTEXT BLOAT REPORT ===
CLAUDE.md: 8 771 tokens (4.4%)
MEMORY.md: 21 864 tokens (10.9%)
rules/*.md: 6 941 tokens (3.5%)
rules/ecc/**: 54 914 tokens (27.5%)
skills/ descriptions: ~47 000 tokens (23.5%)
TOTAL: 139 490 tokens (69.7% of 200K context)
REMAINING: 60 510 tokens (30.3%)

STATUS: 🚨 BLOWUP — > 60% pre-loaded before user message
```

## Workflow

### Step 1 — Measure CLAUDE.md + MEMORY.md (cheap)

```bash
wc -c "C:/Users/amado/.claude/CLAUDE.md" "C:/Users/amado/.claude/projects/c--Users-amado/memory/MEMORY.md"
```

### Step 2 — Measure rules + ecc + skills (D4 read-only)

```bash
find "C:/Users/amado/.claude/rules" -name "*.md" -not -path "*/graphify-out/*" -exec wc -c {} \;
find "C:/Users/amado/.claude/skills" -name "SKILL.md" -exec wc -c {} \;
```

### Step 3 — Compute token estimate

Sum chars, divide by 4 (typical), report as % of 200K.

### Step 4 — Recommend actions (D7 cost-of-escalation)

| Total tokens | Status | Recommendation |
|---|---|---|
| < 60K | 🟢 OK | No action needed |
| 60K-80K | 🟡 WARN | Run `/compact` if context > 80% mid-session |
| 80K-120K | 🟠 BLOWUP | Apply INDEX-ONLY pattern (CLAUDE_INDEX.md + MEMORY_INDEX.md) |
| > 120K | 🔴 CRITICAL | Archive old topics to wiki/hand_offs/, reduce SKILL.md descriptions |

## Anti-patterns interdits

- ❌ Modifier CLAUDE.md ou MEMORY.md pour réduire taille (D4 append-only)
- ❌ Hardcoder une taille fixe (les contextes CC évoluent)
- ❌ Skip la mesure réelle au profit d'une estimation (D1 verify-before-assert)
- ❌ Exécuter automatiquement `/compact` (D7 cost-of-escalation : A0 HITL)

## Doctrine ancrage

- **D1 verify-before-assert** : measure real chars, no estimation
- **D2 research-first** : distribution table D1 receipts 2026-06-22
- **D3 nuance over literal** : ~47K skills ≠ ~543K (frontmatter only injecté)
- **D4 append-only** : never delete CLAUDE.md/MEMORY.md originals, create INDEX siblings
- **D5 proof not narrative** : chars + tokens + % report
- **D6 root-cause** : 5 sources identified, ranked by token cost
- **D7 cost-of-escalation** : A0 HITL before any compression action
- **D8 cross-agent** : worktree-isolated measurement (no context contamination)

## Open follow-ups

1. **Archive old MEMORY.md topics to wiki/hand_offs/** : topics pré-2026-06-15 → canon archive
2. **Skill description trim** : shorten `description:` field for skills not used frequently
3. **Ecc lazy-load** : conditional loading via `paths:` in settings.json (if CC supports)
4. **Context-bloat cron job** : weekly report to A0 board observer
5. **Auto-compress hook** : if pre-load > 100K, suggest actions before user prompt

---

**Created by** : A2 Claude Code orchestrator (A0 escalade 2026-06-22)
**Date** : 2026-06-22
**Cycle** : 12WY Q3 2026 W3
**Doctrine** : D6 #NEW #2 — context blowup prevention canon