---
source: Context7 /nousresearch/hermes-agent MCP docs + MCP spec + A'Space trackers
date: 2026-05-15
type: docs-synthesis
section: MCP Tools Configuration
---

# Hermes Agent — MCP Tools Configuration

## 1. MCP dans Hermes — résumé

Hermes supporte MCP (Model Context Protocol) en **deux modes** :

| Mode | Usage | Commande |
|---|---|---|
| **Client** | Hermes se connecte à des serveurs MCP externes (outils) | Config dans `config.yaml` |
| **Server** | Hermes expose ses propres tools à d'autres clients (Cursor, Claude Desktop) | `hermes mcp serve` |

Pour A'Space, on utilise le **mode Client** : Hermes B2 se connecte aux trackers et outils A'Space via MCP servers.

## 2. Configuration complète `config.yaml`

```yaml
# ~/.hermes/config.yaml

model:
  default: z-ai/glm-4.7-flash           # Frugal default (SDD-009 §8)
  provider: openrouter
  base_url: https://openrouter.ai/api/v1

terminal:
  backend: local                          # WSL local execution

agent:
  personality_file: ~/.hermes/SOUL.md     # A'Space B2 identity (cf. 05_aspace-integration.md)
  context_files: []

display:
  streaming: true

# ═══════════════════════════════════════════
# MCP SERVERS — A'Space Tool Ecosystem
# ═══════════════════════════════════════════
mcp_servers:

  # ─── FILESYSTEM (Obsidian vault, workspaces, code) ───
  filesystem:
    command: "npx"
    args:
      - "-y"
      - "@modelcontextprotocol/server-filesystem"
      - "/home/amadeus"
    tools:
      exclude:
        - "delete_file"                   # Sécurité : pas de suppression
        - "move_file"                     # Sécurité : pas de déplacement racine

  # ─── GITHUB (repos A'Space) ───
  github:
    command: "npx"
    args:
      - "-y"
      - "@modelcontextprotocol/server-github"
    env:
      GITHUB_TOKEN: "${GITHUB_TOKEN}"
    tools:
      include:
        - "list_issues"
        - "create_issue"
        - "get_issue"
        - "add_comment"
        - "list_repos"
        - "search_code"

  # ─── BRAVE SEARCH (recherche web pour les A3) ───
  brave_search:
    command: "npx"
    args:
      - "-y"
      - "@modelcontextprotocol/server-brave-search"
    env:
      BRAVE_API_KEY: "${BRAVE_API_KEY}"

  # ─── SQLITE (mémoire locale, logs) ───
  sqlite:
    command: "npx"
    args:
      - "-y"
      - "@modelcontextprotocol/server-sqlite"
      - "/home/amadeus/.hermes/local.db"

  # ─── SEQUENTIAL THINKING (raisonnement structuré) ───
  thinking:
    command: "npx"
    args:
      - "-y"
      - "@modelcontextprotocol/server-sequential-thinking"
```

## 3. Serveurs MCP A'Space custom (à créer)

Les outils spécifiques A'Space qui n'existent pas encore en MCP standard :

### 3.1 Clara CLI Bridge (MCP → CLI)

Le concept SDD-009 : Clara forge les MCP en CLI pour frugalité.

```yaml
  # Clara CLI Bridge — transforme les appels MCP en commandes CLI locales
  clara_cli:
    command: "python3"
    args:
      - "/home/amadeus/aspace/tools/clara-mcp-bridge.py"
    tools:
      include:
        - "clara_exec"                    # Exécuter une commande Clara
        - "clara_list"                    # Lister les CLI disponibles
```

### 3.2 Donna DLQ Endpoint

```yaml
  # Donna DLQ — escalade des échecs
  donna:
    url: "http://localhost:3101/mcp"
    headers:
      Authorization: "Bearer ${DONNA_API_KEY}"
    tools:
      include:
        - "escalate"                      # Escalader vers Rick A1
        - "reset_counter"                 # Reset retry counter
        - "query_pending"                 # Lister les escalades en attente
```

### 3.3 Symphony Router (B1 → B2)

```yaml
  # Symphony Router — recevoir les Payloads SOC
  symphony:
    url: "http://localhost:3200/mcp"
    headers:
      Authorization: "Bearer ${SYMPHONY_API_KEY}"
    tools:
      include:
        - "get_pending_payloads"          # Payloads en attente
        - "ack_payload"                   # Confirmer réception
        - "report_completion"             # Rapporter completion
```

## 4. Installation des serveurs MCP

