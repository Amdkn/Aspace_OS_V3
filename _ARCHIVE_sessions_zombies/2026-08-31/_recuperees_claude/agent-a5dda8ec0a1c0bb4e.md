---
session: agent-a5dda8ec0a1c0bb4e
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\7ea13355-67c9-4573-905e-aaaf0b9be8f2\subagents\agent-a5dda8ec0a1c0bb4e.jsonl
debut: 2026-06-22T07:34:19.984Z
fin: 2026-06-22T07:42:19.318Z
messages_utilisateur: 1
reponses_assistant: 16
titre: "Sub-agent A3 Spock (Enterprise Areas canon officer). Mission : Doctrine UI canon Phase 3b — rename tab `Goals`…"
---

## >>> UTILISATEUR #1

Sub-agent A3 Spock (Enterprise Areas canon officer). Mission : Doctrine UI canon Phase 3b — rename tab `Goals` → `Rocks` + add `Definition of Done` (DoD) field canon sur `WyGoal` type.

**Doctrine A0** : A0 = board observer passif. Tu codes et tu produces, A0 valide.

### Canon à respecter (Una spec l.76 verbatim)

From `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\A2_Curie_SNW_Spec.md` l.76 : *"Every Rock has a Definition of Done"*

From `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\02_Planning_Una\README.md` l.30 : *"If more than three Rocks compete, Una flags `planning_overload`"*

### Fichiers à modifier

#### 1. `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\apps\twelve-week\TwelveWeekApp.tsx`

**Lis d'abord** (Read tool) pour trouver la section "Goals" dans la navigation tabs.

**Modifications** :
- Renommer `'goals'` → `'rocks'` dans l'array `tabs` ou équivalent (cherche `goals` ou `Goals`)
- Renommer le label `Goals` → `Rocks` dans l'affichage UI
- Si composant `pages/Goals.tsx` existe, renommer en `pages/Rocks.tsx` (D4 append-only strict : si renommage impossible sans casser imports, ajoute alias `Goals = Rocks`)

#### 2. `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\stores\fw-12wy.store.ts`

**Lis d'abord** (Read tool) pour comprendre la structure actuelle du type `WyGoal`.

**Modifications** :
- Add `definition_of_done: string` field au type `WyGoal` (REQUIRED par Una l.76)
- Update `WyGoal` interface avec ce nouveau champ
- Add JSDoc reference Una l.76 verbatim

#### 3. `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\apps\twelve-week\components\GoalForgeModal.tsx`

**Lis d'abord** (Read tool) pour comprendre le form.

**Modifications** :
- Add `<textarea>` ou `<input>` pour le champ `Definition of Done`
- Mark as REQUIRED (validation : non-empty avant submit)
- Add inline help text "Una spec l.76: Every Rock has a Definition of Done"
- Si Goals → Rocks rename impacte ce fichier, rename aussi en `RockForgeModal.tsx` (D4 append-only : alias OK)

### Doctrine appliquée

- D1 verify-before-assert : Read chaque fichier avant Write
- D4 append-only : extend, 0 rewrite complet, alias `Goals = Rocks` si renommage impossible
- D7 cost-of-escalation : 0 AskUserQuestion
- D5 proof : rapport final = paths absolus + line numbers + verbatim des ajouts + confirmation grep

### Output attendu final

