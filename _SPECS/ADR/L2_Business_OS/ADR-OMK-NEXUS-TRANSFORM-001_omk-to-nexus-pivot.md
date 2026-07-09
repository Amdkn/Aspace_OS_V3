---
id: ADR-OMK-NEXUS-TRANSFORM-001
title: OMK → Nexus Transformation Canon (Pivot AaaS Landing Sister)
status: RATIFIED
date: 2026-06-24
ratified_date: 2026-06-24 (A0 verbal GO chat post canon-batch Acquisition Doctrine + 2 guides Premium)
last_updated: 2026-06-24 (Claude Code — A0 ratify GO, sister canon ACQUISITION-DOCTRINE-001 ajouté)
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2) on A0 directive (canon-batch analysis OMK vs Solaris vs Nexus Tier 4)
domain: L2 Business OS / AaaS Doctrine / Front-End / Transformation canon / 3-ICP alignment
tags: [#ADR #omk #nexus #pivot #transformation #front-end #aaas #solarpme #tier4 #conformite #zero-pii #ai-act #self-host #canonical #ratified]
related:
  - ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24, Pilier 1-5 Nexus canon)
  - ADR-ICP-SOLARIS-001 (RATIFIED 2026-06-24, sister canon sister-symétrique)
  - ADR-AAAS-PRICING-001 (RATIFIED + AMENDED 2026-06-24, 5 Tiers USD post-accuponcture)
  - ADR-L2-AAAS-001 (RATIFIED 2026-06-21, 3 Variants Solarpunk Doctrine)
  - ADR-AAAS-ACQUISITION-DOCTRINE-001 (RATIFIED 2026-06-24, 25 455 chars — Acquisition-First MedVie vs Structuration-First A0 OS, canon doctrinal sister direct)
  - ADR-MARKET-STUDY-001 (RATIFIED 2026-06-24, The Builders 2026 136,1 Mds$ intégrateurs système)
  - ADR-OMK-004 (RATIFIED 2026-06-19, OMK Stack Pivot Supabase Cloud + Vercel)
  - ADR-OMK-005 (RATIFIED 2026-06-20, Tenant Isolation Guard)
  - ADR-SOBER-002 (RATIFIED 2026-06-21, Anti-Paperclip doctrine — no greenwashing)
  - ADR-META-001 (Anti-Paresse D1-D8, Verify-Before-Assert)
  - ADR-META-006 (D6 Root Causes Catalog, append-only)
sources_canons:
  - wiki/hand_offs/solaris_omk_front_gap_analysis_2026-06-24.md (D1-verified, 18 receipts, 250+ lignes D1)
  - wiki/hand_offs/omk_nexus_transformation_plan_2026-06-24.md (D1-verified, 4 phases A/B/C/D, 22 tasks, 15 A0 HITL)
  - 01_Guides/03_IT/2026-06-17_etude-de-cas-medvi-400m-2-employes-agents-ia.md (D1-verified, 6 490 chars, MedVie 400M$ Y1 / 2 employés / 16.2% marge canon)
  - 01_Guides/02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md (D1-verified, 22 708 chars PREMIUM, $1M+ Solo AI Agent Business)
  - 01_Guides/07_Growth/onboarding-flows-1460-patterns-acquisition-funnel-Qsq-Sj_rojU.md (D1-verified, 21 873 chars PREMIUM, 1 460 Onboarding Flows Mobbin)
  - Takeout Gemini 2026-05 L19500 (verbatim "84 Trilliards" Family Office)
  - Takeout Gemini 2026-05 L18408 (verbatim "Paradoxe de la Complexité")
  - Takeout Gemini 2026-05 L21519 (verbatim ICP Nexus "Expert méthodique")
  - Takeout Gemini 2026-05 L21780 (verbatim "détruit la Holding")
  - Takeout Gemini 2026-05 L25160-25314 (verbatim "Citadelle du Savoir")
  - Takeout Gemini 2026-05 L25674 (verbatim "$750 Self-Host + $1555 Franchise Whitelabel")
  - Takeout Gemini 2026-05 L19580 (verbatim "Pas de SaaS public · Bare-Metal Zero-Knowledge")
  - Takeout Gemini 2026-05 L8796 (Zero-PII Compliance canon)
  - Takeout Gemini 2026-05 L11303-11306 (Makkari pattern Zero-PII Sanitization)
