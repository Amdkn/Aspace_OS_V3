# Symphony Adapter — Baserow (L1 Shadow Life OS)

> **Statut** : Shadow A0 — adapter Baserow pour Symphony A'Space
> **Date** : 2026-05-14
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L1 Shadow Life OS — USS Strange New Worlds (SDD-008 §3.2)
> **Mappage SDD** : SDD-008 §2 (Pilier 2 — Baserow = 12 Week Year)
> **A2 Manager** : Curie (USS SNW)
> **Méthode** : **12WY** (Quarter Intent / 12 Rocks / Warp Core W1-W12)

## 1. Pourquoi Baserow

- **API REST simple** — CRUD standard, Token auth, batch operations
- **Pilier 2 du Shadow L1** (méthode 12WY, cf. SDD-008)
- **URL active** : `https://baserow.io/database/284361/`
- **Self-hosting facile** — Baserow est open source (Docker)
- **Tables = structured data** — parfaitement adapté aux 3 tables 12WY canoniques
- **Graduation MUSE** → Baserow self-hosted ou NocoDB sur VPS

## 2. Spécificités Baserow vs Linear/Plane

| Aspect | Linear | Plane | Baserow |
|---|---|---|---|
| API | GraphQL | REST v1 | **REST** (auto-generated per schema) |
| Endpoint | `api.linear.app/graphql` | `api.plane.so/api/v1/` | `https://api.baserow.io/api/` |
| Auth | API key Bearer | `X-API-Key` | **`Authorization: Token`** (Database Token) |
| Project concept | Project + Team | Workspace + Project | **Database > Table** |
| Issue concept | Issue | Issue | **Row** (dans une Table) |
| State concept | WorkflowState | State | **Single Select field** |
| Batch ops | No | No | **Yes** (`/batch/` endpoints) |
| Schema-aware docs | No | No | **Yes** (auto-generated per table) |
| Webhooks | Subscriptions | REST | **❌ Pas de webhooks** (polling only) |
| Rate limit | Generous | Generous | **Generous** (60 req/min cloud) |
| Pagination | cursor | cursor | **page** (`?page=N&size=100`) |
| Field names | — | — | `?user_field_names=true` (human-readable) |

⚠️ Baserow Cloud n'a **pas de webhooks**. Polling pur. Self-hosted Baserow supporte les webhooks.

## 3. Architecture des 3 Tables 12WY (SDD-008 §3.2)

Curie orchestre 3 tables canoniques dans la Database Baserow :

### Table 1 : `Quarter Intent` (table_id: 955428)

| Colonne | Type | Usage |
|---|---|---|
| `Layer` | Single Select (`L0`, `L1`, `L2`) | Couche A'Space |
| `Vision` | Long Text | Vision trimestrielle par couche |
| `Status` | Single Select | `Draft`, `Active`, `Archived` |
| `Cycle` | Text | `H1-C2` etc. |

### Table 2 : `The 12 Rocks` (table_id: 955426)

| Colonne | Type | Usage |
|---|---|---|
| `Rock Name` | Text | Objectif trimestriel |
| `Layer Tag` | Single Select (`Rock L0`, `Rock L1`, `Rock L2`) | Couche |
| `Week Target` | Number | Semaine cible (W1-W12) |
| `Status` | Single Select | `Not Started`, `In Progress`, `Done`, `Blocked` |
| `MUSE_GRADUATED` | Boolean | `true` si < 20% temps manuel |
| `Linked Plane Tickets` | Text/URL | Lien vers Plane issues |
| `SLA Max Time` | Number | `max_execution_time_minutes` |
| `SLA Max Cost` | Number | `max_compute_budget_usd` |

### Table 3 : `The Warp Core` (table_id: 955429)

| Colonne | Type | Usage |
|---|---|---|
| `Week` | Text | `W1` à `W12` |
| `Top 3 Mon-Tue-Wed` | Long Text | 3 Commitments L2 (50%) |
| `Top 3 Thu-Fri` | Long Text | 3 Commitments L1 (30%) |
| `Top 3 Sat-Sun` | Long Text | 3 Commitments L0 (20%) |
| `Status` | Single Select | `Planned`, `Active`, `Done`, `Skipped` |
| `Score` | Number | % completion (0-100) |

## 4. WORKFLOW.md type pour Baserow

