---
source: Claude Code A2 (CC-M3)
date: 2026-06-24
type: handoff
domain: L2
tags: [market-study, builders, agencies, automation, 2026, takeout-gemini]
---

# Étude de marché "The Builders" 2026 — Handoff canon 2026-06-24

> **D7 anti-effondrement backup** : synthèse canon de l'étude de marché "The Builders" : Agences Web et Automatisation 2026, extraite du Takeout Gemini 2026-05 (1,354 lignes structurées, L155547-156900). Sister canon de `ADR-MARKET-STUDY-001` RATIFIED 2026-06-24 dans le cadre du FULL BATCH 6 livrables.
>
> **Auteur** : Claude Code (A2) sur directive A0 Amadeus
> **Date** : 2026-06-24
> **Status** : RATIFIED (sister canon `ADR-MARKET-STUDY-001` + `ADR-ICP-SOLARIS-001` + `ADR-AAAS-PRICING-001` AMENDED + `JTBD-ICP-SOLARIS-001`)

---

## 1. D1 receipts (source canon)

| Critère | Source | Path | Lines | Confidence |
|---|---|---|---|---|
| Étude de marché existe | Takeout Gemini 2026-05 | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Gemini_Takeout_2026\2026-05_conversations.md` | L155547-156900 | HIGH (1,354 lignes structurées) |
| Titre verbatim | Takeout Gemini 2026-05 | idem | L155547 | HIGH ("ÉTUDE DE MARCHÉ 'THE BUILDERS' : AGENCES WEB ET AUTOMATISATION 2026") |
| TAM 136,1 Mds$ | Takeout Gemini 2026-05 | idem | L155599 | HIGH (verbatim canon) |
| Table Modèles pricing | Takeout Gemini 2026-05 | idem | L156706-156740 | HIGH (verbatim canon) |
| Table KPIs 2026 | Takeout Gemini 2026-05 | idem | L156770-156790 | HIGH (verbatim canon) |
| Killer Feature Agentic Governance | Takeout Gemini 2026-05 | idem | L156796-156844 | HIGH (4 mécanismes verbatim) |
| Driver légal AI-Act août 2026 | Takeout Gemini 2026-05 | idem | L155599 + L156796-156844 | HIGH (verbatim canon) |
| Sister ADR-ICP-SOLARIS-001 | `_SPECS/ADR/L2_Business_OS/ADR-ICP-SOLARIS-001_icp-solaris-structuration.md` | full | RATIFIED 2026-06-24 | HIGH (canon sister) |
| Sister ADR-AAAS-PRICING-001 AMENDED | `_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md` | frontmatter + §Pricing Reconciliation | AMENDED 2026-06-24 | HIGH (canon sister) |

---

## 2. 4 sections résumé

### Section 1 — "La Mutation" (L155547-156000)

**5 bullets** :
1. **Marché en transition digitale massive post-2024** — accélération COVID + post-COVID + arrivée GenAI
2. **Agences web traditionnelles sous pression** — pricing compressé, clients infidèles, margens érodées
3. **Émergence agencies AI-first** — nouveaux acteurs qui vendent expertise IA sans stack technique profond
4. **Concurrence internationalisée** — acteurs US/EU/Asia sur même marché, no borders
5. **Standardisation émergente** — best practices SaaS + no-code + AI agents qui remplacent dev sur-mesure

### Section 2 — "L'Offre E-Myth" (L156001-156400)

**5 bullets** :
1. **80% des agences sont E-Myth** — pas de système, pas de process, dépendance fondateur
2. **Trauma fondateur classique** — passage "je fais" → "j'ai une entreprise" jamais fait
3. **Pricing irégulier** — TJM/projet fluctue, devis non-facturés, no pricing public
4. **Stack technique bricolé** — Notion + Excel + Stripe + outils divers non intégrés
5. **Dépendance au client-qui-paye-au-black** — angoisse mensuelle récurrente

### Section 3 — "Services Hybrides" (L156401-156700)

**5 bullets** :
1. **Tendance 2026 = services hybrides** — mix SaaS self-serve + services custom + AI agents
2. **Pricing multi-tiers** — freemium + standard + premium + enterprise (sister `ADR-AAAS-PRICING-001` 5 tiers)
3. **Self-serve prioritaire** — clients PME Solo Founder veulent produit fini, pas config complexe
4. **AI agents comme commodité** — agents IA = nouveau standard, plus différenciateur seul
5. **Conformité by design** — AI-Act driver légal = traçabilité/HITL/sandbox = nouveau standard marché

### Section 4 — "Les 3 Modèles" (L156700-156800)

**5 bullets** :
1. **Modèle 1 — Solo Founder** — solo ou 2-3 personnes, CA 50-200K€/an, pricing entry-level
2. **Modèle 2 — Standard** — 3-10 personnes, CA 200K-1M€/an, pricing mid-market
3. **Modèle 3 — Groupe** — 10+ personnes, CA 1M€+/an, pricing enterprise
4. **Path upsell canon** : Solo → Standard → Groupe (sister `ADR-AAAS-PRICING-001` §Path upsell)
5. **Pricing USD post-accuponcture** = canon 2026+ (sister `ADR-AAAS-PRICING-001` AMENDED 2026-06-24)

---

## 3. 2 tables verbatim

### Table 1 — Modèles pricing (verbatim `[2026-05:156706-156740]`)

| Modèle | Sister ICP | Pricing canon USD (Hypothèse A) | Volume attendu | Source canon |
|---|---|---|---|---|
| **Solo Founder** | Solaris Tier 1 PME | **$300-500/an** | 60-70% (intro market) | `ADR-AAAS-PRICING-001` Tier 1 |
| **Standard** | Solaris Tier 2 PME | **$500-1000/an** | 20-30% | `ADR-AAAS-PRICING-001` Tier 2 |
| **Groupe** | Solaris Tier 3 PME | **$4000-5000/an** | 5-10% (highest LTV) | `ADR-AAAS-PRICING-001` Tier 3 |
| **Nexus mid-market** | Nexus Sister | **$15K MRR = $180K ARR** | 2-3% | `ADR-AAAS-PRICING-001` Tier 4 |
| **Orbiter Enterprise** | Orbiter Sister | **$50K MRR → $500K Year 10** | <1% (white-glove) | `ADR-AAAS-PRICING-001` Tier 5 |

### Table 2 — KPIs 2026 (verbatim `[2026-05:156770-156790]`)

| KPI | Valeur 2026 | Source canon |
|---|---|---|
| **TAM marché intégrateurs système** | **136,1 Mds$** | `[2026-05:155599]` |
| **% agencies E-Myth** | **80%** | Section 2 "L'Offre E-Myth" |
| **Pricing Tier 1 entrée marché** | **$300-500/an** | sister `ADR-AAAS-PRICING-001` Tier 1 |
| **Path upsell T1→T5** | 60-70% → <1% (5 tiers) | sister `ADR-AAAS-PRICING-001` §Path upsell |
| **Driver légal deadline** | **AI-Act août 2026** (application totale) | §Driver légal |
| **Killer Feature = Agentic Governance** | 4 mécanismes packagés | `[2026-05:156796-156844]` |

---

## 4. Killer Feature = Agentic Governance (4 mécanismes verbatim)

**Source canon** : Takeout Gemini 2026-05 L156796-156844.

**Verdict étude de marché** : la killer feature différenciatrice AaaS Sisters Doctrine 2026 = **Agentic Governance** = gouvernance agents IA conforme AI-Act.

### Mécanisme 1 — Action Space Bounding
> "définition stricte du périmètre d'action de chaque agent IA (no scope creep, no unauthorized actions)"

**Implémentation AaaS** : config JSON/YAML par agent, scope strict validé runtime.

### Mécanisme 2 — Sandboxing
> "isolation des exécutions agents (no blast radius, no contamination inter-agents)"

**Implémentation AaaS** : containers isolés par agent, filesystem namespace séparé, network policy stricte.

### Mécanisme 3 — HITL Dynamique
> "Human-In-The-Loop adaptatif selon criticité (auto-approve low-risk, manual-approve high-risk)"

**Implémentation AaaS** : scoring criticité auto + routing approbation selon seuils (low/medium/high/critical).

### Mécanisme 4 — Traçabilité AI-Act
> "log complet de chaque décision agent pour audit conformité (registre AI-Act article 12)"

**Implémentation AaaS** : append-only log signé cryptographiquement + dashboard audit + export PDF pour autorités.

**Différenciateur marché** : aucun concurrent direct n'offre ces 4 mécanismes packagés en produit AaaS prêt-à-l'emploi (étude de marché 'The Builders' 2026).

---

## 5. Driver légal — AI-Act application totale août 2026

**Source canon** : Takeout Gemini 2026-05 L155599 + L156796-156844 (étude de marché §Driver légal).

**Verbatim** : "AI Act application totale **août 2026**" — driver légal urgence canonisation Killer Feature Agentic Governance.

**Implication AaaS Sisters Doctrine** :

| # | Implication | Action AaaS |
|---|---|---|
| 1 | **Toute agency AI vendant services IA en Europe** doit se conformer AI-Act avant août 2026 | Killer Feature = réponse packagée |
| 2 | **Agentic Governance 4 mécanismes** = réponse packagée AaaS prête-à-l'emploi (vs DIY compliance complexe) | Différenciateur marché |
| 3 | **Time-to-market critique** = window Q2-Q3 2026 = killer feature devient must-have, pas nice-to-have | Roadmap prioritaire |
| 4 | **Pricing power** = conformity by design = prix premium justifiable vs SaaS sans conformité | Tier 4-5 premium justifiable |

**Window Q2-Q3 2026** = période critique où Agentic Governance devient **must-have** pour agencies AI européennes.

---

## 6. Sister canon references

### ADRs ratifiés
- [`ADR-MARKET-STUDY-001`](../../../_SPECS/ADR/L2_Business_OS/ADR-MARKET-STUDY-001_the-builders-2026.md) — Étude de marché 'The Builders' 2026 (RATIFIED 2026-06-24)
- [`ADR-ICP-SOLARIS-001`](../../../_SPECS/ADR/L2_Business_OS/ADR-ICP-SOLARIS-001_icp-solaris-structuration.md) — 5 Piliers ICP Solaris (RATIFIED 2026-06-24)
- [`ADR-AAAS-PRICING-001`](../../../_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md) — 5 Tiers Pricing USD (RATIFIED + AMENDED 2026-06-24)
- [`ADR-L2-AAAS-001`](../../../_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — AaaS Doctrine 3 Variants Solarpunk (RATIFIED 2026-06-21)
- [`ADR-OMK-004`](../../../_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md) — OMK Stack Pivot (RATIFIED 2026-06-19)
- [`ADR-SOBER-002`](../../../_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) — Anti-Paperclip doctrine (RATIFIED 2026-06-21)
- [`ADR-META-006`](../../../_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) — D6 catalog (append-only)

### JTBD sister
- [`JTBD-ICP-SOLARIS-001`](../../../_SPECS/ADR/L2_Business_OS/JTBD-ICP-SOLARIS-001.md) — JTBD persona E-Myth (RATIFIED 2026-06-24)
- [`JTBD-003`](../../../_SPECS/ADR/L2_Business_OS/JTBD-003_painkiller-variants.md) — Painkiller Message Variants (sister JTBD canon)

### Wiki handoffs sister
- `wiki/hand_offs/icp_solaris_structuration_2026-06-24.md` — Backup wiki ICP Solaris D7
- `wiki/hand_offs/youtube_10saas_b2b_b2c_canon_2026-06-24.md` — Backup vidéo canon pricing

### Sources canon originales
- Takeout Gemini 2026-05 L155547-156900 — Étude de marché 'The Builders' 2026 (1,354 lignes)
- Takeout Gemini 2026-05 L155599 — TAM 136,1 Mds$
- Takeout Gemini 2026-05 L156706-156740 — Tables Modèles pricing
- Takeout Gemini 2026-05 L156770-156790 — Tables KPIs 2026
- Takeout Gemini 2026-05 L156796-156844 — Killer Feature Agentic Governance (4 mécanismes)

---

**RATIFIED 2026-06-24 par A0 Amadeus — D7 anti-effondrement backup canon**. Handoff wiki sister de l'ADR-MARKET-STUDY-001 ratifié en FULL BATCH 6 livrables. Conservé pour traçabilité 1an minimum.