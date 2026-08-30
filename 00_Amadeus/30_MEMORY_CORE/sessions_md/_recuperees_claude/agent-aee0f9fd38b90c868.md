---
session: agent-aee0f9fd38b90c868
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\224e0153-4ecc-4860-81fd-6fae419f08b8\subagents\agent-aee0f9fd38b90c868.jsonl
debut: 2026-07-30T10:29:36.155Z
fin: 2026-07-30T11:08:52.429Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Read-only exploration. Locate Coach OS and analyze its frontend architecture/design system: tokens, CSS strate…"
---

## >>> UTILISATEUR #1

Read-only exploration. Locate Coach OS and analyze its frontend architecture/design system: tokens, CSS strategy, component library, routing/navigation, responsive shell, themes, motion, accessibility patterns. Also identify visual debt relevant to building distinct app detail pages. Return exact file paths and reusable utilities. Do not edit anything. Search breadth: very thorough.

### assistant

# Coach OS — Frontend Architecture & Design System Audit

**Root:** `c:/Users/amado/coach-os/` (a separate project from this worktree)
**Stack:** Vite + React 19 + TypeScript, Tailwind v4, Zustand, lucide-react, motion (Framer), Supabase JS, PostHog, UserTour.
**Cited at:** `c:/Users/amado/coach-os/README.md`, `c:/Users/amado/coach-os/package.json` (lines 12-34).

---

## 1. Boot sequence & routing model (no react-router)

Coach OS is a **windowed desktop OS, not an SPA with routes**. Navigation is done by manipulating a Zustand shell store of open windows + per-window section state.

| Concern | File | Notes |
|---|---|---|
| Entry / boot side-effects | `c:/Users/amado/coach-os/src/main.tsx` | StrictMode + 3 side-effect inits |
| `<App>` wrapper | `c:/Users/amado/coach-os/src/App.tsx` | Mounts `<ThemeApplier>` + `<Desktop>` |
| Desktop shell (the OS) | `c:/Users/amado/coach-os/src/components/Desktop.tsx` | Renders `<Wallpaper>`, `<TopBar>`, `<DesktopIcons>`, `<AnimatePresence>` of `<WindowFrame>`s, `<ToastContainer>`, `<AppDrawer>` |
| Window manager engine | `c:/Users/amado/coach-os/src/stores/shell.store.ts` | Open/close/min/max/focus, z-order, position/size clamp, localStorage persistence (`coach-os-shell-layout-v1`) |
| Native drag/resize/snap hook | `c:/Users/amado/coach-os/src/hooks/useWindowManager.ts` | RAF-throttled, edge-resize handles, half-screen snap |
| Window constraints | `c:/Users/amado/coach-os/src/types/window.types.ts` | `MIN_W=420`, `MIN_H=320`, `TOPBAR=40`, `DOCK=100`, `SNAP=20` |
| Viewport boundary guard | `c:/Users/amado/coach-os/src/components/ViewportGuard.tsx` | 2s tick + resize listener re-clamps window positions |
| App registry (manifest-based plugin) | `c:/Users/amado/coach-os/src/lib/app-registry.ts` | Global `Map` keyed by app id, `registerApp()` side-effect, `getApp/getAllApps/getDockApps` |
| App discovery (boot wiring) | `c:/Users/amado/coach-os/src/lib/app-discovery.ts` | Side-effect import registers all 17 apps incl. hidden `cognition`/`audit` |
| Per-window sub-routing | `c:/Users/amado/coach-os/src/contexts/WindowContext.tsx` | `useWindowPage()` exposes `{activePage, setActivePage, detail, setDetail, windowId}` to drill App → Section → Item |
| URL-driven onboarding entry | `c:/Users/amado/coach-os/src/components/Desktop.tsx` (lines 20-26, 48-65) | Reads `window.location.pathname` — `/onboarding` and `/demo` auto-maximize the onboarding window. No react-router; manual `pathname` checks. |

**Reusable routing/navigation utilities:** `useWindowPage`, `useShellStore.openApp/closeApp/...`, `useVoiceIntentStore` (one-shot section/item intents per window), `useCollectionDrill` (collection list↔detail state).

---

