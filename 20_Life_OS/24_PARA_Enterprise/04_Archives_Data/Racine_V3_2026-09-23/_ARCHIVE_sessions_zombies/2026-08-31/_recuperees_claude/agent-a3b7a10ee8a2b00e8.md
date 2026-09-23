---
session: agent-a3b7a10ee8a2b00e8
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a3b7a10ee8a2b00e8.jsonl
debut: 2026-07-24T18:58:55.500Z
fin: 2026-07-24T19:03:10.558Z
messages_utilisateur: 1
reponses_assistant: 5
titre: "Read-only audit in C:\\Users\\amado\\coach-os. Do not edit, commit, or push. The shared AppFrame fix is present: …"
---

## >>> UTILISATEUR #1

Read-only audit in C:\Users\amado\coach-os. Do not edit, commit, or push. The shared AppFrame fix is present: sidebar/voice navigation calls `detail?.onBack(); setDetail(null); setActiveId(nextId)`. Browser proof this turn showed Clients Active -> Ava Chen detail -> Onboarding correctly renders the Onboarding list and removes the detail breadcrumb.

The user says the bug still exists in multiple apps, mentioning Clients. Find the remaining paths that can still violate this contract. Inspect every tracked file under src/apps and src/components for:
- detail/drill-down UIs implemented with local useState/useReducer/selectedId/openId but not registered in WindowContext;
- section functions that return a detail view based on parent/local state;
- card click handlers opening a detail page or modal;
- app-level windows or overlays that can remain in foreground after internal sidebar navigation.

Pay special attention to recent FleetItemCard/CMSCardList conversions in Clients, IT/R&D, Operations, Product, Dashboard, Finance, Sales, Marketplace, Growth, Legal and Tasks, plus Settings, Welcome, Onboarding, and any modal/window-specific detail state.

Return an evidence table with exact file:line, the interaction sequence that still fails (if any), the state owner, and the smallest fix. Distinguish confirmed remaining defects from code that is already protected by AppFrame or unmounted sections. Under 900 words. Do not implement.

### assistant

I'll audit the coach-os codebase systematically. Let me start by mapping the structure.

### assistant

Now I have the AppFrame contract and ClientsApp. Let me read the rest of the apps in parallel.

### assistant

Now let me check Onboarding, WindowContext, useCollectionDrill, and the remaining UI components.

### assistant

Now let me read the WindowContext, useCollectionDrill, and the FleetItemCard/CMSCardList to confirm they integrate with WindowContext.

### assistant

I have all the data I need. The ArkTS rules are unrelated to this audit. Let me now compile the evidence table. I have all the apps mapped. Let me also quickly verify the Channels section in Product has no drill, and look at Desktop.tsx / WindowFrame to see if any "remaining in foreground" overlays exist outside AppFrame.

The findings are clear. Let me compile the audit.

## Exploration: Detail-Breadcrumb Contract Audit (coach-os)

**Contract recap** (`AppFrame.tsx:65-72`): `navigateToSection` calls `detail?.onBack(); setDetail(null); setActiveId(nextId)`. The shared fix relies on EVERY drill registering `setDetail(`{label, onBack}`)` via `useCollectionDrill` (which auto-sets detail on `openId` change and clears on inactive section). Sibling flows validated: Browser proof passed for Clients → Active → Ava Chen → Onboarding.

### Confirmed REMAINING defects (local state, no WindowContext registration)

