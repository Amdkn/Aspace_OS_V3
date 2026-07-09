# Symphony for A'Space OS — Base Specification (Generalized)

> **Statut** : Shadow A0 — pré-configuration, non canonique
> **Date** : 2026-05-13
> **Référence amont** : `printingpress.dev/spec` (Symphony Service Specification, Draft v1)
> **Couverture** : Spec agnostique du tracker — chaque adapter (Plane, Baserow, Airtable, etc.) hérite de ce document.

## 0. Différence avec la spec Symphony originale

Symphony OSS est conçu pour **Linear**. Cette adaptation A'Space :
1. **Abstrait le tracker** — Linear devient un cas particulier parmi 7
2. **Intègre la trinité SLA/SOA/SOC** — chaque payload porte ses contraintes mathématiques (SDD-009 à venir)
3. **Map les états Symphony aux états A'Space** — `Todo/In Progress/Done` devient un mapping configurable
4. **Documente le coût Compute** — MiniMax 2.7 / GLM 4.7 Flash comme cibles, pas Anthropic premium
5. **Connecte à Donna DLQ** — un run failed après N retries déborde vers Donna (ADR-RICK-001)
6. **Hook CLI Clara** — les Skills MCP sont convertis en CLI via `printingpress.dev` + CLI Anything pour la commodité B2/B3

---

## 1. Problème adressé

Symphony A'Space est un **daemon long-running** qui :
- Lit des tâches dans un tracker (Plane / Baserow / Airtable / ClickUp / Notion / Affine / Obsidian)
- Crée un workspace isolé par tâche
- Lance un coding agent (Claude Code ou OpenHarness avec MiniMax/GLM) dans ce workspace
- Suit le payload SOC (Service-Oriented Communication) avec ses contraintes SLA/SOA

**Boundary critique** : Symphony est un **scheduler + tracker reader**. Les writes (state transitions, comments) sont faits par l'agent via tooling — pas par Symphony.

## 2. Goals & Non-Goals

### Goals
- Polling cadence + dispatch concurrence bornée
- Workspace par-issue déterministe + reuse
- Stop des runs si state change rend l'issue ineligible
- Backoff exponentiel sur transient failures
- WORKFLOW.md repo-owned (versioned avec le code)
- Observability : structured logs minimum
- Restart recovery sans DB (state-driven)

### Non-Goals
- Pas d'UI web (Symphony reste headless)
- Pas de workflow engine généraliste
- Pas de business logic dans Symphony (la logique vit dans le prompt WORKFLOW.md + tooling agent)
- **Pas de remplacement de l'humain** — l'humain valide aux Build Gates ClickUp (cf. SLA Qualitatif)

## 3. Architecture A'Space

### 3.1 Composants

```
┌─────────────────────────────────────────────────────────────┐
│  Shadow A0 (cwd, lance le service)                          │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  Symphony Daemon                                            │
│  ├─ Workflow Loader   (WORKFLOW.md + YAML front matter)     │
│  ├─ Config Layer      (typed getters + env resolution)      │
│  ├─ Tracker Adapter   ← ADAPTER par tool (cf. L1/L2/L0)     │
│  ├─ Orchestrator      (poll loop, dispatch, retry)          │
│  ├─ Workspace Manager (filesystem lifecycle)                │
│  ├─ Agent Runner      (coding agent subprocess + protocol)  │
│  ├─ SOC Validator     ← spécifique A'Space (Zod-like)       │
│  ├─ Donna DLQ Hook    ← spécifique A'Space                  │
│  └─ Status Surface    (logs structurés)                     │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  Tracker (1 parmi 7)                                        │
│  Plane | Baserow | Obsidian | Affine | Airtable | ClickUp  │
│  | Notion                                                   │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Couches d'abstraction

1. **Policy Layer** — `WORKFLOW.md` (prompt + rules, repo-owned)
2. **Configuration Layer** — typed getters, env tokens, paths
3. **Coordination Layer** — orchestrator (polling, eligibility, concurrency, retries)
4. **Execution Layer** — workspace + agent subprocess
5. **Integration Layer** — **un adapter par tracker** (cf. `L1/symphony-<tool>.spec.md`)
6. **Observability Layer** — structured logs + optional status surface

### 3.3 Dépendances externes

- API du tracker cible (variable selon adapter)
- Local filesystem (workspaces + logs)
- Coding agent executable (Claude Code, OpenHarness `oh`, ou compatible JSON-RPC app-server)
- LLM provider :
  - **MiniMax 2.7** (recommandé — $20/4500 turns par 5h, API Anthropic-compatible)
  - **GLM 4.7 Flash** via OpenRouter (fallback ultra-frugal)
  - Claude Sonnet (premium, garder pour Rick A1 critique)

---

## 4. Domain Model

### 4.1 Entités abstraites

#### Issue (normalisé, agnostic du tracker)

```yaml
id: string                # ID interne tracker
identifier: string        # Clé humaine (ex: "PLN-42", "AT-rec123")
title: string
description: string|null
priority: integer|null    # 1 = highest, 4 = lowest, null = unranked
state: string             # État actuel (normalisé lowercase pour comparaison)
branch_name: string|null  # Suggestion de branche Git si dispo
url: string|null          # URL vers le tracker
labels: list[string]      # lowercased
blocked_by: list[BlockerRef]
created_at: timestamp|null
updated_at: timestamp|null

