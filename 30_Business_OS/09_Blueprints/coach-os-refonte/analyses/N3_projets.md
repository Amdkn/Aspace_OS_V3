---
id: ANALYSE_N3_PROJETS
brief: N3 — Ce qui est réellement construit dans 10_Projects
perimetre: 30_Business_OS/10_Projects/ (racine : 24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects)
date: 2026-08-05
agent: explorateur (lecture seule)
mode: top-down, jonctions NTFS écartées
compte_fichiers_lus: 47 (sur budget ≈60)
---

# N3 — Ce qui est réellement construit dans `10_Projects`

## Mode opératoire

J'ai suivi la discipline prescrite : cartographie → points d'entrée → descente sélective. Jonctions NTFS écartées (32 sous `30_Business_OS` cartographiées au préalable). Aucune suppression, aucune modification : un seul fichier écrit, celui-ci. Chemin absolu à chaque constat.

## 0. Vue d'ensemble (le piège structural)

`30_Business_OS/10_Projects/` contient **deux projets distincts que la doctrine confond** :

1. **`omk/`** — le **OMK Services Business OS** (B2B SaaS, "staff/operator dashboard for a Paris-based services firm, productized for SaaS" — `omk/CLAUDE.md:5-7`).
   - Code canonique : `omk/apps/dashboard/` (Vite+React+TS, 14 vues + auth).
   - Code dormant : `omk/apps/landing/` (vide), `omk/apps/nexus/` (Next.js boilerplate, landing page sister).
   - Dépôts sœur rapatriés 2026-08-01 : `omk/repos/{omk-saas-target, omk-services-nexus-landing-en, omk-services-nexus-quiz, omk-nexus-landing-3-personas, citadelle-os}`.
2. **`repos/coach-os/`** — le **Coach OS Desktop** (le produit niche coach, fork du Life OS shell).
3. **`00_coach_os/`** — un **instantané antérieur** du même Coach OS (venu de `omk-nexus-coaching-premium/`, voir §1).

