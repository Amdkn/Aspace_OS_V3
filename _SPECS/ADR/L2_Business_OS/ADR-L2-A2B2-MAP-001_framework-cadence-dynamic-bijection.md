---
id: ADR-L2-A2B2-MAP-001
title: Framework A2 ↔ Domaine B2 — Cadence Opératoire Dynamique (axe 3, rotate par cycle 12WY)
status: RATIFIED
date: 2026-06-27
ratified: 2026-06-27 — A0 Amadeus GO chat ("ratifies les axes maintenant")
proposed_by: A0 jumeau numérique (Opus 4.8) on A0 directive (push BD domains sur frameworks A2, plan giggly-wiggling-fern.md §4.3-4.5 approuvé 2026-06-27)
creation_go: A0 plan approval 2026-06-27 (plan §6 action 5)
deciders: [A0 Amadeus]
domain: L2 Business OS / Doctrine / A2↔B2 Framework Cadence / Dynamique
tags: [#ADR #a2-b2 #framework-cadence #dynamique #12wy-rotation #deal-optimized #gatekeeper-a1-b1 #triple-axe #canonical]
related:
  - ADR-L2-BDLD-MAP-001 (PROPOSED 2026-06-27 — axe 1 ancre LD statique, sœur directe)
  - ADR-L2-AAAS-001 (RATIFIED 2026-06-21 — 3 variants, axe produit Summers)
  - ADR-CANON-001 (roster B2/B3 source of truth)
  - ADR-SOBER-002 (Anti-Paperclip — Posture C, no rotation autonome sans HITL)
  - ADR-META-001 (Anti-Paresse D1-D8)
sources_canons:
  - "fancy-hugging-bengio.md §3.2 (6 A2 engines × A3 twins canon) + §3.1 russian-doll 12WY⊃PARA⊃DEAL / Ikigai⊃LifeWheel⊃Muse"
  - "mindsets/B1_Manifesto.md (A1↔B1 pairing: Beth↔Jerry breadth, Morty↔Summers focus)"
  - "mindsets/Summers_Dispatch_Doctrine.md (axe produit ⊥ axe domaine Jerry)"
  - "A0 directive chat 2026-06-26/27 (mapping A2↔B2 + self-correction 12WY→IT, PARA→Ops + dynamisme rotation)"
provenance: Née 2026-06-26/27 de la directive A0 « pousser les domaines BOS sur les frameworks A2 de Life OS », incluant sa self-correction en direct (12WY mieux à IT/Kang qu'à Ops ; PARA à Ops/F4). Sœur de l'axe 1 (ADR-L2-BDLD-MAP-001). Comble le gap : aucun ADR ne posait la cadence opératoire A2↔B2 ni sa nature dynamique.
---

# ADR-L2-A2B2-MAP-001 — Framework A2 ↔ Domaine B2 (Cadence Opératoire Dynamique)

## Status

**RATIFIED** — 2026-06-27 par A0 Amadeus (« ratifies les axes maintenant »). N'édite aucun ADR RATIFIÉ.

## Context

`ADR-L2-BDLD-MAP-001` (axe 1) pose l'**ancre de sens** (B2 ↔ LD officier Discovery, statique). Manquait la **cadence opératoire** : sur quel framework Life OS A2 chaque domaine business *tourne*. A0 a fourni le mapping + sa nature **dynamique** (rotation par cycle 12WY). C'est le 3e axe du triple-axe (priorité BD ⊥ ancre LD ⊥ cadence framework).

**D3 nuance** : les 3 axes sont **orthogonaux** — un domaine a une place dans chacun, et ils ne coïncident pas (sauf People, doublement Discovery — voir D2).

## Décision

### D1 — Le 3e axe : cadence framework A2 (additive, dynamique)

Chaque B2 domaine **tourne SUR un framework Life OS A2** comme discipline opératoire. C'est le pont isomorphe **A2↔B2** rendu concret : un domaine n'a pas qu'un manager (B2) + squad (B3), il **opère selon la discipline d'un framework A2**.

### D2 — Mapping initial (cycle Q3 2026)

| Triptyque | B2 (DC + Marvel) | Framework A2 (Ship) | A1 owner |
|---|---|---|---|
| T1 | **People** (GreenLantern / X-Men) | **Life Wheel** — Discovery (Zora) | Beth |
| T1 | **Operation** (Batman / Fantastic Four, 4) | **PARA** — Enterprise (Computer) | Morty |
| T1 | **IT** (Cyborg / Kang Dynasty) | **12WY** — SNW (Curie) | Morty |
| T2 | **Product** (Flash / Avengers) | **Ikigai** — Orville (9 = 4P+5H) | Beth |
| T2 | **Growth** (Superman / Guardians) | **GTD** — Cerritos (Holo Deck) | Morty |
| T2 | **Sales** (JohnJones / Illuminati) | **DEAL** — Protostar (Holo Janeway) | Beth |
| Duo | **Finance + Legal** | *rotatif — folded progressivement (D4)* | — |

**Logique** : Beth (le *pourquoi*) → People / Product / Sales ; Morty (le *comment*) → IT / Ops / Growth. Le russian-doll Morty (12WY⊃PARA⊃DEAL) se distribue IT/Ops/Sales ; Beth (Ikigai⊃LifeWheel) → Product/People.

**Self-correction A0 intégrée** : 12WY→IT/Kang (Kang = maître du temps ↔ 12 Week *Year*) ; PARA→Ops/F4 (4 membres ↔ 4 lettres P/A/R/A ↔ 4 A3 Enterprise). L'idée transitoire « F4 + Franklin Richards = 5 » est **caduque** (Ops→PARA, pas 12WY) → F4 reste 4. *Open : ajout Franklin Richards = amendement `ADR-CANON-001` si A0 le veut.*

**Nuance counts** : taille squad B3 ≠ nb agents framework A2 (Avengers 7 vs Ikigai 9 ; Guardians 6 vs GTD 5 ; Kang 6 vs 12WY 5). Le framework = la **cadence/lentille**, le squad **exécute dedans**. Pas d'égalité 1:1.

### D3 — Couche gatekeeper : qui gouverne quel axe (A1↔B1)

Canon `B1_Manifesto.md` : **Beth↔Jerry** (breadth/SYSTEMIZE) · **Morty↔Summers** (focus/SHIP). Conséquence d'allocation :
- **Beth/Jerry gouvernent l'axe 1** (ancre LD statique, `ADR-L2-BDLD-MAP-001`) — le sens/breadth.
- **Morty/Summers gouvernent l'axe 3** (cadence framework dynamique, ce ADR) — le focus/livraison, cadencé par les cycles 12WY de Morty et shippé par variant AaaS de Summers.

### D4 — Dynamisme (mécanisme v1 — gated A0/cycle, Posture C)

Le mapping A2↔B2 **n'est pas figé** ; il rote par cycle 12WY :
1. **Cycle N** : map initial (D2).
2. **Fin de cycle** : Protostar/DEAL (Gwyn) mesure le **D11** (bande passante libérée) par domaine.
3. Le domaine le plus DEAL-libéré (tourne seul) → son framework **gradue** et rote vers un membre du **Duo** le cycle suivant.
4. **Finance fold-in en 1er** (runway), **Legal ensuite** (driver AI-Act 2026-08-02).
5. **Posture C** : chaque réassignation = **HITL A0** (jamais de rotation autonome — `ADR-SOBER-002`).

### D5 — Couche L0 parente (différée, domaine Rick)

Au-dessus de A1/B1, la meta-orchestration L0 (Jumeau Numérique Hermes Perso/Pro supervisant Codex+Claude Code) gouvernera à terme la cadence. **Différée** (Hermes hardening + subscriptions + veto Rick S1) → ADR kernel `ADR-L0-META-ORCH-001` à créer par Rick. Hors scope de ce ADR (qui reste L2).

## Verification (D1 receipts — Opus 2026-06-27)

| Critère | Source | Verdict |
|---|---|---|
| 6 frameworks A2 + crews | `fancy-hugging §3.2` | ✅ exact |
| Russian-doll 12WY⊃PARA⊃DEAL / Ikigai⊃LifeWheel | `fancy-hugging §3.1` | ✅ |
| A1↔B1 pairing Beth↔Jerry / Morty↔Summers | `B1_Manifesto.md` | ✅ |
| Axe produit ⊥ axe domaine | `Summers_Dispatch_Doctrine.md` | ✅ |
| Self-correction 12WY→IT / PARA→Ops | A0 directive 2026-06-27 | ✅ intégrée |

## Conséquences

### Positives
- **Pont A2↔B2 concret** : chaque domaine business opère selon une discipline Life OS éprouvée (pas juste un squad).
- **Dynamisme = anti-stagnation** : la rotation par cycle évite qu'un domaine fossilise une cadence inadaptée ; DEAL pilote l'optimisation.
- **Duo Finance/Legal intégré progressivement** sans surcharge initiale.
- **Gouvernance claire** : axe 1 = Beth/Jerry, axe 3 = Morty/Summers.

### Négatives / risques
- **Complexité rotation** : mécanisme v1 à raffiner ; risque de churn si rotation trop fréquente → mitigation : HITL A0/cycle + rotation seulement sur graduation DEAL prouvée.
- **Counts non-1:1** : peut dérouter ; clarifié D2 (cadence ≠ effectif).
- **Dépendance L0 Hermes** pour l'automatisation de la rotation → différée (D5), rotation manuelle A0 d'ici là.

## Cross-refs
- [`ADR-L2-BDLD-MAP-001`](./ADR-L2-BDLD-MAP-001_business-domains-lifewheel-bijection.md) — axe 1 (ancre LD), sœur directe
- [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — axe produit Summers
- [`ADR-CANON-001`](./ADR-CANON-001_roster-source-of-truth.md) — roster B2/B3
- `mindsets/B1_Manifesto.md` · `mindsets/Summers_Dispatch_Doctrine.md` · `mindsets/Jerry_Dispatch_Doctrine.md`
- Plan : `C:/Users/amado/.claude/plans/giggly-wiggling-fern.md` §4.3-4.5

---

**RATIFIED 2026-06-27 par A0 Amadeus.** Axe 3 du triple-axe = cadence opératoire dynamique. Canon fixé 1an+ minimum, D4 append-only. Couche L0 parente différée (domaine Rick).