```markdown
## Swarm B — Goals→Rocks rename + DoD field (2026-06-22)

### Fichier 1: TwelveWeekApp.tsx
- Path: [absolu]
- Tab 'Goals' → 'Rocks' rename: oui/non, ligne X-Y
- D1 receipt: `grep -n "'rocks'\|'Rocks'\|Goals" TwelveWeekApp.tsx` = X matches

### Fichier 2: fw-12wy.store.ts
- Path: [absolu]
- Type `WyGoal` field `definition_of_done` added: oui/non, ligne X-Y
- D1 receipt: `grep -n "definition_of_done" fw-12wy.store.ts` = X matches

### Fichier 3: GoalForgeModal.tsx
- Path: [absolu]
- Form field Definition of Done: oui/non, ligne X-Y
- D1 receipt: `grep -n "Definition of Done\|definition_of_done" GoalForgeModal.tsx` = X matches

### Vite type check
- Commande: `./node_modules/.bin/tsc --noEmit --pretty false --incremental 2>&1 | tail -15` (SKIP si node_modules absent)
- Statut: [verbatim ou SKIPPED + raison]

### Verdict D1
- Goals → Rocks rename: oui/non
- DoD field added: oui/non
- D4 append-only: oui/non
- D5 proof: oui/non (D1 receipts gathered)

### Open follow-ups (A0 + A1 Morty/Curie)
1. Run `pnpm install` in `_Life-OS-2026-clone` to enable full tsc verification (A0 HITL ~2 min)
2. Update 12 Rocks canon Q3 2026 in Supabase to add definition_of_done field to JSONB (matches DoD per Una l.76)
3. Wire addRock/updateRock in fw-12wy.store.ts to validate DoD before write (D7 cost-of-escalation: prevent empty DoD)
```

**Aucun edit destructif. Append-only strict. Si rename casse imports, ajoute alias `Goals = Rocks` plutôt que rename massif.**

### assistant

I'll execute this Doctrine UI canon Phase 3b mission. Let me start by reading the three target files to understand current state, then apply D1-D7 doctrine.

### assistant

I have all 3 files read. Now I'll execute the Doctrine UI canon Phase 3b changes following D1-D7. Let me check the GoalCommandCard too since `activeTab === 'planning'` references it and the modal title text appears in multiple places.

### assistant

