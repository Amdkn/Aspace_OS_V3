# Citadelle A0 — Local P0 Dashboard

> **Statut** : P0 GREEN (2026-07-04T20:03 ET, awaiting Gate #2 page Décisions).
> **Doctrine** : lecture seule — anti-Ultron — dormants affichés dormants.

## Quickstart

```powershell
cd C:\Users\amado\agent-os\citadel
.\serve.ps1 -RunCollectors   # run 3 collectors + start server
```

Endpoints:

- `http://127.0.0.1:8770/` — Bridge (Overview UI)
- `http://127.0.0.1:8770/api/health` — health check
- `http://127.0.0.1:8770/api/harnesses` — Pilier 1 (Models)
- `http://127.0.0.1:8770/api/skills` — Pilier 4 (Skills)
- `http://127.0.0.1:8770/api/connections` — Pilier 6 (MCP + crons + heartbeat)

Stop:

```powershell
.\serve.ps1 -Stop
```

## Structure

```
citadel/
├── README.md                  # ce fichier
├── serve.py                   # stdlib http.server :8770 + 6 endpoints
├── serve.ps1                  # Windows natif launcher (ADR-LD01-006 §C2)
├── collectors/                # idempotent Python (pattern collect_metrics.py)
│   ├── collector_01_harnesses.py    # CC/Hermes/MC/Codex/Omnigent + 2 dormants
│   ├── collector_04_skills.py       # ~/.claude/skills + ~/.hermes/skills
│   └── collector_06_connections.py  # MCP + crons + heartbeat
├── data/                      # JSON output (lecture serveur)
│   ├── 01_harnesses.json
│   ├── 04_skills.json
│   └── 06_connections.json
├── static/
│   └── bridge.html            # UI overview (no framework, vanilla JS)
├── decisions/                 # append-only D4 (Gate #2 gated page Décisions)
└── logs/
    └── citadel.log            # append-only
```

## Doctrine anti-Ultron (répétée parce que vitale)

1. **Lecture seule par défaut** : `serve.py` lit UNIQUEMENT `data/*.json` (sortie des collectors).
   Aucune mutation des sources canoniques (settings.json, mcp.json, skills/, ADR/, etc.).
2. **Écriture bornée** : `collectors/*.py` écrivent UNIQUEMENT `data/*.json` (overwrite idempotent).
   `decisions/*.json` append-only (Gate #2 à venir).
3. **Dormants affichés dormants** : Paperclip AI + Multica = `status: "dormant"`, jamais réveillés.
4. **Pas d'auto-approval** : aucune action batchée, aucun cron décisionnel, aucun ratify sans GO A+.
5. **Test mental** : *"Si Tony n'a pas dit quoi faire, Jarvis n'exécute rien d'irversible."*

## Sister chain

- **Source canon** : `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md`
- **Sister LD01** : `LD01/99_meta/00_plan_citadelle_a0_sister.md`
- **ADR** : `LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md`
- **Méthodologie** : `LD01/10_methodology/00_fable5_jack_roberts_meta_strategy.md` (Level 3 Jack)
- **Persistence Windows** : `LD01/30_decisions/ADR-LD01-006_strategy_session_meta_skill_canon.md §C2`

## Phasage

- ✅ **P0** (2026-07-04T20:03 ET) : squelette serveur + Bridge + 3 collectors piliers 1/4/6
- ⏳ **P1** (W5 lundi 2026-07-07+) : page Décisions + ratification 1-clic + Windows toast (Gate #2)
- ⏳ P2 (W5-6) : pages Agents/Frameworks/Domaines + Memory + auto-start (Gate #3)
- ⏳ P3 (W6-7) : Zora nightly + Harnesses contrôle sessions (Gate #4)
- ⏳ P4 (W7-8) : embed Life-OS-2026 Vercel (Gate #5)