# Symphony Adapter — Plane.so (L1 Shadow GTD)

> **Statut** : Shadow A0 — adapter Plane.so pour Symphony A'Space
> **Date** : 2026-05-13
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L1 Shadow Life OS — USS Cerritos (Holo Deck A2) — Méthode GTD
> **Mappage SDD** : référence SDD-008 §3.1 (équipage Cerritos : Mariner / Boimler / Tendi / Capt. Freeman / Rutherford)

## 1. Pourquoi Plane en premier

- **Plus proche de Linear** (GraphQL, similar state machine) → effort de port minimal depuis Symphony OSS
- **Pilier 3 du Shadow L1** (méthode GTD, cf. SDD-008)
- **URL active** : `https://app.plane.so/aspace-core/` — déjà en usage par Amadeus
- **Self-hosting possible** (Plane est open source) — chemin de graduation MUSE clair vers L1 souverain

## 2. Spécificités Plane.so vs Linear

| Aspect | Linear | Plane.so |
|---|---|---|
| API | GraphQL | REST (v1) + GraphQL partiel |
| Endpoint default | `https://api.linear.app/graphql` | `https://api.plane.so/api/v1/` |
| Auth | API key Bearer | API token header `X-API-Key` |
| Project concept | Project + Team | Workspace + Project |
| Issue concept | Issue | Issue (idem) |
| State concept | WorkflowState (Backlog/Todo/InProgress/Done/Cancelled) | State (Backlog/Unstarted/Started/Completed/Cancelled) |
| Cycles | Cycles (sprints) | **Cycles natifs** — alignés avec Baserow Warp Core W1-W12 |
| Modules | Projects | Modules (sub-groupes) |
| Labels | Labels | Labels |
| Webhooks | Yes (GraphQL subscriptions) | **Yes (REST webhooks)** — polling optionnel |

## 3. WORKFLOW.md type pour Plane

```yaml
---
tracker:
  kind: plane
  endpoint: "https://api.plane.so/api/v1"
  api_key: $PLANE_API_KEY
  workspace_slug: "aspace-core"
  project_id: $PLANE_PROJECT_LIFE_OS    # UUID du projet "Life OS" dans Plane
  active_states:
    - "Inbox"          # Capture par Mariner — quarantaine
    - "Next Actions"   # Clarify par Boimler → actionnable
    - "Today"          # Engage par Capt. Freeman — contrat du jour
  terminal_states:
    - "Done"
    - "Cancelled"
    - "Trash"
  state_mapping:
    inbox: "Inbox"
    next_actions: "Next Actions"
    in_progress: "Today"
    waiting_for: "Waiting For"
    done: "Done"
    cancelled: "Cancelled"

polling:
  interval_ms: 60000              # 1 min — Plane API rate-friendly

workspace:
  root: "/srv/aspace/workspaces/plane"

hooks:
  before_dispatch: |
    # Validation SOC : un ticket Plane sans label de couche est rejeté
    if ! echo "{{issue.labels | join: ','}}" | grep -qE '(@L0|@L1|@L2)'; then
      echo "ERROR: Ticket sans label de couche A'Space (@L0/@L1/@L2)"
      exit 1
    fi
  after_create: |
    # Sandbox Cerritos : aucun accès SSH au VPS depuis ce workspace
    chmod 700 .
    touch .symphony-cerritos-only

agent:
  max_concurrent_agents: 5         # Plane = L1, charge modérée
  max_turns: 10
  max_retry_backoff_ms: 180000

codex:
  command: "oh -p --output-format=stream-json"  # OpenHarness avec MiniMax 2.7
  turn_timeout_ms: 1800000          # 30 min max par turn

soc:
  schema_version: "1.0"
  default_domain: "Life_OS"
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

Tu es un A3 Compagnon de l'USS Cerritos opérant un ticket Plane.so.

Ton équipage selon l'étape GTD du ticket :
- **Inbox** (état `inbox`) : tu es **Mariner**. Tu captures sans juger.
- **Next Actions** (état `next_actions`) : tu es **Boimler**. Tu transformes en verbe d'action OU expulses vers Obsidian PARA si projet complexe.
- **Today** (état `in_progress`) : tu es **Capt. Freeman**. Tu engages le ticket du jour.

Ticket :
- **ID** : {{issue.identifier}}
- **Titre** : {{issue.title}}
- **Description** : {{issue.description}}
- **État** : {{issue.state}}
- **Labels** : {{issue.labels | join: ', '}}
- **Cycle** : (à enrichir via plane_rest tool si besoin)

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Tu disposes des outils :
- `plane_rest` : query/mutate Plane via REST (état, comments, attachments)
- `aspace_clara_cli` : pour invoquer une CLI A'Space (transformée depuis MCP)
- `aspace_donna_escalate` : si bloqué après 1 tour

**Règle d'or** : Si le ticket est un projet complexe (>1 step), tu n'execute PAS. Tu crée une note Obsidian PARA via `aspace_clara_cli obsidian-create-project` et mets le ticket en `Waiting For` avec lien vers la note.

{% if attempt %}
**Continuation attempt #{{attempt}}** — l'analyse précédente est dans le thread. Continue.
{% endif %}
```

