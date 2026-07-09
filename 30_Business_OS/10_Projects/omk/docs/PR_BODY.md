# 🚀 Phase G — PR GitHub Prête à Merger

## ⚠️ Contexte : PR ne peut pas être créée automatiquement

Le user `Amdkn` (mon token GitHub) **n'est pas collaborateur du repo `omk-services/00-omk-saas-os`** (qui appartient à l'org `omk-services`, pas au user). Seul un membre de l'org a les droits de créer des PRs.

`gh pr create` retourne :
```
pull request create failed: GraphQL: must be a collaborator (createPullRequest)
```

**Solution** : créer la PR via l'UI GitHub (3 clics). Body et title pré-formatés ci-dessous.

---

## 📋 Step 1 — Ouvre ce lien

**URL de création** : https://github.com/omk-services/00-omk-saas-os/compare/main...feature/omk-saas-v1.0?expand=1

L'UI GitHub pré-remplit la comparaison `base: main` ← `compare: feature/omk-saas-v1.0`. Tu cliques **"Create pull request"** (bouton vert).

## 📋 Step 2 — Coller ce title

```
feat(omk-saas): one-sprint customer-ready finalization (Phase A→H)
```

## 📋 Step 3 — Coller ce body (Markdown)

```markdown
## Summary

Sprint goal: ship OMK Tax Service SaaS as customer-ready multi-tenant app in 1 day.

- **23 files** (17 modified + 6 added), **+1424 / -558** lines
- **9 omk_saas.* tables** with RLS + FORCE RLS + 30+ tenant_isolation policies
- **JWT custom_access_token_hook** function deployed (wiring pending A0)
- **Edge Function sign-up-organization** deployed (id `e47f4aa1`, ACTIVE)
- **11/14 views** read from Cloud (3 static = D2 backlog)
- **17 routes** (2 public + 14 protected + 404) with ProtectedRoute auth guard
- **0 TS errors**, vite build 4.25s, bundle 266 KB JS + 41 KB CSS

## Phase breakdown

- **Phase A**: Cloud SQL migration (DESTRUCTIVE one-shot). 7→9 tables. Drift `public.*` archived in `_archive_drift_2026_06_20`.
- **Phase B**: Vercel + Auth wiring runbook persisté (`docs/runbooks/2026-06-20-phase-b-auth-hook-wiring.md`).
- **Phase C**: Repository layer + tenant guard (ADR-OMK-005).
- **Phase D**: 6 static views wrapped in ViewShell, 2 wired to live DB (legal_docs + sales_leads).
- **Phase E**: Routing + auth guard (DEMO_MODE flag removed).
- **Phase F**: Edge Function + Sign Out button.
- **Phase G**: Vercel deploy OK (preview URL live, see D6 #85).
- **Phase H**: ADR-OMK-005 RATIFIED + cloud-bootstrap skill + 8 runbooks + AGENTS.md/wiki.log.md/MEMORY.md.

## D6 lessons shipped (27 cumulées : #50 → #88)

Most critical for A0:
- **D6 #64**: JWT hook wiring is dashboard-only (no API path).
- **D6 #68**: PGRST_DB_SCHEMAS env var is dashboard-only.
- **D6 #85** (NEW, live E2E): Vercel Authentication ON by default — toggle OFF in Settings → Security.

## A0 actions pending before merge (5 total, ~7 min)

1. Wire JWT `custom_access_token_hook` in Auth dashboard (D6 #64)
2. Add `omk_saas` to PGRST_DB_SCHEMAS in Settings → API (D6 #68)
3. **🆕 Disable Vercel Authentication in Settings → Security (D6 #85 — MANDATORY)**
4. *(Optional)* Paste GEMINI_API_KEY for AI features
5. **Then merge this PR** → production URL `omk-saas-os.vercel.app` becomes live

## ADR-OMK-005 (newly ratified)

Implements defense-in-depth tenant guard:
- Server-side: RLS policies (omk_saas.* + JWT hook)
- Client-side: `useOrg()` hook + `getActiveOrgId()` cache + `assertOrgIdForWrite()` pre-flight
- UI: `ProtectedRoute` auth gate + 404 catch-all

## Preview URL (auto-deployed)

https://omk-saas-kbyhsl88j-omk-services.vercel.app/

⚠️ Currently behind Vercel Authentication wall (D6 #85). Toggle OFF in project settings to see the OMK app.

## Test plan

- [ ] A0 toggles Vercel Authentication OFF
- [ ] A0 wires JWT custom_access_token_hook
- [ ] A0 adds `omk_saas` to PGRST_DB_SCHEMAS
- [ ] `curl -sI https://omk-saas-kbyhsl88j-omk-services.vercel.app/` → 200 OK + LoginView HTML
- [ ] Browser sign in with `dev+omk@acme-demo.fr` / `dev-password-not-for-prod`
- [ ] Decode JWT at https://jwt.io → expect `app_metadata.org_id = 00000000-0000-0000-0000-000000000a01`
- [ ] Dashboard renders with 5 client cards (Boulangerie Martin, etc.)
- [ ] Navigate to /legal → 7 docs from omk_saas.legal_docs
- [ ] Navigate to /sales → 4 leads in kanban
- [ ] Click Sign Out (sidebar bottom) → redirected to /login

## Refs

- `_SPECS/ADR/L2_Business_OS/ADR-OMK-005_tenant-isolation-guard.md`
- Skill: `~/.claude/skills/cloud-bootstrap/`
- Runbooks: `omk/docs/runbooks/2026-06-20-phase-{a,b,c,d,e,f,g,h}-receipt.md`
```

## 📋 Step 4 — Click "Create pull request"

L'UI GitHub crée la PR et te renvoie l'URL `https://github.com/omk-services/00-omk-saas-os/pull/N`.

## 📋 Step 5 — Reviewer + Merge

1. Ajoute un reviewer (toi-même si solo, ou un teammate)
2. Si tu as déjà fait les 3 actions A0 (Vercel Auth, hook, PGRST), tu peux **Merge pull request** immédiatement
3. Vercel auto-promote le SHA sur **production** (URL `omk-saas-os.vercel.app`)

## 📋 Step 6 — Vérification live (post-merge)

Une fois mergé, le SHA est sur `main` → Vercel déclenche un deploy production. Run :
```bash
curl -sI https://omk-saas-os.vercel.app/
# Expected: 200 OK + HTML body <title>OMK Services</title>
```

---

## 🔑 Récap ultra-court

**Action 1 (toi)** : Ouvre https://github.com/omk-services/00-omk-saas-os/compare/main...feature/omk-saas-v1.0?expand=1
**Action 2 (toi)** : Colle title + body ci-dessus (ou utilise la version complète dans le fichier)
**Action 3 (toi)** : Click "Create pull request"
**Action 4 (optionnel)** : Merge si les 3 A0 manuels sont faits (Vercel Auth + hook + PGRST)

**C'est 30 sec de UI work pour créer la PR, puis merge quand tu veux.**

---

*Note pour plus tard : pour les futures PRs cross-org, il faudrait soit (a) ajouter `Amdkn` comme collaborator sur `omk-services`, soit (b) utiliser un PAT issu d'un compte membre de l'org. C'est un D6 #89 candidate.*
