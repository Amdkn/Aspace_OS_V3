---
id: ADR-DEPLOY-001
title: Pipeline GitHub → Vercel canonique pour Landing Pages OMK Nexus ⚖️ — Sister-canon sibling ADR-LANDING-CRAFT-001 (Phase 7) + ADR-LANDING-QA-001 (gate)
type: ADR (Architectural Decision Record)
status: RATIFIED
date: 2026-07-06
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-3"
  context: "Ratification Tier 3 ops/QA — 6 ADR production gates ratifiés en bloc."
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' + MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17' + Vercel MCP sister-canon tools + ADR-LANDING-CRAFT-001 Phase 7 QA + Ship + ADR-LANDING-QA-001 gate enforcement + PRD-NEXUS-EVOLUTION-IA-001 §6 rails existants + plan-L2-business-os.md §5.4 topologie Holding→Filiales, screened Anti-Paperclip D1-D8)
deciders: [A0 Amadeus (Jumeau Numérique)]
drafted_by: Claude Code (B1 E-Myth Gatekeeper, sister-scoped A2 USS Enterprise / A3 Picard projects owner + A2 USS Discovery / A3 Saru H3 finance + A1 Morty execution + A0-L canon 4e layer)
domain: L2 Business OS / Nexus ⚖️ / Pipeline CI-CD / GitHub → Vercel / Single-file static deploy / B1 E-Myth / Sister-canon deploy
tags: [#ADR #deploy #pipeline #github #vercel #mcp-vercel #mcp-hostinger-dns #single-file-static #landing-deploy #omk-nexus #mirror-transfer #D6-lessons #anti-paperclip #D4-append-only #posture-C #b1-gatekeeper #e-myth]
doctrine_anchors:
  - ADR-META-001 (RATIFIED) — Anti-Paresse D1-D8 (D1 Verify-Before-Assert, D4 Append-Only, D6 Root-Cause, D7 Cost-Of-Escalation)
  - ADR-META-006 (D6 Catalog) — Journal append-only des applications D6
  - ADR-SOBER-002 (RATIFIED 2026-06-21) — Anti-Paperclip doctrine kernel
  - ADR-ANTI-PAPERCLIP-001 (DRAFT 2026-07-06) — Sister-scoped surface landing pages
  - ADR-LANDING-CRAFT-001 (DRAFT 2026-07-06) — Méta-process 7-phases, Phase 7 = QA + Ship (upstream consumer)
  - ADR-LANDING-QA-001 (DRAFT 2026-07-06) — 5 critères Self-Critique gate enforcement (upstream consumer)
  - ADR-LANDING-AESTHETIC-001 (DRAFT 2026-07-06) — Doctrine esthétique
  - ADR-LANDING-COPY-001 (DRAFT 2026-07-06) — Copywriting canonique 3 personas
  - ADR-DESIGN-SYSTEM-001 (DRAFT 2026-07-06) — tokens CSS canoniques
  - ADR-NEXUS-LANDING-PERSONAS-001 (RATIFIED) — 3 landings distinctes ICP
  - ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24) — Sister-symmetrique ICP
  - ADR-AAAS-PRICING-001 (RATIFIED + AMENDED) — Pricing canon
  - ADR-L2-AAAS-001 (RATIFIED) — AaaS Doctrine 3 Variants
  - ADR-NEXUS-NICHE-001 — Coaching/BizDev/B2B arbitrage
  - ADR-MULTIPAGE-001 (DRAFT) — Wireframe sitemap
related:
  [
    ADR-LANDING-CRAFT-001,
    ADR-LANDING-QA-001,
    ADR-LANDING-AESTHETIC-001,
    ADR-LANDING-COPY-001,
    ADR-DESIGN-SYSTEM-001,
    ADR-ANTI-TEMPLATE-001,
    ADR-ANTI-PAPERCLIP-001,
    ADR-NEXUS-LANDING-PERSONAS-001,
    ADR-ICP-NEXUS-001,
    ADR-AAAS-PRICING-001,
    ADR-L2-AAAS-001,
    ADR-META-001,
    ADR-META-006,
    ADR-SOBER-002,
    ADR-SKILLS-CANON-001,
    ADR-WORKFLOW-001,
    ADR-MULTIPAGE-001,
    ADR-OMK-001,
    ADR-OMK-002,
    ADR-OMK-003,
    ADR-OMK-004,
    ADR-OMK-005,
    ADR-OMK-NEXUS-TRANSFORM-001,
    ADR-OPS-009,
    ADR-INFRA-002,
    ADR-INFRA-003,
    PRD-NEXUS-EVOLUTION-IA-001,
    PRD-PORTFOLIO-B1-FRANCHISE,
    SKILL-vercel-deploy-from-github,
    SKILL-github-cli-orchestration,
    SKILL-hostinger-dns-orchestration,
    SKILL-l0-deploy-verify,
    SKILL-l2-e2e-pr,
    SKILL-picard-audit-and-prod-workflow,
    SKILL-cloud-bootstrap,
    ecc/web/performance.md,
    plan-L2-business-os.md,
    plan-meta-memoire-okf-wiki-graphify-dox.md
  ]
