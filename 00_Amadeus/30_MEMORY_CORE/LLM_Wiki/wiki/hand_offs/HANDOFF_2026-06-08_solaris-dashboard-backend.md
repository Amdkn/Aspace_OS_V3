---
source: handoff
date: 2026-06-08
type: handoff
domain: L2 Business OS / Solaris (AaaS) / Backend
tags: [#handoff #solaris #supabase #multi-tenant #nextjs #cli #minimax #frugal]
from: Claude Code (A2, Desktop)
to: Claude Code CLI (MiniMax-M3, frugal)
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-META-001]
---

# HANDOFF — Solaris Dashboard : stratégie backend Supabase multi-tenant

> **Pour** : Claude Code CLI (MiniMax-M3, mode frugal).
> **Mission** : appliquer au dashboard **Solaris** la MÊME stratégie backend que celle conçue pour OMK (Supabase self-hosted, schéma + RLS multi-tenant), **adaptée à Next.js**.
> **Cette fiche est auto-suffisante** : la session CLI démarre à froid, tout le contexte nécessaire est ici.

## 0. Doctrine obligatoire (lire avant d'agir)
- **ADR-META-001** (`_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`) : Verify-Before-Assert. AUCUNE affirmation factuelle sans preuve dans le tour (lire fichier / lancer commande). D1-D8.
- **ADR-SUPABASE-001** (ACCEPTED) : multi-tenancy par schéma Postgres ; dual MCP `supabase-solaris` (read) / `supabase-aspace` (write) ; rôles `aspace_admin`/`aspace_observer`.
- **ADR-OMK-001** (ACCEPTED) : pattern dual-product (interne + SaaS), single-schema + org_id + RLS. Solaris suit le même pattern.
- **Frugal MiniMax** : minimiser les tokens. Lire seulement les fichiers nécessaires (liste §2). Pas de re-exploration globale. Réutiliser le code de référence OMK (§4) comme template.

## 1. État vérifié de Solaris (2026-06-08, déjà constaté par A2 Desktop)
Chemin : `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\solaris\apps\dashboard`

| Dimension | État réel |
|---|---|
| Stack | **Next.js 16.2.6** + React 19.2 + Tailwind v4 (PAS Vite — différence clé avec OMK) |
| Nom / repo | `aaas-os` / `github.com/Amdkn/00-AaaS-Agency-Garden` |
| Routing | **Next App Router** (`src/app/`) — déjà URL-based, pas de dette routing |
| Modularisation | ✅ faite : 12 views (`src/components/views/`: Clients, Dashboard, Finance, Growth, ItData, Legal, Marketplace, People, Sales, Settings, SopLibrary, Tasks), `lib/types.ts`, `lib/constants.ts` |
| Backend / persistance | ❌ 100% mock (`lib/constants.ts`), AUCUN `@supabase/supabase-js` |
| Auth / tenant | ❌ aucun |
| Audit existant | `picard_audit.md` (2026-05-25) — vérifier sa fraîcheur avant de t'y fier (celui d'OMK était périmé) |

> Solaris = "AaaS Agency Garden" → c'est par nature un produit **multi-tenant** (agence-as-a-service pour des clients). Le mode `saas` est probablement le mode principal ici, contrairement à OMK où l'interne prime.

## 2. Fichiers à lire (et SEULEMENT ceux-là, frugalité)
1. `solaris/apps/dashboard/package.json`
2. `solaris/apps/dashboard/src/lib/types.ts` + `src/lib/constants.ts`
3. `solaris/apps/dashboard/src/app/layout.tsx` + `src/app/page.tsx` (comprendre le shell + comment les views sont montées)
4. 1-2 views (`src/components/views/Clients.tsx`, `Dashboard.tsx`) pour le pattern data
5. `solaris/apps/dashboard/picard_audit.md` (contexte, à valider)
6. Le code de référence OMK (§4) — c'est ton template.