provenance: Née 2026-06-24 d'une analyse canon-batch D1-vérifiée commandée par A0 (Phase 1 = gap analysis Solaris vs OMK, Phase 2 = transformation plan OMK → Nexus). **RATIFIED 2026-06-24 par A0 verbal GO chat post-canon-batch (Acquisition Doctrine + 2 guides Premium 22 708 + 21 873 chars) — sister canon canon 1an+ minimum, D4 append-only.**
---

# ADR-OMK-NEXUS-TRANSFORM-001 — OMK → Nexus Transformation Canon (Pivot AaaS Landing)

## Status

**RATIFIED** — 2026-06-24 par A0 verbal GO chat (post-canon-batch canon-batch Acquisition Doctrine + 2 guides Premium + 3 MedVie guides canon = D1 receipts suffisants).

Sister canon de :
- [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) (RATIFIED 2026-06-24, Pilier 1-5 Nexus canon)
- [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) (RATIFIED + AMENDED 2026-06-24, 5 Tiers USD)
- [`ADR-ICP-SOLARIS-001`](./ADR-ICP-SOLARIS-001_icp-solaris-structuration.md) (RATIFIED 2026-06-24, sister-symétrique canon)
- [`ADR-AAAS-ACQUISITION-DOCTRINE-001`](./ADR-AAAS-ACQUISITION-DOCTRINE-001_aaas-acquisition-doctrine.md) (RATIFIED 2026-06-24, 25 455 chars, Acquisition-First MedVie vs Structuration-First A0 OS, doctrinal sister direct)
- [`ADR-MARKET-STUDY-001`](./ADR-MARKET-STUDY-001_the-builders-2026.md) (RATIFIED 2026-06-24, The Builders 2026 136,1 Mds$ intégrateurs système)
- [`ADR-OMK-004`](./ADR-OMK-004_pivot-supabase-cloud-vercel.md) (RATIFIED 2026-06-19, OMK Stack pivot base)

## Context

**D6 D3 nuance racine** — Avant cette analyse, **AUCUN gap analysis canon** des deux landings AaaS canon (Solaris local + OMK PROD LIVE) vs ICP Nexus sister canon RATIFIED 2026-06-24. Les 3 sisters canon (Solaris/Nexus/Orbiter) vivaient en doctrine sans confrontation à la prod réelle OMK.

**Discovery canon 2026-06-24** (D1-verified, `wiki/hand_offs/solaris_omk_front_gap_analysis_2026-06-24.md`) :

1. **Solaris (LOCAL)** : 18 fichiers TS/TSX + 2 CSS, 4 297 LOC, Next.js 16.2.6 + React 19.2.4 + hand-rolled design system (CSS variables) + JetBrains Mono "operating signal" + palette solar amber. **72% conformité ICP Solaris canon** (`ADR-ICP-SOLARIS-001`). PAS Nexus — sister canon.
2. **OMK (PROD LIVE)** : `https://omk-landing-page.vercel.app/` HTTP 200, 74 803 bytes, Next.js + Turbopack + Vercel, Space Grotesk + Inter + JetBrains Mono, palette emerald/blue/violet/pink. **9% conformité ICP Nexus canon** (D1 receipts exhaustifs : 14 SaaS publics brandés, 0 mention Expert méthodique, 0 Zero-PII, 0 self-host, 0 SOC2/AI-Act/HIPAA, `/tarifs` 404, devise EUR).
3. **Nexus Tier 4 canon (CIBLE)** : `ADR-ICP-NEXUS-001` Pilier 1-5 canon = Persona "Expert méthodique" + Mantra "L'illusion de la complexité" + Marché 84 Trilliards € Family Offices + 5 sub-types (Expert-comptable/Avocat/Family-Office/Coach/Cabinet-médical) + Killer Feature "Zero-PII Agentic Governance" 5 mécanismes (Action Space Bounding / Sandboxing Bare-Metal / HITL Dynamique légal / Traçabilité AI-Act / Zero-PII Sanitization). Pricing canon 4 tiers USD ($750 / $1000-1500 / $1500-2000+25% / $5K-50K MRR).

**D6 root cause #32 (sister handoff)** : "Un landing 'PROD LIVE' peut avoir 0% alignement avec un ICP canon sister sans que le canon ne le détecte → audit gap-analysis D1 obligatoire sister scope".

