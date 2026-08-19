---
type: Concept
title: Context Pack — contrat d'exécution Morty
description: Schéma obligatoire à 9 champs que toute exécution Morty doit valider avant de toucher un outil Shadow L1. Sans contrat complet → BLOCKED_CONTEXT_PACK_INCOMPLETE.
tags: [context-pack, morty, gate, contract, execution, schema]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: morty-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md
    title: A1 Morty Spec — Execution Gate
    last_modified: 2026-05-20
  - id: cerritos-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md
    title: A2 Cerritos Spec — Acceptance Criteria
    last_modified: 2026-05-20
  - id: snw-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
    title: A2 Curie SNW Spec — Acceptance Criteria
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Context Pack — contrat d'exécution Morty

Le Context Pack est le **contrat de handoff** qui rend toute opération Morty traçable, réversible, et auditable. Sans ses 9 champs, rien ne s'exécute.

## Les 9 champs canoniques

```yaml
required_context_pack_fields:
  - ship           # USS Orville | Discovery | SNW | Enterprise | Cerritos | Protostar
  - crew_member    # ex: Dal, Pike, Tilly, Book...
  - next_action    # phrase d'action, commence par un verbe
  - framework      # Ikigai | Life Wheel | 12WY | PARA | GTD | DEAL
  - domain_impact  # LD01-LD08 selon Life Wheel, ou pillar/horizon Ikigai
  - l0_skill_required  # nom du skill L0 mobilisé
  - beth_clearance # GREEN | ORANGE | RED | HALT_LD03 | HALT_LD04
  - evidence_paths # liste de chemins absolus lus
  - output_artifact # livrable observable
```

## Pourquoi cette forme

Trois propriétés :

1. **Auditabilité** — chaque exécution laisse un journal de ce qu'elle a lu, où elle a écrit, et qui a autorisé.
2. **Réversibilité** — `output_artifact` + `evidence_paths` permettent de revenir en arrière sans deviner.
3. **Anti-bypass** — `beth_clearance` est binaire : sans elle, rien ne passe. C'est la traduction exécutable du veto Beth.

## Format canon d'une exécution Morty

À chaque exécution, Morty écrit ou retourne :

- Commande ou workflow utilisé.
- Chemins sources exacts lus.
- Chemins sortie exacts modifiés.
- Risques résiduels.
- Si Context7 ou la doc officielle a été nécessaire pour configurer un outil externe.
- Prochaine étape réversible.

## Acceptance Criteria par ship (D1 receipts)

Chaque A2 ship publie ses propres critères d'acceptation — le Context Pack est le langage commun, mais chaque ship a ses invariants :

- **SNW** : "Every Rock has a Definition of Done. Every active tactic belongs to one active week. Every score claim maps to evidence."
- **Cerritos** : "Every actionable item has a verb and an owner. Every multi-step item is escalated to Project or Rock."
- **Protostar** : "Every automation candidate has a before/after workflow. Every high-risk automation has Beth approval. Every durable blueprint is routed to Enterprise."

## Anti-patterns

- "Just run it" sans `output_artifact` → Morty blocks.
- Write vers Baserow/Plane/Affine sans dry-run ou signoff → Morty blocks.
- Transformer un projet complexe en une seule tâche Plane → Morty blocks.
- Lancer L1 heartbeats avant que les systèmes observés soient prêts → Morty blocks.