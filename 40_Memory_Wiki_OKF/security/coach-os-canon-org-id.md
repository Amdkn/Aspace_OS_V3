---
type: Security Model
title: Coach OS — un seul vocabulaire de tenant, `org_id uuid`
description: Deux systèmes d'identifiant coexistaient (slug text et uuid) ; le canon RLS l'emporte, base et code alignés le 2026-08-17.
tags: [coach-os, supabase, rls, multi-tenant, uuid]
generated: { by: claude-opus-5, at: 2026-08-17T13:40:00Z }
verified:
  - { by: process:supabase-management-api, at: 2026-08-17T13:20:00Z }
  - { by: human:amdkn, at: 2026-08-17T13:35:00Z }
sources:
  - id: mesure-colonnes
    resource: "information_schema.columns sur ndvqwcapwcnpdvknxcjw — avant/après migration"
    author: process:supabase-management-api
    last_modified: 2026-08-17
  - id: migration
    resource: supabase/migrations/2026-08-17_canon_rls_uuid.sql
    title: Migration d'unification (12 675 octets)
    last_modified: 2026-08-17
  - id: decision
    resource: "arbitrage utilisateur — « c'est le canon RLS qui gagne avec les meilleures pratiques »"
    author: human:amdkn
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : revu par un humain.** L'arbitrage est une décision
> du propriétaire du produit ; les mesures sont issues de l'API de gestion
> Supabase.

# Le problème

Deux systèmes désignaient la même notion — l'organisation à laquelle une
donnée appartient :

| Colonne | Type | Lu par |
|---|---|---|
| `memberships.tenant_id` | `text` (slug, ex. `demo-coach`) | le code |
| `audit_events.tenant_id`, `workspace_*.tenant_id` | `text` | le code |
| `cms_*.tenant_id` | `text` | **personne** |
| `cms_*.org_id` | `uuid` | les policies RLS via `jwt_org_id()` |

Les 25 tables `cms_*` portaient **les deux colonnes**. Le doublon `text`
n'était lu par aucune policy : du poids mort qui invite à l'erreur.

Le symptôme qui a révélé la divergence : `operator does not exist: uuid = text`
en posant une policy reliant `organizations.id` (uuid) à
`memberships.tenant_id` (text).

# La décision

**Le canon RLS l'emporte** : `org_id`, de type `uuid`. C'est ce que
`jwt_org_id()` et les 25 tables `cms_*` utilisaient déjà.

Un cast à l'aveugle aurait fait passer la migration et **masqué** la
divergence. On a d'abord relié par `organizations.slug` (text, donc
type-correct) en nommant le problème, puis tranché.

# Ce qui a été fait

## En base

- doublon `tenant_id text` **supprimé** des 25 tables `cms_*` ;
- `memberships`, `audit_events`, `workspace_branches`, `workspace_prs` :
  `tenant_id text` → `org_id uuid` ;
- clés étrangères vers `organizations(id)` — **sauf `audit_events`**, et
  c'est délibéré : un journal doit survivre à la suppression de
  l'organisation qu'il documente ;
- helpers `est_membre_org(uuid)` / `est_admin_org(uuid)` en `SECURITY DEFINER`
  avec `search_path` figé ;
- hook JWT réécrit sur `org_id`, trié par `invited_at` (il n'y a pas de
  `created_at` sur `memberships`).

**Mesure après** : 0 colonne `text`, 30 colonnes `org_id uuid`, 128 policies,
0 table sans policy.

## Dans le code

Deux notions portaient le même nom et le même type. Elles se séparent :

```ts
export type TenantId = string & { readonly __brand: 'TenantId' }; // partition locale
export type OrgId    = string & { readonly __brand: 'OrgId'    }; // identité en base
```

Le slug reste légitime côté navigateur — `storage-scope.ts` s'en sert pour
cloisonner `localStorage` entre comptes. Il ne doit simplement plus partir
vers Supabase.

**Un `type OrgId = string` nu n'aurait rien empêché** : les deux seraient
restés interchangeables pour le vérificateur, c'est-à-dire exactement l'erreur
qu'on répare. D'où les marques de type.

# Pourquoi le faire à ce moment précis

CUSTOMERS contenait **0 ligne et 0 compte**. La conversion `text → uuid` a
utilisé `using null::uuid` — sans perte, parce qu'il n'y avait rien à perdre.

Sur une base peuplée, il aurait fallu une correspondance slug → uuid ligne à
ligne, avec le risque d'orphelins. **La même opération devenait plus coûteuse
chaque jour.**

# Anti-pièges

- **`tsc --noEmit` ne couvre PAS `api/`.** Le projet a un `api/tsconfig.json`
  dédié. Ne pas le lancer a laissé passer trois régressions de production le
  même jour, dont une qui a coupé l'authentification. Toujours les deux.
- **Un cast qui fait passer la migration masque la divergence.** Nommer
  d'abord, trancher ensuite.
- **`extractTenantId` dans `audit/ingest.ts` n'est PAS à convertir** : il
  parse des charges entrantes d'Observers externes en dialectes variés. Ce
  n'est pas un envoi vers Supabase.
