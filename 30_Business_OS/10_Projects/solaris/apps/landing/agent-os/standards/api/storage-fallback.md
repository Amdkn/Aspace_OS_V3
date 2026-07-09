---
title: Storage Fallback Chain
---

## Rule

Lead persistence uses a **3-tier fallback chain** with no silent loss.

```
Supabase (REST)
  └─ env missing / fetch fails / non-2xx
      └─ Local file (.data/leads.jsonl)  [dev only]
          └─ 503 storage_unavailable  [prod]
```

## Tier 1 — Supabase (canonical, prod)

- Env: `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY` (or `SUPABASE_ANON_KEY` with INSERT RLS policy)
- POST to `${SUPABASE_URL}/rest/v1/leads`
- Table schema defined in `LEADS_SETUP.md`
- If `res.ok` → return `{ ok: true, stored: "supabase" }`

**Never log env values or response bodies** — see
[security/no-secret-leak.md](../security/no-secret-leak.md).

## Tier 2 — Local file (dev fallback)

- Active when **both** Supabase env are absent AND `NODE_ENV !== "production"`
- Appends one JSON record per line to `.data/leads.jsonl` (gitignored)
- Uses `node:fs/promises` `mkdir({ recursive: true })` + `appendFile`

**Why not in prod:** Vercel/serverless `fs` is ephemeral — file would be
lost between invocations. The fallback exists only so local `npm run dev`
captures leads without requiring Supabase setup.

## Tier 3 — 503 honest failure

If Tier 1 fails AND Tier 2 returns `false` (or we are in prod), the
endpoint returns:

```ts
return NextResponse.json(
  { ok: false, error: "storage_unavailable" },
  { status: 503 }
);
```

**No silent loss in prod.** Returning `200` here would be lying to the
client. The 503 lets the frontend surface "service temporarily down" UX.

## Why this chain

- **Supabase** is the source of truth (queried by Symphony, syncs to
  other systems)
- **File** keeps the dev loop tight (no env to set up)
- **503** keeps the contract honest — clients know persistence failed
  and can retry

## Cross-refs

- `api/result-types.md` — 503 response shape
- `LEADS_SETUP.md` (in repo) — Supabase table DDL
