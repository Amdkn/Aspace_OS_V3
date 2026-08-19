---
type: Concept
title: Drift owner correction — Tilly+Spock NOT Saru+Stamets
description: Correction D3 critique du plan fancy-hugging-bengio §15.1.4. "Life Wheel drift" = Tilly (LD04 Cognition) + Spock (Areas), PAS Saru+Stamets. Verrouillé canon par append-only amendement.
tags: [drift-owner, tilly, spock, plan-15-1-4, d3-correction, areas-not-a3]
generated: { by: minimax-m3, at: 2026-08-19T04:12:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:12:00Z }
sources:
  - id: discovery-spec-d3
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — D4 self-contradiction closed §15.1.4
    last_modified: 2026-06-21
  - id: references-index-d3
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A3_Discovery_References_Index.md
    title: A3 Discovery References Index — D3 nuance PAS drift owner
    last_modified: 2026-05-20
  - id: tilly-spec-d3
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/A3_Tilly_LD04_Spec.md
    title: A3 Tilly Spec — D3 nuance critique drift
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Drift owner correction — Tilly+Spock NOT Saru+Stamets

## Énoncé canon

**"Life Wheel drift" = Tilly (LD04 Cognition) + Spock (Areas)**, PAS Saru+Stamets.

Verbatim canon (A2_Discovery_ZORA_Spec.md, ligne 125) :
> *"D4 self-contradiction fermée — 'Life Wheel drift' = Tilly (LD04 Cognition) + Spock (Areas), PAS Saru+Stamets."*

## Origine de la confusion

Le plan canonique `fancy-hugging-bengio.md §15.1.4` mappait initialement :
- *"Life Wheel drift → A3 Saru + Stamets"*

Cette lecture suggérait que les A3 twins Saru (LD02) et Stamets (LD05) étaient **owners** du drift Life Wheel. **Incorrect.**

## Correction D3 (verrouillée 2026-06-21)

Le canon verrouillé distingue deux rôles :
- **Narrow findings** : Saru (LD02) + Stamets (LD05) rapportent leur drift narrow (finance + social).
- **Drift owner** : **Tilly (LD04 Cognition) + Spock (Areas)** — le drift cognitif traverse les A2 ships via Areas (PARA), pas via A3 twins.

Pourquoi Tilly ? LD04 = HARD SAFETY + STOP authority. Tilly supervise la **clarté mentale** nécessaire à la mesure des 8 LDs — donc elle est **owner du diagnostic**, même quand le signal narrow vient de Saru ou Stamets.

Pourquoi Spock (Areas) ? Les **Areas PARA** (responsabilités continues sans deadline) sont le **substrat** sur lequel le drift se manifeste. Sans Areas saines, la mesure Life Wheel perd son cadre.

## Sources canoniques

| Source | Phrase clef |
|---|---|
| `A2_Discovery_ZORA_Spec.md` (D4 close) | *"drift = Tilly (LD04) + Spock (Areas), LD02 + LD05 = Saru + Stamets en narrow findings seulement"* |
| `A3_Discovery_References_Index.md` (D3 nuance) | *"PAS drift owner — 'Life Wheel drift' = Tilly (LD04) + Spock (Areas), PAS Saru+Stamets"* |
| `A3_Tilly_LD04_Spec.md` (D3 nuance critique) | *"PAS Saru+Stamets (correction §15.1.4 du plan). Tilly supervise aussi Item 12 cycle 12WY Q3 2026"* |
| `A3_Stamets_LD05_Spec.md` (Doctrine isolation) | *"PAS drift owner — Life Wheel drift = Tilly (LD04) + Spock (Areas), PAS Saru+Stamets"* |
| `A3_Saru_LD02_Spec.md` | Anti-paperclip 1000T — Saru reste narrow findings LD02 |

**Cinq sources convergent** vers la même correction D3.

## Verdict distillation

`synthese-datee` — le **corps** des specs A3 reste valide (chaque A3 narrow finding tient) ; seule **l'attribution drift owner** a changé. Amendement append-only appliqué, non réécriture (D4 close 2026-06-21).

## Implication pratique

Un agent qui détecte un drift Life Wheel doit :
1. **Déposer** le signal narrow via son A3 twin (Saru/Stamets/etc.).
2. **Notifier** Tilly (LD04 cognition) — owner du diagnostic.
3. **Notifier** Spock (Areas) — owner du substrat.
4. **NE PAS** compiler un rapport Discovery final (A3 ne compile JAMAIS — cf. canon A2 ligne 66).

## Pièges documentés

- **Piège 1** : un agent qui détecte "Saru drift" pense que Saru est owner du drift Life Wheel global. **Faux** : Saru narrow, Tilly+Spock owner.
- **Piège 2** : un rapport Discovery compilé par Saru+Stamets viole le canon. Le pipeline A2/A3 est strict.
