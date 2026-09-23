---
session: agent-a9a47d2f3e9aaa360
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\224e0153-4ecc-4860-81fd-6fae419f08b8\subagents\agent-a9a47d2f3e9aaa360.jsonl
debut: 2026-07-30T10:29:35.971Z
fin: 2026-07-30T11:11:07.885Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Read-only exploration. Locate the Coach OS repository under C:\\Users\\amado. Map all currently registered apps,…"
---

## >>> UTILISATEUR #1

Read-only exploration. Locate the Coach OS repository under C:\Users\amado. Map all currently registered apps, their components, current detail/page routing, app metadata/discovery, shared shell, and any app-specific visual styling. Identify exact paths and important symbols. Do not edit anything. Search breadth: very thorough.

### assistant

# Coach OS Repository Map (read-only)

## 1. Repository root

**Path:** `C:\Users\amado\coach-os\`

Key root files:
- `C:\Users\amado\coach-os\package.json` — name `coach-os`, Vite 8 + React 19.2 + TS 6, Tailwind v4, Zustand 5, @supabase/supabase-js 2.110, lucide-react 1.25, motion 12.42, posthog-js 1.407, usertour.js 0.0.24. Scripts: `dev = vite`, `build = tsc -b && vite build`, `lint = oxlint`, `preview = vite preview`.
- `C:\Users\amado\coach-os\vite.config.ts` — plugins: `react()` + `tailwindcss()`.
- `C:\Users\amado\coach-os\index.html` — title `coach-os`, mounts `/src/main.tsx`.
- `C:\Users\amado\coach-os\tsconfig.app.json`, `tsconfig.node.json`, `tsconfig.json`.
- `C:\Users\amado\coach-os\README.md` — describes 13 apps (Dashboard, People/Agents, Operations, IT/R&D, Clients, Tasks, Marketplace, Product, Growth, Sales, Finance, Legal, Settings), each with its own collapsible sidebar + CMS-driven content (Wix-CMS-style model). Forked from A'Space Life OS shell.
- `C:\Users\amado\coach-os\MIGRATION_SUPABASE.md`, `HANDOVER_M3_PHASE0_SUPABASE.md`, `PHASE0_RECEIPT.md` — Supabase data-layer docs.
- `C:\Users\amado\coach-os\public\favicon.svg`, `C:\Users\amado\coach-os\public\icons.svg`.
- `C:\Users\amado\coach-os\src\index.css` — PostHog-light design system, `var(--theme-*)` tokens, `glass`, `glass-card`, custom scrollbar, toast-in keyframes.

## 2. App discovery + registry

**Self-registration mechanism (no per-app register.ts side-effect — Coach OS uses a central barrel).**

- `C:\Users\amado\coach-os\src\main.tsx` — imports `./lib/app-discovery` (side-effect) before rendering.
- `C:\Users\amado\coach-os\src\lib\app-discovery.ts` — central `registerApp({...})` calls for every app + `seedCms()` call. Sets `dockSlot` for dock favourites (0 = Onboarding, 1 = Welcome). `hidden: true` excludes an app from desktop icons (Cognition, Audit).
- `C:\Users\amado\coach-os\src\lib\app-registry.ts` — exposes `AppManifest`:
  - `id`, `name`, `icon: LucideIcon`, `accent?: string`, `description`, `component: ComponentType`, `dockSlot?: number`, `hidden?: boolean`.
  - Global registry stashed on `window.__CITADELLE_APP_REGISTRY__` (Map).
  - API: `registerApp(manifest)`, `getApp(id)`, `getAllApps()`, `getDockApps()`.

## 3. Shared shell

### Boot
- `C:\Users\amado\coach-os\src\App.tsx` — `ThemeApplier` + `Desktop`.
- `C:\Users\amado\coach-os\src\main.tsx` — calls `initObservability()` + `initWindowOpenTracker()` before mount.

### Macros (in render order)
- `C:\Users\amado\coach-os\src\components\Wallpaper.tsx` — paper-garden SVG scene (sun glow, paper grain, layered hills, crop rows) + `<BackgroundFX>` overlay from canvas-ui.
- `C:\Users\amado\coach-os\src\components\TopBar.tsx` — fixed top bar (h-7 inside rounded-2xl glass): brand tile (Leaf icon, emerald→cyan gradient), File/View/Window menu, Reset chip, global theme quick-switcher (Palette → `THEME_META` dropdown), `BorderBeam` ecosystem healthy chip, voice mic (`useVoiceNavigation`), bell (`notificationCount`), clock. Theme applied via `useThemeStore` (`tokensFor('__global__')`).
- `C:\Users\amado\coach-os\src\components\DesktopIcons.tsx` — left-edge icon grid (7 rows × cols), single-click selects, double-click opens via `useShellStore.openApp`. Filters out `hidden: true` apps.
- `C:\Users\amado\coach-os\src\components\WindowFrame.tsx` — draggable/resizable window, traffic lights (`X`, `Minus`, `Maximize2`), 8-direction resize handles, snap-zone preview (left/right half), title bar with breadcrumb row, body slot. Wraps children in `<WindowContext.Provider>` for per-window state. `WindowContext` exports `windowId`, `activePage`, `setActivePage`, `detail`, `setDetail`.
- `C:\Users\amado\coach-os\src\components\Breadcrumbs.tsx` — `App > Section > Item` trail; `meta` label upper-right; section segment is clickable when a detail is open and calls `onBackToActivePage`.
- `C:\Users\amado\coach-os\src\components\Desktop.tsx` — orchestrator. On first mount: clears `coach-os-shell-layout-v1`, calls `restoreLayout()`. If no restored layout → opens onboarding window (auto-maximizes on `/onboarding` or `/demo` paths). Seeds `useDemoShellStore` with 6 citadel windows (`__citadel__`, `ip-vault`, `apps`, `quiz-result`, `compliance`, `audit`); calls `markCitadelSeen()`. Persists layout on `beforeunload`.
- `C:\Users\amado\coach-os\src\components\AppDrawer.tsx` — Launchpad overlay (full-screen `bg-[var(--canvas)]/85 backdrop-blur-2xl`), opens on a window with `id === 'drawer'`. Searchable grid across all registered apps.
- `C:\Users\amado\coach-os\src\components\Toast.tsx` — `ToastContainer` + `ToastItem` (auto-dismiss 5s, animated slide-in).
- `C:\Users\amado\coach-os\src\components\ViewportGuard.tsx` — keeps windows inside safe area on resize.
- `C:\Users\amado\coach-os\src\components\ErrorBoundary.tsx` — `Citadelle app error` fallback with Reload.

### Stores
- `C:\Users\amado\coach-os\src\stores\shell.store.ts` — Zustand store (no persist). State: `windows: AppWindow[]`, `activeWindowId`, `notificationCount`, `toasts`. API: `openApp/closeApp/minimizeApp/maximizeApp/focusApp/updatePosition/updateWindowState`, `bootClean`, `addToast/dismissToast/clearNotifications`, `saveLayout/restoreLayout` (key `coach-os-shell-layout-v1`, schema `0.1.0`, JSON envelope `{ version, state: { windows } }`). `clampPosition`, `nextZ` (cap 1000). Constants: `TOPBAR_HEIGHT = 40`, `DOCK_SAFE_AREA = 100`. Avoids persisting the citadel-only state.
- `C:\Users\amado\coach-os\src\lib\demoShell.ts` — separate Zustand store (`useDemoShellStore`) for the Onboarding Mini Desktop OS. `windows: DemoAppWindow[]`, `activeWindowId`, `openApp/closeApp/closeAll/minimizeApp/maximizeApp/focusApp/updatePosition/updateWindowState`. Persists only `hasBooted` flag via `localStorage` key `demo-coach-boot-flag-v1` (`hasSeenCitadel()` / `markCitadelSeen()`). Citadel window sizes to 820×640 centered.

### Hooks
- `C:\Users\amado\coach-os\src\hooks\useWindowManager.ts` — fork of Life OS drag/resize/snap. Uses `WI
