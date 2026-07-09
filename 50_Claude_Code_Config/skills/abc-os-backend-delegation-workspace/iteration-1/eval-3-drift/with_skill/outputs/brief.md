---
brief_id: A3-eval-3-doc-seed-drift-reconcile
issued_by: A2 (Claude Code orchestrator)
issued_to: A3 (sub-agent, general-purpose)
issued_at: 2026-06-12
eval: eval-3-drift (reconcile-doc-seed-drift)
skill: abc-os-backend-delegation
target_file: ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md (P3 section)
doctrine_anchors: ADR-META-001 (D1 Verify-Before-Assert, D3 Nuance over Literal, D4 No self-contradiction), ADR-ABCOS-001 (D5 mixed-tenancy, D10 build_hub_v2 coexistence)
precedent: 2026-06-12 build_hub_v2 apply (P3 section, 12 migrations, 17 tables, 42 RLS, FORCE_TARGET=1)
---

# A2-to-A3 Brief — Doc/Seed Drift Reconciliation (eval-3-drift)

## TASK

Reconcile the 3 known doc/seed drifts in the P3 section of `handoff_abc_os_community_dev_2026-06-10.md` so the docs match the actual `abc_os` schema on the VPS. The schema and seed files are CORRECT — only the handoff doc is wrong. Adapt the doc to the schema (D3), do NOT adapt the schema to the doc.

**A0's intent (verbatim, from eval prompt)**: "Reconcile the docs to match the actual schema. First run a verification query against abc_os on the VPS to confirm the actual state of these 3 things. Then edit the handoff file to use the correct names/ids. Write back to wiki/log.md noting the reconciliation. Do NOT touch the schema or seed files — only the docs."

**The 3 drift items** (all in the P3 section, around lines 705-717 + the Spot-checks block around lines 679-683):

| # | Doc claim (WRONG) | Actual reality (CORRECT) |
|---|-------------------|---------------------------|
| 1 | Column `name` on `build_projects` | Column is **`title`** |
| 2 | Phase id `complete-offgrid-system-p1` | Phase id is **`og-p1`** (shorter id, prefix per project) |
| 3 | Category id `self-sufficiency` | Category id is **`homesteading`** (real category name in TS) |

---

## DOCTRINE ANCHORS (cite at the top of your reply to A2)

- **D1 Verify-Before-Assert** (ADR-META-001): prove with observed query output, never assert. The 3 verification queries below are the receipts — run them, capture the raw output, include the raw rows in your report. If a query returns an empty result, that is a different drift (not this one); stop and escalate to A2.
- **D3 Nuance over Literal** (ADR-META-001): doc/seed drift is real. The seed faithfully ports the actual `buildData.ts` structure, not the Antigravity-idealized doc. **Adapt the docs to the schema, not the reverse.** Do not refuse the edits because "the doc came first" — the doc is wrong, the schema is right.
- **D4 No self-contradiction**: do not report "reconciled" if any verify count is off or any Edit fails the `old_string` match.
- **D5 + D10 Mixed-tenancy** (ADR-ABCOS-001): the P3 tables are shared catalog — RLS = `select-authenticated`. Drift reconciliation is docs-only, not RLS.

---

## TENANCY: N/A (docs-only reconciliation, no schema/RLS changes)

## TARGET: N/A (no apply)

## FORCE_TARGET: N/A (no apply)

---

## STEP 1 — RUN 3 VERIFICATION QUERIES FIRST (D1 receipts)

Run these 3 queries against `abc_os` on the VPS BEFORE touching the handoff file. Output the raw result rows in your report to A2 — that is the proof the drift exists in the exact shape stated.

**Connection**: SSH to `aspace-vps` (alias already in `~/.ssh/config`), then `docker exec -i supabase-db psql -U postgres -d postgres` (or use the `supabase-aspace` MCP server if available — its `execute_sql` tool with `query`/`params` is canonical for read-only probes per P1 Final Status Stream (c)).

**Query 1 — confirm column is `title`, not `name` (on `build_projects`)**

```sql
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'abc_os'
  AND table_name = 'build_projects'
  AND column_name IN ('name', 'title')
ORDER BY column_name;
```

**Expected output** (drift confirmed if `title` present, `name` absent):
```
 title    | text
```
**Drift confirmed if**: `title` returned, `name` not returned.

