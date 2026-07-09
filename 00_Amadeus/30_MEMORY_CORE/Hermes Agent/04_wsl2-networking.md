---
source: Context7 /nousresearch/hermes-agent + WSL2 docs + ASpace isolation_protocol.md
date: 2026-05-15
type: docs-synthesis
section: WSL2 Networking + Windows Access
---

# Hermes Agent — WSL2 Networking & Windows Access

## 1. Deux modes réseau WSL2

| Mode | Config | Comment accéder depuis Windows | Port forwarding |
|---|---|---|---|
| **NAT** (default) | Rien dans `.wslconfig` | `http://<WSL_IP>:<port>` | Manuel (`netsh portproxy`) |
| **Mirrored** (recommandé) | `networkingMode=mirrored` | `http://localhost:<port>` | Automatique |

### 1.1 Vérifier le mode actuel

```powershell
# Depuis Windows PowerShell
wsl --version              # Doit être WSL 2.x
wsl hostname -I            # Si renvoie une IP ≠ 127.x → NAT mode
```

```bash
# Depuis WSL
ip addr show eth0          # NAT: IP type 172.x ou 10.x
                           # Mirrored: IP miroir du Windows host
```

### 1.2 Activer le mode Mirrored (recommandé)

**Option A — GUI** (Windows 11 22H2+) :
1. Menu Démarrer → "WSL Settings"
2. Onglet Networking → **Mirrored**
3. Fermer → `wsl --shutdown` depuis PowerShell

**Option B — `.wslconfig`** :

```ini
# C:\Users\amado\.wslconfig
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
firewall=true
```

```powershell
# Redémarrer WSL
wsl --shutdown
wsl -d ASpace-L0
```

### 1.3 Vérification post-config

```bash
# Depuis WSL — lancer un test server
python3 -m http.server 9999 &

# Depuis Windows — tester accès
curl http://localhost:9999         # Mirrored: ✅ fonctionne
curl http://$(wsl hostname -I | awk '{print $1}'):9999  # NAT: ✅ fonctionne
```

## 2. Accès Hermes depuis Windows

### 2.1 Ports Hermes dans l'isolation A'Space

Conformément à `isolation_protocol.md` :

| Port | Service Hermes | Bind | Accès Windows |
|---|---|---|---|
| **8642** | Gateway API | `0.0.0.0` (requis `API_SERVER_KEY`) | `http://localhost:8642` (mirrored) |
| **9119** | Web Dashboard | `0.0.0.0` (via `HERMES_DASHBOARD=1`) | `http://localhost:9119` (mirrored) |

⚠️ Ces ports **NE SONT PAS** dans la table d'isolation existante (qui liste 18789/18790/3000/8000). Il faudra les ajouter à l'isolation protocol via un ADR.

### 2.2 Config `.env` pour accès Windows

```bash
# ~/.hermes/.env — section networking
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0          # REQUIS pour accès Windows
API_SERVER_PORT=8642
API_SERVER_KEY=<your-key>        # OBLIGATOIRE avec 0.0.0.0
HERMES_DASHBOARD=1               # Active dashboard :9119
```

### 2.3 Test complet depuis Windows

```powershell
# Depuis PowerShell Windows
# 1. Gateway API
curl -H "Authorization: Bearer <API_KEY>" http://localhost:8642/health
# → 200 OK

# 2. Dashboard
Start-Process "http://localhost:9119"
# → Dashboard Kanban dans le navigateur Windows
```

## 3. Mode NAT — Fallback si Mirrored ne marche pas

Si le mode Mirrored cause des problèmes (Docker Desktop conflict, etc.) :

### 3.1 Trouver l'IP WSL

```bash
# Depuis WSL
hostname -I | awk '{print $1}'
# → Ex: 172.24.112.1
```

### 3.2 Port forwarding Windows → WSL (optionnel)

```powershell
# Depuis PowerShell Admin
$wslIp = (wsl hostname -I).Trim().Split(' ')[0]

# Forward port 8642
netsh interface portproxy add v4tov4 listenport=8642 listenaddress=0.0.0.0 connectport=8642 connectaddress=$wslIp

# Forward port 9119
netsh interface portproxy add v4tov4 listenport=9119 listenaddress=0.0.0.0 connectport=9119 connectaddress=$wslIp

# Vérifier
netsh interface portproxy show all

# Cleanup quand plus nécessaire
netsh interface portproxy delete v4tov4 listenport=8642 listenaddress=0.0.0.0
netsh interface portproxy delete v4tov4 listenport=9119 listenaddress=0.0.0.0
```

⚠️ L'IP WSL change à chaque reboot. Il faudrait un script de refresh si NAT mode est utilisé.

### 3.3 Script auto-refresh (optionnel)

```bash
#!/bin/bash
# /home/amadeus/scripts/refresh-port-proxy.sh
WSL_IP=$(hostname -I | awk '{print $1}')
powershell.exe -Command "
  netsh interface portproxy delete v4tov4 listenport=8642 listenaddress=0.0.0.0 2>\$null
  netsh interface portproxy delete v4tov4 listenport=9119 listenaddress=0.0.0.0 2>\$null
  netsh interface portproxy add v4tov4 listenport=8642 listenaddress=0.0.0.0 connectport=8642 connectaddress=$WSL_IP
  netsh interface portproxy add v4tov4 listenport=9119 listenaddress=0.0.0.0 connectport=9119 connectaddress=$WSL_IP
"
echo "Port proxy refreshed → WSL IP: $WSL_IP"
```

## 4. Persistance cross-reboot (systemd + lingering)

```bash
# CRITIQUE pour WSL2 — sans ça, le gateway meurt au logout Windows
sudo loginctl enable-linger $USER

# Vérifier
loginctl show-user $USER | grep Linger
# → Linger=yes

# Le service Hermes gateway survit aux fermetures de terminal
hermes gateway status
```

## 5. Firewall Windows (si nécessaire)

En mode Mirrored avec `firewall=true`, Windows Firewall s'applique au trafic WSL :

```powershell
# Autoriser les ports Hermes
New-NetFirewallRule -DisplayName "Hermes Gateway API" -Direction Inbound -LocalPort 8642 -Protocol TCP -Action Allow
New-NetFirewallRule -DisplayName "Hermes Dashboard" -Direction Inbound -LocalPort 9119 -Protocol TCP -Action Allow
```

## 6. Tailscale (accès distant — optionnel)

Si Tailscale est installé dans WSL :

```bash
# Hermes accessible depuis n'importe quel device Tailscale
# Via le hostname Tailscale de la machine WSL
curl -H "Authorization: Bearer <KEY>" http://<tailscale-hostname>:8642/health
```

→ Permet l'accès au Dashboard depuis mobile ou VPS sans exposer sur internet.

## 7. Diagnostic rapide

```bash
# Depuis WSL — Hermes tourne ?
hermes gateway status
ss -tlnp | grep -E '(8642|9119)'

# Port binding correct ?
# → 0.0.0.0:8642 = accessible Windows ✅
# → 127.0.0.1:8642 = local WSL only ❌ (Windows ne voit pas)

# Logs
journalctl --user -u hermes-gateway -f
```

---

*Documenté Docs Dogmatique — WSL2 Networking pour Hermes Agent — 2026-05-15*
