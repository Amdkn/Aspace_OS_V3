# Symphony Adapter — Airtable (L2 Shadow Business)

> **Statut** : Shadow A0 — adapter Airtable pour Symphony A'Space
> **Date** : 2026-05-14
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L2 Shadow Business OS — Matrice 3×8 (SDD-009 §5.2)
> **Slot primaire** : **Growth / Sales / Finance** (3 domaines PLEINS sur 8)
> **A2 Managers** : Superman (Growth), John Jones (Sales), Wonder Woman (Finance)
> **A3 Squads** : Gardiens de la Galaxie, Illuminati, Thunderbolts

## 1. Pourquoi Airtable en premier (L2)

- **Meilleure API du lot L2** — REST mature, stable, bien documentée
- **Webhooks natifs** — réactivité événementielle sans polling intensif
- **Slot Lead/Sales/Finance** — les 3 domaines qui génèrent du cashflow (Beth Veto)
- **Formulaires natifs** — capture externe (leads, briefs) sans code
- **Relational DB** — modélisation CRM + pipeline naturelle
- **Graduation MUSE** → NocoDB self-hosted ou Supabase native

## 2. Spécificités Airtable vs Linear/Plane

| Aspect | Linear | Plane | Airtable |
|---|---|---|---|
| API | GraphQL | REST v1 | **REST** (v0) |
| Endpoint | `api.linear.app/graphql` | `api.plane.so/api/v1/` | `api.airtable.com/v0/` |
| Auth | API key Bearer | `X-API-Key` | **Bearer PAT** |
| Project concept | Project + Team | Workspace + Project | **Base + Table** |
| Issue concept | Issue | Issue | **Record** (row) |
| State concept | WorkflowState | State | **Single Select field** |
| Webhooks | GraphQL subscriptions | REST webhooks | **REST webhooks** (7j expiration) |
| Rate limit | Generous | Generous | **5 req/s par base** |
| Pagination | cursor | cursor | **offset** (100/page) |

## 3. WORKFLOW.md type pour Airtable

```yaml
---
tracker:
  kind: airtable
  endpoint: "https://api.airtable.com/v0"
  api_key: $AIRTABLE_PAT
  base_id: $AIRTABLE_BASE_BUSINESS
  table_id: $AIRTABLE_TABLE_PIPELINE
  active_states:
    - "New Lead"
    - "Qualified"
    - "Proposal Sent"
    - "In Production"
  terminal_states:
    - "Won"
    - "Lost"
    - "Churned"
    - "Archived"
  state_mapping:
    inbox: "New Lead"
    next_actions: "Qualified"
    in_progress: "In Production"
    waiting_for: "Proposal Sent"
    done: "Won"
    cancelled: "Lost"
  state_field: "Status"

polling:
  interval_ms: 300000              # 5 min backup — webhooks actifs

workspace:
  root: "/srv/aspace/workspaces/airtable"

hooks:
  before_dispatch: |
    if [ -z "{{issue.soc_metadata.target_soa_domain}}" ]; then
      echo "ERROR: Record sans domaine SOA assigné"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l2-business-only

agent:
  max_concurrent_agents: 3
  max_turns: 15
  max_retry_backoff_ms: 300000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 2400000

soc:
  schema_version: "1.0"
  default_domain: "Growth"
  zod_validation: true
  forbidden_lexicon_global:
    - "synergie"
    - "disrupter"
    - "innover"
    - "révolutionnaire"

donna_dlq:
  enabled: true
  threshold_failed_attempts: 3
  donna_endpoint: "http://localhost:3101/donna/escalate"

clara_cli:
  convert_mcp_to_cli: true
  preferred_runtime: "cli"
---

# Prompt template

Tu es un A3 Squad Marvel opérant un record Airtable dans le Shadow L2 Business.

Ton squad selon le domaine SOA :
- **Growth** : **Gardien de la Galaxie** (Star-Lord=copy, Rocket=ads, Gamora=pipeline, Groot=brand)
- **Sales** : **Illuminati** (CRM, pipeline, demo, contrats)
- **Finance** : **Thunderbolt** (Taskmaster=pricer, Zemo=auditor, Red Hulk=budget, Ghost=leaks)

Record :
- **ID** : {{issue.identifier}}
- **Titre** : {{issue.title}}
- **Description** : {{issue.description}}
- **État** : {{issue.state}}
- **Domaine SOA** : {{issue.soc_metadata.target_soa_domain}}

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Outils : `airtable_rest`, `aspace_clara_cli`, `aspace_donna_escalate`, `aspace_soc_emit`

**Règle Wonder Woman** : compute > 80% budget → STOP immédiat.
**Règle Captain America** : forbidden_lexicon dans output → rejet.

{% if attempt %}
**Continuation attempt #{{attempt}}**
{% endif %}
```

## 4. Tracker Adapter — implémentation Airtable

### 4.1 Operations requises

