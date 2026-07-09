---
type: project-mapping
project: omk-nexus-coaching-premium
parent: ../MANIFEST.md
doctrine: D4 append-only · L1 gstack sober install · c1/c2/c3 enforced
date: 2026-07-05
author: Hermes Agent (HA, A3 Picard in PARA, re-roled)
---

# E-Myth ↔ gstack — mapping pour omk-nexus-coaching-premium

> Sister du plan `plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §4 L1-4`.
> Mapping **gstack commands** ↔ **canon E-Myth B1/B2/B3 du Business OS** pour ce projet spearhead.

## Pourquoi ce mapping

gstack = stack "CEO/eng-manager/designer/reviewer/QA/CSO/release" en mode dev. C'est **exactement** l'organigramme E-Myth B1→B2→B3 en mode SHIP. Mapping = la même structure sous deux noms. Quand un skill gstack s'invoque, il porte l'autorité canon d'un rôle B1/B2/B3.

## Table de correspondance

| gstack command | Rôle canon B1/B2/B3 | E-Myth domain | Sister canon |
|---|---|---|---|
| `/gstack-autoplan` (auto-review pipeline : CEO + design + eng + DX) | **Jerry Prime** (B1 Direction macro, gate SYSTEMIZE) + **Flash Product** (B2 Avengers captain) + **Superman Growth** (B2 Guardians lead) | E-Myth strategic cadrage + product spec + growth | `mindsets/Jerry_Mindset.md` SYSTEMIZE · `b1-jerry-prime` agent · `b2-03-flash-product` |
| `/gstack-cso` (Chief Security Officer : OWASP + STRIDE + secrets + dep supply chain) | **Aquaman Legal** (B2 Eternals lead, Ikaris AI-Act 2026-08-02) + **Cyborg IT** (B2 Kang Dynasty lead) | E-Myth Legal conformité + IT architecture | `mindsets/Jerry_Mindset.md` (B1 legal routing) · `b2-08-aquaman-legal` · `b2-06-cyborg-it` |
| `/gstack-ship` (merge + tests + review + VERSION bump + CHANGELOG + PR) | **Summers SHIP** (B1 SHIP gate, variant + ICP) + **Marvel/Avengers** sub-squad (Thor flagship, Iron Man tech, Scarlet Witch reality-bending) | E-Myth SHIP vers ICP Nexus + Avengers release | `mindsets/Summers_Mindset.md` SHIP · `b1-summers-nexus-omk-bos` · `b3-3-thor` |

## Mapping vers le projet coaching premium

| Phase projet (R1→R5 du MANIFEST) | gstack command à invoquer | Rôle canon E-Myth |
|---|---|---|
| R1 — Project ouvert + MANIFEST | (déjà fait) | — |
| R2 — 3 guides LD01 → `_PREMIUM.md` | (déjà fait) | — |
| R3 — Atelier pilote capté | (signals/ws_atelier_1.md → source pour R4) | — |
| **R4 — Triage 4 catégories du 1er atelier** | `/gstack-autoplan` sur le signal brut | **Jerry + Flash Product** = cadrage stratégique + structure produit |
| **R5 — 1ère capsule Coach premium (1 page)** | `/gstack-cso` (check conformité AI-Act) + `/gstack-ship` (release vers ICP Nexus) | **Aquaman Legal + Summers** = conformité + ship |

## Subtilités c1/c2/c3 (rappel)

- **c1** : `/gstack-*` invoqué depuis ce projet — aucun write dans `~/.claude/CLAUDE.md` (sacred P4, sister canon Règle d'Or #3)
- **c2** : `/browse` (headless chromium gstack) = OPTION, pas défaut. Notre harness `mcp__claude-in-chrome__*` prime
- **c3** : auto-update gstack = OFF. Wrapper `gstack-env.sh` neutralise en amont

## Sister canon (D4 traceability)

- Plan : `.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §4 L1-4`
- Wrapper : `omk-nexus-coaching-premium/.claude/commands/_lib/gstack-env.sh`
- README commands : `omk-nexus-coaching-premium/.claude/commands/README.md`
- War Room decision : `citadel/decisions/2026-07-05_l0_pocock_installed.md`
- ADR-ICP-NEXUS-001 (variant ICP coach premium)
- ADR-OMK-NEXUS-TRANSFORM-001 (Phase A-D canon)

*Mapping append-only. Si le projet change de phase → éditer ce fichier, pas le MANIFEST (canon Picard).*