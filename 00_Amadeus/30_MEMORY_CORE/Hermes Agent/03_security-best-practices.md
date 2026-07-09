---
source: Context7 /nousresearch/hermes-agent + SECURITY.md + faq.md
date: 2026-05-15
type: docs-synthesis
section: Security + Best Practices + Troubleshooting
---

# Hermes Agent — Security & Best Practices (validated)

## 1. Defense-in-Depth — 7 couches de sécurité

(Verbatim de `website/docs/user-guide/security.md`)

> *"Hermes Agent is designed with a defense-in-depth security model that covers various boundaries, from command approval to container isolation and user authorization on messaging platforms."*

| # | Couche | Mission |
|---|---|---|
| 1 | **User authorization** | Allowlists par platform (TELEGRAM_ALLOWED_USERS, etc.) |
| 2 | **Dangerous command approval** | Confirmation interactive avant exécution de commandes risquées |
| 3 | **Container isolation** | Terminal backend Docker / sandbox |
| 4 | **MCP credential filtering** | Filtrage auto des creds dans les payloads MCP |
| 5 | **Context file scanning** | Scan des fichiers de contexte pour secrets/PII |
| 6 | **Cross-session isolation** | Séparation des sessions (pas de leak inter-conversation) |
| 7 | **Input sanitization** | Validation des inputs externes (messaging platforms) |

## 2. API_SERVER_KEY — les règles d'or

### Quand est-elle OBLIGATOIRE
- ✅ Bind `API_SERVER_HOST=0.0.0.0` → **REQUIS sinon refus de démarrage**
- ✅ Tout déploiement non-localhost (Docker exposé, VPS, etc.)
- ✅ Multi-user accès

### Quand elle est OPTIONNELLE
- 🟡 Loopback `127.0.0.1` strict + single user → optionnelle mais recommandée

### Génération sécurisée (validée)
```bash
# ✅ Méthode recommandée (Python secrets)
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# ✅ Alternative OpenSSL (vérifier que la commande retourne bien)
openssl rand -base64 32

# ❌ NE PAS faire — bash $RANDOM est faible cryptographiquement
echo $RANDOM$RANDOM
```

### Configuration end-to-end
```bash
# 1. Generate
HERMES_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
echo "Key: $HERMES_KEY"

# 2. Set dans Hermes
echo "API_SERVER_KEY=$HERMES_KEY" >> ~/.hermes/.env

# 3. Set dans client (Workspace)
echo "HERMES_API_TOKEN=$HERMES_KEY" >> ~/hermes-workspace/.env

# 4. Test
curl -H "Authorization: Bearer $HERMES_KEY" http://localhost:8642/health
# → 200 OK si correct, 401 sinon
```

## 3. GATEWAY_ALLOW_ALL_USERS — quand l'utiliser

```bash
GATEWAY_ALLOW_ALL_USERS=true   # Local dev / single user only
```

⚠️ **À NE JAMAIS faire en production** ou sur VPS multi-tenant. Préfère :
- `TELEGRAM_ALLOWED_USERS=<your_id>`
- `DISCORD_ALLOWED_USERS=<your_id>`
- Allowlists par platform

## 4. Troubleshooting officiel (FAQ Nous)

### "Gateway won't start"
```bash
# 1. Install messaging deps
pip install "hermes-agent[messaging]"

# 2. Check port conflicts
lsof -i :8642
lsof -i :9119

# 3. Verify config
hermes config show

# 4. Check logs
journalctl --user -u hermes-gateway -f
```

### "Cannot connect from Windows browser to WSL"
- **Vérifier bind** : `ss -tlnp | grep 8642` → doit être `0.0.0.0:8642` pour Windows access
- **Vérifier API_SERVER_KEY** : sans clé, le bind 0.0.0.0 est refusé
- **WSL2 mirrored mode** : Windows 11 22H2+ peut accéder via `http://localhost:8642`
- **WSL2 NAT mode (default)** : utiliser `http://<WSL_IP>:8642` (cf. `wsl hostname -I`)

### "Dashboard 9119 not reachable"
- Vérifier `HERMES_DASHBOARD=1` dans `~/.hermes/.env`
- Restart gateway après modif env
- Vérifier `hermes dashboard --status`

### "API returns 401 Unauthorized"
- Client doit envoyer `Authorization: Bearer <API_SERVER_KEY>`
- OR `?api_key=<key>` query param
- OR `X-API-Key: <key>` header

## 5. Anti-patterns documentés à éviter

