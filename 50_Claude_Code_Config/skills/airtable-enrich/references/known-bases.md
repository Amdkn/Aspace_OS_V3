---
date: 2026-05-17
status: ACTIVE
---

# Known A'Space Airtable bases

Mapping `serviceName` → `baseId` / `tableId` so the skill can resolve `/airtable-enrich aaas-solaris-marketing` without the user typing IDs.

When a new A'Space base is provisioned, add a row here and the skill picks it up automatically.

## Lead-table-shaped bases

These bases contain a Leads/Audits table with the canonical schema (`Statut d'Enrichissement`, `Score de Friction Technique`, `Note Globale de Qualité`, etc.).

| serviceName | baseId | tableId | Lead table label | Purpose |
|---|---|---|---|---|
| `aaas-solaris-marketing` | `appmWf5Xm7w9Ae0ky` | `tblj0xmSXLH4Xsd8c` | 🦸 Leads & Audits | Solaris AaaS — OH/KY agency leads (RevOps/Forges/AAA/Boutiques) |

## Schema contract

Any base referenced here MUST expose at least these fields on its lead table :

| Field name | Type | Used for |
|---|---|---|
| `Nom de l'Agence` | singleLineText | Founder lookup query |
| `URL du Site Web` | url | Lighthouse + footprint scan target |
| `Statut d'Enrichissement` | singleSelect (1-Raw / 2-Enrichi / 3-Rejeté) | Pipeline gate |
| `Score de Friction Technique / Lighthouse` | number | Write target — perf 0-100 |
| `Email du Fondateur` | email | Write target — founder lookup |
| `Lien LinkedIn du Fondateur` | url | Write target — founder lookup |
| `Note Globale de Qualité` | number | Write target — recomputed score 0-10 |
| `Commentaires Internes` | multilineText | Append-only enrichment trail |
| `Secteur d'Activité` | singleLineText | Read — helps archetype detection |
| `Pays de l'Agence` | singleLineText | Read — helps founder search disambiguation |

If a base doesn't have all these fields, the skill should fail-fast with exit code 4 and a clear schema diff message.

## Adding a new base

```
1. Provision the Airtable base + Lead table with the schema above
2. Get the baseId from URL: https://airtable.com/appXXX/...
3. Get the tableId from URL: https://airtable.com/appXXX/tblYYY/...
4. Add the row to this table with a kebab-case serviceName
5. Smoke test: /airtable-enrich <new-name> --limit 1 --dry-run
```

## Cross-refs

- Airtable Meta API for tableId discovery: `GET /v0/meta/bases/{baseId}/tables`
- Solaris ICP source of truth: `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\solaris-aaas\src\lib\data.ts`
