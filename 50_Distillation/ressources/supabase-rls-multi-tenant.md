---
type: Backend
title: Supabase Sovereign — multi-tenant RLS par JWT custom claim
description: Architecture de déploiement souverain Supabase sur VPS Hostinger (148.230.92.235) : Caddy (reverse-proxy frontal) → Kong (API gateway) → services internes. Isolation multi-tenant stricte par RLS basée sur `org_id` injecté dans JWT via custom_access_token_hook PostgreSQL.
tags: [supabase, rls, multi-tenant, jwt-custom-claim, caddy, kong, vps, sovereignty]
generated: { by: minimax-m3, at: 2026-08-17T21:18:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:18:00Z }
sources:
  - id: concept-supabase-architecture
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_supabase_architecture.md"
    title: "Concept: Supabase Sovereign Architecture & Multi-Tenant RLS"
    last_modified: 2026-06-10
  - id: aspace-governance-dashboard
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_aspace_governance_dashboard.md"
    title: "A'Space Governance Dashboard — console unifiée d'infrastructure"
    last_modified: 2026-06-05
okf_version: "0.2"
---

# Supabase Sovereign — multi-tenant RLS par JWT custom claim

> Architecture de déploiement souverain Supabase sur VPS Hostinger (`148.230.92.235`),
> reverse-proxying via Caddy + Kong, et isolation multi-tenant stricte par Row Level
> Security (RLS) basée sur des claims JWT personnalisés.

## 1. Topologie réseau et routage (Caddy ↔ Kong)

Sur le VPS, l'écosystème Supabase tourne dans Docker Compose (Database, REST PostgREST,
Auth GoTrue, Realtime, Kong).

**Exposition publique sécurisée** par double routage :

- **Caddy** (reverse-proxy frontal) : expose l'API en HTTPS sur
  `supabase-api.148.230.92.235.sslip.io`. SSL Let's Encrypt automatique.
- **Kong** (API gateway Supabase) : Caddy redirige vers `127.0.0.1:8000` (Kong).
  Kong aiguille ensuite vers Auth (`/auth/v1`), REST (`/rest/v1`), Storage (`/storage/v1`).

```caddy
supabase-api.148.230.92.235.sslip.io {
    reverse_proxy 127.0.0.1:8000
}
```

## 2. Isolation multi-tenant par JWT custom claim

**Problème** : cloisonnement strict des données entre organisations (ou coopératives ABC)
sans jointure SQL lourde dans chaque politique RLS.

**Solution** : injecter `org_id` (et `role`) dans `app_metadata` du JWT au moment de sa
génération. La politique RLS lit le claim directement.

### A. Custom Access Token Hook (Postgres)

```sql
create or replace function public.custom_access_token_hook(event jsonb)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  claims jsonb;
  user_org_id uuid;
  user_role text;
begin
  select cooperative_id, role into user_org_id, user_role
  from public.profiles
  where id = (event->>'user_id')::uuid;

  claims := event->'claims';

  if user_org_id is not null then
    claims := jsonb_set(claims, '{app_metadata, org_id}', to_jsonb(user_org_id));
    claims := jsonb_set(claims, '{app_metadata, role}', to_jsonb(user_role));
  end if;

  event := jsonb_set(event, '{claims}', claims);
  return event;
end;
$$;

grant execute on function public.custom_access_token_hook(jsonb) to supabase_auth_admin;
```

### B. Lecture du claim dans PostgreSQL

```sql
create or replace function public.current_org_id()
returns uuid
language sql stable security definer
set search_path = public
as $$
  select nullif(
    current_setting('request.jwt.claims', true)::jsonb->'app_metadata'->>'org_id',
    ''
  )::uuid;
$$;
```

## 3. RLS déterministe

Chaque table métier possède ce cloisonnement strict :

```sql
alter table public.build_projects enable row level security;

create policy "Les membres peuvent lire les projets de leur organisation"
  on public.build_projects for select
  using (cooperative_id = public.current_org_id());

create policy "Les leaders peuvent insérer/modifier les projets de leur organisation"
  on public.build_projects for all
  using (cooperative_id = public.current_org_id())
  with check (cooperative_id = public.current_org_id());
```

## 4. Workflow de déploiement live

1. **Migrations SQL DDL locales** : fichiers séquentiels (`supabase/migrations/0001_*.sql`).
2. **Tunneling / copie sur VPS** : SCP ou Git push.
3. **Application physique directe** :
   ```bash
   docker exec -i supabase-db psql -U postgres -d postgres -v ON_ERROR_STOP=1 < migration.sql
   ```
4. **Vérification API PostgREST** : MAJ `PGRST_DB_SCHEMAS` + restart conteneur REST.
5. **Smoke test** : curl/REST avec token anonyme + token user. Vérifier codes HTTP
   (`200 OK` avec données filtrées, `401` si non auth, `403` si cross-tenant).

## 5. Pourquoi cette stack (et pas JWT standard)

- **JWT standard** ne porte que `sub` (user_id) + `aud/exp/iat`. Pas d'`org_id`.
- **Joindre `profiles` à chaque requête** ralentit et complique la gouvernance.
- **Custom claim** = `org_id` vit dans `app_metadata`, signé par Supabase Auth, lisible
  par Postgres via `request.jwt.claims`. Une seule round-trip.

## 6. Lien à la souveraineté

- Niveau 1 (Trust Zone) : VPS `148.230.92.235` dans la zone souveraine.
- Niveau 2 (Code) : migrations SQL signées via ADRs (voir ADR-INFRA-002/003).
- Niveau 3 (Mémoire) : `state.json` du bus `40_SYMPHONY_BUS` trace chaque écriture.

## Liens entrants

- `aspace-governance-dashboard.md` — la console où Supabase Health apparaîtra
- `sovereignty-3-niveaux.md` — la souveraineté tri-niveaux incarnée dans Supabase
- `ntfs-junction-aliasing.md` — le filesystem sous-jacent au VPS
