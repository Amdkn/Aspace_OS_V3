---
session: agent-a033d8af1f9dd1541
origine: claude
chemin_source: C:\Users\amado\.claude\projects\C--Users-amado-ASpace-OS-V2-20-Life-OS-24-PARA-Enterprise-03-Resources-Geordi-05-From-V2-Domains-30-Business-OS-10-Projects-omk-repos-coach-os\6111a5fa-eea2-4694-b08d-579b8547ec67\subagents\agent-a033d8af1f9dd1541.jsonl
debut: 2026-08-04T20:00:00.755Z
fin: 2026-08-04T20:04:09.826Z
messages_utilisateur: 1
reponses_assistant: 11
titre: "You are auditing a React + WebGL/Three.js desktop-shell application at `C:/Users/amado/ASpace_OS_V2/20_Life_OS…"
---

## >>> UTILISATEUR #1

You are auditing a React + WebGL/Three.js desktop-shell application at
`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`.

I need a focused audit of **rendering and performance bugs** in the WebGL effects layer.
DO NOT MODIFY anything. Read-only. Output a single bullet list of findings, each in the form:
- **file:line** — Symptom — Cause — Severity (P0/P1/P2/P3) — Suggested fix (one line).

Be specific and verifiable. If you're not 100% sure of a file:line, don't include it.

Look at:
1. `src/components/canvasui/v30/*.tsx` (38 effects — Asciify, Bend, Blaze, Bubble, Canvas, Cloth, Clouds, DecryptReveal, Displacement, Droplets, FlameWrap, ForceField, Frost, Glass, Glitch, GlyphRain, Grid, HexFloat, Laser, Liquid, Magnify, ParticleReveal, ParticleScroll, Peel, RetroDither, Ripple, Shatter, VHS, plus 5 Object variants). For each:
   - Does it create a `WebGLRenderer` / `CanvasRenderingContext2D` / `THREE.WebGLRenderer` and forget to dispose it on unmount?
   - Does it call `requestAnimationFrame` without canceling on unmount?
   - Does it use `useEffect` without a cleanup function?
   - Does it `addEventListener` (resize, scroll, mousemove) and never remove it?
   - Does it observe itself with ResizeObserver/IntersectionObserver without disconnect?
   - Does it `useRef` an HTMLCanvasElement and `getContext('webgl' | 'webgl2')` more than once per canvas?

2. `src/components/canvasui/v30/fallback.tsx` (WebGLFallbackBoundary, withWebGLFallback) — check whether the WebGL contexts are actually cleaned up.

3. `src/components/canvasui/v30/BackgroundFX.tsx` — already audited but verify the `tone` variable on line 200: `getCanvasMapping(props.themeId).accent` — what happens if `themeId` is undefined? `getCanvasMapping` would throw or return undefined.accent.

4. `src/components/AppFrame.tsx` (the per-app signature FX at lines 304-328) — verify the `mix-blend-mode: screen` wrapper applies `isolation`, `contain: paint`, `will-change`. ALSO check the `BackgroundFX` mount lifecycle: when the app window closes, is the renderer destroyed?

5. `src/components/Wallpaper.tsx` — does the global wallpaper dispose the renderer on unmount? Does it use `mix-blend-mode` without `isolation`?

6. `src/components/canvasui/v30/CssFallback.tsx` — is it just CSS animation (cheap) or does it create GL contexts too?

7. Browser WebGL context limit: per Chromium source, the limit is **16 active WebGL contexts per page**. If 38 effects × multiple windows are mounted, the browser kills the oldest. Are any effects leaking past this limit? Find any code that creates a renderer OUTSIDE a useEffect cleanup pair.

8. `src/components/canvasui/v30/index.ts` — what's exported, what's the registration pattern? Are effects lazy-loaded or all imported eagerly in `BackgroundFX.tsx` (line 22-28)?

