---
type: Concept
title: SDD-V0.9 Agent Portal Nexus — la vague post-V3
description: SDD-V0.9_AgentPortal_Nexus.md, seul dans TOTAL_Spec/SDD/, qui introduit le portail agent Nexus comme couche d'orchestration des agents A0-A3 dans une fenêtre Vercel après le versement V3 du 2026-08-02.
tags: [sdd, v0.9, agent-portal, nexus, post-v3, 2026-08-02, orchestration, vercel]
generated: { by: minimax-m3, at: 2026-08-19T15:00:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:00:00Z }
sources:
  - id: sdd-v09-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/SDD/SDD-V0.9_AgentPortal_Nexus.md"
    title: SDD-V0.9_AgentPortal_Nexus.md (lu directement)
    last_modified: 2026-08-02
  - id: sdd-w33-w42
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SDD/SDD-W33-W42_fable_aspace_wargames_2026-07-13.md"
    title: SDD-W33-W42 (10 wargames Fable canon)
    last_modified: 2026-07-13
okf_version: "0.2"
---

# SDD-V0.9 Agent Portal Nexus — la vague post-V3

## Le constat d'isolement

`SDD-V0.9_AgentPortal_Nexus.md` est **le seul** document V0.9 dans
l'archive Legacy. Il vit dans `TOTAL_Spec/SDD/` (pas `_SPECS/`), et
**n'a pas de pendant V0.9.x ou V0.10** — la chaîne s'arrête à V0.8-Phase2
sauf pour ce document isolé.

La date `last_modified: 2026-08-02` le range **le jour même** du
versement V3 (2026-08-02). C'est l'unique doc Legacy modifié
pendant la bascule.

## Verdict

`synthese-datee` — l'**intention** (un portail agent Nexus) est portée
par d'autres documents plus récents (notamment SDD-W33-W42 wargames,
voir [[concept-sdd-w33-w42-fable-wargames]]), mais le **détail
d'implémentation** n'est plus la référence.

## Pourquoi pas canon

Trois raisons :

1. **Pas de ratification explicite dans le frontmatter** : le
   document ne porte pas de statut « Approuvé » ou « Ratifié » au sens
   des V0.2 → V0.8.
2. **Date ambiguë** : `last_modified: 2026-08-02` pourrait être une
   modification mineure, pas une re-ratification.
3. **Successeur immédiat** : les wargames SDD-W33-W42 (10 fiches
   canon) couvrent l'intégration Multica ↔ Agent Portal en mieux
   (multica-chat-agent-portal, multica-runtimes-recovery,
   aspace-meta-os-dashboard).

## Source du décompte

`find .../Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/SDD/` →
13 fichiers (les 12 V0.x + SDD-V0.9). Seul `SDD-V0.9` n'a pas de
miroir `_SPECS/SDD/` équivalent.

## Concepts liés

- [[concept-sdd-chain-v0x-legacy]] — la chaîne parente (V0.x).
- [[concept-sdd-w33-w42-fable-wargames]] — le successeur canon.
