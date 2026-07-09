---
id: ADR-ABCOS-001
title: ABC OS Community — Stratégie Backend Supabase Multi-Tenant (single-schema-per-entity, RLS org_id)
status: ACCEPTED
date: 2026-06-10
ratified_by: A0 Amadeus (airlock 3-tours clos 2026-06-10 — GO tel quel)
proposed_by: Claude Code (A2) — session "ABC OS"
domain: L2 Business OS / ABC OS & Child Care BOS / Product (Avengers)
tags: [#ADR #abc_os #supabase #multi-tenant #rls #org_id #schema #nextjs]
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-INFRA-002, ADR-INFRA-003, ADR-META-001, CERRIROS_HANDOVER, handoff_abc_os_community_dev_2026-06-10]
supersedes: none
---

> **⚠️ STATUS UPDATE 2026-06-19** : **HOSTING PIVOTED par `ADR-ABCOS-002` RATIFIED**. La couche **hosting** (self-host VPS `148.230.92.235` → Supabase Cloud ABC-OS-COMMUNITY Org) est pivotée. Le **multi-tenant model** (org_id + RLS, ce ADR §D1-D5) et le **mixed-tenancy model** (§D10) restent valides 100%. **Voir ADR-ABCOS-002 §Decision D1 + Runbook Étape 2 sub-steps 2.4 (5 fichiers doc sync atomic) + 2.5 (JWT hook Cloud migration) + 2.7 (PGRST_DB_SCHEMAS Dashboard action — P0 BLOCKER pour queries `abc_os` live data)**.

# ADR-ABCOS-001 — ABC OS Community — Stratégie Backend Supabase Multi-Tenant

## Status
**ACCEPTED** — 2026-06-10. Airlock 3-tours clos :
- **Tour 1 (clarification)** : 5 décisions extraites (domaines, auth phase 2, public coop dir, JWT hook impl, i18n)
- **Tour 2 (organisation)** : ADR rédigé avec 9 décisions D1–D9 + 12 phases P1.1–P5.2
- **Tour 3 (veto review)** : A0 = **GO tel quel** + 2 ajustements explicites :
  - **Domaine ABC OS** = `abc.kalybana.com` (TLD souverain kalybana aligné infra Supabase existante)
  - **JWT Hook impl** = Postgres native function (recommandé)
- Sous-décisions par défaut (non contestées) : auth email/password Phase 1, anon sans accès public coop directory, i18n FR-only non bloquant

Ancre le produit **ABC OS Community** (GitHub `Amdkn/02-ABC-OS`, local `30_Business_OS/10_Projects/abc/apps/abc-os-community/`, design source of truth `apps/ABC OS Community-01/`) sur le Supabase self-hosted déjà opérationnel.

## Context

`abc-os-community` est un dashboard **multitenant** (chaque coopérative = un tenant) déjà en prod côté UI (Vercel `prj_HSw4IBR2omI5qegmEinOksr6xzo0`) mais **100% mock côté données** (`src/data/mockData.ts` = Umoja Weavers / Amara / Nairobi hardcodés). Le handoff `handoff_abc_os_community_dev_2026-06-10.md` ouvre les tickets #1–#7 ; **#5 (env vars Supabase)** est celui que cet ADR ferme.

Le canon existe déjà :
- `ADR-SUPABASE-001` (ACCEPTED 2026-06-08) — **un schéma Postgres par produit**, double MCP (`supabase-solaris` read, `supabase-aspace` write à créer), rôles PG `aspace_admin`/`aspace_observer`.
- `ADR-OMK-001` (ACCEPTED 2026-06-08) — **précédent** OMK dual-product : 2 schémas (`omk_internal`, `omk_saas`), multi-tenancy par `org_id` + RLS (PAS schéma-par-tenant), auth mutualisée via `auth.users`.
- `05_supabase/AGENTS.md` — contrat opérationnel (DOCKER-USER iptables W2, grants explicites W3, HITL W4, JWT `org_id` claim W5).
- `CERRIROS_HANDOVER.md` — l'entité **Child Care BOS** est un **produit distinct** soumis à conformité G8 Legal, PAS un module de ABC OS.

