---
session: agent-a84a25d8fcb3f288a
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\441d3dbe-6b5b-4f20-a37b-9f8ca8e44bbe\subagents\agent-a84a25d8fcb3f288a.jsonl
debut: 2026-07-31T21:15:17.807Z
fin: 2026-07-31T21:28:36.564Z
messages_utilisateur: 1
reponses_assistant: 11
titre: "You are fixing the **5 Important findings** from the final whole-branch review of the Cognition Memory Unifica…"
---

## >>> UTILISATEUR #1

You are fixing the **5 Important findings** from the final whole-branch review of the Cognition Memory Unification work. Current HEAD: `1b6e8d4`. Your fixes will land as a single new commit on top.

## Context

Sister spec: `ASpace_OS_V2/docs/superpowers/specs/2026-07-31-cognition-unification-design.md` (READ §2.5 + §5 + §9).

35 tests currently passing across 4 scripts:
- `walk_scatter_sources.py` (Task 2, fix `7671365`)
- `classify_via_b1.py` (Task 3, fix `e5b55be`)
- `migrate_with_sha256.py` (Task 4, style `bda3662`)
- `verify_migration.py` (Task 5)

Working dir: `C:/Users/amado/ASpace_OS_V2/`.

## Findings to Fix (all 5 — Important, not Critical)

### F1 — Collision suffix MUST be source-content-hash (not basename-hash)

**File**: `scripts/cognition/migrate_with_sha256.py` line 85

**Current**:
```python
suffix_hash = hashlib.sha256(base_name.encode()).hexdigest()[:8]
```

**Problem**: Two files with same basename (e.g. `doc.md` from `_specs` AND `wiki`) collide because `base_name.encode()` is not source-unique.

**Fix**:
```python
suffix_hash = hashlib.sha256(src_sha.encode()).hexdigest()[:8]
```

Use `src_sha` which is already computed at line 110 (re-hash of source). The hash MUST be source-content-derived, not basename-derived.

### F2 — Walker must apply per-bucket scope (non-recursive + date pattern for daily_note)

**File**: `scripts/cognition/walk_scatter_sources.py` line 33

**Current**: `for p in source.rglob("*.md"):` — recursive walk.

**Problem**: `00_Amadeus/30_MEMORY_CORE/` has 23,709 nested files (Obsidian vault + Claude Export + sessions) inflating `daily_note` from spec ~297 → 23,709.

**Fix**: Add a per-bucket glob policy. The walker needs to know the bucket type to choose:
- `adr` (`_SPECS/ADR/**`): recursive OK (hierarchical doctrine)
- `handoff` (`wiki/hand_offs/**`): recursive OK (flat, but defensive)
- `draft` (`_DRAFTS_PPR_LANE/**`): recursive OK
- `daily_note` (`00_Amadeus/30_MEMORY_CORE/**`): **non-recursive only + filter `YYYY-MM-DD.md`** per spec §2.5
- `early_canon` (`00_Amadeus/04_Digital_Memory/Archives/_SPECS/**`): recursive OK
- `forensic` (`_TRASH_*/**`): recursive OK

Implementation: extend `_walk_dir(source, source_type)` to take `source_type` and apply the policy. For `daily_note`:
```python
# Non-recursive + date pattern
for p in source.glob("*.md"):  # not rglob
    if not re.match(r"\d{4}-\d{2}-\d{2}\.md$", p.name):
        continue  # skip non-date-named files
    entries.append({...})
```

Also extend the default extensions to `*.{md,jsonl,tsv,txt}` per spec §2.5 PPR drafts bucket. Make the extension list configurable per-bucket.

### F3 — Walk→migrate SHA mismatch abort (spec §5)

**File**: `scripts/cognition/migrate_with_sha256.py` line 110-112

**Current**:
```python
src_sha = compute_sha256(src_path)
```

**Problem**: Spec §5 mandates: "Source file modifié entre walk et migrate → Re-calculate SHA256, abort si mismatch (D1 verify)". The recompute exists but is never compared to `entry["sha256"]` from walk.

**Fix**: After computing `src_sha`, compare to `entry["sha256"]`. If mismatch, raise a clear error and abort the batch (or skip with a logged warning — pick ONE consistent policy).

```python
src_sha = compute_sha256(src_path)
if src_sha != entry["sha256"]:
    raise RuntimeError(
        f"SHA mismatch for {src_path}: walk={entry['sha256'][:8]}... migrate={src_sha[:8]}... "
        f"Source modified between walk and migrate. Re-run walk first."
    )
```

Add a test: `test_migrate_aborts_on_sha_mismatch` that pre-modifies a file between walk output generation and migrate invocation.

### F4 — Content size filter (spec §9)

**File**: `scripts/cognition/walk_scatter_sources.py` (after extension filter)

**Problem**: Spec §9 says "Filtre : *.md avec content > 100 chars (sinon skip)". Empty/stub files bloat the index.