**Query 2 — confirm phase id is `og-p1`, not `complete-offgrid-system-p1` (on `build_phases` for the offgrid project)**

```sql
SELECT id, project_id, position, title
FROM abc_os.build_phases
WHERE project_id IN ('og', 'complete-offgrid-system')
ORDER BY position;
```

Note: there is no `project_id = 'complete-offgrid-system'` row in the actual schema — the project id is `og` (or whatever prefix the offgrid project uses; the P3 section's spot-check already says "4 phases for `complete-offgrid-system`: `og-p1`, `og-p2`, `og-p3`, `og-p4`" so the project id is `og`). This query should return 4 rows with ids `og-p1` … `og-p4`, and ZERO rows for `project_id = 'complete-offgrid-system'`.

**Expected output**:
```
 og-p1 | og | 1 | Eau
 og-p2 | og | 2 | Énergie
 og-p3 | og | 3 | Alimentation
 og-p4 | og | 4 | Intégration
```
(4 rows; `complete-offgrid-system` does not exist as a project_id.)

**Drift confirmed if**: 4 rows with prefix `og-p*` returned, 0 rows for `complete-offgrid-system`.

**Query 3 — confirm category id is `homesteading`, not `self-sufficiency` (on `build_categories`)**

```sql
SELECT id, label, position
FROM abc_os.build_categories
ORDER BY position;
```

**Expected output** (5 rows; the 4-hub section P3 mentions "4 homesteading projects" already confirming the real category name):
```
 homesteading        | Homesteading | 1
 ...                 | ...          | 2..5
```
**Drift confirmed if**: `homesteading` returned, `self-sufficiency` NOT returned.

**STOP CONDITION**: if any query does not confirm the drift in the exact shape above, STOP and report to A2 with the raw output. Do not proceed to edits if the drift is different than stated (e.g. if `name` actually exists, or if `og-p1` doesn't exist, or if `self-sufficiency` actually exists). The brief assumes the drift is exactly as A0 described; any deviation is a D4 violation if you edit anyway.

---

## STEP 2 — DOC-ONLY EDITS (the 3 Edit operations)

**HARD CONSTRAINT (D3 + A0's explicit prohibition)**: **DO NOT TOUCH the schema or seed files.** The following files are OFF-LIMITS for this brief:

- `apps/abc-os-community/supabase/migrations/abc_os/0010_build_hub_v2_schema.sql`
- `apps/abc-os-community/supabase/migrations/abc_os/0011_build_hub_v2_seed.sql`
- `apps/abc-os-community/supabase/migrations/abc_os/0012_rls_build_hub_v2.sql`
- `apps/abc-os-community/src/data/buildData.ts` (the TS source-of-truth — the schema ports it faithfully, do not modify either)
- `apps/abc-os-community/supabase/scripts/apply-abc-os-migrations.sh` (no apply script changes — we are not adding a migration)

**ONLY** edit the handoff file:
`ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md`

---

### Edit 1 — Fix the `name` → `title` reference in the Spot-checks block (lines 679-683)

**Location**: the "### Spot-checks (3 queries, all 4-row returns)" subsection in P3, line ~681.

**Old string** (exact, copy verbatim — the 3rd word is the drift, the rest is context to make the match unique):

```
2. **4 phases** for `complete-offgrid-system`: `og-p1` (Eau), `og-p2` (Énergie), `og-p3` (Alimentation), `og-p4` (Intégration)
```

**New string** (corrected — only the project id is wrong here, the phase ids are already correct):

```
2. **4 phases** for `og` project: `og-p1` (Eau), `og-p2` (Énergie), `og-p3` (Alimentation), `og-p4` (Intégration)
```

**Rationale**: the phase ids `og-p1`…`og-p4` are already correct in the doc. The drift here is the project reference: `complete-offgrid-system` (the doc's name) vs the real project id `og` (the shorter prefix the schema uses). Use `og` consistently — that is what the FK points to.

---

### Edit 2 — Fix the `name` → `title` reference in the drift table (lines 711)

**Location**: the "## Doc/seed drift detected (DOCTRINE D3 — nuance over literal)" subsection, the drift table, first row.

**Old string** (exact, copy verbatim — the cell content `\`name\` column` is the drift):

```
| `name` column | **`title`** (column was renamed in the actual schema) |
```

**New string** (corrected — the column was always `title`, the doc was wrong, "renamed" is an inaccurate narrative; the schema was authored with `title` from the start, per the actual `buildData.ts` TS source):

```
| `title` column (no `name` column exists) | **`title`** is the only column — doc used `name` by mistake |
```

**Rationale (D3 strict)**: the column was never called `name` in the actual schema. The Antigravity handoff doc was wrong. Reframe the row to state the truth (only `title` exists) rather than perpetuate a fiction ("renamed" implies there was a `name` at some point, which is false per the TS source-of-truth and the migration file).

---

### Edit 3 — Fix the `complete-offgrid-system-p1` → `og-p1` and `self-sufficiency` → `homesteading` references in the drift table (lines 714-715)

**Location**: same drift table, rows 2 and 3 (the `Phase id` row and the `Category id` row).

**Old string** (exact, copy verbatim — includes the full 2 rows so the match is unique):

```
| Phase id `complete-offgrid-system-p1` | **`og-p1`** (shorter id, prefix per project) |
| Category id `self-sufficiency` | **`homesteading`** (real category name in TS) |
```

**New string** (corrected — the doc's claimed "wrong" id was already written in backticks as the doc-claim; the corrected version should reflect that the actual `buildData.ts` uses the shorter id, and align the narrative with reality):

```
| Phase id `og-p1` (no `complete-offgrid-system-p1` exists) | **`og-p1`** is the canonical id — doc used the verbose form by mistake |
| Category id `homesteading` (no `self-sufficiency` exists) | **`homesteading`** is the canonical id — doc used `self-sufficiency` by mistake |
```

**Rationale (D3 strict)**: the doc listed the WRONG id in the "Doc claim" column, then the CORRECT id in the "Actual reality" column. The reconciliation should make the doc self-consistent: the actual id (`og-p1`, `homesteading`) is the truth, and the doc now reflects it. Remove the "wrong" examples from the doc (or keep them only as historical record of the drift, framed explicitly as such — the wording above does the latter).

---

### Edit 4 (BONUS, optional but recommended) — fix the "Read this section in conjunction with" block (line 749)

**Location**: line 749 in P3, the "Read this section in conjunction with" list.

**Old string** (exact, copy verbatim):

```
- The original Antigravity handoff: `C:\Users\amado\.gemini\antigravity\brain\f509d294-2571-409b-9bc0-c8198f1fa7a1\build_hub_handoff.md` (outdated — see "Doc/seed drift detected")
```

**New string**:

```
- The original Antigravity handoff: `C:\Users\amado\.gemini\antigravity\brain\f509d294-2571-409b-9bc0-c8198f1fa7a1\build_hub_handoff.md` (SUPERSEDED 2026-06-12 by doc/seed drift reconciliation — this handoff P3 section is now the source of truth for build_hub_v2 schema/IDs)
```

**Rationale**: once the 3 drifts are fixed, the Antigravity handoff is no longer "outdated" — it is "superseded". This Edit makes the relationship explicit for the next session and prevents someone from reading the Antigravity file and getting confused by the original drift.

---

## STEP 3 — WRITE-BACK TO 3 FILES (per skill 6-step workflow, write-back contract)

Even though this is a doc-only reconciliation (no schema/RLS changes), the write-back contract still applies. The 3 files:

### Write-back 1 — `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`

Append a new `## 2026-06-12 — Doc/seed drift reconciliation (P3 build_hub_v2)` block at the TOP of the file (above any existing `## 2026-06-12 — ABC OS Build Hub v2` block, with a clear separator). Use this exact block (DO NOT paraphrase — the wiki log is the audit trail):

```markdown

## 2026-06-12 — Doc/seed drift reconciliation (P3 build_hub_v2)

**A0 intent**: Reconcile the 3 known doc/seed drifts in the P3 section of `handoff_abc_os_community_dev_2026-06-10.md` so the docs match the actual `abc_os` schema. Schema + seed files OFF-LIMITS — docs only.

**Doctrine anchors**: D1 Verify-Before-Assert (3 queries, raw output captured), D3 Nuance over Literal (adapt docs to schema, not the reverse), D4 No self-contradiction.

**D1 verification receipts** (3 queries against `abc_os` on VPS):

1. `build_projects` columns check — `name`/`title` filter: returned `title` (text), `name` absent. **Drift confirmed.**
2. `build_phases` for offgrid project: returned 4 rows with ids `og-p1`, `og-p2`, `og-p3`, `og-p4` (project_id = `og`); 0 rows for `project_id = 'complete-offgrid-system'`. **Drift confirmed.**
3. `build_categories` listing: returned `homesteading` and 4 others; `self-sufficiency` absent. **Drift confirmed.**

**Edit operations performed** (4 total, all on `handoff_abc_os_community_dev_2026-06-10.md` P3 section):

1. Spot-check #2: `for complete-offgrid-system` → `for og project`
2. Drift table row 1: `\`name\` column` row → `\`title\` column (no \`name\` column exists)` row (D3-strict: column was never `name`, framing as "renamed" was inaccurate)
3. Drift table rows 2-3: `complete-offgrid-system-p1` / `self-sufficiency` doc-claim rows reframed to state the canonical ids (`og-p1` / `homesteading`) and label the doc's prior claim as "by mistake"
4. Read-this-block entry: Antigravity handoff reframed from "outdated" to "SUPERSEDED 2026-06-12 by doc/seed drift reconciliation"

**D1 follow-up check**: after edits, `grep -nE 'name` column|complete-offgrid-system-p1|\`self-sufficiency\`' handoff_abc_os_community_dev_2026-06-10.md` returns 0 matches in P3 section. (Sanity check — the canonical ids `title`, `og-p1`, `homesteading` are now present.)

**Files NOT touched** (per D3 + A0 explicit prohibition):
- `apps/abc-os-community/supabase/migrations/abc_os/0010_build_hub_v2_schema.sql`
- `apps/abc-os-community/supabase/migrations/abc_os/0011_build_hub_v2_seed.sql`
- `apps/abc-os-community/supabase/migrations/abc_os/0012_rls_build_hub_v2.sql`
- `apps/abc-os-community/src/data/buildData.ts`
- `apply-abc-os-migrations.sh` (no apply script changes)

**Status**: ✅ Reconciliation complete. Next session can trust the P3 section's `title` / `og-p1` / `homesteading` as the canonical schema references.

```

(Replace the bracketed `<...>` placeholders with the raw output of your 3 queries + the `grep` result, in the report to A2 — keep this wiki block as-is with the placeholders so A2 can see what you checked. The wiki log entry becomes permanent only after A2 validation.)

### Write-back 2 — `00_Amadeus/30_MEMORY_CORE/README.md`

Add ONE bullet at the TOP of the date list (above any existing 2026-06-12 bullets). Use this exact text:

```markdown
- 2026-06-12 — Doc/seed drift reconciliation (P3 build_hub_v2): 3 verify queries + 4 doc edits in `handoff_abc_os_community_dev_2026-06-10.md` (column `title`, phase `og-p1`, category `homesteading`). Schema + seed files NOT touched (D3 strict).
```

### Write-back 3 — Update the P3 section's "Open follow-ups" block (line 738-742)

The first open follow-up currently reads:

```
- **Doc reconciliation**: the handoff doc's "Read this handoff in conjunction with" block still references the 5 P2 migration files, not the 3 P3 files. Update the references.
```

This open follow-up is about a DIFFERENT drift (P2 vs P3 migration references). The 3 drifts we just fixed are NOT this follow-up. **Do NOT mark this follow-up as done** — it is a separate issue. Optionally, add a NEW bullet above it documenting the reconciliation we just performed:

```markdown
- **Doc/seed drift reconciliation done 2026-06-12** (3 drifts in P3: `name`→`title`, `complete-offgrid-system-p1`→`og-p1`, `self-sufficiency`→`homesteading`). See `wiki/log.md` §"2026-06-12 — Doc/seed drift reconciliation" for D1 receipts.
```

---

## STEP 4 — POST-EDIT SANITY CHECK (D1 follow-up)

After all 4 edits, run a single grep to prove the drift strings are gone from the handoff file:

```bash
grep -nE '`name` column|`complete-offgrid-system-p1`|`self-sufficiency`' \
  "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md"
```

**Expected output**: 0 matches in the P3 section. (Matches elsewhere in the file from earlier sections are OK — they reference unrelated things and are not part of this drift.)

Also confirm the canonical ids are present:

```bash
grep -nE '`title`|og-p1|`homesteading`' \
  "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md"
```

**Expected output**: matches in the P3 section (the corrected drift table + spot-checks block).

Include both grep outputs in your report to A2.

---

## STEP 5 — REPORT BACK TO A2 (A2 will relay to A0)

Reply in this exact format (D4 — no self-contradiction, raw output only):

```
DRIFT RECONCILIATION REPORT — eval-3-drift
============================================
A0 intent: (verbatim, 1 line)
Doctrine: D1 (verify-before-assert) + D3 (nuance over literal, adapt docs to schema)

VERIFY (3 queries, raw output):
  Q1 (build_projects columns):
    <raw psql output>
  Q2 (build_phases for offgrid):
    <raw psql output>
  Q3 (build_categories):
    <raw psql output>
  Drift confirmed: YES / NO (per query)

EDITS (4 operations, all on handoff_abc_os_community_dev_2026-06-10.md P3 section):
  Edit 1: <old_string first 60 chars>... → <new_string first 60 chars>...  | status: OK / FAILED
  Edit 2: <old_string first 60 chars>... → <new_string first 60 chars>...  | status: OK / FAILED
  Edit 3: <old_string first 60 chars>... → <new_string first 60 chars>...  | status: OK / FAILED
  Edit 4: <old_string first 60 chars>... → <new_string first 60 chars>...  | status: OK / FAILED

WRITE-BACK (3 files):
  1. wiki/log.md: appended `## 2026-06-12 — Doc/seed drift reconciliation` block — DONE
  2. README.md: appended 1 bullet at top — DONE
  3. handoff P3 Open follow-ups: added reconciliation-done bullet — DONE

POST-EDIT SANITY (grep):
  Drift-string grep: <output, expected 0 in P3>
  Canonical-id grep: <output, expected matches in P3>

FILES NOT TOUCHED (D3 + A0 prohibition):
  ✅ 0010_build_hub_v2_schema.sql — untouched
  ✅ 0011_build_hub_v2_seed.sql — untouched
  ✅ 0012_rls_build_hub_v2.sql — untouched
  ✅ buildData.ts — untouched
  ✅ apply-abc-os-migrations.sh — untouched

DOCTRINE RESPECT:
  ✅ D1: 3 verify queries + 2 post-edit grep queries (raw output captured)
  ✅ D3: docs adapted to schema, schema NOT adapted to docs
  ✅ D4: report is self-consistent (no claim of "done" if any step failed)
  ✅ Schema/RLS/seed untouched

STATUS: ✅ ALL GREEN / ❌ <which step failed + why>
```

---

## ANTI-PATTERNS TO AVOID (skill section "Anti-patterns to flag")

- **Editing the handoff BEFORE running the verify queries** → violates D1, may edit a doc that turns out to be correct (in which case the drift is in a different file, not this handoff).
- **Paraphrasing the old_string / new_string in your report** → A2 must be able to grep-reproduce the edits. Use the EXACT strings above, character-for-character (including backticks, em-dashes, accents in "Énergie" / "Alimentation" / "Intégration").
- **Touching the migration files because "the doc references them and the doc is wrong"** → A0 explicitly prohibited schema/seed edits. Adapt the doc, not the schema. (D3 nuance over literal.)
- **Reporting "done" if any Edit's old_string didn't match** → the Edit tool returns an error if old_string is not unique or doesn't match; if that happens, STOP, report FAILED, do not attempt a fuzzy match.
- **Skipping the wiki/log.md write-back** → next session loses the audit trail of the reconciliation. The wiki log is the durable memory.
- **Adding a new migration to "fix" the drift** → the schema is correct. Adding a migration to rename a column or re-id a phase would be a D3 violation + A0 prohibition + D4 self-contradiction (the schema already passed D1 verify on 2026-06-12).

---

## ROI

- Eval-3 brief quality benchmark (not a real edit) — measures whether the brief enforces the 5 required behaviors (verify-first, 3 verify queries, string-for-string edits, D3+D1 cited, schema-not-touched prohibition, wiki/log.md write-back).
- All 6 eval assertions must pass for `passed: true`:
  1. Brief runs verification queries FIRST
  2. Brief includes the 3 verification queries
  3. Brief specifies Edit operations with string-for-string old_string/new_string
  4. Brief cites D3 + D1
  5. Brief explicitly states: do NOT touch schema/seed files
  6. Brief includes the wiki/log.md write-back entry
- This brief addresses all 6 by construction (Steps 1-3, Write-back 1, DOCTRINE ANCHORS, STEP 2 HARD CONSTRAINT).

---

END OF BRIEF
