---
type: Concept
title: Beth Thresholds — 5 états mutuellement exclusifs + seuils SDD-005
description: Machine à 5 états Beth (GREEN/ORANGE/RED/HALT_LD03/HALT_LD04) avec seuils canoniques LD03/LD04 minimaux et multi-domain alert.
tags: [beth, thresholds, halt, ld03, ld04, hard-safety, 5-states]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — Decision Rules
    last_modified: 2026-05-20
  - id: culber-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD03_Health_Culber/A3_Culber_LD03_Spec.md
    title: A3 Culber LD03 Spec — HARD SAFETY doctrine
    last_modified: 2026-05-20
  - id: tilly-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/A3_Tilly_LD04_Spec.md
    title: A3 Tilly LD04 Spec — HARD SAFETY doctrine
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Beth Thresholds — 5 états mutuellement exclusifs + seuils SDD-005

Beth retourne **un seul** de ces cinq états, mutuellement exclusifs. Chaque état déclenche une action différente dans le pipeline Morty.

## Table canon des 5 états

| État | Sens | Action Morty |
|---|---|---|
| `GREEN` | Preuve présente, santé OK, priorité cohérente | Exécuter selon Context Pack |
| `ORANGE` | Utile mais incomplet ou risqué | Dry-run seulement, demander la preuve manquante |
| `RED` | Violation santé / cognition / priorité | Stopper l'exécution |
| `HALT_LD03` | Contrainte santé/sommeil déclenchée | Stopper l'accélération L0/L2 |
| `HALT_LD04` | Surcharge cognitive déclenchée | Réduire le scope, ouvrir cleanup GTD/PARA |

## Seuils SDD-005 canon

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

Si LD03 < 4.0 → Beth doit retourner `HALT_LD03` ou escalader.
Si LD04 < 3.5 → Beth doit retourner `HALT_LD04` ou escalader.
Si ≥3 LD sont en alerte → multi_domain_alert déclenche revue A0.

## HARD SAFETY (cascade LD03 → LD04)

Verbatim canon `A3_Culber_LD03_Spec.md` :

> *"LD03 is primary gravity: when it degrades, LD04 cognition degrades in cascade."*

Verbatim canon `A3_Tilly_LD04_Spec.md` :

> *"Tilly = STOP authority si Culber LD03 RED. Cross-check obligatoire. PAS exécution sans recovery signal."*

C'est la seule doctrine où **un A3 peut overrider un autre A3** : Tilly STOP si Culber RED, sans passer par le pipeline classique.

## Ren's Law — règle Health négative nette

Du `a0_reasoning_map.md` (A0 Reasoning Map, A0 directif) :

> *"Règle de Beth (Veto) : Si ❤️ Santé/Énergie = Négatif → 🔴 STOP. Aucun score ne compense."*

C'est un **veto dur** : aucun score Ikigai, aucune faisabilité OS, aucune conformité E-Myth ne peut compenser une Santé LD03 négative.

## Beth Veto dans state.json

Chaque décision Beth écrit dans `00_Amadeus/40_SYMPHONY_BUS/state.json` :

```yaml
status: GREEN | ORANGE | RED | HALT_LD03 | HALT_LD04
agent_path: "A1:Beth > A2:<ship> > A3:<crew>"
evidence_paths: [...]
```

## Cycle heartbeat — pas d'empty heartbeat

Verbatim canon : *"Running L1 heartbeats before the watched systems are ready"* = Morty blocks. Cette règle bloque le création d'état parallel quand les systèmes observés ne sont pas encore actifs.

## Anti-paperclip Saru par Beth

Beth supervise Saru (LD02 Finance) via :

- Book (LD01) + Tilly (LD04 Cognition review hebdo) + Gwyn (DEAL D11 bandwidth) + Rick veto rare (1×/an max).