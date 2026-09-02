---
session: agent-ab035704aebefbd40
projet: subagents
debut: 2026-08-04T20:17:07.224Z
fin: 2026-08-04T20:23:12.576Z
messages_utilisateur: 1
reponses_assistant: 14
---

## >>> UTILISATEUR #1

You are auditing a React 19 + TypeScript desktop-shell application at
`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`.

I need a focused audit of **accessibility and security issues only**. DO NOT MODIFY anything. Read-only.

Output a single bullet list of findings, each in the form:
- **file:line** — Symptom — Cause — Severity (P0/P1/P2/P3) — Suggested fix (one line).

Look ONLY at:

### ACCESSIBILITY (P1 priority)

1. **Clickable `<div>` with onClick but no keyboard handler / no role="button" / no tabIndex={0}**. The desktop has movable window headers — those are draggable. Find `<div onClick={...}>` or `<div onPointerDown={...}>` patterns that lack keyboard equivalents.

2. **Icon-only `<button>` missing `aria-label`**. Search `lucide-react` `<Xxx className>` children of `<button>` without `aria-label` or `title`. Files: `src/components/TopBar.tsx`, `src/components/AppDrawer.tsx`, `src/components/DesktopIcons.tsx`, `src/components/AppFrame.tsx`, `src/components/WindowFrame.tsx`, `src/components/TopBarMenu.tsx`.

3. **`<img>` without `alt`**.

4. **Modal/window without `role="dialog"` `aria-modal="true"`** — WindowFrame is the modal equivalent.

5. **Disabled `<button>` with no `aria-disabled`** and no explanation in the visible label.

6. **`<button>` inside `<button>` or `<a>` inside `<a>`**.

### SECURITY (P1 priority)

7. **`dangerouslySetInnerHTML`**.

8. **Hardcoded secrets** — patterns: `sk-`, `sbp_`, `pk_live_`, `Bearer eyJ`, JWT-shaped strings.

9. **Supabase calls without `.catch()` or try/catch** — `await supabase.from(...)`, `supabase.auth.*`, `supabase.functions.invoke`.

10. **`eval`, `new Function(...)`, `Function('...')`**.

11. **`window.open(url, '_blank')` without noopener**.

12. **`localStorage.setItem(key, ...)` where key looks like a token**.

13. **`postMessage(..., '*')`**.

14. **`target="_blank"` without `rel="noopener noreferrer"`**.

15. **Test key pragma**: search for things that LOOK like dev keys that should not be in a committed file. The `.env.example` file is checked into the repo as a template.

Limit to `src/**`. Return at most 40 findings, grouped by severity.

Format: bullet list, no preamble.

### assistant

I'll audit the codebase systematically for accessibility and security issues. Let me start by exploring the structure.

### assistant

The .env files are in the parent directory which is restricted. Let me continue with the src audit. I'll work without TaskCreate since this is a focused single shot.

### assistant

Good - repository.ts has try/catch. Now let me look at other Supabase usage and security.

### assistant

Now let me look at hardcoded secrets, content rendering, and the rest of the targeted files.

### assistant

Let me look directly in the persisted output for divs with onClick:

### assistant

Now let me look at minidock, breadcrumbs, and tour modals.

### assistant

Now let me look at the Dashboard and OperationsDetailPage for the role="img" patterns and other risks.

### assistant

Now let me check a few more key files: tour.js, marketplace, and store.

### assistant

The cms/repository.ts file wraps everything in try/catch already - that's secure. cognition/queries.ts propagates errors instead - intentional API pattern.

Let me check ThemeDetailPage and a few more places, and check the AppDrawer / window manager.

### assistant

Now let me check the AppDetailOverlay (modal) and Breadcrumb-related modals.

### assistant

Now let me look at the Breadcrumbs disabled state with no aria-disabled, and the ThemeDetailPage SelectOption, and check for buttons with disabled but no aria.

### assistant

Now I have enough to compile the audit. Let me also check the SettingsApp disabled tour button and Button without aria more:

### assistant

I have enough. Let me also check the TourManager tour button in widget.tsx and the role="dialog" usage:

### assistant

Now I have enough data. Let me compile the findings. I have a clear picture of the audit. The trash SalesDetailDrawer is being deleted (in a TRASH folder). Let me put the final report together.

## Findings

### ACCESSIBILITY — P0

- **src/components/WindowFrame.tsx:37-52** — Window-level draggable `<div>` has `onMouseDown={() => focusApp(id)}` and no `role="dialog"` / `aria-modal="true"` / `aria-label`. The window IS the modal equivalent — screen readers can't announce it as a dialog or tell users the window is interactive. — Cause: skipped because keyboard handlers live on titlebar/buttons. — **P0** — Add `role="dialog"` `aria-modal="true"` `aria-label={title}` to the outer window div; close-on-Escape and focus-trap are also missing.

- **src/components/WindowFrame.tsx:61-85** — Titlebar `<div onMouseDown={handleTitleBarMouseDown}>` is the drag handle. Keyboard-only users cannot move or operate the window at all. — Cause: no keyboard equivalent for "maximize" / "move" / window-control. — **P0** — Add keyboard handler (e.g. focus+Arrow keys move, Enter/Space toggles maximize) and `tabIndex={0}` `role="toolbar"` `aria-label="Window controls"`.