**A0 décision 2026-06-24** : Lancer le canon-batch analysis 4 livrables (gap analysis + transformation plan + ADR draft + log entry) pour outiller la décision A0 sur le pivot OMK → Nexus.

## Décision : 4 Phases A/B/C/D Canon (PROPOSED → target RATIFIED)

### Phase A — Quick Wins Persona + Messaging (Semaine W1, 13-19 h, 6 tasks)

**Objectif** : 9% → 35% conformité Nexus.

| # | Task | Effort |
|---|---|---|
| A1 | Hero tagline pivot vers "OS Expert / OS Conformité" (verbatim `ADR-ICP-NEXUS-001:25651-25740`) | 2-3 h |
| A2 | Section Mantra "L'illusion de la complexité" (verbatim L18408) | 3-4 h |
| A3 | 5 sub-types personas (Expert-comptable/Avocat/Family-Office/Coach/Cabinet-médical verbatim L21519) | 4-5 h |
| A4 | CTA async pivot "Recevoir mon audit 24h · Sans visio" | 2-3 h |
| A5 | Trust strip enrichi (RGPD + AI-Act + Zero-PII + Données européennes) | 1-2 h |
| A6 | Nova rebrand "Agent Vocal Conforme AI-Act" | 1-2 h |

### Phase B — Pricing Canon Refresh + Visual Identity Pivot (Semaine W2-W3, 29-41 h, 8 tasks)

**Objectif** : 35% → 65% conformité Nexus.

| # | Task | Effort |
|---|---|---|
| B1 | Implémenter `/tarifs` page avec 4 tiers canon Nexus USD | 6-8 h |
| B2 | Footer link fix `/tarifs` (404 actuellement) | 0.5 h |
| B3 | Pricing toggle EUR/USD avec canon USD par défaut | 2-3 h |
| B4 | Hero pricing snippet "À partir de $750/an · 14 jours d'essai" | 1-2 h |
| B5 | Visual identity pivot palette "Citadelle/Souverain" (or sobre + gris-bleu nuit) | 8-12 h |
| B6 | Typography shift Spectral/IBM Plex Serif (gravité expert) | 3-4 h |
| B7 | Section "Zero-PII Agentic Governance" 5 mécanismes | 6-8 h |
| B8 | Kill SaaS-public messaging OU rebrand "Stack private-by-default" | 2-3 h |

### Phase C — Conformité Badges + Trust Signals (Semaine W4, 18-25 h, 5 tasks)

**Objectif** : 65% → 85% conformité Nexus.

| # | Task | Effort |
|---|---|---|
| C1 | Trust strip enrichi Phase 2 (SOC2 + AI-Act + ISO 27001 + HDS + HIPAA) | 2-3 h |
| C2 | Page `/securite` ou `/trust-center` avec documentation AI-Act article 12 | 6-8 h |
| C3 | Sub-type Expert-comptable landing dédié `/expert-comptable` | 6-8 h |
| C4 | Témoignage cabinet canon (Family Office ou cabinet comptable) | 2-3 h |
| C5 | AI-Act countdown banner "Applicable 2 août 2026" | 2-3 h |

### Phase D — Self-Host Messaging + i18n EN/FR (Semaine W5+, 19-27 h, 4 tasks)

**Objectif** : 85% → 95% conformité Nexus.

| # | Task | Effort |
|---|---|---|
| D1 | Self-host messaging landing "Bare-Metal Zero-Knowledge" (verbatim L25674) | 4-5 h |
| D2 | i18n FR/EN minimum next-intl | 8-12 h |
| D3 | 3-ICP sister-symétrique link (Solaris/Nexus/Orbiter footer) | 3-4 h |
| D4 | English copy review copywriter natif | 4-6 h (external) |

### Total effort canon

| Phase | Effort | Délai | Conformité atteinte |
|---|---|---|---|
| A | 13-19 h | 2-3 jours | 9% → 35% |
| B | 29-41 h | 1-1.5 semaines | 35% → 65% |
| C | 18-25 h | 3-5 jours | 65% → 85% |
| D | 19-27 h | 3-4 jours + ongoing | 85% → 95% |
| **TOTAL** | **79-112 h = ~10-14 jours ouvrés** | **W1-W5+ (~2-3 semaines calendaires)** | **9% → 95%** |

### A0 HITL obligatoires (15 décisions bloquantes)

