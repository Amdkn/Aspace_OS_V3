# Symphony Adapter — Obsidian (L1 Shadow Life OS)

> **Statut** : Shadow A0 — adapter Obsidian pour Symphony A'Space
> **Date** : 2026-05-14
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L1 Shadow Life OS — USS Enterprise (SDD-008 §3.3)
> **Mappage SDD** : SDD-008 §2 (Pilier 1 — Obsidian = PARA)
> **A2 Manager** : Picard (USS Enterprise)
> **Méthode** : **PARA** (Projects / Areas / Resources / Archives)
> **Spécificité** : Obsidian est **offline-first** — l'API est locale (Local REST API plugin)

## 1. Pourquoi Obsidian

- **Offline-first** — vault local, aucune dépendance cloud
- **Pilier 1 du Shadow L1** (méthode PARA, cf. SDD-008)
- **MANIFEST.md** — chaque P et A contient un YAML frontmatter lisible par Rick + 13th Doctor
- **Tasks plugin** — gestion de tâches inline avec statuts et dates
- **Dataview** — requêtes SQL-like sur les fichiers Markdown
- **Local REST API** — plugin d'Adam Coddington pour accès externe HTTPS
- **Graduation MUSE** → vault reste Obsidian + LiveSync Supabase (déjà souverain)

## 2. Le cas unique Obsidian

⚠️ **Obsidian n'est PAS un SaaS.** C'est un éditeur Markdown local avec un vault filesystem. L'adapter Symphony accède au vault via le plugin **Local REST API**.

| Aspect | Tracker classique | Obsidian |
|---|---|---|
| Issue = | Row/Ticket | **Tâche** (`- [ ] text`) ou **Note** (fichier .md) |
| State = | Status field | **Task status** (`- [ ]`, `- [x]`, `- [/]`) ou **YAML frontmatter** |
| Description = | Text field | **Contenu du fichier Markdown** |
| API = | REST cloud | **Local REST API plugin** (localhost HTTPS) |
| Location = | Cloud DB | **Fichier système local** (vault) |
| Sync = | Native | **LiveSync** plugin vers Supabase (optionnel) |

### Architecture d'accès

```
Symphony Daemon
    ↓ HTTPS (localhost:27124)
Local REST API plugin (Obsidian)
    ↓ Filesystem read/write
Obsidian Vault (local)
    ↓ LiveSync (optionnel)
Supabase CouchDB-compatible (remote backup)
```

## 3. WORKFLOW.md type pour Obsidian

```yaml
---
tracker:
  kind: obsidian
  endpoint: "https://localhost:27124"         # Local REST API plugin default port
  api_key: $OBSIDIAN_REST_API_KEY             # API key configuré dans le plugin
  vault_path: "/home/amadeus/vault-para"      # Path absolu du vault
  project_folder: "01_Projects"               # Dossier PARA Projects
  active_states:
    - "incubating"       # Picard — projet en gestation
    - "active"           # Picard — projet actif (cycle 12WY en cours)
  terminal_states:
    - "graduated"        # MUSE — promu en module Life Web OS
    - "archived"         # PARA — déplacé vers 04_Archives
  state_mapping:
    inbox: "incubating"
    next_actions: "active"
    in_progress: "active"
    waiting_for: "incubating"
    done: "graduated"
    cancelled: "archived"
  state_source: "frontmatter"                 # "frontmatter" ou "tasks"
  state_field: "muse_status"                  # Clé YAML dans le frontmatter

polling:
  interval_ms: 120000              # 2 min — local, pas de rate limit

workspace:
  root: "/srv/aspace/workspaces/obsidian"

hooks:
  before_dispatch: |
    # Validation : un projet PARA sans MANIFEST.md est rejeté
    manifest="{{issue.soc_metadata.manifest_path}}"
    if [ ! -f "$manifest" ]; then
      echo "ERROR: Projet PARA sans MANIFEST.md"
      exit 1
    fi
  after_create: |
    chmod 700 .
    touch .symphony-l1-para-only

agent:
  max_concurrent_agents: 2
  max_turns: 8
  max_retry_backoff_ms: 180000

codex:
  command: "oh -p --output-format=stream-json"
  turn_timeout_ms: 1200000

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

Tu es un A3 Compagnon du USS Enterprise opérant un projet PARA dans Obsidian.

Tu es sous le commandement de **Picard (A2 Enterprise)**. Le système PARA structure le vault :
- **01_Projects** : cycles 12WY actifs (tu opères ici)
- **02_Areas** : 8 Domaines Roue de Vie + 8 Domaines Business (maintenance continue)
- **03_Resources** : knowledge base, templates, références
- **04_Archives** : projets terminés, notes obsolètes

Projet PARA :
- **ID** : {{issue.identifier}}
- **Titre** : {{issue.title}}
- **Description** : {{issue.description}}
- **Statut MUSE** : {{issue.state}}
- **Domaine** : {{issue.soc_metadata.target_soa_domain}}
- **Rock Baserow** : {{issue.soc_metadata.rock_baserow_link}}
- **Cycle** : {{issue.soc_metadata.cycle}}

Contraintes SLA :
- **Temps max** : {{issue.sla_constraints.max_execution_time_minutes}} min
- **Coût max** : ${{issue.sla_constraints.max_compute_budget_usd}}

Outils : `obsidian_rest`, `aspace_clara_cli`, `aspace_donna_escalate`

**Règle Picard** : chaque dossier Projet/Area DOIT contenir un `MANIFEST.md` avec YAML frontmatter valide. Si absent, crée-le.

**Règle SDD-008** : le MANIFEST.md est l'interface lue par Rick + 13ème Doctor SANS intervention humaine. Format :

```yaml
---
rock_baserow: <lien Baserow>
cycle: H1-C2
domaine_de_vie: LD04_Cognition
muse_status: incubating | active | graduated
last_review: 2026-05-14
guardian_a3: <nom>
---
```

{% if attempt %}
**Continuation attempt #{{attempt}}**
{% endif %}
```

