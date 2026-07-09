---
source: backfilled 2026-06-06 (hygiene lint remediation)
date: 2026-05-20
type: source
domain: ingestion
title: notebooklm_research — DEPRECATED + ARCHIVED
tags: [#source #sources #backfilled]
---

# notebooklm_research — DEPRECATED + ARCHIVED

> ⚠️ **DEPRECATED** 2026-05-20 — Merged into `notebooklm-bridge` as primary skill.
> Archived before deletion per A0 instruction.

---

## Deprecation Notice

| Field | Value |
|-------|-------|
| **Deprecated** | 2026-05-20 |
| **Reason** | Superseded by `notebooklm-bridge` (Playwright DBSC bypass) |
| **Archive date** | 2026-05-20 |
| **Archive reason** | Dead paths, no working scripts, replaced by working alternative |

---

## Why It Died

### Problem 1: Dead Paths (Critical)
```
C:\Aspace00\A0_Memory\knowledge_base\      ← PURGED 2026-03-05
C:\Aspace00\A0_Memory\youtube_archives\    ← PURGED 2026-03-05
C:\Aspace00\A0_Memory\notebooklm_pods\     ← NEVER EXISTED
```

All source paths referenced in SKILL.md point to `C:\Aspace00\A0_Memory\` which was wiped in the Great Purge of 2026-03-05. No recovery possible.

### Problem 2: Empty Scripts Directory
```
~/.skills/notebooklm_research/scripts/    ← EMPTY (0 files)
```
The skill claimed to have a `create_notebook.py` script but `scripts/` was never populated.

### Problem 3: No Public API (Structural)
Google NotebookLM has no public consumer API. The skill's "Option B (unofficial API)" was marked "Risky — May break with Google updates" — which is exactly what happened.

### Problem 4: DBSC Enforcement (Final)
Even if paths were valid and scripts existed, the `notebooklm-py` CLI fails with DBSC (Device Bound Session Credentials) errors. This is a Google-enforced security layer that binds sessions to specific browser binaries — cookie-based auth alone doesn't work.

---

## What Would Have Been Needed

For this skill to work, someone would need to:

1. [ ] Recreate the entire `C:\Aspace00\A0_Memory\` directory structure
2. [ ] Restore all knowledge_base and youtube_archives content
3. [ ] Write a working `scripts/create_notebook.py` using unofficial API
4. [ ] Maintain the unofficial API as Google updates break it
5. [ ] Implement DBSC bypass (which became `notebooklm-bridge`)

**Verdict**: Too much rework for a broken foundation. `notebooklm-bridge` solves the actual problem correctly.

---

## Replacement

| This Skill (Dead) | Replacement (Living) |
|-------------------|----------------------|
| `~/.claude/skills/notebooklm_research/` | `~/.agent/skills/notebooklm-bridge/` |
| Cookie-based auth (broken) | Playwright Chromium DBSC bypass (working) |
| Manual web upload required | `notebooklm_rpc.py list` via real browser |
| No working scripts | Full RPC bridge: list, login, screenshot |
| Dead paths to purged dirs | No path dependencies |

---

## Files Archived

```
~/.claude/skills/notebooklm_research/
├── SKILL.md                    ← THIS FILE (archived as evidence)
├── scripts/
│   └── (empty — never populated)
```

**Not archived**: Nothing else existed. This skill was a skeleton with broken references.

---

## Lesson Learned (ADR-worthy)

**Do not build skills that depend on:**
1. Paths to directories that are not the Trust Zone (`C:\Users\amado\`)
2. External services without public APIs (unless you control the API)
3. "Unofficial APIs" as production dependencies
4. Skeleton scripts promised "later"

**Instead:**
- Build against working, tested foundations
- Keep skills tightly scoped to what actually works
- Mark deprecated clearly and archive before deleting

---

## Archive Location

Original deprecated skill structure preserved (for historical record) in:
`ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/sources/skill-notebooklm_research-archived-2026-05-20.md`

This file serves as the deprecation certificate and lesson record.