| Phase | # | Décision A0 |
|---|---|---|
| A | A0.1 | Choisir wording Hero parmi 3 options (A1) |
| A | A0.2 | Valider wording légal cabinets (A3) |
| A | A0.3 | Décider quels badges certified vs aspirational (A5) |
| B | A0.4 | Valider wording canon 5 tiers pricing (B1) |
| B | A0.5 | Décider taux EUR/USD live (B3) |
| B | A0.6 | Choisir direction artistique parmi 3 mood boards (B5) |
| B | A0.7 | Valider niveau détail Zero-PII 5 mécanismes (B7) |
| B | A0.8 | Décider rebrand copy "Stack private-by-default" — gros risque greenwashing (B8) |
| C | A0.9 | **CRITICAL** Lister badges VRAIMENT certifiés vs aspirational (C1) anti-greenwashing |
| C | A0.10 | Relecture avocat page sécurité (C2) |
| C | A0.11 | OK landing dédié expert-comptable (C3) |
| C | A0.12 | OK fictif vs réel témoignages (C4) |
| C | A0.13 | Confirmer date AI-Act 2026-08-02 (C5) |
| D | A0.14 | Valider self-host réellement shippable (D1) — gros blocker engineering |
| D | A0.15 | Valider stratégie SEO i18n + budget copywriter EN (D2 + D4) |

## D3 nuance : PIVOT ≠ REPLACEMENT

**Anti-pattern évité** : ce plan est un **PIVOT** (D4 no-hard-delete). OMK landing actuel a une **canon valide pour cible SMB opérationnel / Orbiter Tier 1-2** (Mobile First / Terrain, ops-led) — `ADR-ICP-ORBITER-001` sister canon RATIFIED 2026-06-24. 

**2 options A0 possibles** :

| Option | Description | Risque | Effort |
|---|---|---|---|
| **Option 1 — PIVOT** (recommandé canon-batch) | Transformer OMK actuel vers Nexus canon (4 phases A/B/C/D) | **9% → 95% conformité** + 15 A0 HITL + 10-14 jours | 79-112 h |
| **Option 2 — RÉ-ALLOUER** (D3 nuance) | Conserver OMK actuel comme Orbiter Tier 1-2 landing + créer NOUVEAU landing Nexus séparé | 0 régression OMK + 1 nouveau landing from scratch | 120-150 h (nouveau landing) |

**Recommandation Morty** (D7 anti-effondrement) : **Option 1 (PIVOT)** car (a) la stack OMK actuelle est déjà Next.js + Vercel, donc le pivot = 80% refonte copy + design, pas de reconstruction ; (b) la cible SMB actuel a peu de traction organique (3 mois en prod, peu de backlinks) donc le risque régression SEO = faible ; (c) le ROI = accès au marché 84 Trilliards € Family Office = énorme vs SMB générique.

**A0 décision finale requise** post Phase A (semaine W1).

## Conséquences

### Positives (D7 anti-effondrement canon)

- **D7 backup wiki** : 2 handoffs canon mirror (gap + plan) = D4 append-only, no-hard-delete
- **PIVOT aligné canon** : 4 phases mappées sur 4 semaines W1-W5+, conformité 9% → 95%
- **Sister canon 3-ICP** : Solaris/Nexus/Orbiter alignement cross-canonique
- **Pricing canon 4 tiers USD** : sister `ADR-AAAS-PRICING-001` AMENDED propagé
- **Marché 84 Trilliards €** : TAM Family Office ouvert = hook acquisition
- **AI-Act prêt avant 2026-08-02** : driver légal 6 semaines anticipé
- **D7 anti-effondrement** : rollback possible section par section via git

### Négatives (risques D6)

- **15 A0 HITL bloquants** = A0 escalations coût Phase B/D élevé (D7 cost-of-escalation)
- **B5 Visual identity refonte** = risque régression totale (8-12 h de design system) — A0 mood board obligatoire
- **B7 Zero-PII 5 mécanismes** = copy technique sensible, A0 vulgarisé vs expert
- **B8 SaaS messaging** = si stack réelle = SaaS public, rebrand copy = **greenwashing** (interdit sister `ADR-SOBER-002`)
- **C1 Badges compliance** = si pas certifié, **greenwashing légal** (sister `ADR-SOBER-002` Anti-Paperclip = no invent certifications)
- **D1 Self-host engineering** = pas shippable en 5 semaines = fallback copy honnête requis

