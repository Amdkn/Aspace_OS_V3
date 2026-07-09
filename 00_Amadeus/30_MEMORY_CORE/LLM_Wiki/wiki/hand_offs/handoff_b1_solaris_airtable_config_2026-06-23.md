---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-23
type: handoff
domain: L2
tags: [B1, solaris, airtable, clickup, plane, config]
---

# Handoff B1 Solaris — Airtable Config (2026-06-23)

> Handoff canonique pour A0 (Airtable prioritaire) + A1 Morty/Beth (câblage opérationnel) + futurs agents (anti-amnesia D4).
> **D4 append-only**. Toute modification ultérieure = nouvelle entrée, JAMAIS d'écrasement.
> **v2 amendement 2026-06-23** : pivot D6 #7 — plugin marketplace remplace npm-stdio comme canonical path. Procedure 7-step → 5-step. Sections §A-F amendées. D4 no-amnesia preserved (canon D6 immutable, handoff amend doc vivant).

## A0 Pivot (D3 + D7) — verbatim

**A0 2026-06-23** :
> "On configure Airtable en Priorité et remplace Clickup par Plane pour les Limites d'Appel API qui sont limite pour le plan gratuit de Clickup"

**3 implications** :
1. **Airtable = priorité câblage** (B1 Solaris Gate #3, après Notion ✔ et Plane ✔)
2. **ClickUp = retiré entièrement** (free plan 100 req/min incompatible besoin 200+/h dry-run)
3. **Plane = remplacement ClickUp** pour orchestration multi-agent (workspace `aspace-core` déjà LIVE)

## État Airtable (D1 vérifié 2026-06-23)

### 3 axes indépendants

| # | Axe | D1 receipt | Statut |
|---|---|---|---|
| 1 | Env var `AIRTABLE_PAT` User scope HKCU | length=82, format `pat<14chars>.<43chars>` | ✔ (mais unused en plugin marketplace, OAuth remplace) |
| 2 | Binaire `airtable-mcp-server.cmd` sur PATH Windows | `C:\Users\amado\AppData\Roaming\npm\airtable-mcp-server.cmd` | ✔ MAIS pattern architectural non-préféré (D6 #7) |
| 3 | Package npm global installé | `airtable-mcp-server@1.13.0` | ✔ MAIS sera désinstallé post-plugin LIVE |

### D3 nuance architecturale (A0 correction explicite)

A0 veut **vendor-official MCPs (HTTPS remote avec Bearer/OAuth)**, PAS npm community stdio. Le binaire installé est techniquement fonctionnel MAIS architecturalement incompatible avec A0 intent.

**3 patterns MCP architecturaux** (D6 Entry #7 amendement 2026-06-23) :

| Pattern | Airtable actuel | A0 intent |
|---|---|---|
| **Plugin marketplace** (`@claude-plugins-official`, OAuth browser) | ⏸ pending install | ✔ preferred for 1st-party |
| **stdio local** (npm community, subprocess JSON-RPC, secret env var process) | ✔ `airtable-mcp-server@1.13.0` installé | ✘ non-préféré pour 1st-party |
| **HTTPS distant** (vendor-official, Bearer/OAuth, streaming SSE ou streamable-http) | n/a | ⏸ fallback si plugin indispo |

URL vendor-official candidate : `https://mcp.airtable.com/mcp` (à confirmer en D1 verify post-A0 share — Airtable publie aussi un MCP distant officiel, distinct du package npm community et du plugin marketplace).

**Plugin marketplace = preferred path** : `claude plugin install airtable@claude-plugins-official` (per Airtable docs screenshot 2026-06-23).

## Outil final B1 Solaris (post-pivot)

| Outil | Statut | Pattern | Workspace/Project | Rôle Life OS |
|---|---|---|---|---|
| **Airtable** | 🔴 pending (Test Key Pragma) | vendor-official HTTPS remote | (A0 fourni) | DEAL drafts + Ikigai tracker |
| **Plane** | 🟢 LIVE | Python thin wrapper (Symphony Lane B) | `aspace-core` / `79df867c-06b5-4e61-b3f1-68aa886c39a3` | 12WY + PARA issues |
| **Notion** | 🟢 LIVE | npm stdio `notion-mcp-server` | Bearer `OPENAPI_MCP_HEADERS` | AGENTS canon + Life Wheel LDxx |
| **ClickUp** | ❌ retiré | npm stdio (pivot D3+D7) | n/a | (remplacé par Plane) |

## Étapes de câblage Airtable v2 (D6 #7 — plugin marketplace)

1. **Agent D1 verify préreq** : `claude plugin --help` → exit 0 ✔ (commande existe dans PATH CC)
2. **Agent exec install** : `claude plugin install airtable@claude-plugins-official` → D1 verify output contient `airtable` dans la liste plugins installés
3. **A0 HITL** : `Restart Claude Code` (D6 #4 — CC tool registry STATIC at session start, nouveau plugin = ignoré jusqu'à restart)
4. **A0 Authenticate OAuth** : post-restart, `/plugin` menu → Installed tab → flèche droite sur "Airtable" → Enter sur "Authenticate" → browser OAuth flow Airtable → grant scopes
5. **Agent D1 verify post-auth** : `mcp__airtable__list_bases` → ≥1 base retournée = 🟢 LIVE ; `list_tables` + `list_records` = smoke test OK

## D6 Lessons shipped (cross-link ADR-META-006)

- **Entry #5** : npm community stdio vs vendor-official HTTPS remote (D3 nuance architecturale) — `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md`
- **Entry #6** : ClickUp free plan API rate limits → Plane replacement (A0 D3+D7 pivot) — idem
- **Entry #7** : Claude Code plugin marketplace = canonical 1st-party MCP path (D6 amendement 3-pattern taxonomy) — idem

## Open Follow-ups Q3 2026

- [ ] Agent D1 verify préreq `claude plugin --help` (runbook §1 v2)
- [ ] Agent exec `claude plugin install airtable@claude-plugins-official` (runbook §2 v2)
- [ ] A0 restart CC (runbook §3 v2)
- [ ] A0 Authenticate OAuth browser (runbook §4 v2)
- [ ] Agent D1 verify post-auth 3 axes `list_bases` / `list_tables` / `list_records` (runbook §5 v2)
- [ ] Agent désinstaller npm stdio `airtable-mcp-server` (cleanup, post-LIVE confirmé)
- [ ] Agent désinstaller npm stdio `clickup-mcp-server` (cleanup post-pivot D6 #6)
- [ ] A0 GO loop B1 Solaris (Gates #1-2 verbatim, post-Airtable LIVE)
- [ ] B1 Solaris dry-run 1 semaine (post-câblage complet)
- [ ] B1 Solaris validation 3 sem (Gate #5)

## Refs canoniques

- **Ce handoff** : `wiki/hand_offs/handoff_b1_solaris_airtable_config_2026-06-23.md`
- **ADR-META-006 (D6 catalog append-only)** : `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` (Entries #5 + #6)
- **ADR-META-001 (D1-D8 doctrine)** : `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`
- **ADR-AAAS-001 (AaaS 3 Variants)** : `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (B1 Solaris = first variant on amd)
- **Plane LIVE handoff** : `wiki/hand_offs/handoff_saas_cloud_activated_2026-06-21.md` §10
- **MCP persistence v2 handoff** : `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md`
- **A0 Divinity Arsenal handoff** : `wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md`
- **A0 Jumeau Numérique handoff** : `wiki/hand_offs/handoff_a0_jumeau_numerique_2026-06-21.md`