## 4. Tracker Adapter — implémentation Plane

### 4.1 Operations requises

```python
class PlaneAdapter(TrackerAdapter):
    BASE_URL = "https://api.plane.so/api/v1"

    def fetch_candidate_issues(self) -> list[Issue]:
        # GET /workspaces/<slug>/projects/<id>/issues/?state__group=unstarted,started
        # Pagination via ?per_page=50&cursor=...
        ...

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        # GET /workspaces/<slug>/projects/<id>/issues/?state__name__in=<list>
        ...

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        # GET /workspaces/<slug>/projects/<id>/issues/<id>/ pour chaque
        # (Plane n'a pas de bulk get par ID — accepter le N+1 ou paralléliser)
        ...
```

### 4.2 Normalisation Plane → Issue

```python
def normalize(plane_issue: dict) -> Issue:
    return Issue(
        id=plane_issue["id"],
        identifier=f"PLN-{plane_issue['sequence_id']}",
        title=plane_issue["name"],
        description=plane_issue.get("description_html"),
        priority=PRIORITY_MAP.get(plane_issue.get("priority"), None),
        state=plane_issue["state_detail"]["name"],
        branch_name=None,  # Plane n'a pas de branch hint
        url=f"https://app.plane.so/{workspace_slug}/projects/{project_id}/issues/{plane_issue['id']}",
        labels=[l["name"].lower() for l in plane_issue.get("labels", [])],
        blocked_by=extract_blockers(plane_issue),
        created_at=parse_iso(plane_issue["created_at"]),
        updated_at=parse_iso(plane_issue["updated_at"]),
        soc_metadata=extract_soc_from_labels(plane_issue["labels"]),
        sla_constraints=extract_sla_from_custom_fields(plane_issue),
    )

PRIORITY_MAP = {
    "urgent": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
    "none": None,
}
```

### 4.3 Extraction SOC depuis labels Plane

Convention : les labels Plane portent les metadata SOC :
- `@L0`, `@L1`, `@L2` → couche A'Space
- `@deep-work`, `@brain-dead`, `@5-min` → énergie (Tendi labels)
- `domain:Growth`, `domain:Sales`, etc. → SOA target domain

### 4.4 Extraction SLA depuis Custom Fields Plane

Plane permet des custom fields. Convention :
- `sla_max_time_min` → integer → `max_execution_time_minutes`
- `sla_max_cost_usd` → float → `max_compute_budget_usd`
- `sla_max_retries` → integer → `max_retry_loops`

Si absent, defaults :
- `max_execution_time_minutes`: 60
- `max_compute_budget_usd`: 0.50 (MiniMax 2.7 ~= 2000 turns)
- `max_retry_loops`: 2

## 5. Webhooks Plane (optimisation polling)

Plane supporte les webhooks REST. Configuration :

```bash
curl -X POST "https://api.plane.so/api/v1/workspaces/aspace-core/webhooks/" \
  -H "X-API-Key: $PLANE_API_KEY" \
  -d '{
    "url": "http://symphony.aspace.local:3200/webhook/plane",
    "event_types": ["issue.created", "issue.updated", "issue.deleted"]
  }'
```

