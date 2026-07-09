---
id: ADR-L2-BDLD-MAP-001
title: Business Domains ↔ Life Wheel Bijection — Double-Axe Canon (priorité BD ⊥ ancre LD)
status: RATIFIED
date: 2026-06-27
ratified: 2026-06-27 — A0 Amadeus GO chat ("ratifies les axes maintenant")
proposed_by: A0 jumeau numérique (Opus 4.8) on A0 directive (mapping Business-Domaines-sur-Life-Wheel, plan giggly-wiggling-fern.md approuvé 2026-06-27)
creation_go: A0 plan approval 2026-06-27 (plan §6 action 1 + §11 action 3 "GO pour ADR-L2-BDLD-MAP-001")
deciders: [A0 Amadeus]
domain: L2 Business OS / Doctrine / 8 Domaines ↔ Life Wheel / Double-Axe
tags: [#ADR #bijection #double-axe #business-domains #life-wheel #ld01-ld08 #triptyque #a3-discovery #supersede-tags #canonical]
related:
  - ADR-L2-AAAS-001 (RATIFIED 2026-06-21 — tags LD lâches §D2/§D3 superseded par cette bijection)
  - ADR-CANON-001 (roster source of truth hero↔civilian)
  - ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24 — ICP Coach sub-type #4)
  - ADR-OMK-NEXUS-TRANSFORM-001 (RATIFIED 2026-06-24 — 1er ship OMK→Nexus)
  - ADR-META-001 (Anti-Paresse D1-D8, Verify-Before-Assert)
  - ADR-SOBER-002 (Anti-Paperclip — Posture C, no cron sans HITL)
sources_canons:
  - "fancy-hugging-bengio.md §3.6 (officiers A3 Discovery LD01-LD08 canon)"
  - "Registre agents .claude/agents/ (a3-discovery-* officiers + b2-01..08 + 53 b3)"
  - "A0 directive chat 2026-06-26 (bijection B2-doctrine ↔ A3-doctrine + priorité BD 2 triptyques + 1 duo)"
  - "Audit Opus D1 2026-06-27 (giggly-wiggling-fern.md §2.2 — bijection 8↔8 sans collision)"
provenance: Née 2026-06-26 de la clarification A0 (double-axe) écartant le mapping "lazy" de Gemini (étiquettes, pas doctrines). Vérifiée D1 par Opus contre les officiers A3 Discovery canon. Comble le gap : aucun ADR ne posait la bijection officielle 8 domaines Business ↔ 8 Life Wheel ; les seuls tags existants (ADR-L2-AAAS-001 §D3) étaient lâches/incohérents.
---

# ADR-L2-BDLD-MAP-001 — Business Domains ↔ Life Wheel Bijection (Double-Axe Canon)

## Status

**RATIFIED** — 2026-06-27 par A0 Amadeus (« ratifies les axes maintenant »). Respecte Règle d'Or #3 : **n'édite aucun ADR RATIFIÉ** — supersede uniquement les *tags LD lâches* de `ADR-L2-AAAS-001` §D2/§D3.

## Context

**D3 nuance racine** — Trois numérotations divergentes coexistaient sans bijection canon :
1. **IDs agents runtime** `b2-01..08` (ordre d'instanciation .claude/agents/).
2. **Dossiers Geordi guides** `01_Product..08_People` (ordre de corpus).
3. **Tags LD lâches** dans `ADR-L2-AAAS-001` §D2/§D3 (RATIFIÉ) — ex. « Cyborg IT (LD03) », « Superman Growth (LD07) » — qui **conflictent** avec les officiers A3 Discovery (LD03 = Health/Culber, LD07 = Creativity/Reno) et entre eux.

**D6 root cause** : aucun ADR ne posait l'**ancre de sens** (quel domaine business répond à quel officier Life Wheel). Conséquence : chaque session ré-dérivait un mapping, et Gemini (sans accès SSOT) a produit un mapping « lazy » par étiquettes. A0 a fourni la bijection correcte (B2-doctrine ↔ A3-doctrine) le 2026-06-26.

**Audit D1 (Opus, 2026-06-27)** : la bijection A0 est une **bijection 8↔8 sans collision**, tous les officiers A3 Discovery correctement nommés avec leur LD canon (vérifié contre `fancy-hugging §3.6` + registre agents).

## Décision

### D1 — Double-axe canon (deux axes indépendants)

Le Business OS porte **deux axes orthogonaux** :
- **Axe priorité BD** = ordre de construction des domaines (interne au L2).
- **Axe ancre LD** = enracinement de sens de chaque domaine dans le Life Wheel via son officier A3 Discovery (anti-dérive).

Un domaine business a **une place dans chaque axe** ; les deux ne coïncident pas (c'est voulu).

### D2 — Axe priorité BD : 2 triptyques + 1 duo

| Groupe | Domaines | Rôle |
|---|---|---|
| **Triptyque 1** | People · Operation · IT | cœur empire — l'org qui construit (bâti en 1er) |
| **Triptyque 2** | Product · Growth · Sales | go-to-market |
| **Duo** | Finance · Legal | garde-fous transverses |

### D3 — Axe ancre LD : bijection 8↔8 (CANON)

| LD | Officier A3 Discovery | Life Wheel | Domaine Business B2 | `agentType` B2 | Squad B3 |
|---|---|---|---|---|---|
| LD01 | Book | Business | **Operation** | `b2-02-batman-ops` | Fantastic Four |
| LD02 | Saru | Finance | **Finance** | `b2-07-wonderwoman-finance` | Thunderbolts |
| LD03 | Culber | Health | **Legal** | `b2-08-aquaman-legal` | Eternals |
| LD04 | Tilly | Cognition | **Product** | `b2-03-flash-product` | Avengers |
| LD05 | Stamets | Social | **Sales** | `b2-05-johnjones-sales` | Illuminati |
| LD06 | Burnham | Family | **People** | `b2-01-greenlantern-people` | X-Men |
| LD07 | Reno | Creativity | **IT** | `b2-06-cyborg-it` | Kang Dynasty |
| LD08 | Georgiou | Impact | **Growth** | `b2-04-superman-growth` | Guardians |

### D4 — Supersession ciblée (Règle d'Or #3 respectée)

Cette bijection **supersede les tags LD lâches** de `ADR-L2-AAAS-001` §D2/§D3 (ex. IT=LD03, Growth=LD07) — **uniquement les annotations LD inline**, pas le contenu doctrinal (3 variants × 4 leviers Solarpunk restent intacts). `ADR-L2-AAAS-001` reste RATIFIÉ et immuable ; là où ses tags LD divergent de la table D3 ci-dessus, **la table D3 fait foi**.

### D5 — Règle d'usage runtime

Le routage d'un ship (ex. OMK/Nexus) **pulle ses domaines via la matrice produit** `Summers_Dispatch_Doctrine.md` (axe produit), **pas** par triptyque ni par ordre LD. Les triptyques = ordre de *build* ; l'ancre LD = racine de *sens* (chaque B2 répond à son officier Discovery pour l'anti-dérive Beth).

## Verification (D1 receipts — Opus 2026-06-27)

| Critère | Source | Verdict |
|---|---|---|
| 8 officiers A3 Discovery LD01-LD08 | `fancy-hugging §3.6` + registre `a3-discovery-*` | ✅ exact |
| Bijection 8↔8 sans collision | audit Opus lecture directe | ✅ 0 collision |
| `agentType` B2 réels | registre `.claude/agents/` (b2-01..08) | ✅ 8/8 existent |
| Squads B3 canon | `ADR-CANON-001` roster | ✅ exact |
| Conflit tags ADR-L2-AAAS-001 §D3 | lecture directe (IT=LD03, Growth=LD07) | ⚠️ superseded par D4 |

## Conséquences

### Positives
- **Anti-dérive** : chaque domaine business a une racine de sens Life Wheel (l'officier Discovery devient le contrôle drift Beth du domaine).
- **D7 cost-of-escalation** : fin de la ré-dérivation du mapping à chaque session.
- **Double-axe explicite** : priorité de build (triptyques) ≠ enracinement (LD) — plus de confusion entre les deux.
- **Règle d'Or #3 préservée** : aucun ADR RATIFIÉ édité.

### Négatives / risques
- **Tags lâches résiduels** dans d'autres docs (handoffs, plan §3.5) non corrigés rétroactivement (D4 append-only) → mitigation : cette bijection est la référence ; les divergences pointent ici.
- **Bijection ≠ exclusivité** : un ship peut puller plusieurs domaines (matrice Summers) — l'ancre LD ne restreint pas le routage produit (clarifié D5).

## Cross-refs
- [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — tags LD §D2/§D3 superseded (contenu intact)
- [`ADR-CANON-001`](./ADR-CANON-001_roster-source-of-truth.md) — roster hero↔civilian
- [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) — ICP Coach (1er ship)
- [`ADR-OMK-NEXUS-TRANSFORM-001`](./ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md) — pivot OMK→Nexus
- Plan : `C:/Users/amado/.claude/plans/giggly-wiggling-fern.md` (Business OS, §4 double-axe)
- Dispatch runtime : `C:/Users/amado/.claude/mindsets/Summers_Dispatch_Doctrine.md` + `Jerry_Dispatch_Doctrine.md`

---

**RATIFIED 2026-06-27 par A0 Amadeus.** Bijection ancre LD = racine de sens canon des 8 domaines Business. Canon fixé 1an+ minimum, D4 append-only.
