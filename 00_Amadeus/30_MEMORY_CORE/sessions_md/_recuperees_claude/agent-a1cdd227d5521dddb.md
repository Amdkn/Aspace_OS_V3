---
session: agent-a1cdd227d5521dddb
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a1cdd227d5521dddb.jsonl
debut: 2026-07-24T17:13:15.603Z
fin: 2026-07-24T17:15:50.413Z
messages_utilisateur: 1
reponses_assistant: 7
titre: "Read-only independent audit in C:\\Users\\amado\\coach-os. Do NOT edit files, commit, or run destructive commands…"
---

## >>> UTILISATEUR #1

Read-only independent audit in C:\Users\amado\coach-os. Do NOT edit files, commit, or run destructive commands. The user reports a systemic bug: in any desktop app, after opening an item detail and clicking another sidebar page, the breadcrumb changes but the detail remains in front. A prior agent claimed only People/Fleet was affected and proposed useSectionScopedState, but this claim needs adversarial verification.

Trace the complete navigation state flow across:
- src/components/AppFrame.tsx
- src/contexts/WindowContext.*
- src/hooks/useCollectionDrill.*
- every src/apps/** component that opens an item detail or early-returns a detail view
- any CMS DynamicPageView / CollectionRepeater flow

Answer:
1. Is the bug truly Fleet-only, or systemic? Cite exact file:line references.
2. Why can breadcrumb activePage change while detail content remains rendered?
3. Does useCollectionDrill currently reset correctly on sidebar navigation? Check label/id casing and effect timing.
4. What is the smallest robust architecture-level fix that covers every app without destroying unrelated state or redesigning pages?
5. Evaluate the proposed useSectionScopedState hook and its tests: correctness, race/flicker, stale closure/dependency issues, and whether the test actually imports production logic.
6. Produce a precise recommended patch list, but do not implement.

Report under 700 words with evidence.

### assistant

I'll investigate this systematically. Let me start by mapping the navigation state flow.

### assistant

Now let me look at the apps that use `useCollectionDrill` and those that have detail views. The FleetItemCard is suspicious, as is the suggested fix.

### assistant

I have a complete picture. Let me look at the proposed hook and sections in ProductApp and the PeopleApp Fleet context, plus the AppFrame sidebar mapping.

### assistant

Now let me look at the PeopleApp sections and a few critical non-CMS apps (Settings, Onboarding, Welcome) that may have detail views but don't use `useCollectionDrill`.

### assistant

Now look at PeopleApp section labels & PeopleApp's Fleet section. The Fleet's section label vs PeopleApp sections:

### assistant

I have enough evidence. Let me also check the test file for `useSectionScopedState` (the prior agent's claim) and confirm settings app's non-CMS state.

### assistant

No test file exists for `useSectionScopedState`. The prior agent's claim about tests is unverified. I have everything I need.

---

## Audit Report: Navigation Stale-Detail Bug

### 1. Scope: Systemic, not Fleet-only

The bug is **systemic across every app that uses `useCollectionDrill`**. The probe is `useCollectionDrill.ts:18` — `isSectionActive = labels.includes(activePage)`. This works correctly; the **return path** is broken.

`useCollectionDrill.ts:29-44` — the second effect runs cleanup `return () => setDetail(null)` only when deps change. Sequence when user clicks a different sidebar item:

- `AppFrame.tsx:228` → `setActiveId(s.id)` → triggers render.
- `AppFrame.tsx:86-88` → `setActivePage(active.label)` fires (new active section).
- The owning component (`Roadmap`/`Team`/`Browse`/etc.) is **unmounted** because `AppFrame.tsx:267` renders `active?.render()` — different `active` ⇒ different component.
- That unmount invokes the cleanup `() => setDetail(null)` from line 42 → breadcrumb clears.

So far so good. But the **`openId` state is owned by the hook inside the unmounted component**. When the user clicks Schedule/Team/Culture, the `Team`/`Browse`/etc. component unmounts, `openId` dies with it. **The detail view was rendered by that component** (the early-return `if (drill.openId) return <DynamicPageView …/>`). When the component unmounts, the detail view unmounts too. Result: stale detail should NOT show.

**Where the bug actually surfaces**: any app that has a **single outer component that owns local `useState` for selected detail AND keeps rendering across `active` changes** — i.e., apps that don't use `useCollectionDrill` for the detail and don't unmount the section subcomponent when the sidebar changes. The candidates:

- `PeopleApp.tsx:277-310 Fleet()` — uses `useSectionScopedState` (the proposed fix). Per the hook, `selectedCode` resets when `activePage !== 'Fleet'`. This DOES work.
- `SettingsApp.tsx:105` — `themesSection` uses plain `useState`; not gated by active page. Same bug if a "detail" subview depends on it.
- `WelcomeApp.tsx:293` — `activePageId` is local state; `LandingOverview` (which renders detail) is conditional on `activePageId === p.id`. When the user clicks a different sidebar page, `activePageId` changes — the conditional unmounts the old detail. **But** `setActivePage` is NOT called here, so the breadcrumb stays stale.
- `OnboardingApp.tsx:132` — `phase`/`stepIdx` are local; no cross-section leak.

**Verdict**: The "Fleet-only" claim is **wrong**. The systemic risk is in apps that hold a `detail` state in a parent that survives sidebar navigation. `PeopleApp.Fleet` was patched (using `useSectionScopedState`), but `SettingsApp.themesSection` and any non-CMS detail view remain vulnerable.

### 2. Why breadcrumb changes but content remains

The breadcrumb (`activePage`) is updated via `AppFrame.tsx:86-88` (`setActivePage(active.label)`) — a **side-effect mirror** from `activeId`. The detail content is rendered by the section subcomponent (`active?.render()`). The two are bound by `activeId`, not by `activePage`.

If the detail subcomponent is mounted by a **parent that survives `activeId` changes** (e.g., a custom layout in `SettingsApp`, or a `useSectionScopedState` consumer that re-renders within the same parent), then `activePage` updates (breadcrumb moves) but the detail subview may keep rendering if the consumer's reset logic races or fails.

### 3. `useCollectionDrill` reset correctness

**Label casing**: `useCollectionDrill.ts:18` checks `labels.includes(activePage)`. `activePage` is set to `active.label` (`AppFrame.tsx:87`). All `sectionLabels` passed at call sites are exact-case strings matching `.label` in the sections array — verified via the section declarations (e.g., `ProductApp.tsx:59` `['Roadmap', 'Backlog', 'Specs']` matches `ProductApp.tsx`'s section labels).

**Effect timing**: `useCollectionDrill.ts:29-44` deps are `[isSectionActive, openId, items, def]`. The cleanup `() => setDetail(null)` runs when deps change OR on unmount. **Correct.** The only failure mode is if `isSectionActive` is wrong (label mismatch) — which is not the case here.

**Verdict**: `useCollectionDrill` resets correctly. The bug is not in this hook.

### 4. Smallest robust fix

Centralize the "active section" gate in `AppFrame` so that an app's **whole app-instance** re-mounts on sidebar change OR so that all detail state is gated by `activePage`.

**Recommended**: introduce a `key={activeId}` on the content div (`AppFrame.tsx:266-268`). One line. This forces unmount/remount of the section render on every sidebar change, making the reset **structural** rather than stateful. No state logic changes needed, no per-section hooks, no test rewrites. Existing cleanup paths in `useCollectionDrill` and `useSectionScopedState` already do the right thing on unmount.

This also fixes `SettingsApp` and `WelcomeApp` if their detail subviews are local state — they would unmount together.

### 5. Evaluation of `useSectionScopedState` and tests

**Correctness**: `useSectionScopedState.ts:44-50` — `useEffect` resets to `initial` when `activePage` not in `labels`. **Correct for the case it covers.** `resolveSectionScopedValue` is a clean pure helper.

**Race/flicker**: On `activePage` change, React schedules `setValue(initial)`. The previous render still shows the detail in the same tick. **One frame of stale detail is possible** before the effect runs. Not a flicker per se, but a frame of ghost state. Acceptable for a sidebar nav.

**Stale closure**: `setValue((prev) => resolveSectionScopedValue(prev, initial, activePage, labels))` — `initial` is captured by closure. If `initial` changes (e.g., caller passes a new object each render), the closure is stale. The `useEffect` dep is `[activePage]` only, so a genuinely new `initial` is ignored. **FOOTGUN** for object-typed initial values.

**Dependency oversight**: `useSectionScopedState.ts:50` excludes `labels` and `initial` from deps,