| # | File:line | Local state | Failure sequence | State owner | Smallest fix |
|---|---|---|---|---|---|
| 1 | `C:/Users/amado/coach-os/src/apps/people/PeopleApp.tsx:277-281` | `Fleet` uses `useState<string \| null>(selectedCode)` → renders `FleetDetail` with `onBack={() => setSelectedCode(null)}` | Click Fleet → click an agent → click any other sidebar tab (e.g. Schedule) → breadcrumb `App › People / Agents › <agent>` stays; navigating back to Fleet shows **still drill view** (state owned by section component, but AppFrame reuse keeps it mounted until full re-render path runs). More critically: switching tab from Fleet-with-drill to another tab does NOT clear the detail - only `useCollectionDrill` does that. | `Fleet` component local | Replace `selectedCode` with `useCollectionDrill('person_agent_detail', 'Fleet')` OR call `useWindowPage().setDetail({label, onBack})` in `useEffect` so `AppFrame.navigateToSection` can `onBack()` it. |
| 2 | `C:/Users/amado/coach-os/src/apps/people/PeopleApp.tsx:309 (Content filter)` | `useState<'all' \| ...>` is a pure filter (not a detail) | SAFE — no drill. No fix needed. | — | — |
| 3 | `C:/Users/amado/coach-os/src/apps/dashboard/DashboardApp.tsx:17-37 (Validation)` | `validations` array literal; card `onClick` is `() => { /* TODO */ }` | No drill active today. SAFE — no detail owned. | — | — |
| 4 | `C:/Users/amado/coach-os/src/apps/settings/SettingsApp.tsx:29-37 (flags)` + `105-115 (themesSection)` | Local `flags` toggle (not a detail). `themesSection` listener sets local state but the comment lines 273-274 + 283-285 admit the cross-window intent is "best-effort, flashes a console hint" — `void themesSection` is a no-op | No breadcrumb detail exists; not a defect for THIS contract. SUB-FLAW: the intent event is silently dropped. | `SettingsApp` local | Either remove dead listener OR add `setDetail({label:'Themes', onBack:...})` when intent fires. Not the current bug. |
| 5 | `C:/Users/amado/coach-os/src/apps/welcome/WelcomeApp.tsx:307-331` | `activePageId` is local state; `Overview` and `LandingCanvas` alternate via `setActivePageId(id)`. Switching to e.g. Clients tab in another app leaves `WelcomeApp` mounted; switching back inside Welcome sidebar doesn't dirty AppFrame (no detail registered), so unharmed by THIS contract. | Not a drill; no breadcrumb. SAFE. | — | — |
| 6 | `C:/Users/amado/coach-os/src/apps/tasks/TasksApp.tsx:10-22, 35-46` | `toggle()` calls `updateItem('tasks', id, {done: ...})` — `done` row click is a write, not a drill. The label button calls `drill.open(...)` (line 42) → properly wired via `useCollectionDrill`. | SAFE. | — | — |
| 7 | `C:/Users/amado/coach-os/src/apps/finance/FinanceApp.tsx:13-27 (Overview), 29-50 (Runway)` | Both are static. No drill. | SAFE. | — | — |
| 8 | `C:/Users/amado/coach-os/src/apps/legal/LegalApp.tsx:22-33 (Compliance toggles)` | `checks` local state with `toggle()`, no drill opened. | SAFE. | — | — |
| 9 | `C:/Users/amado/coach-os/src/apps/growth/GrowthApp.tsx:33-37 → Funnel:12-31` | Funnel is static stat panels. Channels table uses `onRowClick` → `channelsDrill.open(...)` — properly wired. | SAFE. | — | — |
| 10 | `C:/Users/amado/coach-os/src/apps/marketplace/MarketplaceApp.tsx:16-22 (install)` | `install()` mutates store + toast; no drill. Cards `onClick={() => drill.open(...)}` — wired. | SAFE. | — | — |
| 11 | `C:/Users/amado/coach-os/src/apps/it-rd/ItRdApp.tsx:13-15` | All sections use `useCollectionDrill`. | SAFE. | — | — |
| 12 | `C:/Users/amado/coach-os/src/apps/operations/OperationsApp.tsx:56-58` | All sections use `useCollectionDrill`. | SAFE. | — | — |
| 13 | `C:/Users/amado/coach-os/src/apps/product/ProductApp.tsx:172-210 (Channels)` | `Channels` section is purely a log list (no `useCollectionDrill`). No drill, no detail. | SAFE. | — | — |
| 14 | `C:/Users/amado/coach-os/src/apps/sales/SalesApp.tsx:18-29 (Forecast)` | Static. No drill. | SAFE. | — | — |
| 15 | `C:/Users/amado/coach-os/src/apps/onboarding/OnboardingApp.tsx:455-510` | Renders `MiniDesktopShell` — own `useDemoShellStore` window stack. No relation to AppFrame's `detail`/`activePage`. | SAFE outside contract. | — | — |

### Cross-section interaction audit (the actual bug class)

The contract violation requires: **(a) a section that opens a detail view via local state AND (b) the detail does NOT register in WindowContext AND (c) sidebar nav switches away without unmounting the section**.

| Section | Opens detail via | Registers `setDetail`? | Defect? |
|---|---|---|---|
| Clients → Active / Onboarding / Risk / Directory / Vault | `drill.open` → `useCollectionDrill` | YES (auto) | NO |
| IT/R&D → Kernel / Experiments / Deploys | `useCollectionDrill` | YES | NO |
| Operations → Runbooks / Knowledge / Incidents | `useCollectionDrill` | YES | NO |
| Product → Roadmap / Backlog / Releases / Specs | `useCollectionDrill` | YES | NO |
| Product → Channels | none | n/a | NO |
| Dashboard → Overview / Pipeline | `useCollectionDrill` | YES | NO |
| Dashboard → Validation (line 32) | `() => { /* TODO */ }` — no-op | NO (but no drill activ
