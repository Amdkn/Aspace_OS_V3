# Symphony Adapter — Affine (L1 Shadow Life OS)

> **Statut** : Shadow A0 — adapter Affine pour Symphony A'Space
> **Date** : 2026-05-14
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L1 Shadow Life OS — USS Protostar (SDD-008 §3.4)
> **Mappage SDD** : SDD-008 §2 (Pilier 4 — Affine = D.E.A.L)
> **A2 Manager** : Holo Janeway (USS Protostar)
> **Méthode** : **D.E.A.L** (Define / Eliminate / Automate / Liberate)
> **Mode spécial** : Edgeless = Blueprints d'App-Store pour le Life Web OS

## 1. Pourquoi Affine

- **Mode Edgeless** — infinite canvas = atelier de Blueprints (futur iframe Life Web OS)
- **Database Blocks** — Kanban/Table structuré dans le canvas
- **Pilier 4 du Shadow L1** (méthode DEAL, cf. SDD-008)
- **URL active** : `https://app.affine.pro/workspace/ef927d3a-5be0-41ed-b639-829b7f74939b/`
- **Open source** — self-hosting facile (Docker)
- **Pont L0↔L1** — Affine fait le pont entre pensée Beth (L1) et matérialisation Rick (L0)
- **Graduation MUSE** → Affine self-hosted sur VPS

## 2. Le cas atypique Affine

⚠️ **Affine n'est PAS un tracker classique.** C'est un **document-first canvas** avec des Database Blocks intégrés. L'adapter Symphony doit s'adapter :

| Aspect | Tracker classique | Affine |
|---|---|---|
| Issue = | Row/Ticket | **Database Block row** dans une Page ou Edgeless |
| State = | Status field | **Status column** dans le Database Block |
| Description = | Text field | **Page content** (blocks structurés) |
| API = | REST/GraphQL stable | **GraphQL** (app.affine.pro/graphql) + **BlockSuite SDK** |
| Maturity = | Production | **WIP** — API encore en évolution |

### API disponible

| Interface | URL | Usage |
|---|---|---|
| GraphQL API | `https://app.affine.pro/graphql` | Workspace, Pages, metadata |
| BlockSuite SDK | `@blocksuite/affine-*` | CRUD blocks (programmatic) |
| REST (backend) | Dépend du self-hosted setup | File ops, binary data |

## 3. WORKFLOW.md type pour Affine

```yaml
---
tracker:
  kind: affine
  endpoint: "https://app.affine.pro/graphql"
  api_key: $AFFINE_API_TOKEN
  workspace_id: "ef927d3a-5be0-41ed-b639-829b7f74939b"
  database_block_id: $AFFINE_DB_DEAL        # ID du Database Block qui sert de tracker
  active_states:
    - "Define"           # Dal — qu'est-ce que cet outil/processus ?
    - "Eliminate"        # Rok-Tahk — est-ce nécessaire ?
    - "Automate"         # Zero — peut-on automatiser ?
  terminal_states:
    - "Liberated"        # Gwyn — l'humain n'a plus besoin de le faire
    - "Kept Manual"      # Décision consciente de garder manuel
    - "Archived"
  state_mapping:
    inbox: "Define"
    next_actions: "Eliminate"
    in_progress: "Automate"
    waiting_for: "Automate"
    done: "Liberated"
    cancelled: "Kept Manual"
  state_column: "DEAL Status"

polling:
  interval_ms: 300000              # 5 min — API WIP, polling conservateur

workspace:
  root: "/srv/aspace/workspaces/affine"

hooks:
  before_dispatch: |
    # Validation : un item DEAL sans étape est rejeté
    state="{{issue.state}}"
    if [ "$state" != "Define" ] && [ "$state" != "Eliminate" ] && [ "$state" != "Automate" ]; then
      echo "ERROR: Item DEAL sans étape valide (Define/Eliminate/Automate)"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l1-deal-only

agent:
  max_concurrent_agents: 2         # DEAL = travail réflexif, pas volume
  max_turns: 8
  max_retry_backoff_ms: 300000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 1800000

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

Tu es un A3 Compagnon du USS Protostar opérant un item DEAL dans Affine.

Tu es sous le commandement de **Holo Janeway (A2 Protostar)**. La méthode DEAL :
- **Define** (tu es **Dal**) : Qu'est-ce que cet outil/processus ? Documenter clairement.
- **Eliminate** (tu es **Rok-Tahk**) : Est-ce nécessaire ? Si non → Liberated immédiatement.
- **Automate** (tu es **Zero**) : Peut-on l'automatiser ? Si oui → créer le Blueprint Edgeless.
- **Liberate** (tu es **Gwyn**) : L'humain n'a plus besoin de le faire. Archiver + documenter.

Item DEAL :
- **ID** : {{issue.identifier}}
- **Titre** : {{issue.title}}
- **Description** : {{issue.description}}
- **Étape DEAL** : {{issue.state}}

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Outils : `affine_graphql`, `aspace_clara_cli`, `aspace_donna_escalate`

**Règle Holo Janeway** : si un processus passe le test "Eliminate" et mérite "Automate", tu DOIS créer un Blueprint Edgeless (schéma iframe futur) dans Affine avant de marquer Liberated.

**Règle SDD-008** : tout outil Shadow schématisé en Blueprint Edgeless = futur iframe Life Web OS. Ryan (A3, 13ème Doctor) codera le connecteur souverain à partir de ce schéma.

{% if attempt %}
**Continuation attempt #{{attempt}}**
{% endif %}
```