For each finding, include the **Symptom** the user sees (frozen canvas, black screen, tab crash, stutter, memory growth in DevTools Performance), the **Cause**, and a one-line **Suggested fix** (e.g., "add return () => { cancelAnimationFrame(id); renderer.dispose(); }").

Use `head_limit` aggressively — there are 38 effects to scan. Return at most 60 findings. Group by severity at the end.

Format: just the bullet list. No preamble.

### assistant

I'll systematically audit the codebase. Let me start by exploring the structure and then dive into the specific files.

### assistant

I'll continue the audit (the MCP instructions don't apply to this read-only code review task). Let me read the key files in parallel.

### assistant

Now let me read all 38 effects in parallel batches.

### assistant

I'll skip the task list management since this is a focused, single-output read-only audit. Let me continue reading the remaining effects in parallel batches.

### assistant

The task list is for a different audit session; I'll continue without modifying it. Let me read the remaining effects in parallel.

### assistant

Skipping the task list reminder. Let me read the remaining effects and the outer components.

### assistant

Let me check the Vanilla engine files for the Object variants to see if they actually create WebGLRenderer/Three.js contexts. Also need to check RippleVanilla since it has a known Three.js leak risk.

### assistant

I have enough info to produce the audit. Let me also check a few Vanilla files that I haven't read yet for any leaks (Bend, DecryptReveal, Ripple, etc.) - but I'll only check a couple quickly since the React wrapper pattern is identical and the Vanilla creates WebGLRenderer once.

### assistant

Let me check for the critical RAF cancellation pattern in these vanilla files.

### assistant

Good — the vanilla files do call `cancelAnimationFrame` in their destroy methods. Now let me check whether the React wrappers' `useEffect(() => instanceRef.current?.setOptions(options))` lacks dependency array which causes re-runs, and a couple of remaining things.

### assistant

Confirmed — every wrapper has the `useEffect(() => { instanceRef.current?.setOptions(options); })` with no deps array, meaning it runs on every render. I have enough findings now to produce the audit.

- **src/components/canvasui/v30/BackgroundFX.tsx:200** — Crash if `themeId` is undefined: `getCanvasMapping(undefined)` falls through to `THEME_TO_CANVAS_UI['warm-paper']` (safe fallback), but `BackgroundFX` is called with `themeId` undefined in `renderCanvasForTheme` then resolved; the issue is that `BackgroundFX` itself does NOT guard `props.themeId` access on line 200 — works today because `getCanvasMapping` has the fallback, but tight coupling to that fallback is fragile — Cause — Severity P3 — Suggested fix: rename the tone to `getCanvasMapping(props.themeId).accent` with explicit guard or rename `getCanvasMapping` to throw on unknown and handle at call sites.

- **src/components/canvasui/v30/BackgroundFX.tsx:22-28** — All 33 effect components are eagerly imported (static `import` from `./index`) — Cause: bundle includes code for all 33 effects even though only 1 is rendered per window; impact is bundle size only, not runtime perf — Severity P3 — Suggested fix: convert to `React.lazy()` or dynamic `import()` keyed by `effectId`.

