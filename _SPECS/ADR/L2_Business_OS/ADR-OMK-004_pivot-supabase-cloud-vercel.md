---
id: ADR-OMK-004
title: OMK Stack Pivot — Supabase self-host + Dokploy → Supabase Cloud + Vercel/Coolify/N8N
status: RATIFIED
date: 2026-06-19
ratified: 2026-06-19 — Go A0 (post-doc-canonical-sync + Condition A = A1 LOCKED + Sub-step 2.6 cleanup DONE)
last_updated: 2026-06-19 (Claude Code — post-draft context integration + final ratification flip)
deciders: [A0 Amadeus]
proposed_by: Codex (A2) on A0 directive
updated_by: Claude Code (A2) — D1 evidence + 5 conditions (A LOCKED A1 + B/C/D/E post-ratification HITL)
domain: L2 Business OS / OMK Services / Infra
tags: [#ADR #omk #pivot #supabase-cloud #vercel #coolify #n8n #multi-account #3-account #deploy #infra #ratified #claude-update]
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-OMK-002, ADR-OMK-003, ADR-INFRA-002, ADR-ABCOS-001, ADR-META-001, ADR-META-002]
supersedes: "ADR-OMK-001 (deploy section D1-D4: Dokploy → Vercel) + ADR-SUPABASE-001 (hosting: self-host VPS → Supabase Cloud). OMK-001 §runtime **AMENDED 2026-06-19** : single-mode SaaS only (VITE_APP_MODE=saas), `internal` mode retired per Condition A = A1 (A0 directive)."
post_ratification_conditions_hitl: [B_jwt_hook_cloud_migration, D_vercel_auth_off, E_pat_rotation]  # A LOCKED A1, C DONE (_TRASH_2026-06-19_pre_pivot_vercel/)
sign_off_a0: "A0 Amadeus — Go ADR-OMK-004 — 2026-06-19 (post A1 LOCKED + doc canonical sync + Sub-step 2.6 done)"
---

# ADR-OMK-004 — OMK Stack Pivot (Supabase self-host + Dokploy → Supabase Cloud + Vercel/Coolify/N8N)

## Status

**DRAFT** — 2026-06-19 (initial Codex draft) → **2026-06-19 (Claude Code update : 5 conditions + D1 receipts gathered this turn)**. Proposé par Codex (A2) sur directive A0 ("l'abandon de Supabase self host pour Supabase cloud autant de Dokploy pour vercel"). En attente de ratification A0.

**Pre-ratification update (Claude Code, 2026-06-19)** : Codex a rédigé l'ADR sans avoir accès au contexte canon local (CLAUDE.md / AGENTS.md / REBUILD_WORKFLOW.md / `.mcp.json`). Claude Code a lu ces sources, identifié 5 trous qui empêchent la ratification propre, et intégré les corrections + D1 receipts gathered this turn. Voir §"Pre-Ratification Updates" plus bas.

**D1 receipts vérifiés** dans `handoff_github_vercel_separation_2026-06-17.md` + `handoff_mcp_add_omk_abc_2026-06-17.md` + wiki `log.md` (15-19 juin 2026) + **lecture directe `omk/CLAUDE.md`** + **`omk/apps/dashboard/AGENTS.md`** + **`omk/apps/dashboard/REBUILD_WORKFLOW.md`** + **`~/.mcp.json`** (Claude Code, 2026-06-19).

**Périmètre** : la couche **hosting + deploy** de l'écosystème OMK (et par effet de bord ABC). **Ne touche PAS** :
- Le runtime mode baked (ADR-OMK-001 §runtime, toujours valide)
- Les rôles PG (ADR-OMK-002, validé)
- Le MCP supabase-aspace (ADR-OMK-003, en rédaction)

## Pre-Ratification Updates (2026-06-19, Claude Code)

**Trigger** : A0 directive `"C'EST CODEX QUI A ECRIT L'ADR SANS AVOIR T'ES CONTEXTE DONC UPDATE L'ADR 004"`. Codex a rédigé l'ADR sans avoir accès au contexte canon local. Claude Code a lu ces sources et identifié **5 trous** que l'ADR doit fixer avant ratification pour ne PAS reproduire le drift qu'il dénonce.

### D1 receipts gathered this turn (Claude Code, 2026-06-19, lecture directe)

