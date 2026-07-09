# Symphony Adapter — Supabase (L2 Shadow Observability)

> **Statut** : Shadow A0 — adapter Supabase pour Symphony A'Space
> **Date** : 2026-07-03
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L2 Shadow Business OS — Observability slot (SDD-009 §5.2)
> **Slot primaire** : **Observability** (méta-état Symphony) + **Source-of-truth substitué**
> **A2 Managers** : Cerritos — canon Mère §3.2 re-ratifié A+ 2026-07-03 : Mariner/Capture → Boimler/Clarify (handoff→next action + plan + sister ADR) → Rutherford/Organize (router interne frameworks Morty 12WY/PARA/GTD/DEAL) → Tilly/Review (vetos Beth + sobriété Rick, bypass = compressions temporelles A0/A+ uniquement) → Freeman/Engage (transition L1↔L2)
> **A3 Squads** : Lower Deck — orchestre le bus sémantique `40_SYMPHONY_BUS/`

## 1. Pourquoi Supabase (L2 Observability)

- **Source-of-truth canonique pour le meta-état** — `symphony_state` table = persistance durable de state.json
- **Service-role via MCP** — seul canal D5-receipté contre la 401 env-vars (cf. `supabase-specifics.md`)
- **Sidecar sync pattern** — `pending_upserts.ndjson` → MCP drain = eventuel consistency, idempotent
- **RLS-by-default** — anonym read-only + service_role write isolates data plane
- **Graduation MUSE** → self-hosted Supabase + edge functions si scale-out

## 2. Spécificités Supabase vs Airtable/Notion

| Aspect | Airtable | Notion | Supabase |
|---|---|---|---|
| API | REST v0 | REST v1 (paginated) | **PostgREST v1** |
| Auth | Bearer PAT | Bearer PAT | **Bearer anon OR service_role** |
| Project concept | Base + Table | Workspace + Page | **Project + Schema + Table** |
| Issue concept | Record | Page | **Row** |
| State concept | Single Select field | Status property | **`status text` column** |
| Webhooks | REST 7j | REST | **DB triggers → pg_notify → HTTP webhook** |
| Rate limit | 5 req/s/base | 3 req/s | **100 req/s/projet** |
| Pagination | offset 100/page | cursor | **cursor via Range header** |
| Write path | Airtable UI/automation | Notion UI/integration | **`mcp__supabase__execute_sql` service_role** |
| Storage relation | Linked records | Relations DB | **PG foreign keys + jsonb** |
| Auth user | None (API key auth) | Workspace members | **anon + authenticated + service_role** |

## 3. WORKFLOW.md type pour Supabase

```yaml
---
tracker:
  kind: supabase
  endpoint: "https://hjweyhpmrxqsxfbibsnc.supabase.co/rest/v1"
  api_key: $SUPABASE_LIFE_OS_ANON_KEY
  project_id: hjweyhpmrxqsxfbibsnc
  table_id: symphony_state
  active_states:
    - "ACTIVE"
    - "INIT"
  terminal_states:
    - "BLOCKED"
    - "DONE"
  state_mapping:
    inbox: "INIT"
    next_actions: "ACTIVE"
    in_progress: "ACTIVE"
    waiting_for: "BLOCKED"
    done: "DONE"
    cancelled: "BLOCKED"
  state_field: "status"

polling:
  interval_ms: 300000              # 5 min (same as Airtable)

workspace:
  root: "/srv/aspace/workspaces/supabase"

hooks:
  before_dispatch: |
    if [ -z "{{issue.soc_metadata.target_soa_domain}}" ]; then
      echo "ERROR: Row sans domaine SOA assigné"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l2-observability-only

agent:
  max_concurrent_agents: 1    # observability = single-stream
  max_turns: 5
  max_retry_backoff_ms: 120000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 2400000

soc:
  schema_version: "1.0"
  default_domain: "Observability"
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

upstream_sink:
  sidecar: "40_SYMPHONY_BUS/pending_upserts.ndjson"
  drain_cadence_sec: 300
```

## 4. Tracker Adapter — impl Supabase

### 4.1 Operations requises