## 4. Tracker Adapter — implémentation Affine

### 4.1 Stratégie d'accès

Affine expose **2 interfaces complémentaires** :

1. **GraphQL API** (`/graphql`) — pour lister workspaces, pages, metadata
2. **BlockSuite store** — pour CRUD sur les Database Blocks (rows/cells)

Le TrackerAdapter utilise le GraphQL pour la découverte et le BlockSuite SDK (via REST bridge) pour les opérations CRUD.

### 4.2 Operations requises

```python
class AffineAdapter(TrackerAdapter):
    """
    Adapter pour Affine.pro — utilise GraphQL pour workspace/page ops
    et une REST bridge pour les Database Block rows.
    
    Note: L'API Affine est encore en évolution (WIP).
    Ce contract est basé sur l'API au 2026-05.
    """

    def __init__(self, config: ServiceConfig):
        self.endpoint = config.tracker.endpoint  # GraphQL endpoint
        self.token = config.tracker.api_key
        self.workspace_id = config.tracker.workspace_id
        self.db_block_id = config.tracker.database_block_id
        self.state_column = config.tracker.state_column or "DEAL Status"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def fetch_candidate_issues(self) -> list[Issue]:
        # GraphQL query to list Database Block rows
        query = """
        query GetDatabaseRows($workspaceId: String!, $blockId: String!) {
            workspace(id: $workspaceId) {
                block(id: $blockId) {
                    ... on DatabaseBlock {
                        rows {
                            id
                            cells {
                                columnId
                                columnName
                                value
                            }
                        }
                    }
                }
            }
        }
        """
        resp = requests.post(
            self.endpoint,
            headers=self.headers,
            json={"query": query, "variables": {
                "workspaceId": self.workspace_id,
                "blockId": self.db_block_id,
            }},
        )
        resp.raise_for_status()
        rows = resp.json()["data"]["workspace"]["block"]["rows"]
        issues = [self.normalize(r) for r in rows]
        # Filter by active_states client-side
        return [i for i in issues if i.state in self.config.tracker.active_states]

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        all_issues = self.fetch_candidate_issues()
        return [i for i in all_issues if i.state in state_names]

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        all_issues = self.fetch_candidate_issues()
        return {i.id: i.state for i in all_issues if i.id in issue_ids}
```

### 4.3 Normalisation Affine → Issue

