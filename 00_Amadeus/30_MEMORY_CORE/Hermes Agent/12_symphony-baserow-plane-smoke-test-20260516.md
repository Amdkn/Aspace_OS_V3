---
source: Codex / Shadow L0
date: 2026-05-16
type: smoke-test-report
domain: L0_Tech_OS / Hermes_Agent / Symphony
tags: [#Hermes #Symphony #Baserow #Plane #Solaris #SmokeTest #secrets]
status: blocked-plane-auth
---

# Smoke Test — Decomposer W1 Solaris de Baserow vers Plane

## 1. Objective

Test a minimal Symphony handoff:

```text
Baserow Warp Core W1 Solaris -> Plane work-items
```

Scope was intentionally narrow:

- Read the Solaris W1 row from Baserow.
- Decompose its `Top 3 Commitments` into Plane-ready work-items.
- Attempt Plane API authentication before creating anything.
- Do not print or store secrets.

## 2. Official Docs Checked

| Tool | Source |
|---|---|
| Baserow rows API | `https://baserow.io/user-docs/database-api` |
| Baserow token model | `https://baserow.io/user-docs/personal-api-tokens` |
| Plane API | `https://developers.plane.so/api-reference/introduction` |

Plane official docs indicate API access through the Plane REST API using an API key header. The local Symphony spec also expects `PLANE_API_KEY`.

## 3. Baserow Read Proof

Environment:

```text
/home/amadeus/.hermes/.env
BASEROW_DATABASE_TOKEN=<redacted>
```

Command class:

```text
GET https://api.baserow.io/api/database/rows/table/955428/?user_field_names=true&size=100
Authorization: Token <redacted>
```

Result:

```text
table_id=955428
row_id=133
ID Semaine=W1 - Launch Flash (Product) & Batman (Ops)
Quarter=H1-C3A : Solaris
```

Source row content:

```text
[R3A-La Forge] Definir les limites binaires du "Content Pack" Solaris (ex: 30 posts statiques/mois).

[R3A-Le Portail] Creer le formulaire de Brief "Anti-Flou" (Airtable) obligatoire pour le client.

[R3A-Le Portail] Configurer le statut BLOCKED pour tout brief incomplet (Invisible Woman).
```

## 4. Decomposition Plane-Ready

These are the three intended Plane work-items:

```json
[
  {
    "name": "[Solaris W1][R3A-La Forge] Definir les limites binaires du Content Pack",
    "description": "Source: Baserow table 955428 row 133, W1 Solaris. Commitment: definir les limites binaires du Content Pack Solaris, par exemple 30 posts statiques par mois. Build Gate: l'offre Solaris est-elle explicable en une phrase binaire ?",
    "labels": ["@L2", "Solaris", "W1", "R3A-La-Forge", "Product", "Ops"],
    "source": "baserow:table/955428/row/133"
  },
  {
    "name": "[Solaris W1][R3A-Le Portail] Creer le brief Anti-Flou obligatoire",
    "description": "Source: Baserow table 955428 row 133, W1 Solaris. Commitment: creer le formulaire de Brief Anti-Flou obligatoire pour le client. Validation note: le formulaire empeche-t-il la soumission si le champ Brand Book est vide ?",
    "labels": ["@L2", "Solaris", "W1", "R3A-Le-Portail", "Product", "Ops"],
    "source": "baserow:table/955428/row/133"
  },
  {
    "name": "[Solaris W1][R3A-Le Portail] Configurer BLOCKED pour brief incomplet",
    "description": "Source: Baserow table 955428 row 133, W1 Solaris. Commitment: configurer le statut BLOCKED pour tout brief incomplet. Owner hint: Invisible Woman.",
    "labels": ["@L2", "Solaris", "W1", "R3A-Le-Portail", "Product", "Ops"],
    "source": "baserow:table/955428/row/133"
  }
]
```

## 5. Plane Auth Test

Environment:

```text
/home/amadeus/.hermes/.env
PLANE_API_KEY=<redacted>
```

Non-destructive endpoint tested:

```text
GET https://api.plane.so/api/v1/workspaces/aspace-core/projects/
```

Headers tested:

```text
x-api-key: <redacted>
X-API-Key: <redacted>
Authorization: Bearer <redacted>
```

Result:

```text
x-api-key HTTP 403
X-API-Key HTTP 403
Authorization Bearer HTTP 403
```

Conclusion:

```text
No Plane work-item was created.
Plane API key is present but not accepted for this workspace/API scope, or the key has been disabled/rotated after exposure.
```

## 6. Next Actions

1. Rotate the Plane key, because it was pasted in chat.
2. Generate a Plane API key with access to workspace `aspace-core`.
3. Confirm or set `PLANE_PROJECT_LIFE_OS` in `/home/amadeus/.hermes/.env`.
4. Re-run the creation step using the three payloads above.
5. After creation, write Baserow row `955428:133` proof links into `Preuve SSOT` or a dedicated Symphony trace field if available.

## 7. Residual Risk

- Baserow read succeeded; no Baserow write was attempted.
- Plane write was not attempted because authentication failed before project discovery.
- Secrets remain in `/home/amadeus/.hermes/.env`; commands and docs show only redacted values.

*Documente Docs Dogmatique — Baserow to Plane Solaris W1 smoke test — 2026-05-16 — Codex*
