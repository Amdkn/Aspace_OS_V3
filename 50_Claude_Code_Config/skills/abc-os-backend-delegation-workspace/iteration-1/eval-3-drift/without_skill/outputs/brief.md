# A2 → A3 Brief — Doc/Seed Drift Reconciliation (build_hub_v2, 2026-06-12)

> **Mission**: reconcile the doc/seed drift in the P3 section of the build_hub_v2 handoff. The schema/seed is **the source of truth** (per ADR-META-001 D3: "adapt docs to schema, not the reverse"). You are a **docs-only** A3 — DO NOT touch schema, migrations, or seed files.

---

## Scope & Hard Boundaries

**Touch (allowed)**:
- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md` (P3 section only)
- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` (1 append-only entry)

**Do NOT touch (forbidden)**:
- `apps/abc-os-community/supabase/migrations/abc_os/0010_build_hub_v2_schema.sql`
- `apps/abc-os-community/supabase/migrations/abc_os/0011_build_hub_v2_seed.sql`
- `apps/abc-os-community/supabase/migrations/abc_os/0012_rls_build_hub_v2.sql`
- `apps/abc-os-community/src/data/buildData.ts`
- Any other SQL / TS / config file under `apps/abc-os-community/`

Doctrine anchors: **ADR-META-001 D1** (verify drift exists before fixing — D1 verify queries below), **ADR-META-001 D3** (nuance over literal — schema wins, not docs), **ADR-ABCOS-001 D10** (Build Hub v2 coexistence ratified 2026-06-12 — mixed-tenancy is canon).

---

## Phase 0 — Mandatory D1 Verification (BEFORE any Edit)

> Per ADR-META-001 **D1**: verify the actual state in the live database before asserting drift. The drift report is hearsay until you observe it in psql/output.

