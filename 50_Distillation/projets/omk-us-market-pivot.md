---
type: Concept
title: OMK US Market Pivot (2026-07-15)
description: Pivot explicite du projet OMK Business OS vers le marché US — Coach premium B2B ($7.5-25K ACV) + Enterprise mid-market, géographie US-first (Silicon Valley, NYC, Austin), compliance posture AI Bill of Rights + Colorado AI Act (PAS EU AI-Act).
tags: [concept, omk, us-market, pivot, ai-bill-of-rights, colorado-ai-act, adr-aaas-pricing-001]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: ownerbook-T1
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T1_people_ops_product.md"
    title: Ownerbook T1 §3 — US market canon (D1 receipts)
    last_modified: 2026-07-15
  - id: ownerbook-T3
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T3_legal_rd.md"
    title: Ownerbook T3 §10 — US market specific (vs Euro)
    last_modified: 2026-07-15
  - id: chart-producthunt
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/chartes_cycle_2/chart_T2_growth_producthunt_playbook.md"
    title: Chart T2 Growth ProductHunt Playbook
    last_modified: 2026-07-15
okf_version: "0.2"
---

# OMK US Market Pivot (2026-07-15)

## Définition

**Pivot explicite** du projet OMK Business OS vers le **marché US**
daté du 2026-07-15 dans les Ownerbooks T1/T2/T3. Le pivot n'est pas
implicite — il est déclaré comme **A0 directive** et appliqué à
trois dimensions : ICP, géographie, compliance.

## Les trois dimensions du pivot

**1. ICP — segment.** "US market — Coach premium B2B ($7.5-25K ACV)
+ Enterprise mid-market" (Ownerbook T1 §1, §3, §10). Abandon de
l'ICP Euro implicite antérieure (PME Solo Founder).

**2. Géographie.** "US-first (Silicon Valley, NYC, Austin, mid-market
SaaS hubs)" (Ownerbook T1 §geography). Channel ABM LinkedIn orienté
vers les hubs US.

**3. Compliance posture.** Abandon de l'EU AI-Act (2026-08-02) comme
primary driver. Adoption de :
- **AI Bill of Rights** (OSTP 2022, federal guidance)
- **Colorado AI Act 2026** (effective 2026-02-01, first US state AI law)
- **California AB 2013/2885** (training data transparency)
- **NYC LL 144** (automated employment decision tools audit)

EU AI-Act est **legacy Euro context flagged, not constraint** (Ownerbook
T3 §10).

## Pourquoi le pivot

**Contre Devin Karns $100M archetype** (Boris Cherny deepscan) : un
positionnement "AI tool" mid-market est saturé. Le pivot force une
**position différente** — *deployed agent squad, not a Slack bot*
(Ownerbook T1 §2). L'offre devient "Agent IA Squad $7.5-25K ACV" au
lieu de "SaaS subscription".

**Contre USD/EUR drift** : le Ownerbook T1 DoD-5 force
> "no Ownerbook section contradicts ADR-AAAS-PRICING-001 USD tiers
> or W40 cadence 5-4-3-4 — verify: grep -F "EUR\|5k€\|15k€"
> returns 0 hits"

L'ADR-AAAS-PRICING-001 (RATIFIED 2026-06-24) pose 5 tiers USD : PME
Solo Founder $300-500/an → Orbiter Enterprise $50K MRR → $500K Year 10.

## Les marqueurs concrets

- **ADR-AAAS-PRICING-001** RATIFIED 2026-06-24 — pricing canon USD
- **ADR-NEXUS-NICHE-001** RATIFIED — niche ICP canon
- **ADR-OMK-005** RATIFIED 2026-06-20 — tenant isolation guard
- **ADR-OMK-004** §D1 + §Condition B — JWT hook Cloud handoff
- **ADR-ICP-NEXUS-001** §Pilier 5 — Zero-PII Agentic Governance
- **ADR-CRUD-VIEWS** PROPOSED — view-type bibliography (à créer)

## Le forward-flight résiduel

**D6 honest gap** (Ownerbook T3 §3) : le canon antérieur contient
toujours des références EUR. Le pivot **n'est pas rétropropagé** dans
tous les artefacts. C'est un signal de living canon — la migration
EPO/USD n'est pas encore complète.

## Liens

- [[omk-business-os]] — le projet pivoté
- [[triptyque-v4-t1-t2-t3]] — la structure qui consume le pivot
- [[fifty-three-b3-agent-roster]] — la squad 53 agents déployable US
- [[picard-project-pattern]] — pattern antérieur (Euro context)

## Note de confiance

**Confirmé par machine.** 3 Ownerbooks documente le pivot (T1 §3, §10 ;
T2 §10 ; T3 §10). 6 chartes cycle 2 datées 2026-07-15 portent le
wording US. ADR-AAAS-PRICING-001 référencé comme RATIFIED 2026-06-24
— cohérent avec le pivot de 3 semaines après.

*Standing : pivot déclaré, 5 tiers USD pricing, exécution en cours Q3 2026.*