```python
def normalize(self, row: dict) -> Issue:
    cells = {c["columnName"]: c["value"] for c in row["cells"]}
    return Issue(
        id=row["id"],
        identifier=f"AF-{row['id'][:8]}",
        title=cells.get("Name", cells.get("Title", "Untitled")),
        description=cells.get("Description", None),
        priority=None,                       # Affine Database Blocks: pas de priority native
        state=cells.get(self.state_column, "Unknown"),
        branch_name=None,
        url=f"https://app.affine.pro/workspace/{self.workspace_id}/{row['id']}",
        labels=extract_labels_from_cells(cells),
        blocked_by=[],
        created_at=None,                     # Affine: pas de created_at sur les rows
        updated_at=None,
        soc_metadata=extract_soc_from_cells(cells),
        sla_constraints=extract_sla_from_cells(cells),
    )
```

### 4.4 Extraction SOC / SLA depuis cells

| Cell (Column) | Usage | Default |
|---|---|---|
| `DEAL Status` | State (Define/Eliminate/Automate/Liberated) | — |
| `Blueprint Type` | `iframe`, `cli`, `agent`, `manual` | `manual` |
| `Target Ryan` | Boolean — prêt pour Ryan (13th Doctor) | `false` |
| `SLA Max Time` | Number | 60 |
| `SLA Max Cost` | Number | 0.50 |

## 5. Mode Edgeless — Blueprints

Le **mode Edgeless** d'Affine est un infinite canvas. Les Blueprints DEAL y sont créés comme des groupes visuels :

```
┌──────────────────────────────────────┐
│  Blueprint: "Task Capture → Plane"   │
│  ┌──────┐  →  ┌──────┐  →  ┌──────┐│
│  │Trigger│     │ CLI  │     │Plane │ │
│  │Hotkey │     │Clara │     │Inbox │ │
│  └──────┘     └──────┘     └──────┘ │
│  Status: Automate                    │
│  Target: iframe in Life Web OS       │
└──────────────────────────────────────┘
```

L'agent (Zero) crée ces Blueprints via `affine_graphql` tool. Quand `Target Ryan = true`, le Blueprint est prêt pour codification en connecteur souverain.

## 6. Pas de webhooks — Polling pur

Affine Cloud n'offre **pas de webhooks**. Polling à 5 min.

Self-hosted Affine pourrait exposer des hooks custom via le backend Express — à évaluer post-graduation MUSE.

## 7. Coût exploitation

| Item | Coût mensuel |
|---|---|
| Affine Cloud Free | $0 (10 membres, unlimited pages) |
| Affine Cloud Pro | $7/user/mois |
| Affine self-hosted | $0 (Docker) — cible MUSE |
| Compute MiniMax 2.7 | ~$2/mois (DEAL = volume très léger) |
| **TOTAL Free** | **$2/mois** |

## 8. Graduation MUSE

3 semaines stable → PRD-AF-001 :
1. Affine self-hosted via Dokploy (Docker compose — déjà open source)
2. Migration : Affine export → import self-host
3. Activation hooks custom backend
4. Update WORKFLOW.md endpoint vers self-host

## 9. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| API WIP / breaking changes | **Haute** | Pin version + integration tests hebdo |
| GraphQL schema instable | Haute | Fallback REST bridge si dispo |
| Database Block API limitée | Moyenne | Client-side filtering acceptable (DEAL = faible volume) |
| Pas de created_at / updated_at | Moyenne | Track en mémoire Symphony |
| Edgeless blocks non-queryable via API | Moyenne | Blueprints = convention, pas requête |

## 10. Hors-scope

- ❌ Pas de AI integration Affine (Symphony = orchestrateur)
- ❌ Pas de Edgeless programmatic rendering (Blueprints = convention visuelle)
- ❌ Pas de sync Affine ↔ Obsidian (outils complémentaires, pas miroir)
- ❌ Pas de multi-Database Block tracking (1 DB Block = 1 DEAL tracker)
- ❌ Pas d'auto-création blocks (Symphony lit + agent écrit)

---

*Adapter Affine — Shadow A0 — L1 Life OS — DEAL Blueprints — 2026-05-14*
*Le pont entre la pensée Beth (L1) et la matérialisation Rick (L0).*
