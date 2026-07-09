---
source: Codex / Shadow L0
date: 2026-05-16
type: configuration-state
domain: L0_Tech_OS / Hermes_Agent / Symphony
tags: [#Hermes #Symphony #ShadowL0 #Plane #Baserow #AFFiNE #Obsidian #MCP #secrets]
status: active-with-rotation-recommended
---

# Symphony Shadow L0 — API Links, Config Paths, Credentials State

## 1. Scope

This note records the non-secret configuration state for Symphony Shadow L0/L1 tracker integrations:

- Plane.so for GTD / USS Cerritos.
- Baserow for 12 Week Year / USS SNW.
- AFFiNE for DEAL / USS Protostar.
- Obsidian Local REST API for PARA / USS Enterprise.

Secrets are not written in this memory file. Only variable names, local paths, and proof commands are recorded.

## 2. Official API / Token Sources

| Tool | Official / upstream source | Token retrieval |
|---|---|---|
| Plane | `https://developers.plane.so/api-reference/introduction` | Plane API key from Plane developer/API settings; Symphony spec expects `PLANE_API_KEY`. |
| Baserow | `https://baserow.io/user-docs/personal-api-tokens` and `https://baserow.io/user-docs/database-api` | Baserow database/personal token; Symphony spec expects `BASEROW_DATABASE_TOKEN`. |
| AFFiNE | `https://toeverything-affine.mintlify.app/api/graphql/collaboration` | For AFFiNE Cloud MCP, upstream MCP docs indicate Settings -> Integrations -> MCP Server for API token; Symphony spec expects `AFFINE_API_TOKEN`. |
| Obsidian | `https://github.com/coddingtonbear/obsidian-local-rest-api` | Local REST API plugin Settings -> Local REST API; Symphony spec expects `OBSIDIAN_REST_API_KEY`. |

## 3. Local Symphony Specs

| Tool | Local spec | Endpoint | Secret variable |
|---|---|---|---|
| Plane | `00_Amadeus/05_OSS_Twin/symphony/L1/symphony-plane.spec.md` | `https://api.plane.so/api/v1` | `PLANE_API_KEY` |
| Baserow | `00_Amadeus/05_OSS_Twin/symphony/L1/symphony-baserow.spec.md` | `https://api.baserow.io/api` | `BASEROW_DATABASE_TOKEN` |
| AFFiNE | `00_Amadeus/05_OSS_Twin/symphony/L1/symphony-affine.spec.md` | `https://app.affine.pro/graphql` | `AFFINE_API_TOKEN` |
| Obsidian | `00_Amadeus/05_OSS_Twin/symphony/L1/symphony-obsidian.spec.md` | `https://localhost:27124` | `OBSIDIAN_REST_API_KEY` |

## 4. Current Credentials State

Installed in WSL `ASpace-L0`:

```text
/home/amadeus/.hermes/.env
```

Variables present as of 2026-05-16:

```text
PLANE_API_KEY=<redacted>
BASEROW_DATABASE_TOKEN=<redacted>
```

Permissions verified:

```text
600 amadeus:amadeus /home/amadeus/.hermes/.env
```

Backup created before writing:

```text
/home/amadeus/.hermes/.env.bak.20260516_020612_plane_baserow
```

## 5. Verification Commands

Run from Windows PowerShell:

```powershell
wsl.exe -d ASpace-L0 -- bash -lc "stat -c '%a %U:%G %n' `$HOME/.hermes/.env; grep -nE '^(PLANE_API_KEY|BASEROW_DATABASE_TOKEN)=' `$HOME/.hermes/.env | sed -E 's/=.*/=<redacted>/'"
```

Expected proof:

```text
600 amadeus:amadeus /home/amadeus/.hermes/.env
PLANE_API_KEY=<redacted>
BASEROW_DATABASE_TOKEN=<redacted>
```

## 6. Security Notes

- The Plane and Baserow keys were provided in chat on 2026-05-16. Treat them as exposed.
- Recommended next step after smoke testing: rotate both keys in Plane and Baserow, then update `/home/amadeus/.hermes/.env` through a masked/local flow.
- Do not copy these values into Markdown, screenshots, browser-visible config, frontend code, or git-tracked files.
- Existing residual risk remains for any other secret-like values already present in `/home/amadeus/.hermes/.env`; inspect only with redaction.

## 7. Next Config Work

- Add or verify the actual Hermes MCP server entries that consume these variables.
- Add `AFFINE_API_TOKEN` only after retrieving it from AFFiNE settings.
- Add `OBSIDIAN_REST_API_KEY` only after enabling the Obsidian Local REST API plugin.
- Smoke test API auth with redacted output only.

*Documenté Docs Dogmatique — Symphony Shadow L0 API credentials — 2026-05-16 — Codex*
