# Known Direct OpenAPI Spec URLs — Snapshot 2026-05-17

When a service is **not** in the printing-press-library catalog but publishes a curl-able OpenAPI JSON/YAML, list it here. The skill prefers this path (path 2) over docs scraping (path 3) because it's faster and doesn't burn LLM quota.

## Format

```
- <service>: <url> | auth-note (if any) | last-verified YYYY-MM-DD
```

## Confirmed direct specs

- **clickup**: `https://developer.clickup.com/openapi/ClickUp_PUBLIC_API_V3.yaml` | personal token in `Authorization: pk_*` | verified 2026-05-17
- **clickup (v2)**: `https://developer.clickup.com/openapi/clickup-api-v2-reference.json` | older API | verified 2026-05-17
- **airtable** (community): `https://raw.githubusercontent.com/codesicario/airtable-openapi-spec/main/airtable-openapi.json` | env `AIRTABLE_BEARER_AUTH=patXXX...` | verified 2026-05-17 (24 days fresh) — used successfully via `/pp-cli-install airtable -SpecUrl <url>`

## Postman-only (path 4 — manual conversion needed)

These services publish Postman collections but no direct OpenAPI. Convert with `p2o` (Postman-to-OpenAPI converter) or manually then add to the section above.

- **hostinger**: Postman collection linked from `https://developers.hostinger.com` (no direct OpenAPI exposed)
- **apollo.io**: docs at `https://docs.apollo.io/reference`, no public OpenAPI

## Documented-only (path 3 — docs scrape with LLM)

These have docs sites scrape-able by `printing-press generate --docs <url>`. **Warns user about LLM quota consumption.**

- **notion (Agents API only)**: `https://developers.notion.com/reference/intro` — note: this scrapes wrong subtree (Agents not REST). Prefer upstream pre-built (catalog).
- ~~**airtable** docs scrape~~ — SUPERSEDED 2026-05-17 by community OpenAPI spec above. Path 2 works, path 3 was failing.

### 🚨 Community OpenAPI verification protocol (lesson 2026-05-17 — Airtable false positive)

A WebSearch for "airtable openapi spec" surfaced `codesicario/airtable-openapi-spec` as #1 result. The spec compiled cleanly and the CLI built without errors. **BUT** the generated CLI had commands `candidates`, `requisitions`, `candidate-20-matches` — it was a custom **"Airtable Recruiting Matcher"** application schema, NOT the generic Airtable REST API.

**Before using ANY community OpenAPI** :

1. **Verify the `info.title`** in the spec JSON — must match the generic service name (e.g. "Airtable Web API", not "Airtable Recruiting Matcher").
2. **Sample 3 endpoints** : check `paths` keys for the canonical resources (for Airtable : `/v0/{baseId}/{tableId}`, `/v0/meta/bases`).
3. **Smoke build only if generic**.

Airtable still has no public generic OpenAPI. Recommended path : use **Claude Desktop MCP `mcp__airtable__*`** connector (already maintained, auth via UI), not a self-generated CLI.

### ⚠️ Windows path-3 known failure mode (2026-05-17)

When PP invokes `claude` CLI for doc-to-spec extraction, Windows `cmd.exe` argv length limit triggers : `"The filename or extension is too long"`. PP falls back to regex which often fails on JS-rendered SPA docs (Airtable intro returned 0 endpoints).

**Mitigations** :
1. Use narrower per-endpoint URL (e.g. `airtable/web/api/list-records` not `airtable/web/api/introduction`).
2. Delegate to Codex `shadow_l0_exec` — Codex's local LLM bridge may have different argv handling.
3. Prefer Postman → OpenAPI manual conversion (path 4) for these services.

## Adding a new entry

When you discover a new direct OpenAPI URL:

1. Verify it's curl-able: `curl -fsSL <url> | head -5`
2. Check it's a real OpenAPI/Swagger doc (look for `"openapi": "3"` or `"swagger": "2"` keys)
3. Add the entry to "Confirmed direct specs" with date and auth caveat
4. (Optional) Open a PR to `mvanhorn/printing-press-library` to add the service to the upstream catalog — future users get priority-1 path

## Refresh procedure

For each service in the A'Space targets list, periodically check:
- their developer portal for an OpenAPI download link
- their GitHub org for a public `openapi.yaml` / `swagger.json`
- their Postman public workspace

A simple refresh prompt for any agent:

> "For each service in `references/known-spec-urls.md` under 'Postman-only' and 'Documented-only', re-check whether a direct OpenAPI URL was published since 2026-05-17. If yes, move the entry up to 'Confirmed direct specs'."
