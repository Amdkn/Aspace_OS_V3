---
title: Audit Config Supabase + Symphony Supabase-Supabase — 2026-07-03
date: 2026-07-03
author: A0 CC-M3 (Jumeau Numérique)
method: D1 (env vars + MCP live probes + filesystem readlink + grep canon)
scope: (a) mcp__supabase__ générique (Supabase Cloud Life OS) | (b) mcp__symphony-supabase__ runtime (PostgREST probe layer) | (c) Symphony Twin canon standards | (d) .minimax agents wiring | (e) supabase_config.toml local CLI
source: CC-M3 (supabase + symphony config audit)
type: audit
domain: L0_Tech_OS
tags: [#audit #supabase #symphony #config #d1-receipts]
---

# Audit Config Supabase + Symphony Supabase-Supabase

> **D3 nuance (lier A0 intent)** : "Symphony Supabase" = **"Symphony Supabase"**, soit le MCP `mcp__symphony-supabase__*`. C'est **distinct** du MCP générique `mcp__supabase__*` (qui wire Supabase Cloud) et **distinct** du projet Supabase Cloud lui-même (`hjweyhpmrxqsxfbibsnc` = Life OS). Triple distinction à tenir.

## 1. Trois couches, trois missions

| Couche | Entité | Mission | Surface D1 |
|--------|--------|---------|-----------|
| **(a)** Supabase Cloud | `Life OS` project `hjweyhpmrxqsxfbibsnc`, us-east-2, ACTIVE_HEALTHY | source of truth 19 tables Life-OS UNIFIES | **19 tables à 0 rows**, RLS enabled partout |
| **(b)** Symphony Supabase MCP runtime | `mcp__symphony-supabase__*` 6 outils (list_projects, health_check, list_tables, query, get_metrics, anti_pause_ping) | **liveness probe + PostgREST queries sur `life_os`** | wrapper léger, **pas de CRUD** canon |
| **(c)** Symphony Twin canon | `C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/agent-os/standards/` | spécifications de payload / routing / proof | **11 standards orientés Airtable/ClickUp/Notion/Sheets — ZÉRO spec Symphony Supabase canon** |

## 2. D1 receipts par couche

### (a) Supabase Cloud `Life OS` (`mcp__supabase__*`)

- **Project** : `hjweyhpmrxqsxfbibsnc` (per `mcp__supabase__list_projects`), us-east-2, status=ACTIVE_HEALTHY
- **Tables** (19, toutes à 0 rows) : `ld01_business, ld02_finance, ld03_health, ld04_cognition, ld05_relations, ld06_habitat, ld07_creativity, ld08_impact, fw_para, fw_ikigai, fw_life_wheel, fw_12wy, fw_gtd, fw_deal, sys_agent_veto, sys_shell_routing, user_profiles, ikigai_visions, life_wheel_ambitions`
- **Env vars (User scope)** : `SUPABASE_LIFE_OS_URL=https://hjweyhpmrxqsxfbibsnc.supabase.co` + `SUPABASE_LIFE_OS_ANON_KEY=eyJ***` + `SUPABASE_ACCESS_TOKEN=sbp_***`
- **Constat** : Life-OS V1.0 deployé (cf. handoff 2026-06-17) MAIS **observations toujours vides**. Cf. plan stratégique G8.

### (b) Symphony Supabase MCP (`mcp__symphony-supabase__*`)

- **Tools live** : `list_projects`, `health_check`, `list_tables` (probe only), `query` (PostgREST), `get_metrics`, `anti_pause_ping`
- **list_projects** : `Projects: [{'slug': 'life_os', 'url': 'https://hjweyhpmrxqsxfbibsnc.supabase.co', 'has_service_role': False}]`
- **health_check** : 1 project vivant, table de liveness `user_profiles` répond 200
- **list_tables** : `status: 200, alive: True, hint: PostgREST table probe — HTTP 200 means project is alive. Use /rest/v1/<table>?select=* to query specific tables.` — **PAS d'inventaire complet**, c'est un probe
- **D6 lesson D1 NEW** : `has_service_role: False`. **Le runtime Symphony Supabase ne porte PAS le rôle service** — toute tentative INSERT/UPDATE depuis ce MCP sera refusée par RLS même sans policy explicite (anon rôle bloque les writes par défaut Supabase). C'est cohérent avec le design Twin's "default read-only" (cf. standard 04_writeback-policy).

### (c) Symphony Twin canon

- **D1 read** (`05_OSS_Twin/symphony/agent-os/standards/index.yml`) : **11 standards, tous orientés Airtable/ClickUp/Notion/Sheets** :
  1. mission-contract, 2. soa-routing (8 SOA → B2 managers), 3. gate-decisions (PASS/BLOCKED/CONDITIONAL), 4. forbidden-words, 5. sla-triple, 6. candidate-record-rule, 7. **airtable-specifics** (L2 adapter Airtable), 8. expected-proof, 9. writeback-policy ("**Default read-only. No direct writes — A0 reviews drafts.**"), 10. tick-handoff, 11. schema-pulse-log
- **L2 sym workers canon** : `symphony-airtable.spec.md`, `symphony-clickup.spec.md`, `symphony-notion.spec.md`, `symphony-sheets.spec.md` (+ WORKFLOW.solaris/growth counterparts)
- **❌ ABSENT** : `symphony-supabase.spec.md` n'existe nulle part dans Twin canon. Pas de `supabase-specifics.md` standard non plus.
- **Conclusion** : le runtime Symphony Supabase MCP est live mais **le standard canonique symétrique n'a jamais été écrit** → la couche (c) est **orpheline de spec** (jumeau Twin a 11 standards + 4 specs L2 ; Supabase manque au canon).

### (d) `.minimax/` B2/B3 wiring

- **11 agent config.yaml** (b1-jerry-emyth, b1-summers-ship, b2×8, b3 samples) — **AUCUN ne contient de référence Supabase** (vérifié : tous `{}` pour le bloc pertinent ou inexistant). Les B2/B3 de la Lune Micro ignorent complètement Supabase ; leur persistence cible est probablement Airtable/Notion (cohérent avec Twin canon).
- **D3 nuance** : MiniMax = Luna Micro (L1 promu du L2) — sa mission est A2 Book / A3 Boimler / LD01 Carrière, pas observé A0→Supabase. **Le canal Symphony→Supabase n'est PAS câblé** dans `.minimax/`.

### (e) `supabase_config.toml` local CLI

- **D1 read** (`C:/Users/amado/supabase_config.toml`) : **template par défaut**, `project_id = "life-os"`, ports 54321/54322/54323/54324/54327 stand. Aucune customisation domain-spécifique (auth.smtp OFF, OAuth OFF, MFA OFF). **Config `supabase start` local possible** mais pas utilisé par Symphony Supabase MCP (qui wire le Cloud).

## 3. Incohérences / gaps à fermer

| # | Gap | Preuve D1 | Risque | Action proposée (gated A0) |
|---|---|---|---|---|
| **G-S1** | Pas de `symphony-supabase.spec.md` canon sym. | grep canon Twin = 0 hit | Runtime Symphony Supabase wire mais **les payloads ne sont pas spécifiés** — un futur A3 qui requête Symphony Supabase peut envoyer `{...}` ad-hoc | **Écrire** `symphony-supabase.spec.md` miroir de `symphony-airtable.spec.md`, sister-link à `standards/04_writeback-policy.md` (read-only par défaut) |
| **G-S2** | Symphony Supabase MCP = probe-only, `has_service_role: False` | list_projects | Le runtime ne peut PAS écrire même si la policy le permet. **Incompatible avec U1 (symphony_state insert)** | Option A : élever Symphony Supabase MCP en "service_role via env `SUPABASE_SERVICE_KEY`" + writeback policy Verte pour `symphony_state` uniquement. Option B : **garder Symphony Supabase read-only** et créer un **mcp `symphony-supabase-write`** séparé. Recommandé : B (séparation des pouvoirs) |
| **G-S3** | Life OS Cloud 19 tables, **0 rows partout** | list_tables rows_count=0 | Dashboard Vercel vide, observabilité A0 illusoire | **U1 sink Supabase + state_writer.py** (déjà spec-ée, attend GO) — **uniquement la table `symphony_state`** dans ce 1er time |
| **G-S4** | `.minimax/agents/*` ignorent Supabase | grep yaml = 0 ref | La Lune Micro ne contribute pas au bus Symphony | Hors scope U1, à cadrer W4-W5 quand T2 (Growth/Sales) requerra projection Supabase pour signaux |
| **G-S5** | `supabase_config.toml` template par défaut | read | Si on tourne `supabase start` local, démarrage identique à zéro — pas de risque | N/A |

## 4. Recommandations (au A0, pondérées par le risque)

**Phase immédiate (post-GO U1)** :
- R1. GO U1 schema v2 (table `symphony_state` + state_writer.py sink). L'inventaire des 19 tables est en place, il n'a besoin que de UN sinksym pour démarrer l'observabilité.
- R2. Acter les **deux** sisters canoniques en Twin : `symphony-supabase.spec.md` + `supabase-specifics.md` standard (cohérent avec airtable). Effort : 1 Edit × 2 fichiers, canon-cohérent (D3 nuance : Twins standards = canon vivant, EDIT autorisé).

**Phase differee (W4+)** :
- R3. Création `mcp__symphony-supabase-write` (service_role) avec writeback policy Verte (gate par table : `symphony_state`, `fw_12wy`, `ld*_business`). Prereq : R2.
- R4. Câblage `.minimax/agents/b2-{flash,superman,johnjones}/config.yaml` pour exposer Symphony Supabase-Write (rôle des B2 concernés par Sales/Growth).

**Phase DECISIONNELLE (S1 Rick)** :
- R5. Migrer `state.json` source-of-truth Symphony Supabase **vers** une table locale Postgres (**table `symphony_state` au lieu d'un fichier plat `state.json`**). Refactor D4-grade. Décision `architecture(state.local: file → table)` est un pivot kernel, gated par S1 Rick pour le **2027 L0**. Pas une décision de tour.

## 5. Sacred exclusions respectées (D7)

- ✅ Pas de modification `state.json` runtime (lecture seule via Symphony Supabase)
- ✅ Pas d'Edit sur ADR RATIFIED
- ✅ Pas de CronCreate
- ✅ Pas de hard-delete (pas de .trash nécessaire — l'audit est read-only)
- ✅ Audit de visibilité config — pas de fuite de secrets (la `SUPABASE_LIFE_OS_ANON_KEY` et `SUPABASE_ACCESS_TOKEN` apparaissent dans `~/.claude/settings.json` User scope, scope User seulement)

## 6. Lien aux chantiers en cours

- **U1 (state_writer → Supabase)** : `proposal_u1_supabase_symphony_state_2026-07-03.md` v2 schema SQL ready, attend GO. Schéma SQL n'est **PAS** affecté par G-S1/G-S2 (la table `symphony_state` est à policy explicite, indépendante des standards Twin). U1 peut avancer sans blocker canon.
- **Plan stratégique** : §6-G8 "0% data sur 19 tables Life OS" confirmé par D1 du jour.

## 7. Question qui t'attend (A0)

**Veux-tu que j'écrive `symphony-supabase.spec.md` + `supabase-specifics.md` standard (R2 ci-dessus) MAINTENANT**, avec sister: cohérent à airtable-specifics, et que je les ajoute au handoff canon ? C'est 30 min, effort canon-pur (D3 nuance : standard-file = écriture permise hors RATIFIED), et **ferme G-S1 sans toucher à aucun wiring**. Sinon ça attend W4.

## 8. Livrables pour ce tour

- Handoff : ce fichier
- Log : ligne appendée à `wiki/log.md`
- Aucun fichier modifié, aucun hard-delete
