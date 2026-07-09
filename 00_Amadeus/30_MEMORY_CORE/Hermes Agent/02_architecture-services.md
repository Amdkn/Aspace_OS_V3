---
source: Context7 /nousresearch/hermes-agent + SECURITY.md + docker.md
date: 2026-05-15
type: docs-synthesis
section: Architecture + Services + Ports
---

# Hermes Agent — Architecture & Services (validated)

## 1. Architecture officielle (verbatim Nous)

```
User ↔ Messaging Platform ↔ Platform Adapter ↔ Gateway Runner ↔ AIAgent
```

→ Source : `website/docs/developer-guide/adding-platform-adapters.md`

### Diagramme complet avec ports

```
┌─────────────────────────────────────────────────────────────┐
│  External User                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Telegram     │  │ Discord/Slack│  │ Browser      │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
└─────────┼─────────────────┼─────────────────┼──────────────┘
          ↓                 ↓                 ↓
┌─────────────────────────────────────────────────────────────┐
│  Platform Adapters (Gateway sub-processes)                  │
│  Telegram │ Discord │ Slack │ WhatsApp │ ACP (IDE)         │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Gateway Runner (`hermes gateway run`)                      │
│  ├── API Server (HTTP)        :8642   (optional)           │
│  ├── Web Dashboard            :9119   (HERMES_DASHBOARD=1) │
│  └── Cron Scheduler                                         │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  AIAgent Core                                               │
│  ├── Skills System            ~/.hermes/skills/             │
│  ├── Memory System            ~/.hermes/memories/           │
│  ├── Sessions                 ~/.hermes/sessions/           │
│  └── Checkpoints              ~/.hermes/checkpoints/        │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
              Provider API (OpenRouter / Anthropic / Local)
```

## 2. Ports standards

| Port | Service | Activation | Bind par défaut |
|---|---|---|---|
| **8642** | Gateway API (HTTP) | `API_SERVER_ENABLED=true` | `127.0.0.1` (sauf si `API_SERVER_KEY` set) |
| **9119** | Web Dashboard | `HERMES_DASHBOARD=1` | `127.0.0.1` (configurable via `--host`) |

→ **Bind 0.0.0.0 sans API_SERVER_KEY = REFUSÉ** par sécurité.

## 3. Gateway management (4 modes)

### Mode 1 — Foreground (test)
```bash
hermes gateway              # Run in current terminal, Ctrl+C to stop
hermes gateway run          # Alias
```

### Mode 2 — User systemd service (recommandé pour WSL2 / laptop)
```bash
hermes gateway install      # Crée ~/.config/systemd/user/hermes-gateway.service
hermes gateway start
hermes gateway status
hermes gateway stop
hermes gateway restart
hermes gateway uninstall    # Remove

# Logs
journalctl --user -u hermes-gateway -f
```

### Mode 3 — System systemd service (VPS / headless / boot-time)
```bash
sudo hermes gateway install --system   # Linux only
sudo hermes gateway start --system
sudo hermes gateway status --system
journalctl -u hermes-gateway -f
```

### Mode 4 — Windows Task Scheduler
```powershell
hermes gateway install      # Creates schtasks entry + Startup shortcut
hermes gateway status       # Merged view (schtasks + Startup + PID)
hermes gateway start
hermes gateway stop         # Graceful SIGTERM
hermes gateway restart
hermes gateway uninstall

# Diagnostic
schtasks /Query /TN HermesGateway /V /FO LIST
HERMES_GATEWAY_FORCE_STARTUP=1   # Override startup checks
```

## 4. Lingering (cross-logout persistence — CRITIQUE pour WSL2)

```bash
sudo loginctl enable-linger $USER
```

→ Sans cela, user services s'arrêtent quand WSL Ubuntu logout / Windows reboot.

## 5. Dashboard configuration

### Activation
```bash
echo "HERMES_DASHBOARD=1" >> ~/.hermes/.env
hermes gateway restart
```

### Standalone command (sans gateway)
```bash
hermes dashboard --port 9119          # Default port
hermes dashboard --port 8080          # Custom port
hermes dashboard --host 0.0.0.0       # ⚠ DANGEROUS (use --insecure flag)
hermes dashboard --no-open            # Skip auto browser open
hermes dashboard --tui                # Expose embedded TUI chat tab
hermes dashboard --stop               # Stop running dashboard
hermes dashboard --status             # Check if running
```

### Kanban Tutorial flow (selon doc tutorial)

D'après `features/kanban-tutorial` :
- Dashboard à `http://127.0.0.1:9119`
- Multi-agent task management board
- Columns : **Triage → Todo → Ready → In Progress → Blocked → Done**
- **Structured Handoff** : completions incluent summaries + metadata pour les downstream workers
- 4 workflow patterns : solo dev with dependencies, parallel fleet farming, multi-role pipelines, failure recovery

## 6. Surfaces externes (security)

D'après `SECURITY.md` :

1. **Gateway platform adapters** (Telegram, Discord, Slack, WhatsApp, IRC...)
2. **API Server** (HTTP REST sur port 8642)
3. **Web Dashboard** (HTTP UI sur port 9119)
4. **ACP adapter** (Editor/IDE protocol)
5. **TUI gateway** (Local IPC for Ink terminal UI)

→ Chacune a son modèle d'auth (allowlists par platform, API key pour HTTP, etc.).

## 7. Terminal backends (où exécuter les commandes agent)

```bash
hermes setup     # Choisir le backend dans le wizard
```

Backends supportés :
- **local** — directement sur la machine Hermes
- **Docker** — sandboxé dans un container
- **SSH** — sur un host distant
- **Modal** — serverless cloud Modal.com

## 8. Storage layout (memory system)

```
~/.hermes/
├── sessions/       # Conversation history (séparées par thread)
├── memories/       # Persistent KV memory across sessions
├── skills/         # Procedural memory — l'agent crée + réutilise des skills
├── checkpoints/    # State snapshots pour rollback
├── cron/           # Scheduled jobs
└── logs/           # Runtime logs
```

## 9. Configuration `config.yaml` complète

```yaml
model:
  default: gemini-3-flash-preview
  provider: gemini
  base_url: https://generativelanguage.googleapis.com/v1beta

terminal:
  backend: local         # local | docker | ssh | modal
  # docker:
  #   image: nousresearch/hermes-sandbox

agent:
  personality_file: ~/.hermes/SOUL.md
  context_files: []
  # context compression settings
  # auxiliary models
  # security scanning + approvals

display:
  streaming: true
```

## 10. MCP Integration

Le système MCP (Model Context Protocol) permet de connecter Hermes à des serveurs MCP externes pour étendre ses tools.

- Setup via `hermes mcp add <name> <url-or-command>`
- Filter via `~/.hermes/config.yaml` section `mcp.servers`
- Securité : credential filtering automatique

---

*Documenté Docs Dogmatique — sources Context7 multi-fetch officielle*
