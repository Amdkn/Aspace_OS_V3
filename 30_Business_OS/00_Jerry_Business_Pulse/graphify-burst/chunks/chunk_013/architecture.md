---
title: Architecture
---

## Folder layout

```
src/
├── app/                    # Next App Router
│   ├── api/                # API routes (Node runtime, force-dynamic)
│   ├── globals.css         # Global styles
│   ├── layout.tsx          # Root layout (fonts + metadata)
│   ├── page.tsx            # Home composition
│   └── page.module.css     # Page-scoped styles
├── components/
│   ├── sections/           # 12 page sections (Hero, Hook, Anatomy, …)
│   └── diagrams/           # 4 SVG-style domain diagrams
└── lib/
    ├── data.ts             # Const data (short keys for terse JSON)
    ├── types.ts            # Domain model interfaces
    └── leads.ts            # D09 lead-capture core
```

## App Router conventions

- **Page composition** — `src/app/page.tsx` is a thin assembly of section
  components. Page logic ≤ 40 lines, no business logic.
- **Section components** — one file per section in
  `src/components/sections/`. Each is a self-contained module.
- **Diagrams** — pure SVG/Canvas components in `src/components/diagrams/`.
  No fetch, no state, no side effects.
- **Domain data** — `src/lib/data.ts` for const arrays,
  `src/lib/types.ts` for interfaces, `src/lib/leads.ts` for the only
  async business logic.

## Path alias

Only `@/*` → `./src/*` is configured. Use it everywhere instead of
relative `../../` ladders.

## Runtime config (API routes)

Every route in `src/app/api/**/route.ts` MUST export:

```ts
export const runtime = "nodejs";
export const dynamic = "force-dynamic";
```

Required because the route uses `fetch` to Supabase and (in dev) `fs` for
the JSONL fallback. Next 16 won't surface the right runtime otherwise.

## Root layout

- `src/app/layout.tsx` loads 3 fonts via `next/font/google`, exposes them
  as CSS variables, and defines the full metadata block.
- `<html data-archetype="…" data-density="…">` for CSS theming hooks.

## Cross-refs

- `tech-stack.md`
- `api/storage-fallback.md` — why runtime/dynamic are required
- `forms/state-machine.md` — the only client component pattern
