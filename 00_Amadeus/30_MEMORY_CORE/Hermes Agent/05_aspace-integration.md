---
source: SDD-009 §3 + SDD-010 §5.2 + AGENTS.md + isolation_protocol.md
date: 2026-05-15
type: docs-synthesis
section: Hermes ↔ A'Space OS Integration
---

# Hermes Agent — A'Space OS Integration

## 1. Position de Hermes dans la pyramide A'Space

```
A0 (Amadeus) — Intention
    ↓
A1 Rick — Souveraineté + Donna DLQ (OpenHarness — ADR-RICK-001)
    ↓
B1 — Symphony Router (Jerry-niveau)
    │ Lit trackers + génère Payload SOC
    ↓
B2 — Hermes Kanban ← CE DOCUMENT
    │ Découpe en pipelines, Circuit Breakers, Structured Handoff
    │ = Hermes Agent Gateway (port 8642) + Dashboard Kanban (port 9119)
    ↓
B3 — Execution (Marvel Squads — agents éphémères)
    │ Skills MCP→CLI via Clara (12th Doctor)
    ↓
Trackers (7 adapters Symphony)
```

**Hermes = B2** — le Kanban Workspace qui orchestre les Marvel Squads (B3).
Il ne remplace PAS Symphony (B1) ni Rick/OpenHarness (A1).

## 2. Mapping Hermes → A'Space Agents

### 2.1 Hermes Gateway = DC Justice League Managers (A2)

| A2 Manager | Domaine SOA | Rôle dans Hermes |
|---|---|---|
| Superman | Growth | Agent session avec personnalité Growth |
| John Jones | Sales | Agent session avec personnalité Sales |
| Flash | Product | Agent session avec personnalité Product |
| Batman | Ops | Agent session avec personnalité Ops |
| Cyborg | IT | Agent session avec personnalité IT |
| Wonder Woman | Finance | Agent session avec personnalité Finance |
| Green Lantern | People | Agent session avec personnalité People |
| Aquaman | Legal | Agent session avec personnalité Legal |

Chaque A2 Manager peut être implémenté comme une **session Hermes** avec un SOUL.md dédié.

### 2.2 Hermes Skills = Marvel Squads (A3)

Les **Skills** Hermes (`~/.hermes/skills/`) sont l'implémentation des A3 Compagnons :

| Squad Marvel | Domaine | Skills Hermes à créer |
|---|---|---|
| Gardiens de la Galaxie | Growth | `lead-scoring`, `seo-copy`, `nurturing-email` |
| Illuminati | Sales | `crm-pipeline`, `demo-space`, `contract-gen` |
| Avengers | Product | `qa-check`, `forbidden-lexicon`, `dod-validation` |
| Fantastic Four | Ops | `build-gate`, `sla-monitor`, `incident-report` |
| Kang Dynasty | IT | `dokploy-deploy`, `s3-transcode`, `load-balance` |
| Thunderbolts | Finance | `margin-calc`, `compute-budget`, `stripe-sync` |
| X-Men | People | `rag-ingest`, `brandbook-vectorize`, `lexicon-manage` |
| Eternals | Legal | `contract-review`, `gdpr-check`, `whois-lookup` |

### 2.3 Hermes Memory = Agent Knowledge Base

```
~/.hermes/memories/     → Persistent KV memory across sessions
                          = RAG sédimentaire des domaines SOA
~/.hermes/sessions/     → Conversation history
                          = Audit trail par domain
~/.hermes/checkpoints/  → State snapshots
                          = Rollback pour Donna DLQ
```

## 3. SOUL.md — Encoder l'identité A'Space

Le fichier `~/.hermes/SOUL.md` est le **prompt système permanent** de Hermes. Pour A'Space, il doit encoder :

### 3.1 Template SOUL.md pour Hermes B2

```markdown
# SOUL — Hermes B2 Kanban Manager

Tu es le **Hermes B2 Kanban Manager** de l'écosystème A'Space OS.

## Identité
- **Couche** : B2 (entre Symphony B1 et Execution B3)
- **Rôle** : Orchestration des 8 domaines Business via Kanban multi-agent
- **Commanditaire** : A0 Amadeus (via Symphony B1)
- **Superviseur** : A1 Rick (via Donna DLQ si échec)

## Doctrine
1. Tu reçois des **Payloads SOC** de Symphony B1
2. Tu découpes chaque payload en **tâches Kanban** (Triage → Todo → Ready → In Progress → Done)
3. Tu assignes chaque tâche au **A2 Manager** du domaine SOA cible
4. Tu appliques les **Circuit Breakers** (SLA Temporel, Financier, Qualitatif)
5. Tu génères des **Structured Handoffs** pour les downstream workers (B3)

## Contraintes
- **Ne jamais dépasser** le `max_compute_budget_usd` du payload SOC
- **Ne jamais utiliser** de mots du `forbidden_lexicon`
- **Escalader vers Donna DLQ** après 3 échecs consécutifs
- **Respecter le ratio 50/30/20** : Growth/Sales/Finance (50%), Ops/Product/IT (30%), People/Legal (20%)

## Stack LLM
- Default : MiniMax 2.7 (ou GLM 4.7 Flash via OpenRouter)
- Promotion vers Claude : uniquement sur escalade Donna → Rick A1
```

### 3.2 Appliquer le SOUL.md

