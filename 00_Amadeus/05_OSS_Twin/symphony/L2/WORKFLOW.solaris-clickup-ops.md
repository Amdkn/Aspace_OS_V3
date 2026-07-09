---
workflow_id: solaris-clickup-ops
status: DRAFT_PRODUCTION_READY
created: 2026-06-02
layer: L2 Shadow Business
project: Solaris
source_tool: ClickUp
target_runtime: Hermes
evidence:
  context7:
    - /llmstxt/developer_clickup_llms_txt
  local_source_fallback:
    - C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\symphony-base.spec.md
    - C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L2\symphony-clickup.spec.md
    - C:\Users\amado\hermes-workspace\swarm.yaml
---

# WORKFLOW — Solaris ClickUp Ops To Hermes

## 1. Role

Ce workflow fait de ClickUp la surface d'execution pour Solaris quand une action doit devenir une mission Hermes.

ClickUp ne porte pas la memoire canonique et ne porte pas les clients. ClickUp porte les gates, les statuts, les blocages, les preuves et la responsabilite d'execution.

## 2. Boundary

| Zone | Role |
|---|---|
| Symphony | Lit ClickUp, normalise la tache, refuse les tickets incomplets, emet une mission Hermes. |
| ClickUp | Source de verite operationnelle pour Ops, Product et IT. |
| Hermes | Execute, verifie, gate, produit la preuve, puis prepare le retour de statut. |
| Airtable | Reference client/pipeline liee, jamais bi-sync automatique au depart. |
| Notion | SOP/canon lie, lecture et capture post-preuve seulement. |

## 3. Domains

| SOA Domain | B2 Owner | B3 Executor | Hermes route |
|---|---|---|---|
| Ops | Batman | Fantastic4 | orchestrator -> ops-watch |
| Product | Flash | Avengers | orchestrator -> builder -> qa -> reviewer |
| IT | Cyborg | KangDynasty | orchestrator -> builder -> qa -> reviewer |

Les domaines Growth, Sales, Finance, People et Legal peuvent etre references, mais ne doivent pas etre routes par ce workflow sauf exception approuvee par l'orchestrator.

## 4. Candidate Task Rule

Une tache ClickUp devient candidate Hermes uniquement si elle respecte tous les criteres suivants :

| Champ | Exigence |
|---|---|
| Status | `to do`, `in progress`, `review` ou `staging` |
| Description | Non vide |
| Build Gate | Non vide |
| SOA Domain | `Ops`, `Product` ou `IT` |
| Context Pack URL ou Notion SOP URL | Au moins un lien exploitable |
| SLA Max Time | Present, en minutes |
| SLA Max Cost | Present ou explicitement `0` |
| SLA Max Retries | Present |

Tout ticket incomplet reste dans ClickUp et doit recevoir un commentaire de blocage au lieu d'etre delegue.

## 5. Required ClickUp Fields

| Field | Type attendu | Usage |
|---|---|---|
| SOA Domain | Dropdown | Routage B2/B3 |
| Owner B2 | Dropdown | Batman, Flash, Cyborg |
| Executor B3 | Dropdown | Fantastic4, Avengers, KangDynasty |
| Build Gate | Text | Definition de PASS/BLOCKED |
| Context Pack URL | URL | Pack de contexte executable |
| Airtable Record URL | URL | Client/deal associe |
| Notion SOP URL | URL | Procedure canonique associee |
| Forbidden Words | Text | Lexique interdit separe par virgules |
| SLA Max Time | Number | Budget temps en minutes |
| SLA Max Cost | Currency/Number | Budget compute |
| SLA Max Retries | Number | Tentatives max |
| Proof URL | URL | Lien vers preuve produite |
| Gate Status | Dropdown | `CONDITIONAL`, `PASS`, `BLOCKED` |

## 6. Hermes Mission Payload

```yaml
mission_contract_version: "1.0"
source_tool: clickup
source_id: "{{clickup.task.id}}"
source_url: "{{clickup.task.url}}"
project: Solaris
mission_type: operations_execution
soa_domain: "{{custom_fields.SOA Domain}}"
owner_b2: "{{custom_fields.Owner B2}}"
executor_b3: "{{custom_fields.Executor B3}}"
title: "{{clickup.task.name}}"
description: "{{clickup.task.description}}"
build_gate: "{{custom_fields.Build Gate}}"
context_pack_url: "{{custom_fields.Context Pack URL}}"
airtable_record_url: "{{custom_fields.Airtable Record URL}}"
notion_sop_url: "{{custom_fields.Notion SOP URL}}"
forbidden_words: "{{custom_fields.Forbidden Words}}"
sla:
  max_minutes: "{{custom_fields.SLA Max Time}}"
  max_cost_usd: "{{custom_fields.SLA Max Cost}}"
  max_retries: "{{custom_fields.SLA Max Retries}}"
expected_proof:
  - concise_execution_summary
  - files_or_artifacts_changed
  - verification_result
  - gate_decision
greenlight_required: true
writeback_policy:
  external_write_requires_greenlight: true
  allowed_draft_outputs:
    - clickup_comment_draft
    - proof_summary
    - status_recommendation
```

## 7. Hermes Routing

| Condition | Primary worker | Support workers |
|---|---|---|
| SOA Domain = Ops | orchestrator | ops-watch, reviewer |
| SOA Domain = Product | orchestrator | builder, qa, reviewer |
| SOA Domain = IT | orchestrator | builder, qa, reviewer |
| Build Gate unclear | orchestrator | strategist |
| Context missing | orchestrator | km-agent |
| Verification needed | qa | reviewer |
| External writeback requested | orchestrator | reviewer |

## 8. Gate Decision

Hermes must return one of three decisions :

| Decision | Meaning |
|---|---|
| PASS | Build Gate satisfied, proof exists, no forbidden output. |
| BLOCKED | Execution cannot continue without missing input, access, decision, or external approval. |
| CONDITIONAL | Partial proof exists, but gate is not strong enough to close. |

## 9. First Production Use

Premier usage recommande :

1. Selectionner une tache Solaris Ops/Product/IT avec Build Gate clair.
2. Normaliser la tache en payload Hermes.
3. Laisser Hermes produire la preuve localement.
4. Ne preparer qu'un commentaire ClickUp draft tant que le greenlight n'est pas donne.
5. Marquer la gate `PASS`, `BLOCKED` ou `CONDITIONAL` seulement apres preuve.
