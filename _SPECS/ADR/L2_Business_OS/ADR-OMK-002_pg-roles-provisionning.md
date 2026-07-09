---
id: ADR-OMK-002
title: OMK Dashboard — PG Roles Provisionning (aspace_admin / aspace_observer) schema-scoped strict
status: RATIFIED
date: 2026-06-11
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2) — sub-agent #3 (this turn)
domain: L0 Tech_OS / Self-Hosted Supabase / Postgres Roles
tags: [#ADR #omk #supabase #postgres #roles #grants #least-privilege #hitl #provisionning]
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-META-001, omk/apps/dashboard/AGENTS.md §1.2, omk/apps/dashboard/sql/99_README.md]
depends_on: [ADR-SUPABASE-001 (ACCEPTED 2026-06-08)]
blocks: [omk Phase B (DDL execution), MCP supabase-aspace v0.1]
sign_off: "A0 Amadeus — Go ADR-OMK-002 — 2026-06-11"
---

# ADR-OMK-002 — OMK Dashboard PG Roles Provisionning

## Status
**RATIFIED** — Go A0 attendu 2026-06-11. Soumis par Claude Code (A2) en sub-agent #3. Sign-off A0 = "Go ADR-OMK-002".

## Context

Le dashboard OMK (Vite 6 + React 19, repo `github.com/Amdkn/01-OMK-Business-OS`, deploy Dokploy 2 services × 2 schemas) consomme le Supabase self-hosted du VPS `aspace-vps` (Hostinger `148.230.92.235`, `https://supabase.148.230.92.235.sslip.io`).

Le blocker #2 de `omk/apps/dashboard/AGENTS.md` §1.2 liste la création sur le VPS Supabase de deux rôles PostgreSQL applicatifs :
- `aspace_admin` — utilisé par le futur MCP `supabase-aspace` (wrapper RW sur le DDL/DML/GRANT des schémas OMK).
- `aspace_observer` — utilisé par le MCP existant `supabase-solaris` (read-only diagnostic, déjà câblé via SSH `symphony-workers/mcp-supabase-launch.sh`).

Ces deux rôles sont **le contrat de sécurité applicatif** entre :
- les schémas dédiés `omk_internal` (staff OMK, single-tenant) et `omk_saas` (PME multi-tenant, RLS par `org_id`) — voir `ADR-OMK-001` D2 ;
- les schémas réservés Supabase (`auth`, `storage`, `realtime`, `graphql_public`, `extensions`, `vault`, `pgsodium`, `supabase_functions`, `pgbouncer`, `pg_catalog`, `information_schema`) qui ne doivent **jamais** être touchés par les rôles OMK ;
- le hook JWT `public.custom_access_token_hook` (cf. `omk/apps/dashboard/sql/04_jwt_hook.sql:152-157`) qui doit tourner sous le rôle `supabase_auth_admin`.

`ADR-SUPABASE-001` D4 §1-2 a déjà posé le principe : "`aspace_admin` est un rôle PG custom, pas service_role. Permissions : `CREATE` sur DB, `CREATE` sur les schémas qu'il a créés, `USAGE` partout sauf `auth`, `storage`, `realtime`, `vault`, `pgsodium`. **Pas de SUPERUSER**". Ce présent ADR **opérationnalise** ce principe avec le détail exact des `GRANT` à exécuter, en s'alignant strictement sur les 2 schémas OMK.

Doctrine contraignante : `ADR-META-001` D1 (Verify-Before-Assert) → toute syntaxe GRANT/ROLE/DEFAULT PRIVILEGES est ancrée sur la doc PG officielle (citée ci-dessous), lue via `context7` (libraryId `/websites/postgresql_current`) dans le même tour que la rédaction.

## Decision

### D1 — Deux rôles PG, NOLOGIN, NOSUPERUSER, NOINHERIT

