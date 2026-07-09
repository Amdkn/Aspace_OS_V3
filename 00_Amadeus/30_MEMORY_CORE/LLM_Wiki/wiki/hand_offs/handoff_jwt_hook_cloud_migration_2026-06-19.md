---
title: JWT custom_access_token_hook Cloud Migration — OMK SaaS Production
date: 2026-06-19
status: PENDING A0 HITL
priority: P0 (bloquant Phase C auth SaaS)
related: [ADR-OMK-004 Condition B, ADR-SUPABASE-001 §2.2, omk/apps/dashboard/AGENTS.md §2b]
author: Claude Code (A2) on A0 directive (post-ADR-OMK-004 RATIFIED)
domain: L2 Business OS / OMK Services / Auth SaaS
---

# Handoff — JWT custom_access_token_hook Cloud Migration

## TL;DR (A0)

Le `custom_access_token_hook` provisionné sur **self-hosted Supabase** (`148.230.92.235`) doit être **re-provisionné sur Supabase Cloud** (OMK Services Org). **Sans ça, Phase C SaaS auth est cassée silencieusement** (RLS `org_id` claim = null → 0 rows sur toutes les queries RLS-scoped). **Action estimée : ~10 min UI** (Dashboard Supabase OMK → Authentication → Hooks).

## Contexte (D1 receipts gathered)

