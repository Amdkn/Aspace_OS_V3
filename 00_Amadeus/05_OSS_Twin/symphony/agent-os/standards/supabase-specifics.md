---
title: Supabase Specifics (L2 Adapter)
---

> Supabase est le L2 Shadow Business adapter pour **Observability / Cross-table / Source-of-truth substitué**.
> PostgREST v1 + Bearer PAT/service_role + RLS strict + pooling.

## Auth

```yaml
auth:
  type: service_role_or_pat
  header: "Authorization: Bearer <SUPABASE_ANON_OR_SERVICE>"
  rate_limit: 100 req/s par projet (PostgREST pooled)
  pagination: cursor via Range header
```

## Endpoints used

- `GET /rest/v1/{table}?select=*` — list records (avec filter ByFormula-like)
- `GET /rest/v1/{table}?select=col` — minimal select pour observabilité
- `POST /rest/v1/{table}` — create (rare, service_role only via RLS gate)
- `PATCH /rest/v1/{table}?session_id=eq.X` — upsert idempotent
- `POST /pg/query` (MCP only) — raw SQL service_role path

## Webhooks

- Pas d'analogique REST direct ; **Database Webhooks** côté Supabase dashboard
- Trigger : table event → pg_notify → webhook
- Pattern Symphony : **polling 5min via `mcp__symphony_supabase__query`** en absence de webhook actif

## Field types (Supabase-specific gotchas)

| Field type | Supabase quirk | A'Space handling |
|---|---|---|
| `text` | Free-form, no length cap | Sanitize apostrophes (D6 lesson 2026-07-03) |
| `uuid` | Generated ou PG-provided | Default `gen_random_uuid()` côté admin |
| `timestamptz` | Always UTC, ISO 8601 | Parse to `updated_at` |
| `boolean` | True/False strict | Normalise JSON booleans |
| `jsonb` | PG JSON ops | Use `'{}'::jsonb` default |
| `bigserial`/`identity` | Auto-increment | Skip for natural PK (session_id text used) |
| Array `text[]` | PG-native | JSON-array on read |
| Foreign keys | `references` | Use sparingly (anon read isolation) |

## Rate limit handling

- Exceeded (429) = exponential backoff (1s, 2s, 4s, max 60s)
- After 5 consecutive 429s = mark workflow `degraded`, alert via Telegram
- **D6 #NEW 2026-07-03** : REST v1 anon/sbp PAT keys in env vars return 401 "Invalid API key".
  Le **seul** path D5-receipté pour write reste `mcp__supabase__execute_sql` (SDK MCP service_role).
  consumer sidecar pipeline = `pending_upserts.ndjson` → MCP drain.

## Why Supabase (not just Airtable for observability)

- **Source-of-truth substitué** — `symphony_state` table holds the meta-state
- **Webhook-ready if needed** — pg_notify triggered from PG triggers
- **Self-hostable** (post MUSE) — but Cloud-managed works for current scale
- **RLS-by-default** — defense in depth, anon read separates from service_role write

## Anti-patterns

- ❌ Using Supabase as primary tracker (Airtable wins there)
- ❌ REST v1 writes via curl with env vars (401 anomaly — use `mcp__supabase__execute_sql`)
- ❌ Apostrophes/single-quotes in raw text without proper escape (D6 corruption 2026-07-03)
- ❌ Storing PAT/sbp in WORKFLOW.md — use `$SUPABASE_*` env vars or MCP internal key
- ❌ Polling every second (rate-limit hell) — use 5min polling + webhook trigger

## Cross-refs

- `symphony-supabase.spec.md` §2 (table de comparaison adapters)
- `writeback-policy.md` — what writes Symphony permits (default read-only)
- `mission-contract.md` — `source_tool: supabase` + `source_id`
- `40_SYMPHONY_BUS/state_writer.py` — sink producer (sidecar `pending_upserts.ndjson`)
- `wiki/hand_offs/u1_symphony_supabase_sink_shipped_2026-07-03.md` — U1 D5 receipts