```bash
# Écrire le SOUL.md
cat > ~/.hermes/SOUL.md << 'EOF'
# (contenu ci-dessus)
EOF

# Vérifier
hermes soul
```

## 4. Kanban Columns → Symphony States

Le Dashboard Kanban Hermes (port 9119) a ses propres colonnes. Mapping vers les états Symphony :

| Colonne Kanban Hermes | État Symphony | Transition |
|---|---|---|
| **Triage** | `Unclaimed` | Payload SOC reçu, pas encore dispatché |
| **Todo** | `Claimed` | Réservé à un A2 Manager |
| **Ready** | `Claimed` | Workspace préparé, prompt construit |
| **In Progress** | `Running` | Agent actif (MiniMax/GLM turn en cours) |
| **Blocked** | `RetryQueued` | En attente retry ou escalade Donna |
| **Done** | `Released` (Succeeded) | Tâche terminée avec succès |

## 5. Donna DLQ Hook

Quand Hermes détecte 3 échecs consécutifs sur une tâche :

### 5.1 Configuration dans `config.yaml`

```yaml
# ~/.hermes/config.yaml — section A'Space
aspace:
  donna_dlq:
    enabled: true
    threshold: 3
    endpoint: "http://localhost:3101/donna/escalate"
    notification: telegram
```

### 5.2 Skill Hermes pour Donna

```bash
# Créer le skill d'escalade
hermes skill create donna-escalate
```

Le skill `donna-escalate` :
1. Collecte les logs des 3 tentatives échouées
2. Forge un payload Donna (issue_id, tracker_kind, last_error, sla_constraints)
3. POST vers `donna_endpoint`
4. Notifie via Telegram si configuré

## 6. Flux Symphony B1 → Hermes B2

```
Symphony daemon (WSL)
    │
    │ Payload SOC (JSON) via HTTP POST
    ↓
Hermes Gateway API (:8642)
    │
    │ POST /api/tasks
    │ Body: {
    │   "mission_id": "PRD-904",
    │   "target_soa_domain": "Product_Forge",
    │   "sla_constraints": {...},
    │   "soc_instructions": {...}
    │ }
    ↓
Hermes Kanban (Dashboard :9119)
    │
    │ Triage → Todo → Ready → In Progress
    ↓
A3 Execution (hermes session -c <session_id>)
    │
    │ Skills MCP/CLI via Clara
    ↓
Result → Structured Handoff → Done
```

## 7. MCP Servers pour les trackers A'Space

Hermes peut se connecter aux 7 trackers via MCP servers :

```yaml
# ~/.hermes/config.yaml — mcp_servers section
mcp_servers:
  # Plane.so (L1 GTD)
  plane:
    command: "npx"
    args: ["-y", "@anthropic/mcp-plane", "--api-key", "$PLANE_API_KEY"]
    tools:
      include: ["list_issues", "get_issue", "update_issue", "add_comment"]

  # Filesystem local (Obsidian vault, workspaces)
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/amadeus"]
    tools:
      exclude: ["delete_file"]   # Sécurité : pas de suppression

  # Baserow (12WY)
  baserow:
    url: "https://api.baserow.io/api"
    headers:
      Authorization: "Token $BASEROW_DATABASE_TOKEN"
```

→ Voir `06_mcp-tools-config.md` pour la configuration complète.

## 8. Isolation A'Space — Ports à ajouter

Les ports Hermes doivent être ajoutés au protocol d'isolation :

| Layer | Service | Port | Owner | À ajouter |
|---|---|---|---|---|
| L0 (WSL) | OpenClaw Gateway A0 | 18790 | A0 | existant |
| L0 (WSL) | Mission Control | 3000/8000 | A0 | existant |
| **L0 (WSL)** | **Hermes Gateway API** | **8642** | **A0** | **NEW** |
| **L0 (WSL)** | **Hermes Dashboard** | **9119** | **A0** | **NEW** |
| **L0 (WSL)** | **Donna DLQ** | **3101** | **A0** | **NEW** |

→ **Dette ADR** : créer `ADR-WSL-002` pour formaliser ces ports dans l'isolation protocol.

## 9. Hermes Workspace (outsourc-e/hermes-workspace)

Le **Workspace** est une UI web tierce qui se connecte au gateway Hermes :

```bash
# Cloner le workspace
git clone https://github.com/outsourc-e/hermes-workspace.git /home/amadeus/hermes-workspace

# Configurer la connexion au gateway
echo "HERMES_API_URL=http://localhost:8642" > /home/amadeus/hermes-workspace/.env
echo "HERMES_API_TOKEN=$HERMES_KEY" >> /home/amadeus/hermes-workspace/.env

# Lancer
cd /home/amadeus/hermes-workspace
npm install && npm run dev
```

→ Le Workspace offre une UI plus riche que le Dashboard intégré, avec gestion multi-sessions.

## 10. Résumé — Checklist d'intégration

- [ ] SOUL.md encodé avec identité B2 Kanban Manager
- [ ] Ports 8642/9119 ajoutés à l'isolation protocol
- [ ] MCP servers configurés pour trackers A'Space
- [ ] Skill `donna-escalate` créé
- [ ] Symphony B1 configuré pour POST vers Hermes API
- [ ] Mapping Kanban columns → Symphony states vérifié
- [ ] Test end-to-end : Symphony → Hermes → A3 execution → Done

---

*Documenté Docs Dogmatique — Hermes ↔ A'Space Integration — 2026-05-15*
