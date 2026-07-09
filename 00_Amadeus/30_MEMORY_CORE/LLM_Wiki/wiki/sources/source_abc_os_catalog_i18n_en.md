---
source: A0_Directive_2026-06-13_i18n_seed_sync
date: 2026-06-13
type: source
domain: ABC_OS_Catalog_I18N
tags: [i18n, abc-os, catalog, en-first, fr-en-translation, supabase]
---

# i18n EN Seed Sync — abc_os Catalog Strings (2026-06-13)

## A0 Intent (1 line)

Normalize the FR drift left in Supabase catalog seed data after the next-intl commit `5a19439` (UI strings EN, seed data still FR). Decision 2026-06-13: **next-intl + EN default, FR plus tard**. Existing FR in catalog = TEMPORARY drift.

## D1 Verify — Raw Counts (before)

| Table | Column / Key | Total rows | FR non-ASCII rows |
|-------|--------------|------------|-------------------|
| `abc_os.spotlight_projects` | `tag` | 2 | 1 (`Énergie`) |
| `abc_os.hub_pulse` | `payload->'meta'->>'title'` | 40 | 0 |
| `abc_os.hub_pulse` | `payload->'meta'->>'subtitle'` | 40 | 0 |
| `abc_os.hub_pulse` | `payload::text` (any key) | 40 | 0 |