## 4. Tracker Adapter — implémentation Obsidian

### 4.1 Local REST API plugin

Le plugin **Local REST API** expose :

| Endpoint | Méthode | Usage |
|---|---|---|
| `/vault/{path}` | GET | Lire le contenu d'un fichier |
| `/vault/{path}` | PUT | Écrire/mettre à jour un fichier |
| `/vault/` | GET | Lister les fichiers |
| `/search/` | POST | Recherche full-text dans le vault |
| `/search/simple/` | POST | Recherche simplifiée |
| `/active/` | GET | Fichier actif dans l'éditeur |
| `/commands/` | POST | Exécuter une commande Obsidian |

**Auth** : API key dans le header `Authorization: Bearer <key>`.
**TLS** : HTTPS auto-signé sur `localhost:27124`.

### 4.2 Operations requises

```python
class ObsidianAdapter(TrackerAdapter):
    """
    Adapter pour Obsidian via le plugin Local REST API.
    
    Deux modes de tracking :
    1. 'frontmatter' — lit le YAML frontmatter des MANIFEST.md dans les dossiers PARA
    2. 'tasks' — lit les tâches Obsidian Tasks (- [ ] / - [x]) via Dataview
    """

    def __init__(self, config: ServiceConfig):
        self.endpoint = config.tracker.endpoint  # https://localhost:27124
        self.api_key = config.tracker.api_key
        self.vault_path = config.tracker.vault_path
        self.project_folder = config.tracker.project_folder or "01_Projects"
        self.state_source = config.tracker.state_source or "frontmatter"
        self.state_field = config.tracker.state_field or "muse_status"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        # TLS: accept self-signed cert
        self.verify_ssl = False

    def fetch_candidate_issues(self) -> list[Issue]:
        if self.state_source == "frontmatter":
            return self._fetch_from_manifests()
        return self._fetch_from_tasks()

    def _fetch_from_manifests(self) -> list[Issue]:
        # List all MANIFEST.md files in project_folder
        resp = requests.get(
            f"{self.endpoint}/vault/{self.project_folder}/",
            headers=self.headers, verify=self.verify_ssl,
        )
        resp.raise_for_status()
        files = resp.json().get("files", [])
        
        issues = []
        for f in files:
            if not f.endswith("MANIFEST.md"):
                continue
            # Read the MANIFEST.md
            content_resp = requests.get(
                f"{self.endpoint}/vault/{f}",
                headers=self.headers, verify=self.verify_ssl,
            )
            content_resp.raise_for_status()
            content = content_resp.text
            frontmatter = parse_yaml_frontmatter(content)
            state = frontmatter.get(self.state_field, "unknown")
            if state in self.config.tracker.active_states:
                issues.append(self._normalize_manifest(f, frontmatter, content))
        return issues

    def _fetch_from_tasks(self) -> list[Issue]:
        # Use Dataview query via Local REST API /search/
        query = 'TASK FROM "01_Projects" WHERE !completed'
        resp = requests.post(
            f"{self.endpoint}/search/",
            headers=self.headers, verify=self.verify_ssl,
            json={"query": query, "contextLength": 200},
        )
        resp.raise_for_status()
        results = resp.json()
        return [self._normalize_task(r) for r in results]

    def fetch_issues_by_states(self, state_names: list[str]) -> list[Issue]:
        all_issues = self.fetch_candidate_issues()
        return [i for i in all_issues if i.state in state_names]

    def fetch_issue_states_by_ids(self, issue_ids: list[str]) -> dict[str, str]:
        all_issues = self.fetch_candidate_issues()
        return {i.id: i.state for i in all_issues if i.id in issue_ids}
```

### 4.3 Normalisation MANIFEST.md → Issue

