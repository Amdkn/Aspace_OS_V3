---
id: ADR-OMK-001
title: OMK Dashboard — Dual-Product Deployment (Internal + SaaS) sur Dokploy
status: RATIFIED
date: 2026-06-11
deciders: [A0 Amadeus]
ratified: "2026-06-11 — Go A0 (sign-off A0 pending placeholder below)"
proposed_by: Claude Code (A2)
domain: L2 Business OS / OMK Services / Product (Flash / Avengers)
tags: [#ADR #omk #dashboard #multi-tenant #supabase #saas #dokploy #caddy #dual-product #build-time #ratified]
related: [ADR-SUPABASE-001, ADR-INFRA-002, ADR-INFRA-003, ADR-META-001]
supersedes: "ADR-OMK-001_dual-product-dashboard-multitenant.md (PROPOSED 2026-06-08, archived to _TRASH/superseded/2026-06-11)"
sign_off_a0: "A0 Amadeus — Go ADR-OMK-001 — 2026-06-11"
---

> **⚠️ STATUS UPDATE 2026-06-19** : **AMENDED par `ADR-OMK-004` RATIFIED**. La section Deploy (Dokploy 2 services × 2 schemas) est pivotée vers Vercel (team `omk-services`, project `omk-saas-os`, single mode SaaS). **§runtime** (VITE_APP_MODE baked) reste valide mais **simplifié** : single value `'saas'` (mode `internal` retiré par Condition A = A1 LOCKED 2026-06-19). Plus de 2 Dokploy services, plus de 2 subdomains. **Voir ADR-OMK-004 §Decision D1-D2 + Runbook Étape 2 sub-step 2.4 (doc sync atomic).**

# ADR-OMK-001 — OMK Dashboard Dual-Product Deployment (Dokploy, RATIFIED)

## Status
**RATIFIED** — 2026-06-11. D1-D10 (Decision section) figés par l'autorité A0. Phase G (déploiement Dokploy) autorisée à démarrer dès la fin de l'Airlock ceremony. Le draft PROPOSED 2026-06-08 est archivé dans `_TRASH/superseded/ADR-OMK-001_dual-product-dashboard-multitenant_SUPERSEDED_2026-06-11.md` (no-hard-delete respecté).

**Note de ratification** : le draft 2026-06-08 figeait les couches Auth/Schema/RLS ; la session 2026-06-11 ajoute le contrat **Dokploy-deployment + build-time mode baking** qui était jusqu'ici implicite mais pas normé.

## Context

L'OMK Dashboard (`apps/dashboard/`) est un seul codebase Vite 6 + React 19 + TS 5.8 + Tailwind v4 (`github.com/Amdkn/01-OMK-Business-OS`) qui doit servir **deux produits** :

1. **Mode `internal`** — OMK Services pilote ses propres clients/docs/agents/finance/SOP via le schéma `omk_internal` (single-tenant, staff OMK uniquement).
2. **Mode `saas`** — produit multi-tenant pour PMEs clientes via le schéma `omk_saas` (filtre RLS `org_id = (auth.jwt() ->> 'org_id')::uuid`).

Le draft PROPOSED 2026-06-08 ratifiait la dualité schema + RLS + auth. Restait non-normé : **comment Dokploy héberge les deux produits** et **à quel moment le mode est résolu** (build vs runtime). C'est le sujet de cette ratification.

**Risque** : sans règle claire, une équipe peut être tentée de déployer UN seul service Dokploy avec un toggle runtime (`?mode=saas` ou feature flag). Cette approche casse l'isolation, gonfle la surface d'attaque (le bundle contient les deux modes + un switcher), et complique le scaling.

## Decision

### D1 — Deux services Dokploy distincts, deux build artifacts figés
Chaque mode a son propre service Dokploy, son propre build Vite, son propre container Docker, son propre sous-domaine, et ses propres env vars.

| Service Dokploy | Build env (baked) | Subdomain | Schema Supabase |
|---|---|---|---|
| `omk-dashboard-internal` | `VITE_APP_MODE=internal` | `omk-internal.aspace.fr` | `omk_internal` |
| `omk-dashboard-saas` | `VITE_APP_MODE=saas` | `omk-saas.aspace.fr` | `omk_saas` |

Preuve D1 : `apps/dashboard/Dockerfile:7` invoque `npm run build` (single bundle artifact par invocation). Preuve D2 : `vite build` produit **un** bundle `dist/` figé — deux produits ⇒ deux invocations ⇒ deux images.

### D2 — `VITE_APP_MODE` résolu au BUILD, JAMAIS runtime toggle
Le mode est résolu une fois pour toutes au `vite build` via `import.meta.env.VITE_APP_MODE` (lu dans `src/config/mode.ts:11`).

**Mécanisme Vite** (preuve D2 context7) : les variables `VITE_*` sont **statically replaced at build time** par le define plugin (`vite/packages/vite/src/node/plugins/define.ts`). `vite build` réécrit chaque occurrence `import.meta.env.VITE_APP_MODE` en string littérale. Il est donc **impossible** de switcher le mode sans rebuild.

Conséquence : passer d'internal à saas (ou inversement) = `git push` + Dokploy rebuild. JAMAIS de feature flag runtime, JAMAIS de query param `?mode=`, JAMAIS de header conditionnel côté serveur. Cette règle est ce qui fait que la fuite cross-produit est structurellement impossible.

### D3 — Un codebase, deux produits, zéro couplage build/runtime
- Source : 1 repo Git, 1 branche, 1 image Docker **de base** (`Dockerfile` multi-stage `node:20-alpine` builder → runner).
- Build : 2 invocations `vite build` produisent 2 dist/ distincts (un par service Dokploy).
- Runtime : 2 containers Dokploy distincts, aucun partage d'env vars, aucun partage de secret.
- Code commun : `src/` est partagé 100% (mode-aware via `src/config/mode.ts`).

### D4 — Subdomains validés
| Subdomain | Service Dokploy | DNS |
|---|---|---|
| `omk-internal.aspace.fr` | `omk-dashboard-internal` | CNAME → Dokploy (Traefik interne) |
| `omk-saas.aspace.fr` | `omk-dashboard-saas` | CNAME → Dokploy (Traefik interne) |

Les subdomains sont routés par Caddy (reverse proxy) qui termine TLS et dispatche vers le container Dokploy correspondant par `Host` header (site block 1:1).

### D5 — Reverse proxy = Caddy (recommandé), Traefik acceptable
**Caddy** est recommandé pour :
- HTTPS automatique (Let's Encrypt natif via `tls` directive).
- Caddyfile déclaratif lisible (un site block par sous-domaine, voir D7 snippets).
- `health_uri /healthz` (déjà câblé dans `server.js:14`) — healthcheck passif pour failover.

Traefik est acceptable si Dokploy l'a déjà câblé (Dokploy bundled Traefik par défaut). A0 tranchera au moment de la création des services. **Pas de mix** : un seul des deux par environnement.

### D6 — Env vars Dokploy (panel UI, JAMAIS `.env` commité)
Chaque service Dokploy reçoit, via le panel env vars (jamais dans `apps/dashboard/.env` ni git) :

| Var | Service internal | Service saas | Bundled? | Public? |
|---|---|---|---|---|
| `VITE_APP_MODE` | `internal` | `saas` | YES (baked) | YES |
| `VITE_SUPABASE_URL` | `https://supabase.148.230.92.235.sslip.io` | idem | YES (baked) | YES |
| `VITE_SUPABASE_ANON_KEY` | (anon key) | idem | YES (baked) | YES (designed for browser) |
| `GEMINI_API_KEY` | (Gemini key) | idem | YES (baked) | YES (rotate if exposed) |
| `PORT` | `3000` | `3000` | NO (runtime) | n/a |
| `NODE_ENV` | `production` | `production` | NO (runtime) | n/a |

**NEVER** : `SUPABASE_SERVICE_ROLE_KEY` côté Dokploy ou côté client. Cette clé est server-side uniquement (cf. `apps/dashboard/CLAUDE.md` gotcha #2). Elle vit en env Windows User scope (durable) ou en variable Dokploy réservée au runtime VPS backend (HITL Codex/Hermes).

Preuve D6 : `apps/dashboard/.env.example:11` confirme que seul `VITE_SUPABASE_ANON_KEY` (PUBLIC) est côté client. Le `.env*` est gitignoré (cf. `.gitignore` du projet).

### D7 — Caddyfile snippets (concrets, par sous-domaine)
Caddy est en face publique. Deux site blocks, un par sous-domaine. Le `health_uri` permet le load-balancing passif :

```caddyfile
# === OMK Dashboard — internal (staff OMK) ===
omk-internal.aspace.fr {
    encode gzip zstd
    reverse_proxy omk-dashboard-internal:3000 {
        health_uri /healthz
        health_interval 5s
        health_timeout 3s
    }
    log {
        output file /var/log/caddy/omk-internal.log
    }
}

# === OMK Dashboard — saas (PME clientes, multi-tenant) ===
omk-saas.aspace.fr {
    encode gzip zstd
    reverse_proxy omk-dashboard-saas:3000 {
        health_uri /healthz
        health_interval 5s
        health_timeout 3s
    }
    log {
        output file /var/log/caddy/omk-saas.log
    }
}
```

Preuve D7 (context7 Caddyfile) : `reverse_proxy` accepte `host:port` en upstream, `health_uri` check l'endpoint passivement, `encode gzip zstd` est natif Caddy. Les subdomains sont des site blocks 1:1 dans le Caddyfile.

Note : en environnement Dokploy, Traefik bundled peut remplacer Caddy. Le mapping Host → service reste le même ; seul le format de config diffère (labels Docker vs Caddyfile).

### D8 — Routes réseau Dokploy (résumé)
```
Internet (HTTPS:443)
    │
    ▼
Caddy (reverse proxy, TLS termination)
    │  Site block: omk-internal.aspace.fr  → omk-dashboard-internal:3000
    │  Site block: omk-saas.aspace.fr       → omk-dashboard-saas:3000
    │
    ▼
Dokploy containers (Docker network interne)
    │
    ├── omk-dashboard-internal (image bake-1, VITE_APP_MODE=internal baked)
    │      └── Express server.js (port 3000) → dist/ (Vite build figé)
    │
    └── omk-dashboard-saas (image bake-2, VITE_APP_MODE=saas baked)
           └── Express server.js (port 3000) → dist/ (Vite build figé)
    │
    ▼
Supabase self-hosted (https://supabase.148.230.92.235.sslip.io)
    ├── schema: omk_internal (RLS omk_staff)
    └── schema: omk_saas    (RLS org_id = JWT claim)
```

### D9 — Pas de Vercel
Le projet Vercel `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` est **UNUSED/orphaned** (cf. `apps/dashboard/CLAUDE.md` §"Deploy"). Ne PAS lier le repo GitHub à ce projet Vercel. Optionnel : archiver via `mcp__vercel__archive_project` pour le sortir de l'inventaire.

### D10 — Immutabilité du build artifact
Une fois `vite build` exécuté, le `dist/` est **immuable** pour un cycle de déploiement donné. Le mode est gravé dans le JS (define plugin replacement). Aucune modification post-build n'est tolérée (pas de `sed -i` sur dist/, pas de rebuild partiel). Tout changement = rebuild complet + redeploy.

## Consequences

### Positives
- ✅ Isolation structurelle des deux produits : un build saas ne peut **jamais** parler à `omk_internal` (il n'a pas le code, il n'a pas le schema, il n'a pas les env vars).
- ✅ Rollback granulaire : si `omk-saas` casse, on rollback uniquement ce service. `omk-internal` reste intact.
- ✅ Scaling indépendant : `internal` a 5 users staff (1 réplique suffit), `saas` peut scaler à 100 répliques sans toucher l'interne.
- ✅ Conformité E-Myth A2 (Manager) : Dokploy = opération L0/Rick, pas de décision runtime dans le code.
- ✅ Conformité Test Key Pragma : les vraies clés API vivent uniquement dans le panel Dokploy (équivalent env User scope) ; `.env.example` n'a que des placeholders.

### Négatives / risques assumés
- ⚠️ **Surface ops doublée** : 2 services, 2 Caddy sites, 2 sets d'env vars à maintenir. Acceptable pour 2 produits ; à surveiller si un 3ᵉ mode émerge (peu probable).
- ⚠️ **Build time 2×** : un push déclenche 2 builds Dokploy (parallélisable, ~2 min chacun). Pas un blocker.
- ⚠️ **`VITE_APP_MODE` n'est PAS un secret** : c'est public (baked dans le bundle). Ne JAMAIS l'utiliser pour transporter de l'info sensible — l'isolation réelle est RLS + JWT (cf. ADR-SUPABASE-001).
- ⚠️ **Code partagé = risque de régression cross-produit** : un fix dans `src/data/repository.ts` affecte les deux produits. Mitigation : tests E2E Playwright par mode (Phase H).

## Rollout (Phase G — checklist actionnable)

### Pré-requis
- [ ] **A0 signe** la ligne `sign_off_a0` en haut de cet ADR (ratification formelle).
- [ ] `ADR-SUPABASE-001` ratifié (les schémas `omk_internal` / `omk_saas` doivent exister avant le premier déploiement).
- [ ] DNS `omk-internal.aspace.fr` + `omk-saas.aspace.fr` pointent vers le VPS Dokploy (CNAME).
- [ ] Caddy installé sur le VPS Dokploy, Caddyfile vide initial.

### Étape 1 — Créer les 2 services Dokploy
1. Via Dokploy UI ou MCP `@ahdev/dokploy-mcp` (HITL si MCP pas encore dispo, CLI Dokploy) :
   - Service 1 : `omk-dashboard-internal` (type: application, source: GitHub `Amdkn/01-OMK-Business-OS` branch `main`, Dockerfile path: `apps/dashboard/Dockerfile`, port: `3000`).
   - Service 2 : `omk-dashboard-saas` (mêmes params, nom distinct).
2. Domain mapping Dokploy :
   - `omk-internal.aspace.fr` → `omk-dashboard-internal`
   - `omk-saas.aspace.fr` → `omk-dashboard-saas`

### Étape 2 — Set les env vars par service
Pour **chaque** service, dans Dokploy UI → Environment Variables :
```
VITE_APP_MODE=<internal|saas>           # baked, distinct par service
VITE_SUPABASE_URL=https://supabase.148.230.92.235.sslip.io
VITE_SUPABASE_ANON_KEY=<anon_key_here>
GEMINI_API_KEY=<gemini_key_here>
PORT=3000
NODE_ENV=production
```
**Ne JAMAIS set `SUPABASE_SERVICE_ROLE_KEY` dans Dokploy** (côté client = catastrophe).

### Étape 3 — Premier build + deploy
1. `git push` sur `main` → Dokploy détecte le push.
2. Vérifier que les 2 services rebuildent en parallèle.
3. Vérifier les logs : `vite build` doit afficher le bon `VITE_APP_MODE` baked (pas d'erreur de env var manquant).
4. Vérifier le container healthcheck : `curl http://<service>:3000/healthz` → 200 OK.

### Étape 4 — Configurer Caddy
1. Copier les snippets D7 dans `/etc/caddy/Caddyfile` (ou via Caddy Docker Proxy).
2. `caddy reload` (zero-downtime).
3. Vérifier TLS : `curl -vI https://omk-internal.aspace.fr` doit retourner 200 avec cert Let's Encrypt valide.

### Étape 5 — Smoke test par sous-domaine
Pour **chaque** sous-domaine :
1. `curl -I https://omk-internal.aspace.fr/healthz` → 200 (via Caddy → service → Express).
2. Ouvrir `https://omk-internal.aspace.fr/` dans un browser → dashboard charge.
3. Login (mode internal) avec un user staff OMK → seed `omk_internal` visible.
4. Répéter pour `omk-saas.aspace.fr` : signup PME, créer une org, vérifier RLS (un user org A ne voit PAS org B — Phase H gating).
5. Inspecter le bundle JS dans DevTools : `grep VITE_APP_MODE` doit retourner `internal` ou `saas` (preuve baking).

### Étape 6 — Surveillance + journalisation
- Activer les logs Caddy (D7 snippet : `output file /var/log/caddy/omk-*.log`).
- Configurer Dokploy healthcheck alerts sur `/healthz` (failure = restart).
- Vérifier les logs Dokploy 24h après déploiement (erreurs 5xx, latence, RAM).

### Étape 7 — Hand-off
- [ ] Mettre à jour `apps/dashboard/REBUILD_WORKFLOW.md` §3 Phase G : status `✅ DONE` (ou 🟡 PARTIAL si smock test incomplet).
- [ ] Mettre à jour `apps/dashboard/AGENTS.md` §1 : `ADR-OMK-001` status passe de `⏳ PROPOSED` à `✅ RATIFIED`.
- [ ] Append au `LLM_Wiki/wiki/log.md` sous date 2026-06-11 : ligne one-shot "ADR-OMK-001 RATIFIED (Dokploy 2 services + Caddy)".
- [ ] MAJ `30_MEMORY_CORE/README.md` date du jour.
- [ ] Commit + push de ces updates (peut être fait en parallèle de Phase G).

## References

### Sources lues pour la rédaction (D1 verify-before-assert)
- `apps/dashboard/CLAUDE.md:139-170` — Dual-mode runtime contract + Deploy section
- `apps/dashboard/CLAUDE.md:174-187` — Critical gotchas #1, #2, #6
- `apps/dashboard/AGENTS.md:34-41` — Dual-Mode Runtime Contract (mode BAKED at `vite build`)
- `apps/dashboard/AGENTS.md:85` — No Vercel doctrine
- `apps/dashboard/src/config/mode.ts:11` — `import.meta.env.VITE_APP_MODE` (ligne de build-time resolution)
- `apps/dashboard/Dockerfile:7` — `RUN npm run build` (single bundle per build)
- `apps/dashboard/server.js:14` — `/healthz` endpoint (Dokploy healthcheck)
- `apps/dashboard/.env.example:5-14` — env vars PUBLIC baked côté client
- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md:32-36` — D1 verify-before-assert
- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md:42-44` — D2 research FIRST
- `_TRASH/superseded/ADR-OMK-001_dual-product-dashboard-multitenant_SUPERSEDED_2026-06-11.md` — draft PROPOSED archivé (70 lignes, 4906 bytes, MD5 stable)

### Sources externes (D2 context7)
- `/vitejs/vite` — `docs/guide/env-and-mode.md` (env vars `VITE_*` statically replaced at build time) + `vite/packages/vite/src/node/plugins/define.ts` (define plugin pattern) + `docs/guide/build.md` (single bundle per `vite build` invocation)
- `/websites/caddyserver_caddyfile` — `reverse_proxy` directive + `health_uri` healthcheck passif

### Voir aussi (sans duplication)
- **ADR-SUPABASE-001** — Couvre Auth/RLS/DB schemas. Cet ADR-OMK-001 y fait référence mais ne le duplique PAS.
- **ADR-INFRA-002** — Repo-Home Junction Law (le repo `01-OMK-Business-OS` reste court, conforme).
- **ADR-INFRA-003** — Business OS CEO Dashboard Matryoshka (cadrage fractal SOA01-SOA08).
- **ADR-META-001** — Doctrine Anti-Paresse (D1-D8) — appliquée tout au long de cette rédaction.

### Handoff canonique
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_omk_dashboard_dev_2026-06-10.md` — état dev avant cette ratification
- `apps/dashboard/REBUILD_WORKFLOW.md` — contrat 8 phases A→H (Phase G = cet ADR)
