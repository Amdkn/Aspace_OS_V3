---
source: CC-M3 (IAM Supabase App-Level RBAC OMK)
date: 2026-07-03
type: handoff
domain: L2_Business_OS
tags: [#handoff #iam #supabase #rbac #omk #customers]
---

# Handoff — IAM Supabase App-Level RBAC (OMK Services Customers)

- **Date** : 2026-07-03
- **Chantier** : A — IAM App-Level RBAC
- **Project** : `ndvqwcapwcnpdvknxcjw` (omk-saas-os.vercel.app · OMK Services Customers)
- **Schema** : `public` (new) + cross-schema read from `omk_saas.memberships`
- **Doctrine** : `ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md`
- **Pending chain** : `handoff_jwt_hook_cloud_migration_2026-06-19.md` (PENDING 2026-06-19, ce handoff le débloque partiellement — le hook SQL est appliqué, l'activation Dashboard reste HITL A0)
- **Status** : **SQL SHIPPED** · Dashboard activation = HITL A0 · RLS policies live · seed 27/27 permissions OK

---

## D1 Receipts (vérifiés post-migration, requêtes brutes)

### 1. Hook function + tables + counts

```sql
SELECT
  (SELECT count(*) FROM information_schema.routines
     WHERE routine_schema = 'public' AND routine_name = 'custom_access_token_hook') AS hook_fn_count,
  (SELECT count(*) FROM public.user_roles)        AS user_roles_count,
  (SELECT count(*) FROM public.role_permissions)  AS role_permissions_count,
  (SELECT count(*) FROM information_schema.tables
     WHERE table_schema = 'public'
       AND table_name IN ('user_roles','role_permissions')) AS public_tables_count;
```

| Mesure | Valeur | Attendu | Status |
|---|---:|---:|:---:|
| `hook_fn_count` | **1** | 1 | OK |
| `user_roles_count` | **0** | 0 (vierge) | OK |
| `role_permissions_count` | **27** | ≥15 | OK |
| `public_tables_count` | **2** | 2 | OK |

### 2. Routine privileges (sécurité du hook)

```sql
SELECT grantee, privilege_type
  FROM information_schema.routine_privileges
 WHERE routine_schema = 'public'
   AND routine_name = 'custom_access_token_hook'
 ORDER BY grantee, privilege_type;
```

| grantee | privilege_type | Attendu | Status |
|---|---|---|:---:|
| `postgres` | EXECUTE | OK (owner) | OK |
| `service_role` | EXECUTE | OK | OK |
| `supabase_auth_admin` | EXECUTE | **REQUIS** | OK |
| `PUBLIC` | — | absent | OK |
| `anon` | — | absent | OK |
| `authenticated` | — | absent | OK |

### 3. Role × permissions matrix

```sql
SELECT role, count(*) AS perm_count
  FROM public.role_permissions
 GROUP BY role
 ORDER BY CASE role
            WHEN 'admin' THEN 1 WHEN 'coach' THEN 2
            WHEN 'manager' THEN 3 WHEN 'client' THEN 4
            WHEN 'observer' THEN 5 END;
```

| role | perm_count | matrice |
|---|---:|---|
| admin | **14** | audit.{r,w} + clients.{r,w} + invoices.{r,w} + sops.{r,w} + documents.{r,w} + agents.{r,w} + legal_docs.{r,w} |
| coach | **5** | clients.{r,w} + sops.{r,w} + documents.r |
| manager | **4** | clients.r + invoices.{r,w} + documents.r |
| client | **2** | clients.r + invoices.r |
| observer | **2** | clients.r + invoices.r |

### 4. Function attributes (pg_proc)

```sql
SELECT proname, prosecdef, proconfig::text AS config, provolatile
  FROM pg_proc WHERE proname = 'custom_access_token_hook';
```

| attribut | valeur | requis | status |
|---|---|---|:---:|
| `prosecdef` | **true** | true (SECURITY DEFINER) | OK |
| `provolatile` | **s** | s (STABLE) | OK |
| `proconfig` | `{"search_path=""}` | search_path vide | OK |

---

## Architecture livrée

### Tables (public schema — neuves)

1. **`public.user_roles`** — `id`, `user_id` (FK→auth.users), `org_id`, `role` (CHECK in 5 valeurs), `created_at`, UNIQUE(user_id, org_id).
2. **`public.role_permissions`** — `id`, `role`, `permission`, UNIQUE(role, permission).

Les deux ont **RLS ON** + policies gated par `auth.jwt() ->> 'user_role'`.

### Function (cross-schema OK)

`public.custom_access_token_hook(event jsonb) RETURNS jsonb` — plpgsql, **SECURITY DEFINER**, **STABLE**, `search_path=''`.

Logique en 3 temps :
- (a) extract `user_id` depuis event.
- (b) lookup `omk_saas.memberships.org_id` (cross-schema via SECURITY DEFINER).
- (c) lookup `public.user_roles.role` avec **priority admin > coach > manager > client > observer**.
- (d) inject `org_id` + `user_role` dans `event->'claims'` via `jsonb_set` (skip si NULL).

### Sécurité

- `GRANT EXECUTE ... TO supabase_auth_admin` ✓
- `REVOKE EXECUTE ... FROM PUBLIC, anon, authenticated` ✓
- `SET search_path = ''` → force fully-qualified names, anti-search-path-injection ✓
- RLS policies : self-read user_roles + admin-write gated par JWT claim ✓

---

## HITL restant pour A0 (Dashboard Supabase OMK)

> **Pas mon job** (D6 #4 = CC tool registry static). Le hook est créé, l'activation UI est manuelle.

### Étape 1 — Toggle Dashboard

- URL : `https://supabase.com/dashboard/project/ndvqwcapwcnpdvknxcjw/auth/hooks`
- Section : **"Custom Access Token Hook"**
- Toggle : **ON**
- Schema : `public`
- Function : `custom_access_token_hook`
- **Save**

### Étape 2 — Env var (optionnel si non auto-set par toggle)

```bash
# Local : pour validation future via MCP direct
# Dashboard → Settings → API → Env vars (Production) :
GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true
```

### Étape 3 — Seed le 1er admin (bootstrap chicken-and-egg)

Le 1er user_roles row doit être inséré via **service_role** (bypass RLS). Options :

- **Option A** — Dashboard SQL Editor (run-as service_role) :
  ```sql
  INSERT INTO public.user_roles (user_id, org_id, role) VALUES
    ('<uuid-amadeus>', '<uuid-org-from-omk_saas.organizations>', 'admin');
  ```
- **Option B** — Seed script via Edge Function `seed-admin` (à écrire, post-activation hook).
- **Option C** — Service role key dans `.env` local A0 + script Python.

---

## Anti-patterns documentés (à NE PAS re-découvrir)

1. **❌ Hardcoder service_role key en chat** : utiliser MCP (déjà ce qu'on fait), rotation post-test (Test Key Pragma).
2. **❌ Modifier `omk_saas`** : le hook est cross-schema par design (cross-schema read OK via SECURITY DEFINER). Toute mutation `omk_saas.*` = ADR violation.
3. **❌ Oublier `search_path = ''`** : faille d'injection classique, le SECURITY DEFINER court avec les droits du definer, search_path manipulable = privilege escalation. Fixé ici.
4. **❌ Oublier REVOKE FROM PUBLIC** : n'importe quel rôle DB pourrait appeler la fonction et lire les memberships. Fixé.
5. **❌ chicken-and-egg RLS admin-write** : la policy "user_roles admin write" check `(auth.jwt()->>'user_role') = 'admin'`. Pour le 1er admin, la JWT n'a PAS le claim → boucle. **Fix** : insert via service_role (bypass RLS).
6. **❌ Oublier STABLE** : la fonction est deterministe par user_id → STABLE requis pour que Postgres puisse l'inliner/cache. Sans STABLE = performance hit + risque de re-eval par token refresh.
7. **❌ Multi-role user ambigu** : un user peut avoir N rows dans `user_roles`. La priority ORDER BY résout l'ambiguïté (admin > coach > manager > client > observer). Documenter explicitement.

---

## Liens canon

- ADR : `ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md`
- Handoff chain (PENDING avant ce chantier) : `wiki/hand_offs/handoff_jwt_hook_cloud_migration_2026-06-19.md`
- MEMORY.md : ligne "AaaS Doctrine 3 Variants" (Symphony variant Nexus OMK)
- Log audit : `wiki/log.md` 2026-07-03 ligne ajoutée par ce handoff
- Migration appliquée : `iam_omk_app_level_rbac_chantier_a_2026_07_03` (via `mcp__supabase-omk__apply_migration`)

---

## Next steps (post-activation Dashboard)

1. **W4 (post-activation)** : créer un user de test via Supabase Auth, vérifier que le JWT post-login contient `org_id` + `user_role` claims.
2. **W4 (post-activation)** : tester une RLS policy `omk_saas.clients` filtrée par `(auth.jwt()->>'org_id')::uuid = org_id`.
3. **W5+** : brancher l'UI login (omk-saas-os.vercel.app) sur ce nouveau modèle RBAC.
4. **W6+** : Edge Function `seed-admin` pour industrialiser le bootstrap.