Pas de canon existant pour ABC OS → cet ADR填补 le trou.

## Decision

### D1 — Deux schémas Postgres (un par entité business)
Conforme à `ADR-SUPABASE-001` (frontière = produit) + `ADR-OMK-001` (dual-product = 2 schémas) + `CERRIROS_HANDOVER` (ABC OS ≠ Child Care BOS).

| Schéma | Entité | URL cible (per INFRA-003) | Statut |
|---|---|---|---|
| `abc_os` | ABC OS (cooperative dashboard) | **`abc.kalybana.com`** (Vercel + domaine custom) | **Phase 1** |
| `abc_child_care` | Child Care BOS (entité régulée) | `childcare.kalybana.com` (à confirmer Phase 5) | **Scaffold Phase 1, contenu Phase 5 (post G8 sign-off)** |

`auth.users` reste **mutualisé** entre les 2 schémas (un user peut être membre de plusieurs orgs dans les 2 entités).

### D2 — Multi-tenancy = `org_id UUID` + RLS (PAS schéma-par-coop)
Mirror exact du pattern `ADR-OMK-001` §D2 :
- Chaque coopérative = une ligne dans `abc_os.organizations` (le tenant).
- Table pivot `abc_os.memberships(user_id, org_id, role)` — un user peut appartenir à N coops.
- Toutes les tables métier ont une colonne `org_id UUID NOT NULL REFERENCES abc_os.organizations(id)`.
- **RLS obligatoire** sur chaque table :
  ```sql
  USING (org_id = (auth.jwt() ->> 'org_id')::uuid)
  WITH CHECK (org_id = (auth.jwt() ->> 'org_id')::uuid);
  ```
