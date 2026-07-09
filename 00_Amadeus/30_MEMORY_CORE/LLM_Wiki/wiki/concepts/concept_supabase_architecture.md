---
source: LLM_Wiki_A0
date: 2026-06-10
type: concept
domain: Tech_OS / L0_Infra / Database
tags: [#concept #Supabase #RLS #MultiTenant #Caddy #Kong #JWT #VPS #Sovereign]
related:
  - ../L0/entity_solaris_os.md
  - ../hand_offs/sessions_archive/SESSION_a2debbc7_2026-06-08.md
---

# Concept: Supabase Sovereign Architecture & Multi-Tenant RLS

Ce concept documente l'architecture de déploiement souverain de Supabase sur notre VPS Hostinger (`148.230.92.235`), le reverse-proxying, et la stratégie d'isolation multi-tenant stricte par Row Level Security (RLS) basée sur des claims JWT personnalisés.

---

## 1. Topologie Réseau & Routage (Caddy ↔ Kong)

Sur le VPS, l'écosystème Supabase s'exécute via un Docker Compose orchestrant les différents conteneurs (Database, REST PostgREST, Auth GoTrue, Realtime, Kong, etc.).

L'exposition publique sécurisée se fait via un double routage :
- **Caddy (Reverse-Proxy Frontal)** : Expose l'API publiquement via HTTPS sur le domaine `supabase-api.148.230.92.235.sslip.io` et gère le certificat SSL Let's Encrypt automatique.
- **Kong (API Gateway Supabase)** : Caddy redirige le trafic HTTPS vers le port local `8000` (Kong) du VPS. Kong s'occupe ensuite d'aiguiller les requêtes vers l'Auth (`/auth/v1`), la base de données REST (`/rest/v1`), ou le Storage (`/storage/v1`).

### Extrait de configuration Caddyfile (Exposition API)
```caddy
supabase-api.148.230.92.235.sslip.io {
    reverse_proxy 127.0.0.1:8000
}
```

---

## 2. Isolation Multi-Tenant par JWT & Custom Claims

Afin d'assurer le cloisonnement strict des données entre les différentes organisations (ou coopératives dans le cas d'ABC OS) tout en évitant des jointures SQL lourdes dans chaque politique RLS, nous utilisons la stratégie des **JWT Custom Claims**.

### A. Le Custom Access Token Hook
Supabase Auth permet de brancher une fonction PostgreSQL exécutée lors de la génération du token JWT. Cette fonction récupère le `org_id` (ou `cooperative_id`) depuis notre table de profils et l'injecte directement dans les métadonnées (`app_metadata`) du token JWT.

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
  -- Récupération de l'organisation et du rôle de l'utilisateur
  select cooperative_id, role into user_org_id, user_role
  from public.profiles
  where id = (event->>'user_id')::uuid;

  claims := event->'claims';

  -- Injection des claims personnalisés dans app_metadata
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

### B. Lecture du Claim dans PostgreSQL
Pour accéder à ce claim dans les politiques de sécurité (RLS) de manière performante, nous définissons une fonction utilitaire SQL stable :

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

---

## 3. Row Level Security (RLS) Déterministe

Chaque table métier possède un cloisonnement strict. Aucun membre d'un tenant ne peut accéder aux données d'un autre tenant.

### Exemple de Politiques RLS (SaaS Tenant-Isolation)
```sql
-- Activation du RLS sur la table des projets
alter table public.build_projects enable row level security;

-- Politique de sélection
create policy "Les membres peuvent lire les projets de leur organisation"
  on public.build_projects for select
  using (cooperative_id = public.current_org_id());

-- Politique d'insertion/modification
create policy "Les leaders peuvent insérer/modifier les projets de leur organisation"
  on public.build_projects for all
  using (cooperative_id = public.current_org_id())
  with check (cooperative_id = public.current_org_id());
```

---

## 4. Workflow de Relais d'Intégration Live (Session `a2debbc7`)

Le déploiement des structures et des politiques de sécurité suit un protocole rigoureux de validation :
1. **Migrations SQL DDL locales** : Les schémas de base de données sont conçus et testés en local sous format de fichiers de migration séquentiels (`supabase/migrations/0001_init_schemas.sql`, etc.).
2. **Tunneling / Copie sur VPS** : Transfert des fichiers de migration via SCP ou via Git sur le dépôt distant.
3. **Application physique directe** : Injection des migrations dans le conteneur Postgres live du VPS via le moteur Docker :
   ```bash
   docker exec -i supabase-db psql -U postgres -d postgres -v ON_ERROR_STOP=1 < migration.sql
   ```
4. **Vérification de l'API REST PostgREST** : Exposition du nouveau schéma en mettant à jour la variable `PGRST_DB_SCHEMAS` de PostgREST et en redémarrant le conteneur REST pour recharger le schéma.
5. **Smoke Test** : Vérification des accès via curl/REST avec token anonyme et token utilisateur pour s'assurer que les codes de statut HTTP sont corrects (`200 OK` avec données filtrées, `401 Unauthorized` si non authentifié, ou `403 Forbidden` si tentative de cross-tenant).