# Champs A'Space spécifiques
soc_metadata:             # Service-Oriented Communication (Payload metadata)
  target_soa_domain: string|null   # "Growth", "Sales", "Product", etc.
  forbidden_lexicon: list[string]
  context_pack_url: string|null    # urn:aspace:rag:<id>
sla_constraints:          # Service Level Agreement (contraintes math)
  max_execution_time_minutes: integer|null
  max_compute_budget_usd: float|null
  max_retry_loops: integer|null
```

#### Workflow Definition

```yaml
config:                   # YAML front matter
  tracker: {kind, endpoint, api_key, project_slug, active_states, terminal_states}
  polling: {interval_ms}
  workspace: {root}
  hooks: {after_create, before_run, after_run, before_remove, timeout_ms}
  agent: {max_concurrent_agents, max_turns, max_retry_backoff_ms, max_concurrent_agents_by_state}
  codex: {command, approval_policy, thread_sandbox, turn_sandbox_policy, turn_timeout_ms, ...}
  # A'Space-specific
  soc: {schema_version, default_domain}
  donna_dlq: {enabled, threshold_failed_attempts}
  clara_cli: {convert_mcp_to_cli, printingpress_endpoint}

prompt_template:          # Markdown body
```

#### Service Config (typed)

Dérivé du WorkflowDefinition.config + env resolution. Tous les fields ont des defaults.

#### Workspace

```yaml
path: absolute_path
workspace_key: sanitized_identifier  # [A-Za-z0-9._-]+ uniquement
created_now: boolean                  # gating pour after_create hook
```

#### Run Attempt, Live Session, Retry Entry, Orchestrator Runtime State
→ Identiques à la spec Symphony OSS originale (cf. §4.1.5-4.1.8 du spec amont).

### 4.2 Règles de normalisation

- `Workspace Key` : remplacer `[^A-Za-z0-9._-]` par `_`
- `Normalized State` : lowercase pour comparaison
- `Session ID` : `<thread_id>-<turn_id>`

---

## 5. WORKFLOW.md Contract (étendu A'Space)

### 5.1 Découverte

Précédence :
1. CLI startup path explicite
2. Default : `WORKFLOW.md` dans CWD

### 5.2 Format

YAML front matter + Markdown body. Self-contained.

### 5.3 Front Matter Schema A'Space

Top-level keys :
- `tracker` — *(de Symphony OSS, étendu)*
- `polling`
- `workspace`
- `hooks`
- `agent`
- `codex`
- **`soc`** *(A'Space — Service-Oriented Communication)*
- **`donna_dlq`** *(A'Space — escalation)*
- **`clara_cli`** *(A'Space — MCP→CLI conversion)*

#### 5.3.1 `tracker` (extension A'Space)

```yaml
tracker:
  kind: linear | plane | baserow | obsidian | affine | airtable | clickup | notion
  endpoint: <api_url>
  api_key: $ENV_VAR_NAME
  project_slug: <project_id>          # ou équivalent par tracker
  active_states: [list]
  terminal_states: [list]
  state_mapping:                       # A'Space — map tracker states → Symphony states
    inbox: "Backlog"                   # Capture (Mariner)
    next_actions: "Todo"               # Clarify (Boimler) done
    in_progress: "In Progress"
    waiting_for: "Waiting"
    done: "Done"
    cancelled: "Cancelled"
```

#### 5.3.2 `soc` (A'Space)

```yaml
soc:
  schema_version: "1.0"
  default_domain: "Product_Forge"      # SOA target par défaut
  zod_validation: true                  # validation Zod-like avant dispatch
  forbidden_lexicon_global: ["synergie", "disrupter", "innover"]
```

#### 5.3.3 `donna_dlq` (A'Space)

```yaml
donna_dlq:
  enabled: true
  threshold_failed_attempts: 3          # après N échecs → escalade Donna
  donna_endpoint: "http://localhost:3101/donna/escalate"
  notification_channel: "telegram"      # OpenHarness Channels v0.2+
```

#### 5.3.4 `clara_cli` (A'Space — frugality)

```yaml
clara_cli:
  convert_mcp_to_cli: true
  printingpress_endpoint: "https://printingpress.dev/api"
  cli_anything_path: "/usr/local/bin/cli-anything"
  preferred_runtime: "cli"              # cli | mcp (cli moins coûteux)
