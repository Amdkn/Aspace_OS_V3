---
title: Data Shape — Short Keys in data.ts, Long Names in types.ts
---

## Convention

This repo uses **two parallel naming styles** for the same domain
entities, on purpose.

| Where | Style | Why |
|-------|-------|-----|
| `src/lib/data.ts` (const arrays) | **Short keys** (`n`, `vp`, `k`, `v`) | Terse JSON, less scrolling, easier diff review |
| `src/lib/types.ts` (interfaces) | **Long names** (`name`, `squads`, `archetype`) | Self-documenting, accessible to new contributors |

## Example

`src/lib/types.ts`:

```ts
export interface SolarisDomain {
  id: string;
  n: string;          // short
  name: string;       // long
  vp: string;         // short
  squads: string[];   // long
}
```

`src/lib/data.ts` (consumer of the interface, using short keys):

```ts
{ id: "growth", n: "01", name: "Growth", vp: "B2.Superman", squads: [...] }
```

## Why this duality

- **data.ts is the source-of-truth payload** — it ends up serialized in
  the page bundle. Short keys = smaller bundle, faster FCP.
- **types.ts is the contract** — used by components, diagrams, and
  downstream tools. Long names = self-documenting, easier to grep.

## Don't

- ❌ Use the short keys (`n`, `vp`) in component JSX or in
  `src/components/**` — readability matters more than bundle size there
- ❌ Add new entities to data.ts without first extending the matching
  interface in types.ts
- ❌ Rename the short keys to long ones "for consistency" — the bundle
  size matters and the duality is intentional

## Type-driven workflow

When adding a domain entity:

1. Add the interface to `src/lib/types.ts` (long names, with JSDoc if
   non-obvious)
2. Add the const array to `src/lib/data.ts` (uses interface, short keys)
3. Render via components in `src/components/sections/*.tsx`
