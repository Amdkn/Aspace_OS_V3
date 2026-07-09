---
id: ADR-ANTI-PAPERCLIP-001
title: Anti-Paperclip Policy pour Landing Pages OMK Nexus ⚖️ — Sister-scoped de ADR-SOBER-002
type: ADR (Architectural Decision Record)
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-0"
  context: "Ratification Tier 0 foundational DDD Landing Pages — 4 ADR bases (ANTI-TEMPLATE + ANTI-PAPERCLIP + SKILLS-CANON + WORKFLOW) ratifiés en bloc suite Phase 5 multi-workflow validée."
date: 2026-07-06
deciders: [A0 Amadeus (Jumeau Numérique)]
drafted_by: Claude Code (B1 E-Myth Gatekeeper, sister-scoped A1 Rick Sobriété + A1 Beth Ikigai)
domain: L2 Business OS / AaaS Doctrine / Landing pages / Anti-Paperclip / Anti-invention
tags: [#ADR #anti-paperclip #landing #nexus #omk #sister-canon #sober-002 #meta-001 #no-invention #vocabulaire-canon #D7-cost-of-escalation]
doctrine_anchors: [ADR-SOBER-002 (RATIFIED), ADR-META-001 (RATIFIED), ADR-META-006 (D6 Catalog), ADR-AAAS-PRICING-001 (RATIFIED + AMENDED), ADR-ICP-NEXUS-001 (RATIFIED), ADR-NEXUS-LANDING-PERSONAS-001, PRD-NEXUS-EVOLUTION-IA-001, PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3, plan-L2-business-os.md §13.5, MEMORY.md §ADR-LLM-COST-COMPARE-001 (DATA ACTUALIZED 80%)]
related: [ADR-SOBER-002 §D3 (7 Hard-Stop Triggers), ADR-SOBER-002 §D7 (Anti-patterns Musk), ADR-META-001 D1-D8, AGENTS.md §L0/A1 Rick Sobriété, AGENTS.md §L1/A1 Beth Ikigai, wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md, MEMORY.md §"P2.4d Coach spearhead CLOSED 2026-07-04"]
supersedes: none
supersedes_scope: aucune — ce ADR ajoute une **couche application-scoped** à ADR-SOBER-002 (L0 Kernel) ; ne réécrit ni ne contredit le canon ratified
sources_canons:
  - "ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md (RATIFIED 2026-06-21) — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md`"
  - "PRD-NEXUS-EVOLUTION-IA-001 §7 — Confusions Gemini filtrées par A+ — `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md`"
  - "PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3 PRD-UNIT-ECON-PROOF-001 — `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md`"
  - "plan-L2-business-os.md §13.5 — Pricing en travail (⚠️ D4 — non ratifié) — `C:/Users/amado/.claude/plans/plan-L2-business-os.md`"
  - "ADR-AAAS-PRICING-001_aaas-pricing-canon.md (RATIFIED + AMENDED 2026-06-24) — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md`"
  - "ADR-ICP-NEXUS-001_icp-nexus-structuration.md (RATIFIED 2026-06-24) — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md`"
  - "ADR-META-001_anti-paresse-verify-before-assert.md (RATIFIED) — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md`"
  - "MEMORY.md §'ADR-AAAS-PRICING-001 RATIFIED+AMENDED' + §'ADRs canoniques RATIFIED 2026-06-21' — `C:/Users/amado/.claude/projects/c--Users-amado/memory/MEMORY.md`"
  - "MEMORY.md §'ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80%' — Token Plan canon 38.11M tokens/jour A0 usage documenté"
provenance: |
  Née 2026-07-06 de l'observation post-mortem du pipeline landing Nexus (PRD-NEXUS-EVOLUTION-IA-001) :
  §7.6 du PRD a explicitement flaggé le risque « ⚠️ Les chiffres (47% conversion, 700+ signaux, ×1000) —
  non sourcés, à ne JAMAIS republier sans vérification (D1) ; sur une landing = claims à bench ou à
  retirer ». ADR-SOBER-002 (RATIFIED 2026-06-21) donne le kernel anti-paperclip. PRD-PORTFOLIO-B1-FRANCHISE
  §6 Tier 3 PRD-UNIT-ECON-PROOF-001 mandate explicitement « la table de preuve coût-fixe-vs-Jevons
  avec VRAIS chiffres mesurés sur notre propre usage (38M tokens/jour déjà documentés) ». Ce ADR
  opérationnalise la doctrine SOBER-002 au niveau surface = landing pages Nexus ⚖️.
sign_off_a0: pending
sign_off_pending: true
ratification_log: pending A0 GO post-relire ADR-SOBER-002 + plan L2 §13.5 + PRD-NEXUS §7
---

# ADR-ANTI-PAPERCLIP-001 — Anti-Paperclip Policy pour Landing Pages OMK Nexus ⚖️

## 1. Status

**DRAFT 2026-07-06** — Claude Code (B1 E-Myth Gatekeeper) draft → A0 Amadeus (Jumeau Numérique) ratification pending.

⚠️ **D4 no-self-contradiction** : ce ADR est **sister-scoped** (couche application = landing pages) de :

- **`ADR-SOBER-002`** (RATIFIED 2026-06-21, L0 Kernel Sobriété) — la doctrine canonique anti-paperclip maximizer, A1 Rick Sobriété primary author. Ce ADR hérite des **7 Hard-Stop Triggers** (SOBER-002 §D3) et des **10 Anti-patterns Musk** (SOBER-002 §D7) SANS duplication — il les **opérationnalise** sur la surface landing pages.
- **`ADR-META-001`** (RATIFIED) — Anti-Paresse D1-D8. Ce ADR applique particulièrement **D1 Verify before assert**, **D6 Root cause**, **D7 Cost-of-escalation**.
- **`ADR-NEXUS-LANDING-PERSONAS-001`** (RATIFIED) — 3 landings distinctes ICP. Ce ADR-ci régit le **contenu textuel** des landings Nexus (Marcus Vance / Harrison Vance / Clara Sterling / Amara Sow / Christian Vance / David Kross).

Pas de duplication, spécialisation par couche :
- **SOBER-002** = « ce que Rick veto structurellement au niveau kernel »
- **ANTI-PAPERCLIP-001 (ce doc)** = « ce qui est INTERDIT d'écrire sur une landing page Nexus »
- **PRD-UNIT-ECON-PROOF-001** (Tier 3 PRD-PORTFOLIO) = « la table de preuve avec VRAIS chiffres qui peuvent être cités »

## 2. Context

### C1 — Le gap landing-spotted par PRD-NEXUS §7.6

**D1 receipts 2026-07-06** : la rédaction des 6 landing pages Nexus candidates (PRD-NEXUS §4 Personas) a flaggé explicitement le risque d'invention chiffrée :

> **PRD-NEXUS §7.6 verbatim** : « ⚠️ Les chiffres (47% conversion, 700+ signaux, ×1000) — non sourcés, à ne JAMAIS republier sans vérification (D1) ; sur une landing = claims à bench ou à retirer. »

Ces chiffres (47% conversion, 700+ signaux, ×1000) provenaient du brainstorm Gemini 2026-07-06 — filtrés par A+ en cours d'échange pour les raisons explicites §7 du PRD-NEXUS :

1. ❌ « BETH_VETO_DISSOLVED_BY_WF0 » — confusion sur l'architecture gatekeeper (Beth = seul veto, WARMODE-002).
2. ❌ Pitch local-first/0,01$/MiniMax-chez-le-client comme offre 2026 — corrigé par A+ lui-même, **différé 2027**.
3. ❌ « Jstack » — le référent réel est **Gstack** (garrytan/gstack), pas « Jstack ».
4. ❌ Arborescence inventée — vraie racine = `ASpace_OS_V2/`.
5. ❌ `state.json` décoratifs — télémétrie narrative, aucun fichier réel.
6. ⚠️ **Les chiffres non sourcés** — danger landing.

### C2 — Sister-scope avec ADR-SOBER-002 sans duplication

**Doctrine ancrée (SOBER-002 §D1 verbatim)** : « **Paperclip Maximizer** = système (IA / organisation / individu) qui optimise une métrique unique au point de détruire tout le reste, par : (1) Mono-objectif [...] (2) Boucle d'optimisation sans limite [...] (3) Destruction systémique invisible [...] (4) Justification narrative [...] **Anti-pattern canon** : Musk + DOGE + USAID + X algorithm + Starlink monopoly = paperclip maximizer civilisationnel opérationnel depuis 2025. »

**SOBER-002 §D7 table** liste 10 Anti-patterns Musk → Anti-pattern AaaS. Notre surface landing Nexus est vulnérable à un sous-ensemble spécifique :

| Anti-pattern Musk (SOBER-002 §D7) | Manifestation landing page |
|---|---|
| Mono-objectif valorisation | « Augmentez votre ROI de ×10 ! » |
| Boucle d'optimisation sans limite | « Notre IA vous remplace toute votre équipe » |
| Justification narrative | « L'AGI est là, votre business doit suivre » |
| Manipulation algorithmique | Ciblage émotionnel sans transparence (« Vous perdez de l'argent chaque jour sans nous ») |
| Souveraineté privée infrastructure critique | « Notre SaaS remplace vos process critiques » (anti-pattern Zero-PII) |

### C3 — L'obligation de sister-canon avec Token Plan A0

**D1 receipts MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80%** (verbatim) :

> « MiniMax Token Plan · Monthly Max $50/mois pour ~5.1B tokens M3 (D1-verified via screenshots A0 `platform.minimax.io/console/usage` + `subscribe/token-plan`) — usage actuel A0 : 38.11M tokens/jour, 772.20M/7j, 3.85B/30j. »

**Pattern obligatoire pour landing Nexus** : citer ces **38.11M tokens/jour / 772.20M/7j / 3.85B/30j** comme **preuve de coût fixe mesuré** (vs Jevons compteur variable). **JAMAIS** inventer un autre chiffre d'usage (cf. PRD-UNIT-ECON-PROOF-001 §PRD-PORTFOLIO Tier 3).

## 3. Décision

### D1 — Doctrine Anti-Paperclip pour Landing Pages = sister-scoped SOBER-002

**Adoption** : Les 7 Hard-Stop Triggers de SOBER-002 §D3 + les 10 Anti-patterns Musk de SOBER-002 §D7 sont **opérationnalisés** au niveau surface landing pages Nexus ⚖️ par les 5 mécanismes suivants :

1. **Vocabulaire canonique strict** (D2 ci-dessous) : 9 termes mandatés pour parler de l'offre, **0** terme banni autorisé.
2. **Chiffres autorisés vs chiffrés inventés** (D3) : tableau ASCII format avec 2 colonnes. **D1 verify before assert** (ADR-META-001) sur chaque chiffre.
3. **Promesses 2026 vs 2027+** (D4) : scope strict, ce qui est différé 2027 (local-first, IA chez le client, finetuning) est **INTERDIT** sur landing 2026.
4. **Testimonials & chiffres d'usage** (D5) : policy **SISTER-CANON ONLY** — cite `MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80%` ou rien.
5. **Frontière ChatGPT/Gemini confusions** (D6) : reproduit le filtre du PRD §7 sur les 6 confusions.

### D2 — Vocabulaire canonique obligatoire (9 termes mandatés)

| # | Terme canonique | Signification | Source canon |
|---|---|---|---|
| 1 | **Loop Engineering** | Méta-conception du Business OS A'Space, prototype de franchise par conception | PRD-NEXUS §1 verbatim |
| 2 | **Enterprise OS wargamé** | Positionnement vs SaaS wrappers vibe-codés éphémères | PRD-NEXUS §5.1 |
| 3 | **Boucle Medvi** | Quiz → preuve ROI → forfait signé → affiliation 20% Stripe Connect | PRD-NEXUS §5.4 |
| 4 | **Jevons Arbitrage** | Coût fixe d'orchestration vs compteur API variable | PRD-NEXUS §5.3 |
| 5 | **Audit Sdiri** | Cartographie Inputs → Process → Outputs + scorecard 7 KPIs + angles morts nommés | PRD-PORTFOLIO Tier 1 §1 |
| 6 | **Wargame Fable** | Chaque workflow client simulé move-by-move : Action → Réaction → Contre-action | PRD-NEXUS §2 module #2 |
| 7 | **CEO-Bench** | Audit de cohérence des décisions de direction vs leur carnet de route ; angles morts nommés avec preuve | PRD-NEXUS §2 module #3 |
| 8 | **MiroFish** | Simulations de Swarm prédictives (variations comportements équipes/marché simulées en parallèle) | PRD-NEXUS §2 module #4 + plan L2 §13.4 spearhead |
| 9 | **Zero-PII Agentic Governance** | Killer Feature Nexus = gouvernance agents IA conforme AI-Act + secret professionnel + RGPD + Zero-Knowledge Bare-Metal | ADR-ICP-NEXUS-001 Pilier 5 verbatim |

### D3 — Vocabulaire banni (5 termes interdits)

| # | Terme banni | Raison | Source canon |
|---|---|---|---|
| 1 | **« AGI »** / **« super intelligence »** | Anti-pattern Musk (SOBER-002 §D1 mono-objectif) — narratif civilisationnel non sourcé | SOBER-002 §D7 table |
| 2 | **« revolutionize »** / **« transform your business »** | Justification narrative (SOBER-002 §D1 #4) — vide sémantique | SOBER-002 §D7 |
| 3 | **« AGI-powered »** / **« next-gen »** | Empty signifier — pas de claim mesurable | D1 verify before assert (META-001) |
| 4 | **« industry-leading »** / **« best-in-class »** / **« 100% Secure »** | Génériques sans D1 receipt | META-001 D1 + D6 |
| 5 | **« Jstack »** | Confusion Gemini filtrée PRD §7.3 — le vrai référent est **Gstack** (garrytan/gstack) | PRD-NEXUS §7 verbatim #3 |

### D4 — Tableau ASCII : chiffres AUTORISÉS vs chiffres BANNIS

```
┌─────────────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────┐
│ ✅ AUTORISÉ (D1 verified, sister-canon)                      │ ❌ BANNIS (invention non sourcée)                            │
├─────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ $50/mois pour ~5.1B tokens M3 (Token Plan canon)            │ « 1000+ clients » sans D1 receipt                            │
│ 38.11M tokens/jour (usage A0 mesuré)                        │ « 700 signaux » sans D1 receipt                              │
│ 772.20M tokens/7j (usage A0 mesuré)                         │ « 47% conversion » sans D1 receipt                          │
│ 3.85B tokens/30j (usage A0 mesuré)                          │ « ×1000 croissance » sans D1 receipt                        │
│ 1 000 $/mois × 100 clients Premium = 1,2 M ARR              │ « ROI ×10 garanti » sans D1 receipt                         │
│ (plan L2 §13.5, ⚠️ D4 non ratifié — à confronter ADR-AAAS-   │                                                             │
│ PRICING-001)                                                │                                                             │
│ $750/an Nexus Tier 1 Expert Solo (ADR-ICP-NEXUS-001 §       │                                                             │
│ Pricing canon verbatim L25674)                              │                                                             │
│ $1000-1500/an Nexus Tier 2 Cabinet Standard                 │                                                             │
│ $1500-2000/an + Whitelabel 25% Nexus Tier 3                 │                                                             │
│ Family Office 84 Trilliards € verbatim (ADR-ICP-NEXUS-001    │                                                             │
│ Pilier 3 L19500)                                             │                                                             │
│ Boucle Medvi : 400M$/2 employés, 16,2% marge                 │                                                             │
│ (PRD-PORTFOLIO Tier 1 §3 verbatim)                           │                                                             │
│ AI-Act = 2026-08-02 (deadline canon, PRD-PORTFOLIO Tier 1   │                                                             │
│ §2 verbatim)                                                 │                                                             │
└─────────────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

**Règle D7 cost-of-escalation** : tout chiffre non listé dans la colonne AUTORISÉ → **D1 verify avant publication**, sinon **retrait pur**.

### D5 — Promesses 2026 vs 2027+ (scope strict)

**Ce qui est EN SCOPE 2026 (à promettre sur landing)** :

| Promesse 2026 | Source canon |
|---|---|
| **Enterprise OS wargamé** (5 modules) | PRD-NEXUS §2 verbatim |
| **5 modules** : Audit Sdiri / Wargame Fable / CEO-Bench / MiroFish / Gstack Lighting | PRD-NEXUS §2 table verbatim |
| **$1000/mois gated ×100** (hypothèse A0) | plan L2 §13.5 verbatim (« 1 000 $/mois × 100 clients Premium = 1,2 M ARR »), ⚠️ D4 non ratifié |
| **Conformité EU AI Act Articles 9/14/15** | ADR-ICP-NEXUS-001 Pilier 5 (AI-Act article 12 traçabilité + AI-Act 2026-08-02 deadline) |
| **Zero-PII Agentic Governance** (5 mécanismes durs) | ADR-ICP-NEXUS-001 Pilier 5 verbatim |
| **Coût fixe vs Jevons** (Boucle Medvi assainie) | PRD-NEXUS §5.3 |

**Ce qui est DIFFÉRÉ 2027+ (INTERDIT sur landing 2026)** :

| Pitch DIFFÉRÉ 2027+ | Raison | Source canon |
|---|---|---|
| **« IA locale sans GPU »** | Aligné avec Dark L0 différé (wargame 10-localai-minimax) | PRD-NEXUS §1 verbatim « L'IA locale sans GPU = différée 2027 (DSpark, Recursivemas, finetuning du Canon A'Space pour rendre l'organigramme et les workflows natifs aux LLM) » |
| **« 0,01$/token »** / **« inférence locale économique »** | MiniMax chez le client = 2027, pas 2026 | PRD-NEXUS §1 verbatim + PRD-NEXUS §7.2 verbatim « ❌ Le pitch local-first/0,01$/MiniMax-chez-le-client comme offre 2026 — corrigé par A+ lui-même en cours d'échange : différé 2027 » |
| **« Finetuning DSpark/Recursivemas Canon »** | Différé Q4 2026 / Q1 2027 | PRD-NEXUS §1 verbatim |
| **« Local-first complet »** | Pas de SaaS public promis, mais promesse production 2027 | PRD-NEXUS §7.2 |

**Verbatim PRD-NEXUS §1 (gravé par A+)** : « **L'IA locale sans GPU = différée 2027** (DSpark, Recursivemas, finetuning du Canon A'Space pour rendre l'organigramme et les workflows natifs aux LLM). Aligné avec le Dark L0 déjà différé (wargame 10-localai-minimax). **L'offre 2026 n'est PAS l'infrastructure locale.** C'est **l'Évolution IA des Entreprises** : le client achète le contrôle chirurgical de ses processus par le **Loop Engineering** — la méta-conception même du Business OS A'Space, vendue en prototype de **franchise par conception**. »

### D6 — Frontière ChatGPT/Gemini confusions (filtre PRD-NEXUS §7 reproduit)

**Règle** : reproduction littérale des 6 confusions filtrées par A+ dans PRD-NEXUS §7. Toute mention landing doit passer ce filtre :

```
❌ CONFUSION 1 : « BETH_VETO_DISSOLVED_BY_WF0 »
   → Vrai : Beth = seul veto (WARMODE-002) ; la Fenêtre Fable est un bypass TEMPORAIRE
     auto-expirant (WARMODE-003), pas une dissolution.
   → Landing : NE JAMAIS suggérer que les gates disparaissent.

❌ CONFUSION 2 : Pitch local-first/0,01$/MiniMax-chez-le-client comme offre 2026
   → Vrai : différé 2027 par A+.
   → Landing : INTERDIT promettre local-first avant 2027.

❌ CONFUSION 3 : « Jstack Front-End Terminal »
   → Vrai : le référent réel est Gstack (garrytan/gstack) ; « Jstack » n'existe pas.
   → Landing : citer « Gstack » verbatim.

❌ CONFUSION 4 : Arborescence « 10_MÉTA_OS_Y_COMBINATOR / 00_Jerry_Business_Pulse… »
   → Vrai : inventée ; la vraie racine = ASpace_OS_V2/ (00_Amadeus / 10_Tech_OS /
     20_Life_OS / 30_Business_OS / _SPECS).
   → Landing : NE PAS mentionner arborescence interne.

❌ CONFUSION 5 : « state.json décoratifs » (MUSE_EXTRAPOLATION_READY, etc.)
   → Vrai : télémétrie narrative, aucun fichier réel. Les vrais bus d'état =
     citadel/data/*.json + worklog.
   → Landing : NE PAS mentionner artefacts internes fictifs.

❌ CONFUSION 6 : Chiffres (47% conversion, 700+ signaux, ×1000)
   → Vrai : non sourcés, à JAMAIS republier sans vérification (D1) ; sur une landing
     = claims à bench ou à retirer.
   → Landing : UNIQUEMENT chiffres sister-canon D4 ci-dessus.
```

## 4. Doctrine (anti-patterns landing interdits)

### Anti-patterns landing interdits (synthèse SOBER-002 §D7 application-scoped)

| Anti-pattern Musk (SOBER-002) | Traduction INTERDITE landing Nexus |
|---|---|
| Mono-objectif valorisation | « Augmentez votre ROI de ×10 ! » / « Multipliez vos revenus » |
| Boucle optimisation sans limite | « Notre IA vous remplace toute votre équipe » / « Scale infini sans effort » |
| Destruction systémique invisible | Claims chiffrés non sourcés (D3 colonne BANNIS) |
| Justification narrative | « L'AGI est là, votre business doit suivre » / « La révolution IA est en marche » |
| Siphonage données (DOGE) | « Notre SaaS remplace vos process critiques » (anti-pattern Zero-PII) |
| Manipulation algorithmique | Ciblage émotionnel sans transparence (« Vous perdez de l'argent chaque jour sans nous ») |
| Chantage géopolitique (Starlink) | « Sans Nexus, vos concurrents vont vous écraser » (FOMO non sourcé) |
| Valorisation découplée (SpaceX IPO) | Promesses ROI ×10 sans table de preuve D1 |
| Capture régulation | Claims conformité sans citer AI-Act Articles 9/14/15 verbatim |
| Souveraineté privée infra critique | « Nous détenons vos données critiques en cloud » |

## 5. Architecture (gates d'application)

### G1 — Gate de relecture B1 (B2 Superman Growth + B1 Summers Nexus OMK BOS)

Toute landing candidate passe **2 gates** avant publication :

1. **Gate B1 Summers** (B1 Captain variant Nexus OMK BOS) : relecture vocabulary canonique (D2) vs vocabulaire banni (D3).
2. **Gate B2 Superman Growth** : relecture chiffres (D4) — chaque chiffre = sister-canon D1 verified ou retrait.

### G2 — Hook PostToolUse Edit/Write landing (gated future)

Skill `/anti-paperclip-audit-landing` à créer (sister skill `/anti-paperclip-audit` sister-scopé de SOBER-002 §D4 #4) — trigger = Edit/Write sur `**/landing*/**/*.html` ou `**/omk-nexus-landing*/*` — applique les 9 termes mandatés (D2), 5 termes bannis (D3), 11 chiffres sister-canon (D4).

### G3 — Skill `picard-audit-and-prod-workflow` sister-scopé

Sister pattern : `picard-audit-and-prod-workflow` (canon skill existant) → `picard-anti-paperclip-landing` à créer, qui audite chaque landing candidate vs ce ADR avant PR.

## 6. Verification (D1 receipts obligatoires)

### V1 — D1 receipts Landing Nexus candidates

Pour chaque landing candidate des 6 personas (Marcus / Harrison / Clara / Amara / Christian / David) :

| Landing | D1 receipts requis |
|---|---|
| Marcus Vance (Strate A — Coaching C-Suite) | Audit Sdiri livré + Wargame Fable Module #2 + Zero-PII Agentic Governance + AI-Act Articles 9/14/15 verbatim |
| Harrison Vance / Clara Sterling (Strate B — Agence BDR) | Jevons Arbitrage (45k tokens/prospect, 1.5k→9k$/mois, marge 75%→42% = VERBATIM PRD-NEXUS §4 table) + Boucle Medvi verbatim + 38.11M tokens/jour A0 mesuré |
| Amara Sow (Strate B — Growth native-IA) | Harnais Multi-Tenant + RLS canon |
| Christian Vance (Strate B — Sales enablement) | CEO-Bench + Wargame Fable pipeline scoring |
| David Kross (Strate C — Fractional COO) | SOPs → Skills exécutables + W× par client |

### V2 — D1 receipts skill canon-batch-spawn (Hermes-style Phase 2 sister)

Skill `/anti-paperclip-landing-audit` à créer en fin de session si triggers Phase 2 (Hermes-style self-improvement) observés. ROI estimé : ~5 min/landing économisée.

## 7. Risks + Rollback

### Risk 1 — Faux positif filtre trop strict

**Risque** : rejet d'une landing légitime parce qu'elle contient un mot borderline.
**Mitigation** : le filtre vise **le pattern global**, pas le mot isolé. Une phrase contenant « révolution » peut passer si elle est ancrée sur une citation A0 verbatim (ex. « La révolution du contrôle chirurgical des processus » = OK si liée au Loop Engineering §1 PRD-NEXUS).
**Rollback** : gate B1 Summers review manuel pour cas borderline.

### Risk 2 — Sister-canon drift (chiffres deviennent obsolètes)

**Risque** : MEMORY.md §ADR-LLM-COST-COMPARE-001 sera actualisé (les 20% restants = Anthropic API direct pricing). Le tableau D4 devra être actualisé à chaque update MEMORY.md.
**Mitigation** : D4 cite `MEMORY.md §X` au lieu de hardcoder les chiffres ; actualisation = append MEMORY.md + patch D4 dans la même PR.
**Rollback** : si MEMORY.md change et D4 pas actualisé → A0 board observer déclenche A3 Data (PARA Archives) recertification 90 jours.

### Risk 3 — Adoption lente (copywriters / marketers)

**Risque** : copywriters habitués aux patterns « revolutionize your business » résistent au filtre.
**Mitigation** : ce ADR est **gatekeeper**, pas suggestion — Sister G1 ci-dessus est **non-négociable**.
**Rollback** : escalade A0 (D7 cost-of-escalation respectée : la perte d'une landing = ~$0 ; l'invention chiffrée = ~$150K réputation = ROI gate ~10⁹×).

## 8. Statut C (Wargame + Skill canon-batch-spawn)

### Statut wargame (gate publication)

**Wargame 09-gstack M4 cas 4** : « is this worth building tel quel ? » — **le système se grille lui-même**. Application à ce ADR :

- ✅ **Objection 1 résolue** : « Et si le tableau D4 devient obsolète à chaque update MEMORY.md ? » → cf. Risk 2 mitigation.
- ✅ **Objection 2 résolue** : « Le skill `/anti-paperclip-landing-audit` n'existe pas encore, comment auditer sans lui ? » → gate B1/B2 manuel suffit pour Q3 2026, skill = Q4 2026.
- ⚠️ **Objection 3 ouverte** : « Que faire si un prospect potentiel demande explicitement du local-first 2026 ? » → **réponse canon** = « L'offre 2026 est l'Enterprise OS wargamé, le local-first est notre roadmap 2027 — rejoignez les 100 clients Premium pour co-concevoir la roadmap ». **NON** promettre local-first 2026.

### Skill canon-batch-spawn (Hermes-style Phase 2)

**Triggers Phase 2 observés** :
- Répétition : audit landing vs ce ADR = 3+ tool calls par landing × 6 personas = 18+ invocations Q3 2026.
- Checklist longue : 9 sections numérotées + 5 gates à vérifier par landing.

**Skill à créer** : `/anti-paperclip-landing-audit` (sister skill `/canon-batch-spawn`). Brief :
- **Triggers** : Edit/Write landing HTML + grep « AGI » / « revolutionize » / « industry-leading » / « Jstack ».
- **Workflow** : load ce ADR + ADR-SOBER-002 §D7 + PRD-NEXUS §7 → check landing → emit APPROVE / BLOCK avec diff exact.
- **ROI** : ~5 min/landing économisée × 18 landings Q3-Q4 2026 = ~90 min total.
- **Hermes-style auto-create** : trigger pattern observé fin de session.

## 9. Decision summary

**Ce qui est décidé** :

1. ✅ Adoption de la **policy Anti-Paperclip pour Landing Pages Nexus ⚖️** = sister-scoped de ADR-SOBER-002 (L0 Kernel).
2. ✅ Adoption des **9 termes canoniques mandatés** (D2) et **5 termes bannis** (D3).
3. ✅ Adoption du **tableau ASCII chiffres AUTORISÉS vs BANNIS** (D4) avec sister-canon MEMORY.md §ADR-LLM-COST-COMPARE-001.
4. ✅ Adoption du **scope strict 2026 vs 2027+** (D5) — verbatim PRD-NEXUS §1.
5. ✅ Adoption du **filtre 6 confusions Gemini** (D6) — reproduction PRD-NEXUS §7.
6. ✅ Gates d'application (G1 = B1 Summers + B2 Superman Growth) obligatoires avant publication landing.
7. ✅ Skill `/anti-paperclip-landing-audit` à créer Phase 2 Hermes-style fin de session.

**Ce qui est DIFFÉRÉ** :

- Skill canonique `/anti-paperclip-landing-audit` = Q4 2026 (Phase 2 observation 1ère).
- Hook PostToolUse Edit/Write landing = gated A0 GO post-ship 5 premières landings.
- Sister ADRs : ADR-ANTI-PAPERCLIP-002 (Solaris 🎨 Visual First) et ADR-ANTI-PAPERCLIP-003 (Orbiter 🏗️ Mobile First) = gated A0 GO si A0 demande la même rigueur pour les 2 autres variants.

**Ce qui est INTERDIT** :

- ❌ Toute landing Nexus ⚖️ contenant « AGI », « super intelligence », « revolutionize », « transform your business », « AGI-powered », « next-gen », « industry-leading », « best-in-class », « 100% Secure », « Jstack ».
- ❌ Tout chiffre d'usage non listé D4 colonne AUTORISÉ (47% conversion, 700+ signaux, ×1000, ×10 ROI = INTERDIT).
- ❌ Tout pitch local-first / 0,01$ token / MiniMax chez le client / finetuning DSpark Recursivemas Canon sur landing 2026 (= 2027).
- ❌ Tout « 1000+ clients » / « 700 signaux » / « 47% conversion » sans D1 receipt sister-canon.

**Statut final** : DRAFT en attente ratification A0 Amadeus post-relire.

---

## Annexe A — Sister-canon pointers (D1 receipts exhaustifs)

### A.1 — ADR-SOBER-002 (RATIFIED 2026-06-21)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md`
- §D3 : 7 Hard-Stop Triggers (siphonage données / manipulation algo / destruction institutions / chantage géopolitique / valorisation découplée / capture régulation / souveraineté privée).
- §D7 : 10 Anti-patterns Musk → Anti-pattern AaaS (table de correspondance).

### A.2 — PRD-NEXUS-EVOLUTION-IA-001 §7

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md`
- §7 verbatim : 6 confusions Gemini filtrées par A+.
- §1 verbatim : pitch local-first = différé 2027.
- §2 verbatim : 5 modules (Audit Sdiri / Wargame Fable / CEO-Bench / MiroFish / Gstack Lighting).
- §4 verbatim : 6 personas (Marcus / Harrison / Clara / Amara / Christian / David).
- §5 verbatim : 5 frameworks marketing (STP / AAARR Signal-First / Jevons Arbitrage / Boucle Medvi / E-Myth Functional Architecture).

### A.3 — PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md`
- §6 Tier 3 PRD-UNIT-ECON-PROOF-001 verbatim : « la table de preuve coût-fixe-vs-Jevons avec VRAIS chiffres mesurés sur notre propre usage (38M tokens/jour déjà documentés). Résout le ⚠️ du PRD-NEXUS §7.6 : plus jamais un chiffre non sourcé sur une landing. »

### A.4 — plan-L2-business-os.md §13.5

- Path : `C:/Users/amado/.claude/plans/plan-L2-business-os.md`
- §13.5 verbatim : « Hypothèse A0 : **1 000 $/mois × 100 clients Premium = 1,2 M ARR** (« Million de Libération », séparation familiale dans l'abondance structurée à 1 000 clients) avec **ancre 5 000 $** (référence marché : agents SDR premium 18-60 K$/an → l'offre est sous le plancher marché). **À confronter à `ADR-AAAS-PRICING-001` (RATIFIÉ) avant toute ratification** — si conflit : ADR neuf qui supersede, jamais d'édit de l'immuable. »

### A.5 — ADR-AAAS-PRICING-001 (RATIFIED + AMENDED 2026-06-24)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md`
- 5 Tiers canon USD post-accuponcture.

### A.6 — ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md`
- 5 Piliers canon (Persona Expert méthodique / Mantra « L'illusion de la complexité » / Citadelle du Savoir 84 Trilliards / 3-ICP / Zero-PII Agentic Governance).
- Pricing canon Nexus USD post-accuponcture : $750-$2000/an + Whitelabel 25% (Pilier Pricing).

### A.7 — ADR-META-001 (RATIFIED)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md`
- D1-D8 doctrine (Verify / Nuance / No-self-contradiction / Append-only / Root-cause / Proof / Cost-of-escalation / Cross-agent).

### A.8 — MEMORY.md

- Path : `C:/Users/amado/.claude/projects/c--Users-amado/memory/MEMORY.md`
- §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% (sister-canon Token Plan).
- §ADR-AAAS-PRICING-001 RATIFIED+AMENDED (pointeur).
- §ADRs canoniques RATIFIED 2026-06-21 (pointeur).

---

## Annexe B — Open follow-ups (gated A0 GO)

1. **Skill `/anti-paperclip-landing-audit`** : sister skill `/canon-batch-spawn` + `/anti-paperclip-audit` (SOBER-002 §D4 #4). Phase 2 Hermes-style creation gated Q4 2026.
2. **Sister ADRs ADR-ANTI-PAPERCLIP-002 (Solaris 🎨) + ADR-ANTI-PAPERCLIP-003 (Orbiter 🏗️)** : gated A0 GO si A0 demande la même rigueur pour les 2 autres variants. Pas de duplication = scope sister.
3. **Hook PostToolUse Edit/Write landing** : gated A0 GO post-ship 5 premières landings (validation empirique du filtre avant hard-block).
4. **Recertification 90 jours** : A3 Data (PARA Archives) review D4 vs MEMORY.md updates. Si MEMORY.md change sans D4 actualisé → escalate A0.

---

## Signatures

- **Draft author** : Claude Code (B1 E-Myth Gatekeeper, sister-scoped A1 Rick Sobriété + A1 Beth Ikigai) — 2026-07-06.
- **Recorder** : pending A3 Data (PARA Archives) post-ratification.
- **Ratification pending** : A0 Amadeus (Jumeau Numérique) — sign-off attendu post-relire ADR-SOBER-002 + plan L2 §13.5 + PRD-NEXUS §7 + MEMORY.md §ADR-LLM-COST-COMPARE-001.
- **Hash d'intention** : `adr_anti_paperclip_001_draft_2026-07-06_landing_nexus_sister_sober_002_9_termes_5_bannis_11_chiffres_sister_canon`