```

### 5.4 Prompt Template

Liquid-compatible. Variables :
- `issue` (tous les fields normalisés + soc_metadata + sla_constraints)
- `attempt` (null pour 1ère, int pour retry/continuation)
- `tracker_kind` (pour conditionner le prompt par tracker)
- `aspace_layer` (`L0`, `L1`, `L2` — pour adapter le ton selon la couche)

Fallback : si prompt vide, default `"You are an A'Space A3 Companion. Issue: {{issue.title}}"`.

---

## 6. Configuration (résumé)

Précédence : CLI > YAML > Env (`$VAR`) > defaults.

Reload dynamique requis sur tous les champs sauf `server.port` (extension HTTP).

Dispatch preflight : valider tracker.kind + api_key + project_slug + codex.command à chaque tick.

---

## 7. Orchestration State Machine

### 7.1 États internes (claim)

- `Unclaimed` → pas en cours, pas de retry
- `Claimed` → réservé (Running ou RetryQueued)
- `Running` → worker existe
- `RetryQueued` → timer retry actif
- `Released` → claim libéré (terminal, non-active, missing, retry done)

### 7.2 Lifecycle d'un Run Attempt

1. `PreparingWorkspace`
2. `BuildingPrompt`
3. `LaunchingAgentProcess`
4. `InitializingSession`
5. `StreamingTurn`
6. `Finishing`
7. Terminal : `Succeeded` / `Failed` / `TimedOut` / `Stalled` / `CanceledByReconciliation`

### 7.3 Retry & Backoff

- Continuation après succès : 1000 ms fixe
- Failure-driven : `delay = min(10000 * 2^(attempt-1), max_retry_backoff_ms)` (default cap 5 min)
- **A'Space addition** : après `donna_dlq.threshold_failed_attempts`, escalade Donna et release claim

### 7.4 Réconciliation

À chaque tick :
1. Stall detection (elapsed > `codex.stall_timeout_ms` → kill + retry)
2. Tracker state refresh (terminal → kill+clean, active → update snapshot, ni l'un ni l'autre → kill sans clean)

---

## 8. Workspace Management

### 8.1 Layout

```
<workspace.root>/<sanitized_issue_identifier>/
```

Reuse entre runs. Pas d'auto-delete sur succès.

### 8.2 Hooks A'Space

En plus des hooks Symphony OSS :
- **`before_dispatch`** *(nouveau)* : exécute *avant* la création workspace, pour valider le payload SOC. Échec = release claim.
- **`after_soc_validation`** *(nouveau)* : exécute après validation Zod du payload, avant `after_create`.

### 8.3 Safety Invariants (inchangé)

- `cwd == workspace_path` avant launch agent
- `workspace_path` inclus dans `workspace_root` (préfixe)
- Workspace key sanitized `[A-Za-z0-9._-]`

---

## 9. Agent Runner Protocol

### 9.1 Launch

```bash
bash -lc "<codex.command>"
```

Default `codex app-server`. Compatibles A'Space :
- `claude --print --output-format=stream-json`
- `oh -p --output-format=stream-json` (OpenHarness)
- Tout binaire JSON-RPC-like sur stdio

### 9.2 Handshake

`initialize` → `initialized` → `thread/start` → `turn/start`. Cf. spec amont §10.2.

### 9.3 A'Space extension — `aspace_tools` advertised

Outils client-side avancés exposés à l'agent :
- `aspace_donna_escalate` — émet une alerte Donna (override threshold)
- `aspace_soc_emit` — émet un payload SOC vers un autre domaine SOA
- `aspace_clara_cli` — invoque un CLI Clara (équivalent MCP transformé)
- `<tracker>_graphql` ou `<tracker>_rest` — équivalent du `linear_graphql` mais par adapter

### 9.4 Coût Compute (A'Space spécifique)

Tracking obligatoire :
- `cumulative_input_tokens` × prix provider
- `cumulative_output_tokens` × prix provider
- **Budget check à chaque turn** : si `cumulative_cost_usd > sla_constraints.max_compute_budget_usd` → kill + fail

Tarifs de référence (2026-05) :
| Provider | Input/1M | Output/1M | A'Space rating |
|---|---|---|---|
| Claude Sonnet 4.5 | $3.00 | $15.00 | Réservé Rick A1 critique |
| MiniMax 2.7 | $0.30 | $1.20 | **Default A3 Compagnons** |
| GLM 4.7 Flash (OR) | $0.05 | $0.20 | **Fallback ultra-frugal** |
| GPT-4o | $2.50 | $10.00 | Évité (coût + dépendance) |

---

## 10. Tracker Integration Contract (généralisé)

Chaque adapter doit implémenter :

1. **`fetch_candidate_issues()`** — issues dans `active_states` du `project_slug`
2. **`fetch_issues_by_states(state_names)`** — pour startup cleanup
3. **`fetch_issue_states_by_ids(issue_ids)`** — pour réconciliation

### 10.1 Normalisation

Sortie obligatoire conforme au modèle §4.1.1 (Issue normalisé). Tous les champs `soc_metadata` et `sla_constraints` doivent être extraits si présents dans le tracker (selon convention de l'adapter).

### 10.2 Erreurs

Catégories A'Space :
- `unsupported_tracker_kind`
- `missing_tracker_api_key`
- `missing_tracker_project_slug`
- `tracker_api_request` (transport)
- `tracker_api_status` (HTTP non-2xx)
- `tracker_payload_errors` (validation)
- `tracker_unknown_payload`
- `tracker_pagination_error`

### 10.3 Writes (boundary inchangé)

Symphony **ne fait pas de writes**. C'est l'agent (Claude Code / OpenHarness) qui écrit dans le tracker via tooling.

---

## 11. Hook Donna DLQ (A'Space)

Après `donna_dlq.threshold_failed_attempts` retries sur la même issue :

```python
POST {donna_dlq.donna_endpoint}
{
  "issue_id": "<id>",
  "identifier": "<identifier>",
  "tracker_kind": "<kind>",
  "failed_attempts": <N>,
  "last_error": "<error>",
  "sla_constraints": {...},
  "escalate_to": "rick_a1" | "amadeus_a0"
}
```

Donna décide :
- Soit notifie Telegram (OpenHarness Channels v0.2+)
- Soit reset le compteur et donne une 4ème chance avec un autre LLM
- Soit marque l'issue comme `blocked_by_dlq` et release definitivement

---

## 12. Logging & Observability

### 12.1 Required fields par log

- `issue_id`, `issue_identifier`
- `tracker_kind`
- `session_id` (si en cours d'exécution agent)
- `cumulative_cost_usd` (A'Space)
- `aspace_layer` (`L0`, `L1`, `L2`)
- `soc_target_domain` si applicable

### 12.2 Sinks

- Stderr (toujours)
- `/var/log/aspace/symphony.log` rotatif (cf. SDD-001 §6.3)
- Optionnel : Telegram channel `@aspace_symphony_alerts` pour `error` et `dlq_escalation`

### 12.3 Runtime Snapshot

GET `http://localhost:<server.port>/snapshot` retourne :
- `running` (avec `turn_count`, `cumulative_cost_usd`)
- `retrying`
- `donna_escalations_pending`
- `codex_totals` + `aspace_cost_totals`
- `rate_limits` provider

