---
session: agent-a48c068d810dadf5c
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\9259fd84-cac8-42d3-be20-1cfbddc4fec7\subagents\agent-a48c068d810dadf5c.jsonl
debut: 2026-07-30T15:36:04.445Z
fin: 2026-07-30T15:43:04.331Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "You are planning the implementation of the real upstream `canvas-ui` library (https://github.com/DavidHDev/can…"
---

## >>> UTILISATEUR #1

You are planning the implementation of the real upstream `canvas-ui` library (https://github.com/DavidHDev/canvas-ui) into the Coach OS Vite + React 19 project at `C:/Users/amado/coach-os/`. **Read-only** planning task — produce a detailed implementation plan, do not edit any files.

## Context from Phase 1 (already verified)

### Coach OS architecture (verified)
- React 19 + Vite 8 + Tailwind 4 + TypeScript 6 + Zustand 5. SPA, no SSR.
- 12 themes in `src/lib/themes/tokens.ts` (id, name, accent, etc.) + `src/lib/themes/store.ts` Zustand store (`coach-os-themes-v1` localStorage persist).
- Per-window theme scoping via `AppFrame.tsx` (writes scoped CSS vars to its root div).
- 19 apps registered in `src/lib/app-discovery.ts` (Dashboard, People, Operations, IT-R&D, Clients, Tasks, Marketplace, Product, Growth, Sales, Cognition, Audit, Finance, Legal, Settings, Onboarding, Welcome, Design — plus others).
- Settings app exposes the theme picker.
- `applyThemeTokens(target, tokens)` writes scoped CSS variables imperatively.
- 13 hand-rolled CSS/SVG **sister-pattern** components currently live in `src/components/canvas-ui/` — user explicitly called these "minor effects / bubbles / rien à voir avec Canvas UI". They must be **replaced entirely**.
- The 13 existing files: Asciify.tsx, BackgroundFX.tsx, Bend.tsx, Blaze.tsx, BorderBeam.tsx, Bubble.tsx, Frost.tsx, Glitch.tsx, LiquidMetal.tsx, Particle.tsx, ThinkingOrbs.tsx, theme-canvas-mapping.ts, index.ts.
- Currently 3 of them are wired: BackgroundFX (in Wallpaper.tsx), BorderBeam + ThinkingOrbs (in TopBar.tsx).

### canvas-ui upstream (verified by WebFetch)
- Distribution model: **shadcn-registry style** — `npx shadcn@latest add @canvas-ui/<name>-react` (or `bash`/`vue` framework variants). Components drop source files into your project (typically `src/components/canvasui/`).
- NOT a normal npm package. The exact source paths are documented on https://canvasui.dev/docs and the README at https://github.com/DavidHDev/canvas-ui/blob/main/README.md.
- React 19 + Vite + Tailwind 4 supported.
- ~30 components: **Asciify, ASCII Object, Bend, Blaze, Bubble, Canvas, Cloth, Clouds, Decrypt Reveal, Dithered Object, Displacement, Droplets, Flame Wrap, Force Field, Frost, Glass, Glass Object, Glitch, Glyph Rain, Grid, Hex Float, Laser, Liquid, Liquid Object, Magnify, Particle Object, Particle Reveal, Particle Scroll, Peel, Retro Dither, Ripple, Shatter, VHS**.
- All components use WebGL (or experimental HTML-in-Canvas API `chrome://flags/#canvas-draw-element`).
- Three.js is required for `* Object` family (ASCII Object, Dithered Object, Glass Object, Particle Object, Liquid Object). Install `three` + `@types/three` dev dep.
- Component families:
  - **Wrappers** (children required, capture subtree): Liquid, Ripple, Cloth, Droplets, Bubble, Displacement, Blaze, Flame Wrap, Force Field, Laser, Glass, Frost, Magnify, Bend, Peel, Clouds, VHS, Glitch, Retro Dither, Asciify, Decrypt Reveal, Glyph Rain, Particle Reveal, Particle Scroll, Shatter, Grid, Hex Float, Canvas
  - **3D Object components** (`src` URL prop, no children): ASCII Object, Dithered Object, Glass Object, Particle Object, Liquid Object

### User decisions (locked)
1. **Replace entirely**: delete all 13 hand-rolled components, replace with the real upstream 30.
2. **Allocation rule: 1 dominant + 2 nuance per theme**: each of the 12 themes gets 1 signature effect (used as BackgroundFX on Wallpaper / per-app background) + 2 nuance effects (used inline in app section content). 12×3 = 36 slots, 6 excess effects — these become "neutral" effects that can be picked per-app via Settings.
3. **Source strategy: manual download from GitHub raw** — no shadcn init. Surgical.

## Your task — produce a complete implementation plan

For each of the sections below, give concrete, actionable output (no abstract advice — actual file paths, code snippets, table cells).

### 1. File-system plan
- Exact file paths for the 30 new component files (where they land)
- What happens to the 13 existing files (literal `git rm` paths)
- New directory structure (recommendation: `src/components/canvasui/v30/` for the real components + `src/components/canvasui/_v1_css_retired/` for the dead-code archive — explain D4 append-only compliance)

### 2. Dependencies plan
- `npm install` commands for `three` + `@types/three` (dev)
- Anything else needed (e.g., if any component requires a CSS preprocessor plugin not already in vite.config.ts)
- vite.config.ts modifications if any
- tsconfig.json modifications if any (Bend uses `layoutsubtree` JSX attribute → React 19 may need `@ts-expect-error` or a custom HTML attribute type)

### 3. Theme-mapping table (12 themes × 30 effects)
Use the user's "1 dominant + 2 nuance per theme × 12 themes" rule to propose the EXACT distribution:
- Which 1 effect is "dominant" for each of the 12 themes (theme key, effect, rationale)
- Which 2 effects are "nuance" for each (in priority order — primary first, secondary second)
- The 6 "neutral" leftover effects (assigned to a `neutral` slot in the mapping, available via Settings per-app override)

Propose the distribution. Justify each dominant choice in 1 sentence based on what you know about each theme's personality (glassmorphism = translucent Frost is obvious, etc.). For effects you don't have personality details on, note as "needs verification post-installation".

### 4. App-mapping plan
- Which of the 19 apps get ONE of the existing "nuance" effects as their signature element (cross-reference app id → theme id → nuance effect)
- Default: 1 effect per app, mounted near the AppFrame header or section content
- List the 5-7 apps that should NOT get a canvas-ui effect (e.g. onboarding, settings-themes is itself the picker)

### 5. Architecture plan
- The new `theme-canvas-mapping.ts` schema: `THEME_TO_CANVAS_UI`, `getCanvasMapping`, `renderCanvasForTheme` — adapt to the new 30-component set.
- `BackgroundFX.tsx` replacement strategy: per-window scope (read from `useThemeIdFor(appId)`) AND per-global-theme (read from `useThemeIdFor('global')` for Wallpaper).
- How Settings app exposes the neutral/nuance palette picker (it's already in place for themes — extend it).
- D6 honest: WebGL fallback story for non-Chrome browsers + low-power hardware.

### 6. Implementation phases
- Phase A (cleanup): `git rm` 13 CSS files, mark as deprecated in wiki/hand_offs (D4 compliance)
- Phase B (deps): install three, update vite.config.ts, update tsconfig if needed
- Phase C (download): download all 30 source files via WebFetch + Write. Note each canonical GitHub raw URL pattern (e.g. `https://raw.githubusercontent.com/DavidHDev/canvas-ui/main/react/<kebab-case>/<Name>.tsx`)
- Phase D (mapping): rewrite theme-canvas-mapping.ts with new 30-component schema
- Phase E (integration): update BackgroundFX.tsx + Wallpaper.tsx + TopBar.tsx + the 5-7 target apps
- Phase F (Settings): extend theme picker to show the 3-available-effects per theme
- Phase G (verification): npx tsc --noEmit, dev server, manual render of each of the 30 in design/showcase page

### 7. Verification plan
- Concrete commands and observable outputs to confirm each phase succeeded
- E2E test: open Coach OS in browser, click through each app, see at least one real canvas-ui effect render

### 8. Risks / D6 honest gaps
- WebGL on Chromebook / Raspberry Pi
- HTML-in-Canvas Chrome flag dependency
- Bend's `layoutsubtree` JSX attribute with React 19
- Source file drift between canvas-ui commits
- 3D Object family dependency on `three` types

Return: a single coherent plan document. Cite specific file paths from `C:/Users/amado/coach-os/`. Avoid generic advice. Where you're not certain, say "post-installation verification needed" rather than guessing.

### assistant

I have enough context to produce the comprehensive plan. Here it is as my final assistant message.

---

# Implementation Plan — Real Upstream `canvas-ui` Integration into Coach OS

**Path scope:** `C:/Users/amado/coach-os/`
**Mode:** Read-only planning (no edits performed). Plan returned inline; per the constraints in this session, the plan file at `C:\Users\amado\.claude\plans\je-t-aivais-demander-d-implementer-recursive-hinton-agent-a48c068d810dadf5c.md` is **not** written in this turn because the read-only planning system prompt forbids all file writes.
**Status of locked decisions (recap):** Replace the 13 hand-rolled CSS/SVG components entirely with the real upstream 30 (drop-in source files from `DavidHDev/canvas-ui`). 1 dominant + 2 nuance per theme × 12 themes = 36 slots; 6 leftover effects = "neutral" pool available via Settings override. Source strategy: manual `WebFetch` of GitHub raw, surgical paste into `src/components/canvasui/v30/`. Archive the 13 retired files to `src/components/canvasui/_v1_css_retired/` per D4 append-only compliance.

---

## 1. File-system plan

### 1.1 New `v30` directory layout (real upstream source drops)

All 30 components land under `src/components/canvasui/v30/` (one file per component, identical naming convention as upstream so future drops are mechanical). The 5 `* Object` family components drop into a sibling `objects/` sub-folder because they take a `src` URL prop and have no React-children API surface — keeping them grouped makes the schema explicit.

```
src/components/canvasui/
├── v30/
│   ├── Asciify.tsx               ← real (wrapper, children required)
│   ├── Bend.tsx                  ← real (wrapper)
│   ├── Blaze.tsx                 ← real (wrapper)
│   ├── Bubble.tsx                ← real (wrapper)
│   ├── Canvas.tsx                ← real (wrapper — base canvas component)
│   ├── Cloth.tsx                 ← real (wrapper — fabric/cloth capture)
│   ├── Clouds.tsx                ← real (wrapper)
│   ├── DecryptReveal.tsx         ← real (wrapper — note: kebab in upstream is "decrypt-reveal", we PascalCase)
│   ├── Displacement.tsx          ← real (wrapper)
│   ├── Droplets.tsx              ← real (wrapper)
│   ├── FlameWrap.tsx             ← real (wrapper)
│   ├── ForceField.tsx            ← real (wrapper)
│   ├── Frost.tsx                 ← real (wrapper)
│   ├── Glass.tsx                 ← real (wrapper)
│   ├── Glitch.tsx                ← real (wrapper — supersedes the old hand-rolled Glitch)
│   ├── GlyphRain.tsx             ← real (wrapper)
│   ├── Grid.tsx                  ← real (wrapper)
│   ├── HexFloat.tsx              ← real (wrapper)
│   ├── Laser.tsx                 ← real (wrapper)
│   ├── Liquid.tsx                ← real (wrapper)
│   ├── Magnify.tsx               ← real (wrapper)
│   ├── ParticleReveal.tsx        ← real (wrapper)
│   ├── ParticleScroll.tsx        ← real (wrapper)
│   ├── Peel.tsx                  ← real (wrapper)
│   ├── RetroDither.tsx           ← real (wrapper)
│   ├── Ripple.tsx                ← real (wrapper)
│   ├── Shatter.tsx               ← real (wrapper)
│   ├── VHS.tsx                   ← real (wrapper)
│   ├── index.ts                  ← barrel re-export of the 25 wrappers
│   └── objects/
│       ├── AsciiObject.tsx       ← takes `src` URL, WebGL + three.js
│       ├── DitheredObject.tsx    ← takes `src` URL
│       ├── GlassObject.tsx       ← takes `src` URL
│       ├── ParticleObject.tsx    ← takes `src` URL
│       ├── LiquidObject.tsx      ← takes `src` URL
│       └── index.ts              ← barrel re-export of the 5 objects
└── _v1_css_retired/              ← D4 append-only archive (git history keeps the full source)
    ├── README.md                 ← audit note: "Retired 2026-07-30 in favour of upstream v30"
    ├── Asciify.tsx
    ├── BackgroundFX.tsx
    ├── Bend.tsx
    ├── Blaze.tsx
    ├── BorderBeam.tsx
    ├── Bubble.tsx
    ├── Frost.tsx
    ├── Glitch.tsx
    ├── LiquidMetal.tsx
    ├── Particle.tsx
    ├── ThinkingOrbs.tsx
    ├── theme-canvas-mapping.ts
    └── index.ts
```

Total new files: **32** (`30` components + 2 `index.ts` barrels — top-level + `objects/`). Plus the `_v1_css_retired/README.md` audit note (33 new files).

### 1.2 Literal `git rm` paths (D4 append-only — move, don't delete)

The 13 retired files are physically moved to `_v1_css_retired/`, not deleted, so git history remains intact and the design-rationale comments survive:

```bash
cd "C:/Users/amado/coach-os"
mkdir -p src/components/canvasui/_v1_css_retired
git mv src/components/canvas-ui/Asciify.tsx          src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/BackgroundFX.tsx      src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/Bend.tsx             src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/Blaze.tsx            src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/BorderBeam.tsx        src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/Bubble.tsx           src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/Frost.tsx            src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/Glitch.tsx           src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/LiquidMetal.tsx      src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/Particle.tsx         src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/ThinkingOrbs.tsx     src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/theme-canvas-mapping.ts src/components/canvasui/_v1_css_retired/
git mv src/components/canvas-ui/index.ts             src/components/canvasui/_v1_css_retired/
```

> Important: the legacy directory `src/components/canvas-ui/` (hyphen) becomes empty after these moves. Remove it with `rmdir src/components/canvas-ui/` only if `git status` confirms it's truly empty (no orphans). The new directory is `s
