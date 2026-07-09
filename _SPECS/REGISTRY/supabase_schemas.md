---
source: A0_Registry
date: 2026-06-10
type: registry
domain: L0_Tech_OS / Supabase_VPS
tags: [#registry #supabase #schemas #multitenant]
---

# Supabase Schemas Registry

> **Source of truth** : état live des schémas Postgres sur les instances Supabase (Cloud par produit, self-host en archive post-ADR-OMK-004 RATIFIED 2026-06-19).
> **Hosting pivot 2026-06-19** : OMK Services Org (Cloud) + ABC-OS-COMMUNITY Org (Cloud) sont les nouvelles instances prod (per `ADR-OMK-004` + `ADR-ABCOS-002`). Self-host VPS `148.230.92.235` archivé fonctionnellement mais pas encore radié (D4 no-hard-delete).
> **Vérif live** : par projet via `mcp__supabase__*` (Life OS / Agency), `mcp__supabase-omk__*` (OMK Services), `mcp__supabase-abc__*` (ABC-OS-COMMUNITY).
> **HITL-gated ops** (W4 `05_supabase/AGENTS.md`) : DROP SCHEMA, DROP TABLE, DROP POLICY, DISABLE RLS, DELETE on prod.

## Schémas actifs

| Schéma | Tenant | Hosting | ADR | Statut | Tables (count) | RLS ? |
|---|---|---|---|---|---|---|
| `public` | Supabase core (auth, storage, realtime) | per project | — | core (tous projets) | n/a | non |
| `storage` | Supabase Storage | per project | — | core (tous projets) | n/a | non |
| `graphql_public` | PostgREST introspection | per project | — | core (tous projets) | n/a | non |
| `solaris_internal` | Solaris (AaaS Digital Garden) — internal/staff | self-host `148.230.92.235` | ADR-SUPABASE-001 | ⚠️ **ARCHIVED self-host 2026-06-19** (ADR pivot Life OS non encore ratifié formellement, **NON** couvert par ADR-OMK-004 ni ADR-ABCOS-002) | 2 | oui |
| `solaris_saas` | Solaris — multi-tenant (org_id) | self-host `148.230.92.235` | ADR-SUPABASE-001 | ⚠️ **ARCHIVED self-host 2026-06-19** | 3 | oui |
| `omk_internal` | OMK Dashboard — internal | self-host (archivé) | ADR-OMK-001 | ⚠️ **RETIRED 2026-06-19 (A1 LOCKED, ADR-OMK-004)** — mode `internal` retiré, single SaaS mode | n/a | oui |
| `omk_saas` | OMK Dashboard — multi-tenant (org_id) | **Supabase Cloud** (OMK Services Org) | ADR-OMK-004 RATIFIED 2026-06-19 | ✅ **LIVE Cloud** | 7 | oui |
| `abc_os` | ABC OS Community — multi-tenant (org_id) | **Supabase Cloud** (ABC-OS-COMMUNITY Org) | ADR-ABCOS-002 (Claude Code update 2026-06-19) | ✅ **LIVE Cloud** (17 tables + 85 rows + RLS, applied via 4/4 `mcp__supabase-abc__apply_migration` batches 2026-06-17) ⚠️ **PostgREST exposure PENDING A0 HITL** (Condition F, Dashboard Settings → API → Exposed schemas → add `abc_os`) | 17 | oui |
| `abc_child_care` | Child Care BOS — multi-tenant (org_id) | **Supabase Cloud** (ABC-OS-COMMUNITY Org) | ADR-ABCOS-002 | ⚠️ **P5.1 scaffold post G8 Legal sign-off** — schema créé sur Cloud ou self-host? À clarifier A0 | 0 (pas encore provisionné) | oui |

## Convention nommage

- Schémas produits = **kebab-case en snake_case** : `abc-os` → `abc_os`, `abc-childcare-portal` → `abc_child_care` (per ADR-SUPABASE-001 D1).
- Préfixe `omk_*`, `solaris_*`, `abc_*` = isolation par produit (un schéma = un produit, JAMAIS un schéma = un tenant).
- Schémas internes (`_internal`) = staff/admin only, pas de JWT `org_id` claim, policies basées sur `is_staff()`.

## Grants & default privileges

Per `05_supabase/AGENTS.md` W3 :
- `aspace_admin` (Postgres role, noSuperuser) = `USAGE` + `CREATE` sur tous les schémas produits.
- `aspace_observer` (Postgres role, read-only) = `USAGE` + `SELECT` sur tous les schémas produits.
- `ALTER DEFAULT PRIVILEGES FOR ROLE aspace_admin IN SCHEMA <schema> GRANT ...` = futures tables automatiquement grantées.

## Voir aussi

- `_SPECS/ADR/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md` — fondations (un schéma = un produit, dual MCP). **⚠️ SUPERSEDED FONCTIONNELLEMENT 2026-06-19** par ADR-OMK-004 + ADR-ABCOS-002 (self-host → Cloud).
- `_SPECS/ADR/ADR-OMK-001_dual-product-dashboard-multitenant.md` — pattern OMK (org_id + RLS). **⚠️ AMENDED 2026-06-19** par ADR-OMK-004 (mode `internal` retiré, A1 LOCKED).
- `_SPECS/ADR/ADR-OMK-004_pivot-supabase-cloud-vercel.md` — **RATIFIED 2026-06-19**, OMK pivot complet.
- `_SPECS/ADR/ADR-ABCOS-001_multitenant-supabase-strategy.md` — pattern ABC OS (mirror OMK), hosting pivoted.
- `_SPECS/ADR/ADR-ABCOS-002_pivot-supabase-cloud-vercel.md` — **DRAFT 2026-06-19, RATIFIED post-conditions B-F**, ABC pivot complet.
- `10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/05_supabase/AGENTS.md` — contrat opérationnel (W1-W5).
- `_TRASH/2026-06-06_cleanup/` — sessions archivées (no-hard-delete respecté).