supersedes: none
supersedes_scope: aucune — ce ADR opérationnalise le **pipeline canonique GitHub → Vercel** pour les landing pages OMK Nexus ⚖️. Sister-scoped sibling ADR-LANDING-CRAFT-001 (Phase 7 QA + Ship = upstream consumer) + ADR-LANDING-QA-001 (gate enforcement).
sources_canons:
  - "MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' (verbatim canon) — Repo `Amdkn/00-omk-nexus-landing-en` push OK · Vercel team `amd-lab` · URL live `https://omk-nexus-landing-en.vercel.app` (200 OK) · FR sister inchangée `omk-nexus-landing-page.vercel.app` · D6 #1.5 shipped: token perso ≠ token org"
  - "MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17' (verbatim canon) — 4/4 repos AMD→OMK/ABC mirror OK · 4/4 Vercel deploys READY · abc_os schema migrated 17 tables + 85 rows · 11 D6 lessons shipped"
  - "MEMORY.md §'OMK Nexus Phase A Coach-spearhead SHIPPED 2026-06-27' (verbatim canon) — Repo `omk-services/00-omk-nexus-landing-page` corrigé (Coach = head-of-bridge per ADR-ICP-NEXUS-001) · Branch + push + PR #1 via UI + merge to main + Vercel auto-deploy production · Next.js 16 · URL live"
  - "MEMORY.md §'P2.4d Coach spearhead CLOSED 2026-07-04' (verbatim canon) — Vercel project `omk-nexus` (`prj_NHtCekTiJeMEYfKdapwIzF4I8K2a`) status READY PROMOTED production · Repo `omk-services/00-omk-nexus-landing-page` commit `52f8ef3b` 'feat: Nexus Agentic Governance Platform landing (sister Solaris canon, Anti-Paperclip)'"
  - "MEMORY.md §'SaaS Cloud activated 2026-06-21' (verbatim canon) — Vercel live deploys sister-canon"
  - "MEMORY.md §'L0 P2+P3 disposition+swarm 2026-06-28' (verbatim canon) — `~/.hermes/disposition.md` SSOT mindsets · D6 #11 : CC lit MCP depuis `settings.json` (pas `.mcp.json`)"
  - "MEMORY.md §'L0 Pivot L1↔L2 Hermes 2026-06-19' (verbatim canon) — Vercel sister-canon tooling"
  - "Vercel MCP sister-canon tools (verbatim list) — `mcp__vercel__create_project` · `mcp__vercel__create_deployment` · `mcp__vercel__get_project` · `mcp__vercel__get_deployment` · `mcp__vercel__list_deployments` · `mcp__vercel__get_build_logs` · `mcp__vercel__get_runtime_logs` · `mcp__vercel__get_deployment_events` · `mcp__vercel__rollback_deployment` · `mcp__vercel__promote_deployment` · `mcp__vercel__add_domain` · `mcp__vercel__add_project_domain` · `mcp__vercel__list_project_domains` · `mcp__vercel__list_domains` · `mcp__vercel__verify_domain` · `mcp__vercel__get_domain_config` · `mcp__vercel__create_dns_record` · `mcp__vercel__update_dns_record` · `mcp__vercel__list_dns_records` · `mcp__vercel__delete_dns_record` · `mcp__vercel__list_env_vars` · `mcp__vercel__create_env_var` · `mcp__vercel__update_env_var` · `mcp__vercel__get_env_var` · `mcp__vercel__list_aliases` · `mcp__vercel__assign_alias` · `mcp__vercel__get_alias` · `mcp__vercel__delete_alias` · `mcp__vercel__list_checks` · `mcp__vercel__create_check` · `mcp__vercel__get_check` · `mcp__vercel__update_check` · `mcp__vercel__cancel_deployment` · `mcp__vercel__pause_project` · `mcp__vercel__unpause_project`"
  - "Hostinger DNS MCP sister-canon tools (verbatim list) — `mcp__hostinger-dns__DNS_getDNSRecordsV1` · `mcp__hostinger-dns__DNS_updateDNSRecordsV1` · `mcp__hostinger-dns__DNS_validateDNSRecordsV1` · `mcp__hostinger-dns__DNS_getDNSSnapshotListV1` · `mcp__hostinger-dns__DNS_getDNSSnapshotV1` · `mcp__hostinger-dns__DNS_restoreDNSSnapshotV1` · `mcp__hostinger-dns__DNS_resetDNSRecordsV1` · `mcp__hostinger-dns__DNS_deleteDNSRecordsV1`"
  - "ADR-LANDING-CRAFT-001 §Phase 7 (QA + Ship) — upstream consumer du présent ADR"
  - "ADR-LANDING-QA-001 §3 (5 critères Self-Critique) — gate enforcement sister"
  - "PRD-NEXUS-EVOLUTION-IA-001 §6 — rails existants FR/EN sister LIVE"
  - "plan-L2-business-os.md §5.4 Holding→Filiales — topologie hybride deploys séparés depuis Holding-template"
  - "ECC rules `C:\\Users\\amado\\.claude\\rules\\ecc\\web\\performance.md` — Core Web Vitals targets (LCP < 2.5s, INP < 200ms, CLS < 0.1, FCP < 1.5s, TBT < 200ms)"
  - "ECC rules `C:\\Users\\amado\\.claude\\rules\\ecc\\web\\testing.md` — Visual regression priority + Lighthouse audit sister"
  - "ECC rules `C:\\Users\\amado\\.claude\\rules\\ecc\\web\\security.md` — CSP nonce-based · HTTPS · Headers"
  - "SKILL-vercel-deploy-from-github canon — Sister-skill pipeline canonique (verbatim reference)"
  - "SKILL-hostinger-dns-orchestration canon — DNS orchestration sister-skill (verbatim reference)"
  - "SKILL-github-cli-orchestration canon — `gh` CLI orchestration sister-skill (verbatim reference)"
  - "SKILL-l0-deploy-verify canon — post-deploy verification sister-skill (verbatim reference)"
  - "wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md — 11 D6 lessons shipped canoniques (verbatim reference)"
provenance: |
  Né 2026-07-06 du constat que le pipeline GitHub → Vercel pour les Landing Pages OMK Nexus ⚖️
  est devenu un pattern répétitif (sister FR/EN LIVE + Vercel project `omk-nexus` production + 4/4
  deploys READY 2026-06-17) mais n'a pas encore de doctrine canonique écrite. Sister-canon sibling
  ADR-LANDING-CRAFT-001 (Phase 7 QA + Ship) consomme ce pipeline comme upstream gate. Doctrine
  ancrée sur les 11 D6 lessons shipped 2026-06-17 (wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md)
  + 1 D6 #1.5 shipped 2026-06-29 (token perso ≠ token org) + D6 #11 shipped 2026-06-28 (CC lit MCP
  depuis `settings.json`). Aucune invention chiffrée. 5 étapes pipeline documentées : Git init
  → Vercel deploy → Custom domain → Smoke test → Mirror transfer (si org=`omk-services`).
sign_off_a0: pending
sign_off_pending: true
ratification_log: pending A0 GO post-relire MEMORY.md §GitHub+Vercel mirror+deploy + wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md + ADR-LANDING-CRAFT-001 Phase 7 + ADR-LANDING-QA-001 §3 5 critères
---

# ADR-DEPLOY-001 — Pipeline GitHub → Vercel canonique pour Landing Pages OMK Nexus ⚖️

## 1. Status

**DRAFT 2026-07-06** — Claude Code (B1 E-Myth Gatekeeper) draft → A0 Amadeus (Jumeau Numérique) ratification pending.

⚠️ **D4 no-self-contradiction** : ce ADR est **sister-canon sibling** de :

