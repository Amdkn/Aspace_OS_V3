---
name: adr-symph-003
type: ADR
namespace: SYMPH
status: RATIFIED
date: 2026-06-06
ratified_date: 2026-06-06
level: L0
canon_path: 10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-003_agent-os-standards-injection.md
extends: adr-symph-001
links:
  - entity_adr_symph_001
  - entity_adr_symph_002
  - entity_adr_heart_002
  - entity_symphony_router
  - entity_agent_os
  - concept_agent_os_best_practices
source: LLM_Wiki_A0
domain: L0 Tech_OS / Entity
tags: [#wiki #hygiene #backfill]
---

# ADR-SYMPH-003 — Agent OS = Standards Injection + Observability

Ratification du re-cadrage A0 (2026-06-06) : Agent OS = **couche d'interface** entre `~/agent-os/` (base doctrine) et les tick handlers Symphony (workers éphémères). Comprend le **protocole d'injection de standards par phase** (D2) et le **schema `pulse.log` 8 phases** (D3) qui rend les daemons Symphony observables.

## Points clés (5)
1. **D1** — Agent OS = couche d'injection de standards obligatoire entre base et tick handler
2. **D2** — Protocole : à chaque phase (PROBE/DECIDE/EXECUTE/OBSERVE/SIGNAL), le tick handler lit `index.yml` + injecte ≥ 1 standard dans le prompt agent
3. **D3** — `pulse.log` schema : 1 ligne JSONL par phase, 8 lignes par tick, UTC ISO-8601, append-only, rotation hebdo
4. **D4** — Contrat minimum du tick handler Symphony (7 obligations : lire index, sélectionner, injecter, écrire log, calculer coût, vérifier budget, émettre error)
5. **D5** — Validation par pilote sur `WORKFLOW.solaris-airtable-clients` 2026-06-06 (artefacts runnables : `symphony-tick-demo.{sh,ps1}` + 8 lignes pulse.log conformes)

## Format d'injection (D2)
Markdown brut, tronqué à 1 écran par standard, pas de JSON/YAML imbriqué. Ce que les agents LLM lisent nativement.

## Schéma pulse.log (D3)
```json
{
  "ts": "<ISO 8601 UTC ms>",
  "tick_id": "<workflow_id>-<UTC ts min>",
  "workflow_id": "<string>",
  "issue_id": "<string>|null",
  "phase": "WAKE|PROBE|DECIDE|EXECUTE|OBSERVE|LEARN|SIGNAL|SLEEP",
  "duration_ms": <int>,
  "standards_injected": ["<file.md>", ...],
  "decision": "<string>",
  "evidence_url": "<string>|null",
  "cost_delta_usd": <float>|null,
  "cumulative_cost_usd": <float>|null",
  "aspace_layer": "L0|L1|L2",
  "soc_target_domain": "<string>|null",
  "error": "<string>|null"
}
```

## Statut ratification
- **RATIFIÉ** 2026-06-06 (A0 explicite, après validation du pilote)
- Pilote 8/8 phases conformes, gate=PASS, $0.015 USD mock MiniMax 2.7
- Pas de période d'observation 1 semaine (décision A0 = ratifier maintenant)

## Backlinks
- [[entity_adr_symph_001]] — bus Symphony parent (N8N → Symphony)
- [[entity_adr_symph_002]] — matrice variants harness (CLI vs IDE, complémentaire)
- [[entity_adr_heart_002]] — instrumentation anti-panique
- [[entity_symphony_router]] — orchestrateur B1 qui consume Agent OS
- [[entity_agent_os]] — base doctrine `~/agent-os/`
- [[concept_agent_os_best_practices]] §11 — BP doctrine avec rôle Symphony

## Artefacts
- `00_Amadeus/05_OSS_Twin/symphony/agent-os/` — install Agent OS au niveau Symphony
- `agent-os/standards/<11 standards>.md` + `index.yml`
- `agent-os/standards/schema-pulse-log.md` — annexe technique du schema
- `scripts/symphony-tick-demo.{sh,ps1}` — tick handler runnable, validé 8/8 phases
- `agent-os/pulse.log` — 8 lignes du tick démo, audit trail