```yaml
---
tracker:
  kind: baserow
  endpoint: "https://api.baserow.io/api"
  api_key: $BASEROW_DATABASE_TOKEN
  table_id: 955426                           # Table "The 12 Rocks" — primary tracking table
  active_states:
    - "Not Started"
    - "In Progress"
    - "Blocked"
  terminal_states:
    - "Done"
    - "Cancelled"
  state_mapping:
    inbox: "Not Started"
    next_actions: "In Progress"
    in_progress: "In Progress"
    waiting_for: "Blocked"
    done: "Done"
    cancelled: "Cancelled"
  state_field: "Status"
  user_field_names: true                     # Use human-readable field names

polling:
  interval_ms: 120000              # 2 min — pas de webhooks sur Baserow Cloud

workspace:
  root: "/srv/aspace/workspaces/baserow"

hooks:
  before_dispatch: |
    # Validation : un Rock sans Layer Tag est rejeté
    if ! echo "{{issue.labels | join: ','}}}" | grep -qE '(Rock L0|Rock L1|Rock L2)'; then
      echo "ERROR: Rock sans Layer Tag (@L0/@L1/@L2)"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l1-12wy-only

agent:
  max_concurrent_agents: 3
  max_turns: 8                    # 12WY tasks = focused, short
  max_retry_backoff_ms: 180000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 1200000        # 20 min max

soc:
  schema_version: "1.0"
  default_domain: "Life_OS"
  zod_validation: true
  forbidden_lexicon_global:
    - "innover"
    - "disrupter"
    - "synergie"

donna_dlq:
  enabled: true
  threshold_failed_attempts: 3
  donna_endpoint: "http://localhost:3101/donna/escalate"

clara_cli:
  convert_mcp_to_cli: true
  preferred_runtime: "cli"
---

# Prompt template

Tu es un A3 Compagnon du USS Strange New Worlds opérant un Rock dans Baserow.

Tu es sous le commandement de **Curie (A2 SNW)**. Le système 12 Week Year structure ton travail :
- **Quarter Intent** : vision L0/L1/L2 du trimestre
- **12 Rocks** : objectifs trimestriels concrets (tu opères un Rock)
- **Warp Core** : décomposition hebdomadaire W1-W12 avec ratio 50/30/20

Rock :
- **ID** : {{issue.identifier}}
- **Nom** : {{issue.title}}
- **Description** : {{issue.description}}
- **État** : {{issue.state}}
- **Layer** : {{issue.labels | join: ', '}}
- **Semaine cible** : W{{issue.soc_metadata.target_week}}

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Outils : `baserow_rest`, `aspace_clara_cli`, `aspace_donna_escalate`

**Règle Curie** : si le Rock nécessite > 1 semaine de travail, décompose-le en sous-tâches dans le Warp Core de la semaine active.

**Règle MUSE** : si le Rock atteint < 20% temps manuel → flag `MUSE_GRADUATED=true`.

{% if attempt %}
**Continuation attempt #{{attempt}}**
{% endif %}
```

## 5. Tracker Adapter — implémentation Baserow

### 5.1 Operations requises

```python
class BaserowAdapter(TrackerAdapter):
    BASE_URL = "https://api.baserow.io/api"

    def __init__(self, config: ServiceConfig):
        self.token = config.tracker.api_key
        self.table_id = config.tracker.table_id
        self.state_field = config.tracker.state_field or "Status"
        self.headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json",
        }

    def fetch_candidate_issues(self) -> list[Issue]:
        # GET /database/rows/table/{table_id}/
        # ?user_field_names=true
        # ?filter__{state_field}__single_select_equal=Not Started
        # Baserow: multiple filters via filter__field__type=value
        # Pagination: ?page=N&size=100
        rows = []
        page = 1
        for state in self.config.tracker.active_states:
            while True:
                params = {
                    "user_field_names": "true",
                    f"filter__{self.state_field}__single_select_equal": state,
                    "page": page,
                    "size": 100,
                }
                resp = requests.get(
                    f"{self.BASE_URL}/database/rows/table/{self.table_id}/",
                    headers=self.headers, params=params,
                )
                resp.raise_for_status()
                data = resp.json()
                rows.extend([self.normalize(r) for r in data["results"]])
                if not data.get("next"):
                    break
                page += 1
            page = 1
        return rows

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        # Same pattern per state
        ...

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        # GET /database/rows/table/{table_id}/{row_id}/?user_field_names=true
        results = {}
        for rid in issue_ids:
            resp = requests.get(
                f"{self.BASE_URL}/database/rows/table/{self.table_id}/{rid}/",
                headers=self.headers,
                params={"user_field_names": "true"},
            )
            resp.raise_for_status()
            row = resp.json()
            results[str(rid)] = row.get(self.state_field, {}).get("value", "Unknown")
        return results
```