- **Hook self-host existant** : `omk_saas.memberships` first → `solaris_saas` fallback, `SECURITY DEFINER`, `GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true` (per AGENTS.md §2b + ADR-SUPABASE-001 §2.2). Activated 2026-06-14.
- **Post-pivot ADR-OMK-004 RATIFIED 2026-06-19** : Supabase Cloud OMK Services Org est désormais l'instance prod. Le hook self-host reste actif sur VPS mais ne sert plus l'app prod (Dokploy killed, seule l'app Vercel `omk-saas-os` est live).
- **Test Key Pragma** : si A0 veut que je teste le hook Cloud, paste le PAT `sbp_<new>` pour `supabase-omk` en chat et je peux faire le D1 verify post-migration via curl/CLI.

## Étapes UI (A0 HITL)

### Étape 1 — Dashboard Supabase Cloud OMK

URL : https://supabase.com/dashboard/project/<project_id_omk_cloud>/auth/hooks

> Le project_id OMK Cloud est dans `SUPABASE_OMK_URL` env var (format `https://<project_id>.supabase.co`). Liste des MCPs OMK dans `~/.mcp.json` ligne ~96.

### Étape 2 — Activer "Custom Access Token" hook

1. Toggle "Enable Custom Access Token Hook" → ON
2. Schema : `public`
3. Function name : `custom_access_token_hook`
4. Save

### Étape 3 — Créer la fonction SQL

Dans SQL Editor (Dashboard → SQL → New query) :

```sql
CREATE OR REPLACE FUNCTION public.custom_access_token_hook(event jsonb)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path = ''
AS $$
DECLARE
  claims jsonb;
  user_id uuid;
  org_id uuid;
  fallback_org_id uuid;
BEGIN
  -- Extract user_id from the event
  user_id := (event->>'user_id')::uuid;

  -- Priority 1: look up in omk_saas.memberships (production schema)
  SELECT m.org_id INTO org_id
  FROM omk_saas.memberships m
  WHERE m.user_id = user_id
  LIMIT 1;

  -- Priority 2: fallback to solaris_saas.memberships (legacy)
  IF org_id IS NULL THEN
    SELECT m.org_id INTO org_id
    FROM solaris_saas.memberships m
    WHERE m.user_id = user_id
    LIMIT 1;
  END IF;

  -- Inject org_id into JWT claims
  claims := event->'claims';
  IF org_id IS NOT NULL THEN
    claims := jsonb_set(claims, '{org_id}', to_jsonb(org_id::text));
  END IF;

  -- Return modified event
  RETURN jsonb_set(event, '{claims}', claims);
END;
$$;

-- Grant execute to supabase_auth_admin
GRANT EXECUTE ON FUNCTION public.custom_access_token_hook TO supabase_auth_admin;

-- Revoke from public/authenticated/anon (security)
REVOKE EXECUTE ON FUNCTION public.custom_access_token_hook FROM PUBLIC;
REVOKE EXECUTE ON FUNCTION public.custom_access_token_hook FROM anon, authenticated;
```

> **Note** : la même fonction SQL peut être portée self-host → Cloud telle quelle. Le code est identique, seul le schéma `omk_saas` doit déjà exister sur Cloud (Phase B ADR-OMK-004, déjà OK si tables provisionnées).

### Étape 4 — Test post-migration

1. Login un user OMK SaaS test (créer via SignupView)
2. Dans SQL Editor, query :

```sql
SELECT
  current_setting('request.jwt.claims', true)::json->>'org_id' AS org_id,
  current_setting('request.jwt.claims', true)::json->>'sub' AS user_id;
```

3. D1 receipt attendu : `org_id` = UUID valide, `user_id` = UUID du user loggé
4. Si `org_id` = null : hook pas actif ou memberships vide → debug

### Étape 5 — Application env (automatique)

L'app Vercel `omk-saas-os` n'a pas besoin de changement — le hook Cloud est sur le serveur Supabase, transparent pour le client. Le client continue à envoyer le JWT dans les headers Authorization, le hook ajoute `org_id` au moment du `signIn`.

> ⚠️ **Caveat** : les users self-host `omk-admin@kalybana.com` (premier user provisionné 2026-06-14) doivent être **migrés vers Cloud** (création manuelle dans Auth + insertion dans `omk_saas.memberships`). Sinon la première prod login échoue.

## D1 verification checklist (A0 ou Claude Code post-migration)

- [ ] Cloud project OMK URL accessible : `curl -I $SUPABASE_OMK_URL/auth/v1/health` → 200
- [ ] Hook visible dans Dashboard : Authentication → Hooks → "Custom Access Token" = ENABLED
- [ ] Function `public.custom_access_token_hook` existe : SQL Editor → `\df public.custom_access_token_hook` → listée
- [ ] Memberships table seedée : `SELECT count(*) FROM omk_saas.memberships` → ≥1
- [ ] Login user test : JWT contient `org_id` claim
- [ ] RLS isolation test : user org A query `SELECT * FROM omk_saas.clients WHERE org_id != '<org_a>'` → 0 rows

## A0 HITL decision

- **Tester soi-même** : coller le PAT `sbp_<new>` pour `supabase-omk` en chat (Test Key Pragma), Claude Code fait Étapes 1-4 via MCP + curl, ~10 min
- **Faire soi-même** : suivre ce handoff UI directement
- **Différer** : marquer ce handoff `status: DEFERRED` et l'ADR-OMK-004 reste RATIFIED avec Condition B en PENDING (acceptable car Condition B est HITL post-ratification per runbook Étape 2.5)

## Cross-refs

- ADR-OMK-004 §Operational Runbook Étape 2 sub-step 2.5 (création de ce handoff)
- ADR-OMK-004 §Condition B (D1 receipts AGENTS.md §2b)
- ADR-SUPABASE-001 §2.2 (SQL DDL original)
- `omk/apps/dashboard/AGENTS.md` §1 row 2b (status PENDING re-provisioning)
- `omk/apps/dashboard/REBUILD_WORKFLOW.md` §2.2 + §5 (hook row updated post-pivot)
- `omk/CLAUDE.md` gotcha #4 (Cloud hook mention)
- `wiki/log.md` 2026-06-19 (ratification entry)
- `_TRASH_2026-06-19_pre_pivot_vercel/dashboard_dot_vercel/` (pivot cleanup)

---

**Status** : PENDING A0 HITL. Si A0 choisit de tester soi-même : ~10 min. Si A0 veut que je fasse : paste PAT `sbp_<new>` pour `supabase-omk` en chat (Test Key Pragma).