```python
class AirtableAdapter(TrackerAdapter):
    BASE_URL = "https://api.airtable.com/v0"

    def __init__(self, config: ServiceConfig):
        self.pat = config.tracker.api_key
        self.base_id = config.tracker.base_id
        self.table_id = config.tracker.table_id
        self.state_field = config.tracker.state_field or "Status"
        self.headers = {
            "Authorization": f"Bearer {self.pat}",
            "Content-Type": "application/json",
        }

    def fetch_candidate_issues(self) -> list[Issue]:
        # GET /v0/{base_id}/{table_id}?filterByFormula=OR(...)
        # Pagination via offset token
        records = []
        offset = None
        while True:
            params = {
                "filterByFormula": self._build_active_states_formula(),
                "pageSize": 100,
            }
            if offset:
                params["offset"] = offset
            resp = requests.get(
                f"{self.BASE_URL}/{self.base_id}/{self.table_id}",
                headers=self.headers, params=params,
            )
            resp.raise_for_status()
            data = resp.json()
            records.extend([self.normalize(r) for r in data["records"]])
            offset = data.get("offset")
            if not offset:
                break
        return records

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        formula = self._build_states_formula(state_names)
        # Same pagination pattern as above
        ...

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        # Bulk read via filterByFormula — no N+1
        formula = "OR(" + ",".join(f'RECORD_ID()="{rid}"' for rid in issue_ids) + ")"
        ...

    def _build_active_states_formula(self) -> str:
        states = self.config.tracker.active_states
        clauses = [f'{{{self.state_field}}}="{s}"' for s in states]
        return f"OR({','.join(clauses)})"
```

### 4.2 Normalisation Airtable → Issue

```python
def normalize(self, record: dict) -> Issue:
    fields = record["fields"]
    return Issue(
        id=record["id"],                                    # recXXXXXXXXX
        identifier=f"AT-{record['id'][:8]}",
        title=fields.get("Name", "Untitled"),
        description=fields.get("Description", None),
        priority=PRIORITY_MAP.get(fields.get("Priority", ""), None),
        state=fields.get(self.state_field, "Unknown"),
        branch_name=None,
        url=f"https://airtable.com/{self.base_id}/{self.table_id}/{record['id']}",
        labels=[l.lower() for l in fields.get("Tags", [])],
        blocked_by=extract_blockers_from_linked(fields),
        created_at=parse_iso(record.get("createdTime")),
        updated_at=None,    # Airtable ne retourne pas updated_at par défaut
        soc_metadata=extract_soc_from_fields(fields),
        sla_constraints=extract_sla_from_fields(fields),
    )

PRIORITY_MAP = {"Urgent": 1, "High": 2, "Medium": 3, "Low": 4, "": None}
```

### 4.3 Extraction SOC depuis champs Airtable

| Champ Airtable | Type | Mapping SOC |
|---|---|---|
| `SOA Domain` | Single Select | `target_soa_domain` |
| `Forbidden Words` | Long Text (comma-sep) | `forbidden_lexicon` |
| `Context Pack` | URL | `context_pack_url` |
| `Tags` | Multi Select | Labels normalisées |

### 4.4 Extraction SLA depuis champs Airtable

| Champ Airtable | Type | Mapping SLA | Default |
|---|---|---|---|
| `SLA Max Time (min)` | Number | `max_execution_time_minutes` | 120 |
| `SLA Max Cost ($)` | Currency | `max_compute_budget_usd` | 1.50 |
| `SLA Max Retries` | Number | `max_retry_loops` | 2 |

## 5. Webhooks Airtable

### 5.1 Lifecycle

```bash
# Création
curl -X POST "https://api.airtable.com/v0/bases/$BASE_ID/webhooks" \
  -H "Authorization: Bearer $AIRTABLE_PAT" \
  -d '{"notificationUrl":"http://symphony.aspace.local:3200/webhook/airtable",
       "specification":{"options":{"filters":{"dataTypes":["tableData"]}}}}'
```

**Expiration 7 jours** — refresh automatique tous les 5 jours via cron Symphony.

### 5.2 Stratégie hybride

- Webhook actif → dispatch immédiat
- Polling 5 min → backup
- ~90% dispatches via webhook, 10% polling

## 6. Matrice 3×8 Airtable (SDD-009 §5.2)

| Domaine | Statut | Squad Marvel |
|---|---|---|
| **Growth** | 🟢 PLEIN | Gardiens de la Galaxie |
| **Sales** | 🟢 PLEIN | Illuminati |
| **Finance** | 🟢 PLEIN | Thunderbolts |
| Ops | 🌙 dormant | — |
| Product | 🌙 dormant | — |
| IT | 🌙 dormant | — |
| People | 🌙 dormant | — |
| Legal | 🌙 dormant | — |

Astuce : utiliser `view` param pour filtrer par domaine sans formule complexe.

## 7. Coût exploitation

| Item | Coût mensuel |
|---|---|
| Airtable Free | $0 (1200 records/base) |
| Airtable Team | $20/user/mois si besoin |
| Compute MiniMax 2.7 | ~$8/mois |
| **TOTAL Free** | **$8/mois** |

## 8. Graduation MUSE

3 semaines stable → PRD-AT-001 :
1. NocoDB self-hosted via Dokploy (API Airtable-compatible)
2. Migration CSV export → import
3. Update WORKFLOW.md `tracker.kind: nocodb`
4. Webhook natif NocoDB (pas de refresh 7j)

## 9. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| Rate limit 5 req/s | Moyenne | Queue + backoff |
| Webhook expiration silencieuse | Moyenne | Cron refresh 5j + polling backup |
| Free plan 1200 records | Moyenne | Archive Won/Lost → Notion |
| URL > 16000 chars | Faible | Switch POST body |

## 10. Hors-scope

- ❌ Pas de Airtable Automations (Symphony = orchestrateur)
- ❌ Pas de Airtable Interfaces (SDD-005 = UI cible)
- ❌ Pas de bi-sync Airtable ↔ ClickUp/Notion
- ❌ Pas d'auto-création records (Symphony lit + agent écrit)

---

*Adapter Airtable — Shadow A0 — L2 Business — Growth/Sales/Finance — 2026-05-14*
