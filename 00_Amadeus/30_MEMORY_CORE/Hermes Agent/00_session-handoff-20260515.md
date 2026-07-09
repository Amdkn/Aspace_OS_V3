---
source: Session Claude Opus 4.7 — installation Hermes WSL2 propre (Docs Dogmatique)
date: 2026-05-15
type: session-handoff
domain: L0_Tech_OS / Hermes_Agent
tags: [#Hermes #handoff #WSL2-NAT-issue #docs-dogmatic #ADR-WSL-002-pending]
session_context:
  api_limit_remaining: "5% (resets 6:30am)"
  context_used: "77% / 1M tokens"
  next_agent: "Codex ou Antigravity (Gemini)"
related:
  - README.md
  - 01_installation-setup.md
  - 02_architecture-services.md
  - 03_security-best-practices.md
  - 04_wsl2-networking.md (Codex)
  - 05_aspace-integration.md (Codex)
  - 06_mcp-tools-config.md (Codex)
---

# Session Handoff — Installation Hermes WSL2 2026-05-15

## 🎯 État actuel à l'heure du handoff

### ✅ Ce qui FONCTIONNE en interne WSL (curl depuis WSL)

```
Gateway   8642 → HTTP 200 ✅  (curl localhost:8642/health depuis WSL)
Dashboard 9119 → HTTP 200 ✅  (curl localhost:9119 depuis WSL)
Workspace 3000 → HTTP 200 ✅  (curl localhost:3000 depuis WSL)
```

### ❌ Ce qui NE FONCTIONNE PAS depuis Windows browser

```
localhost:8642 → ERR_CONNECTION_REFUSED
```

**Cause identifiée** : WSL2 en mode **NAT** (pas Mirrored). Le forwarding `localhost` Windows → WSL ne fonctionne pas pour les ports binds `0.0.0.0` dans WSL.

→ **Action requise** : appliquer la procédure de `04_wsl2-networking.md` §1.2 pour activer **Mirrored mode** :

```ini
# C:\Users\amado\.wslconfig
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
firewall=true
```

Puis `wsl --shutdown` et relancer.

**Alternative fallback** : tester d'abord avec WSL IP directe :
```bash
# Depuis Windows PowerShell
wsl -d ASpace-L0 hostname -I    # Récupère l'IP WSL
# Puis ouvrir http://<WSL_IP>:8642 dans browser
```

## 🏗️ Architecture systemd-user déployée

Trois services dans `~/.config/systemd/user/` :

| Service | Port | Type | Source |
|---|---|---|---|
| `hermes-gateway.service` | **8642** (0.0.0.0) | OFFICIEL (créé par `hermes gateway install`) | Nous Research |
| `hermes-gateway.service.d/aspace-override.conf` | — | Override : `EnvironmentFile=~/.hermes/.env` | A'Space custom |
| `hermes-dashboard.service` | **9119** (127.0.0.1) | CUSTOM mais nécessaire (`hermes dashboard` n'a pas de `install`) | A'Space custom |
| `hermes-workspace.service` | **3000** (0.0.0.0) | CUSTOM (vite dev server du repo outsourc-e/hermes-workspace) | A'Space custom |

### Override systemd (critique)

`~/.config/systemd/user/hermes-gateway.service.d/aspace-override.conf` :
```ini
[Service]
EnvironmentFile=-/home/amadeus/.hermes/.env
```

→ Sans cet override, le gateway officiel ne lit pas les vars custom (`API_SERVER_KEY`, `HERMES_DASHBOARD`, etc.) de `.env`.

## 🔐 Configuration appliquée

### `~/.hermes/.env` (chmod 600)

```bash
HERMES_PROVIDER=openrouter
HERMES_MODEL=z-ai/glm-4.7-flash
HERMES_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=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

# === Docs Dogmatique — Gateway + Dashboard (2026-05-15) ===
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=W-c3vQ3zlrAy59xGDyOjqa8svvVuWSI1Wzc_0RzJp4c
API_SERVER_CORS_ORIGINS=*
HERMES_DASHBOARD=1
GATEWAY_ALLOW_ALL_USERS=true
```

⚠️ **API_SERVER_KEY (W-c3vQ3zlrAy59xGDyOjqa8svvVuWSI1Wzc_0RzJp4c)** est aussi dans `~/hermes-workspace/.env` sous `HERMES_API_TOKEN=` (sync auto fait).

### `~/.hermes/SOUL.md` — Identité B2 Kanban Manager (Codex template)

Appliqué : voir contenu dans `05_aspace-integration.md` §3.1.
Backup créé : `~/.hermes/SOUL.md.bak.20260515_*`

### `~/.hermes/config.yaml` — Fixes appliqués

- ✅ `api_mode: chat` déplacé du root vers sous `model:` section (warning éliminé)
- ✅ Backup `~/.hermes/config.yaml.bak.20260515_*` préservé

## 📊 Versions

```
Hermes Agent: v0.13.0 (2026.5.7)
Python: 3.11.15 (venv at ~/.hermes/hermes-agent/venv/)
Node: v22.22.2 (NodeSource)
pnpm: 11.1.2
Hermes Workspace: v2.3.0 (cloned outsourc-e/hermes-workspace)
Vite: 7.3.2
WSL distro: ASpace-L0 (Ubuntu 24.04.4 LTS)
systemd: enabled in /etc/wsl.conf
linger: enabled for user amadeus
```

## 🪦 Nettoyage effectué cette session

- ✅ 3 services systemd custom anciens (hermes-gateway, hermes-workspace, hermes-dashboard de la 1ère tentative) → supprimés
- ✅ Paperclip AI rogue process dans WSL (`~/aspace/Paperclip AI/src/index.ts` à 84% CPU) → killed
- ✅ Multi-restart loop gateway → résolu par fix api_mode
- ✅ `hermes doctor --fix` exécuté (1/3 issues fixed auto)

## 🟡 Issues résiduelles à traiter par next agent

### 1. WSL2 Mirrored mode pas activé (BLOQUANT pour browser Windows)

**Action** : éditer `C:\Users\amado\.wslconfig` (cf. §État actuel ci-dessus).

### 2. Skill `donna-escalate` à créer

Référence : `05_aspace-integration.md` §5.2

```bash
hermes skill create donna-escalate
```

### 3. MCP servers Hermes à configurer

Référence : `06_mcp-tools-config.md` §2

Ajouter dans `~/.hermes/config.yaml` les serveurs MCP standards (filesystem, github, brave_search, sqlite, thinking) — voir template Codex.

### 4. ADR-WSL-002 à créer

Référence : `05_aspace-integration.md` §8 + `04_wsl2-networking.md` §2.1

Ports Hermes (8642, 9119, 3101) doivent être formalisés dans isolation_protocol.md.

### 5. 2 issues hermes doctor non auto-fixables

```
1. Run 'hermes setup' to configure missing API keys for full tool access
   (DISCORD_BOT_TOKEN, TINKER_API_KEY, WANDB_API_KEY, EXA_API_KEY, etc.)
2. Various tools require system dependencies (homeassistant, image_gen, etc.)
```

→ Optionnel selon usage A'Space.

### 6. Custom A'Space MCP bridges (Phase 2 — futur)

Référence : `06_mcp-tools-config.md` §3
- `clara_cli` — bridge MCP → CLI (doctrine SDD-009)
- `donna` — escalade DLQ (port 3101 — pas encore monté)
- `symphony` — recevoir Payloads SOC B1→B2 (port 3200 — pas encore monté)

## 🎮 Commandes utiles pour reprise

```bash
# Depuis WSL ASpace-L0
hermes gateway status                          # État gateway
systemctl --user status hermes-gateway hermes-dashboard hermes-workspace
journalctl --user -u hermes-gateway -f         # Logs gateway live
hermes doctor                                  # Check config

# Restart d'un service
systemctl --user restart hermes-gateway

# Verify ports
ss -tln | grep -E ':8642|:9119|:3000'

# Test HTTP interne (depuis WSL)
curl http://localhost:8642/health
curl -H "Authorization: Bearer W-c3vQ3zlrAy59xGDyOjqa8svvVuWSI1Wzc_0RzJp4c" http://localhost:8642/api/...

# Logs
journalctl --user -u hermes-gateway --since '5 minutes ago' --no-pager
```

## 📁 Fichiers backup créés cette session

```
~/.hermes/.env.bak.20260515_*
~/.hermes/SOUL.md.bak.20260515_*
~/.hermes/config.yaml.bak.20260515_*
~/hermes-workspace/.env.bak.20260515_*
```

## 🔗 Cross-refs Canon V0

- **SDD-009** §3 tri-tier B1/B2/B3 → Hermes EST le B2
- **SDD-010** §5.2 TARDIS Inversé → Hermes orchestre via Kanban
- **ADR-RICK-002** Paperclip Deprecation → Hermes remplace Paperclip (VPS purgé 2026-05-13)
- **05_aspace-integration.md** §10 → checklist A'Space (10 items)

## 📍 Settings Claude Desktop appliqués (contexte session)

- ✅ "Mode contournement par défaut" activé (Settings → Claude Code → Sessions locales)
- ✅ Mode session "Ignorer les permissions" (Ctrl+Shift+M → option 4)
- ✅ Hooks audio configurés dans `~/.claude/settings.json` :
  - `Stop` → `[System.Media.SystemSounds]::Asterisk.Play()`
  - `Notification` → `[System.Media.SystemSounds]::Question.Play()`
- ⚠️ Hooks audio dépendent du parsing Claude Desktop → à confirmer si effectifs

## 🎯 Direction recommandée pour next session

**Step 1 (CRITIQUE)** — Activer WSL2 Mirrored mode → débloquer browser Windows
**Step 2** — Tester localhost:9119 (Kanban Dashboard) + localhost:3000 (Workspace UI)
**Step 3** — Si OK, créer ADR-WSL-002 formalisant les ports
**Step 4** — Skill `donna-escalate` + MCP servers config selon Codex 06_*.md

---

*Handoff doc — 2026-05-15 16:11 — Claude Opus 4.7 → next agent (Codex / Antigravity / Claude après reset 6:30am)*
*Tous les services WSL tournent. Tous les fichiers config sont sauvegardés. La connexion Windows ↔ WSL est le SEUL blocage final.*
