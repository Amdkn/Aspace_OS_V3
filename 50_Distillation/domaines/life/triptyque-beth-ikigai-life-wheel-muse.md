---
type: Concept
title: Triptyque BETH — Ikigai ⊃ Life Wheel ⊃ Muse de Libération
description: Architecture meaning canonique — trois couches imbriquées où le sens (Ikigai) englobe l'équilibre (Life Wheel) quienglobe la libération (DEAL Muse).
tags: [triptyque, beth, ikigai, life-wheel, muse, liberation, architecture]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: orville-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/21_Ikigai_Orville/A2_Orville_Spec.md
    title: A2 Orville Spec — Triptyque BETH
    last_modified: 2026-05-20
  - id: orville-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/21_Ikigai_Orville/README.md
    title: 21_Ikigai_Orville README — Doctrine verrouillée
    last_modified: 2026-06-21
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — Triptyque BETH
    last_modified: 2026-05-20
  - id: protostar-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md
    title: A2 Holo Janeway Spec — Triptyque BETH
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Triptyque BETH — Ikigai ⊃ Life Wheel ⊃ Muse de Libération

Le triptyque BETH est l'architecture **meaning** de Life OS. Il décrit la relation d'inclusion entre les trois couches sémantiques sous le veto d'A1 Beth (Ikigai Centrée).

## La structure

```
Ikigai (Orville) ⊃ Life Wheel (Discovery) ⊃ Muse de Libération (Protostar via Data)
```

Cette inclusion est stricte : passer à la couche inférieure exige que la couche supérieure soit validée.

- **Ikigai** porte le **sens** — 4 Pillars (Profession/Mission/Passion/Vocation) × 5 Horizons (H1/H3/H10/H30/H90).
- **Life Wheel** porte l'**équilibre** — 8 domaines LD01-LD08 télémétrés par ZORA.
- **Muse de Libération** porte la **libération** — pipeline D/E/A/L Protostar.

## Imbrication opérationnelle

- Le sens filtre l'équilibre : une intention alignée Ikigai peut viser un domaine Life Wheel précis.
- L'équilibre filtre la libération : on ne libère que ce qui sert un domaine équilibré.
- La libération préserve le sens : si D11 bandwidth > gain, retour à D (Define).

## Routage par intention A0

| Intention A0 | Triptyque actif | A1 → A2 → A3 |
|---|---|---|
| "Vérifier sens (Ikigai)" | BETH couche 1 | A1 Beth → A2 Orville → Kelly + Isaac → GO/NO-GO |
| "Vérifier équilibre (Roue)" | BETH couche 2 | A1 Beth → A2 Discovery → Saru + Stamets |
| "Libérer du temps" | BETH couche 3 | A1 Beth → A2 Protostar (via Data) → Dal → Rok-Tahk → Zero → Gwyn |

## Sortie canon

Chaque couche écrit son packet dans `00_Amadeus/40_SYMPHONY_BUS/state.json` :

```yaml
ship: ORVILLE | DISCOVERY | PROTOSTAR
alignment: GREEN | YELLOW | RED
beth_recommendation: approve | hold | veto | needs_evidence
morty_route: <next_ship>
evidence_paths: [...]
```

## Kardashev trajectory (H1 → H90)

Le triptyque BETH est la projection sur le temps de la trajectoire Kardashev-4 (héritée de `00_Amadeus/01_Identity_Core/SOUL.md`) :

- **H1** = désactiver le Hard Mode systémique (1 an).
- **H3** = flotte autonome (3 ans).
- **H10** = contre-infrastructure Solarpunk (10 ans).
- **H30** = civilization engine continental (30 ans).
- **H90** = ascension Kardashev / Source Wall (90 ans).

Orville voit l'ensemble du fractal (A1 → A3) à travers le temps (H1 → H90) — perspective Kardashev-4.