**Regex used**: `~ '[^[:ascii:]]'` (broader than the brief's French-specific char class — catches all accented characters and reveals the true FR surface).

**hub_pulse payload structure** (real, not from brief): `{"events": 2, "members": 12, "threads": 4}` — pure numeric metrics blob. The `meta.title` / `meta.subtitle` JSON keys the brief mentioned **do not exist in the current payload schema**. Future schema evolution may add them; the regex queries are idempotent and re-runnable.

## D1 Verify — Distinct Values Before

```
spotlight_projects.tag distinct = {Artisanat, Énergie}
```

## UPDATEs Applied (D3 idiomatic EN, idempotent single-row)

| id | org_id | name | tag before | tag after | D3 rationale |
|----|--------|------|------------|-----------|--------------|
| `eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee` | `11111111-…` | Solaris Agri-Coop | `Énergie` | `Energy` | Project name already carries "Solaris" → tag = category "Energy", not "Solar Energy" (avoid duplication) |
| `ffffffff-ffff-ffff-ffff-ffffffffffff` | `11111111-…` | Umoja Weavers | `Artisanat` | `Craft` | Standard solarpunk/cooperative-movement term; literal "Craftsmanship" = verbose, loses category brevity |

## D1 Verify — Raw Counts (after)

| Table | Column / Key | FR non-ASCII rows |
|-------|--------------|-------------------|
| `abc_os.spotlight_projects` | `tag` | **0** |
| `abc_os.hub_pulse` | `payload::text` | **0** |

```
spotlight_projects.tag distinct = {Craft, Energy}
```

## Spot-Check (3 random hub_pulse rows)

```
id 92026ab7-ef23-471a-9a13-739ad04c9262 | {"events": 2, "members": 12, "threads": 4}
id 0565dacf-b5fc-4097-8ac3-9aea3f446ad0 | {"projects": 3, "milestone": 2, "milestoneTotal": 5}
id 41f31e73-4c1a-40cc-95c5-dbff4d6f1770 | {"courses": 6, "completed": 2, "inProgress": 3}
```

No `meta.title` / `meta.subtitle` keys present. Pure numeric metrics, EN-clean.

## Translation Table — FR → EN (full mapping, D3 idiomatic)

The brief listed hypothetical FR strings ("Développement Durable", etc.) that **do NOT exist in the current DB**. They are saved here for future seeds/migrations where they may reappear. **D4 no-fabrication**: these were NOT UPDATEd, only documented.

| # | FR source | EN target | D3 nuance / context |
|---|-----------|-----------|---------------------|
| 1 | `Énergie` | `Energy` | Category tag. If used as compound ("Énergie Solaire" in a non-solaris-named project), use "Solar Energy" |
| 2 | `Artisanat` | `Craft` | Standard solarpunk/coop movement term. Avoid "Craftsmanship" (verbose), avoid "Handicraft" (older, exoticizing) |
| 3 | `Développement Durable` | `Sustainable Development` | Idiomatic. NOT literal "Durable Development" |
| 4 | `Énergie Solaire` | `Solar Energy` | Idiomatic. Word order swaps FR→EN |
| 5 | `Coopération` | `Cooperation` OR `Collaboration` | Both valid EN; choose by context. "Cooperation" = working together on shared goal. "Collaboration" = cross-functional working. A0 to decide per use case |
| 6 | `Agroécologie` | `Agroecology` | One word in EN (no hyphen) |
| 7 | `Permaculture` | `Permaculture` | No translation (loanword in EN too) |
| 8 | `Souveraineté Alimentaire` | `Food Sovereignty` | Standard EN term (used by FAO, La Via Campesina, USFSA) |
| 9 | `Assemblée` | `Assembly` | In context of cooperative governance (general assembly, not political assembly) |
| 10 | `Séchoir` | `Dryer` | Solar dryer for crops. Context-specific: NOT "drying room" (too literal) |
| 11 | `Teintures` | `Dyes` | Natural dyes for textiles. Plural EN. If singular context, "Dye" |
| 12 | `Préparer assemblée` | `Prepare assembly` | action_items.title example (not in current scope) |
| 13 | `Finaliser teintures` | `Finalize dyes` | action_items.title example |
| 14 | `Livrer séchoir` | `Deliver dryer` | action_items.title example |
| 15 | `Publier Soko` | `Publish Soko` | "Soko" = proper noun (market name), keep as-is |

## D4 Honesty — Brief vs Reality

The brief assumed 5-10 FR strings across `spotlight_projects.tag` AND `hub_pulse.payload.meta`. **Actual state** = 2 rows in `spotlight_projects` (1 with non-ASCII FR), 0 FR in `hub_pulse.payload` (40 rows). The `meta.title` / `meta.subtitle` JSON keys do not exist in the current payload schema.

This is consistent with the i18n migration timeline: next-intl `5a19439` shipped UI strings EN, but seed `0003_seed_umoja.sql` (P1.1 Gate 3) was applied 2026-06-11 with 4 hub_pulse rows using numeric metrics only. The FR drift the brief warned about is **mostly hypothetical at this point** — there are 2 actual FR strings to fix, not the imagined 10+.

## Doctrine Anchors

- **D1 Verify-Before-Assert**: every claim backed by raw SQL count output, not "I ran it and it worked"
- **D3 Nuance over Literal**: "Sustainable Development" not "Durable Development", "Craft" not "Craftsmanship"
- **D4 No Self-Contradiction**: brief listed strings that don't exist in DB → documented, not UPDATEd
- **D6 Root Cause Real**: `app.env='dev'` mutation impossible (Supabase hardened) — N/A for this UPDATEs (no app.env gate on these tables, direct row UPDATE)
- **D10 Mixed-Tenancy** (ADR-ABCOS-001): spotlight_projects = per-org via RLS `current_org_id()` + FK to `abc_os.organizations`. The UPDATE is targeted by `id = '...'`, only the matching row is affected. RLS policies (`spotlight_admin_update`) permit `authenticated` role with matching `org_id` to UPDATE — admin/owner only. Single-row scope = no tenancy leak
- **Idempotency**: each UPDATE uses `WHERE id = '...'` so re-running is safe (row already at target value, UPDATE 0)

## Tenancy Verification

`abc_os.spotlight_projects` schema:
- `org_id` NOT NULL, FK to `abc_os.organizations(id)`, `ON DELETE CASCADE`
- RLS `spotlight_select_member` (USING `org_id = current_org_id()`)
- RLS `spotlight_admin_update` (USING + WITH CHECK on `current_org_id()` + `current_role() IN ('admin','owner')`)
- Both UPDATEs target org `11111111-1111-1111-1111-111111111111` (Umoja Weavers)

## SQL Re-Runnable Pattern (for future drifts)

```sql
-- 1. Count FR strings
SELECT count(*) FROM abc_os.spotlight_projects
WHERE tag ~ '[^[:ascii:]]';

-- 2. Inspect distinct values
SELECT DISTINCT tag FROM abc_os.spotlight_projects ORDER BY tag;

-- 3. Idempotent single-row UPDATE
UPDATE abc_os.spotlight_projects
SET tag = '<EN_TARGET>'
WHERE id = '<UUID>' AND tag = '<FR_SOURCE>';

-- 4. D1 verify
SELECT count(*) FROM abc_os.spotlight_projects WHERE tag ~ '[^[:ascii:]]';
```

Same pattern for `hub_pulse.payload.meta.*` if those keys are ever added to the payload schema.

## Open Follow-Ups

1. **`abc_os.action_items`** (4 rows from seed 0003): titles contain FR ("Préparer assemblée", "Finaliser teintures", "Livrer séchoir", "Publier Soko"). **NOT in current scope** per brief. Translation #12-15 above are ready to apply when A0 opens the scope.
2. **`abc_os.feed_items`** (4 rows from seed 0003): body/content may contain FR. Worth a follow-up scan.
3. **`abc_os.members`** (2 rows from seed 0003): city names are real-world proper nouns (Nairobi, Accra) — no translation needed.
4. **Schema evolution**: if `hub_pulse.payload.meta.title` / `meta.subtitle` keys are ever added, re-run the D1 verify queries from this file.

## Files Touched

- `wiki/log.md` (1 entry append, 2026-06-13)
- `wiki/sources/source_abc_os_catalog_i18n_en.md` (this file)
- `~/.claude/projects/C--Users-amado/memory/MEMORY.md` (1 new section "## i18n catalog strings")
- 2 UPDATEs on `aspace-vps` self-hosted Supabase (no files, in-place DB changes)
- 0 git commits (DB state, not code)
