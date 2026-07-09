# Shadow L2 — Mesh Tri-Plateforme Doctrine VERROUILLÉE

**Date :** 2026-05-27 (session de soir)
**Niveau :** L2 Business OS
**Sources doctrinales :** ADR-MESH-L2-001 + ADR-ID-001 + ADR-CK-FREE-001 (3 ADRs créés cette session)
**Status :** ✅ COMPLETED — Doctrine tri-plateforme cohérente Notion×ClickUp×Airtable, mesh prêt pour Phase 2 Symphony

---

## Acquis de cette session

### 1. Cartographie des 3 plateformes

| Plateforme | Rôle sémantique | Volume |
|------------|------------------|--------|
| **Notion** (Business Pulse ∞ AMADEUS) | WHAT — Doctrine | 57 entries (1 top + 8 portails + 2 DBs + 8 squads + 38 SOPs) |
| **ClickUp** (workspace 90141225938) | WHEN/WHO — Exécution | 97 lists (1 + 32 + 32 + 32, sur 12 folders productifs) |
| **Airtable** (AaaS Solaris Marketing) | HOW MUCH — Données | 9 tables relationnelles hub-and-spoke autour 🌞 Clients |

### 2. ADRs ratifiés (3 P0/P1)

1. **ADR-MESH-L2-001** Doctrine tri-plateforme — 7 décisions D1-D7 (séparation sémantique, flux unidirectionnels, anti-patterns)
2. **ADR-ID-001** Conventions identifiants universels — 8 décisions D1-D8 (12 IDs canoniques, slugs, immutabilité)
3. **ADR-CK-FREE-001** Contraintes ClickUp Free — 8 décisions D1-D8 (5 spaces forcés, 0 Custom Field, tags illimités, time tracking gratuit, critères migration payant)

### 3. SOPs promues Draft → Active (8 — couverture roue complète)

| Squad | SOP | Page ID |
|-------|-----|---------|
| Guardians | GROWTH — Publish LinkedIn Personal Brand Post | `36c7e9e2-658c-8172-b6e0-d043980480c3` |
| Illuminati | SALES-001 — Qualify Inbound Lead | `36c7e9e2-658c-8125-98b9-d542466b2894` |
| Avengers | PRODUCT-003 — Bug Triage P0-P3 | `36c7e9e2-658c-815e-8511-daeab4d00414` |
| Fantastic4 | OPS-001 — Onboard New Nexus Client | `36c7e9e2-658c-816c-a0e3-d6a871c3150a` |
| KangDynasty | IT-001 — Provision VPS Nexus | `36c7e9e2-658c-81b6-8540-c45e4a56a97f` |
| Thunderbolts | FINANCE-001 — Send Invoice Stripe | `36c7e9e2-658c-8123-bbbb-d07fe7084d57` |
| XMen | PEOPLE-001 — Onboard New Agent Capsule | `36c7e9e2-658c-81e7-b06f-c9ba927a5081` |
| Eternals | LEGAL-001 — New Client Contract Signing | `36c7e9e2-658c-81ff-adb5-f730ba099506` |

Chaque promotion porte `Build_Gate = "Doctrinal walkthrough A0+Claude 2026-05-27 + alignement ADR-MESH-L2-001"` et `Last_Audited = 2026-05-27`.

État global MASTER_SOP_DB post-session : **30 Draft / 8 Active / 0 Deprecated / 0 Under_Audit**.

### 4. AntiPanicGuards.psm1 codé + testé

📍 `10_Tech_OS/11_Infra_13th_Doctor/02_Ryan_SysAdmin/modules/AntiPanicGuards.psm1`

6 fonctions exportées + Donna DLQ + heartbeat lean (cf. ADR-HEART-002).

**Test smoke 2026-05-27** :
- `Import-Module` : ✅ 6 fonctions visibles
- `Write-AndVerify` round-trip : ✅ True

### 5. Bascule Notion MCP OAuth → Bearer (souverain)

- Plugin marketplace `productivity` désinstallé
- `@notionhq/notion-mcp-server` configuré dans `.mcp.json` avec `OPENAPI_MCP_HEADERS` Bearer
- Token `NOTION_TOKEN` env var User scope
- Notion now exposes both high-level `notion-*` tools and low-level `API-*` tools (bonus 22 endpoints REST)

## Pivots doctrinaux ouverts

| Sujet | Décision attendue |
|-------|-------------------|
| Migration 3 bases 12-Week-Year Airtable → Baserow L1 | Différé (ADR-MIGR-001 à créer) |
| ADR-SYNC-002 Symphony connectors triplateforme | Différé post-cluster A2 (commencé) |
| Plane.so = L1 Cerritos GTD layer | Cartographie séparée à faire |
| Obsidian = L1 PARA layer | Cartographie séparée à faire |
| Baserow = L1 SNW 12WY layer | Cartographie séparée à faire |

## Références croisées

- Shadow_L0/05 — Tmux/PM2 persistence base
- Shadow_L2/09 — Notion bootstrap plan
- Shadow_L2/10 — Notion Phase 1 completed + ID reference
- Shadow_L2/11 — ClickUp Solaris II/III peuplement
- ADR-NOTION-001 — Back-office Solaris template (Business OS canon)
- ADR-HEART-002 — Heartbeat anti-panique
- ADR-INFRA-001 — Tmux WSL dev + PM2 VPS prod
- ADR-RICK-001 — OpenHarness incarnation + Donna DLQ

## Prochaine session (anticipée)

1. Supabase self-hosted sur VPS Hostinger (en cours)
2. Schema-per-project multi-tenancy
3. Symphony worker `sync-notion-to-supabase.ps1` (utilise AntiPanicGuards)
4. Premier client réel onboardé (déclenche 8 SOPs Active réelles)
5. Cartographie L1 (Plane.so + Obsidian + Baserow)
