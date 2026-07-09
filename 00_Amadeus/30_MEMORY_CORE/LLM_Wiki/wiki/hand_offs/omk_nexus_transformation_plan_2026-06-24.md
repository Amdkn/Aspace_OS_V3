---
id: handoff-omk-nexus-transformation-plan-2026-06-24
title: Plan de Fixation OMK → Nexus Tier 4 (4 phases A/B/C/D)
date: 2026-06-24
author: A1 Morty (executed by Claude Code A2)
status: D1-verified, sister ADR draft in parallel (ADR-OMK-NEXUS-TRANSFORM-001 PROPOSED)
domain: L2 Business OS / AaaS Doctrine / Front-End / Transformation canon
sister_adrs:
  - ADR-OMK-NEXUS-TRANSFORM-001 (PROPOSED, sister plan détaillé)
  - ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24, Pilier 1-5)
  - ADR-AAAS-PRICING-001 (RATIFIED + AMENDED 2026-06-24, 5 Tiers USD)
  - ADR-ICP-SOLARIS-001 (RATIFIED 2026-06-24, sister canon)
related: ADR-L2-AAAS-001, JTBD-ICP-SOLARIS-001, ADR-OMK-004, ADR-SOBER-002
total_effort_estimate: 18.5-26.5 h = ~3-4 jours (Phase A) + 1-1.5 semaines (B) + 3-5 jours (C) + ongoing (D)
---

# Plan de Fixation OMK → Nexus Tier 4 (4 phases A/B/C/D)

> **D7 anti-effondrement backup** : ce plan est la **mémoire opérationnelle D1-vérifiée** du chemin de transformation OMK vers Nexus Tier 4. Sister `ADR-OMK-NEXUS-TRANSFORM-001` PROPOSED contient la ratification canon. Source gap-analysis : `solaris_omk_front_gap_analysis_2026-06-24.md`.

> **D3 nuance** : ce plan est un **PIVOT** (D4 no-replacement). OMK a sa propre canon valide (SMB/Orbiter) ; le pivot vers Nexus = re-ciblage + restylage + re-pricing, pas destruction.

---

## Phase A — Quick Wins Persona + Messaging (Semaine W1, 4-6 tasks, < 1 jour chacune)

**Objectif Phase A** : passer le landing OMK de **9% conformité Nexus** à **~35%** (sections persona + mantra + 1 sub-type). Faible effort, fort impact sur le trafic organique "expert-comptable / family office".

| # | Task | Fichier(s) à modifier | Owner | Effort | D6 root cause si blocker | D7 backup wiki |
|---|---|---|---|---|---|---|
| **A1** | **Hero tagline pivot** : remplacer "Arrêtez de travailler DANS votre entreprise" par **"L'OS Expert / L'OS de la Conformité"** (verbatim `ADR-ICP-NEXUS-001:25651-25740`) ou "Arrêtez de subir. Sanctuarisez votre expertise." (aligné `ADR-ICP-NEXUS-001:25160-25314` "Citadelle du Savoir") | `app/page.tsx` Hero section + metadata `<title>` + `<meta description>` | A3 sub-agent (A2) | **2-3 h** | Tagline trop générique actuelle ne matche aucun ICP canon → A0 HITL sur le wording exact (3 options A0 choisit) | `etude_marche_the_builders_2026_canon_2026-06-24.md` (study verbatim) |
| **A2** | **Mantra doctrinal** : ajouter une section "Mantra" (juste sous Hero) avec **"L'illusion de la complexité"** (verbatim L18408) + 1-phrase explication "Nexus contre le Paradoxe de la Complexité" | Nouveau `components/sections/MantraSection.tsx` + insertion `app/page.tsx` entre Hero et Trust strip | A3 sub-agent (A2) | **3-4 h** | Rédaction copy doit citer verbatim → sister `JTBD-ICP-SOLARIS-001` style guide | `solaris_omk_front_gap_analysis_2026-06-24.md` (Phase A mandate) |
| **A3** | **5 sub-types personas** : remplacer la section "Stack opérationnelle orchestrée" (14 SaaS brandés) par **"5 cabinets. Un seul système."** listant les 5 sub-types Nexus canon (Expert-comptable / Avocat / Family-Office / Coach / Cabinet-médical verbatim L21519) avec 1 tagline par cabinet | Réduire `app/page.tsx` section Stack → remplacer par `<SubTypesSection />` + 5 cards | A3 sub-agent (A2) | **4-5 h** | Naming cabinet = trademark check requis (avocat=Ordre, médecin=Ordre) → A0 HITL sur le wording légal | `ADR-ICP-NEXUS-001:63-70` 5 sub-types canon |
| **A4** | **CTA async pivot** : remplacer "Réserver mon audit stratégique · Visio" par **"Recevoir mon audit 24h · Sans visio · Sans engagement"** (aligné Solaris `#vault-form` async model) | `components/LeadForm.tsx` + Hero + FinalCTA + Topbar sticky | A3 sub-agent (A2) | **2-3 h** | L'Expert méthodique canon déteste les visio (verbatim L18408) → friction actuelle = bounce | `Hero.tsx:59-64` Solaris sister async CTA |
| **A5** | **Trust strip enrichi** : remplacer "Conforme RGPD · données européennes" par **"RGPD · AI-Act ready · Zero-PII by design · Données européennes"** (4 badges, aligné `ADR-ICP-NEXUS-001` Pilier 5 mécanisme 5 "Zero-PII Sanitization") | `app/page.tsx` Trust strip | A3 sub-agent (A2) | **1-2 h** | Aucun des 4 badges n'est auditable publiquement → A0 HITL sur ce qui est certifié vs aspirational (anti-pattern greenwashing) | `ADR-ICP-NEXUS-001:144-159` 5 mécanismes Pilier 5 |
| **A6** | **Nova rebrand** : renommer la section "Flotte IA" en **"Nova · Agent Vocal Conforme AI-Act"** (ajout mention conformité) + changer démo transcript "Madame Léger · facturation cabinet" (déjà aligné sub-type Expert-comptable) | `app/page.tsx` section Nova + `components/NovaDemo.tsx` | A3 sub-agent (A2) | **1-2 h** | "Conforme AI-Act" doit être vrai → si Nova n'est pas auditable, fallback "AI-Act compatible architecture" + A0 HITL | `Nova` live demo D1 receipt text "facturation de votre cabinet" = déjà sub-type canon |

