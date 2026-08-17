---
type: Security Model
title: Une policy RLS sans son GRANT ne s'applique jamais
description: Postgres vérifie le privilège de table avant la policy. Une policy correcte sans GRANT a toutes les apparences d'une configuration valide et fait échouer le hook JWT en 500.
tags: [supabase, rls, postgres, grant, jwt, hook, coach-os, auth]
generated: { by: claude-opus-5, at: 2026-08-17T18:35:00Z }
verified:
  - { by: process:supabase-auth-logs, at: 2026-08-17T18:30:00Z }
  - { by: process:supabase-management-api, at: 2026-08-17T18:32:00Z }
sources:
  - id: journal-auth
    resource: "logs auth de ndvqwcapwcnpdvknxcjw — 24 h, entrées « Hook errored out » sur /callback et /verify"
    author: process:supabase-auth-logs
    last_modified: 2026-08-17
  - id: mesure-privileges
    resource: "has_table_privilege / has_function_privilege sur supabase_auth_admin, avant et après GRANT"
    author: process:supabase-management-api
    last_modified: 2026-08-17
  - id: correctif
    resource: coach-os/supabase/migrations/2026-08-17_hook_jwt_grant_memberships.sql
    title: La migration du GRANT
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Le journal d'authentification
> nomme l'erreur, et les privilèges ont été mesurés avant et après.

# La règle

**Postgres vérifie le privilège de table AVANT d'évaluer la policy RLS.**

Sans `GRANT SELECT`, la policy n'est jamais atteinte. La lecture échoue en
`permission denied (SQLSTATE 42501)` — pas en « zéro ligne ».

C'est le piège : une policy correcte, visible dans `pg_policies`, avec le bon
rôle et le bon `USING`, **donne toutes les apparences d'une configuration
valide**. Rien dans l'interface ne signale que le GRANT manque.

| Ce qu'on voit | Ce qui compte |
|---|---|
| `pg_policies` → policy présente, `roles = {supabase_auth_admin}`, `qual = true` | `has_table_privilege('supabase_auth_admin', 'public.memberships', 'SELECT')` |

Le premier était vrai. Le second valait **false**.

# Le symptôme observé

Toute authentification de Coach OS échouait, Google comme courriel :

```
500: Error running hook URI: pg-functions://postgres/public/custom_access_token_hook
ERROR: permission denied for table memberships (SQLSTATE 42501)
```

Le hook `custom_access_token_hook` s'exécute sous le rôle
`supabase_auth_admin`. Il lit `memberships` pour poser le claim `org_id`.

# La cascade, plus vicieuse que l'échec

**L'erreur du hook fait échouer la transaction de GoTrue.** Tout ce que la
requête avait déjà fait est donc annulé :

- une inscription Google créait l'utilisateur… puis l'annulait. Le journal
  montrait plusieurs `user_signedup` réussis quand `auth.users` ne contenait
  qu'un seul compte ;
- un clic sur le lien de confirmation renvoyait un `303` et marquait l'adresse
  confirmée… puis l'annulait. `email_confirmed_at` restait `null`, et la
  connexion suivante répondait « Email not confirmed ».

D'où l'impression, pour l'utilisateur, que **le lien reçu par courriel ne
servait à rien**. Il fonctionnait parfaitement ; c'est la suite qui défaisait
son effet.

Effet de bord utile : le jeton de confirmation survit lui aussi à l'annulation.
Après correction, le lien déjà reçu reste valide — inutile d'en redemander un.

# Le correctif

```sql
grant usage  on schema public        to supabase_auth_admin;
grant select on table public.memberships to supabase_auth_admin;

revoke execute on function public.custom_access_token_hook(jsonb) from authenticated, anon, public;
grant  execute on function public.custom_access_token_hook(jsonb) to   supabase_auth_admin;
```

Le `revoke` n'est pas cosmétique : un hook appelable par un rôle client est une
surface d'attaque, puisqu'il lit une table d'adhésions.

# Le geste de diagnostic

Quand une lecture échoue sous RLS, **mesurer le privilège avant de suspecter la
policy** :

```sql
select has_table_privilege('<role>', '<schema>.<table>', 'SELECT') as grant_ok,
       (select count(*) from pg_policies
         where schemaname='<schema>' and tablename='<table>'
           and '<role>' = any(roles))                              as policies;
```

`grant_ok = false` avec `policies >= 1` est la signature exacte de ce défaut.

Et **distinguer les deux échecs** : `permission denied` est un refus de
privilège ; zéro ligne sans erreur est un refus de policy. Ils ne se corrigent
pas au même endroit.

# Anti-piège de lecture du journal

Le journal `auth` de Supabase rend l'erreur en clair — c'est la source qui
tranche. Le navigateur, lui, n'affichait qu'un `error=server_error` tronqué
dans l'URL, et l'application une carte « la session n'a pas pu être récupérée
dans le temps imparti », qui décrit un *délai* et oriente vers une fausse
piste.

**Quand l'app parle de timeout et que le serveur parle de permission, c'est le
serveur qui a raison.**
