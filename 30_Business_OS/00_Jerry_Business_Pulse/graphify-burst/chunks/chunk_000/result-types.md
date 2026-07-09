---
title: API Result Types (Discriminated Unions)
---

## Rule

**Never throw across an HTTP boundary.** Every endpoint returns a
discriminated union result, not a thrown error.

## Pattern

```ts
export type CaptureResult =
  | { ok: true; stored: "supabase" | "file" }
  | { ok: false; error: "validation"; fields: string[] }
  | { ok: false; error: "storage" };
```

- `ok: true` branch — success, narrows to `stored: "..."`
- `ok: false` branch — typed failure, narrows to `error: "..."` with
  contextual data (e.g. `fields: string[]` for validation errors)

## Response shape (HTTP)

```ts
// Success
return NextResponse.json({ ok: true });

// Validation
return NextResponse.json(
  { ok: false, error: "validation", fields: result.fields },
  { status: 422 }
);

// Storage unavailable
return NextResponse.json(
  { ok: false, error: "storage_unavailable" },
  { status: 503 }
);
```

| Status | Meaning | When |
|--------|---------|------|
| 200    | success | `{ ok: true }` |
| 400    | bad request | malformed JSON body |
| 422    | validation | `{ ok: false, error: "validation", fields }` |
| 503    | service down | `{ ok: false, error: "storage_unavailable" }` |

## Why

- TypeScript narrows the result on the call site, no `try/catch` needed
  for expected failure modes
- HTTP semantics are explicit (422 vs 503 vs 500)
- Frontend can pattern-match `result.error` for error UX

## Anti-pattern

```ts
// ❌ throws across the boundary — caller has to know what to catch
if (!valid) throw new Error("invalid url");
```