```python
from mcp__supabase__execute_sql import execute_sql
from mcp__supabase__list_tables import list_tables

class SupabaseAdapter(TrackerAdapter):
    BASE_URL = "https://hjweyhpmrxqsxfbibsnc.supabase.co/rest/v1"

    def __init__(self, config: ServiceConfig):
        self.anon_key = config.tracker.api_key
        self.project_id = config.tracker.project_id
        self.table_id = config.tracker.table_id  # "symphony_state"
        self.state_field = config.tracker.state_field or "status"

    def fetch_candidate_issues(self) -> list[Issue]:
        # D5-receipted 2026-07-03 : use MCP execute_sql, not REST
        result = execute_sql(
            project_id=self.project_id,
            query=f'SELECT * FROM public.{self.table_id} WHERE {self.state_field} IN (\'ACTIVE\',\'INIT\')'
        )
        return [self.normalize(r) for r in result]

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        states_csv = ",".join(f"'{s}'" for s in state_names)
        result = execute_sql(
            project_id=self.project_id,
            query=f'SELECT * FROM public.{self.table_id} WHERE {self.state_field} IN ({states_csv})'
        )
        return [self.normalize(r) for r in result]

    def normalize(self, record: dict) -> Issue:
        return Issue(
            id=record["session_id"],
            identifier=f"SYM-{record['session_id'][:8]}",
            title=f"Symphony state @ {record['week']}/{record['stage']}",
            description=record.get("raw_input_preview", "")[:200],
            priority=None,
            state=record[self.state_field],
            branch_name=None,
            url=f"https://supabase.com/dashboard/project/{self.project_id}/editor/{record['session_id']}",
            labels=[record["cycle"], record["week"], record["agent_id"]],
            blocked_by=[],
            created_at=record["updated_at"],
            updated_at=record["updated_at"],
            soc_metadata={"target_soa_domain": "Observability"},
            sla_constraints={},
        )
```

### 4.2 Idempotent upsert (service_role path)

```python
def upsert_issue(self, issue: Issue) -> None:
    """D5-receipted 2026-07-03 : service_role via MCP execute_sql is the only path that works.

    REST v1 curl with anon/PAT env vars returns HTTP 401.
    All writes MUST go through this method.
    """
    payload = json.dumps(issue_to_payload(issue), ensure_ascii=False)
    sql = f"""
    INSERT INTO public.{self.table_id} (session_id, status, week, stage, agent_path, ...)
    VALUES (...)
    ON CONFLICT (session_id) DO UPDATE SET status = EXCLUDED.status, ...
    RETURNING session_id, updated_at
    """
    execute_sql(project_id=self.project_id, query=sql)
```

## 5. Sidecar Sync Pattern (key innovation)

The Symphony Bus writes to a local NDJSON sidecar (`pending_upserts.ndjson`), which is periodically drained into Supabase via `mcp__supabase__execute_sql`.

**Why sidecar?** REST v1 curl returns 401 with env-var credentials. The MCP `execute_sql` is the D5-receipted write path. We don't want to couple every state_writer call to a network round-trip — local file append is atomic, best-effort, network-agnostic.

**Drain loop (R3)** : a scheduled task reads each NDJSON line, validates against schema, invokes the idempotent upsert, and rotates the sidecar file.

## 6. Matrice 3×8 Supabase (Observability)

| Domaine | Statut | Squad |
|---|---|---|
| **Observability** (meta) | 🟢 PLEIN | Lower Deck (Cerritos) |
| **People** (LD06) | 🟡 partial | (future: people_pipeline via RLS view) |
| **Health** (LD03) | 🟡 partial | (future: rls_health_journal) |
| Growth | 🌙 dormant | — |
| Sales | 🌙 dormant | — |
| Finance | 🌙 dormant | — |
| Ops | 🌙 dormant | — |
| Product | 🌙 dormant | — |
| IT | 🌙 dormant | — |
| Legal | 🌙 dormant | — |

Note : only `symphony_state` table active today. Growth/Sales/Finance stay on Airtable (proven pattern).

## 7. Coût exploitation

| Item | Coût mensuel |
|---|---|
| Supabase Cloud Free | $0 (500 MB, 50k rows) |
| Compute MCP | ~$0 (mcp__supabase__execute_sql = free tool runtime) |
| Sidecar storage | ~0 (NDJSON evanescent) |
| **TOTAL** | **$0/mois** |

## 8. Graduation MUSE

3 semaines stable → PRD-SB-001 :
1. Self-host Supabase via Docker (API-compatible)
2. Migrate `symphony_state` schema via pg_dump/restore
3. Add 5 more 12WY tables (fw_12wy, ld01-08) wired through sidecar
4. Replace NDJSON sidecar with pg_notify (realtime)

## 9. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| 401 curl anomaly persists | Moyenne | Use only `mcp__supabase__execute_sql` for writes |
| Apostrophe corruption in raw_text | Elevée (D6 #NEW) | Sanitize on sidecar write |
| Sidecar grows unbounded | Moyenne | Drainer toutes les 5 min via cron-like |
| Service-role key leak | Moyenne | Use MCP internal key, not env var |
| MCP tool unavailable | Faible | Fallback: sidecar accumulates, retry on MCP restore |

## 10. Hors-scope

- ❌ Tracking business records (Airtable wins — Symphont = meta only)
- ❌ User authentication flows (use Supabase Auth, not Symphony adapter)
- ❌ Storage buckets (use raw Supabase Storage SDK, not adapter)
- ❌ Realtime subscriptions (use Supabase Realtime SDK)
- ❌ Edge functions (R3 swarm will handle separately)

---

*Adapter Supabase — Shadow A0 — L2 Observability — 2026-07-03 — sister: `supabase-specifics.md` standard*
