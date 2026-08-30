---
session: agent-a20a53792dc7eaad6
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a20a53792dc7eaad6.jsonl
debut: 2026-07-25T09:42:20.974Z
fin: 2026-07-25T10:03:02.421Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Read-only audit. Do NOT edit, commit, or push anything. Target: C:\\Users\\amado\\coach-os (Windows path; use for…"
---

## >>> UTILISATEUR #1

Read-only audit. Do NOT edit, commit, or push anything.

Target: C:\Users\amado\coach-os (Windows path; use forward slashes in tools).

Scope: src/apps/ — read every file. Also read src/contexts/WindowContext.ts (or .tsx — find it via Glob) and src/components/AppFrame.tsx, src/hooks/useCollectionDrill.ts (or wherever it lives — grep for it). Do NOT touch src/components/AppFrame.tsx beyond READING, and do not touch useCollectionDrill internals or WindowContext internals.

Two touchpoints in scope (read carefully, do not modify):
- src/components/AppFrame.tsx (ActiveRender wrapper with key={active.id})
- src/apps/people/PeopleApp.tsx (render: Fleet alignment)

Task — Detail / breadcrumb contract audit:
For every file in src/apps/, identify every "detail view" — any section that opens a focused view of a single item (a client card, a task, a deal, a contract, a roadmap item, a People/Fleet agent, etc.). For each one, confirm EITHER:
  (a) the detail is registered in WindowContext via setDetail({ label, onBack }) before rendering, OR
  (b) the detail uses useCollectionDrill (which auto-registers and provides onBack via context).

For each detail view, cite file:line and report the registration mechanism. Flag any detail view that renders a single-item focused UI without either registration mechanism — that's a bug (no breadcrumb = no back button).

Then cross-check AppFrame.tsx's `navigateToSection` (or equivalent handler that switches active app): does it call `detail?.onBack()` BEFORE `setActiveId(...)`? This is the structural fix being verified. If onBack is missing or called after setActiveId, that's the bug the previous turn was meant to fix.

Also check: when a user clicks a sidebar section while a detail view is open, does the active app change? If yes, does the detail close cleanly? Look for any state where the detail is left dangling because the wrapper remounts (key={active.id} forces remount — that should be fine) but useCollectionDrill's listener is unsubscribed on unmount.

Look for these specific patterns and flag if present:
- A `setDetail(...)` call without a paired `onBack` (stuck back button)
- A detail view that uses local state instead of WindowContext (won't show breadcrumb)
- Any "Back" button that calls `setDetail(null)` without calling the previous `onBack` first
- The PeopleApp Fleet alignment specifically — is `useCollectionDrill` being used correctly when clicking an agent card? The previous turn's KEY test is "click Orchestrator → click Content". Verify the breadcrumb survives both clicks.

Output: a single markdown report, file:line citations, P0/P1/P2 severity on each finding. Under 500 words.

### assistant

# Detail / Breadcrumb Contract Audit

**Scope:** Read all 27 files under `C:/Users/amado/coach-os/src/apps/`, plus the requested context, hook, and frame files.

## Detail-view coverage

All focused single-item views have a valid registration mechanism:

- **Dashboard clients:** `/C:/Users/amado/coach-os/src/apps/dashboard/DashboardApp.tsx:41,49,85` — `useCollectionDrill`.
- **Clients:** `/C:/Users/amado/coach-os/src/apps/clients/ClientsApp.tsx:13-14,22,51,81,107,133` — client and session-note drills.
- **Tasks:** `/C:/Users/amado/coach-os/src/apps/tasks/TasksApp.tsx:13,58,62,66` — `useCollectionDrill`.
- **Sales:** `/C:/Users/amado/coach-os/src/apps/sales/SalesApp.tsx:32,37,65` — `useCollectionDrill`.
- **Finance invoices:** `/C:/Users/amado/coach-os/src/apps/finance/FinanceApp.tsx:52,57` — `useCollectionDrill`.
- **Product roadmap/backlog/releases/specs:** `/C:/Users/amado/coach-os/src/apps/product/ProductApp.tsx:58-59,66,90,118,146` — two drills.
- **Operations:** `/C:/Users/amado/coach-os/src/apps/operations/OperationsApp.tsx:55-57,61,89,117` — three drills.
- **IT/R&D:** `/C:/Users/amado/coach-os/src/apps/it-rd/ItRdApp.tsx:12-14,21,33,58` — three drills.
- **Growth:** `/C:/Users/amado/coach-os/src/apps/growth/GrowthApp.tsx:34-35,39,62` — two drills.
- **Marketplace:** `/C:/Users/amado/coach-os/src/apps/marketplace/MarketplaceApp.tsx:13,53-60` — one drill.
- **Legal:** `/C:/Users/amado/coach-os/src/apps/legal/LegalApp.tsx:23-24,54,66` — two drills.
- **People Team/Agents:** `/C:/Users/amado/coach-os/src/apps/people/PeopleApp.tsx:517-518,524,536` — two drills.
- **People Fleet agent detail:** `/C:/Users/amado/coach-os/src/apps/people/PeopleApp.tsx:277-290` — mechanism (a), explicit `setDetail({ label, onBack })`; card click is at `:310`, detail Back delegates at `:132-136`.

`useCollectionDrill` auto-registers and cleans up the breadcrumb at `/C:/Users/amado/coach-os/src/hooks/useCollectionDrill.ts:28-42`. `DynamicPageView` delegates its Back button through `onBack` at `/C:/Users/amado/coach-os/src/components/cms/DynamicPageView.tsx:47-49`.

## Structural checks

- **PASS:** `/C:/Users/amado/coach-os/src/components/AppFrame.tsx:75-80` calls `detail?.onBack()` before `setDetail(null)` and `setActiveId(nextId)`.
- **PASS:** `key={active.id}` remounts the active section at `:281`.
- **PASS:** People Fleet’s Orchestrator → Content transition closes local selection, clears the detail, then changes section.
- **PASS:** No `setDetail(...)` lacks `onBack`; no Back button directly clears context incorrectly.

## Findings

- **P0:** None.
- **P1:** None.
- **P2:** `/C:/Users/amado/coach-os/src/hooks/useCollectionDrill.ts:37-42` does not clear `detail` if an open item disappears from the collection. `DynamicPageView` then returns `null` at `/C:/Users/amado/coach-os/src/components/cms/DynamicPageView.tsx:30`, potentially leaving a stale breadcrumb.
