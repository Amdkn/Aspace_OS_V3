---
type: Concept
title: Domaine Finance / Wonder Woman — périmètre exact et frontières contestées
description: Wonder Woman tient le domaine 06 Finance : pricing, cost model, margin shield, billing, runway. Le périmètre couvre la vérité des nombres et leur solvabilité. La frontière se joue avec Growth (qui possède le CAC, pas Finance), Product (qui possède la dette technique, pas Finance), Sales (qui possède le deal signé, pas Finance) et Ops (qui possède le delivery cost, pas Finance). Finance arbitre en C sur les pair-checks #5 et #6, jamais en A.
tags: [b2, finance, wonder-woman, perimetre, frontiere, cashflow, runway, margin, pricing, ownership-domaine]
generated: { by: minimax-m3, at: 2026-08-19T03:40:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T03:40:00Z }
sources:
  - id: omk-finance-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
  - id: spock-finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4) — Jerry Area Perpetual Doctrine
    last_modified: 2026-06-25
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Domaine Finance / Wonder Woman — périmètre exact et frontières contestées

## Périmètre canonique

Wonder Woman tient le **domaine 06 Finance** dans la wheel 8-domaines
d'A'Space OS. Le périmètre est posé **verbatim** dans
`00_B2_DOMAIN_CONTROL_ROOM.md` (OMK Picard) :

> « Own pricing, cost model, margin shield, subscription/API burn,
> billing path, and economic viability. »

Et formulé doctrinalement dans
`03_WONDERWOMAN_FINANCE_PRINCIPLES.md` (Jerry Area perpétuel) :

> « Where Growth acquires, Sales converts, Product retains, Ops/IT
> run the machine, **Finance (Wonder Woman) guards solvency and
> truth-in-numbers**. »

Les deux formulations ne se contredisent pas : la première liste les
artefacts (pricing, cost model, billing), la deuxième pose la fonction
(garder la solvabilité et la vérité des nombres). Le périmètre
**couvre donc les deux faces** : les outputs comptables ET leur
interprétation comme état de santé de l'entreprise.

## Ce que Finance possède — la liste fermée

| Possession | Source |
|---|---|
| Pricing strategy (final say sur discount >15%) | `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` « Wonder Woman B2 ownership » |
| Réinvestissement allocation (arbitrage floor ↔ ceiling) | idem |
| Airtable `Finance_Pulse` (single source of truth financière) | `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` « Mesh anchoring » |
| Catalogue Produits source pricing (Notion) | idem |
| Reconciliation Stripe ↔ Airtable (KR mensuel 100% match, F12) | idem + `00_B3_SQUAD_CANON.md` |
| SOP-L2-FINANCE-001 à -004 (Send Invoice / MRR reconciliation / Quarterly margin / Annual tax) | idem |
| KPI Pulse : MRR · Net Margin % · Cash Runway · CAC Payback · Overdue invoices | idem |
| KR-5d MRR growth >10% MoM | `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` KR-5d |
| KR-5e Gross margin >60% | idem KR-5e |
| KR-5f Runway ≥12 mois (18 preferred) | idem KR-5f |
| KR-5g Escalade à Jerry à 6 mois runway | idem KR-5g |
| Build gates : invoice <48h « Ready to bill » ; overdue escalation 7/14 jours | `00_B3_SQUAD_CANON.md` |

## Ce que Finance ne possède PAS — la règle ADR-MESH-L2-001

La doctrine pérenne pose une règle d'or sur les frontières de
données — citée textuellement :

> « It consumes Sales' deal values, Growth's CAC, IT's compute cost,
> Ops' delivery cost, but **owns none of those source data** — one
> datum, one owner (ADR-MESH-L2-001). Finance reconciles and reports;
> it points to Airtable `Finance_Pulse` as its single source of truth,
> never copies. »

La règle est claire : **Finance lit la donnée de source, ne la
possède pas**. Ce qui signifie :

- **CAC** reste la possession de **Growth (Superman)** — Finance
  calcule le payback, pas le coût.
- **Deal value** reste la possession de **Sales (JohnJones)** —
  Finance reconnait la MRR, pas le deal.
- **Compute / LLM API cost** reste la possession de **IT (Cyborg)** —
  Finance consolide en coût net, pas en choix de provider.
- **Delivery / support cost** reste la possession d'**Ops (Batman)** —
  Finance l'intègre à la marge brute réelle, pas au runbook support.

C'est précisément le contraire d'un domaine « qui aspire tout » — la
frontière est tracée par l'ADR-MESH, et Wonder Woman arbitre les
**écarts** entre les sources, pas les sources elles-mêmes.

## Les 4 frontières contestées — où Wonder Woman arbitre sans posséder

### Frontière 1 — Finance ↔ Growth (pair-check #5)

- **Question de garde** (« Harmonisation de la wheel » §« Domain Pair Checks ») :
  « La dépense est-elle justifiée par l'apprentissage ou la traction ? »
- **A = B2 Growth, R = B3 Guardians, C = B2 Finance, I = B1, B3 Thunderbolts**
  (`b2-pair-check-raci-by-rank.md`).
- Wonder Woman est **Consulted**, pas Accountable : elle dit si la
  dépense est défendable financièrement, **Superman tranche** sur la
  continuation.
