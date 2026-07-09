---
source: handoff
date: 2026-06-08
type: handoff
domain: L0 Tech_OS + L2 Business OS / Supabase prod / Dashboards deploy
tags: [#handoff #antigravity #supabase #dokploy #caddy #omk #solaris #prod #bypass]
from: Claude Code (A2, Desktop)
to: Antigravity (VS Code extension, MiniMax, TRUE bypass channel)
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-META-001, skill:aspace-supabase-mastery]
---

# HANDOFF — Antigravity prend le relais : Supabase prod + déploiement dashboards

> **Pourquoi toi (Antigravity)** : la suite touche VPS prod + Dokploy + déploiement → canal **bypass réel** requis (Claude Desktop est limité). Tu as le bouton "Bypass permissions" fonctionnel.
> **Lis EN PREMIER** : le skill `~/.claude/skills/aspace-supabase-mastery/SKILL.md` (tout le savoir VPS Supabase, gotchas inclus) + ADR-SUPABASE-001 + ADR-OMK-001 + ADR-META-001 (Verify-Before-Assert).
> **Auto-suffisant** : tu démarres à froid, tout est ici.

## État VÉRIFIÉ au 2026-06-08 (ne pas re-supposer)
- **Incident réseau RÉSOLU** : la chain `DOCKER-USER` droppait le trafic interne vers 5432/6543/8000... Fix appliqué + persisté (`/etc/iptables/rules.v4`, backup `.bak.20260608-supabase-fix`). Détail : `wiki/sources/source_incident_supabase_docker_user_drop_2026_06_08.md`.
- **Supabase 13/13 conteneurs healthy** sur `aspace-vps`.
- **Phase E solaris FAITE** : schémas `solaris_internal` + `solaris_saas` créés, grants table appliqués, anon révoqué de `solaris_internal`, exposés via `PGRST_DB_SCHEMAS`. Vérif REST : saas 200 `[]`, internal 401, public 200.
- **OMK dashboard** (`30_Business_OS/10_Projects/omk/apps/dashboard`, Vite/React) : Phase A+B locales faites (data layer Supabase-ready + fallback localStorage, 6 views branchées, `tsc` + `build` GREEN). PAS commité. PAS de schémas OMK sur le VPS encore.
- **Solaris dashboard** (`30_Business_OS/10_Projects/solaris/apps/dashboard`, **Next.js 16**) : CLI a fait Phase D scaffolding (repos/hooks) avant de brûler son quota. À vérifier/finir.

## Mission (ordre recommandé)

### 1. Caddy : exposer l'API REST HTTPS (débloque les dashboards prod)
Actuellement seul `supabase-studio.148.230.92.235.sslip.io` est routé. Les dashboards ont besoin d'un endpoint REST HTTPS.
- Ajouter un bloc Caddy `supabase-api.148.230.92.235.sslip.io` (ou domaine au choix A0) → reverse_proxy `localhost:8000` (kong).
- ⚠️ kong:8000 est dans la liste `DOCKER-USER` ; Caddy host→localhost:8000 passe par la règle `127.0.0.1 ACCEPT` (OK). Vérifier après reload Caddy : `curl -s -o /dev/null -w '%{http_code}' https://<domaine>/rest/v1/ -H 'apikey: <ANON>'` → 200/401, pas 000.
- Mettre à jour les `.env` des dashboards avec ce domaine (corriger le `.env.example` OMK qui pointe par erreur sur `supabase.148.230.92.235.sslip.io`).

### 2. Créer les schémas OMK (miroir solaris)
Via le pattern du skill `aspace-supabase-mastery` (section bootstrap). `omk_internal` (staff) + `omk_saas` (tenant org_id+RLS). Tables selon `omk/apps/dashboard/REBUILD_WORKFLOW.md` §2 (clients, documents, agents, invoices, sops + organizations, memberships). **Appliquer les grants sur tables existantes** (gotcha #2) + exposer via PGRST_DB_SCHEMAS. Vérifier end-to-end.

### 3. Finir Solaris (Next.js) — Phases C→E frontend
Per `HANDOFF_2026-06-08_solaris-dashboard-backend.md` : `@supabase/ssr`, `middleware.ts` tenant, auth, brancher les 12 views sur les repos. `npm run build` + `eslint` GREEN.

### 4. Déploiement Dokploy (Phases F/G) pour les 2 dashboards
- OMK (Vite) : `server.js` Express + Dockerfile multi-stage. 2 services Dokploy (`omk-dashboard-internal` VITE_APP_MODE=internal, `omk-dashboard-saas` saas).
- Solaris (Next.js) : `output: 'standalone'`, pas de server.js. Service(s) Dokploy.
- Dokploy piloté par MCP `@ahdev/dokploy-mcp` (déjà câblé VPS, `DOKPLOY_URL=http://localhost:3000`, port hôte 3002).
- **Test isolation tenant** (org A ≠ org B) avant trafic réel.

## Garde-fous (ADR-META-001 + sécurité)
- **Verify-Before-Assert** : chaque affirmation = une commande qui la prouve. Pas de "c'est réglé" sans `curl`/`docker ps`/`tsc` à l'appui.
- Toute règle DROP `DOCKER-USER` doit être précédée d'un ACCEPT `172.16.0.0/12` (gotcha #1).
- Grants : `psql -c` explicite, jamais heredoc-over-ssh ; vérifier avec `has_table_privilege`.
- Backup `.env` / `rules.v4` / Caddyfile avant toute édition.
- Jamais SERVICE_ROLE_KEY côté client ni en git. anon en env Dokploy uniquement.
- Born-short (ADR-INFRA-002) pour les repos build-bearing.
- VPS/Dokploy = ton canal bypass ; commit seulement sur accord A0.

## Definition of Done
- [ ] REST API HTTPS routée + testée (200/401, pas 000)
- [ ] Schémas OMK créés, grants OK, exposés, testés end-to-end
- [ ] Solaris Next.js build GREEN, connecté Supabase
- [ ] Dashboards déployés Dokploy (internal + saas), isolation tenant prouvée
- [ ] `30_MEMORY_CORE/README.md` + `wiki/log.md` mis à jour
- [ ] Rapport final à A0 avec preuves (codes HTTP, statuts conteneurs)