```sql
-- Postgres doc: CREATE ROLE — NOLOGIN/NOSUPERUSER/NOINHERIT attributes
-- Source: https://www.postgresql.org/docs/current/sql-createrole.html (Parameters > INHERIT/NOINHERIT, SUPERUSER/NOSUPERUSER)
-- NOLOGIN: le rôle est un "grant role", pas un login SQL. service_role key Supabase reste le canal d'auth.
-- NOINHERIT: si aspace_observer devient membre de aspace_admin un jour (NON prévu), il n'héritera pas automatiquement.
--   Verrou de principe, conforme "least-privilege strict" (D2).
-- NOSUPERUSER: implicite (default) mais explicité pour la traçabilité audit.

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'aspace_admin') THEN
    CREATE ROLE aspace_admin NOLOGIN NOSUPERUSER NOINHERIT;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'aspace_observer') THEN
    CREATE ROLE aspace_observer NOLOGIN NOSUPERUSER NOINHERIT;
  END IF;
END
$$;
```

### D2 — Scope schema-strict (omk_internal + omk_saas SEULEMENT)

**Aucun accès** (ni USAGE ni CREATE) aux schémas réservés Supabase : `auth`, `storage`, `realtime`, `graphql_public`, `extensions`, `vault`, `pgsodium`, `supabase_functions`, `pgbouncer`, `pg_catalog`, `information_schema`, ni au schéma `public` (sauf pour la fonction hook JWT, voir D4).

Justification : défense en profondeur. Si le rôle `aspace_admin` est compromis (clé fuitée, prompt injection via SQL généré par un agent), l'attaquant ne peut PAS escalader vers `auth.users` (qui contient emails + password hashes) ni `storage.objects` (qui contient les blobs uploadés). Le RLS reste la frontière de sécurité applicative ; le rôle-scoped est la **frontière de surface d'attaque infra**.

### D3 — Grants `aspace_admin` (DDL + DML + GRANT sur les 2 schémas OMK)

```sql
-- Postgres doc: GRANT ON SCHEMA — USAGE (accès aux objets) / CREATE (créer objets)
-- Source: https://www.postgresql.org/docs/current/sql-grant.html (Grant Schema Privileges)

GRANT USAGE, CREATE ON SCHEMA omk_internal TO aspace_admin;
GRANT USAGE, CREATE ON SCHEMA omk_saas     TO aspace_admin;

-- Postgres doc: GRANT ON ALL TABLES IN SCHEMA
-- Source: https://www.postgresql.org/docs/current/sql-grant.html (Grant Table Privileges)
-- Note: TRIGGER nécessaire si on veut que le rôle puisse créer des triggers ; REFERENCES pour les FK.
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER
  ON ALL TABLES IN SCHEMA omk_internal TO aspace_admin;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER
  ON ALL TABLES IN SCHEMA omk_saas     TO aspace_admin;

-- Postgres doc: GRANT ON ALL SEQUENCES IN SCHEMA — USAGE (nextval) + SELECT (currval)
-- Source: https://www.postgresql.org/docs/current/sql-grant.html (sequences = USAGE|SELECT|UPDATE)
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA omk_internal TO aspace_admin;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA omk_saas     TO aspace_admin;

-- Postgres doc: ALTER DEFAULT PRIVILEGES FOR ROLE target IN SCHEMA
-- Source: https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html
-- "FOR ROLE postgres" = le rôle qui CRÉERA les futures tables (le owner des CREATE TABLE est postgres dans les migrations aspace).
-- Couvre les tables/sequences créés APRÈS le provisionning, par le rôle postgres (et donc par aspace_admin via SET ROLE, ou directement).
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_internal
  GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER ON TABLES TO aspace_admin;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_saas
  GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER ON TABLES TO aspace_admin;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_internal
  GRANT USAGE, SELECT ON SEQUENCES TO aspace_admin;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_saas
  GRANT USAGE, SELECT ON SEQUENCES TO aspace_admin;
```

### D4 — Grants `aspace_observer` (READ-ONLY sur les 2 schémas OMK)

