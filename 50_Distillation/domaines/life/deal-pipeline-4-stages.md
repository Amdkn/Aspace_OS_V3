---
type: Concept
title: D.E.A.L. Pipeline 4 stages — Protostar Liberation Engine
description: Pipeline canonique Define → Eliminate → Automate → Liberate d'USS Protostar. Éliminer AVANT automatiser — Rok-Tahk protège du gaspillage automatisé.
tags: [deal, protostar, liberation, define, eliminate, automate, karpathy-loop]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: protostar-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md
    title: A2 Holo Janeway Spec — Doctrine canon DEAL 4 stages
    last_modified: 2026-05-20
  - id: protostar-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/README.md
    title: 26_DEAL_Protostar README
    last_modified: 2026-06-21
  - id: dal-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/01_Definition_Dal/A3_Dal_Definition_Spec.md
    title: A3 Dal Spec — Define
    last_modified: 2026-05-20
  - id: roktahk-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/02_Elimination_RokTahk/A3_RokTahk_Elimination_Spec.md
    title: A3 Rok-Tahk Spec — Eliminate
    last_modified: 2026-05-20
  - id: zero-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/03_Automation_Zero/A3_Zero_Automation_Spec.md
    title: A3 Zero Spec — Automate
    last_modified: 2026-05-20
  - id: gwyn-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/04_Liberation_Gwyn/A3_Gwyn_Liberation_Spec.md
    title: A3 Gwyn Spec — Liberate
    last_modified: 2026-05-20
okf_version: "0.2"
---

# D.E.A.L. Pipeline 4 stages — Protostar Liberation Engine

DEAL est le framework **libération** d'A'Space OS, géré par USS Protostar (Holo Janeway) via Affine Edgeless. Pipeline canonique à 4 stages — D, E, A, L — avec règle dure : **éliminer avant automatiser**.

## Les 4 stages et leurs A3 canon

| Étape | A3 twin | Output canon | Rôle canon |
|---|---|---|---|
| **D**efine | Dal | `pattern_definition.md` | Pattern detection + outcome specification |
| **E**liminate | Rok-Tahk | `elimination_proposal.md` | NO-GO propositions + permission de delete |
| **A**utomate | Zero | `skill_<name>/SKILL.md` + risk_class + D1 proof | Skill creation + sub-agent deployment |
| **L**iberate | Gwyn | `d11_score.json` | D11 bandwidth measurement + maintenance tax |

## Karpathy loop appliqué (plan §25.3)

```
D Define ───► A3 Dal capture pattern friction (Mariner inbox upstream)
    │
E Eliminate ──► A3 Rok-Tahk NO-GO propose (Tendi review upstream)
    │
A Automate ─► A3 Zero crée skill canon (skill-reflex-detect.ps1)
    │
L Liberate ─► A3 Gwyn mesure D11 (heartbeat-tick.ps1)
    │
Karpathy retest ─► si val_score < target → amend → re-D Define
```

**D11 bandwidth metric = output Gwyn** : gain bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine). Upkeep > gain → route back to Zero/Rok-Tahk.

## Règle dure : éliminer avant automatiser

Verbatim canon : *"Éliminer first ; automation later — Rok-Tahk protège le système de l'automation du gaspillage."*

L'automation candidate n'est valide que si Rok-Tahk a éliminé ce qui pouvait l'être. Sans residual workflow nommé → pas d'automation.

## Position dans le triptyque

A2 Holo Janeway est le **Manager of Liberation (DEAL)** dans le triptyque BETH (Ikigai ⊃ Life Wheel ⊃ Muse de Libération). A1 Beth (Ikigai Centrée) conserve le **veto d'alignement**. A3 Data (PARA Archives) supervise **opérationnellement** Holo Janeway par le pattern DEAL ⊂ PARA ⊂ 12WY (plan §3.1 imbrication poupée russe).

## Loi d'héritage DEAL (plan §25.2)

- Un PRD DEAL ne peut pas contredire son ADR parent (`_SPECS/ADR/ADR-DEAL-001` ratifié cible fin Item 11 Q3 2026).
- Un DDD skill ne peut pas contredire son ADR parent.
- Le CODE doit implémenter le DDD, pas l'interpréter.

## Context7 Boundary

Toute claim d'API/plugin/MCP/CLI = `NEEDS_CONTEXT7`. Local blueprint writing ne nécessite pas Context7.

## Anti-patterns

- Provider/API/MCP/CLI claims sans `NEEDS_CONTEXT7` flag.
- Automation à risque haut sans Beth approval.
- Pas de source path → pas de proof.
- Upkeep > gain sans route-back vers Zero/Rok-Tahk.
- Destructive deletion sans A0 approval.

## Note sur une règle chiffrée attendue et non-trouvée

Le brief de cette escouade attendait une règle chiffrée du type *"3 occurrences pour automatiser, 5 occurrences pour rembourser"*. **Cette règle chiffrée n'apparaît dans aucun fichier de `26_DEAL_Protostar/`** dans la V2 lue. Seules traces du comptage : `dal.twin.md` mentionne *"Pattern detection and recurrence counting aboard USS Protostar"* — Dal compte les occurrences, mais aucun seuil chiffré 3/5 n'est posé. Voir `RAPPORT_life.md` § Contradictions.