## 3. Différence FRAMEWORK critique (D3 — ne PAS copier OMK littéralement)
OMK est **Vite + Express + server.js + Dockerfile**. Solaris est **Next.js** → l'approche backend change :
- **Pas de server.js/Express** : Next a son propre serveur (`next start`) et ses **Route Handlers** (`src/app/api/.../route.ts`).
- **Client Supabase** : utiliser **`@supabase/ssr`** (pas seulement `@supabase/supabase-js`) pour gérer les cookies/session côté serveur Next (Server Components + middleware).
- **Tenant resolution** : via **`middleware.ts`** Next (lit le JWT/cookie → injecte `org_id`), pas via un flag client seul.
- **Env** : `NEXT_PUBLIC_SUPABASE_URL` / `NEXT_PUBLIC_SUPABASE_ANON_KEY` (préfixe `NEXT_PUBLIC_`, pas `VITE_`). `SERVICE_ROLE_KEY` server-only (sans préfixe public).
- **Déploiement Dokploy** : image Next standalone (`output: 'standalone'` dans `next.config.ts`), pas le pattern Express d'OMK.

## 4. Code de référence OMK (template à adapter)
A2 Desktop a déjà fait la Phase A d'OMK (GREEN, tsc OK). Lis ces fichiers comme modèle conceptuel :
- `omk/apps/dashboard/src/config/mode.ts` (résolution mode internal/saas)
- `omk/apps/dashboard/src/lib/supabase.ts` (client schema-aware)
- `omk/apps/dashboard/.env.example`
- `omk/apps/dashboard/REBUILD_WORKFLOW.md` (les 8 phases A→H, SQL schémas + RLS)

Adapte : `VITE_*`→`NEXT_PUBLIC_*`, `import.meta.env`→`process.env`, client → `@supabase/ssr` createServerClient/createBrowserClient.

## 5. Schémas Supabase pour Solaris (via MCP `supabase-aspace`)
- Créer `solaris_internal` (ops internes agence) + `solaris_saas` (clients multi-tenant).
- `solaris_saas` : tables avec `org_id` + RLS `org_id = (auth.jwt() ->> 'org_id')::uuid`, tables `organizations` + `memberships` (cf. REBUILD_WORKFLOW.md §2.2 d'OMK, identique).
- Étape HITL : ajouter `solaris_internal,solaris_saas` à `PGRST_DB_SCHEMAS` + restart `supabase-core` (VPS).

## 6. Livrables attendus du CLI
1. `ADR` ou section : décision archi Solaris (réutiliser ADR-OMK-001, juste noter les specifics Next.js).
2. `REBUILD_WORKFLOW.md` dans `solaris/apps/dashboard/` (calqué sur OMK, adapté Next.js).
3. Phase A locale Solaris : `@supabase/ssr` installé, client browser+server, `middleware.ts` tenant stub, `.env.example` (NEXT_PUBLIC_*), `next.config.ts` standalone. `npm run lint` (eslint) + `npx tsc --noEmit` GREEN.
4. Rapport court : ce qui est fait, ce qui reste (schémas VPS, auth, déploiement) = bloqué sur canal bypass.

## 7. Garde-fous
- VPS / Dokploy / migrations prod = **canal bypass uniquement** (CLI `--dangerously-skip-permissions` ou extension Antigravity). Le Desktop ne peut pas (cf. session 2026-06-08).
- `SERVICE_ROLE_KEY` jamais côté client. Jamais de secret en .md/.json/git (Test Key Pragma).
- Born-short (ADR-INFRA-002) : repo build-bearing reste court ; vérifier MAX_PATH Windows.
- Tester l'isolation tenant (org A ≠ org B) avant tout trafic réel.

## 8. Commande de démarrage suggérée (CLI frugal)
```
claude --dangerously-skip-permissions
> Lis HANDOFF_2026-06-08_solaris-dashboard-backend.md puis ADR-SUPABASE-001 + ADR-OMK-001.
> Applique la stratégie backend à solaris/apps/dashboard en Next.js-native. Phase A locale d'abord, tsc/eslint GREEN, rapport.
```
