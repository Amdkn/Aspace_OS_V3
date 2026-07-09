---
type: adr
id: ADR-NEXUS-NICHE-001
title: Niches de l'industrie du Coaching — arbitrage B2B Coaching Premium × Agences Business Development
status: RATIFIED
date: 2026-07-05
ratified_by: A+ (arbitrage direct — sélection de niche)
variant: Nexus (⚖️ Data First / Conformité)
sisters:
  - ADR-ICP-NEXUS-001_icp-nexus-structuration.md
  - ADR-MARKET-STUDY-001_the-builders-2026.md
  - ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md
  - ADR-AAAS-PRICING-001_aaas-pricing-canon.md
  - 20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-011_omk_nexus_bos_poc_initiation.md
canon_source: ADR-CANON-001 (roster 8 domaines B2 + squads)
---

# ADR-NEXUS-NICHE-001 — L'arbitrage des niches Coaching B2B

> Origine : Deep Research NotebookLM (synthèse OMK Nexus), arbitré par A+. Ce document
> **fige la décision de niche** (couche marché) ; le PoC exécutable vit dans son sœur
> `ADR-LD01-011_omk_nexus_bos_poc_initiation.md` (zone Book, portée par Hermes).

## Correction canon préalable (D4 — nommer l'erreur, prouver, clore)

La source Deep Research a **collé des tags LDxx** sur les domaines Business (People=LD06,
IT=LD07, Ops=LD01, Product=LD04, Growth=LD08, Sales=LD05, Legal=LD03, Finance=LD02).
**Erreur de catégorie** : `LDxx` = axe **Life Wheel** (Discovery) — LD01 Business, LD02
Finance, LD03 Health, LD04 Cognition, LD05 Social, LD06 Family, LD07 Creativity, LD08 Impact.
Les **8 domaines Business** (People/Ops/Product/Growth/Sales/IT/Finance/Legal) sont un **autre
axe** (sous Jerry B1), et ils vivent **tous sous LD01 (Career/Business)** de la Life Wheel.
Preuve : agent registry ADR-CANON-001 + arbre `LD01_Business_Book/`. → Cet ADR utilise le
mapping domaine↔captain↔squad canon, **sans** les tags LDxx erronés.

## Contexte — l'arbitrage

A+ **rejette** les niches médicales (Biohacking) et psychologiques (TDAH) : piège
réglementaire fédéral US (HIPAA, FDA) qui a coulé le précédent (voir §Medvi). Il **recentre**
l'offensive Nexus sur la frontière B2B la plus lucrative et la moins régulée :

> **Niche = l'intersection {Cabinets de Coaching Premium} × {Agences de Business Development}.**

Matière noire de ces agences = **logistique, pas médicale** : transcriptions d'appels de vente
(Zoom/Gong), playbooks informels non documentés, flux de prospection LinkedIn éparpillés.
Nexus capture cette connaissance et la fige en savoir propriétaire.

## Case study (attribué à la source — NON vérifié A'Space, sert de rationale)

> ⚠️ D1 : chiffres Watchgang/Medvi issus du Deep Research, **non vérifiés ce turn**. Traités
> comme narratif de cas, pas comme fait A'Space.

- **Watchgang** (Matthew Gallager) : faillite à ~60 salariés — masse salariale explose, la
  décision humaine devient le goulot d'étranglement. Déclic 2024 : *les humains sont le
  bottleneck*.
- **Medvi** : ~1,8 Md$ avec 2 employés (80 % logistique déléguée à des agents + marque
  blanche). **Mais** chute éthique/judiciaire : acquisition grand public, tunnels d'affiliation
  agressifs, deepfakes → intervention FDA.
- **Leçon Nexus** : extraire la *puissance* de Medvi (agents + coût écrasé), **rejeter** son
  ventre mou (mass-market, affiliés sauvages, deepfakes). D'où → **haute couture, 100 clients**.

## Décision

### D1 — Niche verrouillée
Business/Sales Coaching Premium + Agences Business Development. Ni médical ni psy.