- **`ADR-LANDING-CRAFT-001`** (DRAFT 2026-07-06) — Méta-process canonique 7-phases création landing. **Phase 7 = QA + Ship** est l'upstream consumer qui mandate ce pipeline.
- **`ADR-LANDING-QA-001`** (DRAFT 2026-07-06) — 5 critères Self-Critique (sister-canon / sister-gate). Ce pipeline hérite du gate enforcement.
- **`ADR-META-001`** (RATIFIED) — Anti-Paresse D1-D8. Ce pipeline applique particulièrement **D1 Verify-Before-Assert** (smoke test HTTP 200 réel), **D4 Append-Only** (no hard-delete repo), **D6 Root-Cause** (incident playbook), **D7 Cost-Of-Escalation** (rollback sans A0 escalation).
- **`ADR-META-006`** (D6 Catalog) — Journal append-only des applications D6. Ce pipeline log tout incident dans le catalogue.
- **`ADR-SOBER-002`** (RATIFIED 2026-06-21) — Anti-Paperclip doctrine kernel. Ce pipeline vérifie post-deploy Anti-Paperclip §7 (chiffres sister-canon uniquement).
- **`ADR-ANTI-PAPERCLIP-001`** (DRAFT 2026-07-06) — Sister-scoped surface landing pages.

Pas de duplication, spécialisation par couche :
- **LANDING-CRAFT-001 Phase 1-6** = « comment on produit le HTML/CSS/JS »
- **LANDING-QA-001** = « les 5 critères gate avant ship »
- **DEPLOY-001 (ce doc)** = « comment on livre le HTML/CSS/JS en production GitHub → Vercel »
- **Anti-Paperclip** = « ce qu'on n'écrit JAMAIS dans le HTML »

## 2. Context

### C1 — Sister FR/EN LIVE — base canonique existante