**Total Phase A** : **13-19 h = ~2-3 jours ouvrés** (1 owner A3 sub-agent en parallèle sur A1+A2+A6, 1 owner sur A3+A4, 1 owner sur A5).

**A0 HITL Phase A** (3 décisions requises) :
- A0 choisit entre 3 wording options pour Hero (A1)
- A0 valide wording légal cabinets (A3)
- A0 décide quels badges sont certified vs aspirational (A5)

**D7 anti-effondrement Phase A** : ce handoff = backup live. Si git push fail, A3 revert aux sections actuelles. Pas de hard-delete.

---

## Phase B — Pricing Canon Refresh + Visual Identity Pivot (Semaine W2-W3, 5-8 tasks, 1-3 jours chacune)

**Objectif Phase B** : passer de **9% à ~65% conformité Nexus** = (1) pricing canon Nexus visible (4 tiers USD), (2) restylage palette "Citadelle / Souverain", (3) création page `/tarifs` canon.

| # | Task | Fichier(s) à modifier | Owner | Effort | D6 root cause si blocker | D7 backup wiki |
|---|---|---|---|---|---|---|
| **B1** | **Implémenter `/tarifs` page** (actuellement 404) avec les **4 tiers canon Nexus USD** ($750 / $1000-1500 / $1500-2000+25% / $5K-50K MRR verbatim `ADR-ICP-NEXUS-001:177-183`) | Nouveau `app/tarifs/page.tsx` + composants `PricingTable.tsx` (4 cards) + `TiersComparison.tsx` (feature matrix) | A3 sub-agent (A2) | **6-8 h** | Page `/tarifs` 404 = deal-breaker A0 verbal GO sister scope → A0 HITL sur wording canon 5 tiers (Hypothèse A USD) | `ADR-AAAS-PRICING-001:175-198` pricing canon |
| **B2** | **Footer link fix** : `/tarifs` footer link pointe vers `/tarifs` (404 actuellement) — fix routing Next.js | `components/Footer.tsx` (lien + breadcrumb) | A3 sub-agent (A2) | **0.5 h** | Lien mort = trust break (D6 #34) | Fix immédiat sans blocker |
| **B3** | **Pricing toggle EUR/USD** : ajouter switch EUR ↔ USD avec canon USD par défaut (post-accuponcture AMENDED 2026-06-24) | `components/PricingTable.tsx` + state `useState('USD')` | A3 sub-agent (A2) | **2-3 h** | Taux de change EUR/USD non-archivé canon → A0 HITL sur taux live (Stripe canon) | `ADR-AAAS-PRICING-001:34-42` EUR historique superseded |
| **B4** | **Hero pricing snippet** : ajouter sous le Hero "**À partir de $750/an · Sans engagement · 14 jours d'essai**" (aligné Solaris `$1,555` snippet) | `app/page.tsx` Hero section (entre sub et CTA) | A3 sub-agent (A2) | **1-2 h** | Pricing visible = test du canon AaaS (pas de friction visio) → alignement Solaris sister | `Hero.tsx:42-44` Solaris value prop sister |
| **B5** | **Visual identity pivot** : remplacer la palette moderne (emerald/blue/violet/pink `#34D399 #3B82F6 #8B5CF6 #EC4899`) par palette **"Citadelle / Souverain"** : `--accent: #c9a86b` (or canon sobre) + `--bg: #0a0d12` (gris-bleu nuit) + `--flare: #5e3023` (rouge sobre). Sister à `globals.css:7-32` Solaris MAIS shift vers gravité Nexus | `app/globals.css` + tous les composants utilisant Tailwind utility classes → migrate vers CSS variables | A3 sub-agent (A2) | **8-12 h** | Refonte design system lourde → A0 HITL sur direction artistique (3 mood boards proposés) | `globals.css:7-32` Solaris palette sister reference |
| **B6** | **Typography shift** : remplacer **Space Grotesk** (display) par **Spectral / Source Serif** (gravité expert) OU garder Space Grotesk mais +bold + uppercase tracking. Remplacer **Inter** (body) par **Inter Display** ou **IBM Plex Serif** pour body expert | `next/font` config + `globals.css` | A3 sub-agent (A2) | **3-4 h** | License font check (Spectral/IBM Plex open-source OK) | `globals.css:26-28` Solaris font tokens |
| **B7** | **Killer Feature "Zero-PII" section** : remplacer la section "Nova Flotte IA" générique par une section **"Zero-PII Agentic Governance · 5 mécanismes"** illustrant les 5 mécanismes canon (Action Space Bounding / Sandboxing Bare-Metal / HITL Dynamique légal / Traçabilité AI-Act / Zero-PII Sanitization) avec icônes SVG sobres | Nouveau `components/sections/ZeroPIIGovernance.tsx` (5 cards) + insertion `app/page.tsx` après Business OS | A3 sub-agent (A2) | **6-8 h** | 5 mécanismes = copywriting long → A0 HITL sur niveau de détail (vulgarisé vs expert verbatim) | `ADR-ICP-NEXUS-001:144-159` 5 mécanismes Pilier 5 verbatim |
| **B8** | **Hero kill SaaS-public messaging** : retirer la mention "Stack opérationnelle orchestrée" (14 SaaS brandés = anti-pattern verbatim L19580) OU la transformer en "**Stack private-by-default · Bring-your-own-cloud**" | `app/page.tsx` section Stack → `PrivateStack.tsx` (optionnel) | A3 sub-agent (A2) | **2-3 h** | Si la stack réelle OMK est Notion+Airtable+Make → A0 HITL sur rebranding copy (peut induire erreur marketing) | `ADR-ICP-NEXUS-001:152` verbatim "Pas de SaaS public" |

**Total Phase B** : **29-41 h = ~1-1.5 semaines** (2 owners A3 en parallèle, front-end + design).

**A0 HITL Phase B** (5 décisions) :
- A0 valide wording canon 5 tiers pricing (B1)
- A0 décide taux EUR/USD (B3)
- A0 choisit direction artistique parmi 3 mood boards (B5)
- A0 valide niveau détail Zero-PII 5 mécanismes (B7)
- A0 décide rebrand copy "Stack private-by-default" (B8 — gros risque si stack réelle est SaaS public)

**D7 anti-effondrement Phase B** : rollback git possible section par section. Si B5 (palette) fail → revert CSS + conserver Inter+Space Grotesk (status quo OMK).

---

## Phase C — Conformité Badges + Trust Signals (Semaine W4, 3-5 tasks, 1-2 jours chacune)

**Objectif Phase C** : passer de **65% à ~85% conformité Nexus** = (1) badges conformité critiques (SOC2/AI-Act/HIPAA), (2) certifications page, (3) trust center link.

| # | Task | Fichier(s) à modifier | Owner | Effort | D6 root cause si blocker | D7 backup wiki |
|---|---|---|---|---|---|---|
| **C1** | **Trust strip enrichi Phase 2** : ajouter 4-6 badges supplémentaires : **"SOC 2 Type II · AI-Act ready · ISO 27001 · Hébergement HDS · HIPAA compatible · Backup 3-2-1"** (aligné Expert méthodique verbatim L21780 "détruit la Holding") | `components/TrustStrip.tsx` + images SVG badges | A3 sub-agent (A2) | **2-3 h** | Aucun badge n'est auditable publiquement → A0 HITL urgent sur **ce qui est VRAIMENT certifié** vs aspirational (anti-greenwashing légal) | Sister `ADR-SOBER-002` Anti-Paperclip doctrine (no greenwashing) |
| **C2** | **Page `/securite` ou `/trust-center`** : créer page dédiée avec documentation sécurité (AI-Act article 12 conformité, registre traitement, RBAC, chiffrement, backup, incident response) | Nouveau `app/securite/page.tsx` + `components/SecurityDocs.tsx` (4-6 sections) | A3 sub-agent (A2) | **6-8 h** | Documentation sécu = légal sensible → A0 HITL sur relecture avocat | `ADR-ICP-NEXUS-001:154` mécanisme 4 "Traçabilité AI-Act article 12" |
| **C3** | **Sub-type Expert-comptable landing dédié** : créer variante `/expert-comptable` (ou sous-section landing) avec messaging spécifique "**OMK Nexus pour cabinets comptables · Anti-blanchiment · RGPD · AI-Act · Liaison Pennylane**" | Nouveau `app/expert-comptable/page.tsx` + `components/CabinetComptableHero.tsx` | A3 sub-agent (A2) | **6-8 h** | Sub-type spécifique = 1 des 5 canon (verbatim L21519) → ouvre funnel d'acquisition verticale | `ADR-ICP-NEXUS-001:64` sub-type 1 verbatim |
| **C4** | **Témoignage cabinet canon** : ajouter 1-2 témoignages typés (Family Office OU cabinet comptable) — pas de nom réel requis, mais persona-accurate (verbatim L19477 "Family Office détruit la Holding") | `components/Testimonials.tsx` | A3 sub-agent (A2) | **2-3 h** | Témoignages = preuve sociale canon → A0 HITL sur fictif vs réel (citer client OK?) | `etude_marche_the_builders_2026_canon_2026-06-24.md` étude |
| **C5** | **AI-Act countdown banner** : ajouter bannière countdown "**AI-Act applicable 2 août 2026 · Préparez votre cabinet · Audit gratuit 14 jours**" (driver légal cité verbatim) | `components/AIActBanner.tsx` + insertion topbar sticky | A3 sub-agent (A2) | **2-3 h** | Date AI-Act = **2026-08-02** réel (à vérifier) → A0 HITL confirmation | `ADR-ICP-NEXUS-001:147` "driver légal application totale août 2026" |

**Total Phase C** : **18-25 h = ~3-5 jours ouvrés** (1-2 owners A3).

**A0 HITL Phase C** (4 décisions) :
- A0 liste badges VRAIMENT certifiés vs aspirational (C1) — **CRITICAL anti-greenwashing**
- A0 relecture avocat page sécurité (C2)
- A0 OK landing dédié expert-comptable (C3)
- A0 OK fictif vs réel témoignages (C4)
- A0 confirme date AI-Act 2026-08-02 (C5)

**D7 anti-effondrement Phase C** : si badges pas certifiés → fallback "**compatible architecture**" wording, retirer badges. Anti-pattern greenwashing détecté = rollback immédiat.

---

## Phase D — Self-Host Messaging + i18n EN/FR (Semaine W5+, 3-4 tasks, ongoing)

**Objectif Phase D** : passer de **85% à ~95% conformité Nexus** = (1) self-host messaging explicite, (2) i18n FR+EN minimum (cible Family Offices cross-border), (3) sister 3-ICP link vers Solaris/Orbiter.

| # | Task | Fichier(s) à modifier | Owner | Effort | D6 root cause si blocker | D7 backup wiki |
|---|---|---|---|---|---|---|
| **D1** | **Self-host messaging landing** : section "**Self-Host Souverain · Bare-Metal Zero-Knowledge**" (verbatim L25674) avec 3 cards : "Cloud géré OMK $750/an" vs "Self-Host sur votre infra" vs "Franchise Whitelabel $1500/an + 25%" | Nouveau `components/sections/SelfHostSection.tsx` (3 cards) | A3 sub-agent (A2) | **4-5 h** | Self-host réel = engineering setup Docker/OnPrem → A0 HITL sur ce qui est **vraiment shippable** vs marketing | `ADR-ICP-NEXUS-001:177-194` 4 tiers canon |
| **D2** | **i18n FR/EN minimum** : next-intl ou next-i18next pour landing `/en/` + `/` (FR par défaut). Traduire Hero, Mantra, 5 sub-types, Pricing, CTA. Pas besoin de traduire `/securite` etc. Phase 1 = landing only | `app/[locale]/page.tsx` + `i18n/fr.json` + `i18n/en.json` + `next.config.js` | A3 sub-agent (A2) | **8-12 h** | i18n = refonte routing → risque régression SEO FR existant → A0 HITL sur stratégie SEO (redirect 301) | Cible FR+Suisse+BE+LUX verbatim L74 |
| **D3** | **3-ICP sister-symétrique link** : ajouter footer/section "**L'écosystème AaaS**" avec 3 cards (Solaris 🎨 / Nexus ⚖️ / Orbiter 🏗️) pointant vers les 3 landings canon. Sister Solaris `SOLARIS_HOLDING` data.ts:309-333 | Nouveau `components/sections/SisterICPs.tsx` (3 cards) | A3 sub-agent (A2) | **3-4 h** | A0 HITL sur URLs sister (solaris.factory ? + nouvelle URL Orbiter) | `ADR-L2-AAAS-001` 3 Variants canon |
| **D4** | **English landing copy review** : un copywriter EN natif review les traductions pour le marché US/UK Family Offices (cible plus large post-pivot) | Task externe (Upwork/Fiverr) ou A0 HITL sur budget | A0 HITL | **4-6 h** (external copywriter) | Copy EN = qualité critique pour cible cross-border → A0 budget décision | Phase D4 = ongoing Q3 2026 |

**Total Phase D** : **19-27 h = ~3-4 jours ouvrés** (1-2 owners A3 + A0 HITL ongoing).

**A0 HITL Phase D** (3 décisions) :
- A0 valide self-host réellement shippable (D1) — gros blocker engineering
- A0 valide stratégie SEO i18n (D2)
- A0 budget copywriter EN (D4)

**D7 anti-effondrement Phase D** : si D1 self-host engineering pas prêt → fallback copy "**Architecture self-host-ready · Setup Q4 2026**" (honnête) sans claim shippable.

---

## Synthèse effort + risks

| Phase | Effort | Délai | Owner count | A0 HITL count | Conformité Nexus atteinte |
|---|---|---|---|---|---|
| **A** (Quick wins persona+msg) | 13-19 h | 2-3 jours | 1-2 A3 | 3 décisions | 9% → **35%** |
| **B** (Pricing+visual+killer) | 29-41 h | 1-1.5 semaines | 2 A3 | 5 décisions | 35% → **65%** |
| **C** (Conformité+trust) | 18-25 h | 3-5 jours | 1-2 A3 | 4 décisions | 65% → **85%** |
| **D** (Self-host+i18n) | 19-27 h | 3-4 jours | 1-2 A3 + external | 3 décisions | 85% → **95%** |
| **TOTAL** | **79-112 h = ~10-14 jours ouvrés (~2-3 semaines calendaires)** | **W1-W5** | 2-3 A3 peak | **15 décisions A0** | **9% → 95%** |

### Risques majeurs Phase B (CRITICAL)

1. **B5 Visual identity refonte** = 8-12 h + risque régression totale. **A0 HITL mood board obligatoire** avant code.
2. **B7 Zero-PII section** = copy technique sensible. **A0 HITL vulgarisé vs expert** avant publication.
3. **B8 SaaS messaging** = si stack réelle = SaaS public, **rebrand copy = greenwashing**. A0 doit décider vérité marketing.

### Risques majeurs Phase C (CRITICAL)

1. **C1 Badges compliance** = si pas certifié, **greenwashing légal**. Sister `ADR-SOBER-002` Anti-Paperclip doctrine = **interdit d'inventer des certifications**.

### Sister deliverable

- **ADR-OMK-NEXUS-TRANSFORM-001 PROPOSED** : `_SPECS/ADR/L2_Business_OS/ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md` (status PROPOSED → target RATIFIED 2026-07-03)
- **D7 wiki backup** : ce handoff + `solaris_omk_front_gap_analysis_2026-06-24.md` = 2 handoffs canon mirror

---

**Auteur** : A1 Morty (Claude Code A2) — 2026-06-24 — sister de `solaris_omk_front_gap_analysis_2026-06-24.md`
**D1 receipts cumulés** : 4 paths canon + 5 ADR sister refs + 4 phases × 4-8 tasks = 22 tasks D1-spec + 15 A0 HITL flags
**Total effort** : 79-112 h sur 5 semaines (W1-W5+)
**Sister canon status** : `ADR-ICP-NEXUS-001` RATIFIED + `ADR-AAAS-PRICING-001` RATIFIED+AMENDED + `ADR-ICP-SOLARIS-001` RATIFIED
**A0 HITL YES** : **15 décisions bloquantes** = aucun phase ne peut démarrer sans A0 verbal GO