```python
def _normalize_manifest(self, filepath: str, fm: dict, content: str) -> Issue:
    project_name = filepath.split("/")[-2]  # Parent folder name
    return Issue(
        id=sanitize_workspace_key(filepath),
        identifier=f"OB-{sanitize_workspace_key(project_name)[:12]}",
        title=project_name,
        description=content,                 # Full MANIFEST.md content
        priority=None,
        state=fm.get(self.state_field, "unknown"),
        branch_name=None,
        url=None,                            # Local file — no URL
        labels=extract_labels_from_frontmatter(fm),
        blocked_by=[],
        created_at=None,
        updated_at=parse_iso(fm.get("last_review")),
        soc_metadata=SOCMetadata(
            target_soa_domain=fm.get("domaine_de_vie"),
            forbidden_lexicon=[],
            context_pack_url=fm.get("rock_baserow"),
            manifest_path=filepath,
            cycle=fm.get("cycle"),
            rock_baserow_link=fm.get("rock_baserow"),
        ),
        sla_constraints=SLAConstraints(
            max_execution_time_minutes=fm.get("sla_max_time", 60),
            max_compute_budget_usd=fm.get("sla_max_cost", 0.50),
            max_retry_loops=fm.get("sla_max_retries", 2),
        ),
    )
```

### 4.4 MANIFEST.md — format standard SDD-008

```yaml
---
rock_baserow: https://baserow.io/database/284361/table/955426/row/42
cycle: H1-C2
domaine_de_vie: LD04_Cognition
muse_status: incubating
last_review: 2026-05-14
guardian_a3: Spock
sla_max_time: 60
sla_max_cost: 0.50
---

# Project: Cognitive Dashboard

## Objectif
Créer un dashboard de suivi cognitif...

## Rocks associés
- Rock L1: "Build Cognitive Tracker" (W3-W6)
```

## 5. Mode Tasks (alternatif)

En mode `state_source: tasks`, l'adapter lit les tâches Obsidian Tasks :

```markdown
- [ ] Configurer LiveSync #L1 📅 2026-05-20 ⏫
- [/] Rédiger MANIFEST.md pour Cognition #L1
- [x] Installer Local REST API plugin #L0 ✅ 2026-05-10
```

Mapping :
- `- [ ]` → `inbox`
- `- [/]` → `in_progress`
- `- [x]` → `done`

Ce mode est utile pour le **micro-tracking** (tâches individuelles) vs le mode frontmatter qui track les **projets**.

## 6. LiveSync → Supabase (optionnel)

Si LiveSync est configuré, le vault est synchronisé en temps réel vers une instance CouchDB-compatible (Supabase ou PouchDB).

Symphony **n'interagit pas avec LiveSync**. Il lit le vault local via le plugin REST API. LiveSync est une couche de backup/sync transparente.

## 7. Coût exploitation

| Item | Coût mensuel |
|---|---|
| Obsidian | $0 (gratuit pour usage personnel) |
| Local REST API plugin | $0 (community plugin) |
| LiveSync → Supabase | $0 (inclus dans SDD-001 Supabase) |
| Compute MiniMax 2.7 | ~$2/mois (PARA = faible volume) |
| **TOTAL** | **$2/mois** |

## 8. Graduation MUSE

Obsidian est **déjà souverain** (offline-first, vault local). La graduation MUSE signifie :
1. ✅ Vault PARA structuré avec MANIFEST.md dans chaque P et A
2. ✅ LiveSync opérationnel vers Supabase
3. ✅ Dataview queries stables pour reporting
4. ✅ Symphony adapter stable 3 semaines
5. → **Promotion** : vault devient la **source de vérité PARA** pour L1 + L2 (poupée russe SDD-010 §5.4)

## 9. Risques

| Risque | Probabilité | Mitigation |
|---|---|---|
| Local REST API plugin instable | Faible | Pin version + alternative: filesystem direct |
| Obsidian doit être ouvert | **Haute** | Le plugin REST nécessite Obsidian running → systemd headless ou always-open |
| Self-signed TLS cert warnings | Faible | `verify_ssl=False` + Tailscale internal |
| MANIFEST.md format non-respecté | Moyenne | Validation Zod avant dispatch |
| Vault corruption (concurrent writes) | Faible | Symphony = read-mostly, agent writes via tool |

## 10. Hors-scope

- ❌ Pas de Obsidian Publish (vault privé)
- ❌ Pas de Obsidian Canvas (Affine Edgeless = le canvas tool)
- ❌ Pas de bi-sync Obsidian ↔ Notion (graduation Notion → Obsidian = migration one-way)
- ❌ Pas de Obsidian Git sync (LiveSync Supabase = le sync layer)
- ❌ Pas de template Templater automation (Symphony = orchestrateur)
- ❌ Pas d'auto-création notes (Symphony lit + agent écrit via `obsidian_rest`)

---

*Adapter Obsidian — Shadow A0 — L1 Life OS — PARA — 2026-05-14*
*Le moins urgent car déjà souverain. Le plus important car c'est la mémoire.*