**Fix**: Add a content-length check after reading. For each candidate, read first 200 chars; if total content is ≤ 100 chars (or file is empty), skip with a logged warning.

```python
content = p.read_text(encoding="utf-8", errors="ignore")
if len(content.strip()) <= 100:
    continue  # skip stub files
```

Add a test: `test_walk_skips_stub_files` that creates a file with content `<= 100 chars` and verifies it's not in the entries.

### F5 — Daily_note non-recursive walker test

**File**: `tests/test_walk_scatter_sources.py`

**Add**: A test that creates a `30_MEMORY_CORE/` directory with:
- A `2026-07-20.md` file (matches date pattern) — should be included as `daily_note`
- A nested `vault/sub-note.md` file — should be EXCLUDED (non-recursive)
- A `not-a-date.md` file (no date pattern) — should be EXCLUDED

## Your Job

1. **Read** current `walk_scatter_sources.py` and `migrate_with_sha256.py`.
2. **Apply F1, F2, F3, F4 fixes**.
3. **Add tests** for F2 (daily_note scope), F3 (SHA mismatch abort), F4 (stub filter).
4. **Run RED→GREEN TDD** for each new test.
5. **Run full cognition suite** — must all pass (target 38+ tests).
6. **Commit** with message: `fix(cognition): pre-live hardening (collision hash, daily_note scope, SHA mismatch abort, stub filter)`
7. **Self-review**.
8. **Write full report** to `C:/Users/amado/.superpowers/sdd/final-fix-report.md`.
9. **Report back**.

## Tests Required

| Test name | Verifies |
|---|---|
| `test_walk_daily_note_non_recursive` | F2: `30_MEMORY_CORE/2026-07-20.md` included; nested `vault/sub.md` excluded |
| `test_walk_daily_note_filters_non_date_files` | F2: `30_MEMORY_CORE/notadate.md` excluded |
| `test_walk_skips_stub_files` | F4: content `<= 100 chars` excluded |
| `test_walk_includes_draft_extensions` | F2/F5: `.jsonl`/`.tsv` files in `_DRAFTS_PPR_LANE` included as `draft` |
| `test_migrate_aborts_on_sha_mismatch` | F3: source modified between walk & migrate → RuntimeError |
| `test_migrate_collision_uses_source_sha` | F1: two files same basename → distinct suffixes derived from source SHA |

## Code Organization

Keep `walk_scatter_sources.py` focused. Per-bucket policy is a function-level concern, not a class. Update `_walk_dir` signature to accept `source_type`.

## Self-Review

- All 6 new tests RED→GREEN verified?
- Full suite (target 38+ tests) passing?
- No regression in existing 35 tests?
- F1-F5 ALL applied?
- Commit message clean?

## Report Format

Write to `C:/Users/amado/.superpowers/sdd/final-fix-report.md`:
- Fixes applied (F1-F5 mapped to file:line changes)
- TDD RED→GREEN evidence
- New test count + total passing count
- Files changed
- Self-review findings
- Concerns

Report back with ONLY:
- **Status:** DONE | DONE_WITH_CONCERNS | BLOCKED
- Commits (short SHA + subject)
- One-line test summary (e.g. "41/41 passing, output pristine")
- Concerns
- Report file path

### assistant

Now I'll write the new test file with all 6 RED tests:

### assistant

Now let me run the new tests to confirm they're RED:

### assistant

All 6 tests are RED as expected. Now let me apply the fixes. First, I'll fix `walk_scatter_sources.py` with F2 and F4:

### assistant

Walker tests GREEN. Now F1 + F3 fixes to `migrate_with_sha256.py`:

### assistant

Now let's run the migrate tests:

### assistant

Now let me rewrite the F1 test with correct semantics (both files must collide):

### assistant

All 6 new tests GREEN. Let me run the full suite to confirm no regressions:

### assistant

The stub filter breaks existing tests because their fixture files have content < 100 chars. I need to update the fixture to comply with the new policy:

### assistant

All 41 tests pass (35 existing + 6 new). Let me do a quick self-review of the changed files, then commit:

### assistant

Commit landed. Now writing the final report:

### assistant

**Status:** DONE

**Commit:** `b2c84e6` — fix(cognition): pre-live hardening (collision hash, daily_note scope, SHA mismatch abort, stub filter)

**Tests:** 41/41 passing (35 prior + 6 new), output pristine

**Concerns:**
1. Stub filter is global — could drop legitimate small files in `_DRAFTS_PPR_LANE` (mitigated by tunable constant `STUB_CONTENT_MIN_CHARS`)
2. F3 aborts the batch but does not roll back already-migrated entries (per spec §5 — reversal via `_TRASH_*` ledger)
3. `_BUCKET_RECURSIVE` defaults `True`, so new bucket types must explicitly choose recursion policy (no silent fall-through; explicit > implicit)

**Report file:** `C:/Users/amado/.superpowers/sdd/final-fix-report.md`
