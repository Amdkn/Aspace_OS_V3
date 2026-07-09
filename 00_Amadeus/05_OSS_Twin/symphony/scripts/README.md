# Symphony × Agent OS — Scripts

## Symphony UI Server (Grafana-lite) — http://127.0.0.1:8080

`scripts/symphony-ui-server.py` est un serveur HTTP léger (stdlib Python uniquement, zéro dépendance) qui sert une UI d'observabilité 8 phases sur **http://127.0.0.1:8080/**.

### Endpoints

| Method | Path | Description |
|---|---|---|
| GET  | `/`                        | Dashboard HTML (single page) |
| GET  | `/static/<file>`           | CSS/JS assets |
| GET  | `/api/health`              | Health check (status, pulse line count, standards count) |
| GET  | `/api/snapshot`            | Métriques agrégées (tick_count, total cost, standards used, phases seen, last decision) |
| GET  | `/api/pulse?last=N`        | Last N lines of pulse.log (parsed JSONL) |
| GET  | `/api/standards`           | Liste des standards avec descriptions |
| GET  | `/api/standards/<name>`    | Contenu brut d'un standard .md |
| GET  | `/api/cost`                | Coût agrégé par phase |
| GET  | `/api/phase-stats`         | Durée moyenne + count par phase (bar chart data) |
| POST | `/api/tick`                | Trigger un tick demo (re-run `symphony-tick-demo.sh` en subprocess) |

### Lancer

```bash
cd "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony"
C:/Python314/python.exe scripts/symphony-ui-server.py
```

Options env :
- `SYMPHONY_UI_PORT=8080` (default)
- `SYMPHONY_UI_HOST=127.0.0.1` (default, localhost only — pas d'exposition LAN)

### UI sections
1. **Header** : status (● vert pulse), clock live, **▶ Trigger tick**, **↻ Refresh**, auto-refresh toggle
2. **Standards** (gauche) : 11 standards cliquables, descriptions inline, click pour expand le .md
3. **Pulse stream** (centre) : 8 phases colorées (WAKE→SLEEP), auto-scroll, métriques inline (duration/cost/issue)
4. **Cost chart** (haut-droite) : bar chart CSS-only, coût par phase
5. **Duration chart** (milieu-droite) : bar chart, durée moyenne par phase
6. **Snapshot** (bas) : workflow, tick_count, total cost, last decision (color-coded PASS/BLOCKED/CONDITIONAL), standards used (tags), phases seen

### Notes
- Stdlib Python uniquement (http.server, json, socketserver, subprocess). Zéro `pip install`.
- Bind 127.0.0.1 = localhost only. Pour LAN, override `SYMPHONY_UI_HOST=0.0.0.0` (avec garde-fou A0).
- Le tick trigger lance le demo handler (bash) en subprocess, ne bloque pas l'API.
- Polling frontend = 1.5s (configurable dans `dashboard.js`).
- Artefact runnable, validé 2026-06-06 avec screenshot Playwright 1400×900.

## Demo Tick Handlers

Voir `symphony-tick-demo.sh` (Bash) et `symphony-tick-demo.ps1` (PowerShell) — produisent le même `pulse.log` schema-conforme.
