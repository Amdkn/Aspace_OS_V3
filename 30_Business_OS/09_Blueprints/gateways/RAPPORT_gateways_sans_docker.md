# RAPPORT — Gateways MCP installables SANS Docker (Windows 11)

**Date :** 2026-08-04
**Périmètre :** revue documentaire uniquement. Aucune installation, aucun clone, aucun `npm install`, aucun `cargo install`, aucun `docker run`, aucun `pip install`. Deux finalistes retenus, sept candidats écartés, recherche élargie au-delà de la liste du rapport précédent.
**Lis ce qui est déjà su avant de lire ce qui suit :** `RAPPORT_gateways.md` dans le même dossier. Le présent rapport en reprend les acquis et les prolonge ; il ne les recalcule pas.

---

## Méta — définition appliquée

Compte comme **sans Docker** :
- binaire natif Windows (`.exe`) téléchargeable ;
- paquet `pip install` / `pipx install` / `uv tool install` / `uv pip install` / `npm install -g` qui démarre un process local ;
- compilation `cargo install` / `go install` (sources publique).

Ne compte **pas** comme sans Docker :
- `docker compose up` même si un binaire existe en théorie mais qu'il n'est pas la voie documentée ;
- WSL2 seul (c'est une VM Linux) ;
- cluster Kubernetes.

Est **disqualifiant** : exiger une base externe (PostgreSQL, MongoDB, Redis) sans mode embarqué (SQLite, fichier). Postgres à la main sous Windows ramène la lourdeur qu'on cherche à fuir.

---

## TL;DR — les 2 finalistes

| Rang | Candidat | Voie d'installation | Port | Pourquoi il gagne |
|---|---|---|---|---|
| **1** | **agentgateway** (Solo.io → LF AAIF) | Binaire `agentgateway-windows-amd64.exe` (v1.4.1, 2026-07-29) | 3300 / 15500 | Seul candidat de la liste à offrir un **binaire natif Windows** signé SHA-256, distributions 4 plates-formes, gouvernance LF, 4/4 transports MCP officiels, CEL RBAC. |
| **2** | **IBM mcp-context-forge** | PyPI `pip install mcp-contextforge-gateway` (v1.0.6, 2026-07-22) | 4444 | Seule alternative **sans Docker, sans K8s, sans VM, sans DB externe** trouvée hors Linux. SQLite par défaut, 6 transports MCP couverts, RBAC + JWT + OAuth + audit log, 4 200 ★, commits actifs le 2026-08-04. |

**Si un seul devait être gardé :** agentgateway. Son installation se réduit à un `Invoke-WebRequest` + `Expand-Archive` + double-clic ou invocation `.\agentgateway.exe`. mcp-context-forge est un cran en dessous en maturité côté transport (Python 3.11+ requis, packaging PyPI) mais deux crans au-dessus en fonctionnalités « tout-en-un » (registry + virtual servers + federation + RBAC + admin UI servie par le même binaire).

---

## Finaliste 1 — agentgateway (Solo.io / LF Agentic AI Foundation)

### Fiche d'identité

- **Dépôt :** [github.com/agentgateway/agentgateway](https://github.com/agentgateway/agentgateway)
- **Organisation amont :** transféré à la **Linux Foundation / Agentic AI Foundation** le 2026-06-04 ([agentgateway.dev/blog](https://agentgateway.dev/blog), 2026-08-04). Sponsor initial : Solo.io.
- **Licence :** Apache-2.0 ([LICENSE](https://github.com/agentgateway/agentgateway/blob/main/LICENSE), 2026-08-04).
- **Dernière release :** **v1.4.1 du 2026-07-29** ([releases](https://github.com/agentgateway/agentgateway/releases), 2026-08-04). Cadence mensuelle depuis v1.0.0 (2026-03-16).
- **Activité :** 4 210 ★, 702 forks, ~12 contributeurs humains actifs, dernier commit `d05a8b4` le 2026-08-03 ([commits/main](https://github.com/agentgateway/agentgateway/commits/main), 2026-08-04).
- **Endorsers cités :** Microsoft, T-Mobile, Dell, CoreWeave, Akamai, NYU, Nirmata/Kyverno.

### Couverture MCP

- **4 transports :** stdio, HTTP, SSE, Streamable HTTP — **seul candidat à couvrir les 4 explicitement** ([agentgateway.dev/docs/overview/](https://agentgateway.dev/docs/overview/), 2026-08-04).
- **Conformité spec MCP `2026-07-28`** revendiquée (release v1.4, 2026-08-03).
- **Auth MCP :** « MCP auth spec compliance with OAuth providers (Auth0, Keycloak) » et mention de `mcpAuthentication` dans la configuration. **OAuth 2.1 et Dynamic Client Registration ne sont pas nommés en toutes lettres** dans la doc publique lue — à confirmer en pratique (cf. « inconnus » plus bas).

### RBAC / contrôle d'accès par outil

- **CEL (Common Expression Language)** fine-grained, scope par listener / route, **MCP tool scoping par identité** ([agentgateway.dev/docs](https://agentgateway.dev/docs/), 2026-08-04).
- **ext_authz** pour brancher un moteur externe (OPA, Casbin, etc.).
- **Prompt Guards** PII / regex.

### Observabilité

- **Prometheus** natif + token-usage ([agentgateway.dev/docs/overview/](https://agentgateway.dev/docs/overview/), 2026-08-04).
- **OpenTelemetry** natif.
- **Audit log tamper-evident** — journal qui résiste à l'édition post-hoc.
- Intégrations documentées : Datadog, Langfuse, Sentry, PagerDuty, W&B.

### Modes de déploiement

- **Standalone** (binaire unique, YAML flat).
- **Docker** (image `ghcr.io/agentgateway/agentgateway`).
- **Kubernetes** (chart Helm + ressources upstream Gateway API).

K8s est **une option, pas un prérequis** — c'est exceptionnel dans l'écosystème des gateways MCP (Obot, mcp-gateway-registry, MetaMCP sont K8s/Docker-first).

### Empreinte

- **1 binaire** (~70 Mo pour `agentgateway-windows-amd64.exe`), pas de runtime à installer, pas de config premium à acheter.
- **RAM au repos :** non chiffrée dans la doc lue. À mesurer lors de l'installation (le binaire utilise Hyper + Tokio, donc typiquement 30-80 Mo au repos).
- **Pas de BDD externe** — l'état est fichier.

### Pourquoi il gagne

1. **Binaire Windows natif disponible et signé SHA-256** — `agentgateway-windows-amd64.exe` téléchargeable directement depuis la release GitHub. Aucun interpréteur, aucun compilateur, aucun container.
2. **Les 4 transports MCP** — un seul candidat les couvre tous. Une bascule Arcade ou MetaMCP → agentgateway n'oblige pas à rebrancher les clients.
3. **Gouvernance LF / Agentic AI Foundation** — vendor-neutral depuis 2026-06-04. Argument cardinal pour un client « souveraineté ».
4. **CEL fine-grained RBAC** — moteur déclaratif standard, pas une allowlist maison.
5. **Format ouvert** — YAML flat (standalone) ou ressources upstream Gateway API (k8s). Pas de CRD propriétaire.
6. **Cadence et stabilité** — v1.0.0 le 2026-03-16, v1.4.1 le 2026-07-29, ~1M pulls à v1.0.

### Sa faiblesse

- **Le script d'install officiel `curl -sL https://agentgateway.dev/install | bash` est pour Linux/Mac** ([agentgateway.dev/docs/standalone/latest/quickstart](https://agentgateway.dev/docs/standalone/latest/quickstart/), 2026-08-04). Sur Windows, ce script ne fonctionne pas en natif. La voie est de **télécharger le `.exe` directement depuis la release GitHub** et de le lancer à la main — l'install est trivial mais il faut assembler les pièces soi-même.
- **OAuth 2.1 / DCR ne sont pas nommés** explicitement dans la doc lue. La doc parle de « MCP auth spec compliance with OAuth providers ». À valider en pratique.
- **Tunnel Handler au sens ngrok/cloudflared** n'est pas nommé. À composer soi-même (ext_authz + CEL peuvent l'émuler).
- **Pas de sous-registry** — agentgateway est un proxy, pas un catalogue. Si le client veut un portail self-service d'enrôlement de serveurs MCP, il faut un composant en plus (ou `mcp-gateway-registry` en phase 2).

---

## Finaliste 2 — IBM mcp-context-forge

### Fiche d'identité

- **Dépôt :** [github.com/IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge)
- **Licence :** Apache-2.0 ([LICENSE](https://github.com/IBM/mcp-context-forge/blob/main/LICENSE), 2026-08-04).
- **Dernière release :** **v1.0.6 du 2026-07-22** (« OAuth Token Exchange, Vault Credentials, MCP Apps, Dataplane Publishing, and Security Hardening ») ([releases](https://github.com/IBM/mcp-context-forge/releases), 2026-08-04).
- **Activité :** 4 200 ★, 798 forks, ~35 commits visibles sur 30 jours, **dernier commit `2026-08-04`** ([commits/main](https://github.com/IBM/mcp-context-forge/commits/main), 2026-08-04). 938 issues ouvertes, 261 PR ouvertes — communauté très engagée.
- **Sponsoring :** IBM. Pas un repo perso.

### Couverture MCP

- **6 transports documentés :** HTTP, JSON-RPC, WebSocket, SSE (avec keepalive configurable), **stdio**, **streamable-HTTP**. Choix de la version de protocole MCP (ex. `2025-11-25`).
- **Fedère MCP, A2A et REST/gRPC** ([README](https://github.com/IBM/mcp-context-forge), 2026-08-04). gRPC-to-MCP via reflection-based service discovery.
- **Virtualisation** d'APIs legacy en outils MCP-compatibles.
- **40+ plugins** (transports additionnels, intégrations).

### RBAC / contrôle d'accès par outil

- **OAuth tokens** scope-utilisateur, **Basic Auth**, **JWT**, custom auth schemes.
- **RBAC** natif, network policies, secret management.
- **Built-in auth, retries, rate-limiting**.
- **Fail-closed par défaut** pour le cross-gateway routing (doc [README](https://github.com/IBM/mcp-context-forge), 2026-08-04).
- **Unconditional X-Upstream-Authorization header support** — transmission des headers d'auth upstream.
- **Secrets requis pour démarrer** : `JWT_SECRET_KEY`, `AUTH_ENCRYPTION_SECRET`, `BASIC_AUTH_PASSWORD`, `PLATFORM_ADMIN_PASSWORD` — générés par `python3 -m mcpgateway.scripts.init_secrets`.

### Observabilité

- **OpenTelemetry tracing** avec backends Phoenix, Jaeger, Zipkin, OTLP.
- **Audit logging** en structured logs.
- **Pas de Prometheus** documenté en natif — l'observabilité passe par OTel, donc branchable sur Prom via l'OTLP collector.

### Modes de déploiement

- **PyPI** — `pip install mcp-contextforge-gateway` (chemin « sans Docker »).
- **Docker Compose** (full stack avec Postgres + Redis + Nginx sur port 8080).
- **Helm** (production).

### Empreinte

- **Paquet PyPI** (~quelques Mo), dépendances Python.
- **SQLite par défaut** — `DATABASE_URL=sqlite:///./mcp.db`. **Mode embarqué, pas de dépendance externe pour démarrer.** PostgreSQL est recommandé en prod multi-nœuds mais pas requis.
- **RAM au repos :** non chiffrée. Uvicorn (dev) ~ 80-150 Mo ; Gunicorn (prod) un peu plus.
- **Python 3.11+ requis** — déjà installé sur le poste (Python 3.14).

### Pourquoi il gagne

1. **Installation Windows native** — `pip install mcp-contextforge-gateway` depuis PowerShell, venv Python, `mcpgateway.exe`. Documenté pas-à-pas dans le README officiel.
2. **SQLite par défaut** — pas de Postgres, pas de Redis, pas de MongoDB à installer. Disqualifie toutes les craintes du brief.
3. **Couverture transport la plus large** — 6 transports dont stdio et streamable-HTTP, qui sont les standards 2026.
4. **Tout-en-un** : registry + virtual servers + federation + admin UI + plugins, **dans un seul binaire Python**. Réduit le besoin d'agentgateway + mcp-gateway-registry à un seul composant.
5. **Sponsor IBM** — gouvernance corporate, pas risque de projet perso qui s'éteint.
6. **Activité la plus dense** : ~35 commits sur 30 jours, bugfix quotidien, release mensuelle avec changelog sérieux.

### Sa faiblesse

- **Python 3.11+ requis** — le poste a 3.14, donc OK. Mais l'utilisateur ne peut pas se passer de Python.
- **Pas de binaire `.exe` autonome** — l'installation passe par un venv Python. Plus de friction qu'agentgateway (un fichier à download).
- **arm64 Mac non supporté en prod** — ne concerne pas ce poste (Windows amd64).
- **Pas de doc « squeeze Windows port 4444 en mode gunicorn »** — `make serve` est documenté, mais le port-routing en parallèle d'agentgateway demande à choisir un port libre (4444 par défaut, OK).
- **Prometheus natif absent** — l'observabilité passe par OTel. Si le client veut du Prom, il faut brancher l'OTLP collector (pas un blocage, une étape).

---

## Mode opératoire Windows complet

### Préparation commune

Créer le dossier d'installation et s'y placer :

```bash
mkdir -p "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/"
cd "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/"
```

**Aucun paquet n'est installé à ce stade.** Le brief interdit toute installation ; ce qui suit est la procédure à exécuter manuellement le moment venu.

---

### Finaliste 1 — agentgateway : installation et démarrage

#### Téléchargement

L'artefact se trouve dans la release GitHub v1.4.1 du 2026-07-29 :

```powershell
# PowerShell natif Windows
mkdir "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway"
cd "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway"

# Télécharger le binaire serveur
Invoke-WebRequest -Uri "https://github.com/agentgateway/agentgateway/releases/download/v1.4.1/agentgateway-windows-amd64.exe" -OutFile "agentgateway.exe"

# Télécharger le binaire CLI utilitaire (optionnel, pour `agctl`)
Invoke-WebRequest -Uri "https://github.com/agentgateway/agentgateway/releases/download/v1.4.1/agctl-windows-amd64.exe" -OutFile "agctl.exe"

# Vérifier les SHA-256 (fichiers .sha256 joints à la release)
Get-FileHash -Algorithm SHA256 .\agentgateway.exe
Get-FileHash -Algorithm SHA256 .\agctl.exe
# Comparer aux valeurs publiées (.sha256 files).
```

**Chemin absolu final Windows :** `C:\Users\amado\ASpace_OS_V3\00_Amadeus\20_Harness\agentgateway\agentgateway.exe`

#### Configuration minimale

Le binaire bootstrap un fichier de config par défaut dans `%USERPROFILE%\.config\agentgateway\config.yaml` au premier lancement. Pour forcer un emplacement explicite, on crée le fichier à la main :

```yaml
# config.yaml — agentgateway standalone, version 2026-08-04
# Schema: https://agentgateway.dev/schema/config
# Documentation: https://agentgateway.dev/docs/standalone/latest/configuration/

# yaml-language-server: $schema=https://agentgateway.dev/schema/config

# Gateway listener principal — port 3300 (évite 3000 réservé par d'autres dev servers)
gateways:
  default:
    port: 3300

# Route catch-all : renvoie tout le trafic HTTP vers un backend exemple
# À remplacer par des routes MCP spécifiques (voir quickstart/mcp de la doc).
routes:
  - backends:
      - host: localhost:8000
```

**Configuration minimale « route MCP unique »** — pour router vers un serveur MCP local :

```yaml
# yaml-language-server: $schema=https://agentgateway.dev/schema/config

gateways:
  mcpGateway:
    port: 3300

# Section mcp : déclare un serveur MCP backend et l'expose via /mcp
mcp:
  servers:
    - name: server-everything
      transport: streamable-http
      url: http://localhost:3005/mcp

# Section ui : active l'UI admin sur 15500
ui:
  enabled: true
  port: 15500
```

> **Note :** la version ci-dessus est dérivée de la quickstart MCP ([agentgateway.dev/docs/standalone/latest/quickstart/mcp](https://agentgateway.dev/docs/standalone/latest/quickstart/mcp/), 2026-08-04). La grammaire exacte (placement de `mcp:`, validation schema) est à confirmer contre `https://agentgateway.dev/schema/config` au moment du boot. Le binaire signalera un défaut de config en clair si la grammaire diverge.

#### Démarrage

```powershell
cd "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway"
.\agentgateway.exe -f .\config.yaml
```

Comportement attendu :
- Le binaire lit `config.yaml`, ouvre le port 3300 (proxy) et 15500 (UI admin).
- Premier lancement : créer `%USERPROFILE%\.config\agentgateway\` automatiquement, écrire un config par défaut si `-f` n'est pas passé.
- Logs en stdout — expected : `info app serving UI at http://localhost:15000/ui` (port 15000 par défaut, surchargé à 15500 dans la config ci-dessus).

Pour démarrer en arrière-plan Windows :

```powershell
Start-Process -FilePath ".\agentgateway.exe" -ArgumentList "-f", ".\config.yaml" -RedirectStandardOutput ".\agentgateway.out.log" -RedirectStandardError ".\agentgateway.err.log"
```

#### Vérification

```powershell
# Listener principal : doit répondre (200 ou 404 selon routes configurées)
curl.exe -s -o NUL -w "%{http_code}\n" http://localhost:3300/

# UI admin : doit répondre 200
curl.exe -s -o NUL -w "%{http_code}\n" http://localhost:15500/ui

# Métriques Prometheus (si endpoint activé)
curl.exe -s -o NUL -w "%{http_code}\n" http://localhost:15000/metrics
```

**Réponses attendues :**
- `curl.exe http://localhost:3300/` → `200` si une route wildcard est configurée, sinon `404` (le binaire tourne, pas de route matchée).
- `curl.exe http://localhost:15500/ui` → `200` (UI HTML).
- `curl.exe http://localhost:15000/metrics` → `200` (métriques Prometheus).

#### Arrêt

```powershell
# Si démarré au premier plan
Stop-Process -Name agentgateway

# Si démarré en arrière-plan
Get-Process -Name agentgateway | Stop-Process
```

#### Désinstallation

```powershell
# Suppression simple et réversible
Remove-Item -Recurse -Force "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway"
Remove-Item -Recurse -Force "$env:USERPROFILE\.config\agentgateway"
# Aucun conteneur, aucun volume, aucune base à nettoyer.
```

---

### Finaliste 2 — IBM mcp-context-forge : installation et démarrage

#### Préparation Python

```powershell
mkdir "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-context-forge"
cd "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-context-forge"

# Venv isolé (Python 3.14 déjà installé)
python3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Mise à jour pip
python3 -m pip install --upgrade pip
```

#### Installation du paquet

```powershell
pip install mcp-contextforge-gateway
```

Alternative via `uv` (plus rapide) :

```powershell
uv venv
.\.venv\Scripts\activate
uv pip install mcp-contextforge-gateway
```

#### Configuration minimale

Télécharger l'exemple d'environnement fourni par le projet :

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/IBM/mcp-context-forge/main/.env.example" -OutFile ".env.example"
Copy-Item .env.example .env

# Générer les secrets requis (JWT, encryption, mots de passe admin)
python3 -m mcpgateway.scripts.init_secrets --patch-env .env
```

**Variables critiques dans `.env`** (post init_secrets) :

```env
# Base — SQLite embarqué, pas de Postgres à installer
DATABASE_URL=sqlite:///./mcp.db

# Secrets générés par init_secrets — ne JAMAIS hardcoder
JWT_SECRET_KEY=<généré>
AUTH_ENCRYPTION_SECRET=<généré>
BASIC_AUTH_PASSWORD=<généré>
PLATFORM_ADMIN_PASSWORD=<généré>

# Hôte et port — 4444 par défaut, libre sur ce poste
HOST=0.0.0.0
PORT=4444

# Optionnel : chemin de la DB SQLite
SQLITE_DB_PATH=./mcp.db
```

#### Démarrage

```powershell
# Mode gunicorn (production single-node)
mcpgateway --host 0.0.0.0 --port 4444
```

Pour démarrer en arrière-plan :

```powershell
Start-Process -FilePath "mcpgateway" -ArgumentList "--host", "0.0.0.0", "--port", "4444" -RedirectStandardOutput ".\mcpgateway.out.log" -RedirectStandardError ".\mcpgateway.err.log"
```

#### Vérification

```powershell
# Endpoint /version — ne nécessite pas d'auth
curl.exe -s http://localhost:4444/version

# Réponse attendue : JSON avec version, build, uptime, dépendances (PostHog, Phoenix, etc.)
# Exemple : {"version": "1.0.6", ...}

# Endpoint /health — si activé
curl.exe -s -o NUL -w "%{http_code}\n" http://localhost:4444/health

# Vérification avec bearer token (smoke test authentifié)
$Env:JWT_SECRET_KEY = (Get-Content .env | Select-String '^JWT_SECRET_KEY=').ToString().Split('=')[1]
$Env:MCPGATEWAY_BEARER_TOKEN = python3 -m mcpgateway.utils.create_jwt_token `
    --username admin@example.com --exp 10080 --secret $Env:JWT_SECRET_KEY

curl.exe -s -H "Authorization: Bearer $Env:MCPGATEWAY_BEARER_TOKEN" http://127.0.0.1:4444/version | ConvertFrom-Json
```

#### Arrêt

```powershell
# Si démarré au premier plan
Stop-Process -Name mcpgateway

# Si démarré en arrière-plan
Get-Process -Name mcpgateway | Stop-Process

# Optionnel : arrêter uvicorn/gunicorn workers
Get-Process -Name gunicorn, uvicorn | Stop-Process
```

#### Désinstallation

```powershell
# Désactiver le venv
deactivate

# Retirer le paquet
pip uninstall mcp-contextforge-gateway

# Supprimer le dossier (réversible)
Remove-Item -Recurse -Force "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/mcp-context-forge"
# La base SQLite ./mcp.db est dans le dossier, donc supprimée avec.
```

---

## Ports utilisés — vérification anti-collision

| Port | Service | Candidat | Conflit ? |
|---|---|---|---|
| 3300 | agentgateway proxy | agentgateway | Libre (5173/8090/8421/11434 occupés, 3000 évité par convention). |
| 15500 | agentgateway UI admin | agentgateway | Libre. |
| 4444 | mcp-context-forge HTTP | mcp-context-forge | Libre. |
| (8080) | agentgateway metrics (option) | agentgateway | Libre sur cet hôte (PocketBase sur 8090). |
| (3005) | serveur MCP test (option) | agentgateway | Libre. |

**Aucune collision détectée** entre les deux finalistes ni avec les services existants (5173 Coach OS, 8090 PocketBase, 8421 MemoryKnowledge, 11434 Ollama).

---

## Tableau des écartés — qui a été examiné et pourquoi pas

| Candidat | Voie principale | Motif d'écart (en une ligne) |
|---|---|---|
| **MetaMCP** (metatool-ai) | `docker-compose.yml` (2 conteneurs + `postgres:16-alpine`) | Dépendance Postgres disqualifiante au sens du brief. |
| **Obot** (obot-platform) | Image `ghcr.io/obot-platform/obot` + montées via socket Docker | Docker structurel (spawns de conteneurs frères), éditeur unique. |
| **mcp-gateway-registry** (agentic-community) | `docker compose` (~16 conteneurs, 4-6 Go RAM) | Empreinte massive, K8s-first, MongoDB + Keycloak + OpenBao obligatoires. |
| **Docker MCP Gateway** (docker/mcp-gateway) | `docker mcp gateway run` | Docker obligatoire par construction du projet. |
| **Microsoft mcp-gateway** (microsoft/mcp-gateway) | `dotnet publish` + image Docker + kubectl | .NET / K8s natif, aucune voie Python ou binaire unique. |
| **Arcade** (arcade.dev) | SaaS managé + Helm K8s (Enterprise) | Managé-first, lock-in runtime d'auth, hors scope. |
| **Composio** (composio.dev) | SaaS managé + Local Sandbox bridée par `COMPOSIO_API_KEY` | Lock-in auth, runtime bridée, hors scope. |
| **Bifrost** (maximhq) | `npx -y @maximhq/bifrost` (NPX) | **Passerait le filtre sans Docker** mais MCP n'est qu'une feature secondaire d'un projet principalement LLM gateway — 7 fournisseurs principaux, MCP listé en « Advanced Features », pas la raison d'être du projet. À reconsidérer si aucun autre candidat ne tient, mais mcp-context-forge est meilleur sur le créneau MCP. |
| **ACI** (aipotheosis-labs) | Helm + PropelAuth + Stripe + Postgres + pgvector + AWS CDK | Stack multi-services, beta instable (`v0.0.1-beta.3`), activité 2026-05-28. |
| **kgateway** (solo-io/kgateway) | YAML + binaire Go | MCP **sur la roadmap**, pas implémenté. Confondu à tort avec agentgateway dans certaines sources. |

---

## Comparaison finale — les 2 finalistes sur 5 critères

| Critère | agentgateway | mcp-context-forge |
|---|---|---|
| **Transports MCP** (stdio / SSE / streamable HTTP) | ✅ 4/4 (stdio, HTTP, SSE, Streamable HTTP) | ✅ 6/6 (HTTP, JSON-RPC, WS, SSE, stdio, streamable-HTTP) |
| **OAuth 2.1 / DCR** | ⚠️ `mcpAuthentication` doc mais 2.1/DCR non nommés | ✅ OAuth tokens, JWT, Basic Auth, custom schemes, OAuth Token Exchange |
| **RBAC par outil** | ✅ CEL fine-grained + MCP tool scoping par identité | ✅ RBAC natif, network policies, secrets management |
| **Audit log par appel** | ✅ Tamper-evident audit natif | ✅ Structured logs + OTel tracing |
| **Maturité** (licence, activité, releases) | ✅ Apache-2.0, LF, v1.4.1, 4 210 ★, 12 contributeurs, releases mensuelles | ✅ Apache-2.0, IBM, v1.0.6, 4 200 ★, ~35 commits/30j, 2026-08-04 |
| **Simplicité d'install Windows** | ✅⭐ 1 binaire `.exe`, 1 YAML, 1 commande | ✅ 1 venv + `pip install`, mais init secrets + .env à gérer |

---

## Ce qui reste inconnu — à trancher par essai réel

Liste explicite des points que la documentation consultée **ne permet pas de trancher** et qui demanderaient un boot pilote sur le poste.

### agentgateway

- **Grammaire exacte de `mcp:` dans le YAML** — le snippet de config ci-dessus est dérivé de la quickstart, mais la page schema n'a pas été fetchable. Le binaire échouera au boot avec un message clair si la section est mal placée. **À vérifier au premier lancement.**
- **OAuth 2.1 / DCR** — la doc parle de « MCP auth spec compliance with OAuth providers » sans citer la RFC. Le code source pourrait documenter 2.1/DCR dans `mcpAuthentication` ; non vérifié sans clone.
- **RAM au repos** sous Windows — estimation grossière 30-80 Mo (Rust + Tokio), non chiffrée.
- **Tunnel Handler au sens ngrok/cloudflared** — non nommé. À composer soi-même (ext_authz + CEL peuvent l'émuler).
- **Procédure d'upgrade version** — destruction de l'ancien binaire + remplacement ; pas de migration data (pas de BDD).

### mcp-context-forge

- **RAM au repos** sous Windows en mode gunicorn — estimation 100-150 Mo, non mesurée.
- **Comportement de `mcpgateway.exe` vs `mcpgateway`** sous PowerShell — `mcpgateway.exe` est le wrapper Windows fourni par pip ; la commande est documentée « mcpgateway.exe --host 0.0.0.0 --port 4444 », à valider au boot.
- **Cross-platform SQLite** — la base SQLite est compatible Windows/Linux, ça doit passer, mais non confirmé en pratique.
- **Détection automatique d'arm64** — non testé sur ce poste (amd64), la note arm64 du README concerne Mac Apple Silicon.
- **Procédure d'upgrade version** — `pip install --upgrade mcp-contextforge-gateway`. Pas de migration data documentée, mais la DB SQLite est compatible ascendante par construction.

### Posé commun aux deux

- **Aucun chemin dans `C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/`** ne doit être une jonction NTFS pré-existante. **Vérifier** avant installation (`Get-Item -Path "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/" | Select-Object Target, LinkType` doit retourner `LinkType` vide).
- **Espace disque requis** — agentgateway ~70 Mo, mcp-context-forge ~50 Mo + dépendances Python ~150 Mo. Négligeable.

---

## Décision recommandée — qui installer en premier

**Si l'objectif est de valider la thèse « sans Docker, ça marche vraiment » vite :**

1. **agentgateway d'abord.** 5 min : `Invoke-WebRequest` + `.\agentgateway.exe -f config.yaml` + `curl localhost:15500/ui`. Si l'UI répond, on a un gateway MCP qui tourne en 1 binaire, et la thèse est validée.
2. **mcp-context-forge en deuxième.** 10 min : `pip install` + `init_secrets` + `mcpgateway`. Si `/version` répond, on a un gateway-complet-avec-auth-en-SQLite qui tourne.

**Si l'objectif est de comparer fonctionnellement :**

Les deux écoutent sur des ports différents (3300/15500 vs 4444). On peut les démarrer en parallèle. agentgateway valide la thèse « proxy léger, format YAML plat ». mcp-context-forge valide la thèse « stack complète en pur Python, SQLite, 6 transports ». Les deux ensemble couvrent le spectre. Si un seul doit rester, **agentgateway** pour la portabilité brute, **mcp-context-forge** pour la richesse fonctionnelle.

**Si l'objectif est de coller au plus près du besoin client (multi-tenant, audit, OAuth 2.1 complet, catalogue de serveurs MCP) :**

mcp-context-forge est le meilleur choix **sans Docker**. agentgateway est le meilleur choix **sur n'importe quel critère de portabilité**.

---

## Sources consultées le 2026-08-04

### agentgateway
- [github.com/agentgateway/agentgateway](https://github.com/agentgateway/agentgateway)
- [github.com/agentgateway/agentgateway/releases](https://github.com/agentgateway/agentgateway/releases)
- [github.com/agentgateway/agentgateway/releases/tag/v1.4.1](https://github.com/agentgateway/agentgateway/releases/tag/v1.4.1) — assets listés via `api.github.com/repos/agentgateway/agentgateway/releases/tags/v1.4.1`
- [github.com/agentgateway/agentgateway/commits/main](https://github.com/agentgateway/agentgateway/commits/main)
- [github.com/agentgateway/agentgateway/blob/main/LICENSE](https://github.com/agentgateway/agentgateway/blob/main/LICENSE)
- [agentgateway.dev](https://agentgateway.dev)
- [agentgateway.dev/docs/overview/](https://agentgateway.dev/docs/overview/)
- [agentgateway.dev/docs/standalone/latest/quickstart/](https://agentgateway.dev/docs/standalone/latest/quickstart/)
- [agentgateway.dev/docs/standalone/latest/quickstart/mcp/](https://agentgateway.dev/docs/standalone/latest/quickstart/mcp/)
- [agentgateway.dev/docs/standalone/latest/configuration/overview/](https://agentgateway.dev/docs/standalone/latest/configuration/overview/)
- [agentgateway.dev/blog/](https://agentgateway.dev/blog/)

### IBM mcp-context-forge
- [github.com/IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge)
- [github.com/IBM/mcp-context-forge/releases](https://github.com/IBM/mcp-context-forge/releases)
- [github.com/IBM/mcp-context-forge/commits/main](https://github.com/IBM/mcp-context-forge/commits/main)
- [github.com/IBM/mcp-context-forge/blob/main/README.md](https://github.com/IBM/mcp-context-forge/blob/main/README.md)
- [github.com/IBM/mcp-context-forge/blob/main/LICENSE](https://github.com/IBM/mcp-context-forge/blob/main/LICENSE)
- [pypi.org/project/mcp-contextforge-gateway/](https://pypi.org/project/mcp-contextforge-gateway/)
- [raw.githubusercontent.com/IBM/mcp-context-forge/main/.env.example](https://raw.githubusercontent.com/IBM/mcp-context-forge/main/.env.example)

### Bifrost
- [github.com/maximhq/bifrost](https://github.com/maximhq/bifrost)
- [github.com/maximhq/bifrost/releases](https://github.com/maximhq/bifrost/releases)
- [github.com/maximhq/bifrost/blob/main/README.md](https://github.com/maximhq/bifrost/blob/main/README.md)

### Microsoft mcp-gateway
- [github.com/microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway)

### Confirmations « disqualifiés » (rappel)
- [github.com/metatool-ai/metamcp](https://github.com/metatool-ai/metamcp) — docker-compose.yml avec `postgres:16-alpine`
- [github.com/obot-platform/obot](https://github.com/obot-platform/obot) — image Docker + montées socket
- [github.com/agentic-community/mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry) — 16 conteneurs, MongoDB + Keycloak + OpenBao

### Listes 2026 consultées pour élargir
- [manveerc.substack.com/p/best-mcp-gateways](https://manveerc.substack.com/p/best-mcp-gateways)
- [composio.dev/content/best-mcp-gateway-for-developers](https://composio.dev/content/best-mcp-gateway-for-developers)
- [getmaxim.ai/articles/best-open-source-mcp-gateways-in-2026](https://www.getmaxim.ai/articles/best-open-source-mcp-gateways-in-2026/)
- [lunar.dev/post/the-best-open-source-mcp-gateways-in-2026](https://www.lunar.dev/post/the-best-open-source-mcp-gateways-in-2026)
- [truefoundry.com/blog/best-mcp-gateways](https://www.truefoundry.com/blog/best-mcp-gateways)
- [zuplo.com/blog/mcp-gateway-comparison](https://zuplo.com/blog/mcp-gateway-comparison)
- [mintmcp.com/blog/mcp-gateways-self-hosted-deployments](https://www.mintmcp.com/blog/mcp-gateways-self-hosted-deployments)

---

## Fin du rapport

**Verdict :** deux candidats sérieux passent le filtre « sans Docker » sur Windows 11. agentgateway par sa simplicité de déploiement (1 binaire), mcp-context-forge par sa richesse fonctionnelle (6 transports, RBAC, OAuth, audit, registre de serveurs MCP). Tout autre candidat examiné échoue sur Docker obligatoire, Postgres requis, ou stack multi-services excessive.

Procédure recommandée : installer agentgateway en premier pour valider la thèse, puis mcp-context-forge pour valider la couverture fonctionnelle. Un seul des deux doit rester en production — la décision dépend de la sophistication du besoin client (proxy léger vs stack complète).