### D2 — Baseline pricing (sœur ADR-AAAS-PRICING-001)
**1 000 $/mois × 100 clients premium = 1,2 M$ ARR.** Structure humaine minimale (A+ vision +
ingénieur Abdaty). Zéro stock. Marge nette cible **> 90 %** via plan fixe MiniMax + inférence
locale. (Baseline niche ; ne réécrit pas le canon 5-tiers de PRICING-001, s'y adosse.)

### D3 — PoC tri-axial (mapping canon, triptyque plan-L2 §4.1)

| Axe | Domaine B2 | Captain (DC) | Squad (Marvel B3) | Rôle PoC |
|---|---|---|---|---|
| **T1 Backbone** | People | GreenLantern | X-Men (Prof X) | partition stricte humain/agents (humain garde vision A0 + closing grands comptes ; IA prend 100 % taxe admin) |
| **T1 Backbone** | Operations | Batman | Fantastic Four | SOPs Notion → **Skills agentiques `.md` exécutables** (bus d'état PARA live, zéro conduite du changement) |
| **T1 Backbone** | IT | Cyborg | Kang Dynasty | **cache sémantique local** (SQLite/OPFS, latence ~0, zéro token cloud sur re-hit) + watchdog nettoyage anti bash-hang / KV-cache saturation |
| **T2 GTM** | Product | Flash | Avengers | segmentation création : modèle local léger pour 1er jet, **MiniMax M3 1M ctx** réservé à l'injection matière-noire en validation finale |
| **T2 GTM** | Growth | Superman | Guardians | scrapers locaux, **>700 signaux d'affaires** (levées, embauches sales via Apollo, goulots Reddit), tri **AARRR**, séquences pré-rédigées en base locale |
| **T2 GTM** | Sales | JohnJones | Illuminati | **Quiz de Diagnostic d'Inférence** (pattern Medvi assaini) : prospect entre ses volumes → simulation → cartographie de pertes ($X RH+tokens gaspillés) → closing par preuve ROI |
| **Duo** | Finance | WonderWoman | Thunderbolts | **Token Plan MiniMax (5,1 Md tokens / 50 $)** + inférence locale → coût variable écrasé en charge fixe. Anti-Paradoxe de Jevons |
| **Duo** | Legal | Aquaman | Eternals | **proxy DLP déterministe** (expurge PII/secrets avant réseau), contrats marque-blanche audités SOC2 / EU AI Act, liquidité contractuelle (zéro lock cloud long-terme) |

### D4 — Ancrage souveraineté
MiniMax fixed plan vérifié canon (sœur `ADR-LLM-COST-COMPARE-001` : 5,1 Md tokens / 50 $/mois,
D1-verified). GPT banni (M3 default). Inférence locale = anti-Jevons + anti-PII-leak.

## Ce qui reste à BUILD (le fork — non ratifié, choix A+)

L'arbitrage de niche est **RATIFIED**. Deux chantiers d'implémentation restent ouverts :
- **A. Duo Legal** — scripts de rédaction/redaction DLP Supabase (proxy PII avant réseau).
- **B. Growth** — les 11 prompts de signal d'acquisition (framework AARRR, scrapers locaux).

## Bus d'état (référence)

```json
{ "status":"ACTIVE","cycle":"Q3-2026","week":"W01",
  "stage":"poc_b2b_coaching_agency_structured",
  "target_niche":"BUSINESS_COACHING_AND_DEV_AGENCIES",
  "pricing_baseline":"1000_USD_MRR_TARGET_100_CLIENTS",
  "next_action":"FORK: DLP_LEGAL | GROWTH_11_SIGNAL_PROMPTS" }
```

## Réversibilité
Append-only. Statut RATIFIED sur la niche uniquement ; le fork build reste choix A+.

*A+ arbitre la niche. A0-Amodei trace. Mapping canon corrigé (pas de LDxx erronés). Le PoC
exécutable = sœur ADR-LD01-011 (Book/Hermes). Portes over Freins : Beth seul veto.*
