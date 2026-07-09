---
title: ABC OS — JWT custom_access_token_hook Cloud Migration + PGRST_DB_SCHEMAS Dashboard Action
date: 2026-06-19
status: PENDING A0 HITL
priority: P0 (bloquant queries `abc_os` live data via PostgREST)
related: [ADR-ABCOS-002 Condition B + F, ADR-SUPABASE-001 §2.2, abc/CLAUDE.md, abc-os-community/AGENTS.md §l.23]
author: Claude Code (A2) on A0 directive (post-ADR-ABCOS-002 RATIFIED 2026-06-19)
domain: L2 Business OS / ABC OS Community & Child Care BOS
---

# Handoff — ABC Cloud Migration (JWT hook + PostgREST exposure)

## TL;DR (A0)

Deux actions **P0 bloquantes** pour l'app ABC OS en production :

1. **Condition B — JWT hook Cloud migration** (SI hook ABC existait sur self-host) : `custom_access_token_hook` doit être re-provisionné sur **Supabase Cloud** (ABC-OS-COMMUNITY Org). Sans ça, queries RLS-scoped retournent 0 rows silencieusement.

2. **Condition F — PGRST_DB_SCHEMAS Dashboard action** ⚠️ **CRITIQUE** : `abc_os` schema est migré sur Cloud (17 tables + 85 rows + RLS) MAIS PostgREST n'expose PAS le schema. Queries via API retournent **404**. Cause : env var `PGRST_DB_SCHEMAS` est read-once at boot, valeur par défaut = `public,storage,graphql_public`. **Visible data dans l'app = fallback UI TypeScript, PAS du live data Supabase.**

**Action estimée** : ~3 min UI total (B = ~10 min SI hook existait, F = ~2 min).

## Contexte (D1 receipts gathered 2026-06-19)

- **App ABC state** : `abc-os-community` (Next.js 15.5.19, target dev) + `abc-childcare-portal` (mature fork, deployed). Custom domain `abc-os.kalybana.com` LIVE depuis 2026-06-14 (CNAME `cname.vercel-dns.com`).
- **Vercel projects ACTIVE** (D1 confirmed via `.vercel/project.json`) :
  - `abc-os-community` → `prj_HSw4IBR2omI5qegmEinOksr6xzo0` (team `team_d3JjRK4fJUE9ACohbdlhv9Gc`, amd-lab)
  - `abc-childcare-portal` → `prj_AN7joKC8eSwEc7adzmjzAXQdyt8C`
  - **NE PAS cleanup** ces `.vercel/` (différent de OMK-004 Condition C)
- **Migration Cloud DONE 2026-06-17** : `abc_os` schema + 17 tables + 85 rows + RLS, applied via 4/4 batches `mcp__supabase-abc__apply_migration`. Voir `wiki/log.md` 2026-06-17 entry.
- **OPEN ticket pré-existant** : `NEXT_PUBLIC_SUPABASE_URL` pointe `https://abc.kalybana.com` (NXDOMAIN, BUG depuis 13 juin). Render 14s RSC timeout. Post-pivot : doit pointer vers Cloud URL `https://<project_ref>.supabase.co`.

## Action 1 — Condition F : PGRST_DB_SCHEMAS Dashboard action (P0 BLOQUANT)

### Étape F.1 — Accéder au Dashboard

URL : https://supabase.com/dashboard/project/<abc_project_id>/settings/api

> Le project_id ABC Cloud est dans `SUPABASE_ABC_URL` env var (format `https://<project_id>.supabase.co`). Liste des MCPs ABC dans `~/.mcp.json` ligne ~96.

### Étape F.2 — Add schemas à "Exposed schemas"

1. Scroller jusqu'à section **"Exposed schemas"** (sous "API Settings")
2. Chercher le multi-select / input box
3. Add **`abc_os`** (CRITIQUE)
4. Add **`abc_child_care`** (si schema existe en Cloud, à vérifier)
5. **Save**

### Étape F.3 — Verify post-action

```bash
# Attendre 10-20 sec pour auto-reload PostgREST
curl -H "apikey: $SUPABASE_ABC_ANON_KEY" \
     "https://<abc_project_id>.supabase.co/rest/v1/organizations?select=*"
# Attendu : HTTP 200 + JSON array avec 1+ org rows
```

Si toujours 404 :
- Vérifier que schema name = exactement `abc_os` (case-sensitive)
- Vérifier que `.mcp.json` `SUPABASE_ABC_URL` pointe vers le bon project
- Forcer reload via SQL Editor : `NOTIFY pgrst, 'reload config'` (⚠️ ne change PAS `PGRST_DB_SCHEMAS` env var, mais peut aider pour cache)

## Action 2 — Condition B : JWT hook Cloud migration (si applicable)

### Étape B.0 — Vérifier si hook existait sur self-host

Avant de re-provisionner, vérifier si un `custom_access_token_hook` était actif sur self-host VPS `148.230.92.235` :

