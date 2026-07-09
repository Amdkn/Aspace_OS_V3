---
id: B3_GUARDIANS_SWARM_CONFIG
layer: B3_SWARM_EXECUTION
surface: Jerry Area J01 LD01 Business
domain: Growth
b2_owner: Superman
b3_swarm: Guardians
mode: Brand/Story-first growth
status: SHADOW_ACTIVE
updated: 2026-05-29
---

# Guardians Swarm Config

Configuration opérationnelle du swarm B3 Guardians, exécutant Growth sous supervision Superman (B2).

## Mission

Exécuter les expériences Growth (cycle Fail Fast, cf. Principe P6) qui font progresser la North Star Metric (P4), dans les limites de la DoD fixée par Superman, sans babysitting.

## Doctrine de référence (immutable inputs)

- **Principes** : `../03_SUPERMAN_GROWTH_PRINCIPLES.md` (18 principes + T-Shaped)
- **Contrat d'autonomie** : `../02_B3_SWARM_SUPERVISION_PROTOCOL.md`
- **Pipeline** : `../01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`
- **Backlog réel** : `../04_SUPERMAN_EXTRACTION_QUEUE.md`

## Rock actif

```yaml
rock_id: J01-B2-GROWTH-2026-01
status: active_shadow
north_star_metric: "ICP-qualified AaaS opportunities generated from non-paid channels"
rock_statement: "Validate the first non-paid Growth loop for the AaaS flagship offer by producing an ICP filter, painkiller message, instrumented experiment plan, and conversion proof path."
definition_of_done:
  - "ICP filter exists and rejects bad-fit leads explicitly."
  - "Painkiller message has 3 testable variants tied to P8/P13/P16."
  - "Non-paid channel experiment has a RICE score and measurable lead/lag indicators."
  - "Proof log has one completed or blocked entry with evidence, not opinion."
  - "No external system is mutated without explicit A0 approval and credential-safe execution."
```

## Mode opératoire

| Paramètre | Valeur |
|-----------|--------|
| Mode growth | Brand/Story-first (Guardians) — bascule data-first (Nexus) sur décision Jerry |
| Cadence revue | Hebdo Lead/Lag + per-milestone sur Rock actif |
| Priorisation | RICE obligatoire (P5) — pas de test sans score |
| Méthode | Idéer → Prioriser → Tester (MVP) → Analyser (P6) |
| Preuve | Chaque expérience loggée dans `03_SHARED_CONTEXT_AND_PROOF_LOG.md` |
| Escalation | Guardian → Superman → Jerry Prime → B1 Rick/Morty |
| Safety exit | Boucle/fabrication de preuve → Donna/DLQ |

## Frontières (forbidden)

Les Guardians NE PEUVENT PAS : changer le Rock ou la DoD, contourner les gates cross-domaines, committer des secrets, ou marquer leur travail "Business Done" sans revue Superman.

## Mesh L2 (surfaces opérationnelles)

- **ClickUp S2-1 Acquisition (Guardians)** : 8 lists = backlog d'exécution + expériences RICE
- **Airtable** : 🦸 Leads (qualification P9), 🛡️ Finance (LTV/CAC P3, Pareto P11), 🌞 Clients
- **Notion MASTER_SOP_DB** : SOPs Growth (encode les principes en procédures)
- **Supabase tenant_aspace_solaris.sops** : miroir queryable

> Ces surfaces sont des destinations d'orchestration. En Shadow mode, les Guardians produisent d'abord les artefacts locaux et les preuves; les mutations Notion/ClickUp/Airtable/Supabase attendent une action explicite et credential-safe.

*B3 swarm under Superman (B2). Last sync: 2026-05-29*
