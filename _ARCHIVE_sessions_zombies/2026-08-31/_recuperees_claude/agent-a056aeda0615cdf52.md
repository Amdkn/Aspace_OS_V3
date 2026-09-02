---
session: agent-a056aeda0615cdf52
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a056aeda0615cdf52.jsonl
debut: 2026-07-24T17:20:01.735Z
fin: 2026-07-24T17:20:36.782Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Read-only architecture review in C:\\Users\\amado\\coach-os; do not edit. Validate the smallest robust fix for th…"
---

## >>> UTILISATEUR #1

Read-only architecture review in C:\Users\amado\coach-os; do not edit. Validate the smallest robust fix for this proven state flow:

- AppFrame owns activeId and sidebar buttons currently do `setActiveId(s.id)` at src/components/AppFrame.tsx around line 226.
- WindowContext exposes `detail: {label,onBack}` and `setDetail`.
- useCollectionDrill is called once in each App parent and shared across several section render functions. Many hooks accept multiple labels, e.g. Clients ['Active','Onboarding','Churn Risk','Directory'], Product ['Roadmap','Backlog','Specs'], Dashboard ['Overview','Client Pipeline'], Sales ['Pipeline','Deals']. Because `isSectionActive` stays true when switching between those labels, `openId` remains non-null and the new section render immediately returns the old DynamicPageView. Breadcrumb activePage updates separately.
- AppFrame's render functions are invoked as `active?.render()`; adding a key to the wrapping div would NOT reset parent-owned drill state.
- A current uncommitted People/Fleet detail uses a new useSectionScopedState hook because Fleet is non-CMS and does not register a detail crumb.

Candidate fix:
1. In AppFrame destructure `detail` and `setDetail` from useWindowPage.
2. Add one `navigateToSection(nextId)` function. If nextId differs from activeId, call `detail?.onBack()` and `setDetail(null)` synchronously before `setActiveId(nextId)`.
3. Use it for sidebar clicks and voice section navigation, so every registered CMS detail closes before any section change, even within a multi-label group.
4. Keep a minimal Fleet-specific reset for the non-CMS detail, or register Fleet detail in WindowContext so the shell handles it too.

Review questions:
- Is this candidate correct under React batched updates and closure semantics?
- Is it safer to register Fleet detail in WindowContext rather than add useSectionScopedState?
- Any loop/stale callback risk from `detail.onBack`?
- Should useCollectionDrill also change, or is AppFrame enough?
- Give exact minimal patch list and regression scenarios. No implementation. Under 500 words.

### assistant

# Architecture Review: Coach-OS Section Detail Closure

## Verdict on the candidate fix

**Correct in shape, but the ordering premise is wrong.** React 18 batches both `setActiveId` and `setDetail(null)` into the same commit, so calling `detail?.onBack()` synchronously *before* `setActiveId` does not create a "clean abort then switch" sequence — it executes the callback in the current render, then queues both state updates for the same commit. The callback fires against the still-rendered current section (good for cleanup), but the breadcrumb `activePage` and `useCollectionDrill.openId` are not guaranteed to be null before `active?.render()` runs.

## What actually needs to happen

The root cause is that `useCollectionDrill` is **parent-scoped** (App owns it, sections consume it). Section render functions are pure functions of `activeId` + `isSectionActive`. There is no way for a sidebar click to evict `openId` from outside the owning tree without `openId` being lifted to AppFrame.

**Recommendation: lift `openId`/drill state to AppFrame**, behind `useWindowPage` (or alongside it). Then section render functions read drill state from props/hook instead of from a parent-owned `useCollectionDrill`. `navigateToSection` becomes:

1. `setActiveId(nextId)`
2. `drill.reset()` (new exposed reset)
3. `setDetail(null)` + `detail?.onBack?.()` if previous was a CMS detail

This guarantees that on the next render, `active?.render()` sees a fresh drill state — no race, no closure capture of stale `openId`.

## Review questions

- **Batched updates / closures:** Correct concern. The candidate's "synchronous before" claim is misleading — both sets coalesce. The fix is ownership, not ordering.
- **Fleet in WindowContext vs useSectionScopedState:** **Register Fleet detail in WindowContext.** `useSectionScopedState` is a code smell — it exists because the shell's detail contract doesn't cover non-CMS sections. Extending the contract is the right abstraction; per-section escape hatches fragment the model.
- **Stale `detail.onBack`:** Low risk if `onBack` is bound at render time via `useCallback` with `[openId]` deps. If bound stale, you get a closure over a deleted record — recoverable but ugly. Add `useCallback` audit as a regression check.
- **useCollectionDrill change:** Yes — it must move to AppFrame ownership with an exposed `reset()`. Otherwise the candidate fix is a band-aid that breaks on the next multi-label section.

## Minimal patch list

1. `src/components/AppFrame.tsx` — own `useCollectionDrill` here; expose `drill` via context or props to sections.
2. `src/lib/window-page.tsx` (or wherever `useWindowPage` lives) — add `drill` + `drill.reset()`; add `navigateToSection(nextId)` that calls `drill.reset()`, `setDetail(null)`, `onBack?()`, `setActiveId(nextId)` in that order.
3. Section render functions — replace `useCollectionDrill()` calls with `useDrillContext()` (read-only consumer).
4. Fleet — register its detail in `WindowContext` (label + onBack + reset of People/Fleet scoped state). Delete `useSectionScopedState`.
5. Sidebar + voice nav — route through `navigateToSection`.

## Regression scenarios

- **Multi-label section switch (Clients Active→Onboarding):** drill.reset() must fire before render; verify `openId` is null on first render of new label.
- **CMS detail open → sidebar click:** breadcrumb collapses, `onBack` fires once, no double-fire on re-render.
- **Fleet detail open → switch to Clients:** Fleet's onBack runs, then drill resets, then Clients renders empty.
- **Voice nav mid-drill:** same path as sidebar; ensure no race when `setDetail` and `drill.reset` are queued together.
- **Stale `onBack`:** simulate rapid nav clicks; assert `onBack` callback identity is current per render.

## Files referenced

- `C:\Users\amado\coach-os\src\components\AppFrame.tsx`
- `C:\Users\amado\coach-os\src\contexts\WindowContext.tsx` (inferred)
- `C:\Users\amado\coach-os\src\hooks\useCollectionDrill.ts` (inferred)
- `C:\Users\amado\coach-os\src\hooks\useSectionScopedState.ts` (inferred — Fleet)

**Bottom line:** Lift drill state to AppFrame, fold Fleet into WindowContext, delete `useSectionScopedState`. The candidate's intent is right; its mechanism is one layer too shallow.