- L'isolation se fait au niveau JWT : un user connecté a **un** `org_id` actif dans son access token (sélection via UI = "switch org"). Pas de session multi-org simultanée.
- **Pas de schéma-par-coop** (ne scale pas ; ADR-OMK-001 l'a explicitement rejeté). Réservé à un futur tier enterprise (ADR ultérieur si besoin).

### D3 — Auth + JWT custom claims
- **Supabase Auth** (`auth.users` partagé) — remplace le "Amara" hardcodé.
- **Custom Access Token Hook** (Postgres function) injecte `org_id` + `role` + `entity_type` dans le JWT.
- Rôles RBAC : `'owner' | 'admin' | 'member' | 'viewer'`.
- Phase 1 : email/password. Phase 2 (optionnelle) : magic link + OAuth (Google) — à arbitrer.
- Switch d'org actif : client-side `supabase.auth.setSession()` après sélection d'une `membership`.

### D4 — Modèle de données (mapping types Next.js → tables Postgres)

Types source : `apps/abc-os-community/src/types/index.ts` (vérifié lecture 2026-06-10).

| Type Next.js | Table Postgres | Colonnes clés | RLS ? |
|---|---|---|---|
| `Member` | `abc_os.members` | `id`, `org_id`, `user_id` (FK auth.users), `name`, `full`, `initials`, `tint` | oui |
| `HubPulse.community` | `abc_os.hub_pulse` | `id`, `org_id`, `hub` (enum), `payload` (JSONB) | oui |
| `HubPulse.learn/build/brand` | (même table, filtrée par `hub`) | idem | oui |
| `ActionItem` | `abc_os.action_items` | `id`, `org_id`, `hub`, `title`, `description`, `due_at`, `urgent`, `assignee_id` | oui |
| `SpotlightProject` | `abc_os.spotlight_projects` | `id`, `org_id`, `name`, `tag`, `description`, `place`, `ms`, `ms_total`, `pct`, `team` (JSONB) | oui |
| `FeedItem` | `abc_os.feed_items` | `id`, `org_id`, `who`, `av` (JSONB), `hub`, `what`, `detail`, `when_at`, `place` | oui |
| (nouveau) | `abc_os.organizations` | `id`, `slug` (unique), `name`, `place`, `created_at` | oui (admin-only) |
| (nouveau) | `abc_os.memberships` | `id`, `user_id`, `org_id`, `role`, `created_at` | oui (self + admin) |

Indexs : `(org_id)` sur chaque table métier + `(org_id, hub)` sur `hub_pulse` et `action_items` + UNIQUE sur `memberships(user_id, org_id)`.

Enum `hub` = `'community' | 'learn' | 'build' | 'brand'` (aligné sur `ActionItem.hub`).

`INITIAL_DATA` actuel (Umoja Weavers / Amara / Nairobi) devient un **seed** : `apps/abc-os-community/supabase/migrations/abc_os/0003_seed_umoja.sql` — exécutable seulement en dev (`mcp__supabase-aspace__execute_sql` gated par `app_env = 'dev'`).

### D5 — RLS policies (template)

5 politiques minimum, à créer par table métier (mirror OMK 7 `*_isolation`) :

| Policy | Rôle | USING | WITH CHECK |
|---|---|---|---|
| `<table>_select_member` | authenticated | `org_id = (auth.jwt() ->> 'org_id')::uuid` | n/a |
| `<table>_insert_admin` | authenticated | n/a | `org_id = (...) AND (auth.jwt() ->> 'role') IN ('admin','owner')` |
| `<table>_update_admin` | authenticated | `org_id = (...)` | `org_id = (...) AND role IN ('admin','owner')` |
| `<table>_delete_owner` | authenticated | `org_id = (...)` | `org_id = (...) AND role = 'owner'` |
| `memberships_self_select` | authenticated | `user_id = auth.uid() OR role IN ('admin','owner')` | n/a |

`anon` : **aucun accès** aux tables `abc_os.*` (cohérent avec `omk_saas` "SELECT only" — pour ABC OS on est plus strict, c'est full auth).

### D6 — Frontend integration (Next.js 15)

```ts
// src/lib/supabase.ts
import { createClient } from '@supabase/supabase-js';
import { Database } from '@/types/supabase';  // généré par supabase-aspace

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
  { db: { schema: 'abc_os' }, auth: { persistSession: true } }
);
```

- Remplacer l'import `INITIAL_DATA, HUB_CONFIG` dans `page.tsx` + les 4 hub pages par des hooks TanStack Query (`useQuery(['hub_pulse', orgId], ...)`).
- Server Components Next.js 15 : utiliser `@supabase/ssr` (cookie-based session) pour le rendu initial.
- Génération types : `supabase-aspace.generate_typescript_types({ schema: 'abc_os' })` → commit `src/types/supabase.ts` (mirror OMK D4).

### D7 — Env vars Vercel (3 scopes)

Per `04_vercel/AGENTS.md` W2 — pattern `update_env_variable` × 3 en parallèle.

| Key | Scope dev/preview/prod | Secret ? |
|---|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | les 3 | non (URL publique) |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | les 3 | non (anon JWT) |
| `SUPABASE_SERVICE_ROLE_KEY` | **JAMAIS** | n/a (VPS-side only) |

`anon_key` = celui du Supabase self-hosted VPS, **pas** un clé jetable. Stocké en env User Windows `ASPACE_SUPABASE_ANON_KEY` (jamais en `.md`/`.json`/git, per Test Key Pragma).

### D8 — Dépendance amont (blockers)
- [ ] **`supabase-aspace` MCP implémenté** (D2 ADR-SUPABASE-001) — sans lui, on ne peut pas bootstrapper `abc_os` schema depuis le client Claude. Fallback : bootstrap manuel via SSH `aspace-vps` + script Python (codex, one-shot).
- [ ] **`PGRST_DB_SCHEMAS` étendu** (HITL ADR-SUPABASE-001 D7) — ajout de `abc_os` et `abc_child_care` à la liste, suivi de `systemctl restart supabase-core`. Étape HITL.
- [ ] **`aspace_admin` GRANT initial** sur les 2 nouveaux schémas (HITL ADR-SUPABASE-001 D7).
- [ ] **`.env.local` jamais commité** (`.gitignore` ligne 34) — seul `NEXT_PUBLIC_*` exposé au client.

### D9 — Phased delivery

| Phase | Livrable | Owner | Bloqueur |
|---|---|---|---|
| P1.1 | Schéma `abc_os` créé + tables + indexs | Claude A2 + Codex SSH | D8#1, D8#2, D8#3 |
| P1.2 | Policies RLS (D5) | Claude A2 | P1.1 |
| P1.3 | Types TypeScript générés + commit | Claude A2 | P1.1 |
| P1.4 | Env vars Vercel 3-scope (D7) | Claude A2 + Vercel MCP | aucune |
| P2.1 | Seed Umoja Weavers | Claude A2 | P1.1 |
| P2.2 | TanStack Query + remplacement mockData | Claude A2 + TDD guide | P1.3, P2.1 |
| P3.1 | Auth UI (login/signup/logout) | Claude A2 | P1.1 |
| P3.2 | Custom Access Token Hook (org_id claim) | Codex SSH | P1.1 |
| P3.3 | Switch-org UI | Claude A2 | P3.2 |
| P4.1 | E2E Playwright (login → 4 hubs → logout) | e2e-runner | P3.x |
| P5.1 | Scaffold `abc_child_care` schema (vide) | Claude A2 | G8 Legal sign-off (CERRIROS) |
| P5.2 | Contenu Child Care | BLOQUÉ | G8 Legal sign-off |

### D10 — Build Hub v2 shared catalog coexistence (2026-06-12)

Build Hub v2 ajoute 4 tables shared catalog (`build_categories`, `build_projects`, `build_phases`, `build_tasks`) qui coexistent avec `build_milestones` (per-tenant, D4). Les 17 projets physiques sont des TEMPLATES partageables communauté (homesteading, architecture, offgrid, micro_revenue, agentic_build), pas per-tenant. Mixed-tenancy model : pas d'org_id sur les 4 nouvelles tables, RLS = `TO authenticated USING (true)` (mirror Learn D4). Le handoff Antigravity proposait org_id sur ces tables — REJETÉ pour cette raison. Tables ajoutées en migration 0010, seedées en 0011, RLS en 0012.

**Mixed-tenancy summary après D10** (référence opérationnelle pour les 4-hub) :

| Table family | Tenancy | RLS pattern | Migration(s) |
|---|---|---|---|
| Learn (4) | shared catalog | `FOR SELECT TO authenticated USING (true)` | 0004 + 0008 |
| Build — milestones (1) | per-tenant | 4 policies : select_member, admin_insert/update, owner_delete | 0005 + 0008 |
| Build — v2 catalog (4) | shared catalog | `FOR SELECT TO authenticated USING (true)` | 0010 + 0012 |
| Brand (1) | per-tenant append-only | 4 policies : select_member, admin_insert, owner_update, owner_delete | 0005 + 0008 |

## Consequences

- ✅ **Aligné avec le canon** : 100% compatible avec ADR-SUPABASE-001 (schéma unique par produit) et ADR-OMK-001 (multi-tenancy `org_id` + RLS, pas schéma-par-tenant).
- ✅ **Auth mutualisée** : `auth.users` partagé → futur SSO A'Space unlocked.
- ✅ **Self-hosted** : pas de Vendor lock-in Supabase Cloud, conforme doctrine A'Space.
- ✅ **Testable adversarialement** : isolation tenant = RLS = preuve mathématique par `EXPLAIN` et tests dédiés.
- ⚠️ **2 schémas ≠ 1** : double migration / double type-gen. Acceptable car 2 entités business distinctes (per CERRIROS).
- ⚠️ **Phase 1 bloquée par `supabase-aspace` MCP** : si l'impl MCP prend du retard, fallback SSH manuel. Pas bloquant long-terme.
- ⚠️ **Child Care vide Phase 5** : risque d'oubli. Mitigation : ADR tracker + check-in mensuel (B1 cadence).
- ⚠️ **Custom Access Token Hook** = code SQL côté VPS — toute erreur casse l'auth globale. Mitigation : staging schema d'abord + tests adversariaux + HITL deploy.

## Validation Plan (avant passage en ACCEPTED)

- [x] A0 ratifie ("Go ADR-ABCOS-001" via airlock 3-tours) — **2026-06-10, GO tel quel**
- [x] Domaine ABC OS arrêté : `abc.kalybana.com`
- [x] JWT Hook impl arrêtée : Postgres native function
- [ ] `supabase-aspace` MCP livré (D2 ADR-SUPABASE-001), OU fallback SSH documenté
- [ ] Schéma `abc_os` créé sur Supabase VPS (vérif : `mcp__supabase-solaris__list_schemas` retourne `abc_os`)
- [ ] `PGRST_DB_SCHEMAS` étendu + `supabase-core` restart OK (vérif : `curl http://aspace-vps:8000/rest/v1/organizations -H "Accept-Profile: abc_os"` → 200)
- [ ] 5 RLS policies testées adversarialement (org A ne lit jamais org B)
- [ ] Frontend : `npm run dev` + login Umoja + voir les 4 hubs + logout, sans mock
- [ ] Ticket #5 du handoff clôturé (env vars Vercel câblées en 3 scopes)
- [ ] `_SPECS/REGISTRY/supabase_schemas.md` mis à jour (ajout `abc_os`, `abc_child_care`)
- [ ] Wiki log entry : `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` + `30_MEMORY_CORE/README.md`
- [ ] Build Hub v2 schema appliqué (4 tables) — migration 0010
- [ ] Build Hub v2 seed appliqué (5 categories + 17 projects + 40 phases + 111 tasks) — migration 0011
- [ ] Build Hub v2 RLS appliqué (4 nouvelles policies) — migration 0012
- [ ] ADR-ABCOS-001 D10 amendé (coexistence mixed-tenancy)

## Décisions arbitrées par A0 (airlock 2026-06-10)

1. ~~**Domaines**~~ : ✅ **ABC OS** = `abc.kalybana.com` (kalybana = TLD infra souveraine). **Child Care** = `childcare.kalybana.com` (à confirmer Phase 5 post G8).
2. **Auth Phase 2** : 🔵 **reporté** — email/password Phase 1 suffit, magic link + Google OAuth = Phase 2 optionnelle (re-ouvrir ADR si besoin).
3. **Public coop directory** : 🔵 **derrière auth** — anon = 0 accès, conforme doctrine OMK et modèle souverain.
4. ~~**Custom Access Token Hook**~~ : ✅ **Postgres native function** (D8#2 — pas de dépendance externe, versionnable en migrations).
5. **i18n** : 🔵 **non bloquant** — FR-only Phase 1, next-intl en couche séparée (ticket #6 reste ouvert hors-ADR).

## Décisions A0 post-ratification (2026-06-12)

> Section append-only : décisions A0 post-airlock-2026-06-10. Chaque entrée référence le D# amendé/ajouté.

- **D10 Build Hub v2 (airlock 2026-06-12)** : GO Option A (coexistence ordonnée) — 4 tables shared catalog à côté de `build_milestones` per-tenant. Renommage migration Antigravity en 0010/0011/0012 (le 0008 RLS existant n'est pas écrasé). Mixed-tenancy model respecté.