## 2. Design tokens — two layers

### 2a. Hard-coded global CSS tokens (root layer)
File: `c:/Users/amado/coach-os/src/index.css`
- `:root` defines `--theme-accent` (`#f08143` PostHog-orange), `--theme-text` (`#292524` stone-800), `--canvas` (`#f4f5f0`), `--panel`, `--panel-border`, `--shadow-window`, `--shadow-panel`, `--topbar-height: 40px`.
- `@layer utilities` exposes `.top-bar`, `.glass` (floating chrome — `blur(20px) saturate(1.4)`), `.glass-card`, `.custom-scrollbar`, `.no-scrollbar`.
- Single keyframe `@keyframes toast-in` + `.animate-toast-in`.
- Google Fonts import: Inter (body) + Outfit (display). No `@font-face` self-hosting.
- Tailwind v4 single import: `@import "tailwindcss";` + `@tailwindcss/vite` plugin (`vite.config.ts`).

### 2b. Runtime theme tokens (12 themes × ~17 tokens, scoped per app)
File: `c:/Users/amado/coach-os/src/lib/themes/tokens.ts`
- Type `ThemeTokens`: accent (hex + rgb + hover + soft), bg/canvas/surface/surfaceHover, text/textMuted/textDim, border/borderSubtle, radius/radiusSm/radiusLg, shadow/shadowLg, blur, fontDisplay/fontBody, isDark.
- 12 themes registered: `warm-paper`, `glassmorphism`, `neumorphism`, `brutalism`, `dark-oled`, `aurora`, `cyberpunk`, `editorial`, `liquid-glass`, `claymorphism`, `trust`, `vibrant-block`. Each carries `sourceStyleId`, `description`, `bestFor: appId[]`, `mood`, `lightMode/darkMode`.
- `CANONICAL_APP_THEMES` mapping app → default theme (17 apps, e.g. `sales → liquid-glass`, `finance → trust`, `it-rd → cyberpunk`).
- `THEME_META` precomputed convenience accessors.

### 2c. Theme applier + store
- `c:/Users/amado/coach-os/src/lib/themes/ThemeApplier.tsx` — mounts once at `<App>`, applies tokens to `:root` on `globalTheme` change, sets `data-theme` + `data-theme-dark` attributes.
- `c:/Users/amado/coach-os/src/lib/themes/store.ts` — Zustand+persist store (`coach-os-themes-v1` localStorage). Exports `applyThemeTokens(target, tokens, prefix)` which writes `--theme-*` CSS variables to any DOM node. Per-app theme overrides via `appThemes[appId]`. Includes a `_v` sentinel to defeat shallow-equality (line 33-34).
- `useThemeFor(appId)` and `useThemeIdFor(appId)` — subscribed hooks.
- AppFrame applies per-app tokens as scoped CSS vars on its own root → each window gets its own design identity while the global shell uses the global theme (`c:/Users/amado/coach-os/src/components/AppFrame.tsx` lines 86-91).

### 2d. Background FX (canvasui.dev integration)
- `c:/Users/amado/coach-os/src/components/canvas-ui/theme-canvas-mapping.ts` — 12 themes × 9 canvasui components (`Asciify`, `Bend`, `Blaze`, `Bubble`, `Frost`, `Glitch`, `LiquidMetal`, `Particle`, `ThinkingOrbs`).
- `BackgroundFX.tsx` (lines 41-69) — switch-case dispatching to the per-theme effect.
- All canvasui components (`Asciify.tsx`, `Bend.tsx`, `Blaze.tsx`, `BorderBeam.tsx`, `Bubble.tsx`, `Frost.tsx`, `Glitch.tsx`, `LiquidMetal.tsx`, `Particle.tsx`, `ThinkingOrbs.tsx`) are **GPU-accelerated** (transform/opacity only), pause off-screen via IntersectionObserver, and respect `prefers-reduced-motion` (see `BorderBeam.tsx` lines 44-49, `ThinkingOrbs.tsx` lines 40-44).
- `Wallpaper.tsx` — fixed full-bleed gradient + SVG paper-garden scene + theme-driven `<BackgroundFX>` overlay (mix-blend-mode: screen).

---

## 3. Component library