Run these 3 verification queries against the live `abc_os` schema on the VPS (`aspace-vps`, via `supabase-solaris` MCP or `ssh aspace-vps "docker exec -i supabase-db psql -U postgres -d postgres -c '<sql>'"`). Each query must return a single row that **confirms the actual name** (not the doc's claim).

### Query 0.1 — Confirm column name on `build_projects`

```sql
SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'abc_os'
  AND table_name   = 'build_projects'
  AND column_name IN ('name', 'title');
```

Expected: **1 row → `title`**. If `name` is returned instead → STOP, do not edit docs, the drift claim is wrong.

### Query 0.2 — Confirm phase id for the off-grid "Eau" phase

```sql
SELECT id
FROM abc_os.build_phases
WHERE id IN ('complete-offgrid-system-p1', 'og-p1')
ORDER BY id;
```

Expected: **at least the row `og-p1` is present**. The `complete-offgrid-system-p1` row may or may not exist — the only load-bearing fact is that `og-p1` is the real id.

### Query 0.3 — Confirm category id for the homesteading category

```sql
SELECT id
FROM abc_os.build_categories
WHERE id IN ('self-sufficiency', 'homesteading')
ORDER BY id;
```

Expected: **at least the row `homesteading` is present**. Again, the load-bearing fact is that `homesteading` is the real id.

**D1 Gate**: if all 3 queries confirm the drift as described, proceed to Phase 1. If ANY query contradicts the drift report → STOP, escalate to A2, do not edit docs (we are docs-only A3; schema correction is a separate L0/Rick task).

**Capture proof**: log the exact output of all 3 queries in your final report to A2 (D5 proof on disk). The wiki log.md entry should reference the verification but should NOT paste the full output (D7 cross-agent — keep it tight).

---

## Phase 1 — Edit the Handoff (P3 Section)

Target file (absolute, Bash-style):
```
C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md
```

### Edit 1.1 — Drift row: `name` column → `title`

In the "Doc/seed drift detected" drift table (around line 711), replace:

```
| `name` column | **`title`** (column was renamed in the actual schema) |
```

The string **already says** "actual reality = `title`" — that row is **correct as-is**. **No edit needed for this row.** (A2 note: the drift is that the *Antigravity* doc says `name`; the *handoff* table already shows the reconciliation target. The reconciliation is complete here.)

→ **Verification action**: re-read the table at line 711 and confirm it says `title` in the Actual reality column. If a future contributor has re-introduced `name`, then flip it back. Otherwise no Edit.

### Edit 1.2 — Drift row: phase id `complete-offgrid-system-p1` → `og-p1`

In the same table (around line 714), the row currently reads:

```
| Phase id `complete-offgrid-system-p1` | **`og-p1`** (shorter id, prefix per project) |
```

Same as above — the **target value is already correct**. **No edit needed.** Verification-only.

### Edit 1.3 — Drift row: category id `self-sufficiency` → `homesteading`

In the same table (around line 715), the row currently reads:

```
| Category id `self-sufficiency` | **`homesteading`** (real category name in TS) |
```

Same — **target value already correct**. Verification-only.

### Edit 1.4 — The OTHER drift items (the D1 audit may reveal more)

The drift table (lines 709–715) also has these rows that the original prompt did **not** mention but are listed in the same section:

| Doc claim | Actual reality | Action |
|-----------|----------------|--------|
| `status` on `build_tasks` | DOES NOT EXIST (per-user, not catalog) | already correct in handoff table — verification only |
| `difficulty`, `est_minutes` on `build_tasks` | Exists ✓ | already correct — verification only |

**You are NOT being asked to fix all drift items**, only the 3 named in the original A2 prompt (column, phase id, category). But as a docs-only A3, do a quick visual scan: if any of the rows in the drift table currently misstate the actual reality, fix them in the **same Edit pass**. Do not silently expand scope — if you find drift beyond the 3 named items, mention it in your A2 report and let A2 decide.

### Edit 1.5 — Reconciled-tone paragraph

The paragraph at line 707 says:

> "The sub-agent's brief was updated to use the **real** schema, but the spot-check queries in the docs still reference the old names. **Reconciliation needed**"

And line 717:

> "**Next session task**: amend the Antigravity handoff doc to reflect real schema/IDs, OR re-author the seed docs from `buildData.ts` directly."

After you complete the 3 verification queries, replace the "**Reconciliation needed**" sentence with:

```
**Reconciliation status (2026-06-12)**: drift confirmed via 3 D1 verification queries against live `abc_os` (column `title` not `name`, phase id `og-p1` not `complete-offgrid-system-p1`, category `homesteading` not `self-sufficiency`). The drift table in this section already documents the **target** (Actual reality column), so the doc is reconciled at the handoff level. Outstanding work: re-author the Antigravity handoff (`build_hub_handoff.md`) to match — out of scope for this brief, gated on A0.
```

And change line 717 from:

```
The seed SQL faithfully ports the **actual** `buildData.ts` structure, not the Antigravity-idealized doc. The docs need to be updated to match. **Next session task**: amend the Antigravity handoff doc to reflect real schema/IDs, OR re-author the seed docs from `buildData.ts` directly.
```

to:

```
The seed SQL faithfully ports the **actual** `buildData.ts` structure, not the Antigravity-idealized doc. The handoff table above is now reconciled (2026-06-12, see status line); the remaining `build_hub_handoff.md` (Antigravity original) is still outdated — flagged as out-of-scope follow-up.
```

### Edit 1.6 — "Next safe action" step 2 (line 728)

The current step 2 reads:

```
2. **Update handoff docs** to reflect real schema/IDs (see "Doc/seed drift detected" above)
```

Mark it as **DONE** (2026-06-12 reconciliation pass), keeping the original text as a reference:

```
2. ✅ **Update handoff docs** to reflect real schema/IDs (DONE 2026-06-12, this brief) — see "Doc/seed drift detected" status line. Remaining: Antigravity `build_hub_handoff.md` (out of scope).
```

---

## Phase 2 — wiki/log.md Write-back (append-only)

Target file:
```
C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md
```

Prepend (NOT append — `log.md` is reverse-chronological, newest on top) a single bullet, **at the very top of the bullet list** (right after the YAML frontmatter, before the existing 2026-06-12 entries). The format must match the existing convention: `- **YYYY-MM-DD** : <emoji> **<headline>** : <body>`.

### Entry to insert

```
- **2026-06-12** : 🛠️ **ABC OS Build Hub v2 — Doc/seed drift reconciliation (handoff P3, docs-only, D1-verified)** : A0 prompt 2026-06-12 (eval-3-drift baseline run) signalé dérive doc/seed dans `handoff_abc_os_community_dev_2026-06-10.md` P3 section : (1) column `name` (réel = `title`), (2) phase id `complete-offgrid-system-p1` (réel = `og-p1`), (3) category `self-sufficiency` (réel = `homesteading`). **D1 verify (3 queries avant Edit, ADR-META-001 D1)** : (a) `SELECT column_name FROM information_schema.columns WHERE table_schema='abc_os' AND table_name='build_projects' AND column_name IN ('name','title')` → 1 row `title` ✓ ; (b) `SELECT id FROM abc_os.build_phases WHERE id IN ('complete-offgrid-system-p1','og-p1')` → `og-p1` présent ✓ ; (c) `SELECT id FROM abc_os.build_categories WHERE id IN ('self-sufficiency','homesteading')` → `homesteading` présent ✓. **Résultat** : drift confirmé, doc handoff P3 table already à jour (les 3 lignes target = Actual reality) — pas d'Edit nécessaire sur les 3 lignes de drift elles-mêmes, MAIS added 2 status lines (paragraph 707 + paragraph 717 + step 2 line 728) pour expliciter "DONE 2026-06-12" et flag le build_hub_handoff.md Antigravity comme follow-up out-of-scope. **Doctrine** : (a) **D1 verify-before-assert** (3 queries obligatoires avant Edit — D5 preuve capturée) ; (b) **D3 nuance over literal** (schema = source of truth, doc s'adapte au schema, pas l'inverse) ; (c) **D6 no scope creep** — touched handoff P3 + log.md UNIQUEMENT, schema/seed/migrations/buildData.ts intacts (D6 = root cause protection) ; (d) **D2 ADR-ABCOS-001 D10** (Build Hub v2 coexistence = canon ratified 2026-06-12). **Forbidden files verified untouched** : `0010_build_hub_v2_schema.sql`, `0011_build_hub_v2_seed.sql`, `0012_rls_build_hub_v2.sql`, `buildData.ts` — 0 Edit, 0 Write, 0 Bash mutation. **Total** : 1 handoff file (3 status-line Edits, 0 data-row Edits car table déjà réconciliée) + 1 log.md entry. **Prochaine** : A0 decide si on ré-author le `build_hub_handoff.md` Antigravity original (out-of-scope brief), et si on amende ADR-ABCOS-001 pour pointer explicitement le seed = port of `buildData.ts` réel.
```

**Insertion method**: read the log file first (you must read before Write/Edit), then use the Edit tool to add the entry as a new top-level bullet right after the existing frontmatter (the 3 lines `---\n...\n---` block at the top) and BEFORE the first existing bullet (`- **2026-06-12** : ✅ **ABC OS Build Hub v2 ...`).

---

## Phase 3 — Verification & Report

After the 2 file mutations:

1. **D1 self-check** (you do this, not the human):
   - `grep -nE 'name.*title|complete-offgrid-system-p1.*og-p1|self-sufficiency.*homesteading' handoff_abc_os_community_dev_2026-06-10.md` → expect 3 hits, all in the drift table (lines ~711, 714, 715), all showing the **target** value on the right of the `|`
   - `grep -c 'Reconciliation status (2026-06-12)' handoff_abc_os_community_dev_2026-06-10.md` → expect 1
   - `grep -c 'DONE 2026-06-12, this brief' handoff_abc_os_community_dev_2026-06-10.md` → expect 1
   - `head -10 log.md` → expect the new entry to be the first bullet
2. **D6 no-scope-creep check**:
   - `git status` (in `apps/abc-os-community/`) → expect **0 changes** to schema/seed/migrations/buildData.ts
   - `git status` (in `30_MEMORY_CORE/LLM_Wiki/wiki/`) → expect exactly 2 files changed: `handoff_abc_os_community_dev_2026-06-10.md` + `log.md`
3. **Report back to A2**: include (a) the 3 query outputs as D1 proof, (b) the diff stats (lines added/removed per file), (c) confirmation that no forbidden file was touched, (d) any drift items discovered beyond the 3 named ones (for A2's next A0 conversation, not your action).

---

## Doctrine Compliance Checklist (D1–D8 + ADR-ABCOS-001 D10)

| # | Doctrine | How you comply |
|---|----------|----------------|
| D1 | Verify drift exists before fixing | Phase 0 = 3 queries mandatory, D1 Gate before any Edit |
| D2 | Research first, re-derive second | Brief = canon, schema = already verified 2026-06-12 (per log) |
| D3 | Nuance over literal; adapt docs to schema, not reverse | Doc handoff P3 → matches `abc_os` schema; buildData.ts unchanged |
| D4 | No self-contradiction | Status line + step-2 mark = consistent with log entry |
| D5 | Proof on disk, not assertion | 3 query outputs captured in your report; `git status` proof of no scope creep |
| D6 | Root cause protection | Forbidden files list explicit; verification `git status` clean for them |
| D7 | No escalation without warrant | If drift claim is wrong, STOP and escalate to A2 (not A0 — A2 owns L1/L2) |
| D8 | Cost of escalation to A0 | Use A2 as your primary reporter; only escalate A0 if schema needs to change |
| D10 | ADR-ABCOS-001 Build Hub v2 coexistence (ratified 2026-06-12) | Documented in the new log entry; no edit to ADR-ABCOS-001 itself (canon = immutable) |

---

## Anti-patterns Forbidden

1. **Editing schema/seed/migrations/buildData.ts** — D6 violation, A2 escalation + airlock
2. **Patching the 3 drift rows in the table to "fix" them** — they already show the target, you would re-introduce drift
3. **Appending to log.md** (vs prepending) — log.md is reverse-chronological
4. **Pasting the 3 query outputs into log.md** — D5 proof goes in your report to A2, log is the headline
5. **Touching the Antigravity `build_hub_handoff.md`** — out of scope, gated on A0
6. **Amending ADR-ABCOS-001** — canon is immutable, new decisions spawn new ADRs
7. **Re-running the apply script** (`apply-abc-os-migrations.sh`) — we are docs-only
8. **Re-pushing Vercel / re-deploying** — completely out of scope

---

## Summary

- **3 verification queries** (Phase 0) — must observe drift before editing
- **1 handoff file** (Phase 1) — 3 status-line Edits (lines ~707, ~717, ~728), 0 data-row Edits because the drift table is already correct
- **1 log.md entry** (Phase 2) — prepend, reverse-chronological
- **0 schema/seed/migration/TS edits** — D6 hard guard
- **Report to A2** with D1 proof, D5 diff stats, D6 git status, and any extra drift discovered
