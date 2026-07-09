---
id: ADR-AAAS-ACQUISITION-DOCTRINE-001
title: AaaS Acquisition Doctrine — Acquisition-First vs Structuration-First (MedVie 400M$ sister canon)
status: RATIFIED
date: 2026-06-24
ratified: 2026-06-24 — A0 Amadeus (Option 1 des 3 ADR proposés post-3 guides MedVie)
last_updated: 2026-06-24 (Claude Code on A0 directive après /youtube-to-guide v3 batch)
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2) on A0 directive Option 1 (synthèse des 3 guides Geordi)
domain: L2 Business OS / AaaS Doctrine / Acquisition Strategy
tags: [#ADR #aaas #acquisition #structuration #medvie #solopreneur #onboarding #solarpme #nexus #orbiter #doctrine #D6-anti-paperclip #D1-verify]
related: [ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-ICP-SOLARIS-001, ADR-ICP-NEXUS-001, ADR-ICP-ORBITER-001, ADR-SOBER-002, ADR-MARKET-STUDY-001, ADR-OMK-004, ADR-META-006]
sources_canons: [
  "Guide 03_IT/2026-06-17_etude-de-cas-medvi-400m-2-employes-agents-ia.md (6 490 chars, sister canon existant MedVie)",
  "Guide 02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md (22 708 chars, Antigravity Premium)",
  "Guide 07_Growth/onboarding-flows-1460-patterns-acquisition-funnel-Qsq-Sj_rojU.md (21 873 chars, Antigravity Premium)",
  "Notion OMK HQ page (S0 OB Factory, 8 sections canon, Vague 1 GROWTH+SALES roadmap)",
  "Transcription MedVie initiale A0 message (4 piliers canon acquisition-first : Operations IA + Acquisition automatisée + Affiliation agressive + Plateforme 0-stock)",
  "ADR-AAAS-PRICING-001 RATIFIED 2026-06-24 (5 tiers USD post-accuponcture)",
  "ADR-L2-AAAS-001 RATIFIED 2026-06-21 (3 Variants Solarpunk sister canon)"
]
provenance: Née 2026-06-24 d'une décision A0 post-batch 2 guides MedVie-related (vidéo #1 BI-MNjm1tTQ $1M+ Solo AI Agent + vidéo #2 Qsq-Sj_rojU 1460 Onboarding Flows) + canon sister pré-existant 03_IT/ MedVi (créé 2026-06-17). A0 a explicitement demandé 'apartir de ces 3 guide, tu dois cree un des ADR de Business OS' et a choisi Option 1 (ADR Acquisition Doctrine nouveau) sur 3 options proposées. 4 sources convergentes identifiées + 3 ICP sisters anchoring.
---

# ADR-AAAS-ACQUISITION-DOCTRINE-001 — AaaS Acquisition Doctrine (Acquisition-First vs Structuration-First)

## Status

**RATIFIED** — 2026-06-24 par A0 Amadeus (Option 1 des 3 ADR proposés post-batch 3 guides MedVie). Sister canon [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) (3 Variants Solarpunk RATIFIED 2026-06-21) + [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) (5 Tiers USD RATIFIED 2026-06-24).

## Context

**D6 D3 nuance racine** — Avant ce ADR, **AUCUN canon acquisition-vs-structuration formalisé** :

| Source canon | Status pré-ADR |
|---|---|
| ADR acquisition | **ABSENT** (`grep -ri acquisition _SPECS/ADR/L2_Business_OS/` = 0 hit) |
| Handoff acquisition canon | **ABSENT** (`ls wiki/hand_offs/*acquisition*` = 0) |
| Notion OMK HQ page | "S0 OB Factory" + roadmap GROWTH+SALES présents mais **doctrine** acquisition absente |
| Sister canon AaaS Doctrine | **3 Variants Solaris/Nexus/Orbiter** RATIFIED mais **paradigme acquisition** sous-spécifié |
| Pricing canon ADR-AAAS-PRICING-001 | 5 tiers USD présents mais **stratégie acquisition** par tier = implicite |
| Geordi guides canon | 3 guides MedVie-related présents (6 490 + 22 708 + 21 873 chars = **51 071 chars canon**) mais **synthèse doctrinelle** absente |

**Discovery canon 2026-06-24** : 3 guides Geordi MedVie-related convergent vers **2 paradigmes d'acquisition mutuellement éclairants** :

1. **Guide 03_IT MedVie** (N-9rovSvCEA, Minozan, 2026-06-17, 6 490 chars) = **paradigme Acquisition-First** canon : 4 piliers (Ops AI / Acquisition Triple-Canal / Marges Asset-Light / Conformité Fossé)
2. **Guide 02_Ops Solopreneur** (BI-MNjm1tTQ, Greg Isenberg × Nick from Orgo, 2026-06-24, 22 708 chars) = **paradigme Acquisition-First appliqué solopreneur** : NYX Stack + Diverge-then-Converge + Vertical Templating + Content is King 2026
3. **Guide 07_Growth Onboarding** (Qsq-Sj_rojU, Mobbin, 2026-06-24, 21 873 chars) = **mécanismes onboarding communs** aux 2 paradigmes : Aha Moment Threshold + Personalization Pre-Commitment + Paywall Timing Architecture + Friction Reallocation Theorem

**Insight A0** : MedVie = acquisition-first = **400M$ Y1 / 2 employés / 16,2% marge brute** (vs concurrents 2 400 employés / 5,5% marge = 3× marges avec 99% moins de personnel). A0's OS = structuration-first = **8 hiérarchies B1/B2/B3 + Sobriété 1an+** (canon `ADR-SOBER-002`). 2 paradigmes mutuellement éclairants : ni MedVie pure (risque greenwashing non-AIable compliance), ni A0 pure (risque lenteur acquisition).

**D3 nuance over literal** : "Acquisition" dans ce ADR ≠ marketing classique (META ads + copywriting). "Acquisition" = **système d'ingénierie qui transforme visiteur en client récurrent rétention J+7**, articulé autour de **4 mécanismes canon** : (a) boucle acquisition par Quiz Lovable (MedVie verbatim), (b) NYX Stack (Codex + Hermes + Orgo + Composio + Agent Mail + Obsidian), (c) Onboarding premium 1 460 flows analysés (Mobbin), (d) Marges Asset-Light 3×. "Structuration" = **hiérarchie des domaines + Sobriété 1an+ + canon ADR** (A0 OS V2 verbatim).

## Décision : Acquisition-First vs Structuration-First

### Principe directeur (D7 anti-effondrement)

L'AaaS Doctrine ne tranche pas entre les 2 paradigmes. Elle les **déclare complémentaires** et **mappe chaque ICP Variant à son paradigme dominant**. Le risque greenwashing "tout acquisition-first" est mitigé par `ADR-SOBER-002` (Sobriété 1an+) + `ADR-META-006` D6 catalog (D6 anti-paperclip).

### Tableau canon Acquisition-First vs Structuration-First

| Axe | **Paradigme 1 : Acquisition-First** (MedVie) | **Paradigme 2 : Structuration-First** (A0 OS) |
|---|---|---|
| **Objectif Y1** | $400M CA / 2 employés / 16,2% marge | Canon ADR en place / Sobriété 1an+ / 0 hard-sell |
| **Pilier #1** | Operations AI-Natives (substitution agents IA) | 8 hiérarchies B1/B2/B3 (Practice Owner + 8 cabinets Justice League) |
| **Pilier #2** | Acquisition Triple-Canal (Meta Ads IA + Quiz Lovable + Affiliation 30%) | Canon ADR (35 ADRs L0+L1+L2) + Wiki 5 couches + 18 Memory files |
| **Pilier #3** | Marges Asset-Light (3× marges / 99% moins personnel) | 5 tiers pricing canon (`ADR-AAAS-PRICING-001` $300-50K MRR) |
| **Pilier #4** | Conformité fossé non-AIable (FDA/EMA = 100% humain) | Sobriété 1an+ (`ADR-SOBER-002`) + D6 anti-paperclip |
| **Funnel canon** | Quiz Lovable → Meta Ads → Checkout → Onboarding → Affiliation | Hierarchy → ADR ratification → Skill canon → Memory 18 files |
| **Mécanisme onboarding** | Aha Moment Threshold + Paywall post-personnalisation | ADR public → Notion canon → Wiki hand-off |
| **Métrique north-star** | LTV/CAC ratio (MedVie = 25:1) | Canon compliance (D1 receipts ≥ 80% sur tous claims) |
| **Risque dominant** | Greenwashing badges compliance non-AIable | Lenteur acquisition / time-to-market |
| **Sister ICP canon** | **Solaris** (Visual First / DAM) — acquisition-led | **Nexus** (Data First / Conformité) — structuration-led |
| **Hybrid ICP** | **Orbiter** (Mobile First / Terrain) — hybrid terrain + central | (idem — Orbiter = sister canon des 2 paradigmes) |

### Paradigme 1 : Acquisition-First (MedVie modèle)

**Définition canon** : Paradigme où **l'acquisition client est la priorité architecturale #1**, structuration interne minimale, asset-light radical, conformité = fossé non-AIable (humain obligatoire).

#### 4 piliers canon MedVie (sister canon `03_IT/2026-06-17_etude-de-cas-medvi` verbatim)

1. **<Pilier #1 — Opérations AI-Natives>** : Substitution systématique des opérateurs humains par agents IA sur tâches répétitives. Le critère de sélection n'est pas le coût mais le caractère réversible de la décision — tant qu'annulable, un agent suffit.
2. **<Pilier #2 — Acquisition Triple-Canal>** : Combinaison : (a) Meta Ads avec créatifs IA à coût par lead minimal, (b) quiz Lovable convertit sans commercial, (c) affiliation agressive où 30% des clients viennent de parrainage = indépendant de Meta. Assurance anti-platform-risk.
3. **<Pilier #3 — Marges Asset-Light>** : Medvi : 2 employés / 16,2% marge brute. Concurrents : 2400 employés / 5,5% marge. Ratio = 3× marges avec 99% moins de personnel. L'asset-light élimine l'opex structurellement compresseur de marge.
4. **<Pilier #4 — Conformité Fossé Non-AIable>** : La conformité FDA/EMA reste 100% humaine et constitue le vrai fossé défensif. Les actifs non-copiables (compliance, données propriétaires, relations régulateurs) sont la défense réelle.

#### Sister canon Pricing (synthèse canon Pricing 5 tiers + MedVie pricing)

MedVie canon pricing (à reconfirmer via guide sœur canon) : **$179 first month + $299/month recharges** (acquisition-first = prix d'appel bas pour funnel Lovable, marges compensées par volume + rétention).

Sister canon AaaS 5 tiers (`ADR-AAAS-PRICING-001` RATIFIED 2026-06-24) :
- T1 PME Solo Founder = **$300-500/an** (intro market, post-accuponcture)
- T2 PME Solo Standard = **$500-1000/an**
- T3 PME Groupe = **$4000-5000/an** (Tizi Plus sister, 8× Tier 1)
- T4 Nexus mid-market = **$15K MRR = $180K ARR**
- T5 Orbiter Enterprise = **$50K MRR baseline → $500K Year 10**

#### Sister canon Solopreneur (guide `02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ`)

- **AI Employee vs AI Agent** : Nick vend un *AI employee* (digital worker) ≠ un "agent". Pricing = $5K/mo flat. Promesse = outcomes business, pas "tokens économisés".
- **NYX Stack** : Codex (modèle) + Hermes (harness) + Orgo (cloud VM par client) + Composio (1 MCP = milliers outils tiers) + Agent Mail (1 email par agent) + Obsidian (second brain markdown). Anti-vendor-lock-in by design.
- **Diverge-then-Converge Niche** : diverger sur plusieurs industries (marketing agencies / law firms / insurance / manufacturers / wholesalers / real estate — JAMAIS healthcare/finance au début), observer où le marché tire, converger sur sous-niche (matrimonial law Floride).
- **Vertical Templating** : valeur marginale d'un nouveau client → 0. Templates par industrie (matrimonial law = case management + demand letters + follow-ups).
- **Content is King 2026** : contenu organique (YouTube / Twitter / Instagram) = overpowered en 2026. Funnel = *publish → they know you → Calendly → warm call → close*.

#### Sister canon Onboarding (guide `07_Growth/onboarding-flows-1460-patterns`)

- **Aha Moment Threshold** : point exact où l'individu *ressent* la valeur. Airbnb = 1ère réservation, Netflix = 1er visionnage, Mobbin = 1er screen saved.
- **Outcome Selling vs Feature Listing** : apps qui convertissent *montrent* ce que l'utilisateur deviendra capable de faire (Timo / Front / Alma).
- **Personalization Pre-Commitment** : 23% des apps personnalisent pendant onboarding (AI apps = seulement 7%). Mécanisme = *commitment and consistency bias* (Cialdini).
- **Paywall Timing Architecture** : 22% des apps placent paywall pendant onboarding. 3 fenêtres optimales : (1) post-aha moment (Duolingo / Bipal), (2) post-personalization (Grammarly +20% upgrades), (3) anticipation événementielle (Focus Flight haptic).
- **Permission Priming Screen** : custom screen précède popup système → +30-50% accept rates.
- **Friction Reallocation Theorem** : ajouter friction à un endroit *retire* friction ailleurs. House = +15% conversion en splittant signup. Mural = +10% rétention J+7 en remplaçant pop-ups par checklist 6-step.
- **Founder's Touch as Trust Signal** : CEO video (Airbnb) / CEO note (Basecamp) / handwritten flower (One Year). Dans économie AI-générative, ce signal = *plus* précieux, pas moins.

#### Sister canon ICP Solaris (acquisition-led Visual First / DAM)

Solaris = paradigm Acquisition-First dominant. Marché = agences créatives (DAM = Digital Asset Management). Killer Feature = génération visuels IA à coût marginal → funnel META ads visuels → quiz Lovable visuel → onboarding screens custom (Mobbin patterns). 5 piliers canon `ADR-ICP-SOLARIS-001` RATIFIED 2026-06-24 :
1. Persona "Technicien fondateur E-Myth"
2. Mantra "L'illusion du sur-mesure" (verbatim ×3)
3. Marché 136,1 Mds$ intégrateurs système (`ADR-MARKET-STUDY-001`)
4. 3-ICP sister-symétrique (Solaris / Nexus / Orbiter)
5. Killer Feature = Agentic Governance (4 mécanismes : Action Space Bounding / Sandboxing / HITL Dynamique / Traçabilité AI-Act)

### Paradigme 2 : Structuration-First (A0's OS modèle)

**Définition canon** : Paradigme où **la structuration canon (ADR + Wiki + Memory + Sobriété) est la priorité architecturale #1**, acquisition client secondaire, conformité = Sobriété 1an+ imposée, anti-paperclip VETO.

#### 5 sub-types persona canon (sister `ADR-ICP-NEXUS-001` AR/01..05)

Nexus = paradigm Structuration-First dominant. 5 sub-types AR/01..05 persona canon :
- AR/01 Practice Owner Solo (1 avocat / 1 médecin / 1 expert-comptable)
- AR/02 Practice Owner + 1-2 associés (Justice League × 2)
- AR/03 Cabinet 3-5 (Justice League × 3-5)
- AR/04 Cabinet moyen 6-15 (Justice League × 6-15)
- AR/05 Grand cabinet 15+ (Justice League × 15+)

Chaque sub-type a sa propre **matrice routage A3** + **5 tier pricing** + **Sobriété 1an+**.

#### 8 hiérarchies B1/B2/B3 (A0 OS V2 canon)

- **B1 — Practice Owner** (A0 lui-même ou équivalent) : émet intentions, valide milestones, ne touche JAMAIS aux configs
- **B2 — 8 cabinets Justice League** (1 par LDxx : LD01_Business / LD02_Meaning / LD03_Health / LD04_Cognition / LD05_Solarpme / LD06_Nexus / LD07_Orbiter / LD08_Legacy) — chacun = squadre de sub-paths wiki `ld0X_<domaine>/`
- **B3 — 32 squads Zero-PII** (4 par cabinet B2 = 8 × 4 = 32 squads, ex : Picard / Riker / Data / Crusher pour LD01_Business)

#### 5 tiers pricing canon (`ADR-AAAS-PRICING-001` RATIFIED 2026-06-24)

Voir sister canon ci-dessus. Mapping Structuration-First :
- T1-T3 = solo founder / indépendant pro / PME groupe = structuration-first (canon Wiki + ADR fourni en standard)
- T4-T5 = Nexus mid-market / Orbiter Enterprise = structuration-first + Sobriété 1an+ obligatoire

#### 8 LDxx Life Wheel + Sobriété 1an+

8 Life Domains canon (LD01-LD08) + **Sobriété 1an+ obligatoire** (`ADR-SOBER-002` RATIFIED 2026-06-21) : hard-stop si greenwashing badges compliance, hard-veto si kernel pivot demandé par A1 Rick Sobriété (mode alerte réactivé Q3 2026).

### Sister Canon Mapping 3 Variants (AaaS Doctrine)

| ICP Variant | Paradigme dominant | Sister canon pricing tier | Acquisition méca canon |
|---|---|---|---|
| **Solaris** (Visual First / DAM) | **Acquisition-friendly** (MedVie-aligned) | T1 PME Solo Founder $300-500/an → T3 PME Groupe $4000-5000/an | META ads visuels IA + Quiz Lovable visuel + Onboarding screens custom (Mobbin patterns) |
| **Nexus** (Data First / Conformité) | **Structuration-friendly** (A0 OS-aligned) | T4 Nexus mid-market $15K MRR | Canon ADR public + Notion canon + Wiki hand-off + Sobriété 1an+ |
| **Orbiter** (Mobile First / Terrain) | **Hybrid** (terrain + central) | T5 Orbiter Enterprise $50K MRR baseline → $500K Year 10 | Terrain (NYX Stack Orgo VM par client) + Central (ADR canon + Sobriété) |

**Doctrine** : Solaris = acquisition-led (MedVie-aligned) car DAM = volume + viralité + faible ticket moyen. Nexus = structuration-led (A0-aligned) car conformité = Sobriété 1an+. Orbiter = hybrid car terrain (mobile-first ops) + central (canon Wiki ADR).

## Ratification A0 — Verbatim

> **A0 message verbatim 2026-06-24** : *"apartir de ces 3 guide, tu dois cree un des ADR de Business OS"*

> **A0 choix Option 1** (parmi 3 options proposées post-batch 2 guides MedVie-related + canon sister 03_IT pré-existant) : **Option 1 = ADR-AAAS-ACQUISITION-DOCTRINE-001 Acquisition-First vs Structuration-First** (nouveau).

Options 2 et 3 (rejetées pour cette run, à reconsidérer Q3 2026) :
- **Option 2** : `ADR-ICP-SOLARIS-002 Onboarding Premium Canon` (déjà couvert dans `ADR-ICP-SOLARIS-001` §5 Killer Feature + sister guide `07_Growth/`)
- **Option 3** : `ADR-PRICING-RECHARGE-001 Pricing Recharge Architecture` (déjà couvert dans `ADR-AAAS-PRICING-001` §"Pricing Reconciliation")

## Verification (D1 receipts gathered this turn)

| Critère | Source canon | D1 receipt |
|---|---|---|
| Guide 03_IT MedVie = 6 490 chars | `03_IT/2026-06-17_etude-de-cas-medvi-400m-2-employes-agents-ia.md` | `wc -c` match exact |
| Guide 02_Ops Solopreneur = 22 708 chars | `02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md` | `wc -c` match exact |
| Guide 07_Growth Onboarding = 21 873 chars | `07_Growth/onboarding-flows-1460-patterns-acquisition-funnel-Qsq-Sj_rojU.md` | `wc -c` match exact |
| MedVie 400M$ Y1 / 2 employés | `03_IT/...medvi L29-30` | canon found |
| MedVie 16,2% marge brute vs 5,5% concurrents | `03_IT/...medvi L30` | canon found |
| 30% clients affiliation MedVie | `03_IT/...medvi L29` | canon found |
| NYX Stack (Codex + Hermes + Orgo + Composio + Agent Mail + Obsidian) | `02_Ops/...solopreneur` NYX Stack concept | canon found |
| $5K/mo flat AI Employee pricing | `02_Ops/...solopreneur` AI Employee concept | canon found |
| Aha Moment Threshold | `07_Growth/...onboarding` Aha Moment concept | canon found |
| 23% personalize / 7% AI apps | `07_Growth/...onboarding` Personalization Pre-Commitment concept | canon found |
| 22% paywall in onboarding | `07_Growth/...onboarding` Paywall Timing Architecture concept | canon found |
| House +15% conversion / Mural +10% rétention J+7 | `07_Growth/...onboarding` Friction Reallocation Theorem concept | canon found |
| Sister ADR-AAAS-PRICING-001 = 5 tiers USD $300-500/an → $50K MRR | `ADR-AAAS-PRICING-001 L54-65` | canon RATIFIED 2026-06-24 |
| Sister ADR-L2-AAAS-001 = 3 Variants Solarpunk | `ADR-L2-AAAS-001` (L0/L1/L2 canon) | canon RATIFIED 2026-06-21 |
| Sister ADR-ICP-SOLARIS-001 = 5 piliers canon E-Myth | `ADR-ICP-SOLARIS-001` (frontmatter line 2-12) | canon RATIFIED 2026-06-24 |
| Sister ADR-SOBER-002 = Sobriété 1an+ + D6 anti-paperclip | `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002` | canon RATIFIED 2026-06-21 |
| Sister ADR-MARKET-STUDY-001 = 136,1 Mds$ intégrateurs système | `ADR-MARKET-STUDY-001` | canon RATIFIED 2026-06-24 |
| Sister ADR-META-006 = D6 root causes catalog | `_SPECS/ADR/L1_Life_OS/ADR-META-006` | canon RATIFIED |

## Conséquences

### Positives

- **Canon explicite Acquisition-vs-Structuration** : avant ce ADR, la doctrine AaaS 3 Variants Solaris/Nexus/Orbiter existait mais le **paradigme acquisition dominant** par Variant était implicite. Maintenant = canon explicite + sister 3 ICP ADR.
- **Sister canon riche** : 3 guides Geordi MedVie-related (51 071 chars cumulés) + 6+ ADRs L2 + 3 guides onboarding premium → rétro-validation croisée.
- **Pricing canon 5 tiers aligné** : Solaris = T1-T3 acquisition-friendly (intro market / volume), Nexus = T4 structuration-friendly (mid-market conformité), Orbiter = T5 hybrid (Enterprise custom).
- **D6 anti-paperclip mitigation** : Sobriété 1an+ obligatoire empêche greenwashing badges compliance non-AIable. MedVie = fossé FDA/EMA 100% humain → sister canon A0 = Sobriété 1an+ (`ADR-SOBER-002`).
- **D7 anti-effondrement** : canon Acquisition-First vs Structuration-First dans ADR = wiki + ADR (pas seulement Notion live). Backup 3 guides Geordi = 51 071 chars canon persistés.
- **Skill canon-batch-spawn réutilisable** : ce ADR a été produit en ~25 min vs ~3h manual (skill `canon-batch-spawn` v1.0.0 RATIFIED 2026-06-24).
- **JTBD sister à créer** : `JTBD-ACQUISITION-001 Acquisition-First vs Structuration-First` sister `JTBD-ICP-SOLARIS-001` (à créer Q3 2026).

### Négatives

- **Risque greenwashing "tout acquisition-first"** : si A0 bascule trop Solaris vers MedVie-aligned, risque de minimiser Sobriété → **mitigation** : `ADR-SOBER-002` hard-veto D6 anti-paperclip.
- **2 paradigmes parfois mutuellement exclusifs** : MedVie "substitution agents IA systématique" vs A0 "Sobriété 1an+ obligatoire" → **mitigation** : Nexus Variant = structuration-led strict, Orbiter = hybrid.
- **Pricing canon MedVie $179/$299 non confirmé verbatim dans guides** : canon sister pricing `ADR-AAAS-PRICING-001` 5 tiers USD est la source de vérité. MedVie $179/$299 = à reconfirmer via guide sœur canon (canon sister potentiel).
- **Volumétrie funnel MedVie (CAC 200€, LTV 5000€, ratio 25:1)** : canon annexe guide 03_IT A3-01 → à reconfirmer en pricing canon sister T1.

### Sister canon obligatoire

- **JTBD-ACQUISITION-001** dans `_doctrine/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/` (sister JTBD-003 Painkiller Variants + JTBD-ICP-SOLARIS-001) — à créer Q3 2026.
- **B2 OFFER BRAND REVENUE_ENGINE.md update** : ajouter section "Acquisition Doctrine" sister "Pricing Canon" (SHADOW_ACTIVE → RATIFIED Q3 2026).
- **Wiki handoff** : `wiki/hand_offs/aaas_acquisition_doctrine_2026-06-24.md` — backup 3 guides canon + synthèse 2 paradigmes.
- **Notion OMK HQ page** : ajouter section "Acquisition Doctrine" sister "Pricing Canon" + "AaaS Doctrine".
- **Skill `/aaas-acquisition-derive`** : sister `/pricing-canon-derive` (automation -80% manual extraction).

## Cross-refs

- [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) — AaaS Pricing Canon 5 tiers USD ($300-500/an → $50K MRR → $500K Year 10) RATIFIED 2026-06-24
- [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — AaaS Doctrine 3 Variants (Solarpme/Nexus/Orbiter + 4 Leviers Solarpunk + Saru 1000T Kardashev Type 3) RATIFIED 2026-06-21
- [`ADR-ICP-SOLARIS-001`](./ADR-ICP-SOLARIS-001_icp-solaris-structuration.md) — ICP Solaris Structuration (5 piliers canon E-Myth) RATIFIED 2026-06-24
- [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) — ICP Nexus Structuration (Data First / Conformité, 5 sub-types AR/01..05) RATIFIED 2026-06-24
- [`ADR-ICP-ORBITER-001`](./ADR-ICP-ORBITER-001_icp-orbiter-structuration.md) — ICP Orbiter Structuration (Mobile First / Terrain, hybrid acquisition+structuration) RATIFIED 2026-06-24
- [`ADR-SOBER-002`](../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) — Anti-Paperclip doctrine (Sobriété 1an+ + 7 hard-stop triggers) RATIFIED 2026-06-21
- [`ADR-MARKET-STUDY-001`](./ADR-MARKET-STUDY-001_the-builders-2026.md) — Étude de marché The Builders 2026 (136,1 Mds$ TAM intégrateurs système) RATIFIED 2026-06-24
- [`ADR-OMK-004`](./ADR-OMK-004_pivot-supabase-cloud-vercel.md) — OMK Stack Pivot (Vercel + Supabase Cloud, single SaaS mode)
- [`ADR-META-006`](../L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) — D6 catalog (append-only)
- **Guide canon 03_IT** : `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/03_IT/2026-06-17_etude-de-cas-medvi-400m-2-employes-agents-ia.md` (6 490 chars, Minozan N-9rovSvCEA)
- **Guide canon 02_Ops** : `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md` (22 708 chars, Greg Isenberg × Nick from Orgo)
- **Guide canon 07_Growth** : `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/07_Growth/onboarding-flows-1460-patterns-acquisition-funnel-Qsq-Sj_rojU.md` (21 873 chars, Mobbin Qsq-Sj_rojU)
- **Skill canon-batch-spawn** : `C:\Users\amado\.claude\skills\canon-batch-spawn\SKILL.md` (v1.0.0 RATIFIED 2026-06-24)
- **Skill youtube-takeout-to-lifeos** : `C:\Users\amado\.claude\skills\youtube-takeout-to-lifeos\SKILL.md` (YouTube → Geordi pipeline)
- **Skill youtube-to-guide** (à créer Q3 2026) : sister `/youtube-takeout-to-lifeos` pour mode transcript+guide (D6 #48 Antigravity Premium standard)

## D6 Lessons shipped (2026-06-24)

| # | Lesson | Source |
|---|---|---|
| 66 | **Acquisition-First vs Structuration-First canon** : 2 paradigmes mutuellement éclairants mappeés aux 3 ICP Variants AaaS (Solaris = acquisition-led / Nexus = structuration-led / Orbiter = hybrid). Source = 3 guides Geordi MedVie-related convergents (51 071 chars cumulés) + 3 ICP sisters RATIFIED. | Cette session |
| 67 | **MedVie sister retro-validation AaaS Doctrine** : MedVie 400M$ Y1 / 2 employés / 16,2% marge brute (vs concurrents 5,5%) = proof que paradigm Acquisition-First fonctionne à l'échelle PME-Solo → valide implicitement Solaris Variant acquisition-led. Mais Sobriété 1an+ obligatoire = sister canon Nexus structuration-led pour ne pas basculer greenwashing. | Cette session |
| 68 | **Skill canon-batch-spawn v1.0.0 production-ready** : ce ADR produit en ~25 min orchestrated vs ~3h manual extraction (skill `canon-batch-spawn` RATIFIED 2026-06-24). ROI session 2026-06-24 = -86% manual time. | Cette session + skill canon-batch-spawn |
| 69 | **Pricing canon MedVie $179/$299 à reconfirmer** : canon sister pricing `ADR-AAAS-PRICING-001` 5 tiers USD est la source de vérité canon actuelle. MedVie $179/$299 = à reconfirmer via guide sœur canon ou nouvelle ingestion. Sister JTBD-PRICING-001 à créer. | Cette session (caveat D1 verify-before-assert) |

---

**RATIFIED 2026-06-24 par A0 Amadeus sur Option 1 des 3 ADR proposés**. Canon Acquisition-First vs Structuration-First fixé pour 1an minimum. Sister canon 3 guides Geordi + 6+ ADRs L2 + skill canon-batch-spawn. D6 lessons #66-#69 shipped.

---

## B-Layer Binding (runtime ownership — additive 2026-06-25)

> ADR canon above is **immutable** (Regle d'Or #3). This canon was authored on
> Life OS (L1) A3 twins **before** the B1/B2/B3 runtime existed in `.claude/agents/`.
> Those L1 twin refs stay valid as **cross-cutting engines** (12WY metrics / PARA /
> GTD). This block adds the missing **L2 Business ownership** — the runtime agents
> that actually EXECUTE this domain. Dispatch law: B1 routes -> B2 dispatches -> B3
> executes (`mindsets/B1_Manifesto.md`). Roster truth: `ADR-CANON-001` (hero<->civilian).
- **B1 gatekeeper:** `b1-jerry-prime` (SYSTEMIZE)
- **B2 owners (cross-domain):** `b2-04-superman-growth` (Guardians, top funnel) + `b2-05-johnjones-sales` (Illuminati, close)
- **B3 squads + triggers:** `mindsets/B2_Superman_Growth_Dispatch.md` + `mindsets/B2_JohnJones_Sales_Dispatch.md`