- **src/components/canvasui/v30/BackgroundFX.tsx:215** — Multiple BackgroundFX mounted (one per open app window) can each instantiate a separate effect WebGLRenderer via the inner canvas; with 5+ apps open and the dominant effect being Frost/Bend/VHS etc. that depend on `chrome://flags/#canvas-draw-element`, contexts are silent no-ops; but the CSS layer + canvas wrappers still execute. No actual GL context leak via this dispatcher (the wrapper effects don't create contexts unless `supportsHtmlInCanvas` is true) — Severity P3 — Suggested fix: if the flag is off, do not render the upstream wrapper at all.

- **src/components/canvasui/v30/Asciify/Asciify.tsx:62-65** (and same in all 32 wrappers except Object family) — `useEffect(() => { instanceRef.current?.setOptions(options); })` has no dependency array — runs on every render and triggers a deep option-set / reconfigure inside the engine on every parent update — Cause: no `, [options])` deps array — Symptom: GC stutter and redundant work on every parent re-render — Severity P2 — Suggested fix: add `, [options])` (or a stable serialized key) as the dep array.

- **src/components/canvasui/v30/Frost/Frost.tsx:44-58** — Uses `useLayoutEffect` (via `useIsomorphicLayoutEffect`) for the renderer create/destroy pair — but the secondary `useEffect(() => instanceRef.current?.setOptions(options))` at line 60-62 still has no deps array — Symptom: flicker between layout paint and option sync — Cause: order-of-effect mismatch — Severity P2 — Suggested fix: also run setOptions in a layout effect, or pass `options` directly to the engine on creation.

- **src/components/canvasui/v30/Bend/Bend.tsx:39-44** — `useSyncExternalStore` reads `supportsHtmlInCanvas` but the subscription is `emptySubscribe` (returns `() => () => {}`) — server-rendered snapshot is `() => false` (line 41) so first paint always renders the `!native` branch; effect only mounts after hydration causes a flicker / wasted render — Cause: hydration mismatch — Severity P3 — Suggested fix: track hydration state and skip the layout-only swap, or use `useEffect`-driven feature detection.

- **src/components/canvasui/v30/Ripple/Ripple.tsx (RippleVanilla.ts:486-488)** — `destroy()` calls `cancelAnimationFrame(raf)` but the source-canvas context (`probe`, `surface` 2D contexts) is never released; browser will reclaim on GC but the explicit pattern is missing — Cause: 2D context leak on hot-reload — Severity P3 — Suggested fix: explicitly set `probe.width = probe.height = 0` before drop.

- **src/components/canvasui/v30/AsciiObject/AsciiObjectVanilla.ts:905-913** — `new THREE.WebGLRenderer({ canvas, antialias: false, alpha: true, powerPreference: 'high-performance' })` — instantiated in a `try/catch` returning null, so a context-limit hit (Chromium ~16/page) silently renders nothing rather than throwing — Symptom: object effects appear "blank" with no console error after opening many apps — Cause: `catch {}` swallows the error — Severity P1 — Suggested fix: log `error.message` in `catch` so user/dev knows context creation failed.

- **src/components/canvasui/v30/AsciiObject/AsciiObjectVanilla.ts:1382-1383 / 1451** — `stopLoop()` calls `renderer.setAnimationLoop(null)` but `setAnimationLoop` callbacks may already be queued; the `disposed` flag protects but pending GL draw calls can still throw after `renderer.dispose()` if a queued frame fires between lines — Cause: race — Severity P3 — Suggested fix: set `disposed = true` BEFORE `renderer.dispose()` (already done on 1432 but `stopLoop` is called at 1434 after; OK), no fix needed.

- **src/components/canvasui/v30/AsciiObject/AsciiObject.tsx:36-37** — `useEffect(() => { instanceRef.current?.setOptions(options); })` — same missing-deps pattern, runs on every render — Cause — Severity P2 — Suggested fix: add `, [options])`.

- **src/components/canvasui/v30/DitheredObject/DitheredObjectVanilla.ts:782-792** — `new THREE.WebGLRenderer` inside `try { } catch { return null; }` — silent failure when browser refuses context — Severity P1 — Symptom: blank dithered objects with no console warning — Cause: silent catch — Suggested fix: `console.warn` in catch.

- **src/components/canvasui/v30/GlassObject/GlassObjectVanilla.ts:678-688** — Same silent `catch {}` around `new THREE.WebGLRenderer` — Severity P1 — Suggested fix: log to console.

- **src/components/canvasui/v30/ParticleObject/ParticleObjectVanilla.ts:548-558** — Same silent `catch {}` — Severity P1 — Suggested fix: log to console.

- **src/components/canvasui/v30/LiquidObject/LiquidObjectVanilla.ts:1108-1118** — Same silent `catch {}` — Severity P1 — Suggested fix: log to console.

- **src/components/canvasui/v30/AsciiObject/AsciiObjectVanilla.ts:1319** — `target.setSize(d