```bash
# Vérifier que npx est disponible
which npx || npm install -g npx

# Tester chaque serveur individuellement
npx -y @modelcontextprotocol/server-filesystem /home/amadeus --help
npx -y @modelcontextprotocol/server-github --help

# Installer le support MCP dans Hermes si pas déjà fait
cd ~/.hermes/hermes-agent
uv pip install -e ".[mcp]" 2>/dev/null || pip install "hermes-agent[mcp]"

# Vérifier les serveurs configurés
hermes mcp list
```

## 5. Gestion des credentials

### 5.1 Variables d'environnement dans `.env`

```bash
# ~/.hermes/.env — section MCP credentials
# (ajouté aux variables existantes)

# GitHub
GITHUB_TOKEN=ghp_...

# Brave Search
BRAVE_API_KEY=BSA...

# A'Space custom
DONNA_API_KEY=<generated>
SYMPHONY_API_KEY=<generated>
```

### 5.2 Sécurité credentials MCP

Hermes inclut un **credential filtering** automatique (couche 4 de defense-in-depth) :
- Les tokens dans les payloads MCP sont filtrés avant d'être envoyés au LLM
- Les logs ne contiennent pas de credentials en clair

```bash
# Vérifier les permissions
chmod 600 ~/.hermes/.env
chmod 700 ~/.hermes/
```

## 6. Tool filtering — bonnes pratiques A'Space

### 6.1 Principe de moindre privilège

Chaque serveur MCP ne doit exposer que les outils **nécessaires** au domaine :

| Serveur | Include (whitelist) | Exclude (blacklist) | Raison |
|---|---|---|---|
| filesystem | — | `delete_file`, `move_file` | Sécurité : pas de suppression racine |
| github | `list_issues`, `create_issue`, etc. | — | Pas besoin de `delete_repo` |
| sqlite | — | — | Accès complet à la DB locale |
| brave_search | — | — | Recherche = safe |

### 6.2 Per-session tool filtering

Pour les sessions A3 spécifiques, on peut filtrer par domaine :

```bash
# Session Growth → uniquement outils Growth
hermes -c growth_session --tools "brave_search,filesystem"

# Session Ops → outils Ops + GitHub
hermes -c ops_session --tools "github,filesystem,sqlite"
```

## 7. Rechargement à chaud

Après modification de `config.yaml` :

```bash
# Option 1 : commande /reload-mcp dans le chat Hermes
# (dans une session active)

# Option 2 : restart du gateway
hermes gateway restart

# Option 3 : vérifier la config actuelle
hermes config show
hermes mcp list
```

## 8. Troubleshooting MCP

| Problème | Diagnostic | Solution |
|---|---|---|
| Server ne se connecte pas | `hermes mcp list` → absent | Vérifier que `npx`/`command` est dans le PATH |
| Tool non disponible | `hermes mcp list` → tool absent | Vérifier `include`/`exclude` dans config |
| Credentials refusées | Logs : `401 Unauthorized` | Vérifier `.env` + redémarrer gateway |
| Timeout MCP | Logs : `timeout` | Augmenter timeout ou vérifier le serveur |
| Conflit npx version | `npx` installe une vieille version | `npx -y @scope/package@latest` |

```bash
# Debug logs
tail -f ~/.hermes/logs/mcp-*.log
journalctl --user -u hermes-gateway -f | grep -i mcp
```

## 9. Hermes comme MCP Server (mode inverse)

Hermes peut aussi **exposer ses outils** à d'autres clients AI :

```bash
# Lancer Hermes en mode MCP server
hermes mcp serve

# Connecter depuis Claude Desktop ou Cursor :
# Dans les settings MCP du client, ajouter :
# {
#   "hermes": {
#     "command": "hermes",
#     "args": ["mcp", "serve"]
#   }
# }
```

→ Permet à **Antigravity** (A'"0 GravityClaw) d'utiliser les tools Hermes directement.

## 10. Roadmap MCP A'Space

| Phase | Serveurs MCP | Priorité |
|---|---|---|
| **Phase 1** (maintenant) | `filesystem`, `github`, `brave_search`, `sqlite` | Standard MCP servers |
| **Phase 2** (post-Symphony) | `clara_cli`, `donna`, `symphony` | Custom A'Space bridges |
| **Phase 3** (post-MUSE) | Serveurs MCP par tracker (Plane, Baserow, Airtable, etc.) | Quand les adapters sont validés |
| **Phase 4** (self-hosted) | Hermes MCP server → Antigravity/Claude Desktop | Bidirectionnel |

---

*Documenté Docs Dogmatique — MCP Tools Configuration pour Hermes Agent — 2026-05-15*