### Mitigation

- **D7 cost-of-escalation** : 15 A0 HITL regroupés en 4 sessions A0 (1 par phase) plutôt que 15 escalations
- **D6 rollback par section** : git revert section par section si mood board B5 fail
- **D3 nuance Option 2** : si Option 1 explose Phase B, A0 peut basculer Option 2 (ré-allouer OMK → Orbiter + nouveau landing Nexus)
- **Sister Anti-Paperclip** : si stack réelle = SaaS public, **INTERDIT** de rebrand copy en "private-by-default" — fallback "**Architecture self-host-ready · Setup Q4 2026**" honnête

## Verification (D1 receipts sister scope)

| Critère | Source | D1 receipt | Confidence |
|---|---|---|---|
| Solaris LOCAL stack Next.js 16.2.6 | `package.json:12` | verbatim | HIGH |
| Solaris LOCAL 4 297 LOC TS/TSX/CSS | `find ... -name "*.tsx" -o -name "*.ts" -o -name "*.css"` | `wc -l` total = 4 297 | HIGH |
| Solaris LOCAL 18 TS/TSX | `src/` directory listing | 12 sections + 4 diagrams + 1 lib + 1 api | HIGH |
| Solaris LOCAL 72% conformité ICP Solaris | `solaris_omk_front_gap_analysis_2026-06-24.md` | score calculé 18/25 | HIGH |
| OMK PROD LIVE HTTP 200 | `curl -sI` | `HTTP/1.1 200 OK`, 74 803 bytes | HIGH |
| OMK PROD LIVE 9% conformité Nexus | `solaris_omk_front_gap_analysis_2026-06-24.md` | score calculé 3/35 | HIGH |
| OMK `/tarifs` 404 | `curl -sI https://omk-landing-page.vercel.app/tarifs` | `HTTP/1.1 404 Not Found` | HIGH |
| OMK devise EUR | `LeadForm.tsx` CA Annuel select | `<100k€`, `100k€-500k€`, etc. | HIGH |
| OMK 14 SaaS brandés | Section "Stack opérationnelle orchestrée" | Notion/Airtable/Make/n8n/Slack/Stripe/HubSpot/Pennylane/Webflow/OpenAI/Twilio/Calendly/Pipedrive/Zapier | HIGH |
| Nexus Tier 1 $750 Self-Host | `ADR-ICP-NEXUS-001:179` L25674 verbatim | canon sister | HIGH |
| Nexus Tier 2 $1000-1500 | `ADR-ICP-NEXUS-001:180` L61000 verbatim | canon sister | HIGH |
| Nexus Tier 3 $1500-2000+25% | `ADR-ICP-NEXUS-001:181` L25674 verbatim | canon sister | HIGH |
| Nexus Tier 4 $5K-50K MRR | `ADR-ICP-NEXUS-001:182` sister `ADR-AAAS-PRICING-001` Tier 5 | canon sister | HIGH |
| Persona "Expert méthodique" | `ADR-ICP-NEXUS-001:53-79` L21519 verbatim | canon sister | HIGH |
| Mantra "L'illusion de la complexité" | `ADR-ICP-NEXUS-001:84-98` L18408 verbatim | canon sister | HIGH |
| Marché 84 Trilliards € | `ADR-ICP-NEXUS-001:99-124` L19500 verbatim | canon sister | HIGH |
| Killer Feature "Zero-PII Agentic Governance" | `ADR-ICP-NEXUS-001:143-163` L19477-19580 verbatim | canon sister | HIGH |
| "Pas de SaaS public" Bare-Metal | `ADR-ICP-NEXUS-001:152` L19580 verbatim | canon sister | HIGH |
| AI-Act application 2 août 2026 | `ADR-ICP-NEXUS-001:147` | canon sister | HIGH |
| "détruit la Holding" Family Office | `ADR-ICP-NEXUS-001:104` L21780 verbatim | canon sister | HIGH |
| Transformation 4 phases | `omk_nexus_transformation_plan_2026-06-24.md` | 4 phases × 4-8 tasks = 22 tasks D1 | HIGH |
| 15 A0 HITL bloquants | `omk_nexus_transformation_plan_2026-06-24.md` | décompte 1 par task | HIGH |
| Effort total 79-112 h | `omk_nexus_transformation_plan_2026-06-24.md` | agrégation Phase A+B+C+D | HIGH |

