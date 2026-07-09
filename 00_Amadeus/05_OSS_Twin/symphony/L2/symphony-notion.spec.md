# Symphony Adapter — Notion (L2 Shadow Business)

> **Statut** : Shadow A0 — adapter Notion pour Symphony A'Space
> **Date** : 2026-05-14
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L2 Shadow Business OS — Matrice 3×8 (SDD-009 §5.2)
> **Slot primaire** : **People / Legal** (2 domaines PLEINS sur 8)
> **A2 Managers** : Green Lantern (People), Aquaman (Legal)
> **A3 Squads** : X-Men (People), Eternals (Legal)

## 1. Pourquoi Notion

- **Knowledge base native** — Database API + Pages = mémoire sédimentaire (RAG, Brand Books, SOPs)
- **Slot People/Legal** — les 2 domaines orientés connaissance/compliance
- **Compound filters** — requêtes puissantes sur properties (AND/OR, multi-type)
- **Rich text content** — chaque Page = document structuré, pas un simple ticket
- **Graduation MUSE** → Obsidian + Supabase (vault PARA + RAG vectorisé)

## 2. Spécificités Notion vs Linear/Plane

| Aspect | Linear | Plane | Notion |
|---|---|---|---|
| API | GraphQL | REST v1 | **REST** (v1) |
| Endpoint | `api.linear.app/graphql` | `api.plane.so/api/v1/` | `api.notion.com/v1/` |
| Auth | API key Bearer | `X-API-Key` | **Bearer** Internal Integration Token |
| Project concept | Project + Team | Workspace + Project | **Database** (dans un Workspace) |
| Issue concept | Issue | Issue | **Page** (row dans un Database) |
| State concept | WorkflowState | State | **Status property** (Select/Status type) |
| Rich content | Markdown | HTML | **Blocks API** (structured blocks) |
| Webhooks | Subscriptions | REST webhooks | **❌ Pas de webhooks** — polling only |
| Rate limit | Generous | Generous | **3 req/s** (strict) |
| Pagination | cursor | cursor | **cursor** (`next_cursor`, 100/page max) |
| API Version header | — | — | **`Notion-Version: 2022-06-28`** requis |

⚠️ **Point critique** : Notion **n'a pas de webhooks**. Symphony doit fonctionner en **polling pur**. Intervalle recommandé : 3-5 min pour respecter le rate limit.

## 3. WORKFLOW.md type pour Notion

```yaml
---
tracker:
  kind: notion
  endpoint: "https://api.notion.com/v1"
  api_key: $NOTION_INTEGRATION_TOKEN        # Internal Integration Token
  database_id: $NOTION_DB_PEOPLE_LEGAL      # Database ID (32-char hex)
  active_states:
    - "New"              # People — Green Lantern — nouveau record
    - "In Review"        # Legal — Aquaman — compliance review
    - "Active"           # Both — document actif
  terminal_states:
    - "Archived"
    - "Rejected"
  state_mapping:
    inbox: "New"
    next_actions: "In Review"
    in_progress: "Active"
    waiting_for: "In Review"
    done: "Archived"
    cancelled: "Rejected"
  state_property: "Status"                   # Nom de la property Status dans le Database

polling:
  interval_ms: 180000              # 3 min — pas de webhooks, rate limit 3 req/s

workspace:
  root: "/srv/aspace/workspaces/notion"

hooks:
  before_dispatch: |
    # Validation SOC : vérifier que le domaine People ou Legal est assigné
    domain="{{issue.soc_metadata.target_soa_domain}}"
    if [ "$domain" != "People" ] && [ "$domain" != "Legal" ]; then
      echo "ERROR: Notion adapter réservé People/Legal, reçu: $domain"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l2-knowledge-only

agent:
  max_concurrent_agents: 2               # 2 domaines seulement — charge légère
  max_turns: 10
  max_retry_backoff_ms: 300000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 1800000

soc:
  schema_version: "1.0"
  default_domain: "People"
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

Tu es un A3 Squad Marvel opérant un Page Notion dans le Shadow L2 Business.

Ton squad selon le domaine SOA :
- **People** : **X-Men** (Prof X=vision, Cyclops=field, Jean Grey=empathy, Beast=knowledge)
  - Mission : RAG Manager, Brand Books vectorisés, lexicons interdits, onboarding docs
- **Legal** : **Eternals** (Ikaris=force, Ajak=compliance, Phastos=IP, Thena=defense)
  - Mission : Contrats, compliance GDPR, WHOIS, terms of service

Page Notion :
- **ID** : {{issue.identifier}}
- **Titre** : {{issue.title}}
- **Description** : {{issue.description}}
- **État** : {{issue.state}}
- **Domaine SOA** : {{issue.soc_metadata.target_soa_domain}}

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Outils : `notion_rest`, `aspace_clara_cli`, `aspace_donna_escalate`, `aspace_soc_emit`

**Règle Ajak (Compliance)** : tout document People/Legal doit être vérifié contre GDPR/données personnelles avant archivage.

**Règle Beast (Knowledge)** : si un Brand Book ou SOP est généré, il DOIT être vectorisé dans le RAG Supabase pgvector via `aspace_clara_cli rag-ingest`.

{% if attempt %}
**Continuation attempt #{{attempt}}**
{% endif %}
```