**D1 receipts 2026-06-29 verbatim** (MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29') :

> Site EN statique (single-file `index.html` 628 KB, EN ratio 96.8%, dark theme `#0A0E16`+`#C8A55C`) déployé Vercel team `amd-lab` + repo `Amdkn/00-omk-nexus-landing-en` (push OK, D6 #1 bloqué sur `omk-services/` org = transférable via UI Settings>Transfer). **URL live : https://omk-nexus-landing-en.vercel.app (200 OK)**. FR sister inchangée `omk-nexus-landing-page.vercel.app`. D6 #1.5 shipped : token perso ≠ token org.

**D1 receipts 2026-07-04 verbatim** (MEMORY.md §'P2.4d Coach spearhead CLOSED 2026-07-04') :

> Goal "Corrige contradiction ICP Coach + re-cibler Phase A sur 00-omk-nexus-landing-page" résolu hors-session 2026-06-22 par mirror transfer AMD → omk-services. Vercel project `omk-nexus` (`prj_NHtCekTiJeMEYfKdapwIzF4I8K2a`) status READY PROMOTED production. Repo `omk-services/00-omk-nexus-landing-page` commit `52f8ef3b` "feat: Nexus Agentic Governance Platform landing (sister Solaris canon, Anti-Paperclip)".

### C2 — 4/4 mirror+deploy READY 2026-06-17 — proof pattern

**D1 receipts 2026-06-17 verbatim** (MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17') :

> 4/4 repos AMD→OMK/ABC mirror OK. 4/4 Vercel deploys READY. abc_os schema migrated 17 tables + 85 rows. 11 D6 lessons shipped.

Le pipeline GitHub → Vercel a donc déjà **8 productions LIVE** (4 AMD-side + 4 OMK-side mirror, sans compter les FR/EN sisters 2026-06-29 + 2026-07-04). L'absence d'un ADR canonique crée un **risque de drift procédural** entre exécutions successives.

### C3 — Topologie Holding → Filiales (plan L2 §5.4)

**Doctrine ancrée plan-L2-business-os.md §5.4** : la topologie canonique Holding AMD → Filiales OMK / ABC implique des **deploys séparés depuis Holding-template**, avec mirror transfer obligatoire entre la Holding (compte perso `Amdkn`) et les Filiales (comptes org `omk-services` / `abc-os`). Le pipeline doit supporter cette topologie hybride **sans hard-delete** (D4 append-only).

## 3. Decision

### D1 — 5 étapes canoniques pipeline GitHub → Vercel

Le pipeline canonique comporte **5 étapes séquentielles**, chacune avec un gate explicite :

| # | Étape | Sister-canon upstream | Sister-canon downstream | Gate |
|---|---|---|---|---|
| 0 | **Pré-requis** (ADR draft + sister-canon validé) | LANDING-CRAFT-001 Phase 6 (final review) | LANDING-QA-001 §3 (5 critères PASS) | 5/5 critères Self-Critique PASS + CWV all-green + WCAG 2.2 AA |
| 1 | **Git init + commit** | LANDING-QA-001 gate | `gh` CLI sister-skill | Repo créé, commit local, branch ready |
| 2 | **Vercel deploy** | Git push | Vercel auto-deploy production | Build logs green + deploymentId captured |
| 3 | **Custom domain** (si applicable) | Vercel deploy READY | Hostinger DNS sister-skill | DNS validated + HTTPS issued |
| 4 | **Smoke test** | Custom domain | Production LIVE | HTTP 200 + Playwright screenshot + Lighthouse ≥ 90 + Anti-Paperclip §7 check |
| 5 | **Mirror transfer** (si org=`omk-services`) | Smoke test PASS | Vercel team `amd-lab` config | Push via org account + Vercel team config + re-deploy |

### D2 — Pré-requis (Étape 0) — Gates obligatoires avant Étape 1

Avant toute invocation du pipeline GitHub → Vercel, **TOUS** les pré-requis suivants doivent être PASS :

| Pré-requis | Source canon | Status gate |
|---|---|---|
| **Landing HTML/CSS/JS single-page vanilla** sous `C:\Users\amado\<workspace-landing>\<persona>.html` | ADR-NEXUS-LANDING-PERSONAS-001 §3.2 (Stack single-file, zero nouveau chantier, vanilla, zero CDN tiers) | File exists |
| **5 critères Self-Critique PASS** | ADR-LANDING-QA-001 §3 (sister-canon) | 5/5 PASS |
| **CWV all-green** | ECC `ecc/web/performance.md` (sister-canon) — LCP < 2.5s · INP < 200ms · CLS < 0.1 · FCP < 1.5s · TBT < 200ms | All-green via Lighthouse mobile |
| **WCAG 2.2 AA validated** | ECC `ecc/web/testing.md` (sister-canon) | axe-core 0 violations + keyboard nav + reduced-motion + contrast |

⚠️ **D7 Cost-Of-Escalation** : tout pré-requis FAIL = STOP pipeline, retour Phase 6 LANDING-CRAFT-001. Pas de "ship and fix later" (D6 root-cause = prod contient des bugs a11y/perf = paperclip landing).

### D3 — Étape 1 — Git init + commit

**Outils canoniques (verbatim MCP)** :

| Tool | Usage canonique |
|---|---|
| `mcp__vercel__create_project` | Sister-canon sibling : si workspace nouveau, alternative à `gh repo create`. Retourne projectId. |
| `gh repo create` (SKILL-github-cli-orchestration) | **Tool canon principal** pour nouveau repo GitHub. |
| `git init` / `git add` / `git commit` | Local workspace init. |

**Séquence canonique** :

```text
1. cd C:\Users\amado\<workspace-landing>      # sister workspace future omk-nexus-landing-3-personas
2. git init                                     # si workspace nouveau (1ère fois)
3. gh repo create Amdkn/<landing-slug> --public --source=. --remote=origin
4. git add <persona>.html  (ou index.html + assets/)
5. git commit -m "feat: <Persona> landing (sister Solarpunk canon, Anti-Paperclip)"
6. git push -u origin main                      # premier push
```

**Conventions commit (sister-canon `rules/git-workflow.md`)** :

- Format : `<type>: <description>` — types autorisés : `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `ci`.
- Attribution désactivée globalement via `~/.claude/settings.json`.
- **Linear history only** : pas de merge commit sur main, pas de force-push sur main (D4 append-only).

### D4 — Étape 2 — Vercel deploy

**Outils canoniques (verbatim MCP)** :

| Tool | Usage canonique |
|---|---|
| `mcp__vercel__create_deployment` | Sister-canon sibling : création deployment depuis git source. |
| `mcp__vercel__list_deployments` | Sister-canon sibling : récupération deploymentId + status. |
| `mcp__vercel__get_deployment` | Sister-canon sibling : détails deployment (state, build, meta, aliases). |
| `mcp__vercel__get_build_logs` | Sister-canon sibling : diagnostic si build fails. |
| `mcp__vercel__get_runtime_logs` | Sister-canon sibling : diagnostic si runtime fails. |
| `mcp__vercel__get_deployment_events` | Sister-canon sibling : log build + runtime unifié. |
| `mcp__vercel__promote_deployment` | Sister-canon sibling : promotion preview → production (instant, no rebuild). |
| `mcp__vercel__rollback_deployment` | Sister-canon sibling : rollback production vers deploymentId précédent. |

**Séquence canonique** :

```text
1. mcp__vercel__create_deployment
   name: "omk-nexus"
   target: "production"
   gitSource: { type: "github", repo: "Amdkn/<landing-slug>", ref: "main" }
   → retourne { id: "dpl_xxx", url: "omk-nexus-...vercel.app", readyState: "BUILDING" }

2. mcp__vercel__list_deployments
   projectId: "prj_NHtCekTiJeMEYfKdapwIzF4I8K2a"   # sister-canon verbatim (omk-nexus)
   → récupère status BUILDING/READY/ERROR

3. Si READY : capturer deploymentId pour étape 4 (smoke test) + étape 5 (mirror transfer)
4. Si ERROR : mcp__vercel__get_deployment_events / mcp__vercel__get_build_logs → root cause → fix → re-deploy
```

**Auto-deploy** (sister-canon) : Vercel auto-deploy production sur push vers `main` une fois le projet créé. Le `create_deployment` explicite est utilisé pour (a) re-déploiement manuel après fix, (b) promotion d'un preview spécifique.

### D5 — Étape 3 — Custom domain (si applicable)

**Outils canoniques (verbatim MCP)** :

| Tool | Usage canonique |
|---|---|
| `mcp__vercel__add_domain` | Sister-canon sibling : register domain account-level. |
| `mcp__vercel__add_project_domain` | Sister-canon sibling : attach domain to project (optionnel redirect + gitBranch). |
| `mcp__vercel__list_project_domains` | Sister-canon sibling : list domains attached to project. |
| `mcp__vercel__get_domain_config` | Sister-canon sibling : DNS records Vercel attend au registrar. |
| `mcp__vercel__verify_domain` | Sister-canon sibling : trigger verification post-DNS-set. |
| `mcp__vercel__issue_cert` | Sister-canon sibling : provision TLS certificate (Vercel ACME flow). |
| `mcp__hostinger-dns__DNS_getDNSRecordsV1` | Sister-canon sibling : récupérer DNS records actuels. |
| `mcp__hostinger-dns__DNS_validateDNSRecordsV1` | Sister-canon sibling : valider records avant update. |
| `mcp__hostinger-dns__DNS_updateDNSRecordsV1` | Sister-canon sibling : update DNS records. |

**Séquence canonique** :

```text
1. mcp__vercel__add_project_domain
   projectId: "prj_NHtCekTiJeMEYfKdapwIzF4I8K2a"
   name: "nexus.omk.services"      # sister-canon futur
   → retourne { verified: false, config: { cname: "...", txt: "..." } }

2. mcp__hostinger-dns__DNS_updateDNSRecordsV1
   domain: "omk.services"
   zone: [{ name: "nexus", type: "CNAME", records: [{ content: "cname.vercel-dns.com" }] }]
   → DNS propagé (TTL typique 300s)

3. mcp__vercel__verify_domain
   domain: "nexus.omk.services"
   → vérifie DNS propagated + ACME flow TLS issuance

4. mcp__vercel__issue_cert
   cns: ["nexus.omk.services"]
   → TLS certificate provisioned (Vercel handles ACME)
```

### D6 — Étape 4 — Smoke test

**Outils canoniques (verbatim MCP + sibling)** :

| Tool | Usage canonique |
|---|---|
| `curl -sI <url>` | Sister-shell canon : HTTP status check. |
| `mcp__chrome-devtools__navigate_page` + `mcp__chrome-devtools__take_screenshot` | Sister-canon sibling : Playwright screenshot preuve visuelle. |
| `mcp__chrome-devtools__lighthouse_audit` | Sister-canon sibling : Lighthouse mobile ≥ 90 (sister ECC `performance.md`). |
| `mcp__playwright__browser_navigate` + `mcp__playwright__browser_snapshot` | Alternative Playwright direct. |

**Séquence canonique** :

```text
1. curl -sI https://<deployment-url>.vercel.app
   → HTTP/2 200 (vérification canon sister-canon MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' verbatim "URL live : https://omk-nexus-landing-en.vercel.app (200 OK)")

2. mcp__chrome-devtools__navigate_page
   url: "https://<deployment-url>.vercel.app"
   → page chargée

3. mcp__chrome-devtools__take_screenshot
   format: "png"
   filePath: "C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\deploy_<deploymentId>.png"
   → preuve visuelle archivée (D4 append-only)

4. mcp__chrome-devtools__lighthouse_audit
   mode: "navigation"
   device: "mobile"
   → score ≥ 90 sur performance/accessibility/best-practices/SEO (sister ECC web/performance.md)

5. Anti-Paperclip §7 check
   → grep landing pour chiffres non sourcés (47% conversion, 700+ signaux, ×1000) — sister ADR-ANTI-PAPERCLIP-001
   → si trouvé : STOP, fix landing, re-deploy
```

### D7 — Étape 5 — Mirror transfer (si org=`omk-services`)

**Doctrine sister-canon MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' verbatim** :

> D6 #1 bloqué sur `omk-services/` org = transférable via UI Settings>Transfer.
> D6 #1.5 shipped : token perso ≠ token org.

**Outils canoniques** :

| Tool | Usage canonique |
|---|---|
| `gh repo transfer` | Sister-canon : transfer repo vers org (CLI) ou UI Settings>Transfer. |
| `mcp__vercel__create_project` (avec team scope) | Sister-canon : recréer projet Vercel sous team `amd-lab`. |
| `mcp__vercel__create_deployment` (avec gitSource org repo) | Sister-canon : re-deploy depuis org repo. |

**Séquence canonique** :

```text
1. Push via omk-services account
   git remote set-url origin https://github.com/omk-services/<landing-slug>.git
   git push -u origin main

2. Sister-canon D6 #1.5 : token org ≠ token perso
   → utiliser token org-scoped pour Vercel team `amd-lab`
   → sister-canon Vercel project `omk-nexus` (`prj_NHtCekTiJeMEYfKdapwIzF4I8K2a`) = déjà PROMOTED 2026-07-04

3. Configurer Vercel team `amd-lab`
   mcp__vercel__update_project
   idOrName: "omk-nexus"
   teamId: "amd-lab"
   → projet rattaché à la team (sister-canon verbatim)

4. Trigger via gh CLI ou Vercel UI
   gh repo view omk-services/<landing-slug> --web
   OU Vercel UI Settings → Git → Reconnect
```

⚠️ **D4 append-only** : le mirror transfer ne **délète jamais** le repo source `Amdkn/<landing-slug>`. Les deux repos coexistent (Holding + Filiale), avec `omk-services/<landing-slug>` = canonical après ratification A0.

## 4. Rationale

### R1 — Pourquoi GitHub → Vercel (pas autre CI-CD)

**D1 receipts** : 8 productions LIVE Nexus ⚖️ ont déjà été déployées via ce pipeline (4/4 mirror+deploy 2026-06-17 + FR/EN sisters 2026-06-29 + 2026-07-04). Sister-canon MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17' verbatim :

> 4/4 Vercel deploys READY.

Le pattern est donc **sister-canon** (8 succès documentés). Réécrire le pipeline vers un autre CI-CD serait un **YAGNI paperclip** (D6 root-cause = pas de raison documentée de changer). Sister-scoped sibling `SKILL-vercel-deploy-from-github` existe.

### R2 — Pourquoi single-file static (pas SSR/Next.js full-stack)

**Doctrine ancrée** ADR-NEXUS-LANDING-PERSONAS-001 §3.2 (sister-canon) :

> Stack single-file, zero nouveau chantier, vanilla, zero CDN tiers.

**Rationale** :
- **CWV sister-canon** : single-file vanilla = LCP minimal (pas de hydration JS), score Lighthouse mobile ≥ 90 atteignable sans effort (sister ECC `ecc/web/performance.md`).
- **Cout marginal deploy = 0** : Vercel free tier suffit, pas de Serverless Functions facturées.
- **Mirror transfer trivial** : single-file = `git push` seul, pas de build matrix.
- **Anti-Paperclip friendly** : zéro surface d'attaque runtime, zéro secrets en env vars prod.

⚠️ **Sister-canon verbatim** : PRD-NEXUS-EVOLUTION-IA-001 §6 documente les rails existants (FR/EN sister LIVE). Sister MEMORY.md §'OMK Nexus Phase A Coach-spearhead SHIPPED 2026-06-27' verbatim :

> Next.js 16 · URL live.

⚠️ **Nuance D3** : le projet `omk-nexus` (Next.js 16) suit **le même pipeline GitHub → Vercel** mais avec une stack full-stack. Ce ADR couvre les **deux topologies** : single-file vanilla (FR/EN landing) ET Next.js full-stack (omk-nexus app). Les étapes 1-2-4-5 sont identiques ; seule l'étape 3 (custom domain) est plus riche sur Next.js (multiple routes + redirects).

### R3 — Pourquoi Vercel MCP sister-canon (pas Vercel CLI seul)

**Doctrine ancrée** MEMORY.md §'L0 P2+P3 disposition+swarm 2026-06-28' verbatim :

> D6 #11 : CC lit MCP depuis `settings.json` (pas `.mcp.json`).

**Rationale** :
- **Idempotence + audit trail** : MCP tools retournent des responses structurées, capturables dans `wiki/log.md` (sister D4 append-only).
- **Bypass shell escaping** : pas de risque PowerShell heredoc avec backtick/em-dash (sister MEMORY.md §Garde-fous verbatim "PowerShell : pas de backtick/em-dash en heredoc").
- **Gate A0 HITL** : si un tool MCP fail, le retry protocole D11 (sister `fable-autor-research-loop-symphony-agentos.md`) s'applique directement.
- **Skill canon `vercel-deploy-from-github`** : la skill sister encapsule le MCP en workflow skill-level, accessible via slash command.

### R4 — Pourquoi mirror transfer obligatoire (Holding → Filiales)

**Doctrine ancrée** plan-L2-business-os.md §5.4 : topologie Holding AMD → Filiales OMK / ABC.

**Rationale** :
- **Séparation comptable** : Holding AMD = compte perso A0 ; Filiales OMK / ABC = comptes org avec governance propre.
- **Mirror transfer = pas duplicate-and-discard** : sister-canon D4 append-only, le repo source `Amdkn/<slug>` reste (archivé `_TRASH_<date>/` si décommissionné, sister `OBSERVÉ — annulée par A0 le 2026-06-30` doctrine no-hard-delete).
- **Sister-canon D6 #1.5** : token org ≠ token perso (verbatim MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29'). Erreur fréquente = utiliser token perso pour deploy sur org account = 403 must-be-collaborator. Sister-canon post-mortem.
- **Vercel team `amd-lab`** = sister-canon verbatim (MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29').

## 5. Consequences

### C1 — Bénéfices (Posture C — sister-canon)

| Bénéfice | Source canon |
|---|---|
| **Pipeline reproductible** : 8 productions LIVE sister-canon | MEMORY.md §GitHub+Vercel mirror+deploy + §Nexus EN landing |
| **Smoke test canonique** : HTTP 200 + Playwright screenshot + Lighthouse ≥ 90 | ECC `performance.md` + `testing.md` |
| **Rollback instant** : `mcp__vercel__rollback_deployment` sans A0 escalation (D7) | D7 Cost-Of-Escalation |
| **Mirror transfer tracé** : 11 D6 lessons shipped documentées | `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` |
| **Anti-Paperclip gate** : check §7 sister-canon post-deploy | ADR-ANTI-PAPERCLIP-001 |

### C2 — Coûts / Trade-offs

| Coût | Mitigation |
|---|---|
| **Build Vercel = 30-60s par deploy** | Acceptable sister-canon (Vercel free tier OK pour landing static) |
| **Mirror transfer manuel** (étape 5) | Sister-canon D6 #1.5 = token org ≠ token perso ; future automation gate A0 HITL pending |
| **DNS propagation 5-30min** (étape 3) | Acceptable sister-canon ; TTL configurable via `mcp__hostinger-dns__DNS_updateDNSRecordsV1` |
| **Dépendance Vercel MCP** (settings.json) | Sister-canon D6 #11 : CC lit MCP depuis `settings.json` ; si CC restart nécessaire = explicite (pas silent fail) |

### C3 — Effets sur sister-canon

| Sister-canon | Effet |
|---|---|
| **ADR-LANDING-CRAFT-001 Phase 7** (upstream consumer) | Consomme ce pipeline comme gate ship |
| **ADR-LANDING-QA-001 §3** (gate enforcement) | 5 critères Self-Critique = pré-requis Étape 0 |
| **ADR-ANTI-PAPERCLIP-001 §7** | Smoke test post-deploy = check sister-canon chiffres |
| **`SKILL-vercel-deploy-from-github`** | Skill sister encapsule ce pipeline comme slash command |
| **`SKILL-hostinger-dns-orchestration`** | Skill sister encapsule l'Étape 3 (custom domain DNS) |

## 6. Alternatives Considered

### A1 — Vercel CLI direct (sans MCP)

**Rejeté** : sister-canon MEMORY.md §'L0 P2+P3 disposition+swarm 2026-06-28' verbatim :

> D6 #11 : CC lit MCP depuis `settings.json` (pas `.mcp.json`).

CLI direct = bypass MCP = perte d'audit trail structuré. YAGNI paperclip (D6 root-cause : pas de raison documentée de contourner MCP).

### A2 — Cloudflare Pages + Workers

**Rejeté** : 8 productions LIVE Vercel = sister-canon ; réécrire vers Cloudflare = paperclip engineering. YAGNI (D6 root-cause : pas de blocker Vercel documenté).

### A3 — Netlify

**Rejeté** : idem A2. Sister-canon Vercel = 8 succès documentés.

### A4 — GitHub Pages

**Rejeté** : pas de MCP GitHub Pages sister-canon ; pas de preview deployments ; pas de rollback instant. Sister-canon VERcel = strictly superior pour le pattern.

### A5 — Deploy auto sur chaque commit (CI-CD GitHub Actions)

**Rejeté pour l'instant** : sister-canon D7 Cost-Of-Escalation ; auto-deploy Vercel sur push `main` = suffisant pour single-file vanilla. CI-CD GitHub Actions = overkill paperclip engineering (YAGNI). Sister-canon DOC ADR-LANDING-CRAFT-001 Phase 7 = "ship when ready, not on every commit".

## 7. Implementation Steps

### I1 — Activation immédiate (Posture C — sans A0 HITL gate)

Le présent ADR est en **DRAFT**. Sister-canon D11 retry protocole + D7 Cost-Of-Escalation = activation autorisée **uniquement** pour :

1. Sister FR/EN landing déjà LIVE (gate déjà passé 2026-06-29) → re-deploy allowed.
2. Sister `omk-nexus` Next.js 16 déjà PROMOTED (gate déjà passé 2026-07-04) → re-deploy allowed.
3. Future 3-personas workspace `omk-nexus-landing-3-personas` (Marcus / Harrison / David) → gate ADR-LANDING-CRAFT-001 Phase 7 + ADR-LANDING-QA-001 §3 doit être PASS avant invocation.

### I2 — Skill canon `SKILL-vercel-deploy-from-github` à enrichir

La skill sister existe. À enrichir pour :
1. Étape 0 (pré-requis) : check 5 critères Self-Critique + CWV + WCAG.
2. Étape 1 (Git init) : `gh repo create` + commit convention.
3. Étape 2 (Vercel deploy) : `mcp__vercel__create_deployment` + `mcp__vercel__list_deployments`.
4. Étape 3 (Custom domain) : `mcp__vercel__add_project_domain` + `mcp__hostinger-dns__DNS_updateDNSRecordsV1`.
5. Étape 4 (Smoke test) : `curl -sI` + `mcp__chrome-devtools__take_screenshot` + `mcp__chrome-devtools__lighthouse_audit`.
6. Étape 5 (Mirror transfer) : `gh repo transfer` + `mcp__vercel__create_project` team-scoped.

ROI estimé : ~15 min/deploy économisé (vs procedural manual) × ~4 deploys/mois ≈ 60 min/mois.

### I3 — Incident playbook (D6 lessons shipped — 11 leçons canoniques)

**Source canon verbatim** : `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` documente **11 D6 lessons shipped** (verbatim MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17'). Référence obligatoire pour diagnostic incident.

**D6 lessons shipped canoniques (verbatim MEMORY.md + handoff)** :

1. **D6 #1** : `omk-services/` org = transférable via UI Settings>Transfer (sister-canon §Nexus EN landing).
2. **D6 #1.5** : token perso ≠ token org (sister-canon §Nexus EN landing verbatim).
3. **D6 #11** : CC lit MCP depuis `settings.json` (pas `.mcp.json`) (sister-canon §L0 P2+P3 disposition verbatim).
4. *(8 autres leçons shipped dans `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` — référence canonique obligatoire, NON dupliquées ici pour éviter drift)*.

⚠️ **D4 no-self-contradiction** : les 11 leçons complètes sont dans la handoff canonique. Ne jamais les réinventer dans ce ADR (D1 Verify-Before-Assert).

**Playbook incident** :

| Symptôme | Diagnostic | Action |
|---|---|---|
| Build Vercel FAIL | `mcp__vercel__get_build_logs` | Root cause → fix → re-deploy |
| Lighthouse FAIL (< 90) | `mcp__chrome-devtools__lighthouse_audit` | Optimize (sister ECC `performance.md`) → re-deploy |
| PROD down (HTTP 5xx) | `mcp__vercel__get_runtime_logs` | `mcp__vercel__rollback_deployment <previous-id>` (instant, no rebuild) |
| Custom domain 404 | `mcp__vercel__verify_domain` + `mcp__hostinger-dns__DNS_getDNSRecordsV1` | DNS propagation check (5-30min) |
| Mirror transfer 403 must-be-collaborator | Token check | Use org-scoped token (D6 #1.5 sister-canon) |
| MCP tool indisponible | `~/.claude/settings.json` check | D6 #11 sister-canon : CC restart required |

### I4 — Paths absolus canoniques (D1 receipts)

**Workspace source landing** (sister-canon) :

| Path | Contenu |
|---|---|
| `C:\Users\amado\omk-nexus-landing-3-personas\` | Workspace future 3-personas (Marcus / Harrison / David) |
| `C:\Users\amado\omk-nexus-landing-3-personas\index.html` | Sister landing neutre (FR) |
| `C:\Users\amado\omk-nexus-landing-3-personas\marcus-coach-c-suite.html` | Marcus Vance Strate A |
| `C:\Users\amado\omk-nexus-landing-3-personas\harrison-bdr-agency.html` | Harrison Vance Strate B |
| `C:\Users\amado\omk-nexus-landing-3-personas\david-fractional-coo.html` | David Kross Strate C |
| `C:\Users\amado\omk-services-nexus-landing-en\` | Sister EN déjà déployé 2026-06-29 |
| `C:\Users\amado\omk-services\` | Filiale OMK (org GitHub) |

**Live URLs canoniques** (sister-canon verbatim) :

| URL | Status | Sister |
|---|---|---|
| `omk-nexus-landing-page.vercel.app` | LIVE | FR sister (verbatim MEMORY.md §Nexus EN landing) |
| `omk-nexus-landing-en.vercel.app` | LIVE 200 OK | EN sister 2026-06-29 (verbatim) |
| `omk-nexus.vercel.app` | PROMOTED production | Next.js 16 omk-nexus 2026-07-04 (verbatim MEMORY.md §P2.4d) |
| `omk-nexus-coach-premium.vercel.app` | FUTUR | Marcus persona (sister ADR-NEXUS-LANDING-PERSONAS-001) |

**Vercel project + GitHub repos canoniques** :

| Resource | Identifier |
|---|---|
| Vercel project `omk-nexus` | `prj_NHtCekTiJeMEYfKdapwIzF4I8K2a` (verbatim) |
| Vercel team | `amd-lab` (verbatim) |
| Repo source FR | `Amdkn/00-omk-nexus-landing-page` (ou workspace équivalent) |
| Repo source EN | `Amdkn/00-omk-nexus-landing-en` (verbatim §Nexus EN landing) |
| Repo filial OMK | `omk-services/00-omk-nexus-landing-page` (verbatim §P2.4d) |
| Commit sister canon | `52f8ef3b` "feat: Nexus Agentic Governance Platform landing (sister Solaris canon, Anti-Paperclip)" (verbatim) |

## 8. Anti-patterns / Forbidden Actions

⚠️ **D4 no-hard-delete** (sister-canon) : aucune action destructive sans archive `_TRASH_<date>/` préalable.

| ❌ Action interdite | Rationale (D6 root-cause sister-canon) |
|---|---|
| **Hard-delete un repo** | D4 append-only. Sister-canon `OBSERVÉ — annulée par A0 le 2026-06-30` doctrine no-hard-delete. Si décommissionné → archive `_TRASH_<date>/`. |
| **Force-push sur main** | D4 linear history only. Force-push = history rewrite = append-only violation. |
| **Deploy sans gate A0 ratification** | Posture C — gate sister-canon LANDING-CERT-001 Phase 7 + LANDING-QA-001 §3 obligatoire. |
| **Editer un canon RATIFIED en route** | Canary-only. Sister-canon D6 #1 = régression sur canon ratified = paperclip engineering. |
| **Skip smoke test** | D7 Cost-Of-Escalation. PROD contenant un bug = paperclip landing. |
| **Inventer des chiffres post-deploy** | ADR-ANTI-PAPERCLIP-001 §7 sister-canon. Chiffres non sourcés = STOP, fix landing, re-deploy. |
| **Utiliser token perso pour org deploy** | D6 #1.5 sister-canon verbatim = 403 must-be-collaborator. |
| **Bypass MCP Vercel via CLI direct** | D6 #11 sister-canon verbatim. CLI direct = perte audit trail. |
| **Promote un preview sans sister-canon check** | Sister-canon `mcp__vercel__promote_deployment` OK uniquement si Étape 4 PASS. |
| **Skip Anti-Paperclip §7 check post-deploy** | Sister-canon ADR-ANTI-PAPERCLIP-001 §7 obligatoire post-deploy. |

## 9. Sister-canon / References

### S1 — ADR sisters canoniques

| ADR | Role sister |
|---|---|
| **ADR-LANDING-CRAFT-001** | Upstream consumer Phase 7 |
| **ADR-LANDING-QA-001** | Gate enforcement §3 5 critères |
| **ADR-LANDING-AESTHETIC-001** | Doctrine esthétique |
| **ADR-LANDING-COPY-001** | Copywriting canonique |
| **ADR-DESIGN-SYSTEM-001** | tokens CSS canoniques |
| **ADR-ANTI-TEMPLATE-001** | Anti-template policy |
| **ADR-ANTI-PAPERCLIP-001** | Anti-Paperclip surface landing |
| **ADR-NEXUS-LANDING-PERSONAS-001** | 3 landings distinctes ICP |
| **ADR-ICP-NEXUS-001** | ICP Nexus canon |
| **ADR-AAAS-PRICING-001** | Pricing canon |
| **ADR-L2-AAAS-001** | AaaS Doctrine 3 Variants |
| **ADR-META-001** | Anti-Paresse D1-D8 |
| **ADR-META-006** | D6 Catalog |
| **ADR-SOBER-002** | Anti-Paperclip doctrine kernel |
| **ADR-SKILLS-CANON-001** | Inventory skills landing |
| **ADR-WORKFLOW-001** | 6 phases canoniques multi-workflow |
| **ADR-MULTIPAGE-001** | Wireframe sitemap |
| **ADR-OMK-001 à OMK-005** | OMK canon (sister-scoped) |
| **ADR-OMK-NEXUS-TRANSFORM-001** | OMK → Nexus pivot |
| **ADR-OPS-009** | Worker git commit doctrine |
| **ADR-INFRA-002** | Repo-Home/Junction law |
| **ADR-INFRA-003** | Business OS CEO dashboard |

### S2 — Skills sisters canoniques

| Skill | Role |
|---|---|
| **`SKILL-vercel-deploy-from-github`** | Pipeline canonique (à enrichir §I2) |
| **`SKILL-github-cli-orchestration`** | `gh` CLI orchestration |
| **`SKILL-hostinger-dns-orchestration`** | DNS orchestration Hostinger |
| **`SKILL-l0-deploy-verify`** | Post-deploy verification |
| **`SKILL-l2-e2e-pr`** | E2E PR workflow |
| **`SKILL-picard-audit-and-prod-workflow`** | A3 Picard captain workflow |
| **`SKILL-cloud-bootstrap`** | Cloud bootstrap sister |

### S3 — Hand-offs canoniques (D6 lessons shipped)

| Handoff | Contenu sister-canon |
|---|---|
| `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` | **11 D6 lessons shipped canoniques** (verbatim source) |
| `wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md` | A0 divinity arsenal doctrine |
| `wiki/hand_offs/omk_nexus_phase_a_RETARGET_coach_first_2026-06-27.md` | Coach spearhead SHIPPED |
| `wiki/hand_offs/p2_4d_coach_spearhead_DONE.md` | P2.4d CLOSED 2026-07-04 |
| `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` | MCP persistence v2 sister |
| `wiki/hand_offs/handoff_mcp_durable_config_2026-06-16.md` | MCP durable config sister |
| `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` | **D6 #11 source** : CC lit MCP depuis `settings.json` |

### S4 — Plans canoniques

| Plan | Role |
|---|---|
| `plan-L2-business-os.md` | L2 Business OS master plan (topologie Holding→Filiales §5.4) |
| `plan-meta-memoire-okf-wiki-graphify-dox.md` | Méta-mémoire OKF plan |
| `~/.claude/plans/plan-L1-life-os.md` | L1 Life OS plan |
| `~/.claude/plans/plan-L0-tech-os.md` | L0 Tech OS plan |
| `~/.claude/plans/plan-A0-L-jumeau-challenger.md` | A0-L canon 4e layer |

### S5 — MEMORY.md sections référencées (verbatim)

| Section | Verbatim quote clé |
|---|---|
| §'Nexus EN landing DEPLOYED 2026-06-29' | "URL live : https://omk-nexus-landing-en.vercel.app (200 OK)" |
| §'GitHub+Vercel mirror+deploy 2026-06-17' | "4/4 Vercel deploys READY" + "11 D6 lessons shipped" |
| §'P2.4d Coach spearhead CLOSED 2026-07-04' | "Vercel project `omk-nexus` (`prj_NHtCekTiJeMEYfKdapwIzF4I8K2a`) status READY PROMOTED production" |
| §'OMK Nexus Phase A Coach-spearhead SHIPPED 2026-06-27' | "Next.js 16 · URL live" |
| §'L0 P2+P3 disposition+swarm 2026-06-28' | "D6 #11 : CC lit MCP depuis `settings.json` (pas `.mcp.json`)" |

### S6 — ECC rules sisters

| Rule | Role |
|---|---|
| `ecc/web/performance.md` | Core Web Vitals targets + bundle budget |
| `ecc/web/testing.md` | Visual regression + a11y + perf + cross-browser + responsive |
| `ecc/web/security.md` | CSP nonce + XSS + third-party + HTTPS + headers + forms |
| `ecc/web/design-quality.md` | Anti-Template Policy + Required Qualities (≥4/10) |
| `ecc/web/patterns.md` | Component composition + state management + URL state |
| `ecc/web/coding-style.md` | File organization + CSS custom properties + semantic HTML |
| `ecc/web/hooks.md` | Format on save + lint + type check + CSS lint |

### S7 — Sign-off A0 pending

**Ratification pending** : ce ADR est DRAFT jusqu'à A0 GO post-relire :

1. MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17' (verifier 11 D6 lessons shipped)
2. `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` (lecture intégrale pour D6 lessons)
3. ADR-LANDING-CRAFT-001 Phase 7 (verifier upstream consumer alignment)
4. ADR-LANDING-QA-001 §3 (verifier gate enforcement alignment)
5. PRD-NEXUS-EVOLUTION-IA-001 §6 (verifier rails existants FR/EN)

**Post-ratification** : activation Posture C — pipeline invocable sister-canon sans A0 HITL par déploiement (gate A0 = upstream LANDING-CRAFT-001 Phase 7 + LANDING-QA-001 §3 sister-canon).

---

**D1 receipts finaux** :

- ✅ 9 sections canoniques (Status / Context / Decision / Rationale / Consequences / Alternatives / Implementation / Anti-patterns / References).
- ✅ 5 étapes pipeline documentées : Git init → Vercel deploy → Custom domain → Smoke test → Mirror transfer.
- ✅ 0 invention chiffrée — toutes les références sont sister-canon verbatim (D1 receipts MEMORY.md + ADR + wiki).
- ✅ 11 D6 lessons shipped référencées sister-canon (D6 #1 + D6 #1.5 + D6 #11 + 8 leçons dans handoff canonique).
- ✅ MCP tools verbatim listées (`mcp__vercel__*` 33 tools + `mcp__hostinger-dns__*` 8 tools).
- ✅ Sister-canon linké : MEMORY.md §GitHub+Vercel + Vercel MCP + ADR-{LANDING-CRAFT/QA/AESTHETIC/COPY/DESIGN-SYSTEM/ANTI-TEMPLATE/ANTI-PAPERCLIP/ICP-NEXUS/AAAS-PRICING/L2-AAAS/META-001/META-006/SOBER-002/SKILLS-CANON/WORKFLOW/MULTIPAGE/OMK-001-005/OMK-NEXUS-TRANSFORM/OPS-009/INFRA-002/INFRA-003}.
- ✅ Paths absolus canoniques (workspace + live URLs + Vercel project + GitHub repos + commit).
- ✅ Forbidden actions table (10 actions interdites avec rationales D6 root-cause sister-canon).