---

## 13. Migration depuis n8n

Pour les utilisateurs venant de n8n :

| n8n concept | Symphony A'Space équivalent |
|---|---|
| Workflow JSON | `WORKFLOW.md` (Markdown + YAML) |
| Webhook trigger | Tracker polling (interval_ms) |
| HTTP Request node | Agent tooling (Claude Code MCP/CLI) |
| Switch/IF node | Prompt logic dans WORKFLOW.md |
| Error trigger | Donna DLQ hook |
| Cron node | `polling.interval_ms` |
| Code node | `before_run` hook |
| Self-host pénible | `oh autopilot` + Symphony daemon = systemd unit |

---

## 14. Sécurité

### 14.1 Secrets

Jamais en clair dans WORKFLOW.md. Toujours `$ENV_VAR_NAME`.

### 14.2 Sandbox

`codex.thread_sandbox` et `codex.turn_sandbox_policy` : utilisé selon le tracker.
- L0 (Yaz/Ryan/Graham) : `workspace_write` autorisé
- L1 (Beth ships) : `workspace_write` autorisé
- L2 (DC managers) : `read_only` par défaut, écriture sur approbation Build Gate

### 14.3 Network

Tailscale Private Access pour les endpoints internes (`donna_endpoint`, `clara_cli`).

---

## 15. Validation MVP — Critères d'usage

Un adapter Symphony est validé pour graduation MUSE (cf. SDD-008 §4) si :
1. 3 semaines consécutives sans intervention manuelle de A0
2. Coût compute mensuel < $20 (MiniMax/GLM)
3. Taux d'escalade Donna < 5% des runs
4. Zero workspace orphelin après terminal cleanup

Après validation, un adapter peut être promu en PRD dans `_SPECS/PRD/PRD-<NN>_symphony-<tool>.md` (sous condition que le PRD ne crée pas un SDD nouveau — il référence SDD-008/009/ADR-RICK-001 existants).

---

*Spec generalisée — Shadow A0 — A0 Amadeus — 2026-05-13*
*Toute spécificité tool vit dans `L0/`, `L1/`, ou `L2/` selon la couche A'Space.*