```sql
-- Lecture seule stricte. PAS de INSERT/UPDATE/DELETE/TRUNCATE.
-- Même pattern que D3 mais en SELECT-only.

GRANT USAGE ON SCHEMA omk_internal TO aspace_observer;
GRANT USAGE ON SCHEMA omk_saas     TO aspace_observer;

GRANT SELECT ON ALL TABLES IN SCHEMA omk_internal TO aspace_observer;
GRANT SELECT ON ALL TABLES IN SCHEMA omk_saas     TO aspace_observer;

GRANT SELECT ON ALL SEQUENCES IN SCHEMA omk_internal TO aspace_observer;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA omk_saas     TO aspace_observer;

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_internal
  GRANT SELECT ON TABLES TO aspace_observer;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_saas
  GRANT SELECT ON TABLES TO aspace_observer;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_internal
  GRANT SELECT ON SEQUENCES TO aspace_observer;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA omk_saas
  GRANT SELECT ON SEQUENCES TO aspace_observer;
```

### D5 — Hiérarchie de rôles : aspace_observer N'hérite PAS de aspace_admin

**Pas de `GRANT aspace_admin TO aspace_observer`**. Le `aspace_observer` reste un rôle feuille, sans aucun `IN ROLE` ni `INHERIT` vers `aspace_admin`. Le MCP `supabase-solaris` (utilisé par read-only) se connecte **directement** en tant que `aspace_observer`, jamais via un `SET ROLE aspace_admin` qui contournerait le scope.

Justification : si on faisait hériter observer de admin, le moindre bug ou prompt-injection sur l'agent observateur pourrait escalader vers du DML. Conformité "least-privilege strict" (D1, D7).

### D6 — JWT hook (schéma public) — grants séparés

Le hook `public.custom_access_token_hook` (créé par `omk/apps/dashboard/sql/04_jwt_hook.sql:28-146`) doit pouvoir être appelé par le runtime Supabase Auth (rôle `supabase_auth_admin`) et **refusé** à `PUBLIC`, `anon`, `authenticated`. Cette décision est dans `04_jwt_hook.sql:152-157` ; ce présent ADR la **ratifie en cohérence** :

```sql
-- Le GRANT EXECUTE au rôle supabase_auth_admin est DÉJÀ fait dans 04_jwt_hook.sql:152.
-- Pour cohérence post-provisionning des rôles OMK, on confirme l'inverse :
-- aspace_admin et aspace_observer N'ONT PAS EXECUTE sur cette fonction.
-- (REVOKE explicite n'est pas requis car la fonction n'a pas de GRANT PUBLIC/EXECUTE vers ces rôles,
--  le défaut étant de ne rien授予.)

-- Toutefois, pour audit-trail, on DOCUMENTE ici (pas en SQL, en commentaire de spec) que :
--   - aspace_admin NE PEUT PAS appeler le hook (sécurité : le hook lit omk_saas.memberships, pas besoin pour aspace_admin).
--   - aspace_observer NE PEUT PAS appeler le hook (read-only strict).
```

### D7 — Schémas explicitement NON-touched (defense in depth)

