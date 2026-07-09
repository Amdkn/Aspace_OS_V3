# Symphony Adapter — ClickUp (L2 Shadow Business)

> **Statut** : Shadow A0 — adapter ClickUp pour Symphony A'Space
> **Date** : 2026-05-14
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L2 Shadow Business OS — Matrice 3×8 (SDD-009 §5.2)
> **Slot primaire** : **Ops / Product / IT** (3 domaines PLEINS sur 8)
> **A2 Managers** : Batman (Ops), Flash (Product), Cyborg (IT)
> **A3 Squads** : Fantastic Four (Ops), Avengers (Product), Kang Dynasty (IT)

## 1. Pourquoi ClickUp

- **Build Gates natifs** — statuts custom par liste = QA workflow naturel (Captain America QA)
- **Custom Fields robustes** — SLA portées en champ natif (Number, Currency, Dropdown)
- **Slot Ops/Product/IT** — les 3 domaines de contrôle qualité et delivery
- **API v2 stable** — REST, pagination, webhooks, rate limit clair (100-10k req/min selon plan)
- **Graduation MUSE** → Plane self-hosted ou Supabase native + Kanban UI

## 2. Spécificités ClickUp vs Linear/Plane

| Aspect | Linear | Plane | ClickUp |
|---|---|---|---|
| API | GraphQL | REST v1 | **REST v2** |
| Endpoint | `api.linear.app/graphql` | `api.plane.so/api/v1/` | `api.clickup.com/api/v2/` |
| Auth | API key Bearer | `X-API-Key` | **Bearer** Personal Token |
| Hierarchy | Project + Team | Workspace + Project | **Workspace > Space > Folder > List** |
| Issue concept | Issue | Issue | **Task** |
| State concept | WorkflowState | State | **Status** (custom per list) |
| Subtasks | Yes | No | **Yes** (nested, `subtasks=true`) |
| Custom Fields | Limited | Custom fields | **Rich** (Number, Currency, Date, Dropdown, etc.) |
| Webhooks | Subscriptions | REST webhooks | **REST webhooks** (event-driven) |
| Rate limit | Generous | Generous | **100 req/min** Free, 1k Biz+, 10k Enterprise |
| Terminology | — | — | **Team = Workspace** in API v2 |

## 3. WORKFLOW.md type pour ClickUp

```yaml
---
tracker:
  kind: clickup
  endpoint: "https://api.clickup.com/api/v2"
  api_key: $CLICKUP_API_TOKEN
  team_id: $CLICKUP_TEAM_ID                 # = Workspace ID in API v2
  list_id: $CLICKUP_LIST_OPS                 # List ID (numerical)
  active_states:
    - "to do"            # Ops — Batman — triage initial
    - "in progress"      # Product — Flash — en cours
    - "review"           # QA — Captain America — Build Gate
    - "staging"          # IT — Cyborg — pré-production
  terminal_states:
    - "closed"
    - "cancelled"
  state_mapping:
    inbox: "to do"
    next_actions: "in progress"
    in_progress: "in progress"
    waiting_for: "review"
    done: "closed"
    cancelled: "cancelled"

polling:
  interval_ms: 120000              # 2 min — ClickUp rate limit aware

workspace:
  root: "/srv/aspace/workspaces/clickup"

hooks:
  before_dispatch: |
    # Validation : Build Gate check — un ticket sans DoD est rejeté
    if [ -z "{{issue.description}}" ]; then
      echo "ERROR: Ticket sans Description / DoD — Batman refuse le dispatch"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l2-ops-only

agent:
  max_concurrent_agents: 3
  max_turns: 12
  max_retry_backoff_ms: 300000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 1800000          # 30 min max

soc:
  schema_version: "1.0"
  default_domain: "Ops"
  zod_validation: true
  forbidden_lexicon_global:
    - "synergie"
    - "disrupter"
    - "innover"

donna_dlq:
  enabled: true
  threshold_failed_attempts: 3
  donna_endpoint: "http://localhost:3101/donna/escalate"

clara_cli:
  convert_mcp_to_cli: true
  preferred_runtime: "cli"
---

# Prompt template

Tu es un A3 Squad Marvel opérant un ticket ClickUp dans le Shadow L2 Business.

Ton squad selon le domaine SOA :
- **Ops** : **Fantastic Four** (Mr Fantastic=arch, Inv. Woman=docs, Thing=stability, Torch=speed, Doom=audit)
- **Product** : **Avengers** (Cap America=QA, Iron Man=build, Thor=ship, Widow=research)
- **IT** : **Kang Dynasty** (Kang=repo, Immortus=legacy, Iron Lad=new, Rama-Tut=access)

Ticket :
- **ID** : {{issue.identifier}}
- **Titre** : {{issue.title}}
- **Description** : {{issue.description}}
- **État** : {{issue.state}}
- **Domaine SOA** : {{issue.soc_metadata.target_soa_domain}}

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Outils : `clickup_rest`, `aspace_clara_cli`, `aspace_donna_escalate`, `aspace_soc_emit`

**Règle Build Gate** : Un ticket en `review` ne passe à `closed` QUE si Captain America (QA) valide contre le DoD et le `forbidden_lexicon`.

**Règle The Thing** : Si SLA Temporel > 80%, freeze + escalade.

{% if attempt %}
**Continuation attempt #{{attempt}}**
{% endif %}
```

