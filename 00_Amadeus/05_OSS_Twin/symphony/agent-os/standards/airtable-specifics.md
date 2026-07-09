---
title: Airtable Specifics (L2 Adapter)
---

> Airtable is the L2 Shadow Business adapter for **Growth / Sales /
> Finance**. REST v0, Bearer PAT, webhooks 7j, 5 req/s/base.

## Auth

```yaml
auth:
  type: Bearer_PAT
  header: "Authorization: Bearer <AIRTABLE_PAT>"
  rate_limit: 5 req/s per base  # shareable across tables in same base
  pagination: offset 100/page
```

## Endpoints used

- `GET /v0/{baseId}/{tableIdOrName}` — list records (with `filterByFormula`)
- `GET /v0/{baseId}/{tableIdOrName}/{recordId}` — single record
- `POST /v0/{baseId}/{tableIdOrName}` — create record (rare, only for
  drafts per `writeback-policy.md`)
- `PATCH /v0/{baseId}/{tableIdOrName}/{recordId}` — update record
  (writes require greenlight)

## Webhooks

- 7-day expiration: must be re-registered every 7 days
- Polling fallback: `polling.interval_ms: 300000` (5 min) — webhooks
  are the primary, polling is the safety net
- Webhook payload: `{baseId, tableId, action: "create|update|delete",
  record, timestamp}`

## Field types (Airtable-specific gotchas)

| Field type | Airtable quirk | A'Space handling |
|---|---|---|
| Single Select | String value, not enum | Normalize to lowercase in payload |
| Multiple Select | Array of strings | Lowercase + sort alphabetically |
| Linked Record | Array of record IDs | Resolve to `[{id, name}]` for context |
| Attachment | Array of `{id, url, filename}` | Pass `url` only, expire after 24h |
| Formula | String result, may be empty | Default to `""` |
| Lookup | Pre-resolved by Airtable | Treat as read-only |
| Rollup | Pre-aggregated | Pass-through |
| Created/Modified time | ISO 8601 UTC | Parse to `created_at` / `updated_at` |
| Created/Modified by | User ID + email | Strip email (RGPD), keep ID |
| Long text | 100k char limit | Slice at 100k, log warning |
| URL | Validated by Airtable | Trust Airtable, no double-check |

## Rate limit handling

- Exceeded (429) = exponential backoff (1s, 2s, 4s, 8s, max 30s)
- After 5 consecutive 429s = mark workflow `degraded`, alert via
  Telegram
- Never burst > 5 req/s even if just below limit (Airtable counts
  partial seconds)

## Why Airtable (not Linear, not Plane)

Per `symphony-airtable.spec.md` §1 :

- **Best API of the L2 lot** — REST mature, stable, well-documented
- **Native webhooks** — réactivité événementielle sans polling intensif
- **Slot Lead/Sales/Finance** — 3 domaines qui génèrent du cashflow
- **Native forms** — capture externe (leads, briefs) sans code
- **Relational DB** — modélisation CRM + pipeline naturelle
- **Graduation MUSE** → NocoDB self-hosted ou Supabase native

## Anti-patterns

- ❌ Using Airtable for Ops/Product/IT/People/Legal — use ClickUp
- ❌ Polling every 10s (rate-limit hell) — use 5min polling + webhooks
- ❌ Re-registering webhooks daily "to be safe" — wastes the 7-day
  budget, masks real issues
- ❌ Storing the PAT in WORKFLOW.md — use `$AIRTABLE_PAT` env var

## Cross-refs

- `symphony-airtable.spec.md` §2 (table de comparaison adapters)
- `writeback-policy.md` — what writes Symphony permits
- `mission-contract.md` — `source_tool: airtable` + `source_id`