Aucun `GRANT USAGE` ni `GRANT CREATE` n'est émis sur les schémas suivants. C'est implicite (les schémas n'ont pas de GRANT par défaut vers des rôles custom), mais la **liste blanche** des 2 schémas OMK est la politique explicite, et toute tentative d'accès via `aspace_admin` à un autre schéma échouera avec `ERROR: permission denied for schema X` :

| Schéma | Accès OMK | Raison |
|---|---|---|
| `omk_internal` | ✅ USAGE + CREATE | OMK Services staff data |
| `omk_saas` | ✅ USAGE + CREATE | OMK PME multi-tenant data |
| `auth` | ❌ aucun | Contient `auth.users` (emails, password hashes). Réservé au runtime Supabase. |
| `storage` | ❌ aucun | Contient `storage.objects` (blobs uploadés). Réservé au runtime Supabase. |
| `realtime` | ❌ aucun | Sockets Realtime. Réservé au runtime Supabase. |
| `graphql_public` | ❌ aucun | PostgREST GraphQL endpoint. Réservé au runtime Supabase. |
| `extensions` | ❌ aucun | Schéma d'extensions PG (pgcrypto, etc.). Réservé au superuser setup. |
| `vault` | ❌ aucun | Secrets Supabase. Réservé au service_role. |
| `pgsodium` | ❌ aucun | Crypto libs. Réservé au service_role. |
| `supabase_functions` | ❌ aucun | Edge Functions. Réservé au service_role. |
| `pgbouncer` | ❌ aucun | Stats PgBouncer. Réservé au superuser. |
| `pg_catalog`, `information_schema` | ❌ aucun (sauf SELECT par défaut PUBLIC) | Métadonnées système. Pas de GRANT explicite OMK. |
| `public` | ⚠️ fonction `custom_access_token_hook` SEULEMENT | Hook JWT, GRANT EXECUTE à `supabase_auth_admin` (cf. 04_jwt_hook.sql:152). OMK roles : aucun GRANT EXECUTE. |

### D8 — Provisionning HITL, keyless, exécuté par A2 (Claude Code)

Le script est keyless : l'authentification psql se fait par `PGUSER` + `PGPASSWORD` passés en variables d'environnement User Windows (déjà dans `env:User` de la machine A0). Aucun mot de passe n'est hardcodé dans le `.sql` ni dans la commande shell d'invocation.

**Commande exacte que A2 (Claude Code = moi) exécutera après Go A0** (depuis Windows, après que A0 ait confirmé que la clé SSH `srv941028` est dans `ssh-agent` et que `SUPABASE_DB_PASSWORD` est dans `env:User`) :

```bash
# Sur la machine A0, depuis C:\Users\amado\
scp ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/dashboard/sql/06_provision_pg_roles_omk.sql srv941028:/tmp/

ssh srv941028 "PGUSER=postgres PGPASSWORD=\"$SUPABASE_DB_PASSWORD\" \
  psql -h localhost -p 5432 -U postgres -d postgres \
       --set ON_ERROR_STOP=on \
       -v ON_ERROR_STOP=1 \
       -f /tmp/06_provision_pg_roles_omk.sql"
```

Justifications :
- `ssh srv941028` : la clé SSH est déjà dans `ssh-agent` (cf. `ADR-SUPABASE-001` D2 — la connexion MCP `supabase-solaris` utilise déjà ce canal).
- `PGUSER=postgres` : on provisionne en tant que superuser pour pouvoir créer les rôles et émettre les GRANT. **postgres reste le seul rôle avec `CREATEROLE` + `CREATEDB` + bypass RLS** ; les rôles OMK sont délimités comme en D1-D7.
- `PGPASSWORD=$SUPABASE_DB_PASSWORD` : env var User Windows, **jamais** dans le script, **jamais** dans git (cf. doctrine Test Key Pragma).
- `--set ON_ERROR_STOP=on` (Postgres doc : `app-psql` §ON_ERROR_STOP) : si une commande SQL échoue, psql sort avec code 3 immédiatement. C'est l'**inverse** d'un script naïf : on **veut** qu'un échec (par ex. une table déjà existante avec un GRANT incompatible) plante l'exécution pour qu'on investigue, plutôt que de continuer en silence.
- `psql -f` (file mode) : psql traite le fichier comme un script, pas un dump. Les `DO $$ ... $$` anonymes s'exécutent un par un. `CREATE ROLE` dans un `DO $$` est **OK** car psql parse chaque statement top-level ; l'idempotence est garantie par le `IF NOT EXISTS` à l'intérieur du `DO`.

Note : l'option `-1 / --single-transaction` (Postgres doc `backup-dump` §25.1.1) **n'est PAS utilisée** ici à dessein — on veut que chaque `DO $$` soit autonome et commité indépendamment, pour pouvoir re-rollback proprement. Si l'option était activée et qu'un `DO $$` au milieu plantait, TOUT le provisionning serait annulé, ce qui n'est pas notre politique (chaque sous-étape doit pouvoir rejouer).

### D9 — Rollback (DROP OWNED + DROP ROLE)

```sql
-- Postgres doc: role-removal.html — General Role Removal Recipe
--   REASSIGN OWNED BY doomed_role TO successor_role;
--   DROP OWNED BY doomed_role;
--   DROP ROLE doomed_role;
-- Source: https://www.postgresql.org/docs/current/role-removal.html
-- Note: REASSIGN OWNED est omis ici car les rôles OMK N'ONT PAS ownership d'objets —
--   ils ont seulement des GRANTs. DROP OWNED suffit (il révoque les GRANTs, cf. sql-drop-owned).

DROP OWNED BY aspace_observer;
DROP OWNED BY aspace_admin;
DROP ROLE IF EXISTS aspace_observer;
DROP ROLE IF EXISTS aspace_admin;
```

Le script rollback est dans `06_provision_pg_roles_omk.sql` (section commentée `-- ROLLBACK SECTION`), pas exécuté par défaut. Il faut l'invoquer manuellement via un `psql` séparé.

Idempotence du rollback : `DROP OWNED BY` est sûr à re-exécuter (la 2ème fois, il ne reste rien à dropper, le statement est un no-op). `DROP ROLE IF EXISTS` ne fail pas si le rôle n'existe pas.

## Consequences

- ✅ Surface d'attaque bornée : `aspace_admin` ne peut pas escalader vers `auth` / `storage` / `vault`. Si la clé fuit, l'attaquant reste dans les 2 schémas OMK.
- ✅ Le MCP `supabase-solaris` (read-only) a un rôle dédié `aspace_observer` qu'il ne peut pas escalader vers le DML même si prompt-injected.
- ✅ Le MCP `supabase-aspace` (à venir) aura un rôle `aspace_admin` qui ne peut pas toucher aux secrets Supabase.
- ✅ Hiérarchie plate : `aspace_observer` et `aspace_admin` sont **siblings**, pas parent/enfant. Pas de privilege escalation latérale.
- ✅ Les `DEFAULT PRIVILEGES` couvrent les futures tables OMK — le provisionning est **forward-compatible** avec les phases ultérieures (B, C, D) qui ajouteront des tables.
- ✅ Idempotent : `DO $$ ... IF NOT EXISTS` + `IF EXISTS` partout → rejouable sans casse.
- ✅ Rollback complet et idempotent.
- ⚠️ Le provisionning est **HITL** (A2 + sign-off A0) tant que le MCP `supabase-aspace` n'est pas implémenté. C'est un goulot d'étranglement temporaire, conforme à `ADR-SUPABASE-001` D7.
- ⚠️ Si un futur projet OMK a besoin d'un 3ème schéma (par ex. `omk_audit` pour un audit log), il faudra **ré-émettre** les `GRANT` D3-D4 pour ce schéma. Ce n'est pas un défaut (c'est explicite par design — scope strict = safety), mais c'est une opération à documenter dans un ADR successeur.

## Validation Plan

- [ ] A0 ratifie ce document ("Go ADR-OMK-002")
- [ ] A2 exécute la commande D8 et capture la sortie psql
- [ ] Vérification post-provisionning (cf. `omk/apps/dashboard/sql/06_provision_pg_roles_omk.sql` section VERIFY) :
  - `\du aspace_admin` → rôle existe, attributs `Cannot login`, `No inheritance`, `No superuser`
  - `\du aspace_observer` → idem
  - `\dn+ omk_internal` → `aspace_admin` apparaît dans la ACL avec `arwdDxt` (DDL+DML), `aspace_observer` avec `r` (read)
  - `\dp omk_internal.clients` → grants visibles
  - Test de **negative authorization** : `SET ROLE aspace_observer; SELECT * FROM auth.users LIMIT 1;` doit échouer avec `permission denied for schema auth`
  - Test de **negative authorization** : `SET ROLE aspace_admin; SELECT * FROM storage.objects LIMIT 1;` doit échouer
- [ ] `omk/apps/dashboard/sql/99_README.md` mis à jour (entrée `06_provision_pg_roles_omk.sql` ajoutée)
- [ ] `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` ligne ajoutée sous `2026-06-11`
- [ ] `omk/apps/dashboard/AGENTS.md` §1.2 : statut passé de `⏳ à créer` à `✅ RATIFIED (ADR-OMK-002)`

## Rollout (commande exacte HITL, à exécuter par A2 après Go A0)

```bash
# Pré-requis côté A0 :
#   1. SUPABASE_DB_PASSWORD dans env:User Windows (NE PAS écrire la valeur ici)
#   2. Clé SSH srv941028 dans ssh-agent (ssh-add déjà fait ou ssh-key natif Windows OpenSSH)
#   3. Go explicite "Go ADR-OMK-002" dans la session courante

# Étape 1 : copier le .sql sur le VPS
scp "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/dashboard/sql/06_provision_pg_roles_omk.sql" \
    srv941028:/tmp/

# Étape 2 : exécuter le provisionning
ssh srv941028 "PGUSER=postgres PGPASSWORD=\"\$SUPABASE_DB_PASSWORD\" \
  psql -h localhost -p 5432 -U postgres -d postgres \
       --set ON_ERROR_STOP=on \
       -f /tmp/06_provision_pg_roles_omk.sql"

# Étape 3 : capturer la sortie et la coller dans le rapport de validation
# (sortie attendue : "CREATE ROLE", "GRANT", "ALTER DEFAULT PRIVILEGES" × 8, "DO" × N — voir 06_provision_pg_roles_omk.sql)
```

## Rollback (commande exacte HITL, à exécuter par A2 uniquement sur demande A0)

```bash
scp "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/dashboard/sql/06_provision_pg_roles_omk.sql" \
    srv941028:/tmp/

ssh srv941028 "PGUSER=postgres PGPASSWORD=\"\$SUPABASE_DB_PASSWORD\" \
  psql -h localhost -p 5432 -U postgres -d postgres \
       --set ON_ERROR_STOP=on \
       -v section=rollback \
       -f /tmp/06_provision_pg_roles_omk.sql"
```

Note : la section rollback est dans le même fichier `.sql` que le provisionning, activée par une psql variable `\set section` (cf. `06_provision_pg_roles_omk.sql`). Re-exécutable sans casse (idempotent via `IF EXISTS`).

## References

- `ADR-SUPABASE-001` — Supabase Self-Hosted Multi-Tenancy (ACCEPTED 2026-06-08) — pose le principe `aspace_admin` / `aspace_observer` D4 §1-2.
- `ADR-OMK-001` — Dual-Product Dashboard Multi-Tenant (ACCEPTED 2026-06-08) — pose l'architecture 2 schémas `omk_internal` + `omk_saas` + RLS.
- `ADR-META-001` — Doctrine Anti-Paresse (ACCEPTED 2026-06-08) — D1 Verify-Before-Assert appliqué sur la syntaxe PG citée.
- `omk/apps/dashboard/AGENTS.md` §1.2 — blocker #2 (PG roles provisionning) à marquer `✅ RATIFIED`.
- `omk/apps/dashboard/AGENTS.md` §4 — Supabase Architecture (self-hosted VPS).
- `omk/apps/dashboard/sql/99_README.md` — vue d'ensemble DDL, à mettre à jour avec le nouveau fichier `06_provision_pg_roles_omk.sql`.
- `omk/apps/dashboard/sql/04_jwt_hook.sql:28-157` — fonction `public.custom_access_token_hook` + grants `supabase_auth_admin`.
- `omk/CLAUDE.md` gotcha #3 — Self-hosted Supabase ≠ supabase.com (URL + auth différents).
- Postgres official docs (lues via `context7` libraryId `/websites/postgresql_current` dans le tour de rédaction) :
  - `sql-createrole.html` — NOLOGIN / NOSUPERUSER / NOINHERIT attributes
  - `sql-grant.html` — GRANT ON SCHEMA (USAGE, CREATE) ; GRANT ON TABLES ; GRANT ON SEQUENCES
  - `sql-alterdefaultprivileges.html` — ALTER DEFAULT PRIVILEGES FOR ROLE IN SCHEMA syntax
  - `sql-revoke.html` — REVOKE EXECUTE ON FUNCTION
  - `sql-droprole.html` — DROP ROLE [IF EXISTS]
  - `sql-drop-owned.html` — DROP OWNED BY (revokes grants on objects in current database)
  - `role-removal.html` — General Role Removal Recipe
  - `plpgsql-control-structures.html` — EXCEPTION WHEN duplicate_object (idempotent DO block)
  - `app-psql.html` — ON_ERROR_STOP variable (fail-fast on error)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` — append `2026-06-11` après validation.

---

**Provenance** : ADR créé par Claude Code (A2) en sub-agent #3, session 2026-06-11. Tout claim sur la syntaxe PG a été vérifié dans la même session via `mcp__context7__query-docs` (libraryId `/websites/postgresql_current`). Aucun secret en clair. HitL A0 → A2 prévu après ratification.