## 4. Tracker Adapter — implémentation ClickUp

### 4.1 Operations requises

```python
class ClickUpAdapter(TrackerAdapter):
    BASE_URL = "https://api.clickup.com/api/v2"

    def __init__(self, config: ServiceConfig):
        self.token = config.tracker.api_key
        self.team_id = config.tracker.team_id
        self.list_id = config.tracker.list_id
        self.headers = {
            "Authorization": self.token,     # ClickUp: token direct, pas "Bearer"
            "Content-Type": "application/json",
        }

    def fetch_candidate_issues(self) -> list[Issue]:
        # GET /list/{list_id}/task?statuses[]=to+do&statuses[]=in+progress&...
        # Pagination via page number (0-indexed)
        tasks = []
        page = 0
        while True:
            params = {
                "statuses[]": self.config.tracker.active_states,
                "page": page,
                "subtasks": "false",
                "include_closed": "false",
            }
            resp = requests.get(
                f"{self.BASE_URL}/list/{self.list_id}/task",
                headers=self.headers, params=params,
            )
            resp.raise_for_status()
            data = resp.json()
            batch = data.get("tasks", [])
            tasks.extend([self.normalize(t) for t in batch])
            if data.get("last_page", True):
                break
            page += 1
        return tasks

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        # Same endpoint with explicit statuses[] param
        ...

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        # GET /task/{task_id} — N+1 unavoidable, parallelize
        # ClickUp has no bulk task-by-ids endpoint
        results = {}
        for tid in issue_ids:
            resp = requests.get(f"{self.BASE_URL}/task/{tid}", headers=self.headers)
            resp.raise_for_status()
            task = resp.json()
            results[tid] = task["status"]["status"]
        return results
```

### 4.2 Normalisation ClickUp → Issue

```python
def normalize(self, task: dict) -> Issue:
    return Issue(
        id=task["id"],
        identifier=f"CU-{task['id']}",
        title=task["name"],
        description=task.get("description", None),
        priority=CU_PRIORITY_MAP.get(task.get("priority", {}).get("id"), None),
        state=task["status"]["status"],
        branch_name=None,
        url=task.get("url", f"https://app.clickup.com/t/{task['id']}"),
        labels=[t["name"].lower() for t in task.get("tags", [])],
        blocked_by=extract_cu_dependencies(task),
        created_at=parse_ms_timestamp(task.get("date_created")),
        updated_at=parse_ms_timestamp(task.get("date_updated")),
        soc_metadata=extract_soc_from_custom_fields(task.get("custom_fields", [])),
        sla_constraints=extract_sla_from_custom_fields(task.get("custom_fields", [])),
    )

# ClickUp priority IDs: 1=Urgent, 2=High, 3=Normal, 4=Low
CU_PRIORITY_MAP = {"1": 1, "2": 2, "3": 3, "4": 4, None: None}
```

### 4.3 Extraction SOC depuis Custom Fields ClickUp

Custom Fields sont identifiés par `field_id` et portent les metadata SOC :

| Custom Field Name | Type | Mapping SOC |
|---|---|---|
| `SOA Domain` | Dropdown | `target_soa_domain` |
| `Forbidden Words` | Text | `forbidden_lexicon` (comma-sep) |
| `Context Pack` | URL | `context_pack_url` |

