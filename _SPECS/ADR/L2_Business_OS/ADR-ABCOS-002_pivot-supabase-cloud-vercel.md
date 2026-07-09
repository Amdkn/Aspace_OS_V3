---
id: ADR-ABCOS-002
title: ABC OS Stack Pivot — Supabase self-host → Supabase Cloud + Vercel 3-account separation
status: RATIFIED
date: 2026-06-19
ratified: 2026-06-19 — Go A0 (post-doc-canonical-sync + 6 conditions identified + 4/5 fixed or N/A, Condition F P0 PENDING A0 HITL)
last_updated: 2026-06-19 (Claude Code — post-draft context integration + final ratification flip)
deciders: [A0 Amadeus]
proposed_by: Codex (A2) on A0 directive
updated_by: Claude Code (A2) — D1 evidence + 6 ABC-specific conditions (A N/A · B post-ratification HITL · C N/A (CURRENT) · D post-ratification HITL · E post-ratification HITL · **F P0 PENDING A0 HITL**)
domain: L2 Business OS / ABC OS Community & Child Care BOS
tags: [#ADR #abc_os #pivot #supabase-cloud #vercel #multi-account #3-account #deploy #infra #ratified #claude-update]
related: [ADR-ABCOS-001, ADR-SUPABASE-001, ADR-OMK-001, ADR-OMK-004, ADR-INFRA-002, ADR-META-001, ADR-META-002]
supersedes: "ADR-ABCOS-001 (hosting: self-host VPS → Supabase Cloud). Does NOT supersede ABCOS-001 §multi-tenant (org_id + RLS) which is still valid; nor D10 mixed-tenancy model."
post_ratification_conditions_hitl: [B_jwt_hook_abc_cloud, D_vercel_auth_off, E_pat_rotation, F_pgrst_db_schemas_action]  # A N/A, C N/A (CURRENT documented)
sign_off_a0: "A0 Amadeus — Go ADR-ABCOS-002 — 2026-06-19 (post 5-file doc sync + 6 conditions identified)"
---

# ADR-ABCOS-002 — ABC OS Stack Pivot (Supabase self-host → Supabase Cloud + Vercel 3-account)

## Status
**DRAFT** — 2026-06-19 (initial Codex draft) → **2026-06-19 (Claude Code update : 6 conditions ABC-specific + D1 receipts gathered this turn)**. Proposé par Codex (A2) sur directive A0 ("fait la même chose pour ABC OS que tu as fait pour OMK"). En attente de ratification A0.

**Pre-ratification update (Claude Code, 2026-06-19)** : Codex a rédigé l'ADR avec un bon contexte ABC (déjà Vercel, etc.) mais sans avoir lu les fichiers canoniques locaux. Claude Code a lu ces sources, identifié 5 trous spécifiques à ABC (vs OMK-004) et 1 **CRITICAL P0 blocker** (PGRST_DB_SCHEMAS Dashboard action), intégrés ci-dessous. Voir §"Pre-Ratification Updates" plus bas.

**D1 receipts vérifiés** dans `handoff_mcp_add_omk_abc_2026-06-17.md` + `handoff_github_vercel_separation_2026-06-17.md` + **lecture directe `abc/CLAUDE.md`** + **`abc/apps/abc-os-community/AGENTS.md`** + **`abc/apps/abc-childcare-portal/CLAUDE.md`** + **`abc/apps/abc-childcare-portal/AGENTS.md`** + **`~/.mcp.json`** + **`abc/apps/*/.vercel/project.json`** (Claude Code, 2026-06-19).

**Périmètre** : la couche **hosting + deploy + multi-account** de l'écosystème ABC OS. **Ne touche PAS** :
- Le multi-tenant schema model (ADR-ABCOS-001 §D1-D5, toujours valide)
- Le mixed-tenancy model (ADR-ABCOS-001 §D10, validé 2026-06-12)
- Les custom domains `abc-os.kalybana.com` + `abc.kalybana.com` (déjà LIVE)

## Pre-Ratification Updates (2026-06-19, Claude Code)

**Trigger** : A0 directive *"FAIT LA MEME CHOSE POUR ABC OS QUE TU AS FAIT POUR OMK APRES CLAUDE VA METTRE A JOUR"*. Codex a rédigé l'ADR-002 (17KB) sans lecture directe des fichiers canoniques locaux. Claude Code a lu ces sources et identifié **5 conditions spécifiques à ABC (vs OMK-004) + 1 CRITICAL P0 blocker**.

### D1 receipts gathered this turn (Claude Code, 2026-06-19, lecture directe)

| Source lue | Contenu vérifié | Statut |
|---|---|---|
| `C:\Users\amado\.mcp.json` | l.96+ contient `supabase-omk`, `supabase-abc` (PAT `sbp_4121633e…`), `vercel-omk`, `vercel-abc` | ✅ MCPs configurés (CC restart requis pour hot-load, D6 #7) |
| `30_Business_OS/10_Projects/abc/CLAUDE.md` (7 016 bytes) | l.30 mentionne `prj_HSw4IBR2omI5qegmEinOksr6xzo0` + team `team_d3JjRK4fJUE9ACohbdlhv9Gc` (amd-lab) ; l.23 login BROKEN ticket pending | ⚠️ Partiellement stale : ne mentionne pas explicitement le pivot Cloud |
| `abc/apps/abc-os-community/AGENTS.md` (8 136+ bytes) | l.23 OPEN TICKET (A0 HITL pending) : Vercel env var `NEXT_PUBLIC_SUPABASE_URL` doit passer de `https://abc.kalybana.com` (NXDOMAIN) à `https://supabase.kalybana.com` (VPS self-host) ou **mieux : Cloud URL** (post-pivot) ; render = 14s RSC timeout sans le fix | ❌ Stale (pointe vers self-host, pas Cloud) |
| `abc/apps/abc-childcare-portal/CLAUDE.md` (1 ligne) | `@AGENTS.md` (import seul) | ⚠️ Pas de Hosting section explicite |
| `abc/apps/abc-childcare-portal/AGENTS.md` (minimal) | juste nextjs-agent-rules | ⚠️ Pas de Hosting section |
| `abc/apps/abc-os-community/.vercel/project.json` | `{"projectId":"prj_HSw4IBR2omI5qegmEinOksr6xzo0","orgId":"team_d3JjRK4fJUE9ACohbdlhv9Gc","projectName":"abc-os-community"}` | ✅ ACTIVE (not orphan, vs OMK's `.vercel/` which was orphan `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3`) |
| `abc/apps/abc-childcare-portal/.vercel/project.json` | `{"projectId":"prj_AN7joKC8eSwEc7adzmjzAXQdyt8C","orgId":"team_d3JjRK4fJUE9ACohbdlhv9Gc","projectName":"abc-childcare-portal"}` | ✅ ACTIVE (also not orphan) |
| `abc/apps/abc-os-community/supabase/` | contient `migrations/` + `scripts/` + `BUILD_HUB_WIRING_NOTES.md` | ⚠️ Source canonique des migrations ABC (à vérifier si seedées sur Cloud) |
| `_SPECS/REGISTRY/supabase_schemas.md` | registry canonique des schémas | ❌ Probablement stale (doit mentionner Cloud pour `abc_os` + `abc_child_care`) |
| MEMORY.md §"Vercel mirror+deploy 2026-06-17" + "abc-os/kalybana" | abc_os schema migré 17 tables + 85 rows + RLS sur Cloud. **PostgREST exposure BLOCKED** : `PGRST_DB_SCHEMAS` env var read-once at boot, fix = Dashboard UI Settings | ⚠️ **P0 BLOCKER** |

### 6 conditions à fixer avant ratification (ABC-specific)

#### Condition A — Mode `internal` → **N/A pour ABC**

**Pas de mode `internal` dans ABC** (single-mode community SaaS, pas de dual-mode runtime comme OMK). Cette condition ne s'applique pas. Le runtime multi-tenant `org_id` + RLS (ADR-ABCOS-001 §D2) reste valide 100% — seul le hosting pivote.

#### Condition B — JWT custom_access_token_hook Cloud migration (ABC-specific)

**Trou** : ADR §Decision D1 mentionne que `abc_os` schema est désormais sur Cloud, mais ne mentionne PAS la migration du hook. AGENTS.md §`abc-os-community` ne référence pas explicitement le hook `custom_access_token_hook`. Le hook self-host (si provisionné) doit être re-provisionné sur Cloud.

**Risque si non fixé** : queries RLS-scoped retournent 0 rows silencieusement (mêmes symptoms que OMK-004 Condition B).

**Action Étape 2.5 (runbook, ajoutée par Claude Code)** : sub-step "Hook Cloud re-provision" via Dashboard UI OMK Cloud. À vérifier si hook ABC était bien provisionné sur self-host en premier lieu.

#### Condition C — `.vercel/` directories → **CURRENT (PAS orphan), differs from OMK**

**Découverte critique** : contrairement à OMK où `.vercel/` contenait `prj_FJpNDykkNMhDJUEg2FvKAegeeQG3` (projet Vercel orphaned pré-pivot), les deux `.vercel/` ABC contiennent des **projets ACTIVE** :
- `abc-os-community/.vercel/project.json` → `prj_HSw4IBR2omI5qegmEinOksr6xzo0` (ACTIF, déployé, custom domain `abc-os.kalybana.com` wired)
- `abc-childcare-portal/.vercel/project.json` → `prj_AN7joKC8eSwEc7adzmjzAXQdyt8C` (ACTIF, déployé)

**Conclusion** : **NE PAS move vers `_TRASH_`** (D4 no-hard-delete ne s'applique PAS ici, ces projets sont vivants). Le sub-step 2.6 du runbook OMK-004 ne se transpose PAS à ABC.

**Action requise** : aucun cleanup. Juste clarifier dans le runbook ABC que `.vercel/` reste (les projets sont canoniques).

#### Condition D — Vercel Authentication OFF (déjà runbook)

ADR §Operational Runbook Étape 4 mentionne "Vercel Authentication → Off". À appliquer aux 4 Vercel projects ABC :
- `abc-community-os` (dpl_7qqUAvn)
- `abc-landing-page` (dpl_HFfpo2q)
- `prj_HSw4IBR2omI5qegmEinOksr6xzo0` (legacy, may need OFF too)
- `prj_AN7joKC8eSwEc7adzmjzAXQdyt8C` (legacy, may need OFF too)

⚠️ **À clarifier avec A0** : les 2 legacy projects sont-ils encore actifs ou archivés ? Le ADR-002 ne mentionne que les 2 nouveaux (mirror 17 juin). Si les legacy sont toujours live, ils doivent aussi avoir Auth OFF.

#### Condition E — Rotation du PAT `sbp_4121633e…`

`.mcp.json` expose `SUPABASE_ABC_ACCESS_TOKEN=<REDACTED-SUPABASE-PAT>`. Per Test Key Pragma, rotation recommandée post-test.

**Action** : identique à OMK-004 Condition E (A0 crée nouveau PAT, update env vars, update `.mcp.json`, revoke ancien).

#### Condition F — ⚠️ **P0 BLOCKER : `PGRST_DB_SCHEMAS` Dashboard action**

**Découverte critique** (per MEMORY.md §"Vercel mirror+deploy 2026-06-17" D6 #11) : `abc_os` schema est migré sur Cloud (17 tables + 85 rows + RLS enabled) MAIS **PostgREST n'expose PAS le schema**. Queries via PostgREST API retournent **404**. Cause : env var `PGRST_DB_SCHEMAS` est **read-once at boot** et la valeur par défaut est `public,storage,graphql_public`. `NOTIFY pgrst, 'reload config'` ne change PAS cette env var.

**Fix A0 action requise (~2 min UI)** :
1. Dashboard https://supabase.com/dashboard/project/<abc_project_id>/settings/api
2. Section "Exposed schemas" → add `abc_os` + `abc_child_care` (si ce schema existe en Cloud aussi)
3. Save → PostgREST auto-reload 5-10 sec

**D1 honest** : jusqu'à cette action, **les données ABC visibles dans le HTML sont des constantes TypeScript hardcodées** (fallback UI), PAS du live data Supabase. Les tables existent, RLS actif, mais inaccessibles via API PostgREST.

**Cette condition est P0 et BLOQUE la ratification effective** du pivot. Une fois l'action UI faite, D1 verify : `curl https://<abc_url>/rest/v1/organizations?select=*` doit retourner 200 + données.

### Doc canonical sync (atomic avec ratification)

L'ADR §Operational Runbook Étape 2 #4-5 dit "MAJ `abc/CLAUDE.md` + `abc-os-community/AGENTS.md`". **Insuffisant** — Claude Code identifie **5 fichiers canoniques stale** à MAJ atomiquement :

| Fichier | Sections à MAJ | Source de vérité post-MAJ |
|---|---|---|
| `abc/CLAUDE.md` (7 016 bytes) | l.30 Vercel map (déjà OK) · l.23 ticket kalybana login (à MAJ : pointer vers Cloud URL, pas VPS self-host) · l.75-82 Vercel contract (clarifier `prj_HSw4IBR2...` = legacy toujours actif OU archivé) | ADR-ABCOS-002 §Decision + Condition F |
| `abc/apps/abc-os-community/AGENTS.md` (8 136+ bytes) | l.13 Vercel project ID (déjà OK) · l.23 OPEN TICKET (changer `https://supabase.kalybana.com` → Cloud OMK URL `SUPABASE_ABC_URL` env var) · l.39 Playwright MCP (déjà OK) | ADR-ABCOS-002 §Decision D1 + Condition F |
| `abc/apps/abc-childcare-portal/CLAUDE.md` (1 ligne import) | Add Hosting section pointer | ADR-ABCOS-002 §Decision |
| `abc/apps/abc-childcare-portal/AGENTS.md` (minimal) | Add Hosting + Vercel contract section | ADR-ABCOS-002 §Decision |
| `_SPECS/REGISTRY/supabase_schemas.md` | `abc_os` + `abc_child_care` schema entries now on Cloud (was self-host `148.230.92.235`) | ADR-ABCOS-002 §Decision D1 + Condition F |

**Pourquoi atomic** : même doctrine que OMK — sans MAJ atomique, fresh sessions lisent doctrine stale et reproduisent le pivot en imagination. Pire pour ABC car Condition F est un P0 blocker invisible jusqu'à la prochaine session qui découvre.

---

## Context

L'écosystème ABC OS avait été dimensionné (ADR-ABCOS-001 2026-06-10) autour de :
- **DB** : Supabase **self-hosté** sur VPS Hostinger KVM 2 (148.230.92.235), schema `abc_os` + `abc_child_care`, multi-tenant via `org_id` + RLS
- **Deploy** : Vercel project `prj_HSw4IBR2omI5qegmEinOksr6xzo0` (team `guindopapa3-7646s`) avec custom domain `abc-os.kalybana.com` (LIVE depuis 2026-06-14)
- **GitHub** : `Amdkn/02-ABC-OS` + `Amdkn/02-ABC-FrontEnd` (single org)

**Quatre jalons** ont préparé le terrain du pivot entre le 8 et le 17 juin 2026 :

1. **8 juin 2026 — Vercel Production Deploy `abc-childcare-portal`** (wiki log ligne 57)
   - Premier déploiement Vercel pour ABC family
   - `vercel link --yes` → projet créé dans team `guindopapa3-7646s`
   - Valide le pattern "Vercel + GitHub Amdkn" comme baseline

2. **10 juin 2026 — `ADR-ABCOS-001` ACCEPTED** (multi-tenant self-host Supabase)
   - Airlock 3-tours clos, A0 GO tel quel
   - Domaine ABC OS arrêté : `abc.kalybana.com`
   - JWT Hook = Postgres native function
   - 2 schémas : `abc_os` + `abc_child_care`

3. **12-14 juin 2026 — Production LIVE sur `abc-os.kalybana.com`**
   - 12 juin : `picard-audit-and-prod-workflow` Phases 1-6 (Phases 3-7 GitHub push sans Dokploy déjà)
   - 13 juin : 3 UX/perf bugs fixed (self-host Material Symbols, Theme Context SSR, Supabase URL fix)
   - 14 juin : `abc-os.kalybana.com` FULLY LIVE (HTTPS 200, JWT org_id+role, RLS-scoped queries)

4. **17 juin 2026 — Stack cible 3-comptes + mirror GitHub** (handoff MCP + handoff github_vercel_separation)
   - 3 comptes Supabase Cloud isolés (Life OS, OMK, ABC) avec PATs `sbp_*`
   - Mirror 4 repos vers `omk-services` (team OMK) et `ABC-OS-COMMUNITY` (team ABC) sur GitHub
   - 4 projets Vercel créés (2 OMK + 2 ABC) + deploys READY

**Différence avec OMK** : ABC OS était **déjà sur Vercel** depuis le 8 juin, donc le pivot Dokploy→Vercel ne s'applique pas. Le pivot ABC est purement **hosting (self-host Supabase → Cloud) + multi-account formalization** (3-comptes Supabase + GitHub org split).

**Risque** : sans formalisation, le drift doctrinal continue. ADR-ABCOS-001 dit self-host (acceptable), mais l'implémentation dit Supabase Cloud. Les sessions futures vont proposer des solutions qui contredisent la stack en place.

## Decision

### D1 — Abandon Supabase self-hosté → Supabase Cloud (3-comptes isolés)

L'écosystème ABC est désormais sur **Supabase Cloud** (compte séparé `ABC-OS-COMMUNITY`), pas sur le VPS Hostinger.

| Compte Supabase | MCP tool prefix | Org / Projet | PAT (env var) | Usage |
|---|---|---|---|---|
| **Life OS / Agency as a Service** | `mcp__supabase__*` | `zttbgnlgwizveqryknkd` (Life OS), `xuefwzzxsbdzlooitpwu` (Agency) | legacy env vars | Life OS A0 + Agency (hors scope ABC) |
| OMK Services | `mcp__supabase-omk__*` | OMK Services Org (2 projects) | `SUPABASE_OMK_ACCESS_TOKEN=sbp_f2af0f71...` (User scope) | OMK dashboard + landing (hors scope ABC) |
| **ABC-OS-COMMUNITY** | `mcp__supabase-abc__*` | ABC-OS-COMMUNITY's Org (2 projects : `abc-os` + `abc-child-care`) | `SUPABASE_ABC_ACCESS_TOKEN=sbp_4121633e...` (User scope) | abc-community-os + abc-landing-page + abc-childcare-portal |

**Mécanisme D1** : 1 organisation Supabase Cloud = 1 Personal Access Token (PAT) = 1 MCP server entry dans `.mcp.json`. Multi-compte = multi-PATs = multi-MCPs (tool prefix distinct pour éviter collision de tool name).

**Spécificité ABC** : 2 schémas Postgres (`abc_os` + `abc_child_care`) restent la séparation business, mais sont désormais hébergés sur **Supabase Cloud** au lieu de self-host. Le multi-tenant model (org_id + RLS, ADR-ABCOS-001 §D2) est conservé 100% — seul le hosting pivote.

### D2 — Vercel 3-account separation (déjà opérationnel depuis le 8 juin)

ABC OS était déjà sur Vercel (1er deploy 8 juin). Le pivot 3-comptes (17 juin) ajoute 2 nouveaux Vercel projects dans la **team ABC séparée** (`guindopapa3-7646s-projects`) :

| Vercel project | Team | GitHub link | Framework | Deploy ID | URL preview |
|---|---|---|---|---|---|
| `abc-community-os` | ABC | ✅ github `ABC-OS-COMMUNITY/abc-community-os` | Next.js (auto-detect) | dpl_7qqUAvn | `abc-community-87cl71c40-guindopapa3-7646s-projects.vercel.app` |
| `abc-landing-page` | ABC | ✅ github `ABC-OS-COMMUNITY/abc-landing-Page` | Next.js (auto-detect) | dpl_HFfpo2q | `abc-landing-page-1jsm1kx8j-guindopapa3-7646s-projects.vercel.app` |

**Custom domain existant** : `abc-os.kalybana.com` (LIVE depuis 2026-06-14) wired vers Vercel project `prj_HSw4IBR2omI5qegmEinOksr6xzo0`. CNAME `cname.vercel-dns.com` (D1 receipts independently verified).

### D3 — Séparation GitHub org : Amdkn → ABC-OS-COMMUNITY

| Source AMD (legacy) | Cible (séparée) | Branch | SHA |
|---|---|---|---|
| `Amdkn/02-ABC-OS` | `ABC-OS-COMMUNITY/abc-community-os` | main | `7e21afc` |
| `Amdkn/02-ABC-FrontEnd` | `ABC-OS-COMMUNITY/abc-landing-Page` | main | `9ed1691` |

`pushed_at` = 2026-06-17T22:34. 20 autres repos AMD restent sous `Amdkn/`.

**Pattern de séparation** : 1 organisation GitHub par entité business souveraine (OMK = `omk-services`, ABC = `ABC-OS-COMMUNITY`, AMD = `Amdkn` pour Life OS / Agency / kernels).

### D4 — `.mcp.json` final 16 servers (D1 verified 2026-06-17)

```
context7, notion, chrome-devtools, playwright, supabase, vercel, hostinger-dns,
symphony-supabase, symphony-baserow, symphony-affine, symphony-obsidian, symphony-plane,
supabase-omk, supabase-abc, vercel-omk, vercel-abc
```

Pour ABC spécifiquement : `mcp__supabase-abc__*` (DB) + `mcp__vercel-abc__*` (deploy). Vercel token partagé entre `vercel-omk` et `vercel-abc` (1 token team-wide, pas par-projet).

## Consequences

### Positives

- **Isolation des entités business** : ABC (communautaire + childcare régulé) est isolé de OMK et de AMD/Life OS. Une fuite de token ABC ne compromet pas OMK.
- **Scalabilité per-team** : chaque team GitHub/Vercel/Supabase scale indépendamment
- **Conformité G8 Legal facilitée** : Child Care BOS (entité régulée) a son propre org Supabase Cloud → audit trail + DPA facilités
- **Multi-tenant model conservé** : `org_id` + RLS (ADR-ABCOS-001 §D2) reste 100% valide, pas de régression
- **D1 receipts vérifiables** : mirror git (SHAs), Vercel deploy IDs, custom domain LIVE, 401 HTTP HEAD
- **Vercel pre-existant** : ABC a 2 semaines d'avance sur OMK côté Vercel, donc moins de risk sur le setup

### Négatives

- **Coût récurrent** : Supabase Cloud + Vercel Pro = ~$50-100/mois par team (vs gratuit self-host Dokploy)
- **Vendor lock-in** : Supabase Cloud (pas de RLS offline), Vercel (build lié à leur infra)
- **Vercel Authentication default ON** : les URLs preview retournent 401 même quand READY (lesson D6 #5)
- **CC tool registry static** : ajouter un nouveau MCP server nécessite **un CC restart** (lesson D6 #4)
- **3 PATs à rotationner** : si A0 veut zeroize (Test Key Pragma Phase 4), il faut 3 opérations parallèles
- **Mirror git** : 4 repos dupliqués sur 2 orgs GitHub (20 autres restent sur AMD, à terme à migrer)
- **`PGRST_DB_SCHEMAS` exposure blocker (Condition F, P0)** (ajoutée Claude Code 2026-06-19) : `abc_os` schema migré sur Cloud MAIS PostgREST ne l'expose pas (env var read-once at boot, D6 #11). Sans action Dashboard UI 2 min, l'app ABC ne peut pas query live data via API. **Bloquant silencieux pour go-live ABC.**
- **Doc canonical drift** (ajoutée Claude Code 2026-06-19) : 5 fichiers canoniques stale (vs OMK-004 qui en avait 3). Risque fresh sessions reproduisent pivot en imagination. Mitigation : Sub-step 2.4 du runbook (atomic sync avec ratification).
- **Login BROKEN ticket pré-existant** : `NEXT_PUBLIC_SUPABASE_URL` pointe vers `https://abc.kalybana.com` (NXDOMAIN) au lieu de `https://supabase.kalybana.com` (self-host) OU **mieux** : Cloud URL post-pivot. Sans fix, render 14s RSC timeout. (AGENTS.md l.23, OPEN depuis 13 juin).

## Verification (par receipt D1)

| Critère | Preuve | Statut |
|---|---|---|
| Mirror git 2/2 repos ABC | SHAs `7e21afc` + `9ed1691` matchent les sources AMD | ✅ |
| Vercel deploys 2/2 READY (ABC) | deploy IDs + URLs preview | ✅ |
| HTTP HEAD 4/4 → 401 (incl. ABC) | Vercel Auth ON (par design) | ✅ |
| `mcp__supabase-abc__*` + `mcp__vercel-abc__*` registered | `.mcp.json` 16 servers | ✅ (need CC restart) |
| Custom domain `abc-os.kalybana.com` | CNAME `cname.vercel-dns.com`, HTTPS 200 | ✅ (LIVE depuis 14 juin) |
| 6 env vars User scope ABC | `SUPABASE_ABC_URL/ANON_KEY/ACCESS_TOKEN` | ✅ |
| **Condition A** (mode internal) | N/A pour ABC — single-mode community SaaS | ✅ **N/A** |
| **Condition B** (JWT hook Cloud ABC) | `custom_access_token_hook` re-provisioned via Dashboard UI ABC Cloud (conditional : si hook existait sur self-host, à vérifier B.0 handoff) | ⚠️ **POST-RATIFICATION HITL** |
| **Condition C** (`.vercel/` cleanup) | **N/A** — `.vercel/` contient projets ACTIVE (`prj_HSw4IBR2...` + `prj_AN7joKC8...`), NE PAS move vers `_TRASH_`. Doc clarifiée | ✅ **N/A (CURRENT DOCUMENTED)** |
| **Condition D** (Vercel Auth OFF) | UI Settings → Security → Vercel Authentication → Off × 4 projects (abc-community-os, abc-landing-page, + 2 legacy si encore actifs) | ⚠️ **POST-RATIFICATION HITL** |
| **Condition E** (PAT rotation ABC) | Nouveau PAT `sbp_<new>` + env var `SUPABASE_ABC_ACCESS_TOKEN` + `.mcp.json` update + revoke `sbp_4121633e…` + CC restart | ⚠️ **POST-RATIFICATION HITL** |
| **Condition F** (PGRST_DB_SCHEMAS expose abc_os) | **P0 BLOCKER** — Dashboard Settings → API → Exposed schemas → add `abc_os` (+ `abc_child_care` si existe en Cloud) | ⚠️ **POST-RATIFICATION HITL (P0)** |
| Doc canonical sync (5 fichiers ABC) | `abc/CLAUDE.md` (Hosting pivot note) + `abc-os-community/AGENTS.md` (NEXT_PUBLIC_SUPABASE_URL → Cloud) + `abc-childcare-portal/CLAUDE.md` (hosting pointer) + `abc-childcare-portal/AGENTS.md` (Hosting + Work Guidance) + `_SPECS/REGISTRY/supabase_schemas.md` (abc_os LIVE Cloud + ADR refs) — tous MAJ 2026-06-19 atomic avec ratification | ✅ **DONE 2026-06-19** |

## Rollback (Reversibility)

**D1 — Revert Supabase Cloud → self-host** :
1. Re-provisionner `abc_os` + `abc_child_care` sur le VPS
2. Migrer les données via `pg_dump` Cloud → VPS
3. Restaurer les MCP servers `supabase-abc` self-host (legacy URL `https://supabase.148.230.92.235.sslip.io`)
4. Supprimer les PATs Cloud
5. **Risque data loss** : si RLS ABC a changé entre temps (ajout d'org, nouveaux tenants), la migration peut casser

**D2 — Revert Vercel** : pas applicable, ABC est déjà sur Vercel depuis le 8 juin. Le rollback serait "retour en arrière sur Dokploy" qui n'a jamais été utilisé pour ABC. **Pas de risque.**

**Conclusion** : le pivot ABC est **partiellement irréversible** (D1 self-host = risqué, D2 Vercel = non-applicable). La stack Cloud est désormais le default opérationnel.

## Operational Runbook (post-ratification)

### Étape 1 — Ratification A0
Mettre à jour le frontmatter : `status: DRAFT` → `status: RATIFIED`, `date` → date du GO A0, `sign_off_a0` rempli.

### Étape 2 — Propagation doctrine

**Note Claude Code** : la liste originale (étapes 1-5) ne couvrait que 2 fichiers canoniques stale. Claude Code élargit à **5 fichiers + 3 sub-steps** (incluant Condition F PGRST_DB_SCHEMAS).

1. Append au `LLM_Wiki/wiki/log.md` sous date du jour : "ADR-ABCOS-002 RATIFIED (Supabase self-host → Cloud, Vercel 3-account separation)".
2. Append au `30_MEMORY_CORE/README.md` date du jour.
3. **Marquer fonctionnellement superseded** : append une note en tête de `ADR-ABCOS-001_*.md` :
   ```
   > **STATUS UPDATE 2026-06-19** : See `ADR-ABCOS-002`. Hosting (self-host → Cloud) is pivoted. Multi-tenant model (§D1-D5) and mixed-tenancy model (§D10) are still valid.
   ```
   Ne PAS radié (radier = `mv _TRASH/superseded/`). Coexistence possible avec note de supersession.

#### Sub-step 2.4 — Doc canonical sync (5 fichiers, **ATOMIC avec ratification**)

**Gating** : ne PAS ratifier tant que ces 5 fichiers ne sont pas MAJ. Sinon fresh sessions lisent la doctrine stale et reproduisent le pivot en imagination.

- **2.4.a** `30_Business_OS/10_Projects/abc/CLAUDE.md` :
  - l.23 OPEN TICKET kalybana login : clarifier que `NEXT_PUBLIC_SUPABASE_URL` doit pointer vers Cloud OMK URL (`SUPABASE_ABC_URL` env var), PAS self-host `https://supabase.kalybana.com`
  - l.30 Vercel map : ajouter les 2 nouveaux Vercel projects (`abc-community-os` dpl_7qqUAvn + `abc-landing-page` dpl_HFfpo2q) à côté des legacy `prj_HSw4IBR2...` + `prj_AN7joKC8...`
- **2.4.b** `30_Business_OS/10_Projects/abc/apps/abc-os-community/AGENTS.md` :
  - l.23 OPEN TICKET (A0 HITL pending) : update Vercel env var `NEXT_PUBLIC_SUPABASE_URL` vers Cloud URL `https://<project_id>.supabase.co`
  - l.13 Vercel project ID : ajouter les 2 nouveaux Vercel projects aux legacy
- **2.4.c** `30_Business_OS/10_Projects/abc/apps/abc-childcare-portal/CLAUDE.md` (1 ligne) :
  - Expandir pour pointer Hosting + Vercel contract
- **2.4.d** `30_Business_OS/10_Projects/abc/apps/abc-childcare-portal/AGENTS.md` (minimal) :
  - Add Hosting + Vercel contract section
- **2.4.e** `_SPECS/REGISTRY/supabase_schemas.md` :
  - `abc_os` schema entry : hosting = Cloud (was self-host `148.230.92.235`)
  - `abc_child_care` schema entry (si existe) : hosting = Cloud

#### Sub-step 2.5 — JWT custom_access_token_hook Cloud migration (Condition B)

**À vérifier en premier** : est-ce que `abc_os.memberships` ou un hook similaire était provisionné sur self-host ? Si oui :

1. Supabase Cloud Dashboard → ABC-OS-COMMUNITY Org → Authentication → Hooks → "Custom Access Token" → Enable
2. SQL hook function (similaire à OMK Condition B) :
   - Lit `abc_os.memberships` first
   - Fallback si nécessaire
   - `SECURITY DEFINER`
   - Inject `org_id` dans JWT claims
3. `GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true` dans ABC Cloud project env vars
4. Test : login user ABC → `SELECT current_setting('request.jwt.claims', true)::json->>'org_id'` retourne UUID valide
5. D1 receipt : handoff `handoff_jwt_hook_abc_cloud_migration_2026-06-19.md` créé

#### Sub-step 2.6 — `.vercel/` documentation (Condition C — **N/A mais à clarifier**)

**N/A pour ABC** : les deux `.vercel/project.json` contiennent des projets ACTIVE (`prj_HSw4IBR2...` pour `abc-os-community`, `prj_AN7joKC8...` pour `abc-childcare-portal`). NE PAS move vers `_TRASH_`.

**Action requise** : juste clarifier dans le runbook et la doc (déjà fait dans §Pre-Ratification Updates Condition C) que `.vercel/` est conservé.

#### Sub-step 2.7 — ⚠️ **P0 : `PGRST_DB_SCHEMAS` Dashboard action (Condition F)**

**P0 BLOCKER** : sans cette étape, l'app ABC ne peut pas query `abc_os` via PostgREST (404 sur toutes les queries). Visible data = fallback UI TypeScript, PAS live data.

**Action A0 HITL (~2 min)** :
1. Dashboard Supabase : https://supabase.com/dashboard/project/<abc_project_id>/settings/api
2. Section "Exposed schemas" → add `abc_os` (+ `abc_child_care` si schema existe en Cloud) à la liste
3. Save → PostgREST auto-reload 5-10 sec
4. D1 verify : `curl -H "apikey: $SUPABASE_ABC_ANON_KEY" https://<abc_project_id>.supabase.co/rest/v1/organizations?select=*` → 200 + données

### Étape 3 — CC restart
1. Close + reopen Claude Code (ou tout agent Codex CLI)
2. D1 verify post-restart :
   - `mcp__supabase-abc__list_organizations` → `[{name: "ABC-OS-COMMUNITY's Org", projects: 2}]`
   - `mcp__vercel-abc__list_projects` → 2 projets ABC (mirror 17 juin)
   - `mcp__supabase-omk__list_organizations` → unchanged (OMK)
   - `mcp__supabase__list_organizations` → unchanged (Life OS + Agency)

### Étape 4 — Vercel Authentication OFF (Condition D)
Pour chaque projet Vercel ABC :
1. **Mirror 17 juin** (2 projets) : `abc-community-os` + `abc-landing-page` (team `guindopapa3-7646s-projects`)
2. **Legacy** (si encore actifs, à clarifier A0) : `prj_HSw4IBR2...` + `prj_AN7joKC8...`
3. UI Project Settings → Security → Vercel Authentication → **Off**
4. D1 verify : `curl -I https://<project_url>/` → 200 (au lieu de 401)

### Étape 5 — Custom domain verification (déjà fait)
- `abc-os.kalybana.com` est déjà wired vers Vercel project `prj_HSw4IBR2omI5qegmEinOksr6xzo0`
- `curl -vI https://abc-os.kalybana.com` doit retourner 200 avec cert Let's Encrypt valide
- Si ABC OS 2 a un nouveau domain (`childcare.kalybana.com`, ADR-ABCOS-001 §D1), le câbler maintenant

### Étape 6 — Pat rotation (Test Key Pragma, Condition E)
1. Générer nouveau PAT pour `supabase-abc` (garder `sbp_4121633e...` en backup pendant transition)
2. Update env var User scope `SUPABASE_ABC_ACCESS_TOKEN`
3. Update `.mcp.json` (le PAT actuel a été lu par le shell agent — rotation recommandée)
4. D1 verify post-rotation

### Étape 7 — Doc canonical sync closeout
Re-vérifier après toutes les actions HITL que les 5 fichiers canoniques restent sync.

## D6 Lessons shipped (cumulatif — miroir OMK-004)

| # | Lesson | Date | Source |
|---|---|---|---|
| 1 | `cp1252 Windows console` : `PYTHONIOENCODING=utf-8` requis | 2026-06-17 | handoff_github_vercel |
| 2 | Git 2.53.0 `safe.bareRepository='explicit'` | 2026-06-17 | handoff_github_vercel |
| 3 | MCP Vercel wrapper ne sérialise pas `gitRepository` : bypass `curl -X POST` direct | 2026-06-17 | handoff_github_vercel |
| 4 | Vercel `projectSettings` required + auto-detect via `?skipAutoDetectionConfirmation=1` | 2026-06-17 | handoff_github_vercel |
| 5 | Vercel Authentication default ON : à OFF manuellement dans UI | 2026-06-17 | handoff_github_vercel |
| 6 | Vercel PATCH `/v9/projects/{id}` rejette `gitRepository` : DELETE + POST recreates | 2026-06-17 | handoff_github_vercel |
| 7 | CC tool registry static at session start : new MCP server names need CC restart | 2026-06-17 | handoff_mcp_add_omk_abc |
| 8 | A0 explicit "no CC restart" preference | 2026-06-17 | handoff_mcp_add_omk_abc |
| 9 | ABC OS était déjà sur Vercel (8 juin) — le pivot Dokploy→Vercel ne s'applique pas, c'est uniquement hosting+multi-account | 2026-06-19 | wiki log |
| 10 | **Supabase self-host vs Cloud pour entités régulées (Child Care BOS)** : Cloud = DPA + audit facilités, self-host = data residency | 2026-06-15 | wiki log |

## References

### Sources primaires (D1 verify-before-assert)

- `_SPECS/ADR/L2_Business_OS/ADR-ABCOS-001_multitenant-supabase-strategy.md` — multi-tenant model (toujours valide, hosting pivote)
- `_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md` — ADR miroir (pour OMK), créé le 2026-06-19 RATIFIED
- `_SPECS/ADR/L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md` — superseded fonctionnellement (self-host → Cloud), 2026-06-19 status note SUPERSEDED ajoutée
- `30_Business_OS/10_Projects/abc/apps/abc-os-community/CLAUDE.md` — **n'existe PAS** (seulement AGENTS.md dans cette app), Hosting section à MAJ dans AGENTS.md

### Sources canoniques stale (D1 gathered this turn, Claude Code 2026-06-19)

- `30_Business_OS/10_Projects/abc/CLAUDE.md` (7 016 bytes) — l.23 ticket kalybana login BROKEN, l.75-82 Vercel contract → **stale** (pas mention du pivot Cloud)
- `30_Business_OS/10_Projects/abc/apps/abc-os-community/AGENTS.md` (8 136+ bytes) — l.23 OPEN TICKET (NEXT_PUBLIC_SUPABASE_URL → self-host, pas Cloud) → **stale**
- `30_Business_OS/10_Projects/abc/apps/abc-childcare-portal/CLAUDE.md` (1 ligne `@AGENTS.md`) → pas de Hosting section
- `30_Business_OS/10_Projects/abc/apps/abc-childcare-portal/AGENTS.md` (minimal, nextjs-agent-rules only) → pas de Hosting section
- `_SPECS/REGISTRY/supabase_schemas.md` — registry canonique des schémas → probablement stale
- `abc/apps/abc-os-community/.vercel/project.json` → ACTIVE (`prj_HSw4IBR2...`) — NE PAS cleanup
- `abc/apps/abc-childcare-portal/.vercel/project.json` → ACTIVE (`prj_AN7joKC8...`) — NE PAS cleanup
- `C:\Users\amado\.mcp.json` (16 servers) — D1 verified 2026-06-19, contient `supabase-abc` + `vercel-abc` (CC restart requis pour hot-load, D6 #7)

### Sources receipts (D1)

- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` (28.5 KB) — mirror 4 repos (incl. 2 ABC) + 4 Vercel deploys (incl. 2 ABC)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_mcp_add_omk_abc_2026-06-17.md` (9.5 KB) — 3-comptes Supabase + `.mcp.json` 16 servers (incl. `supabase-abc`, `vercel-abc`)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_community_dev_2026-06-10.md` (57 KB) — état dev ABC au 10 juin (avant pivot)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_abc_os_kalybana_login_failure_postmortem_2026-06-14.md` (13.7 KB) — postmortem du 14 juin (déjà LIVE)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` lignes 3257-3670 — chronologie complète (8 juin Vercel first deploy → 14 juin LIVE → 17 juin 3-comptes)
- `C:\Users\amado\.mcp.json` (16 servers) — D1 verified
- Windows User scope env vars (6 nouvelles : SUPABASE_OMK/ABC × URL/ANON_KEY/ACCESS_TOKEN) — D1 set

### Sources doctrine

- `ADR-META-001_anti-paresse-verify-before-assert.md` (D1-D8 doctrine)
- `ADR-META-002_self-choice-autonomy.md` (D9-D12 doctrine)
- `ADR-INFRA-002_repo-home-junction-law.md` — le repo `02-ABC-OS` reste court (mirror = fork)
- `ADR-OMK-004_pivot-supabase-cloud-vercel.md` — pattern miroir pour OMK, sert de référence structurelle

### Sources externes (D2 context7 + WebFetch)

- Supabase Cloud FREE plan limits (D2 wiki 2026-06-15) : pause après 7 jours inactivité, anti-pause via Cron/Wrappers
- Vercel docs : `projectSettings` + auto-detect framework + Vercel Authentication default
- Custom domain `kalybana.com` TLD souverain — géré via Hostinger DNS (wiki log D6 #4 verified via Resolve-DnsName)

## Cross-refs

- `handoff_github_vercel_separation_2026-06-17.md` (Vercel mirror + deploy)
- `handoff_mcp_add_omk_abc_2026-06-17.md` (MCP 3-comptes Supabase, inclut ABC)
- `handoff_abc_os_community_dev_2026-06-10.md` (dev avant pivot)
- `handoff_abc_os_kalybana_login_failure_postmortem_2026-06-14.md` (postmortem LIVE)
- `handoff_mcp_supabase_twin_live_2026-06-17.md` (MCP Symphony twin)
- `handoff_mcp_persistence_v2_2026-06-16.md` (8/8 MCPs .cmd)
- `wiki/log.md` (entrées 8 juin Vercel first deploy, 14 juin LIVE, 17 juin 3-comptes)
- `30_Business_OS/10_Projects/abc/apps/abc-os-community/CLAUDE.md` (à MAJ)
- `30_Business_OS/10_Projects/abc/apps/abc-os-community/AGENTS.md` (à MAJ)
- `_SPECS/REGISTRY/supabase_schemas.md` (à MAJ : `abc_os` et `abc_child_care` désormais sur Cloud)

---

**Next safe action** : faire ratifier par A0 (signature + status RATIFIED) puis exécuter le runbook Étapes 2-7.

---

**Status final** : ADR-ABCOS-002 **RATIFIED 2026-06-19** par A0. Doc canonical sync (5 fichiers) atomique exécuté. Conditions B/D/E = A0 HITL post-ratification (per runbook sub-steps 2.5/4/6, ne bloquent pas la ratification puisque ce sont des actions manuelles UI). Condition F = **P0 HITL bloquant live data queries** (per runbook sub-step 2.7, fix Dashboard UI ~2 min). Condition A/C = N/A pour ABC (single-mode community SaaS / `.vercel/` ACTIVE not orphan).

**D6 Lesson #31 shipped (Claude Code final ratification ABC 2026-06-19)** : pour un ADR mirror (OMK → ABC), **les conditions divergent** significativement. Toujours relire les fichiers canoniques locaux avant de répliquer un pattern. Le `.vercel/` orphan de OMK était une exception, pas la règle : `.vercel/` peut contenir projets ACTIVE. Condition F (PostgREST exposure) est invisible jusqu'à la première query live data — d'où l'importance des D1 receipts gathered this turn.

**Cross-applicable** : pattern "ABC vs OMK" differences = leçons pour futurs pivots mirror. La structure apps/ détermine le doc canonical sync count (3 fichiers pour OMK, 5 pour ABC, peut être 10+ pour un projet avec plus d'apps).