## 4. Tracker Adapter — implémentation Notion

### 4.1 Operations requises

```python
class NotionAdapter(TrackerAdapter):
    BASE_URL = "https://api.notion.com/v1"
    API_VERSION = "2022-06-28"

    def __init__(self, config: ServiceConfig):
        self.token = config.tracker.api_key
        self.database_id = config.tracker.database_id
        self.state_property = config.tracker.state_property or "Status"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": self.API_VERSION,
            "Content-Type": "application/json",
        }

    def fetch_candidate_issues(self) -> list[Issue]:
        # POST /databases/{database_id}/query
        # Body: filter OR compound on Status property
        pages = []
        cursor = None
        while True:
            body = {
                "filter": self._build_active_filter(),
                "page_size": 100,
            }
            if cursor:
                body["start_cursor"] = cursor
            resp = requests.post(
                f"{self.BASE_URL}/databases/{self.database_id}/query",
                headers=self.headers, json=body,
            )
            resp.raise_for_status()
            data = resp.json()
            pages.extend([self.normalize(p) for p in data["results"]])
            if not data.get("has_more"):
                break
            cursor = data["next_cursor"]
        return pages

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        # Same POST /databases/{id}/query with explicit state filter
        ...

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        # GET /pages/{page_id} — N+1 (Notion has no bulk page endpoint)
        results = {}
        for pid in issue_ids:
            resp = requests.get(
                f"{self.BASE_URL}/pages/{pid}",
                headers=self.headers,
            )
            resp.raise_for_status()
            page = resp.json()
            results[pid] = self._extract_status(page)
        return results

    def _build_active_filter(self) -> dict:
        states = self.config.tracker.active_states
        if len(states) == 1:
            return {
                "property": self.state_property,
                "status": {"equals": states[0]},
            }
        return {
            "or": [
                {"property": self.state_property, "status": {"equals": s}}
                for s in states
            ]
        }

    def _extract_status(self, page: dict) -> str:
        prop = page["properties"].get(self.state_property, {})
        if prop.get("type") == "status":
            return prop["status"]["name"] if prop.get("status") else "Unknown"
        if prop.get("type") == "select":
            return prop["select"]["name"] if prop.get("select") else "Unknown"
        return "Unknown"
```

### 4.2 Normalisation Notion → Issue

```python
def normalize(self, page: dict) -> Issue:
    props = page["properties"]
    return Issue(
        id=page["id"],
        identifier=f"NT-{page['id'][:8]}",
        title=self._extract_title(props),
        description=None,                   # Notion: content = blocks, pas une property
        priority=PRIORITY_MAP.get(self._extract_select(props, "Priority"), None),
        state=self._extract_status(page),
        branch_name=None,
        url=page.get("url", f"https://notion.so/{page['id'].replace('-', '')}"),
        labels=[t.lower() for t in self._extract_multi_select(props, "Tags")],
        blocked_by=[],
        created_at=parse_iso(page.get("created_time")),
        updated_at=parse_iso(page.get("last_edited_time")),
        soc_metadata=self._extract_soc(props),
        sla_constraints=self._extract_sla(props),
    )

def _extract_title(self, props: dict) -> str:
    for prop in props.values():
        if prop.get("type") == "title":
            titles = prop.get("title", [])
            return "".join(t["plain_text"] for t in titles) if titles else "Untitled"
    return "Untitled"

def _extract_select(self, props: dict, name: str) -> str | None:
    prop = props.get(name, {})
    if prop.get("select"):
        return prop["select"]["name"]
    return None

def _extract_multi_select(self, props: dict, name: str) -> list[str]:
    prop = props.get(name, {})
    return [ms["name"] for ms in prop.get("multi_select", [])]

PRIORITY_MAP = {"Urgent": 1, "High": 2, "Medium": 3, "Low": 4, None: None}
```

