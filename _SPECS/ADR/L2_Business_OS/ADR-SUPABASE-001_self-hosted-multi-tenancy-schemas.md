---
id: ADR-SUPABASE-001
title: Supabase Self-Hosted — Multi-Tenancy par Schémas Postgres + Dual MCP (solaris read / aspace write)
status: ACCEPTED
date: 2026-06-08
deciders: [A0 Amadeus]
ratified: "2026-06-08 — Go A0 (A+B)"
proposed_by: Claude Code (A2) — session "Dokploy MCP + Supabase self-hosted multi-projet"
domain: L0 Tech_OS / Data Plane / Self-Hosted Supabase
tags: [#ADR #supabase #self-hosted #multi-tenancy #mcp #postgres #schema #rls #life-os]
related: [ADR-INFRA-001, ADR-INFRA-002, ADR-INFRA-003, ADR-RICK-001, ADR-CANON-001]
---

> **⚠️ STATUS UPDATE 2026-06-19** : **SUPERSEDED FONCTIONNELLEMENT par `ADR-OMK-004` RATIFIED**. L'hosting self-host VPS `148.230.92.235` est pivoté vers **Supabase Cloud** (3 organisations : Life OS, OMK Services, ABC-OS-COMMUNITY). `PGRST_DB_SCHEMAS` reload HITL n'est plus requis (Cloud auto-manage). Le hook `custom_access_token_hook` reste valide en logique mais **doit être re-provisionné sur Cloud** (Condition B ADR-OMK-004). Le pattern multi-tenancy par schémas Postgres + RLS reste valide mais le schéma `omk_internal` est retiré (A1 LOCKED 2026-06-19, mode `internal` retiré). **Voir ADR-OMK-004 §Decision D1 + Runbook Étape 2 sub-step 2.5 (JWT hook Cloud migration).**

# ADR-SUPABASE-001 — Supabase Self-Hosted Multi-Tenancy par Schémas

## Status
**ACCEPTED** — Go A0 le 2026-06-08 ("A+B"). Préparé pour ré-incarner **Life-OS-2026** (`Amdkn/Life-OS-2026`, "The Bridge", aspace-web-os) comme premier projet hébergé sur le Supabase self-hosted du VPS `aspace-vps`.

## Context

Le Supabase self-hosted tourne sur le VPS Hostinger (`148.230.92.235`, source `/srv/aspace/supabase/`, runtime `/srv/aspace/supabase/docker/`) hors Dokploy par décision doctrinale (cf. `30_MEMORY_CORE/README.md`). Services Systemd : `supabase-core`, `supabase-frontend`, `supabase-apps`, `aspace-supabase-structure`.

Aujourd'hui un seul projet (Kalybana) consomme cette instance via `https://supabase.kalybana.com/`. La doctrine A'Space exige de **regrouper plusieurs projets** (Life-OS, projets Picard, micro-sites) sur cette infra unique tout en **respectant des frontières claires** entre eux — au-delà du RLS, qui isole les **lignes** d'une même table mais pas les **espaces de nom**.

Trois patterns d'isolation possibles ont été pesés :

1. **RLS seul (status quo)** : tout dans `public`, chaque projet préfixe ses tables (`life_os_ld01_business`...). Fragile : un `DROP TABLE` mal scopé casse tout, les types TypeScript se mélangent, pas de séparation des `EXECUTE` permissions.
2. **Une database Postgres par projet** : isolation forte mais multiplie les connexions, casse la cohabitation Kong/PostgREST (qui pointe sur une DB unique en self-hosted), double les rôles `service_role`.
3. **Un schéma Postgres par projet (RETENU)** : une seule DB, un schéma par projet (`life_os`, `kalybana`, ...), RLS conservé pour l'isolation user-niveau **à l'intérieur** d'un schéma. PostgREST expose la liste via `PGRST_DB_SCHEMAS`. C'est le pattern recommandé par Supabase pour le multi-tenancy léger.

Côté agentique : Dokploy et Hostinger sont déjà pilotés par MCP (`@ahdev/dokploy-mcp`, `hostinger-api-mcp`). Supabase a deux usages distincts qui justifient **deux MCPs séparés** : observation/diagnostic (read-only, postgres-mcp `crystaldba` style, déjà câblé en `supabase-solaris` via SSH) et écriture/migrations/schéma (à créer, `supabase-aspace`). Séparer permet de rotater les tokens indépendamment selon la doctrine **Test Key Pragma**.

## Decision

### D1 — Isolation : un schéma Postgres par projet
La DB Supabase reste **unique** (`postgres`). Chaque projet vit dans un schéma dédié :

| Projet | Schéma Postgres | URL frontend (cible) |
|---|---|---|
| Kalybana (legacy) | `public` (à migrer ultérieurement vers `kalybana`) | https://kalybana.com |
| Life-OS-2026 (The Bridge) | `life_os` | TBD (sous-domaine Caddy ou Dokploy) |
| `<futur projet picard>` | `<project_snake_case>` | per ADR-INFRA-003 |

**Règle de naming** : `kebab-case` côté repo → `snake_case` côté schéma SQL (ex. `aspace-landing` → `aspace_landing`). Schémas réservés Supabase (`auth`, `storage`, `realtime`, `graphql_public`, `extensions`, `vault`, `pgsodium`, `supabase_functions`) ne sont JAMAIS touchés.

**RLS reste obligatoire** à l'intérieur de chaque schéma pour l'isolation utilisateur. Le schéma isole les projets ; le RLS isole les users d'un projet.

### D2 — Deux MCPs Supabase, responsabilités séparées

| MCP | Direction | Mécanisme | Tools principaux | Token |
|---|---|---|---|---|
| `supabase-solaris` (EXISTANT) | **READ** | SSH `aspace-vps -T /home/amadeus/symphony-workers/mcp-supabase-launch.sh` (postgres-mcp/crystaldba) | `analyze_db_health`, `analyze_query_indexes`, `analyze_workload_indexes`, `explain_query`, `get_top_queries`, `list_objects`, `list_schemas`, `get_object_details`, `execute_sql` (read-only) | Rôle PG `aspace_observer` (SELECT-only) |
| `supabase-aspace` (À CRÉER) | **READ-WRITE** | HTTP/MCP exposé via Caddy : `https://supabase-mcp.148.230.92.235.sslip.io/mcp` OU stdio local via SSH wrapper | `create_project_schema`, `apply_migration`, `execute_sql` (RW), `generate_typescript_types`, `grant_anon_to_schema`, `rotate_anon_key` (futur), `list_project_schemas` | Rôle PG `aspace_admin` (CREATEROLE NoSuperuser, scoped, ne peut PAS toucher `auth.*`, `storage.*`, `realtime.*`) |

Le MCP `supabase-aspace` est un wrapper léger (probablement Python FastMCP ou Node @modelcontextprotocol/sdk) qui se connecte à Postgres directement (pas via PostgREST) avec le rôle `aspace_admin`, et qui maintient une table `_aspace_migrations` par schéma pour idempotence.

### D3 — Bootstrap d'un projet (procédure canonique)
Pour onboarder un nouveau projet `<proj>` :

1. **Schéma SQL** (via MCP `supabase-aspace.create_project_schema`) :
   ```sql
   CREATE SCHEMA IF NOT EXISTS <proj_snake>;
   GRANT USAGE ON SCHEMA <proj_snake> TO anon, authenticated, service_role;
   ALTER DEFAULT PRIVILEGES IN SCHEMA <proj_snake>
     GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO authenticated;
   ALTER DEFAULT PRIVILEGES IN SCHEMA <proj_snake>
     GRANT SELECT ON TABLES TO anon;
   CREATE TABLE <proj_snake>._aspace_migrations (
     id text PRIMARY KEY, applied_at timestamptz DEFAULT now(), checksum text
   );
   ```
2. **PostgREST exposure** : ajouter `<proj_snake>` à `PGRST_DB_SCHEMAS` dans `/srv/aspace/supabase/docker/.env` puis `systemctl restart supabase-core`. Sans ça, `@supabase/supabase-js` ne voit pas le schéma. **Étape manuelle/Codex** — pas dans l'autonomie MCP au MVP (limite acceptée).
3. **Migrations** : repo du projet contient `supabase/migrations/<proj_snake>/NNNN_<name>.sql` ; le MCP applique séquentiellement, traçabilité via `_aspace_migrations`.
4. **Génération des types TypeScript** : `supabase-aspace.generate_typescript_types({ schema: '<proj_snake>' })` produit `src/types/supabase.ts` à committer.
5. **Frontend** : `createClient(url, anon_key, { db: { schema: '<proj_snake>' } })` côté JS.

### D4 — Sécurité & secrets
- `SERVICE_ROLE_KEY` Supabase reste **VPS-side uniquement** (Kong, PostgREST). Jamais distribué aux MCP clients.
- Rôle `aspace_admin` (utilisé par `supabase-aspace`) est un **rôle Postgres custom**, pas service_role. Permissions : `CREATE` sur DB, `CREATE` sur les schémas qu'il a créés, `USAGE` partout sauf `auth`, `storage`, `realtime`, `vault`, `pgsodium`. **Pas de SUPERUSER**.
- Mot de passe `aspace_admin` stocké :
  - VPS : `/srv/aspace/secrets/aspace_admin.pgpass` (chmod 600, owner amadeus)
  - Local Windows : env var User `ASPACE_SUPABASE_ADMIN_DSN` (jamais en .md/.json/git, cf. doctrine Test Key Pragma)
- Rotation : trimestrielle ou post-incident, via `ALTER ROLE aspace_admin PASSWORD '<new>'` + re-set env var.
- Audit : toutes les écritures du MCP loggées dans `<schema>._aspace_audit` (qui ?, quand ?, hash SQL).

### D5 — Documentation ownership (rappel ADR-INFRA-001 D3)
- **Codex documente localement** sur Windows : la spec de chaque migration dans le repo du projet.
- **Hermes documente VPS-side** : l'état effectif (schemas présents, version PostgREST, env vars Kong) dans `/srv/aspace/services/supabase/STATE.md`.
- **Claude Code (A2) maintient cet ADR** et le **registre des schémas** dans `_SPECS/REGISTRY/supabase_schemas.md` (à créer en suivant).

### D6 — Premier livrable : Life-OS-2026
1. Cloner `Amdkn/Life-OS-2026` en born-short `C:\Users\amado\ASpace_OS_V2\30_Business_OS\life-os\` (ADR-INFRA-002).
2. Créer schéma `life_os` via `supabase-aspace.create_project_schema`.
3. Adapter `schema_migration.sql` du repo (qui crée tables dans `public`) → préfixer `CREATE TABLE life_os.<table>` ; le RLS `user_isolation` reste.
4. Ajouter `db: { schema: 'life_os' }` au `createClient` du frontend.
5. Mettre à jour `.env` local pour pointer sur le Supabase VPS (`https://supabase.148.230.92.235.sslip.io` ou `supabase.kalybana.com` selon le routage Caddy) avec `VITE_SUPABASE_ANON_KEY` partagé.
6. `npm run gate` (TSC + Vite build) doit passer.
7. Déploiement frontend via Dokploy (skill `picard-audit-and-prod-workflow` éligible).

### D7 — Pas d'autonomie totale au MVP
Au MVP, **deux étapes restent humain-in-the-loop** :
- L'édition de `PGRST_DB_SCHEMAS` + restart `supabase-core` (impacte tous les projets, risque de coupure)
- Le `GRANT` initial du nouveau schéma à `aspace_admin` (lui-même)

Ces deux étapes seront automatisées plus tard via un sous-skill `supabase-schema-onboard` exécuté par Codex/Hermes côté VPS.

## Consequences

- ✅ **Frontières claires** : chaque projet a son namespace SQL, ses types TS, ses migrations indépendantes.
- ✅ **Une seule infra Supabase** : pas de surcoût mémoire (vs Compose dupliqué), monitoring unifié (`aspace-supabase-health`).
- ✅ **Dual MCP rotable indépendamment** : read et write ont des tokens distincts, conformes Test Key Pragma.
- ✅ **Auth mutualisée** : `auth.users` reste partagé (un user peut être membre de plusieurs projets), ce qui ouvre la voie à un futur **A'Space SSO** pour tous les Bridges/dashboards.
- ⚠️ **Risque : `PGRST_DB_SCHEMAS` partagé** — un mauvais reload Kong coupe tous les projets simultanément. Mitigation : checklist + window de maintenance + `aspace-supabase-health` post-restart.
- ⚠️ **Risque : escalade `aspace_admin`** — si le rôle est mal scopé, il peut écrire dans `auth`. Mitigation : `REVOKE ALL ON SCHEMA auth FROM aspace_admin` explicite dans le bootstrap.
- ⚠️ **Limite : RLS cross-schema** — si un projet a besoin de joindre `auth.users`, c'est OK (lecture), mais joindre une table d'un autre projet est **interdit par design** (pas de policy cross-schema). Si un besoin émerge, ce sera une vue dédiée approuvée par ADR ultérieur.

## Validation Plan (avant passage en ACCEPTED)

- [ ] A0 ratifie ce document ("Go pour ADR-SUPABASE-001")
- [ ] Création du rôle PG `aspace_admin` (Hermes côté VPS)
- [ ] Création du rôle PG `aspace_observer` (Hermes côté VPS) si pas déjà fait pour `supabase-solaris`
- [ ] Implémentation MCP `supabase-aspace` v0.1 (cf. plan d'impl séparé)
- [ ] Bootstrap schéma `life_os` + migration initiale
- [ ] `Life-OS-2026` local en born-short, build PASS, connecté au Supabase VPS
- [ ] Mise à jour `_SPECS/REGISTRY/supabase_schemas.md`
- [ ] Mise à jour `30_MEMORY_CORE/README.md` (paragraphe Supabase VPS)
- [ ] Mise à jour `00_Amadeus/01_Identity_Core/AGENTS.md` si nouvelle responsabilité agent