## Cross-refs

- [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) — ICP Nexus 5 Piliers (RATIFIED 2026-06-24)
- [`ADR-ICP-SOLARIS-001`](./ADR-ICP-SOLARIS-001_icp-solaris-structuration.md) — ICP Solaris 5 Piliers (RATIFIED 2026-06-24)
- [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) — AaaS Pricing 5 Tiers USD (RATIFIED + AMENDED 2026-06-24)
- [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — AaaS Doctrine 3 Variants Solarpunk (RATIFIED 2026-06-21)
- [`ADR-OMK-004`](./ADR-OMK-004_pivot-supabase-cloud-vercel.md) — OMK Stack Pivot (RATIFIED 2026-06-19)
- [`ADR-OMK-005`](./ADR-OMK-005_tenant-isolation-guard.md) — Tenant Isolation Guard (RATIFIED 2026-06-20)
- [`ADR-SOBER-002`](../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) — Anti-Paperclip doctrine
- [`ADR-META-001`](../L0_Kernel_OS/ADR-META-001_anti-paresse-verify-before-assert.md) — Anti-Paresse D1-D8
- [`ADR-META-006`](../L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) — D6 Root Causes Catalog
- `wiki/hand_offs/solaris_omk_front_gap_analysis_2026-06-24.md` — Backup wiki D7 anti-effondrement (gap analysis)
- `wiki/hand_offs/omk_nexus_transformation_plan_2026-06-24.md` — Backup wiki D7 anti-effondrement (plan détaillé)

## D6 Lessons shipped (2026-06-24)

| # | Lesson | Source |
|---|---|---|
| 32 | **Landing PROD LIVE peut avoir 0% alignement ICP canon sister sans détection** — audit gap-analysis D1 obligatoire | `solaris_omk_front_gap_analysis_2026-06-24.md` |
| 33 | **Stack Notion+Airtable+Make+14 SaaS publics = anti-pattern verbatim "Pas de SaaS public" L19580** — landing doit refléter canon Stack | `solaris_omk_front_gap_analysis_2026-06-24.md` Phase A8 |
| 34 | **Page `/tarifs` footer link mais 404 = anti-pattern UI** (lien mort > absence de lien) | `solaris_omk_front_gap_analysis_2026-06-24.md` |
| 35 | **PIVOT vs REPLACEMENT** (D3 nuance) : 2 options A0 = transformer OMK OU ré-allouer vers Orbiter + nouveau landing | ADR §D3 nuance |
| 36 | **15 A0 HITL bloquants regroupés en 4 sessions** (1 par phase) = D7 cost-of-escalation mitigation | `omk_nexus_transformation_plan_2026-06-24.md` Phase D7 |
| 37 | **Sister Anti-Paperclip** : INTERDIT greenwashing badges compliance ou "private-by-default" copy si stack réelle = SaaS public | `ADR-SOBER-002` cross-ref |

## D7 anti-effondrement canon

- **2 wiki handoffs mirror** : `solaris_omk_front_gap_analysis_2026-06-24.md` + `omk_nexus_transformation_plan_2026-06-24.md`
- **1 ADR PROPOSED** sister scope (ce fichier)
- **1 log entry** : `wiki/log.md` 2026-06-24 (5ème entrée sister batch L2 Solaris)
- **D4 no-hard-delete** : 0 modification aux ADRs canon RATIFIED sister, 0 modification aux handoffs existants, 0 modification au log.md historique
- **A0 escalations regroupées** : 15 HITL en 4 sessions A0 (1 par phase)
- **Rollback possible** : git revert section par section si mood board Phase B5 fail

---

**RATIFIED 2026-06-24 par A0 verbal GO chat (post-canon-batch Acquisition Doctrine + 2 guides Premium + 3 guides MedVie canon) — Canon OMK → Nexus transformation fixé 1an+ minimum**. Backup wiki 2 handoffs + sister ADRs canon maintenus. D3 nuance PIVOT ≠ REPLACEMENT maintenu (Option 2 ré-allocation possible si Phase B explose). Sister canon canon principal : [`ADR-AAAS-ACQUISITION-DOCTRINE-001`](./ADR-AAAS-ACQUISITION-DOCTRINE-001_aaas-acquisition-doctrine.md) (25 455 chars, doctrinal sister direct — Acquisition-First MedVie vs Structuration-First A0 OS).