| Anti-pattern | Documenté dans | Correction |
|---|---|---|
| Créer ses propres unit systemd | `windows-native.md` + `messaging/index.md` | Utiliser `hermes gateway install` |
| Bind 0.0.0.0 sans key | `docker.md` + erreur runtime | `API_SERVER_KEY` obligatoire |
| Dashboard process séparé | `docker.md` Running the dashboard | Side-process intégré via `HERMES_DASHBOARD=1` |
| Stocker secrets dans .service systemd | (general security) | Utiliser `EnvironmentFile=/etc/aspace/secrets.env` chmod 600 |
| `hermes gateway run` sans linger | `messaging/index.md` | `sudo loginctl enable-linger $USER` |
| Permissions ouvertes sur `.env` | (general) | `chmod 600 ~/.hermes/.env` |

## 6. Best Practices — Compilation Nous + community

### Setup propre WSL2 (les 7 étapes documentées)
```bash
# 1. Install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# 2. Setup wizard
hermes setup

# 3. Provider
hermes model openrouter:z-ai/glm-4.7-flash

# 4. Configure API + dashboard
HERMES_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
{
  echo ""
  echo "# Hermes API + Dashboard config — $(date -I)"
  echo "API_SERVER_ENABLED=true"
  echo "API_SERVER_HOST=0.0.0.0"
  echo "API_SERVER_PORT=8642"
  echo "API_SERVER_KEY=$HERMES_KEY"
  echo "API_SERVER_CORS_ORIGINS=*"
  echo "HERMES_DASHBOARD=1"
  echo "GATEWAY_ALLOW_ALL_USERS=true"
} >> ~/.hermes/.env
chmod 600 ~/.hermes/.env

# 5. Install + start user service
hermes gateway install
hermes gateway start

# 6. Enable lingering
sudo loginctl enable-linger $USER

# 7. Verify
hermes gateway status
curl -H "Authorization: Bearer $HERMES_KEY" http://localhost:8642/health
# Open browser: http://localhost:9119
```

### Permissions filesystem
```bash
chmod 600 ~/.hermes/.env                       # Secrets readable only by owner
chmod 700 ~/.hermes/sessions ~/.hermes/skills  # Private dirs
chmod 700 ~/.hermes                            # Whole hermes dir
```

### Workspace ↔ Gateway sync
```bash
# Token doit être IDENTIQUE des deux côtés
grep API_SERVER_KEY ~/.hermes/.env
grep HERMES_API_TOKEN ~/hermes-workspace/.env
# → mêmes 32+ chars
```

## 7. SOUL.md & Personality

```bash
# Edit personality
hermes soul edit                              # Opens editor
hermes soul                                   # View current

# Default path
~/.hermes/SOUL.md
```

→ Doc référence : `features/personality-soul`

## 8. Skills System

```bash
hermes skill list                              # All skills
hermes skill show <name>                       # Show skill source
hermes skill create <name>                     # Manual creation
# OR
hermes (REPL) → agent crée automatiquement quand il identifie un pattern récurrent
```

→ Skills stockés dans `~/.hermes/skills/`, auto-loaded au boot agent.

## 9. Kanban Tutorial workflow (multi-agent coordination)

Selon `features/kanban-tutorial` :

### 4 patterns de workflow officiels
1. **Solo development with dependencies** — un agent gère un graphe de tâches
2. **Parallel fleet farming** — plusieurs agents en parallèle sur tâches indépendantes
3. **Multi-role pipelines** — chaque agent un rôle (researcher → coder → reviewer)
4. **Failure recovery** — retry strategies avec intelligent task inheritance

### Structured Handoff (concept clé)
Chaque task completion inclut :
- Summary du travail effectué
- Metadata (artifacts, decisions, blockers identifiés)
- Context inheritance pour le worker downstream

→ Cohérent avec **SDD-009 §2.2 Payload SOC** (notre architecture A'Space).

## 10. Cross-refs A'Space

| Composant | Lien notre canon |
|---|---|
| Gateway autonome | SDD-009 §3 Architecture tri-tier B1/B2/B3 |
| Dashboard Kanban | SDD-009 §3.1 B2 Hermes Kanban |
| Skills system | SDD-009 §3.3 A3 Hermes Agents |
| Multi-agent coordination | SDD-010 §5.2 TARDIS Inversé |
| Allowlists | ADR-RICK-001 §7 Sécurité réseau |
| API_SERVER_KEY rotation | Dette ADR-RICK-002 §10 |

---

*Documenté Docs Dogmatique — sources Context7 multi-fetch + SECURITY.md + faq.md*
