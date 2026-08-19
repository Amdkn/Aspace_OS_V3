---
type: Concept
title: D11 Bandwidth Metric — output Gwyn, mesure de libération
description: Mesure canon de gain de bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine). Upkeep > gain → route back to Zero/Rok-Tahk.
tags: [d11, bandwidth, gwyn, liberation, maintenance-tax, karpathy-loop, fables-score]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: gwyn-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/04_Liberation_Gwyn/A3_Gwyn_Liberation_Spec.md
    title: A3 Gwyn Spec — Liberate
    last_modified: 2026-05-20
  - id: protostar-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md
    title: A2 Holo Janeway Spec — Karpathy loop
    last_modified: 2026-05-20
  - id: protostar-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/README.md
    title: 26_DEAL_Protostar README — D11 bandwidth metric
    last_modified: 2026-06-21
okf_version: "0.2"
---

# D11 Bandwidth Metric — output Gwyn, mesure de libération

D11 est la métrique canon de mesure de la libération Protostar. Output Gwyn (A3 Liberate), elle quantifie le gain réel vs la maintenance tax d'une automatisation ou d'une élimination.

## Définition canon

**D11 bandwidth metric** = gain de bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine).

## Sortie Gwyn

```yaml
a3: Gwyn
stage: Liberate
finding: liberated | not_liberated | maintenance_tax | needs_measurement | hypothesis
liberation_metric: ""
before_cost: ""
after_cost: ""
evidence:
  - path: ""
    note: ""
next_owner: HoloJaneway | Computer | Beth | SundayUplink
```

Output canon fichier : `d11_score.json`.

## Règle de Karpathy loop (plan §25.3)

```
D → E → A → L → retest
```

**Si val_score < target** → amend → re-D Define. Si upkeep tax > gain → route back to Zero (re-automatiser) ou Rok-Tahk (re-éliminer).

## Pas de libération sans métrique

Verbatim canon `A3_Gwyn_Liberation_Spec.md` :

> *"No metric means no liberation claim."*

Si Gwyn ne peut pas mesurer before/after, la libération n'est pas validée. Pas de saut à "liberated" sans chiffre.

## Fables 5 — référence Jack Roberts Meta-Strategy

La D11 bandwidth metric est aussi connectée à **Fables score** (cf. `00_fable5_jack_roberts_meta_strategy.md`). Les fables mesurent le coût cognitif des sous-agents et permettent à A0 de comparer avant/après une automatisation DEAL.

## Domaines d'application

D11 mesure :

- **Temps libéré** sur une tâche récurrente (ex: 30 min/semaine gagnées en automatisant un rapport).
- **Attention libérée** sur une charge cognitive (ex: 1 tour de clarification éliminée).
- **Charge LD03/LD04 réduite** (ex: stress sommeil ou cognition diminué).
- **Charge L0/L2 réduite** (ex: bandwidth L0 économisée par une délégation).

## Anti-paperclip Saru 1000T par Gwyn

D11 bandwidth = l'un des 4 superviseurs de Saru :

> *"Anti-paperclip Saru 1000T : Beth supervise Saru (LD02 Finance) via Book (LD01) + Tilly (LD04 Cognition review hebdo) + Gwyn (DEAL D11 bandwidth) + Rick veto rare (1×/an max)."*

Si une intention Saru a D11 négatif (upkeep > gain), Gwyn signale → Beth veto.

## Acceptation D11

- `liberation_metric` non-null.
- `before_cost` et `after_cost` documentés.
- `evidence_paths` avec mesures concrètes.
- `next_owner` clair si maintenance_tax ou not_liberated.