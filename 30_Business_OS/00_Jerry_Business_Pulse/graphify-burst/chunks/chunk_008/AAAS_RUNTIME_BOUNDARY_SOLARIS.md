---
source: A0_Amadeus + IT doctrine (Cyborg) + solaris-aaas repo + picard_audit_solaris + SDD-007
date: 2026-06-03
type: it_runtime_boundary
domain: L2_Business / IT / Project 00 Agency as a Service / Mode Solaris
status: DRAFT_V1
tags: [#it #cyborg #runtime #nextjs #github #dokploy #vercel #supabase #openrouter #sovereignty #picard]
---

# 🖥️ IT Runtime Boundary — Solaris AaaS

> Companion to `JTBD-001_AAAS_RUNTIME_BOUNDARY.md`. IT owns the **runtime + source of truth + tracking**; People
> owns the agent-members, IT owns the machine. Doctrine : Cyborg (infra scalable, uptime), P13 sovereignty.

## 1. Runtime réel (existant)
- **App** : Next.js 16 / React 19 / TypeScript — `…/03_Product…/01_solaris-aaas/`.
- **Repo** : **`github.com/Amdkn/00-Solaris`** (commits `81a24b2` init, `5d04494` core layout). CI/CD possible (build pipeline OK — dettes D04/D05 résolues).
- **Cible déploiement (audit)** : **Vercel** (landing, SEO/SSR) | **Dokploy bare-metal** (instance souveraine — l'angle AAA "ton propre Control Plane", ticket franchise).

## 2. Runtime à provisionner (le SaaS dashboard / l'instance Solaris)
Le produit réel (au-delà de la landing) tourne sur le stack Asset-First (SDD-007) :
| Couche | Stack | Rôle |
|---|---|---|
| Stockage assets + recherche | **Supabase Storage + Vector** | Asset Librarian (versioning, dé-doublon, pedigrees) |
| Validation visuelle | **Claude Vision API** | Art Director agent (pré-validation livrables) |
| Orchestration | **Symphony** (`printingpress.dev`, self-host headless daemon) — **remplace n8n** | poll tracker → workspace isolé/tâche → agent sous SOC/SLA → Donna DLQ |
| Modèle | **Gateway OpenRouter** (GLM-4.7-Flash / MiniMax) | model-agnostic + affordable (People PE14/PE15) |
| Contrats inter-domaines | **Master SOC Schema** (Zod) | la "douane" SOC, budget/SLA par `trace_id` |

## 2bis. Symphony remplace n8n (analyse — A0 directive)
Source : `00_Amadeus/05_OSS_Twin/symphony/` (Shadow A0, hors-canon, `printingpress.dev` spec).

| | **n8n** (rejeté) | **Symphony** (retenu) |
|---|---|---|
| Nature | Workflow engine **visuel** rigide | **Daemon headless** : scheduler + tracker-reader (pas de business logic, pas d'UI) |
| Self-host | pénible | conçu pour le self-host frugal |
| Coût modèle | — | **MiniMax 2.7 / GLM 4.7 Flash** (≈100× moins cher que Claude/GPT) — PE15 affordability |
| Exécution | nodes câblés à la main | **workspace isolé par tâche** → lance un agent (Hermes/Claude Code) → l'agent fait les writes via tooling |
| Contrats | aucun | porte nativement la **trinité SLA/SOA/SOC** (= le backbone de l'offre Solaris !) |
| Échec | retry basique | **Donna DLQ** après N retries (ADR-RICK-001) |
| Logique | dans les nodes | dans `WORKFLOW.md` repo-owned + tooling agent |

**Pourquoi c'est supérieur pour AaaS** : Symphony **est déjà** le mécanisme SOC/SLA qu'on vend (l'agence achète
un système propriétaire, pas un n8n générique). Et **des WORKFLOW Solaris existent déjà** :
`symphony/L2/WORKFLOW.solaris-clickup-ops.md` + `WORKFLOW.solaris-airtable-clients.md` → le pipeline
Brief→Concept→Production→Validation→Livraison (Ops SOP-A) se code comme un **Symphony WORKFLOW**, pas un graphe n8n.
Pyramide : **B1 Symphony Router** (lit le tracker, génère le payload SOC) → **B2 Hermes Kanban** (pipelines,
circuit breakers) → **B3 exécution** (skills→CLI via la forge Clara) → trackers (Airtable/ClickUp L2).
⚠️ Symphony reste **Shadow A0 / hors-canon SDD** (veto 90j) — c'est un outil de pilotage A0, pas un SDD promu.

## 3. Source of truth & tracking (le boundary)
- **Lead capture** : ⚠️ **D09 non résolu** — les CTA landing n'ont pas d'endpoint. IT doit livrer l'**API form** (→ Supabase + tracking) pour débloquer Growth (attribution, source-of-truth).
- **Tracking/attribution** : à brancher (Growth VOC exige une "measurement path").
- **Compute/coût** : Compute plafonné par mission (SLA) → métrique IT alimentant Finance (COGS, F4/F24).

## 4. Sécurité / souveraineté (P13 + ADR-HERMES-001 echo)
- Secrets en env (jamais en clair/commit) ; OpenRouter key, Supabase key, Stripe key.
- Loopback + reverse-proxy pour les surfaces admin (cf. topologie Hermes VPS) ; HTTPS via Caddy pour le sovereign tier.
- Uptime/MTTR = North Star IT (escalade Jerry si uptime <99% ou MTTR >1h).

## Dettes IT (audit, post-migration)
- 🟠 D09 backend form/API (bloquant business). · 🟡 D12 tests · D14 exclure TweaksPanel du bundle prod · D13 OG/manifest/favicon.

## Prochains pas
1. Livrer l'**API lead-capture** (débloque Growth).
2. Provisionner l'**instance dashboard** (Supabase + n8n + OpenRouter) — MVP Couche 0+1.
3. Pipeline CI/CD GitHub→Vercel|Dokploy + secrets management.

## Sources
- Repo/app : `01_solaris-aaas` + `picard_audit_solaris.md` (dettes D01-D14). Stack : SDD-007.
- Doctrine : `05_IT_Cyborg_KangDynasty/03_IT_PRINCIPLES_REF.md` ; souveraineté echo `ADR-HERMES-001`.