### 4.3 Extraction SOC depuis Properties Notion

| Property Notion | Type | Mapping SOC |
|---|---|---|
| `SOA Domain` | Select | `target_soa_domain` |
| `Forbidden Words` | Rich Text | `forbidden_lexicon` (comma-sep) |
| `Context Pack` | URL | `context_pack_url` |
| `Tags` | Multi Select | Labels normalisées |

### 4.4 Extraction SLA

| Property Notion | Type | Mapping SLA | Default |
|---|---|---|---|
| `SLA Max Time` | Number | `max_execution_time_minutes` | 90 |
| `SLA Max Cost` | Number | `max_compute_budget_usd` | 0.80 |
| `SLA Max Retries` | Number | `max_retry_loops` | 2 |

### 4.5 Spécificité Notion : contenu = Blocks, pas Description

Notion Pages n'ont **pas de champ description** comme Plane/ClickUp. Le contenu est une **liste de Blocks** (paragraphs, headings, bulleted lists, etc.) accessible via :

```
GET /blocks/{page_id}/children
```

Pour Symphony, 2 stratégies :
1. **Lazy** : ne pas récupérer les blocks, laisser l'agent les lire via `notion_rest` tool
2. **Eager** : récupérer les premiers 20 blocks et les inclure dans le prompt comme `{{issue.description}}`

→ Recommandé : **Lazy** (économie de tokens prompt, l'agent lit à la demande).

## 5. Polling pur (pas de webhooks)

Notion **n'a pas de webhooks**. Symphony fonctionne en polling strict.

### 5.1 Optimisation polling

- `polling.interval_ms: 180000` (3 min)
- Filtre `last_edited_time` pour ne récupérer que les pages modifiées depuis le dernier poll :

```python
def _build_active_filter_with_recency(self, since: str) -> dict:
    return {
        "and": [
            self._build_active_filter(),
            {
                "timestamp": "last_edited_time",
                "last_edited_time": {"after": since},
            },
        ]
    }
```

### 5.2 Rate limit management

- 3 req/s strict → queue interne Symphony avec 350ms entre chaque requête
- Retry 429 avec backoff : `delay = min(1000 * 2^attempt, 30000)`

## 6. Matrice 3×8 Notion (SDD-009 §5.2)

| Domaine | Statut | Squad Marvel |
|---|---|---|
| **People** | 🟢 PLEIN | X-Men |
| **Legal** | 🟢 PLEIN | Eternals |
| Growth | 🌙 dormant | — |
| Sales | 🌙 dormant | — |
| Finance | 🌙 dormant | — |
| Ops | 🌙 dormant | — |
| Product | 🌙 dormant | — |
| IT | 🌙 dormant | — |

Les 6 domaines dormants ont des **Databases miroir** dans Notion mais aucune routine A3 active.

## 7. Coût exploitation

| Item | Coût mensuel |
|---|---|
| Notion Free | $0 (blocks illimités, 10 guests) |
| Notion Plus | $10/user/mois si besoin |
| Compute MiniMax 2.7 | ~$4/mois (People/Legal = volume léger) |
| **TOTAL Free** | **$4/mois** |

## 8. Graduation MUSE

3 semaines stable → PRD-NT-001 :
1. **Obsidian** + LiveSync sur Supabase (vault PARA souverain)
2. **Supabase pgvector** pour le RAG (Brand Books, SOPs vectorisés)
3. Migration : Notion export MD → Obsidian vault import
4. Update WORKFLOW.md `tracker.kind: obsidian`

## 9. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| Rate limit 3 req/s strict | Haute | Queue 350ms + cache réconciliation |
| Pas de webhooks (polling only) | N/A | Intervalle 3 min + filtre last_edited_time |
| N+1 sur fetch_issue_states_by_ids | Moyenne | Paralléliser (3 threads max) |
| Notion API breaking changes | Faible | Pin `Notion-Version` header |
| Blocks API != description | Moyenne | Lazy loading via agent tooling |

## 10. Hors-scope

- ❌ Pas de Notion AI (Symphony = orchestrateur, pas Notion AI)
- ❌ Pas de Notion Synced Databases cross-workspace
- ❌ Pas de bi-sync Notion ↔ Obsidian (graduation MUSE = migration one-way)
- ❌ Pas d'auto-création Pages (Symphony lit + agent écrit)
- ❌ Pas de Notion Comments (l'agent utilise `notion_rest` pour commenter si besoin)

---

*Adapter Notion — Shadow A0 — L2 Business — People/Legal — 2026-05-14*