```bash
# Sur VPS (HITL via Codex/Hermes si pas encore archivé)
psql "postgresql://postgres:<password>@localhost:5432/postgres" \
  -c "SELECT proname FROM pg_proc WHERE proname = 'custom_access_token_hook';"
```

- Si retour 1+ rows : hook existait → Étape B.1-B.5 required
- Si retour 0 rows : hook jamais provisionné pour ABC → skip Étape B, juste Condition F

### Étape B.1 — Dashboard Supabase Cloud ABC

URL : https://supabase.com/dashboard/project/<abc_project_id>/auth/hooks

### Étape B.2 — Activer "Custom Access Token" hook

1. Toggle "Enable Custom Access Token Hook" → ON
2. Schema : `public`
3. Function name : `custom_access_token_hook`
4. Save

### Étape B.3 — Créer la fonction SQL

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
BEGIN
  -- Extract user_id from the event
  user_id := (event->>'user_id')::uuid;

  -- Lookup in abc_os.memberships (production)
  SELECT m.org_id INTO org_id
  FROM abc_os.memberships m
  WHERE m.user_id = user_id
  LIMIT 1;

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

> ⚠️ **Différence avec OMK** : ABC OS n'a PAS de fallback `solaris_saas` (le multi-tenancy ABC est pure single-source). Si l'app utilise un autre schema de membership, ajuster la requête SQL ci-dessus.

### Étape B.4 — Activer env var

Dans Cloud Dashboard → Settings → API → `GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true` (Save).

### Étape B.5 — Verify

```sql
SELECT
  current_setting('request.jwt.claims', true)::json->>'org_id' AS org_id,
  current_setting('request.jwt.claims', true)::json->>'sub' AS user_id;
```

Attendu : `org_id` = UUID valide pour user loggé.

## Action 3 — Fix Vercel env var (OPEN ticket pré-existant)

Dans Vercel project `abc-os-community` (et `abc-childcare-portal`) :
1. Settings → Environment Variables
2. Update `NEXT_PUBLIC_SUPABASE_URL` :
   - **DE** : `https://abc.kalybana.com` (NXDOMAIN, BUG)
   - **À** : `https://<abc_project_id>.supabase.co` (Cloud URL, post-pivot)
3. **3 scopes** : Production, Preview, Development
4. Save → trigger redeploy automatique

Script ready (per AGENTS.md l.23) : `apps/abc-os-community/scripts/apply-vercel-env.ps1` (peut nécessiter update pour pointer Cloud URL).

## D1 verification checklist (A0 ou Claude Code post-migration)

- [ ] Condition F : `curl -H "apikey: $SUPABASE_ABC_ANON_KEY" https://<abc_project_id>.supabase.co/rest/v1/organizations?select=*` → 200 + data
- [ ] Condition B (si applicable) : hook visible Dashboard Authentication → Hooks → ENABLED
- [ ] Condition B : function `public.custom_access_token_hook` existe
- [ ] Condition B : login user test → JWT contient `org_id` claim
- [ ] Condition B : RLS isolation test → user A query org B = 0 rows
- [ ] Action 3 : Vercel env var `NEXT_PUBLIC_SUPABASE_URL` pointe Cloud URL (pas `abc.kalybana.com`)
- [ ] Action 3 : render time `<2s` (vs 14s RSC timeout actuel)

## A0 HITL decision

- **Tester soi-même** : paste PAT `sbp_<new>` pour `supabase-abc` en chat (Test Key Pragma), Claude Code fait Actions 1-3 via MCP + curl, ~10 min total
- **Faire soi-même** : suivre ce handoff UI directement (~5-12 min total)
- **Différer** : marquer ce handoff `status: DEFERRED` et Condition F + B restent PENDING (⚠️ NE PAS recommander cette option : Condition F bloque live data queries)

## Cross-refs

- ADR-ABCOS-002 §Operational Runbook Étape 2 sub-steps 2.5 (Condition B) + 2.7 (Condition F)
- ADR-ABCOS-002 §Condition F (D6 #11 PostgREST exposure blocker)
- `abc/CLAUDE.md` (root, hosting pivot note)
- `abc-os-community/AGENTS.md` l.23 (OPEN TICKET NEXT_PUBLIC_SUPABASE_URL)
- `abc-childcare-portal/CLAUDE.md` (hosting pivot pointer)
- `_SPECS/REGISTRY/supabase_schemas.md` (abc_os LIVE Cloud)
- `wiki/log.md` 2026-06-17 (4/4 batches migration) + 2026-06-19 (ADR-ABCOS-002 ratification)

---

**Status** : PENDING A0 HITL. **Condition F est P0 bloquant** (visible data = fallback UI, pas live data). **Action 1 (F) = 2 min UI, à faire EN PREMIER**. **Action 2 (B) = 10 min UI conditionnel**. **Action 3 = 5 min UI** (résout aussi le ticket BROKEN pré-existant).