```python
def extract_soc_from_custom_fields(custom_fields: list) -> SOCMetadata:
    cf_map = {cf["name"]: cf.get("value") for cf in custom_fields}
    return SOCMetadata(
        target_soa_domain=cf_map.get("SOA Domain"),
        forbidden_lexicon=[w.strip() for w in (cf_map.get("Forbidden Words") or "").split(",") if w.strip()],
        context_pack_url=cf_map.get("Context Pack"),
    )
```

### 4.4 Extraction SLA

| Custom Field | Type | Mapping SLA | Default |
|---|---|---|---|
| `SLA Max Time` | Number | `max_execution_time_minutes` | 90 |
| `SLA Max Cost` | Number | `max_compute_budget_usd` | 1.00 |
| `SLA Max Retries` | Number | `max_retry_loops` | 2 |

### 4.5 Custom Fields — Set via API

ClickUp custom fields require a separate endpoint:
```
POST /task/{task_id}/field/{field_id}
{"value": <value>}
```
→ Agent tooling uses `clickup_rest` tool to update these.

## 5. Webhooks ClickUp

```bash
curl -X POST "https://api.clickup.com/api/v2/team/$CLICKUP_TEAM_ID/webhook" \
  -H "Authorization: $CLICKUP_API_TOKEN" \
  -d '{
    "endpoint": "http://symphony.aspace.local:3200/webhook/clickup",
    "events": ["taskCreated", "taskUpdated", "taskStatusUpdated", "taskDeleted"]
  }'
```

ClickUp webhooks **do not expire** (contrairement à Airtable). Pas de refresh cron requis.

**Stratégie** : Webhook actif + polling 2 min backup.

## 6. Build Gates — Spécificité ClickUp/Ops

Le **Build Gate** est le concept clé du slot Ops :

```
to do → in progress → review (BUILD GATE) → staging → closed
```

- **Build Gate = status `review`** : l'agent (Captain America QA) évalue contre le DoD
- Si DoD non satisfait → agent commente le ticket avec feedback + remet en `in progress`
- Si DoD satisfait → agent fait passer en `staging` puis `closed`

Symphony gère ce flux via le prompt template : l'état `review` déclenche le comportement QA.

## 7. Matrice 3×8 ClickUp (SDD-009 §5.2)

| Domaine | Statut | Squad Marvel |
|---|---|---|
| **Ops** | 🟢 PLEIN | Fantastic Four |
| **Product** | 🟢 PLEIN | Avengers |
| **IT** | 🟢 PLEIN | Kang Dynasty |
| Growth | 🌙 dormant | — |
| Sales | 🌙 dormant | — |
| Finance | 🌙 dormant | — |
| People | 🌙 dormant | — |
| Legal | 🌙 dormant | — |

Astuce : utiliser des **Lists séparées par domaine** dans un même Space, avec `list_id` switchable en config.

## 8. Coût exploitation

| Item | Coût mensuel |
|---|---|
| ClickUp Free | $0 (100 uses, 100MB storage) |
| ClickUp Unlimited | $7/user/mois |
| Compute MiniMax 2.7 | ~$6/mois |
| **TOTAL Free** | **$6/mois** |

## 9. Graduation MUSE

3 semaines stable → PRD-CU-001 :
1. Plane self-hosted (Build Gate concept transposable)
2. Migration via ClickUp export API
3. Update WORKFLOW.md `tracker.kind: plane`, endpoint self-host
4. Ou Supabase native avec Kanban UI custom (SDD-005)

## 10. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| Rate limit 100 req/min (Free) | Haute | Queue + upgrade si nécessaire |
| N+1 sur fetch_issue_states_by_ids | Moyenne | Paralléliser + cache 60s |
| Custom Fields format variable | Moyenne | Validation Zod stricte |
| Team=Workspace naming confusion | Faible | Documentation claire |

## 11. Hors-scope

- ❌ Pas de ClickUp Goals/Dashboards (Life Web OS = UI cible)
- ❌ Pas de ClickUp Docs (Notion = mémoire, Obsidian = PARA)
- ❌ Pas de bi-sync ClickUp ↔ Airtable
- ❌ Pas d'auto-création tasks (Symphony lit + agent écrit)
- ❌ Pas de ClickUp Automations (Symphony = orchestrateur)

---

*Adapter ClickUp — Shadow A0 — L2 Business — Ops/Product/IT — 2026-05-14*
