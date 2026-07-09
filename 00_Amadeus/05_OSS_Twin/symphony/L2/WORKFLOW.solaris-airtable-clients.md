---
workflow_id: solaris-airtable-clients
status: DRAFT_PRODUCTION_READY
created: 2026-06-02
layer: L2 Shadow Business
project: Solaris
source_tool: Airtable
target_runtime: Hermes
evidence:
  context7:
    - /websites/airtable_developers_web_api
  local_source_fallback:
    - C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\symphony-base.spec.md
    - C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L2\symphony-airtable.spec.md
    - C:\Users\amado\hermes-workspace\swarm.yaml
---

# WORKFLOW — Solaris Airtable Clients To Hermes

## 1. Role

Ce workflow fait d'Airtable la surface client pour Solaris.

Airtable porte le pipeline, les clients, les audits, les briefs, les livrables et les signaux business. Hermes ne doit pas traiter un record client comme une simple tache : il doit en extraire une mission avec gate, preuve attendue et responsabilite B2/B3.

## 2. Boundary

| Zone | Role |
|---|---|
| Symphony | Lit Airtable, normalise le record, refuse les records sans domaine/gate, emet une mission Hermes. |
| Airtable | Source de verite client, pipeline, finance et livrables. |
| Hermes | Analyse, produit la preuve, prepare un draft de retour et une recommandation de gate. |
| ClickUp | Execution task liee quand une action operationnelle doit etre suivie. |
| Notion | SOP/canon lie, active uniquement quand la preuve stabilise la procedure. |

## 3. Domains

| SOA Domain | B2 Owner | B3 Executor | Hermes route |
|---|---|---|---|
| Growth | Superman | Guardians | orchestrator -> researcher -> strategist |
| Sales | JohnJones | Illuminati | orchestrator -> strategist |
| Finance | WonderWoman | Thunderbolts | orchestrator -> reviewer |

Les domaines Ops, Product, IT, People et Legal peuvent etre references, mais les actions executables doivent etre transformees en tache ClickUp liee.

## 4. Candidate Record Rule

Un record Airtable devient candidat Hermes uniquement si :

| Champ | Exigence |
|---|---|
| Status | `New Lead`, `Qualified`, `Proposal Sent` ou `In Production` |
| SOA Domain | `Growth`, `Sales` ou `Finance` |
| Name/Title | Non vide |
| Description/Brief | Non vide ou SOP liee |
| Build Gate | Non vide |
| Context Pack URL ou Notion SOP URL | Au moins un lien exploitable |
| SLA Max Time | Present, en minutes |
| SLA Max Cost | Present ou explicitement `0` |
| SLA Max Retries | Present |

Si le record demande une livraison terrain, technique ou process, Symphony doit recommander une tache ClickUp au lieu d'envoyer directement l'execution longue depuis Airtable.

## 5. Required Airtable Fields

| Field | Type attendu | Usage |
|---|---|---|
| SOA Domain | Single select | Routage B2/B3 |
| Owner B2 | Single select | Superman, JohnJones, WonderWoman |
| Executor B3 | Single select | Guardians, Illuminati, Thunderbolts |
| Build Gate | Long text | Definition de PASS/BLOCKED |
| Context Pack URL | URL | Pack de contexte executable |
| ClickUp Task URL | URL | Tache operationnelle liee |
| Notion SOP URL | URL | Procedure canonique associee |
| Forbidden Words | Long text | Lexique interdit separe par virgules |
| SLA Max Time | Number | Budget temps en minutes |
| SLA Max Cost | Currency/Number | Budget compute |
| SLA Max Retries | Number | Tentatives max |
| Proof URL | URL | Lien vers preuve produite |
| Gate Status | Single select | `CONDITIONAL`, `PASS`, `BLOCKED` |

## 6. Hermes Mission Payload

```yaml
mission_contract_version: "1.0"
source_tool: airtable
source_id: "{{airtable.record.id}}"
source_url: "{{airtable.record.url}}"
project: Solaris
mission_type: client_pipeline_execution
soa_domain: "{{fields.SOA Domain}}"
owner_b2: "{{fields.Owner B2}}"
executor_b3: "{{fields.Executor B3}}"
title: "{{fields.Name}}"
description: "{{fields.Description}}"
build_gate: "{{fields.Build Gate}}"
context_pack_url: "{{fields.Context Pack URL}}"
clickup_task_url: "{{fields.ClickUp Task URL}}"
notion_sop_url: "{{fields.Notion SOP URL}}"
forbidden_words: "{{fields.Forbidden Words}}"
sla:
  max_minutes: "{{fields.SLA Max Time}}"
  max_cost_usd: "{{fields.SLA Max Cost}}"
  max_retries: "{{fields.SLA Max Retries}}"
expected_proof:
  - client_or_pipeline_summary
  - recommendation_or_deliverable
  - risk_and_blocker_notes
  - gate_decision
greenlight_required: true
writeback_policy:
  external_write_requires_greenlight: true
  allowed_draft_outputs:
    - airtable_update_draft
    - clickup_task_draft
    - proof_summary
    - status_recommendation
```

## 7. Hermes Routing

| Condition | Primary worker | Support workers |
|---|---|---|
| SOA Domain = Growth | orchestrator | researcher, strategist |
| SOA Domain = Sales | orchestrator | strategist, reviewer |
| SOA Domain = Finance | orchestrator | reviewer |
| Brief incomplete | orchestrator | strategist |
| SOP/canon needed | km-agent | strategist |
| External writeback requested | orchestrator | reviewer |

## 8. Gate Decision

Hermes must return one of three decisions :

| Decision | Meaning |
|---|---|
| PASS | Business gate satisfied, proof exists, no forbidden output. |
| BLOCKED | Missing client input, access, legal/finance decision, or external approval. |
| CONDITIONAL | Partial proof exists, but the client/pipeline state is not ready to advance. |

## 9. First Production Use

Premier usage recommande :

1. Selectionner un record Solaris `Qualified` ou `Proposal Sent`.
2. Normaliser le record en payload Hermes.
3. Produire une preuve business : qualification, proposal draft, pricing note, ou blocker.
4. Si une action operationnelle est necessaire, creer un draft de tache ClickUp liee.
5. Ne jamais faire de bi-sync automatique tant que les gates ne sont pas prouvees.
