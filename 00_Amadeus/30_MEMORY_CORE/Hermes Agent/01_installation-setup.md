---
source: Context7 /nousresearch/hermes-agent
date: 2026-05-15
type: docs-synthesis
section: Installation + Configuration
---

# Hermes Agent — Installation & Setup (validated)

## 1. Installation officielle (3 plateformes)

### Linux / macOS / WSL2
```bash
# One-liner officiel (depuis hermes-agent.nousresearch.com/docs)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```
→ Installe dans `~/.hermes/` + binary `~/.local/bin/hermes`

### Windows native (early beta)
- Pas le path recommandé (encore early beta)
- Préfère WSL2 si possible

### Docker (alternative pour deploy)
```bash
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  -p 9119:9119 \
  -e HERMES_DASHBOARD=1 \
  nousresearch/hermes-agent gateway run
```

## 2. Initial setup wizard

```bash
hermes setup                  # First-time wizard (interactive)
hermes setup --quick          # Only prompts missing items
hermes setup --non-interactive # Uses defaults
hermes setup --reset          # Clears config + restart wizard
hermes setup --reconfigure    # Alias for existing installs
```

Le wizard configure :
- **Model** (provider + model name)
- **Terminal backend** (local shell / Docker / SSH / Modal)
- **Gateway** (messaging platforms)
- **Tools** (built-in toolsets enabled)
- **Agent** (personality / SOUL.md / autonomous mode)

## 3. Provider configuration

```bash
hermes model                                              # Wizard
hermes model openrouter:anthropic/claude-opus-4           # OpenRouter
hermes model openrouter:z-ai/glm-4.7-flash                # GLM frugal (V1 cible)
hermes model nous                                          # Nous Portal OAuth
hermes model openai-compatible --base-url http://localhost:8080/v1  # Local (Ollama)
```

### Providers supportés (20+)
| Provider | Auth | env var |
|---|---|---|
| OpenRouter | API key | `OPENROUTER_API_KEY` |
| Anthropic | API key | `ANTHROPIC_API_KEY` |
| Google Gemini | API key | `GOOGLE_API_KEY` |
| DeepSeek | API key | `DEEPSEEK_API_KEY` |
| OpenAI Codex | OAuth | — |
| Local (Ollama) | None | — |
| Nous Portal | OAuth | — |

## 4. Structure `~/.hermes/`

```
~/.hermes/
├── .env                  # API keys + provider config
├── config.yaml           # Model + backends + agent config
├── cron/                 # Scheduled jobs
├── sessions/             # Conversation history
├── logs/                 # Runtime logs
├── memories/             # Persistent memory across sessions
├── skills/               # Procedural memory (created by agent)
├── checkpoints/          # State snapshots
└── hermes-agent/         # Source code (if installed from git)
```

## 5. config.yaml minimal (post `hermes model`)

```yaml
model:
  default: glm-4.7-flash
  provider: openrouter
  base_url: https://openrouter.ai/api/v1
```

## 6. .env complet (variables validées par doc)

```bash
# === LLM Provider ===
HERMES_PROVIDER=openrouter
HERMES_MODEL=z-ai/glm-4.7-flash
HERMES_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=sk-or-v1-...

# === API Server (gateway HTTP API) ===
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0           # 127.0.0.1 par défaut. 0.0.0.0 = nécessite API_SERVER_KEY
API_SERVER_PORT=8642              # Port gateway API
API_SERVER_KEY=<32+ char secret>  # OBLIGATOIRE pour 0.0.0.0
API_SERVER_CORS_ORIGINS=*         # CORS (Workspace web)

# === Dashboard (intégré au gateway) ===
HERMES_DASHBOARD=1                # Active le dashboard sur :9119

# === Gateway access control ===
GATEWAY_ALLOW_ALL_USERS=true      # Local dev only — sinon allowlists par platform
TELEGRAM_ALLOWED_USERS=user_id    # Allowlist Telegram

# === Messaging platforms (optionnel) ===
TELEGRAM_BOT_TOKEN=...
DISCORD_BOT_TOKEN=...
SLACK_BOT_TOKEN=...
```

## 7. Setup minimal pour usage WSL2 + Workspace

```bash
# Setup wizard (skip platforms si pas de messaging)
hermes setup --quick

# Provider GLM frugal
hermes model openrouter:z-ai/glm-4.7-flash

# Config .env pour dashboard + Windows browser access
HERMES_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
{
  echo "API_SERVER_ENABLED=true"
  echo "API_SERVER_HOST=0.0.0.0"
  echo "API_SERVER_PORT=8642"
  echo "API_SERVER_KEY=$HERMES_KEY"
  echo "API_SERVER_CORS_ORIGINS=*"
  echo "HERMES_DASHBOARD=1"
  echo "GATEWAY_ALLOW_ALL_USERS=true"
} >> ~/.hermes/.env

# Install systemd user service
hermes gateway install
hermes gateway start

# Persistence cross-logout (REQUIS pour WSL2)
sudo loginctl enable-linger $USER

# Verify
hermes gateway status
curl -H "Authorization: Bearer $HERMES_KEY" http://localhost:8642/health
```

## 8. CONTRIBUTING.md — Structure DEV

```bash
mkdir -p ~/.hermes/{cron,sessions,logs,memories,skills}
cp cli-config.yaml.example ~/.hermes/config.yaml
touch ~/.hermes/.env
echo "OPENROUTER_API_KEY=..." >> ~/.hermes/.env
```

## 9. Premier test (Quickstart)

```bash
hermes                        # Mode interactif (REPL)
hermes --tui                  # Mode TUI (Ink)
hermes -p "Hello"             # One-shot
hermes -c "session_id"        # Continue session
```

---

*Documenté Docs Dogmatique — sources Context7 /nousresearch/hermes-agent + CONTRIBUTING.md*
