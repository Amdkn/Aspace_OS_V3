---
title: Next.js 16 — Read Before Coding
---

> **This is NOT the Next.js you know.** APIs, conventions, and file
> structure may all differ from training data. Read
> `node_modules/next/dist/docs/` before writing any code. Heed deprecation
> notices.

## Why this rule exists

Three Next 16 breaking-change incidents caused wasted cycles in this repo
already (audit debt D08, D09, D11). Each time the agent wrote valid
Next 14 / 15 code that Next 16 rejected silently or with a confusing
trace.

## Workflow

1. **Before writing any Next 16 code** — read the relevant doc in
   `node_modules/next/dist/docs/`. If unsure which doc, list the
   directory and pick by topic.
2. **Check deprecation notices** in the doc — Next 16 deprecates are
   surfaced at the top of each page.
3. **If the doc contradicts your training** — trust the doc, not memory.
4. **If still unsure** — read the matching `.d.ts` in
   `node_modules/next/dist/...` for the runtime API surface.

## Reference (training-data deltas)

- `dynamic = "force-dynamic"` is required (not optional) on routes using
  `fs` or `fetch` to external services.
- `runtime` must be set explicitly to `"nodejs"` or `"edge"` per route.
- Font loading moved to `next/font/google` (no more manual `<link>`).
- Image component API tightened — `<Image>` requires `alt` always.

## Cross-refs

- `tech-stack.md` — versions
- `architecture.md` — App Router + runtime config