### 5.2 Normalisation Baserow → Issue

```python
def normalize(self, row: dict) -> Issue:
    return Issue(
        id=str(row["id"]),
        identifier=f"BR-{row['id']}",
        title=row.get("Rock Name", row.get("Name", f"Row {row['id']}")),
        description=row.get("Description", None),
        priority=None,                      # Baserow n'a pas de priority native
        state=row.get(self.state_field, {}).get("value", "Unknown"),
        branch_name=None,
        url=f"https://baserow.io/database/{self.database_id}/table/{self.table_id}/row/{row['id']}",
        labels=extract_labels_from_selects(row),
        blocked_by=[],
        created_at=parse_iso(row.get("created_on")),
        updated_at=parse_iso(row.get("updated_on")),
        soc_metadata=extract_soc_from_row(row),
        sla_constraints=extract_sla_from_row(row),
    )
```

### 5.3 Extraction SOC / SLA

| Champ Baserow | Type | Mapping |
|---|---|---|
| `Layer Tag` | Single Select | Labels (`Rock L0`/`Rock L1`/`Rock L2`) |
| `Week Target` | Number | `soc_metadata.target_week` |
| `MUSE_GRADUATED` | Boolean | flag de graduation |
| `SLA Max Time` | Number | `max_execution_time_minutes` (default: 60) |
| `SLA Max Cost` | Number | `max_compute_budget_usd` (default: 0.50) |

## 6. Cycles Plane ↔ Baserow Warp Core (SDD-008 §3.1)

**Doctrine** : Cycle Plane = 1 semaine W du Warp Core Baserow.

```python
def sync_plane_cycle_to_baserow_week():
    plane_cycle = plane.get_current_cycle(project_id)
    # Find matching Warp Core week in table 955429
    warp_core_rows = baserow.list_rows(table_id=955429, filter_week=f"W{plane_cycle.number}")
    for row in warp_core_rows:
        baserow.update_row(row["id"], {"Status": {"value": "Active"}})
```

→ Permet à Curie (A2 SNW) de voir la semaine active sans switch d'outil.

## 7. Coût exploitation

| Item | Coût mensuel |
|---|---|
| Baserow Cloud Free | $0 (3000 rows) |
| Baserow Cloud Premium | $5/user/mois |
| Baserow self-hosted | $0 (Docker) — cible MUSE |
| Compute MiniMax 2.7 | ~$3/mois (12 Rocks/trimestre × low tokens) |
| **TOTAL Free** | **$3/mois** |

## 8. Graduation MUSE

3 semaines stable → PRD-BR-001 :
1. Baserow self-hosted via Dokploy (Docker compose)
2. Data migration (Baserow export API → import self-host)
3. Webhooks activés en self-hosted (pas dispo en Cloud)
4. Update WORKFLOW.md endpoint vers self-host

## 9. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| Pas de webhooks (Cloud) | N/A | Polling 2 min + cache |
| API schema-dependent (dynamic fields) | Faible | `user_field_names=true` |
| 3000 rows limit (Free) | Faible | 12WY = ~36 rows/trimestre |
| Single Select value format | Faible | Extract `.value` from dict |
| Baserow filter syntax non-standard | Moyenne | Docs auto-generated per table |

## 10. Hors-scope

- ❌ Pas de Baserow Forms (capture → Plane Inbox)
- ❌ Pas de Baserow Kanban view sync (vue = UI, pas adapter)
- ❌ Pas de bi-sync Baserow ↔ Obsidian PARA (Airlock Plane → Obsidian gère ça)
- ❌ Pas d'auto-création rows (Symphony lit + agent écrit)

---

*Adapter Baserow — Shadow A0 — L1 Life OS — 12WY Warp Core — 2026-05-14*