| Source lue | Contenu vérifié | Statut |
|---|---|---|
| `C:\Users\amado\.mcp.json` | l.96+ contient `supabase-omk` (PAT `sbp_f2af0f71…`), `supabase-abc` (PAT `sbp_4121633e…`), `vercel-omk`, `vercel-abc` | ✅ MCPs configurés (CC restart requis pour hot-load, D6 #7) |
| `omk/CLAUDE.md` (17 828 bytes) | l.25 `⚠️ Dokploy (NOT Vercel)` · l.165 `VITE_SUPABASE_URL self-hosted` · l.152-171 section "Deploy (Dokploy, NOT Vercel)" | ❌ 100% stale vs pivot |
| `omk/apps/dashboard/AGENTS.md` (6 717 bytes) | l.5 `Deploy: Dokploy (NOT Vercel)` · l.42 `Two Dokploy services` · l.46-52 Supabase self-hosted · l.86 doctrine `No Vercel` | ❌ stale |
| `omk/apps/dashboard/REBUILD_WORKFLOW.md` (9 872 bytes) | l.32, l.156, l.183 "Phase G Déploiement Dokploy" · l.183 "no Vercel" | ❌ stale |
| `omk/apps/dashboard/.vercel/` | Présent dans `ls -la` workspace | ⚠️ Source à investiguer (Condition C) |
| `omk/apps/dashboard/AGENTS.md` §2b | JWT custom_access_token_hook provisionné sur **self-hosted** `148.230.92.235` (`SECURITY DEFINER`, lit `omk_saas.memberships` first + `solaris_saas` fallback) | ⚠️ Non migré sur Cloud (Condition B) |

### 5 conditions à fixer avant ratification

#### Condition A — Status du mode `internal` (OMK-001 §runtime) — **A1 LOCKED 2026-06-19**

**Trou** : ADR §D2 liste 4 Vercel projects : `omk-saas-os`, `omk-landing-page`, `abc-community-os`, `abc-landing-page`. **Aucun `omk-internal-os`**. Or OMK-001 §runtime = 2 modes baked (`internal` + `saas`).

**Recommandation Claude (D9 self-choice, A0 veto ouvert)** : **retirer le mode `internal`** (option A1). Rationale :
- Dokploy dual-service justifié par 2 subdomains distincts. Vercel = per-project env vars, multiplier par 2 = +$25-50/mois/team pour un produit interne déjà couvert par Life OS + ABC dashboards.
- 4/4 Vercel projects sont customer-facing ou landing. L'interne = noise post-Dokploy-kill.
- L'OMK Business OS est explicitement **un SaaS productisé** (CLAUDE.md l.13 : *"staff/operator dashboard for a Paris-based services firm, productized for SaaS"*).

**Décision A0 (2026-06-19)** : **A1 LOCKED — mode `internal` retiré**. Single-mode SaaS (VITE_APP_MODE=saas). `omk_internal` schema archive-only (données staff migrent ailleurs ou restent en local).

**Conséquences AMEND OMK-001 §runtime** :
- `VITE_APP_MODE` baked = `'saas'` only (plus de switch, plus de 2 Dokploy services)
- Schema `omk_internal` → archive-only (pas de Vercel project qui pointe dessus)
- Toutes les references à `omk_internal` dans les docs canoniques → à clarifier comme "archive-only, dormant" ou à supprimer
- Le runtime baked doctrine reste valide mais simplifiée : single value, single product
- L'OMK internal staff utilise Life OS + ABC dashboards (déjà déployés), pas OMK dashboard

#### Condition B — JWT custom_access_token_hook migration vers Cloud

**Trou** : AGENTS.md §2b confirme hook provisionné sur self-hosted `148.230.92.235` (`SECURITY DEFINER`, `GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true`, hook v2 lit `omk_saas.memberships` first + `solaris_saas` fallback). Supabase Cloud = nouvelle instance, hook **à recréer** via Dashboard UI. Non mentionné dans ADR §D2 ni §Operational Runbook.

**Risque si non fixé** : Phase C auth SaaS cassée silencieusement (RLS `org_id` claim = null → 0 rows). **Bloquant pour go-live SaaS.**

**Action Étape 2.5 (runbook, ajoutée par Claude Code)** : sub-step "Hook Cloud re-provision" entre schemas setup et Phase C deploy. Capture dans `wiki/hand_offs/handoff_jwt_hook_cloud_migration_<date>.md`.

#### Condition C — `.vercel/` directory cleanup

**Trou** : `apps/dashboard/.vercel/` existe dans le workspace (lecture directe `ls -la`). Source inconnue — possible tentative Vercel pré-pivot, ou stale artifact de l'ancien projet Vercel orphaned `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3`.

**Recommandation Claude (D9)** : `git rm -rf apps/dashboard/.vercel/` après move vers `_TRASH_<date>/` (D4 no-hard-delete). Vercel CLI recrée le `.vercel/` au prochain `vercel link` légitime.

**Action Étape 2.6 (runbook, ajoutée par Claude Code)** : cleaner `.vercel/` AVANT propagation doctrine.

#### Condition D — Vercel Authentication OFF (Étape 4, déjà runbook)

ADR §Operational Runbook Étape 4 mentionne "Vercel Authentication → Off" mais c'est **manuel UI**. Doit être confirmé par A0 post-ratification.

**Recommandation Claude (D7 cost-of-escalation)** : ajouter **pré-flight check** Étape 0 — script `mcp__vercel-omk__get_project` × 2 + `mcp__vercel-abc__get_project` × 2 pour vérifier `protectionBypass` / `auth` settings AVANT de considérer les deploys comme "live". Si Auth encore ON → D1 receipt FAIL.

#### Condition E — Rotation des 2 PATs Cloud (Étape 6, déjà runbook)

`.mcp.json` expose :
- `supabase-omk` : `SUPABASE_ACCESS_TOKEN=<REDACTED-SUPABASE-PAT>`
- `supabase-abc` : `SUPABASE_ACCESS_TOKEN=<REDACTED-SUPABASE-PAT>`

Per **Test Key Pragma** (CLAUDE.md section), A0 doit rotate ces PATs post-test. Runbook Étape 6 le mentionne mais ne le fait pas.

**Recommandation Claude** : A0 crée nouveaux PATs (Dashboard Supabase OMK Org / ABC Org → Settings → Access Tokens), update env vars User scope (`SUPABASE_OMK_ACCESS_TOKEN`, `SUPABASE_ABC_ACCESS_TOKEN`), update `.mcp.json`, puis revoke les anciens. **Re-run CC restart Étape 3** post-rotation.

### Doc canonical sync (atomic avec ratification)

L'ADR §Operational Runbook Étape 2 #4 dit "MAJ `omk/CLAUDE.md` section Deploy". C'est **insuffisant**. Claude Code identifie **3 fichiers canoniques stale** à MAJ atomiquement avec la ratification, sinon fresh sessions lisent la doctrine Dokploy et reproduisent le pivot en imagination :

| Fichier | Sections à MAJ | Source de vérité post-MAJ |
|---|---|---|
| `omk/CLAUDE.md` (17 828 bytes) | l.25 (Deploy column) · l.152-171 (Deploy section) · l.165 (Supabase URL) · l.176 (gotcha #11 `.vercel/`) · l.266 (Dual Dokploy complexity) | ADR-OMK-004 §Decision |
| `omk/apps/dashboard/AGENTS.md` (6 717 bytes) | l.5 (Stack line) · l.4 (Dual-mode runtime — clarify Condition A) · l.42 (Two Dokploy services) · l.46-52 (Supabase Architecture → Cloud) · l.86 (No Vercel doctrine) | ADR-OMK-004 §Decision + Condition A |
| `omk/apps/dashboard/REBUILD_WORKFLOW.md` (9 872 bytes) | l.32 (Phase G description) · l.156-183 (Phase G implementation) | ADR-OMK-004 §D2 + Condition A + B |

**Pourquoi atomic** : l'ADR §Context ligne 48 dit *"sans formalisation, le drift doctrinal continue (les anciens ADRs disent Dokploy/self-host, la réalité opérationnelle dit Vercel/Cloud)"*. Or l'état actuel EST précisément ce drift — les 3 fichiers enseignent Dokploy alors que les deploys sont Vercel. Ratifier sans MAJ atomique = canoniser le mensonge que l'ADR dénonce.

---

## Context

L'écosystème OMK avait été dimensionné (ADR-SUPABASE-001 2026-06-08 + ADR-OMK-001 2026-06-11) autour de :
- **DB** : Supabase **self-hosté** sur VPS Hostinger KVM 2 (`148.230.92.235`), schema `omk_internal` + `omk_saas` avec RLS
- **Deploy** : Dokploy 2 services internes (`omk-dashboard-internal` + `omk-dashboard-saas`) sur subdomains `omk-internal.aspace.fr` + `omk-saas.aspace.fr`, Caddy reverse proxy, VITE_APP_MODE baked

**Trois événements** ont rendu ce dimensionnement caduque entre le 15 et le 17 juin 2026 :

1. **15 juin 2026 — Dokploy kill définitif** (wiki `log.md` ligne 3624)
   - 4 containers Dokploy en crashloop (Exited 137 = SIGKILL/OOM)
   - Root cause triple : Dokploy v0.29.7 >500 MB au boot, KVM 2 saturé (89.5% CPU steal time = Hostinger sur-vente vCPU), 3 daemons Hermes accumulés + 2109 zombies
   - A0 directive : "Kill Dokploy definitif" puis "Scale 0 + inspect source"
   - Watchdog custom A0 `aspace-dokploy-guard.service+timer` désactivé (`systemctl disable --now aspace-dokploy-guard.timer`)

2. **15 juin 2026 — Décision architecturale majeure** (wiki `log.md` ligne 3626)
   - A0 "Stop, j'etudie" puis write-back : **retour vers Supabase Cloud multi-orgs + Coolify self-hosted**
   - Recherche D2 (4 screenshots A0) des options Cloud (FREE plan limits, anti-pause via Cron/Wrappers, Supabase Cloud vs self-host)

3. **17 juin 2026 — Stack cible 3-comptes + 4 Vercel projects** (handoff MCP + handoff github_vercel_separation)
   - 3 comptes Supabase Cloud isolés (Life OS, OMK, ABC) avec PATs `sbp_*`
   - 4 repos mirrorés vers `omk-services` (team OMK) et `ABC-OS-COMMUNITY` (team ABC) sur GitHub
   - 4 projets Vercel créés + deploys READY

**Risque** : sans formalisation, le drift doctrinal continue (les anciens ADRs disent Dokploy/self-host, la réalité opérationnelle dit Vercel/Cloud). Les sessions futures qui lisent les ADRs hérités vont proposer des solutions qui contredisent la stack en place.

## Decision

### D1 — Abandon Supabase self-hosté → Supabase Cloud (3-comptes isolés)

L'écosystème est désormais sur **Supabase Cloud** (3 organisations séparées), pas sur le VPS Hostinger.

| Compte Supabase | MCP tool prefix | URL / Projet | PAT (env var) | Usage |
|---|---|---|---|---|
| **Life OS / Agency as a Service** | `mcp__supabase__*` | `zttbgnlgwizveqryknkd` (Life OS), `xuefwzzxsbdzlooitpwu` (Agency) | legacy env vars | Life OS A0 + Agency |
| **OMK Services** | `mcp__supabase-omk__*` | OMK Services Org (2 projects) | `SUPABASE_OMK_ACCESS_TOKEN=sbp_f2af0f71...` (User scope) | OMK dashboard + landing |
| **ABC-OS-COMMUNITY** | `mcp__supabase-abc__*` | ABC-OS-COMMUNITY Org (2 projects) | `SUPABASE_ABC_ACCESS_TOKEN=sbp_4121633e...` (User scope) | abc-community-os + abc-landing-page |

**Mécanisme D1** : 1 organisation Supabase Cloud = 1 Personal Access Token (PAT) = 1 MCP server entry dans `.mcp.json`. Multi-compte = multi-PATs = multi-MCPs (tool prefix distinct pour éviter collision de tool name).

### D2 — Abandon Dokploy → Vercel + Coolify + N8N (deploy stack cible)

Le deploy OMK n'est plus sur Dokploy. La stack cible post-pivot est **Vercel + Coolify + N8N** :

| Service | Rôle | Cible |
|---|---|---|
| **Vercel** | Frontends / web apps (Vite, Next.js) | 4 projets OMK + ABC (omk-saas-os, omk-landing-page, abc-community-os, abc-landing-page) |
| **Coolify** | Self-hosted services (alternative à Dokploy) | À explorer pour backends Node/Deno si besoin |
| **N8N** | Workflows / automatisation | À explorer pour orchestrer les MCPs Supabase |

**Preuve D2 (Vercel)** : 4 projets déployés le 17 juin 2026 :

| Vercel project | Team | Framework | Deploy ID | URL preview |
|---|---|---|---|---|
| `omk-saas-os` | OMK | Vite (auto-detect) | dpl_Fx8b821 | `omk-saas-9q6hbl8xz-omk-services.vercel.app` |
| `omk-landing-page` | OMK | Next.js (auto-detect) | dpl_ERCXgjM | `omk-landing-page-r3wugyjhq-omk-services.vercel.app` |
| `abc-community-os` | ABC | Next.js (auto-detect) | dpl_7qqUAvn | `abc-community-87cl71c40-guindopapa3-7646s-projects.vercel.app` |
| `abc-landing-page` | ABC | Next.js (auto-detect) | dpl_HFfpo2q | `abc-landing-page-1jsm1kx8j-guindopapa3-7646s-projects.vercel.app` |

D1 verify HTTP HEAD : 4/4 → 401 (Vercel Authentication ON par défaut, app sert ~15 KB en ~250ms).

### D3 — Séparation GitHub org : Amdkn → omk-services + ABC-OS-COMMUNITY

| Source AMD (legacy) | Cible (séparée) | Branch | SHA |
|---|---|---|---|
| `Amdkn/01-OMK-Business-OS` | `omk-services/00-omk-saas-os` | main | `ef2cc36` |
| `Amdkn/01-OMK-Service-Landing-Page` | `omk-services/00-omk-landing-page` | master | `63043a3` |
| `Amdkn/02-ABC-OS` | `ABC-OS-COMMUNITY/abc-community-os` | main | `7e21afc` |
| `Amdkn/02-ABC-FrontEnd` | `ABC-OS-COMMUNITY/abc-landing-Page` | main | `9ed1691` |

`pushed_at` = 2026-06-17T22:34. 20 autres repos AMD restent sous `Amdkn/`.

### D4 — `.mcp.json` final 16 servers (D1 verified 2026-06-17)

```
context7, notion, chrome-devtools, playwright, supabase, vercel, hostinger-dns,
symphony-supabase, symphony-baserow, symphony-affine, symphony-obsidian, symphony-plane,
supabase-omk, supabase-abc, vercel-omk, vercel-abc
```

## Consequences

### Positives

- **Isolation des clients** : OMK Services et ABC-OS-COMMUNITY ont chacun leur org GitHub + Supabase + Vercel. Une fuite de token OMK ne compromet pas ABC.
- **Scalabilité per-team** : chaque team scale indépendamment sur Vercel
- **D1 receipts vérifiables** : mirror git, deploys Vercel, 401 HTTP HEAD, MD5 checksums
- **Codex VITE_APP_MODE baked** (ADR-OMK-001 §runtime) reste valide → pas de regression runtime
- **Coût opérationnel** : Supabase Cloud FREE plan suffit pour le staging, scaling à Pro si besoin

### Négatives

- **Coût récurrent** : Supabase Cloud + Vercel Pro = ~$50-100/mois par team (vs gratuit self-host Dokploy)
- **Vendor lock-in** : Supabase Cloud (pas de RLS offline), Vercel (build lié à leur infra)
- **Vercel Authentication default ON** : les URLs preview retournent 401 même quand READY (lesson D6 #5)
- **CC tool registry static** : ajouter un nouveau MCP server (ex `supabase-omk`) nécessite **un CC restart** (lesson D6 #4, handoff MCP). Pas de hot-reload.
- **Mirror git** : 4 repos dupliqués sur 2 orgs GitHub (20 autres restent sur AMD, à terme à migrer)
- **JWT hook re-provisioning** (Condition B, ajoutée Claude Code 2026-06-19) : le `custom_access_token_hook` provisionné sur self-host `148.230.92.235` doit être recréé sur Supabase Cloud via Dashboard UI. **Bloquant silencieux pour Phase C SaaS** (RLS `org_id` claim = null → 0 rows).
- **Doc canonical drift** (ajoutée Claude Code 2026-06-19) : 3 fichiers canoniques (`omk/CLAUDE.md` + `apps/dashboard/AGENTS.md` + `apps/dashboard/REBUILD_WORKFLOW.md`) enseignent encore Dokploy/self-host. Risque que fresh sessions reproduisent le pivot en imagination. Mitigation : Sub-step 2.4 du runbook (atomic sync avec ratification).

## Verification (par receipt D1)

| Critère | Preuve | Statut |
|---|---|---|
| Mirror git 4/4 repos | SHAs `ef2cc36`, `63043a3`, `7e21afc`, `9ed1691` matchent les sources AMD | ✅ |
| Vercel deploys 4/4 READY | deploy IDs + URLs preview | ✅ |
| HTTP HEAD 4/4 → 401 | Vercel Auth ON (par design, pas un bug) | ✅ |
| 3 comptes Supabase + 6 env vars User scope | `SUPABASE_OMK_URL/ANON_KEY/ACCESS_TOKEN` + `SUPABASE_ABC_URL/ANON_KEY/ACCESS_TOKEN` | ✅ |
| `.mcp.json` 16 servers | parse + tools list | ✅ (need CC restart pour les 4 nouveaux) |
| Dokploy kill confirmé | 4 containers Exited (137), `systemctl disable aspace-dokploy-guard.timer` | ✅ |
| **Condition A** (mode internal) | **A1 LOCKED 2026-06-19 par A0** — mode `internal` retiré, single SaaS mode (`VITE_APP_MODE=saas` only) | ✅ **A1 LOCKED** |
| **Condition B** (JWT hook Cloud) | Dashboard Cloud → Authentication → Hooks → re-provisioned (handoff `handoff_jwt_hook_cloud_migration_2026-06-19.md` créé, A0 HITL ~10 min) | ⚠️ **PENDING A0 HITL** |
| **Condition C** (`.vercel/` cleanup) | `mv .vercel _TRASH_2026-06-19_pre_pivot_vercel/` + `git rm` — D1 verified : `project.json` = orphaned `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` | ✅ **DONE 2026-06-19** |
| **Condition D** (Vercel Auth OFF) | UI Settings → Security → Vercel Authentication → Off × 4 projects (omk-saas-os, omk-landing-page, abc-community-os, abc-landing-page) | ⚠️ **PENDING A0 HITL** |
| **Condition E** (PAT rotation) | Nouveaux PATs `sbp_<new>` × 2 (OMK + ABC) + env vars User scope + `.mcp.json` update + revoke `sbp_f2af0f71…` + `sbp_4121633e…` + CC restart | ⚠️ **PENDING A0 HITL** |
| Doc canonical sync (3 fichiers) | `omk/CLAUDE.md` (single-mode SaaS + Vercel) + `apps/dashboard/AGENTS.md` (Single-Mode Runtime + Cloud + ADR-OMK-004) + `apps/dashboard/REBUILD_WORKFLOW.md` (Phase G Vercel + §2 Cloud) — tous MAJ 2026-06-19 atomic avec ratification | ✅ **DONE 2026-06-19** |

## Rollback (Reversibility)

**D1 — Revert Supabase Cloud → self-host** :
1. Re-provisionner les 3 schémas (`omk_internal`, `omk_saas`, `life_os`, `agency`) sur le VPS
2. Migrer les données via `pg_dump` Cloud → VPS
3. Restaurer `model_providers.supabase` self-host dans `config.toml` Codex
4. Re-créer les MCP servers `supabase` self-host (legacy URL `https://supabase.148.230.92.235.sslip.io`)
5. Supprimer les PATs Cloud

**D2 — Revert Vercel → Dokploy (NON RECOMMANDÉ)** : Dokploy a été tué pour cause de saturation VPS. Le revert exigerait un upgrade VPS (KVM 4) + re-install Dokploy + re-deploy des 4 services. **Coût > greenfield Vercel + Supabase Cloud.**

**Conclusion** : le pivot est **irréversible en pratique** (rollback Dokploy = régresser la cause racine du pivot).

## Operational Runbook (post-ratification)

### Étape 1 — Ratification A0
Mettre à jour le frontmatter : `status: DRAFT` → `status: RATIFIED`, `date` → date du GO A0, `sign_off_a0` rempli.

### Étape 2 — Propagation doctrine

**Note Claude Code** : la liste originale d'OmK Codex (étapes 1-5) ne couvrait que 2 fichiers canoniques stale. Claude Code élargit à **3 fichiers + 2 sub-steps** pour atomicité avec la ratification.

1. Append au `LLM_Wiki/wiki/log.md` sous date du jour : "ADR-OMK-004 RATIFIED (Supabase self-host → Cloud, Dokploy → Vercel/Coolify/N8N)".
2. Append au `30_MEMORY_CORE/README.md` date du jour.
3. **Marquer fonctionnellement superseded** : append une note en tête de `ADR-OMK-001_*.md` et `ADR-SUPABASE-001_*.md` :
   ```
   > **STATUS UPDATE 2026-06-19** : See `ADR-OMK-004`. Hosting (self-host → Cloud) and deploy (Dokploy → Vercel) are pivoted. Runtime mode baked (§runtime) still valid (pending Condition A decision).
   ```
   Ne PAS radié (radier = `mv _TRASH/superseded/`, comme `ADR-REG-001` + `ADR-OPS-002` l'ont été le 15 juin). Le user peut choisir de radier formellement ou de laisser coexistés avec note.

#### Sub-step 2.4 — Doc canonical sync (3 fichiers, **ATOMIC avec ratification**)

**Gating** : ne PAS ratifier tant que ces 3 fichiers ne sont pas MAJ. Sinon fresh sessions lisent la doctrine Dokploy et reproduisent le pivot en imagination.

- **2.4.a** `30_Business_OS/10_Projects/omk/CLAUDE.md` :
  - l.25 : `⚠️ **Dokploy** (NOT Vercel)` → `✅ **Vercel** (4 projects, 2 teams)`
  - l.152-171 : section "Deploy (Dokploy, NOT Vercel)" → "Deploy (Vercel + Supabase Cloud)"
  - l.165 : `VITE_SUPABASE_URL (self-hosted: https://supabase.148.230.92.235.sslip.io)` → URL Cloud (`SUPABASE_OMK_URL` env var)
  - l.176 : gotcha #11 `.vercel/` → clarifier status post-Condition C
  - l.266 : "Dual Dokploy service complexity" → adapter si Condition A = retire internal
- **2.4.b** `30_Business_OS/10_Projects/omk/apps/dashboard/AGENTS.md` :
  - l.5 : `Deploy: Dokploy (NOT Vercel)` → `Deploy: Vercel (omk-services team, 2 projects)`
  - l.4 : Dual-mode runtime — clarifier Condition A (retire internal vs 5e project)
  - l.42 : `Two Dokploy services, not one with a switch` → adapter si Condition A = retire internal
  - l.46-52 : Supabase Architecture → Cloud (URL Cloud, JWT hook Cloud)
  - l.86 : `No Vercel` doctrine → radier (Condition A/B validés)
- **2.4.c** `30_Business_OS/10_Projects/omk/apps/dashboard/REBUILD_WORKFLOW.md` :
  - l.32 : Phase G description Dokploy → Vercel
  - l.156-183 : Phase G implementation (2 services Dokploy → Vercel projects)

#### Sub-step 2.5 — JWT custom_access_token_hook Cloud migration (Condition B)

Si l'app est destinée à SaaS production (Condition A = A1 retire internal, OU A2 5e project où internal reste staff-only) :

1. Supabase Cloud Dashboard → OMK Services Org → Authentication → Hooks → "Custom Access Token" → Enable
2. SQL hook function `public.custom_access_token_hook(event jsonb) returns jsonb` :
   - Lit `omk_saas.memberships` first (priority)
   - Fallback `solaris_saas.memberships` (legacy)
   - `SECURITY DEFINER`
   - Inject `org_id` dans JWT claims
3. `GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true` dans OMK Services project env vars (Supabase Dashboard → Settings → API)
4. Test : login user OMK SaaS → `SELECT current_setting('request.jwt.claims', true)::json->>'org_id'` retourne UUID valide
5. D1 receipt : `wiki/hand_offs/handoff_jwt_hook_cloud_migration_<date>.md` créé
6. Si Condition A = A2 (5e project, internal actif) : refaire pour Cloud `omk_internal` Org

#### Sub-step 2.6 — `.vercel/` cleanup (Condition C)

1. `mkdir -p _TRASH_<date>_pre_pivot_vercel/`
2. `mv apps/dashboard/.vercel _TRASH_<date>_pre_pivot_vercel/` (D4 no-hard-delete)
3. `git rm -rf apps/dashboard/.vercel` post-move
4. D1 receipt : handoff capture la présence originelle + raison du cleanup

#### Étape 2.5 (réordonnancée depuis Étape 0) — Pré-flight Vercel Auth check (Condition D)

Avant Étape 3 (CC restart), vérification programmatique de l'état Auth sur les 4 Vercel projects. **Note D6 #4** : MCPs Vercel ne sont hot-loadés qu'après CC restart, donc cette étape est en pratique un HITL UI post-CC-restart.

```bash
# Post-CC-restart :
mcp__vercel-omk__get_project("omk-saas-os")        # → check protectionBypass / auth
mcp__vercel-omk__get_project("omk-landing-page")   # → idem
mcp__vercel-abc__get_project("abc-community-os")   # → idem
mcp__vercel-abc__get_project("abc-landing-page")   # → idem
```

Si `protectionBypass` ou `auth` encore ON → Étape 4 (manual UI) doit être complétée **AVANT** de considérer les deploys comme "live". Sinon CC restart révèle des MCPs wired avec des deploys 401.

### Étape 3 — CC restart
1. Backup `.mcp.json` (déjà OK, 16 servers)
2. Close + reopen Claude Code (ou tout agent Codex CLI)
3. D1 verify post-restart :
   - `mcp__supabase-omk__list_organizations` → `[{name: "OMK Services Org", projects: 2}]`
   - `mcp__supabase-abc__list_organizations` → `[{name: "ABC-OS-COMMUNITY's Org", projects: 2}]`
   - `mcp__vercel-omk__list_projects` → 2 projets OMK
   - `mcp__vercel-abc__list_projects` → 2 projets ABC
   - `mcp__supabase__list_organizations` → unchanged (Life OS + Agency)

### Étape 4 — Vercel Authentication OFF
Pour chaque projet Vercel OMK + ABC :
1. Vercel UI → Project Settings → Security → Vercel Authentication → **Off**
2. D1 verify : `curl -I https://omk-saas-9q6hbl8xz-omk-services.vercel.app/` → 200

### Étape 5 — Custom domains (optionnel)
- `omk.kalybana.com` (déjà LIVE selon wiki log 2026-06-14) + Vercel project `omk-saas-os`
- `abc-os.kalybana.com` (déjà LIVE) + Vercel project `abc-community-os`
- Vérifier les DNS CNAME et HTTPS via `curl -vI`

### Étape 6 — Pat rotation (Test Key Pragma)
1. Générer nouveaux PATs pour `supabase-omk` et `supabase-abc`
2. Update env vars User scope
3. Update `.mcp.json` (la clé actuelle `sbp_f2af0f71...` a été lue par le shell agent — rotation recommandée)
4. D1 verify post-rotation

## D6 Lessons shipped (cumulatif)

| # | Lesson | Date | Source |
|---|---|---|---|
| 1 | `cp1252 Windows console` : `PYTHONIOENCODING=utf-8` requis | 2026-06-17 | handoff_github_vercel |
| 2 | Git 2.53.0 `safe.bareRepository='explicit'` : `git -c safe.bareRepository=all` par commande | 2026-06-17 | handoff_github_vercel |
| 3 | MCP Vercel wrapper ne sérialise pas `gitRepository` : bypass `curl -X POST` direct | 2026-06-17 | handoff_github_vercel |
| 4 | Vercel `projectSettings` required + auto-detect via `?skipAutoDetectionConfirmation=1` | 2026-06-17 | handoff_github_vercel |
| 5 | Vercel Authentication default ON : à OFF manuellement dans UI | 2026-06-17 | handoff_github_vercel |
| 6 | Vercel PATCH `/v9/projects/{id}` rejette `gitRepository` : DELETE + POST recreates | 2026-06-17 | handoff_github_vercel |
| 7 | **CC tool registry static at session start** : new MCP server names need CC restart | 2026-06-17 | handoff_mcp_add_omk_abc |
| 8 | A0 explicit "no CC restart" preference : workarounds first, escalate only if needed | 2026-06-17 | handoff_mcp_add_omk_abc |
| 9 | **Dokploy + KVM 2 = non viable** : 89.5% CPU steal time, swap 1.5 GB, zombie reap | 2026-06-15 | wiki log |
| 10 | **Supabase self-host vs Cloud** : Cloud FREE plan = viable avec anti-pause, self-host = saturation VPS | 2026-06-15 | wiki log |

## References

### Sources primaires (D1 verify-before-assert)

- `_SPECS/ADR/L2_Business_OS/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md` — le runtime baked (D1-D2 conservés, D3-D5 pivotés)
- `_SPECS/ADR/L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md` — la version self-host (superseded fonctionnellement)
- `_SPECS/ADR/L2_Business_OS/ADR-OMK-002_pg-roles-provisionning.md` — toujours valide (rôles PG, indépendants du hosting)
- `_SPECS/ADR/L2_Business_OS/ADR-OMK-003_mcp-supabase-aspace.md` — en rédaction (peut être pivoté : MCP self-host → MCP Cloud)

### Sources canoniques stale (D1 gathered this turn, Claude Code 2026-06-19)

- `30_Business_OS/10_Projects/omk/CLAUDE.md` (17 828 bytes) — ligne 25 + section l.152-171 + l.165 Supabase URL + l.176 gotcha `.vercel/` + l.266 Dual Dokploy complexity → **100% stale vs pivot**
- `30_Business_OS/10_Projects/omk/apps/dashboard/AGENTS.md` (6 717 bytes) — l.5 Stack line + l.42 Two Dokploy services + l.46-52 Supabase self-hosted + l.86 No Vercel doctrine → **stale**
- `30_Business_OS/10_Projects/omk/apps/dashboard/REBUILD_WORKFLOW.md` (9 872 bytes) — l.32 + l.156-183 Phase G Dokploy → **stale**
- `30_Business_OS/10_Projects/omk/apps/dashboard/.vercel/` — dossier présent dans workspace (Condition C)
- `C:\Users\amado\.mcp.json` (16 servers) — D1 verified 2026-06-19, contient `supabase-omk` + `supabase-abc` + `vercel-omk` + `vercel-abc` (CC restart requis pour hot-load, D6 #7)

### Sources receipts (D1)

- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` (28.5 KB, last update 2026-06-19 02:04) — mirror 4 repos + 4 Vercel deploys + 10 D6 lessons
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_mcp_add_omk_abc_2026-06-17.md` (9.5 KB) — 3-comptes Supabase + `.mcp.json` 16 servers
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` lignes 3624-3670 — Dokploy kill + décision Supabase Cloud + stack cible Vercel+SupabaseCloud+Coolify+N8N
- `C:\Users\amado\.mcp.json` (16 servers) — D1 verified
- Windows User scope env vars (6 nouvelles : SUPABASE_OMK/ABC × URL/ANON_KEY/ACCESS_TOKEN) — D1 set

### Sources doctrine

- `ADR-META-001_anti-paresse-verify-before-assert.md` (D1-D8 doctrine) — appliquée tout au long
- `ADR-META-002_self-choice-autonomy.md` (D9-D12 doctrine) — A0 respecte le coût d'escalation
- `ADR-INFRA-002_repo-home-junction-law.md` — le repo `01-OMK-Business-OS` reste court (mirror = fork, pas de duplication de code)
- `ADR-ABCOS-001_multitenant-supabase-strategy.md` (ACCEPTED 2026-06-10) — pattern multi-tenant pour ABC (aligné avec ce pivot)

### Sources externes (D2 context7 + WebFetch)

- Supabase Cloud FREE plan limits (D2 wiki 2026-06-15) : pause après 7 jours inactivité, anti-pause via Cron/Wrappers
- Vercel docs : `projectSettings` + auto-detect framework + Vercel Authentication default

## Cross-refs

- `handoff_github_vercel_separation_2026-06-17.md` (Vercel deploy)
- `handoff_mcp_add_omk_abc_2026-06-17.md` (MCP 3-comptes Supabase)
- `handoff_mcp_supabase_twin_live_2026-06-17.md` (MCP Symphony twin)
- `handoff_mcp_persistence_v2_2026-06-16.md` (8/8 MCPs .cmd)
- `handoff_jwt_hook_cloud_migration_<date>.md` (Condition B — à créer en Sub-step 2.5)
- `wiki/log.md` (entrées Dokploy kill 15 juin, Supabase Cloud 15 juin, mirror 17 juin, **Claude Code update 19 juin**)
- `30_Business_OS/10_Projects/omk/CLAUDE.md` (**Sub-step 2.4.a : à MAJ — Deploy section + Supabase URL + gotcha #11**)
- `30_Business_OS/10_Projects/omk/apps/dashboard/REBUILD_WORKFLOW.md` (**Sub-step 2.4.c : à MAJ — Phase G**)
- `30_Business_OS/10_Projects/omk/apps/dashboard/AGENTS.md` (**Sub-step 2.4.b : à MAJ — No-Vercel doctrine à radier, Supabase Architecture → Cloud**)

---

**Next safe action (post-Claude-Code update, 2026-06-19)** :

1. ~~**A0 tranche Condition A** (A1 retire `internal` vs A2 5e Vercel project) — seul blocker décisionnel.~~ ✅ **A1 LOCKED 2026-06-19**.
2. ~~Une fois A tranché, exécution **atomique** du runbook Étape 2 :
   - Sub-step 2.4 (3 fichiers canoniques MAJ — dépend de Condition A)~~ ✅ **DONE 2026-06-19**
   - ~~Sub-step 2.5 (JWT hook Cloud migration — Condition B)~~ ⚠️ **handoff créé, A0 HITL pending**
   - ~~Sub-step 2.6 (`.vercel/` cleanup — Condition C)~~ ✅ **DONE 2026-06-19** (move to `_TRASH_2026-06-19_pre_pivot_vercel/`)
3. ~~Étape 0/2.5 (pré-flight Vercel Auth — Condition D) post-CC-restart.~~ ⚠️ **A0 HITL pending** (4 projects)
4. ~~Étape 6 (PAT rotation — Condition E) HITL A0.~~ ⚠️ **A0 HITL pending** (2 PATs)
5. ~~Ratification finale : `status: DRAFT → RATIFIED` après toutes les conditions fixées.~~ ✅ **RATIFIED 2026-06-19**

**Status final** : ADR-OMK-004 **RATIFIED 2026-06-19** par A0. Doc canonical sync atomique exécuté. Conditions B/D/E = A0 HITL post-ratification (per runbook Étapes 2.5/4/6, ne bloquent pas la ratification puisque ce sont des actions manuelles UI). Condition C = DONE. Condition A = A1 LOCKED par A0 directive 2026-06-19.

**D6 Lesson #26 shipped (Claude Code final ratification 2026-06-19)** : pour un ADR pivot, la ratification peut précéder les conditions HITL si (a) la décision architecturale est figée, (b) le doc canonical sync est fait, (c) les conditions HITL sont clairement identifiées + handoff créé. Ne PAS bloquer la ratification sur des actions UI manuelles qui peuvent être trackées séparément (handoff dédié).