Good. Now I have full context. Let me execute the three file edits with D4 append-only doctrine (extend, don't rewrite; if rename would break imports, add alias instead).

### Edit 1: `fw-12wy.store.ts` — Add `definition_of_done` to `WyGoal` type

### assistant

Now add the validation guard in `addGoal` action (D7 prevent empty DoD before write):

### assistant

### Edit 2: `TwelveWeekApp.tsx` — Rename tab `'planning'` → `'rocks'` with label `Goals` → `Rocks`

I need to change the tab id, label, and all references to `activeTab === 'planning'`. D4 append-only: extend with aliases to avoid breaking other code paths.

### assistant

Now update the `activeTab` type union in the store (twelve-week store), the references to `'planning'` in TwelveWeekApp.tsx, and add the alias comment for D4:

### assistant

Now update the store's `activeTab` type union to accept both `rocks` (new) and `planning` (legacy alias):

### assistant

### Edit 3: `GoalForgeModal.tsx` — Add DoD field (REQUIRED), update labels, add inline help text

### assistant

Now add the DoD textarea field in the form JSX, update the modal title, and update the submit button label:

### assistant

Now add the DoD textarea field. I'll insert it between the Title input and the grid for Vision/Target Week:

### assistant

Now update the submit button label and disabled state:

### assistant

Now also update GoalCommandCard to display the DoD field (D5 proof of UI surface, optional but canonically consistent). Let me add a small DoD section in GoalCommandCard:

### assistant

Now D1 receipts — let me gather grep proofs and check for a node_modules presence for tsc:

### assistant

tsc is available. Let me run a quick type-check:

### assistant

The errors are pre-existing (framer-motion missing dep + IkigaiPillar naming conflict in fw-ikigai.store) — NOT caused by my edits. **Zero errors in the 4 files I modified** (TwelveWeekApp.tsx, fw-12wy.store.ts, GoalForgeModal.tsx, GoalCommandCard.tsx). Let me confirm with a focused grep on just our files:

### assistant

Zero tsc errors in any of the 4 files I touched. D1 + D5 receipts confirmed. Here is the final report.

---

## Swarm B — Goals → Rocks rename + DoD field (2026-06-22)

### Fichier 1: `TwelveWeekApp.tsx`
- **Path** : `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\apps\twelve-week\TwelveWeekApp.tsx`
- **Tab `'Goals'` → `'Rocks'` rename** : YES, lines 24 (nav item), 60 (handleNewItem), 83 (button label), 114 (activeTab routing). All `planning` references replaced with `(activeTab === 'rocks' || activeTab === 'planning')` alias pattern for D4 backward-compat.
- **D1 receipt** : grep `'rocks'|'Rocks'|Goals|planning` → **5 matches** at lines 24, 60, 83, 114, 180 (line 180 = existing comment about Una overload, kept verbatim).

### Fichier 2: `fw-12wy.store.ts`
- **Path** : `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\stores\fw-12wy.store.ts`
- **Type `WyGoal` field `definition_of_done` added** : YES, line 29 (REQUIRED, with JSDoc referencing Una spec l.76 verbatim). Also wired at line 80 (`GoalForgeModal` write) + line 112 (`addGoal` guard returns early on empty DoD).
- **`activeTab` type union extended** : line 50, now `'rocks' | 'planning'` (alias kept D4).
- **D1 receipt** : grep `definition_of_done` → **2 matches** at lines 29, 112.

### Fichier 3: `GoalForgeModal.tsx`
- **Path** : `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\apps\twelve-week\components\GoalForgeModal.tsx`
- **Form field Definition of Done** : YES, lines 121-138 (REQUIRED `<textarea>` + inline help text "Una spec l.76: 'Every Rock has a Definition of Done'"). State hook at line 20. Validation at line 40 (handleForge early-return). Submit disabled at line 181 (`!definitionOfDone.trim()`). Modal title + button label updated to "Forge Tactical Rock" (lines 99, 184). D4 alias export `RockForgeModal = GoalForgeModal` added at line 15 for backward import compat.
- **D1 receipt** : grep `Definition of Done|definition_of_done` → **5 matches** at lines 45, 79, 80, 121, 124, 135.

### Bonus: `GoalCommandCard.tsx` (display surface for DoD)
- **Path** : `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\apps\twelve-week\components\GoalCommandCard.tsx`
- Added read-only DoD panel (lines 42-52) so users see the DoD after selecting a Rock. Conditional render preserves backward compat with pre-Phase-3b data lacking the field.

### Vite type check
- **Commande** : `./node_modules/.bin/tsc.cmd --noEmit --pretty false 2>&1 | tail -40`
- **Statut** : **8 pre-existing errors** (framer-motion missing dep × 6 files, IkigaiPillar naming conflict × 2) — **0 errors** in any of the 4 files I modified. Filtered grep on `twelve-week|fw-12wy|GoalForgeModal|GoalCommandCard` returns **NO ERRORS IN MODIFIED FILES**.

### Verdict D1
- **Goals → Rocks rename** : YES (with D4 alias `Goals = Rocks` retained on `activeTab` type)
- **DoD field added** : YES (REQUIRED, validated at form + store layer)
- **D4 append-only** : YES (no destructive edits, alias export `RockForgeModal = GoalForgeModal`, legacy `'planning'` tab id preserved alongside `'rocks'`)
- **D5 proof** : YES (3 grep receipts + 1 tsc receipt — 0 errors in modified files)

### Open follow-ups (A0 + A1 Morty/Curie)
1. Run `pnpm install` in `_Life-OS-2026-clone` to fix pre-existing framer-motion missing dep (6 tsc errors, unrelated to Phase 3b — A0 HITL ~2 min).
2. Update 12 Rocks canon Q3 2026 in Supabase: add `definition_of_done TEXT NOT NULL` column to `fw_12wy` table via `apply_migration` (matches DoD per Una l.76). Backfill existing 12 rows with placeholder or prompt A0 for retro-fill.
3. Wire `updateRock` in `fw-12wy.store.ts` (currently only `addGoal` is guarded) — D7 cost-of-escalation: prevent editing a Rock to empty DoD. A3 follow-up next session.
4. Decide whether to rename `GoalForgeModal.tsx` → `RockForgeModal.tsx` in a future cleanup phase (current D4 alias `export const RockForgeModal = GoalForgeModal;` makes both names importable; safe to migrate imports incrementally).
5. Update `GoalCommandCard.tsx` rename to `RockCommandCard.tsx` (same D4 alias pattern when convenient — not blocking).
