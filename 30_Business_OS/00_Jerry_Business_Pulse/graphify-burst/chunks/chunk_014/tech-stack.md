---
title: Tech Stack
---

## Core

- **Next.js 16.2.6** — App Router, Server Components, RSC actions
- **React 19.2.4** — `use()` hook, `useFormState`, async transitions
- **TypeScript 5** — strict + bundler resolution + `incremental: true`
- **ESLint 9** — flat config via `defineConfig([...])` in `eslint.config.mjs`
- **Node runtime** — `runtime = "nodejs"` on API routes needing fs/fetch

## Path alias

- `@/*` → `./src/*` (only alias; no other path shortcuts)

## Versions matter

Next 16 has breaking changes vs prior majors. APIs, conventions, and file
structure may all differ from training data. See [nextjs-16-rules.md](./nextjs-16-rules.md).
