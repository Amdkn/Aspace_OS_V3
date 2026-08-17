---
type: Relation
title: Roster canon 8 Domaines L2 — Notion prime AGENTS.md (ADR-CANON-001)
description: Résolution A0 du 2026-06-02 sur les divergences AGENTS.md (manifeste) vs Notion AGENT_REGISTRY_DB (lore) : Notion prime ; AGENTS.md = structure index avec addendum daté. 8 domaines L2 alignés (Growth/Sales/Product/Ops/IT/Finance/People/Legal) avec leurs squads B3 canon.
tags: [l2-roster, 8-domaines, notion, agents-md, adr-canon-001, squad-canon, ruling]
generated: { by: minimax-m3, at: 2026-08-17T21:24:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:24:00Z }
sources:
  - id: comparison-roster
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/comparisons/comparison_l2_roster_divergence.md"
    title: "Comparison: L2 squad roster divergence — AGENTS.md vs B3 squad canon"
    last_modified: 2026-05-31
  - id: l2-fractal
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_l2_fractal_b1b2b3.md"
    title: "Concept: L2 B1/B2/B3 — The Fractal Command Stack"
    last_modified: 2026-05-31
okf_version: "0.2"
---

# Roster canon 8 Domaines L2 — Notion prime AGENTS.md (ADR-CANON-001)

> **Pattern observé** : sur 8 squads B3, **6 sont des abréviations 4-membres** d'un
> roster Notion plus large (4-10), **2 sont des divergences réelles** tranchées par A0
> en faveur Notion.

## 1. Les 8 Domaines × 8 Squads canoniques (post-ruling 2026-06-02)

| Domaine / Squad | Leader canon | Membres canon (Notion AGENT_REGISTRY_DB) | n |
|---|---|---|---:|
| **Growth / Guardians of the Galaxy** | Star-Lord | Star-Lord · Gamora · Rocket · Groot · Drax · Mantis | 6 |
| **Sales / Illuminati** | **Black Bolt** | Black Bolt · Iron Man · Mr Fantastic · Namor · Professor X · Doctor Strange | 6 |
| **Product / The Avengers** | Captain America | Cap · Iron Man · Thor · Hulk · Black Widow · Hawkeye · Scarlet Witch | 7 |
| **Ops / Fantastic Four** | Mr Fantastic | Mr Fantastic · Invisible Woman · Human Torch · The Thing | 4 |
| **IT / Kang Dynasty** | Kang Prime | Kang Prime · Iron Lad · Scarlet Centurion · Immortus · Victor Timely · Rama-Tut | 6 |
| **Finance / Thunderbolts** | **Bucky Barnes** | Bucky · Yelena Belova · Red Guardian · Ghost · Taskmaster · U.S. Agent | 6 |
| **People / X-Men** | Professor X | Prof X · Cyclops · Jean Grey · Wolverine · Storm · Beast · Nightcrawler · Rogue | 8 |
| **Legal / Eternals** | Ikaris | Ikaris · Sersi · Ajak · Kingo · Phastos · Sprite · Druig · Thena · Gilgamesh · Makkari | 10 |
| **TOTAL** | | | **53** |

## 2. Divergences historiques tranchées par A0 (2026-06-02)

- **Finance / Thunderbolts** : AGENTS.md (Red Hulk, Taskmaster, Zemo, Ghost) ↔ Notion
  canon (Bucky-led). Seuls Ghost + Taskmaster en commun. **Résolu : Notion prime**.
  Red Hulk et Zemo sont retirés.
- **Sales / Illuminati** : AGENTS.md (Illuminati I-V, generic role names) ↔ Notion canon
  (Black Bolt-led, named characters). **Résolu : Notion prime**. Les rôles génériques
  I-V sont retirés.

## 3. Outcome (ADR-CANON-001)

1. **Notion `AGENT_REGISTRY_DB`** + transcriptions fidèles = source de vérité pour le lore des rosters.
2. **AGENTS.md** = structure index (corps immuable préservé). Un **Reconciliation Addendum**
   daté (ADR-CANON-001) a été appended, restating les 8 rosters canon complets.
3. **2 divergences réelles résolues en faveur Notion** (Finance → Bucky-led Thunderbolts,
   Sales → Black Bolt-led Illuminati).
4. Vérification 2026-06-02 : aucune surface de doctrine vivante ne portait les anciens noms,
   seule AGENTS.md, maintenant réconciliée.
5. **Follow-up non bloquant** : renommer/aligner les fichiers `agents/L2_A3_*.md` capsules.

## 4. Pourquoi cette résolution existe

Avant la résolution, **deux surfaces canon décrivaient les squads et divergeaient** :

- `00_Amadeus/01_Identity_Core/AGENTS.md` : manifeste (abréviations 4-membres)
- Chaque `B2_Area_Domains/<NN>/B3_Squad_<X>/00_B3_SQUAD_CANON.md` + `B3_Area_Warp_Core/<NN>/01_B3_AGENT_ROSTER.md` :
  transcriptions du Notion `AGENT_REGISTRY_DB` (4–10 membres)

Le roster B3 lui-même stipulait : *« si Notion et la doctrine locale divergent, Notion
gagne pour le lore, la doctrine locale gagne pour les chemins ».* → Suivi en 2026-06-02.

## 5. Cross-casting intentionnel

Note : Iron Man, Mr Fantastic, Professor X apparaissent dans **deux** squads (Illuminati
emprunte les archétypes « conseil secret »). C'est volontaire dans le lore Notion,
pas une erreur.

## 6. Statut Constitution v1.0

ADR-CANON-001 est postérieur à l'article 5 (Constitution rétrograde les ADR en
jurisprudence). Cependant, le **rôle Notion = source de vérité** est une décision
de gouvernance (qui fait foi pour le lore), pas une décision bloquante — il survit
sans tension à Article 6 (pas de blocage anticonstitutionnel).

## Liens entrants

- `l2-fractal-b1-b2-b3.md` — où logent ces squads dans B3 Warp Core
- `agents-md-identity-canon.md` — la version index, désormais addendumée
- `constitution-aspace-v1.md` — article 5 / 6 cohabitent avec ce ruling