Symphony peut alors :
- Réduire `polling.interval_ms` à `300000` (5 min — backup)
- Réagir aux webhooks pour dispatch immédiat sur `issue.updated`
- Coût compute réduit (moins de polls vides)

## 6. Cycles Plane ↔ Baserow Warp Core

**Doctrine SDD-008** : Cycle Plane = 1 semaine W du Warp Core Baserow.

Mapping automatique au démarrage :
```python
def sync_plane_cycle_to_baserow_week():
    plane_cycle = plane.get_current_cycle(project_id)
    baserow_week = baserow.find_warp_core_week(matching_dates=plane_cycle.dates)
    # Tag les tickets Plane avec le label "warp:<W-N>"
    plane.bulk_add_label(plane_cycle.issues, f"warp:{baserow_week.id}")
```

→ Permet à Curie (A2 SNW Baserow) de voir l'état des tickets Plane sans switch de tool.

## 7. Coût exploitation Plane

| Item | Coût mensuel estimé |
|---|---|
| Plane cloud Free plan | $0 (5 membres, illimité workspaces) |
| Plane cloud Pro | $8/mois si besoin avancé |
| Plane self-hosted | $0 (Docker sur VPS) — cible MUSE H1 |
| Compute (MiniMax 2.7) | ~$5/mois avec ~50 tickets/mois × 1000 tokens moyen |
| **TOTAL** | **$0–13/mois** selon plan |

## 8. Graduation MUSE — Plane vers Self-Hosted

Critère SDD-008 : 3 semaines stable → PRD → 13ème Doctor.

**Trigger** : si pendant 3 semaines consécutives :
- < 5 incidents Symphony-Plane par semaine
- Coût compute < $5/semaine
- Taux Donna escalation < 5%

→ Promouvoir vers PRD-XXX (à définir hors veto SDD) :
1. Self-host Plane via Dokploy sur VPS aspace
2. Migration data (Plane export API → import self-host)
3. Update WORKFLOW.md `tracker.endpoint` vers self-host
4. Désactiver Plane Cloud webhook, activer self-host webhook

## 9. Risques spécifiques Plane

| Risque | Probabilité | Mitigation |
|---|---|---|
| API Plane breaking changes (jeune projet) | Moyenne | Pin version `/api/v1` strict + integration tests hebdo |
| Self-host Docker DB corruption | Faible | Backup quotidien Supabase (déjà SDD-001) |
| Webhook delivery loss | Moyenne | Polling fallback à 5 min de toute façon |
| Rate limit (Free plan) | Faible | Polling 1 min < limite Plane Free |

## 10. Build instructions (MVP)

```bash
# 1. Cloner Symphony OSS de printingpress.dev
git clone https://github.com/printingpress/symphony.git /srv/aspace/services/symphony
cd /srv/aspace/services/symphony

# 2. Implémenter PlaneAdapter (heritage TrackerAdapter de Symphony)
# Fichier : adapters/plane.py
# Suit le contrat §10 de symphony-base.spec.md

# 3. Créer le WORKFLOW.md
cp /home/amadeus/.shadow_a0/symphony/L1/WORKFLOW-plane.md /srv/aspace/services/symphony/WORKFLOW.md

# 4. Variables d'env
export PLANE_API_KEY=...
export PLANE_PROJECT_LIFE_OS=...
export MINIMAX_API_KEY=...

# 5. Test dry-run
symphony --dry-run --once

# 6. Daemon
symphony daemon &
# OU via systemd unit (à créer)
```

## 11. Hors-scope

- ❌ Pas de Plane Pages support (Plane a son propre wiki — utiliser Obsidian via adapter dédié)
- ❌ Pas de Plane Module → SDD mapping (modules sont en dehors du scope GTD)
- ❌ Pas de bi-directional sync Plane ↔ Linear (pas besoin — Plane est seul tracker L1 GTD)
- ❌ Pas d'auto-création de tickets Plane par Symphony (Symphony lit + agent écrit)

---

*Adapter Plane.so — Shadow A0 — Premier proof-of-concept Symphony A'Space — 2026-05-13*
*Modèle de référence pour les 6 autres adapters (Baserow, Obsidian, Affine, Airtable, ClickUp, Notion).*