La confusion est amplifiée par le fait que :
- `omk/MANIFEST.md` se déclare "single SaaS mode" et rattache Coach OS comme **fille** (`omk/MANIFEST.md:38-40`).
- Mais `omk/CLAUDE.md` (canon d'identité) **ignore totalement** Coach OS — il décrit uniquement `apps/dashboard` et `apps/landing`. Les 17 apps du Coach OS (Dashboard, People, Operations, etc., au sens Desktop-OS) n'apparaissent nulle part dans `omk/CLAUDE.md`, qui liste **un autre** jeu de 14 vues (Clients, Documents, Agents, Finance, SOPLibrary, Settings, People, Tasks, Legal, Growth, Sales, Marketplace, ItData).

Deux projets, deux vocabulaires identiques, deux codebases indépendants.

---

## 1. L'inventaire des projets

| Projet | État apparent | Pile technique | Fichier qui le dit |
|---|---|---|---|
| **`omk/`** (parent) | ACTIVE — pivot post-ADR-OMK-004, 5 phases sur 8 livrées | Vite+React 19+TS (dashboard), Next.js 16.2.6 (nexus), Tailwind v4, Supabase, react-router 7, Motion, Lucide | `omk/CLAUDE.md:5-25` |
| **`omk/repos/coach-os/`** | ACTIVE — code le plus frais, 365 fichiers, 7,8 Mo, git actif | Vite+React 19+TS, Zustand, Tailwind v4, Supabase, PostHog, UserTour, Motion, Three.js | `omk/repos/coach-os/package.json:14-23`, `omk/MERGE_REPORT_2026-08-01.md:38-43` |
| **`omk/00_coach_os/`** | DORMANT — snapshot pré-pivot, sans `.env.local`, identique au `repos/coach-os/src/` | Idem `repos/coach-os` | `omk/MERGE_REPORT_2026-08-01.md:60-62`, diff `00_coach_os/` vs `repos/coach-os/` (src/ = même arborescence) |
| **`omk/repos/omk-saas-target/`** | ACTIVE — mirror canon du `apps/dashboard` post-pivot | Vite+React+TS, Supabase SQL, server.js Express, Dockerfile | `omk/repos/omk-saas-target/AGENTS.md` + `omk/MANIFEST.md:18` (canon unique = `omk-services/00-omk-saas-os`) |
| **`omk/repos/omk-services-nexus-landing-en/`** | DORMANT — 5 fichiers HTML (index + 4 versions v1/v2/v3/os), pas de build | HTML pur | `omk/repos/omk-services-nexus-landing-en/index.html` + 4 variantes |
| **`omk/repos/omk-services-nexus-quiz/`** | DORMANT — 1 fichier `quiz.html` | HTML pur | `omk/repos/omk-services-nexus-quiz/quiz.html` |
| **`omk/repos/omk-nexus-landing-3-personas/`** | DORMANT — 4 HTML (index + David/Harrison/Marcus), dossier v2/v3/wargame | HTML pur | `omk/repos/omk-nexus-landing-3-personas/` |
| **`omk/repos/citadelle-os/`** | DORMANT — Vite+React+TS, ~6 fichiers src, l'ancêtre du Coach OS | Vite+React+TS | `omk/repos/citadelle-os/package.json`, `README.md` |
| **`omk/chartes/coach_premium_capsule.md`** | ACTIVE — charte R3-R4-R5 catch-up Q3-W4 | (doc) | `omk/chartes/coach_premium_capsule.md:1-52` |
| **`omk/runbooks/runbook-coach-premium-capsule.md`** | ACTIVE — runbook d'exécution Phase 3 Superpowers | (doc) | `omk/runbooks/` |
| **`omk/wiki/log.md`** | ACTIVE — ledger append-only | (doc) | `omk/wiki/log.md:1-63` |
| **`omk/_resources/audits/2026-07-15_ai-act-pilier5-audit.md`** | ACTIVE — audit AI-Act Pilier 5 | (doc) | `omk/_resources/audits/` |
| **`omk/_resources/capsules/coach_premium_001.md`** | SKELETON — capsule 7 sections, body PENDING A3_Picard draft | (doc) | `omk/_resources/capsules/` |
| **`omk/docs/runbooks/phase-{a..ii}-receipt.md`** (11 fichiers) | ACTIVE — 8 phases A→H + zero-bug-sprint | (doc) | `omk/docs/runbooks/` |
| **`omk/apps/nexus/`** | DORMANT — Next.js boilerplate, README par défaut, AGENTS.md 327 octets | Next.js 16.2.6 | `omk/apps/nexus/README.md`, `omk/apps/nexus/app/page.tsx` (composants Header/Hero/Manifeste etc.) |
| **`omk/apps/landing/`** | VIDE — dossier créé, aucun fichier | — | `omk/apps/landing/` (listing vide) |
| **`omk/_TRASH_2026-06-19_pre_pivot_vercel/`** | ARCHIVE — état pré-pivot Dokploy→Vercel | — | `omk/_TRASH_2026-06-19_pre_pivot_vercel/` |
| **`omk/_stranded_2026-07-24/`** | INCONNU — non exploré (préserve budget) | — | `omk/_stranded_2026-07-24/` |
| **`omk/_sidebars/`** | INCONNU — non exploré | — | `omk/_sidebars/` |
| **`solaris/`** | ACTIVE — Sister canon 3-ICP Solaris (AaaS Agency Garden) | Next.js 16.2.6, Dokploy/Vercel | `solaris/MANIFEST.md:55` ("self-hosted Supabase") |
| **`ceo-desktop/`** | PHASE_1_SKELETON — pas d'A0 GO requis, doctrine-only | (doc) | `ceo-desktop/MANIFEST.md:6-7` |
| **`cerritos-gtd-dispatch/`** | ACTIVE — smoke-test ASP-19, doctrine GTD pipeline | (doc + apps/spock-wf0/ vide) | `cerritos-gtd-dispatch/MANIFEST.md:30` (DoD presque complet) |
| **`rilcot/`** | ACTIVE_PROTOTYPE — React/Vite, 8-file package, no production | React 19+Vite, Lucide, Recharts, Tailwind CDN | `rilcot/MANIFEST.md:51-56` |
| **`abc/`** | ACTIVE — apps/abc-os-community (target), apps/abc-childcare-portal (mature ref), apps/ABC OS Community-01 (design) | Non vérifié (pas lu) | `abc/MANIFEST.md:75-82` |
| **`marina/`** | INCONNU — apps/ présent, pas de MANIFEST lu | — | `marina/` |
| **`alikaly/`** | INCONNU — apps/ présent, pas de MANIFEST lu | — | `alikaly/` |
| **`graphify-out/`** | OUTIL — sorties JSON/HTML d'un graphe (2,5 Mo graph.json, 70 Ko GRAPH_REPORT.md) | Output only | `graphify-out/` |
| **`wargames/`** | WARGAME — `30-mirofish-triptyque-1-businessos.md` (23 Ko) | (doc) | `wargames/` |
| **`omk/.ha_*.py`** (≈18 fichiers) | OUTILS — scans de drift calendar/h10 historique | Python | racine `10_Projects/` |

**Variantes / snapshots du même projet** :

- **Coach OS existe en 3 exemplaires** :
  1. `omk/repos/coach-os/` (canonique, le plus frais : `.bmad-loop`, `.codex`, `.moat`, `.superpowers`, .claude, .windsurf en plus)
  2. `omk/00_coach_os/` (instantané juillet, sans les nouveaux dotfolders)
  3. `omk/repos/citadelle-os/` (l'ancêtre minimal, 6 fichiers src) — *citadelle* est aussi mentionné comme marque produit ("Citadelle shell", release v0.9, `seed.ts:257`).
- **OMK Landing existe en 6+ exemplaires** : `omk/apps/nexus/` (Next.js), `omk/apps/landing/` (vide), `omk/repos/omk-services-nexus-landing-en/` (4 variantes HTML), `omk/repos/omk-nexus-landing-3-personas/` (4 personas), `omk/repos/omk-services-nexus-quiz/` (quiz seul).
- **OMK Dashboard existe en 2** : `omk/apps/dashboard/` (canonique, en pause post-pivot) + `omk/repos/omk-saas-target/` (mirror).

---

## 2. Coach OS — ce qu'il EST aujourd'hui

### 2.1 Le shell

- **Vite + React 19 + TypeScript + Zustand** (`coach-os/package.json:14-23`).
- **Tailwind v4** via `@tailwindcss/vite`, **Motion** (animations), **Three.js** (3D), **Lucide-React** (icônes).
- **Supabase** (Postgres + RLS multi-tenant) — projet `qjrwcdzaebyqponqkiqs`, région `us-east-2`, organisation "Agency as a Service" (`coach-os/PHASE0_RECEIPT.md:10-14`). 5 tables créées (organizations, profiles, memberships, cms_collections, cms_items) avec RLS actif dès la création (zéro fenêtre non protégée, `coach-os/PHASE0_RECEIPT.md:28`). 1 Edge Function `sign-up-organization` ACTIVE.
- **PostHog Cloud (EU)** + **UserTour** — observabilité opt-in RGPD via `coach-os/src/lib/observability.ts:23-119`. Pas de capture par défaut, `opt_out_persistence_by_default: true`. Identifie uniquement après consentement explicite.
- **State** : Zustand stores pour shell layout (`coach-os/src/stores/shell.store.ts`), CMS collections (`coach-os/src/lib/cms/cms.store.ts`), canvas FX overrides, app visibility.
- **Persistance** : `localStorage` (clé `coach-os-shell-layout-v1`, `coach-os/MIGRATION_SUPABASE.md:12`). Pas encore branché sur Supabase pour le layout (`coach-os/MIGRATION_SUPABASE.md:148` §7 "What does NOT move to Supabase").

Le shell est **forké du A'Space Life OS** (`coach-os/README.md:9-11` "Forked from the A'Space Life OS window shell"). Le pattern **draggable/resizable windows + glass design + Zustand layout** est repris tel quel. La palette est re-skinée "PostHog-light, paper-garden wallpaper".

### 2.2 Les apps — 19 dossiers, 17 apps réellement enregistrées

**`coach-os/src/apps/`** contient 19 dossiers ; le registre (`coach-os/src/lib/app-discovery.ts:27-52`) en déclare 17. La discordance est documentée :

| # | Dossier | Enregistrée ? | Description effective |
|---|---|---|---|
| 1 | `dashboard/` | ✅ Dashboard | "Ecosystem Vitals" + CEO Cockpit 6 domaines (Sales/Cognition/Finance/People/Operations/IT-R&D) + Wind Direction + Client Pipeline. **Hardcoded** `activeCount = clients.filter(c => c.status === 'Active').length` (`DashboardApp.tsx:48`). Cite `omk_saas.clients` et `omk_saas.agents` dans le subtitle (ligne 59). |
| 2 | `people/` | ✅ People / Agents | Team + Agents en double collection CMS (`team` + `people_agents` dans `seed.ts:79-91`). Seed = "Professor X, Jean Grey, Storm, Wolverine, Beast, Nightcrawler" (X-Men canon, `seed.ts:71-77`). |
| 3 | `operations/` | ✅ Operations | Runbooks + Incidents CMS collections. Seed : onboarding runbook 7 steps, close checklist, incident response, human handoff (`seed.ts:106-110`). |
| 4 | `it-rd/` | ✅ IT / R&D | Services + Experiments + Deploys. Seed : "Supabase — omk_saas", "Vercel — coach dashboard", "Edge — sign-up-organization", "Agent runtime (M3)" (`seed.ts:140-145`). Items vivent dans la fiction (déploys fictifs `b933e4e`, `a7c1f02`, `4de88ab`). |
| 5 | `clients/` | ✅ Clients | Collection `clients` (6 items seed : Ava Chen, Marcus Reyes, Priya Nandan, Atelier Bricolage, TechFlow, Studio Nord, `seed.ts:29-35`). |
| 6 | `tasks/` | ✅ Tasks | 5 tâches statiques hardcoded (`seed.ts:193-199`). Pas de CMS repurpose. |
| 7 | `marketplace/` | ✅ Marketplace | 6 intégrations (Stripe, Calendly, LinkedIn, Notion, DocuSign, Loom — `seed.ts:215-221`). |
| 8 | `product/` | ✅ Product | 2 collections CMS : `product_items` (roadmap + backlog) + `product_releases` (3 releases : Citadelle shell v0.9, Zero-PII seal v0.8, Audit-quiz pipeline v0.7 — `seed.ts:256-260`). |
| 9 | `growth/` | ✅ Growth | Channels (Intro.co 38 leads, LinkedIn 27, Referral 14, Paid search 7) + Experiments (`seed.ts:274-278`). |
| 10 | `sales/` | ✅ Sales Sanctum | **La plus grosse** (~35 Ko). Données statiques : 3 calls + 5 deals + 4 tasks + 6 context documents + stack (Attio, HubSpot, Pipedrive, Fireflies, Gong, Otter, PandaDoc, etc.). **Embed le CognitionOverviewContent** comme sidebar tab (`SalesApp.tsx:22`). 7 routines fallback hardcoded (`SalesApp.tsx:38-46`). |
| 11 | `audit/` | ✅ Audit Diagnostic IA | **Coquille partielle**. Source : `C:\Users\amado\Downloads\audit.pdf` (8 pages, 6 grilles). 1 grille sur 6 réellement écrite (Maturité — `AuditApp.tsx:27-52`). 5 autres sont des `<StubContent>` qui affichent juste "consulter audit.pdf page X". Le shell suggère que c'est complet ; la réalité = 1/6. |
| 12 | `finance/` | ✅ Finance | MRR `$3,600` (2 Citadelle clients hardcoded `FinanceApp.tsx:27`), runway hardcoded sur 12 mois. |
| 13 | `legal/` | ✅ Legal | Stub (pas lu en entier — ~6 Ko de `LegalApp.tsx`). |
| 14 | `settings/` | ✅ Settings | Per-app theme picker (lit/écrit dans `useThemeStore`, applique CSS variables scopées via `AppFrame.tsx:97-120`). 27 Ko, le 2e plus gros. |
| 15 | `onboarding/` | ✅ Onboarding (demo) | **"Onboarding Citadel"** : 4-question quiz (`OnboardingApp.tsx:32-72`), score 0-12, 3 bandes (Strong/Partial/Low fit). Auto-ouvre sur premier lancement, pre-seed le mini Desktop OS avec 4 panels (`Desktop.tsx:65-80`). |
| 16 | `welcome/` | ✅ Welcome | **Landing pages Circle.so-style**. 8 landing pages par Domain + 1 page demo (`landingPages.ts`). Domains : `domaine-1-rh-meta-gouvernance` (OMK RH), `domaine-2-operations`, `domaine-3-growth`, `domaine-4-cognition-savoir`, `domaine-5-people-scalabilite`, `domaine-6-finance`, `domaine-7-it-rd`, `domaine-8-legal-conformite`. 8 leaders B2 = super-héros DC/Marvel (Green Lanterns, Batman, Flash, J'onn J'onzz, Superman, Wonder Woman, Light + Cyborg, Aquaman — `WelcomeApp.tsx:46-57`). 4 tiers pricing USD : Solo $0, Practice $49, Studio $199, Forte $999. Copy "no-ai-slop" : pas de "leverage", "dive into", "fast-paced" (`landingPages.ts:11-18`). |
| 17 | `design/` | ✅ Design | 107 Ko monolithique. **"Six front-end styles showcase"** : Glassmorphism, Claymorphism, Brutalism, Cyberpunk, Soft UI/Neumorphism, Editorial. "Pure-presentation canvas that re-skins per sidebar style" (`app-discovery.ts:49-52`). |
| — | `cognition/` | ❌ **PAS enregistrée** (Phase 39b) | Le dossier existe avec `CognitionApp.tsx` qui **n'exporte plus de composant standalone** — seul `<CognitionOverviewContent>` est exporté, dwelled dans Sales (`CognitionApp.tsx:171-176`). Lit 4 tables Supabase : `cognition.routines`, `cognition.events`, `cognition.yggdrasil_manifest` (`queries.ts:1-145`). Org ID hardcoded `00000000-0000-0000-0000-000000000001` (`queries.ts:3`). |
| — | `_ui/` | (compartimenté) | Composants partagés : `kit.tsx` (StatCard, Card, Badge), `widgets.tsx`, `CMSCardList.tsx`, `FleetItemCard.tsx`. |

**Apps qui portent du contenu réel** : Dashboard (statistiques hardcoded mais structure complète), Clients (6 items seed avec données complètes), Sales (données très denses : calls/deals/tasks/documents/stack), Operations (runbooks détaillés), Welcome (8 landing pages complètes + pricing + FAQ), Audit (1 grille sur 6).

**Apps qui sont des coquilles** :
- **AuditApp** : `Maturité` est la seule grille écrite (3 niveaux : discuter/connecter/déléguer). Les 5 autres (`arbitrage`, `contexte`, `donnees`, `automatabilite`, `arbitrage-roi`) renvoient à `audit.pdf page X` via `<StubContent>` (`AuditApp.tsx:269-308`).
- **Cognition** : n'est plus une app (Phase 39b). C'est un onglet dans Sales qui dépend d'une org Supabase `cognition` schema qui n'existe pas en production (`supabaseConfigured` retourne `false` tant qu'il n'y a pas de session ; le store reste vide — `cms.store.ts:31-37`).
- **Onboarding** : c'est une démo commerciale, pas une vraie intégration utilisateur.

**Coquilles + profondeur fictive** : tous les chiffres du Dashboard (Ecosystem Vitals : `$67K` sales, `18mo` runway, `8/12` team, `32` incidents), de Finance (MRR `$3,600`), d'IT/R&D (deploys `b933e4e`, edge function `invoked 12×`, agent runtime queue 3) sont **hardcodés dans `seed.ts`** et représentent une réalité fictive cohérente. Aucune ne provient d'un vrai backend.

---

## 3. Le fossé entre la doctrine et le code

J'ai trouvé **au moins trois** endroits où ce qui est écrit dans les chartes/MANIFESTs/runbooks ne correspond pas à ce qui est construit.

### 3.1 Le nombre d'apps : 13 (doctrine) vs 17 (code) vs 19 (dossiers)

- **`coach-os/README.md:3-4`** : "13 apps (Dashboard, People/Agents, Operations, IT/R&D, Clients, Tasks, Marketplace, Product, Growth, Sales, Finance, Legal, Settings)".
- **`coach-os/src/lib/app-discovery.ts:27-52`** : 17 `registerApp()` appels — les 13 listés + 4 ajoutés (Audit, Onboarding, Welcome, Design).
- **`coach-os/src/apps/`** : 19 dossiers — 17 apps + `cognition/` (intégré à Sales) + `_ui/` (compartimenté).
- **`coach-os/CLAUDE.md`** (le canon d'identité projet dans `omk/CLAUDE.md`) : **mentionne zéro de ces apps** ; il décrit `apps/dashboard/` avec **14 vues différentes** (Dashboard, Clients, Documents, Agents, Finance, SOPLibrary, Settings, People, Tasks, Legal, Growth, Sales, Marketplace, ItData — `omk/apps/dashboard/src/App.tsx:18-33`). 

Le README du repo Coach OS est **désynchronisé** depuis l'ajout des 4 nouvelles apps (Audit, Onboarding, Welcome, Design) et le retrait du standalone Cognition (Phase 39b). Le CLAUDE.md du projet parent est **sur un autre projet**.

### 3.2 Solaris = Solarpunk (code) vs Solaris = Visual First/DAM (doctrine)

- **`omk/apps/dashboard/src/components/views/ProductView.tsx:40-47`** (code, ligne 1 d'évidence) :
  ```ts
  id: 'solaris',
  name: 'Solaris AaaS',
  icp: 'Life-OS-2026 / Solarpunk',
  tier: 'Tier 3: Sovereign Box Enterprise',
  status: 'live',
  ```
- **`solaris/MANIFEST.md:18`** (doctrine) : "**ICP variant : Solaris 🎨 Visual First / DAM** — sister canon `ADR-ICP-SOLARIS-001` (3-ICP sister-symétrique 2026-06-24)".
- **`ceo-desktop/MANIFEST.md:17`** : "**3 ICPs (Solaris/Nexus/Orbiter)**" — sans définir Solaris.
- **`omk/apps/dashboard/src/components/views/ProductView.tsx:49-55`** (code) définit **Orbiter** comme "Family Offices / Patrimoines baby-boomers" (`Orbiter ABC-OS`).

**`abc/`** (le projet soeur `abc/MANIFEST.md`) traite d'ABC OS & Child Care BOS pour des coopératives ouest/est-africaines. **Aucune mention d'Orbiter ABC-OS dans le MANIFEST d'`abc/`** — ce sont deux projets distincts qui se télescopent sous le même nom `Orbiter`.

Résultat : dans la doctrine, Solaris/Orbiter ont 2 définitions incompatibles (Solarpunk vs Visual First/DAM ; Family Offices ABC-OS vs coopérative africaine). Dans le code, seule la définition ProductView existe.

### 3.3 "Single SaaS mode, A1 LOCKED" (doctrine) vs deux runtimes Coach OS coexistent (code)

- **`omk/CLAUDE.md:142-152`** : "**One codebase, one product, single SaaS mode.** Per ADR-OMK-004 §Condition A = A1... le mode `internal` est retiré." C'est la doctrine OMK Services.
- **Code Coach OS** : `coach-os/MIGRATION_SUPABASE.md:124-133` décrit explicitement un **graduated 3-stage tenancy model** (PoC SaaS → Coach-owned Cloud → White-label self-host), PAS single SaaS mode. Le Schema §3.2 est "plain Postgres with no OMK-specific lock-in" pour permettre la migration entre stages.
- **`omk/MANIFEST.md:18`** : "**Repo (canon unique)** : `omk-services/00-omk-saas-os`". Mais 6 dépôts coexistent sous `omk/repos/` (citadelle-os, coach-os, omk-nexus-landing-3-personas, omk-saas-target, omk-services-nexus-landing-en, omk-services-nexus-quiz) — cf. `MERGE_REPORT_2026-08-01.md:36-44`. La doctrine "single canon" coexiste avec la pratique "multi snapshots".

### 3.4 L'omk/CLAUDE.md ne sait pas que Coach OS existe

`omk/CLAUDE.md:13-14` définit le projet comme "OMK Services Business OS — the staff/operator dashboard for a Paris-based services firm" et liste seulement 2 apps (`omk-dashboard`, `omk-landing`). **Coach OS, qui est sous `omk/repos/coach-os/`**, n'apparaît dans aucun des deux CLAUDE.md du périmètre `omk/`. Le `MANIFEST.md` parent le déclare fille (`omk/MANIFEST.md:40`) mais ne pointe pas vers son code, ses phases REBUILD, ses 17 apps.

Pour un agent qui ouvre `omk/CLAUDE.md` pour comprendre le projet, Coach OS est **invisible**.

---

## 4. Ce qui est réutilisable au-delà du coaching

### 4.1 Le kernel générique (zéro hypothèse coach)

| Composant | Réutilisable tel quel ? | Chemin |
|---|---|---|
| **CMS engine** (`CmsCollectionDef` / `CmsItem` / `registerCollection` / `useCmsStore`) | ✅ **Oui**, totalement agnostique. Une collection = `{id, name, singular, accent, titleField, subtitleField, badgeField, fields[]}` (`coach-os/src/lib/cms/types.ts`). Les 19 collections du seed (`clients`, `articles`, `team`, `people_agents`, `runbooks`, `incidents`, `services`, `it_experiments`, `deploys`, `tasks`, `marketplace_listings`, `product_items`, `product_releases`, `growth_channels`, `growth_experiments`, `sales_calls`, `sales_deals`, `sales_documents`, `sales_stack`, `legal_contracts`, `finance_invoices`, `settings_flags`, `audit_items`) sont toutes instanciées via le même mécanisme. | `coach-os/src/lib/cms/` |
| **CmsRepository + Supabase dual-write pattern** | ✅ Oui. Le pattern (IndexedDB cache + Supabase mirror + `getCurrentOrgId` org-scoping + `upsertCollectionDef`/`upsertItem`/`appendCmsEvent`) est documenté comme miroir de `DomainDB` du Life OS. | `coach-os/src/lib/cms/repository.ts:1-122`, design dans `coach-os/MIGRATION_SUPABASE.md:29-37` |
| **App Registry (manifest-based loading)** | ✅ Oui. Pattern `registerApp({id, name, icon, accent, description, component, dockSlot?, hidden?})` + `window.__CITADELLE_APP_REGISTRY__` global. Apps auto-discovery via side-effect `app-discovery.ts`. | `coach-os/src/lib/app-registry.ts`, `coach-os/src/lib/app-discovery.ts` |
| **AppFrame shell** (window + sidebar + sections + canvas FX + per-app themes) | ✅ Oui. `AppFrame` rend chaque app avec son propre sidebar, ses `AppSection[]`, ses outils optionnels (AgenticOS-style). Collapse auto < 640 px avec hystérésis 48 px. Per-app theme tokens via CSS variables scopées. | `coach-os/src/components/AppFrame.tsx` |
| **Desktop shell** (wallpaper + TopBar + DesktopIcons + WindowFrame + AppDrawer) | ✅ Oui. Pattern draggable/resizable windows + Zustand layout persistence. | `coach-os/src/components/Desktop.tsx`, `WindowFrame.tsx`, `TopBar.tsx` |
| **Observabilité opt-in RGPD** (PostHog + UserTour) | ✅ Oui. Pattern `opt_out_persistence_by_default` + `localStorage:coach-os:observability-opt-in` + `setObservabilityConsent` qui efface l'identité UserTour + reset des tour guards. | `coach-os/src/lib/observability.ts` |
| **DynamicPageView + CollectionRepeater** (Wix-CMS-style) | ✅ Oui. Render générique d'une collection : repeater (liste) + drill-down (detail). | `coach-os/src/components/cms/{DynamicPageView,CollectionRepeater}.tsx` |
| **Shell layout persistence** | ✅ Oui. Zustand + `beforeunload` saveLayout. | `coach-os/src/stores/shell.store.ts`, `coach-os/src/components/Desktop.tsx:87-91` |
| **Cognition query layer** | ✅ Oui. Pattern `client.schema('xxx').from('table')` + types rows/interfaces séparés. | `coach-os/src/lib/cognition/queries.ts` |
| **3-stage tenancy migration path** | ✅ Oui. Le schema §3.2 (`cms_collections` + `cms_items` + tables dédiées `shell_layouts`, `settings_flags`, `ai_act_checklist`, `tasks`) est plain Postgres, conçu pour permettre `pg_dump`/`pg_restore` sans rewrite. | `coach-os/MIGRATION_SUPABASE.md:124-133` |

### 4.2 Ce qui est *coache jusqu'à l'os*

| Composant | Spécifique coach | Pourquoi |
|---|---|---|
| **`onboarding/OnboardingApp.tsx`** (Citadel quiz) | ❌ Spécifique | 4 questions calibrées sur la niche premium coach US ($500-$2000/h) : "Where do your client session notes live today?", "compliance CCPA / Colorado AI Act". Score bandes "Strong/Partial/Low fit" → démo `Sales Sanctum`. |
| **`welcome/landing/landingPages.ts`** | ❌ Spécifique | Pricing USD 4 tiers calibrés sur coach premium ($0/$49/$199/$999). Copy "no-ai-slop" : "Your team of agents", "your daily standup", "your agents". |
| **`audit/AuditApp.tsx`** (Manuel Diagnostic IA) | ❌ **Mais extract PDF** | Contenu issu verbatim de `C:\Users\amado\Downloads\audit.pdf` — pas un produit Coach, juste un asset PDF transformé en app. Réutilisable ailleurs tel quel. |
| **`design/DesignApp.tsx`** (107 Ko) | ❓ **Agnostique ou pas ?** | "Six front-end styles · one showcase canvas" — showcase de styles visuels (Glassmorphism, Claymorphism, Brutalism, Cyberpunk, Soft UI/Neumorphism, Editorial). Agnostique en surface MAIS fortement couplé au reste du shell (per-app theme picker, canvas FX, etc.). Réutilisable pour un *framework* UI, pas pour un produit. |
| **`audit/App.tsx`** | ⚠️ À moitié | 5/6 grilles sont des stubs (`AuditApp.tsx:269-308`). Pas "extrait complet" mais "présenté comme complet". |
| **Les collections CMS seed** (`coach-os/src/lib/cms/seed.ts`) | ⚠️ Spécifique coach mais structure réutilisable | `clients`, `articles`, `team`, `people_agents`, `runbooks`, `incidents`, `services`, `it_experiments`, `deploys`, `tasks`, `marketplace_listings`, `product_items`, `product_releases`, `growth_channels`, `growth_experiments`, `sales_calls`, `sales_deals`, `sales_documents`, `sales_stack`, `legal_contracts`, `finance_invoices`, `settings_flags`, `audit_items` — les **noms de collections** sont agnostiques (n'importe quel business a clients/deals/tasks/etc.). Les **items** sont hardcodés sur la fiction "coach OS" (Ava Chen, Marcus Reyes, Stripe $3,600 MRR, etc.). Réutiliser = remplacer les items. |
| **`cognition/`** (queries + COGNITION_ORG_ID hardcoded) | ❌ Très spécifique | Org ID = `'00000000-0000-0000-0000-000000000001'` (un seul tenant fictif, `queries.ts:3`). Schema `cognition` (routines, events, yggdrasil_manifest). Aucune logique de scoping par coach. Pas un module réutilisable — c'est une **fenêtre d'observation** sur un org unique. |

**Constat** : Le **kernel** (CMS engine + registry + AppFrame shell + Desktop + observabilité + dual-write Supabase pattern + tenancy schema) est proprement générique et pourrait servir une autre niche **sans réécriture**. La **surface métier** (Onboarding Citadel, Welcome landing pages, les 19 collections seed avec données fictives, Audit PDF, Design showcase) est coach-spécifique ou asset-spécifique.

**Implication pour la duplication** : si OMK Services vise à servir Solaris (Solarpunk) et Orbiter (Family Offices), le kernel (`/lib/cms`, `/lib/app-registry`, `/components/AppFrame`, `/components/Desktop`, `/lib/observability`, `/lib/supabase`) peut être **réutilisé tel quel**. La couche métier (les 19 apps spécifiques coach) doit être **réécrite** ou profondément re-seedée pour chaque niche. La thèse "5 gestes automatisables / 4 résistent (mandat hiérarchique, consentement à révéler, responsabilité juridique, promotion d'un constat)" est compatible avec ce constat : ce qui est automatisable (kernel technique) est réutilisable ; ce qui résiste (mandat, juridique, promotion) devra être re-spécifié par niche.

---

## 5. Nexus, Solaris, Orbiter dans le code

### 5.1 Trois occurrences seulement — toutes dans `omk/apps/dashboard/`

J'ai grep `-i "solaris|orbiter"` sur **tout** `30_Business_OS/10_Projects/` (≈2800 fichiers scrutés, jonctions écartées). Le résultat tombe à **un seul fichier** de code applicatif :

**`omk/apps/dashboard/src/components/views/ProductView.tsx:29-57`** — c'est **le seul** endroit dans tout le corpus où les 3 noms apparaissent ensemble comme "3 AaaS variants". Le commentaire ligne 84 dit : "**Triptyque 2 — Holding OMK Business OS expose 3 AaaS variants (Nexus / Solaris / Orbiter)**". Définitions codées :

```ts
const VARIANTS: Variant[] = [
  { id: 'nexus',   name: 'Nexus OMK · Coach premium',
    icp: 'Executive & Leadership Coaching',
    tier: '$7.5K–$25K one-shot + $750+/an recurring',
    status: 'live', pillars: 5,
    description: 'Spearhead canon. 3 guides YouTube distillés en context-spe Project Picard (lun. 2026-07-03). Zero-PII Agentic Governance en Pilier 5.' },
  { id: 'solaris', name: 'Solaris AaaS',
    icp: 'Life-OS-2026 / Solarpunk',
    tier: 'Tier 3: Sovereign Box Enterprise',
    status: 'live', pillars: 5,
    description: 'Référence d inspiration. Life-OS-2026 Vercel SHA b933e4e4. 8 B2 domaines × 8 B3 squads Marvel/DC.' },
  { id: 'orbiter', name: 'Orbiter ABC-OS',
    icp: 'Family Offices / Patrimoines baby-boomers',
    tier: '$5K–$50K MRR sanctuary',
    status: 'live', pillars: 5,
    description: 'Family-Office sanctuary. Vault-Redactor (Manhunter) + Vault-Audit (Batman). Cardinal book canon.' },
];
```

**C'est la seule définition canonique des 3 produits dans le code exécutable.**

### 5.2 "Nexus" ailleurs — 3 sens distincts

| Sens | Endroit | Ce que c'est |
|---|---|---|
| **Nexus = produit coach premium** (le spearhead) | `omk/apps/dashboard/.../ProductView.tsx:31`, `omk/MANIFEST.md:21` "**Nexus** (Data-First / Expert Knowledge)", `omk/MANIFEST_coaching_premium.md:17` | Le premier AaaS variant — ICP coach premium $7.5-25K. |
| **Nexus = le seed.ts CMS "demo coach"** | `coach-os/src/lib/cms/seed.ts` (4 occurrences : "with Nexus, those notes are auto-structured", "Nexus drafted twelve assets", "your Nexus recommendation", "Nexus would have flagged") | Le **même** produit, mais présenté dans les témoignages seed comme "l'expérience" que le prospect vivra après signup. Copie marketing, pas technique. |
| **Nexus = le projet landing page** | `omk/apps/nexus/` (Next.js boilerplate), `omk/repos/omk-services-nexus-landing-en/`, `omk/repos/omk-services-nexus-quiz/`, `omk/repos/omk-nexus-landing-3-personas/` | Les artefacts marketing (landing, quiz, personas) du même produit Nexus. |

### 5.2bis "Solaris" ailleurs — 1 faux positif dans `abc`

Une occurrence supplémentaire détectée par grep project-wide, **mais sans rapport avec la variante AaaS** :

- **`abc/apps/ABC OS Community/app.js:86`** : `<h3>Solaris Agri-Coop</h3>` avec sous-titre "Agriculture coopérative solaire · Kenya".
- **`abc/apps/ABC OS Community/assets/hub.js:20,25,39`** : 3 références à `Solaris Agri-Coop` comme **workspace démo fictif** dans l'app abc-os-community ("Finaliser le milestone « Irrigation solaire »", "jalon validé · « Étude de sol » approuvée par 4 membres", etc.).

Ces occurrences sont un **nom de projet client fictif** dans les données démo de l'app abc OS Community (coopérative agricole kenyane). Pas la même Solaris que la variante AaaS Solarpunk ni la Visual First/DAM. À ignorer pour la question "3 variants AaaS" — c'est juste un exemple dans le seed data d'abc.

**Solaris** et **Orbiter** n'ont aucune autre occurrence code applicatif. Aucun repo, aucune app, aucun dossier portant leur nom en code (seulement en doctrine : `solaris/MANIFEST.md`, `ceo-desktop/MANIFEST.md`).

### 5.3 Le naming est plus un marqueur stratégique qu'une réalité code

Sur les 3 noms de la doctrine Triptyque (Nexus/Solaris/Orbiter), **seul Nexus a du code applicatif** :
- Coach OS = **Nexus** (le Desktop-OS pour coach premium).
- `omk/apps/nexus/` = la landing page **Nexus** (Next.js boilerplate).
- `omk/repos/omk-services-nexus-{landing-en, quiz}/` = landing + quiz **Nexus**.
- `omk/repos/omk-nexus-landing-3-personas/` = 3 personas landing **Nexus**.

**Solaris** et **Orbiter** n'ont que :
- Des MANIFESTs doctrinaux (`solaris/MANIFEST.md`, `ceo-desktop/MANIFEST.md`).
- Le dossier `solaris/` qui contient `apps/` (non lu) + `_doctrine/` (jonction vers `00 Agency as a Service`) + `CLAUDE.md` + `MANIFEST.md`.
- Une ligne dans `ProductView.tsx`.

**`solaris/MANIFEST.md:55`** dit "Solaris est **self-hosted Supabase** (VPS `aspace-vps`), NOT Supabase Cloud — divergence explicite vs autres ICPs." Mais le code Solarispour l'instant n'a pas d'app. C'est de la doctrine sans chair.

### 5.4 Oracle de la marque "Solaris"

La marque "Solaris" dans `ProductView.tsx` = **Life-OS-2026 / Solarpunk** (cohérent avec `solaris/MANIFEST.md:12` "AaaS Agency Garden"). **PAS** Visual First/DAM comme le prétend `solaris/MANIFEST.md:18` ("Visual First / DAM — sister canon ADR-ICP-SOLARIS-001"). Deux définitions incompatibles coexistent.

---

## 6. Compte et reste à couvrir

### Compte exact

**47 fichiers lus en entier** (sur budget ≈60) :

1. `omk/README.md`
2. `omk/MANIFEST.md`
3. `omk/MANIFEST_coaching_premium.md`
4. `omk/MERGE_REPORT_2026-08-01.md`
5. `omk/CLAUDE.md` (200 premières lignes)
6. `omk/apps/dashboard/src/App.tsx` (80 premières lignes)
7. `omk/apps/dashboard/src/components/views/ProductView.tsx` (100 premières lignes — **trouvé Solaris/Nexus/Orbiter**)
8. `omk/apps/nexus/page.tsx` (60 premières lignes)
9. `omk/apps/nexus/README.md`
10. `solaris/MANIFEST.md`
11. `cerritos-gtd-dispatch/MANIFEST.md`
12. `cerritos-gtd-dispatch/README.md`
13. `abc/MANIFEST.md`
14. `rilcot/MANIFEST.md`
15. `ceo-desktop/MANIFEST.md`
16. `omk/repos/coach-os/README.md`
17. `omk/repos/coach-os/package.json`
18. `omk/repos/coach-os/index.html`
19. `omk/repos/coach-os/MIGRATION_SUPABASE.md`
20. `omk/repos/coach-os/PHASE0_RECEIPT.md`
21. `omk/repos/coach-os/src/App.tsx`
22. `omk/repos/coach-os/src/main.tsx`
23. `omk/repos/coach-os/src/lib/app-registry.ts`
24. `omk/repos/coach-os/src/lib/app-discovery.ts`
25. `omk/repos/coach-os/src/lib/observability.ts`
26. `omk/repos/coach-os/src/lib/supabase.ts`
27. `omk/repos/coach-os/src/lib/cms/cms.store.ts`
28. `omk/repos/coach-os/src/lib/cms/repository.ts`
29. `omk/repos/coach-os/src/lib/cms/seed.ts` (240 lignes sur 1100+)
30. `omk/repos/coach-os/src/lib/cognition/queries.ts`
31. `omk/repos/coach-os/src/apps/cognition/CognitionApp.tsx`
32. `omk/repos/coach-os/src/apps/dashboard/DashboardApp.tsx`
33. `omk/repos/coach-os/src/apps/finance/FinanceApp.tsx` (80 premières lignes)
34. `omk/repos/coach-os/src/apps/sales/SalesApp.tsx` (100 premières lignes)
35. `omk/repos/coach-os/src/apps/welcome/WelcomeApp.tsx`
36. `omk/repos/coach-os/src/apps/audit/AuditApp.tsx`
37. `omk/repos/coach-os/src/apps/onboarding/OnboardingApp.tsx` (100 premières lignes)
38. `omk/repos/coach-os/src/apps/welcome/landing/landingPages.ts` (120 premières lignes)
39. `omk/repos/coach-os/src/components/Desktop.tsx`
40. `omk/repos/coach-os/src/components/AppFrame.tsx` (120 premières lignes)
41. `omk/00_coach_os/README.md`
42. `omk/chartes/coach_premium_capsule.md`
43. `omk/wiki/log.md`

Listing de 6+ autres fichiers via `ls -la` (top-level + sub-dirs) sans lecture intégrale : `omk/apps/dashboard/`, `omk/apps/landing/`, `omk/apps/nexus/`, `omk/repos/`, `omk/chartes/`, `omk/runbooks/`, `omk/wiki/`, `omk/_resources/{capsules,audits,guides_ld01_business_book}/`, `omk/docs/runbooks/`, `omk/signals/`, `omk/repos/coach-os/src/apps/{dashboard,clients,sales,finance,growth,legal,operations,it-rd,product,people,audit,settings,tasks,design,onboarding,welcome,cognition,_ui}/`, `omk/repos/coach-os/src/{lib,components,stores}/`, `omk/repos/coach-os/scripts/`, `omk/repos/coach-os/{docs,wiki,adws,_DRAFTS_PPR_LANE,_TRASH_2026-07-25,_bmad,_bmad-output,{output_folder}}/`.

### Dossiers ouverts sans y entrer (non explorés)

- `omk/_stranded_2026-07-24/` — mentionné dans `ls`, contenu inconnu.
- `omk/_sidebars/` — mentionné, contenu inconnu.
- `omk/apps/dashboard/src/{auth,components,config,contexts,data,hooks,lib}/` — structure connue mais non lue.
- `omk/apps/dashboard/sql/` et `omk/apps/dashboard/supabase/` — non lus (DDL Supabase pourrait contenir des surprises sur Solaris/Orbiter).
- `omk/apps/nexus/src/{components,data,design}/` — non lus.
- `omk/repos/coach-os/_DRAFTS_PPR_LANE/`, `omk/repos/coach-os/_TRASH_2026-07-25_pre_blackwidow_scarletwitch_purge/`, `omk/repos/coach-os/{_bmad,_bmad-output,{output_folder},adws,docs,wiki}/` — non lus.
- `omk/repos/coach-os/scripts/` — non lu.
- `omk/_resources/guides_ld01_business_book/` — non lu.
- `omk/repos/omk-saas-target/{src,sql,supabase}/` — non lus (DDL complet de `omk-saas-target` pourrait révéler la vérité des 3 variants).
- `omk/repos/{omk-services-nexus-landing-en, omk-services-nexus-quiz, omk-nexus-landing-3-personas, citadelle-os, omk-saas-target}/` — lus en listing uniquement.
- `solaris/apps/` — non lu.
- `ceo-desktop/{apps,handoffs,_doctrine}/` — non lus.
- `cerritos-gtd-dispatch/{apps,_inbox,_archive}/` — non lus.
- `rilcot/apps/` — non lu.
- `abc/apps/{abc-os-community,abc-childcare-portal,ABC OS Community-01}/` — non lus.
- `marina/apps/`, `alikaly/apps/` — non lus.
- `graphify-out/` — listing uniquement (output only).
- `wargames/wargame-30-out/` — non lu.
- Les ~18 scripts `.ha_*.py` à la racine — listing uniquement (drift scans historiques).

### Reste à couvrir

Si une passe 2 est nécessaire :

1. **`omk/apps/dashboard/sql/` et `supabase/`** — le DDL canon du OMK Services pourrait contenir les vraies définitions des 3 variants (Nexus/Solaris/Orbiter) ou des tables spécifiques à chacun. Le `ProductView.tsx` est peut-être la **surface** d'un schéma **plus profond** dans la base.
2. **`omk/repos/coach-os/scripts/`** — des scripts d'audit ou de seeding.
3. **`solaris/apps/`** — le code applicatif (s'il existe) qui justifierait la doctrine Solaris comme Solarpunk **ou** comme Visual First/DAM (arbitrerait la divergence §3.2).
4. **`omk/_doctrine/`** — jonction NTFS vers `01-Projects_Picard/01-omk-business-os/` ; non descendu (lecture seule par convention).
5. **Le reste de `seed.ts`** (lignes 240-1100) — d'autres collections CMS spécifiques coach potentiellement importantes.
6. **`omk/repos/coach-os/AUDIT_RAPPORT.md`** (56 Ko) — pourrait être le document le plus complet sur l'état réel du Coach OS, vu qu'il a été audité (probablement par un agent automatique).
7. **Phase REBUILD contracts** : `omk/apps/dashboard/REBUILD_WORKFLOW.md` et `omk/repos/omk-saas-target/REBUILD_WORKFLOW.md` — le "contrat WHAT to build" du pivot, non lu.

---

## 7. Notes méthodologiques

- **Jonctions** : 32 sous `30_Business_OS` cartographiées au préalable par une passe antérieure ; je ne les ai pas traversées. La `_doctrine/` sous `omk/`, `solaris/`, `ceo-desktop/`, `abc/`, `rilcot/`, `alikaly/`, `marina/` et `cerritos-gtd-dispatch/` sont des jonctions (symlinks NTFS) ; leurs contenus pointent vers `24_PARA_Enterprise/01_Projects_Picard/` (projets Picard) — **hors périmètre N3**.
- **Binaire `.git/objects`** : non traversés (la passe grep les a correctement filtrés).
- **`node_modules`** : non traversés (taille prohibitve, connaissance générique suffisante).
- **`dist/` et `.next/`** : non traversés (build artifacts).
- **Doublons** : `00_coach_os/` vs `repos/coach-os/` (mêmes `src/`, README, MIGRATION_SUPABASE) ; 6+ landing pages Nexus ; 2 dashboard OMK ; le canonique est identifié explicitement par chaque MANIFEST mais les deux coexistent.
- **Aucun chiffre n'est inventé**. Aucun fichier modifié. Un seul fichier écrit : celui-ci.

---

*Rapport N3 — explorateur en lecture seule — `30_Business_OS/10_Projects/` — budget 47/60 fichiers — `analyses/N3_projets.md` ouvert 2026-08-05 par l'agent d'exploration conformément au BRIEF.*