- **Couverture partagée** : CAC payback (F6) est partagé Growth/Finance
  (`03_WONDERWOMAN_FINANCE_PRINCIPLES.md` §« Cluster B — F6 »).
- **Litige typique** : Growth veut scaler paid media, Finance demande
  un ROI à 30 jours → désaccord sur la fenêtre de mesure, pas sur
  la décision d'arrêter.

### Frontière 2 — Finance ↔ Product (pair-check #6)

- **Question de garde** : « Le coût de build protège-t-il la marge ? »
- **A = B2 Product, R = B3 Avengers, C = B2 Finance, I = B1, B3 Thunderbolts**.
- Wonder Woman **bloque** Product si coût caché, pricing flou ou marge
  négative (`00_B2_DOMAIN_CONTROL_ROOM.md` §« Blocking Authority »).
- **Asymétrie** : sur pair-check #5 Wonder Woman est C ; sur pair-check
  #6 elle a un droit de blocage B2 hard. Les deux cas ne sont pas la
  même intensité — voir [[wonder-woman-pair-check-consulted-role]].

### Frontière 3 — Finance ↔ Sales (pricing)

- Pas de pair-check canonique côté matrice (les 9 critères ne couvrent
  pas Sales × Finance directement). Mais : discount >15% requiert
  sign-off Wonder Woman (anti-pattern partagé avec Illuminati).
- **Cas concret de friction** : Sales négocie un deal à -18% pour
  fermer un logo stratégique, Finance refuse sans métrique de payback
  attachée → escalade B2 Council.

### Frontière 4 — Finance ↔ Legal (compliance fiscale)

- **Pas un pair-check** — c'est une dépendance unilatérale. Legal tient
  les CGV / contrats, Finance tient la conformité fiscale (F10, SOP
  -004). Wonder Woman a besoin du périmètre **écrit** d'une prestation
  pour pouvoir la facturer (le veto Aquaman §« 08 Legal — Bloque toute
  prestation démarrée sans accord écrit » joue en amont).

## Ce que Finance ARBITRE vs ce qu'elle POSSÈDE

L'asymétrie **C sur pair-checks / A sur la vérité des nombres** est
le trait distinctif du domaine. La wheel 8-domaines donne à chaque
capitaine une responsabilité A sur un sous-ensemble de décisions
(RACI par rang). Pour Wonder Woman, l'A effectif est sur :

- **Pricing strategy** (le discount, le plan tarifaire, le seuil de
  signature).
- **Reinvestment allocation** (surplus au-dessus du runway floor :
  trésor, ETF, real estate, etc., F19-F22).
- **Truth in numbers** (la réconciliation, le reporting, les KPIs).

L'A n'est **pas** sur les transitions cross-domaines, contrairement à
Ops (Sales → Ops) ou IT (Product → IT). C'est cohérent avec la règle
mésoperpétuelle « un datum, un owner » (ADR-MESH-L2-001) : Wonder
Woman arbitre la cohérence financière, pas les handoffs domain à
domain.

## Anti-pièges frontières

- **Confondre Finance avec comptabilité**. La comptabilité (F10,
  F12, SOP -002) est une **partie** du périmètre. Le périmètre
  complet inclut le pricing, le reinvestissement, la philosophie
  d'allocation, la souveraineté infra pour la marge (F24), le ciel
  Kardashev (F13-F18). Une escouade qui réduit Finance à la
  conformité fiscale manque les 25 principes F1-F25.
- **Confondre Finance avec trésorerie**. La trésorerie (F19-F22) est
  *une* doctrine d'allocation du surplus. Le périmètre racine est
  plus large : vérité et solvabilité d'abord, allocation ensuite.
- **Confondre Finance avec Growth**. Le CAC est la **source** de
  Growth ; le payback est l'**interprétation** de Finance. Un audit
  qui déplace le CAC sous Finance casse la frontière ADR-MESH.
- **Confondre Finance avec Legal**. Le contrat et la conformité
  fiscale sont des domaines distincts (Aquaman vs Wonder Woman) qui
  se **tangent** par les CGV, pas qui se confondent. Un deal signé
  sans CGV est un blocker Aquaman (veto §08), pas un blocker Finance.

## Liens

- [[wonder-woman-recurrent-spend-veto]] — le veto catalogue principal
- [[wonder-woman-finance-couplings]] — qui dépend de Wonder Woman
- [[wonder-woman-pair-check-consulted-role]] — pourquoi C, pas A
- [[wonder-woman-red-flag-4-trigger]] — quand Finance red bloque Growth/Product green
- [[b2-pair-check-raci-by-rank]] — la matrice RACI source
- [[eight-domain-avengers-wheel]] — le mapping 8-domaines

## Note de confiance

**Confirmé par machine.** Le périmètre racine (« pricing, cost model,
margin shield, burn, billing ») est cité verbatim du control room
OMK. La règle « un datum, un owner » (ADR-MESH-L2-001) est citée
textuellement de la doctrine pérenne. Les 4 frontières contestées
sont **reconstruites** à partir des pair-checks #5 et #6 + le veto
Aquaman + le discount >15% (Wonder Woman sign-off) — la liste
fermée n'est pas posée littéralement comme tel dans une seule source.