- **src/components/WindowFrame.tsx:111-118** — Eight resize-handle `<div>`s use `onMouseDown` only. No role / no tabIndex / no keyboard resize. — Cause: pointer-only assumption. — **P0** — Implement keyboard resize (e.g. focus with Tab, then arrow keys in the relevant direction) and assign `role="separator"` `aria-orientation` `aria-label="Resize <edge>"`.

- **src/apps/onboarding/citadel/DemoWindowFrame.tsx:114-118** — Same draggable titlebar pattern as WindowFrame, no keyboard equivalent. — Cause: copy-paste of macro-frame pattern. — **P0** — Same fix: add `tabIndex={0}` `role="toolbar"` + keyboard move/maximize.

- **src/apps/onboarding/citadel/DemoWindowFrame.tsx:160-167** — Same eight resize-handle `<div>`s as WindowFrame, no keyboard. — Cause: same. — **P0** — Same fix.

### ACCESSIBILITY — P1

- **src/components/TopBar.tsx:320-335** — Notifications bell `<button>` has only `title="Notifications"` and no `aria-label`; an SVG icon is its only child. `title` is not consistently exposed by screen readers. — Cause: missing `aria-label`. — **P1** — Add `aria-label="Notifications (N unread)"` (or similar with the count).

- **src/components/TopBar.tsx:108-120** — Profile-menu action buttons (Settings / Billing / AI / Sign out) render only icons (`<SettingsIcon>`, `<CreditCard>`, `<Sparkles>`, `<LogOut>`) as the visual cue but the text label is present — they are NOT icon-only. — Mark: false-positive, these are labelled. **Skip.**

- **src/components/AppDrawer.tsx:31-36** — Launchpad close `<button>` contains only `<X />` and has no `aria-label`/`title`. — Cause: missing. — **P1** — Add `aria-label="Close Launchpad"`.

- **src/components/Toast.tsx:49-51** — Toast dismiss `<button>` contains only `<X />` with no `aria-label`. — Cause: missing. — **P1** — Add `aria-label="Dismiss notification"`.

- **src/components/Breadcrumbs.tsx:19-26** — Back-arrow `<button>` with only `<ArrowLeft />`; relies on `title="Back to list"` only when `onBackToActivePage` is set. No `aria-label` at all. — Cause: missing. — **P1** — Add `aria-label="Back"`.

- **src/components/Breadcrumbs.tsx:37-49** — Section crumb `<button disabled={isLast || !isClickableSection}>` has no `aria-disabled` (the `disabled` HTML attribute is present, which is fine, but the visible label is the only context — `aria-current="page"` would help the last crumb). — Cause: missing `aria-current`. — **P2** — Add `aria-current="page"` to the last crumb button.

- **src/components/AppFrame.tsx:435-442** — Tool `<button disabled={tool.status === 'running'}>` has no `aria-disabled` and no visible explanation that "Running…" is the reason; the visible label changes but a screen reader reading the disabled-button label may not announce disabled state on all browsers. — Cause: missing `aria-disabled={true}` and explanatory `aria-describedby`. — **P1** — Add `aria-disabled={tool.status === 'running'}` and `title` or `aria-describedby` pointing to the status badge.

- **src/apps/settings/SettingsApp.tsx:369-381** — Replay-tour button `disabled={!consentOn}` shows no visible explanation of why it's disabled (just greyed out). — Cause: no `aria-disabled` or hint added. — **P2** — Add `aria-disabled={!consentOn}` and surface adjacent consent-inactive hint.

- **src/apps/onboarding/OnboardingApp.tsx:237-243** — Back-step `<button disabled={stepIdx===0}>` has no `aria-disabled`. — Cause: missing. — **P2** — Add `aria-disabled`.

- **src/apps/onboarding/OnboardingApp.tsx:245-250** — Next-step `<button disabled={answers[q.id] === undefined}>` has no `aria-disabled`. — Cause: missing. — **P2** — Add `aria-disabled` and `aria-describedby` pointing to the question.

- **src/components/cms/itemDetailShared.tsx:53-79** and **src/components/cms/DynamicPageView.tsx:163-184** — Prev/Next `<button disabled={!prev}>` / `disabled={!next}` lack `aria-disabled` and a meaningful label describing the action. — Cause: missing. — **P2** — Add `aria-label="Previous item"` / `aria-label="Next item"` and `aria-disabled`.

- **src/components/WindowFrame.tsx:139-150** — Traffic-light close/minimize/maximize buttons have `aria-label` ✓ but are 14×14 px (very small touch target). Not the audit's precise scope but **P1** for keyboard users — keep on the list.

- **src/components/AppFrame.tsx:192-198** — Sidebar-collapse `<button>` has only `title={...}` (no `aria-label`); contains `PanelLeftClose`/`PanelLeftOpen` lucide icons. — Cause: missing `aria-label`. — **P1** — Add `aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}`.

- **src/components/AppFrame.tsx:218-242** — Theme-chip `<button>` has `title` only — no `aria-label`. — Cause: missing. — **P2** — Add `aria-label="Open theme settings"`.

- **src/components/AppFrame.tsx:352-358** — Tools-panel collapse `<button>` has only `title`, no `aria-label`. — Cause: missing. — **P
