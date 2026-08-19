---
type: Concept
title: Symphony bus remplace N8N — orchestration L0 file-based
description: Le bus d'orchestration L0 est Symphony : files JSON en inboxes/outboxes filesystem, jamais WebSocket, jamais Redis. N8N est legacy depuis 2026-05-26.
tags: [tech, symphony, orchestration, bus, n8n]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: symph-001
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-001_symphony-replaces-n8n.md
    title: ADR-SYMPH-001 Symphony Bus Remplace N8N
    last_modified: 2026-05-26
  - id: symph-003
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-003_agent-os-standards-injection.md
    title: ADR-SYMPH-003 Agent OS = Standards Injection
    last_modified: 2026-06-06
okf_version: "0.2"
---

**Symphony** est le bus d'orchestration L0 canonique. Il remplace N8N (marqué legacy 2026-05-26) par un **pattern file-based**, pas un runtime à installer.

## Doctrine (extrait OpenAI Symphony SPEC)

- **Ephemeral tick sessions** — chaque tick = 1 process qui naît, exécute, meurt.
- **Multi-turn continuation** — l'état persiste dans des fichiers (`LLM_Wiki`, `memory/`, `pulse.log`), jamais en RAM.
- **Workspace persistence** — chaque agent capsule a son répertoire `Shadow_L0/agents/<X>/` immuable entre ticks.
- **No daemon** — Windows Task Scheduler fait office d'orchestrateur central.

## Tick cycle 8 phases

```
WAKE → PROBE → DECIDE → EXECUTE → OBSERVE → LEARN → SIGNAL → SLEEP
```

Chaque phase écrit 1 ligne dans `agent-os/pulse.log` (JSONL append-only, 14 champs, timestamps UTC ISO-8601). Aucune ligne n'est jamais réécrite ou supprimée (audit trail immuable), rotation hebdomadaire → `.archive/<date>.jsonl.gz`.

## Interface inter-agent

Tout message passe par le filesystem :

```
agents/<sender>/outbox/<timestamp>_<topic>.json
        │
        └─→ agents/<receiver>/inbox/<timestamp>_<topic>.json
                                │
                                └─→ après traitement : inbox/.done/
```

Format JSON minimal :

```json
{
  "from": "Claude_Code_CLI",
  "to": "Codex_CLI",
  "topic": "vps-provision-nexus",
  "intent": "execute_sop",
  "sop_id": "SOP-L2-IT-001",
  "context_pack_url": "https://notion.so/...",
  "deadline_iso": "2026-05-26T18:00:00Z",
  "trust_required": "requires_signoff"
}
```

**Pas de WebSocket, pas de gRPC, pas de Redis.** Files only.

## Injection de standards (ADR-SYMPH-003)

Chaque tick Symphony consomme `agent-os/standards/index.yml` et injecte au moins 1 standard par phase de décision (PROBE/DECIDE/EXECUTE/OBSERVE/SIGNAL). Format Markdown brut, tronqué à 1 écran. Sans standards injectés, la décision n'est pas justifiable.

## Substituts N8N

| Cas d'usage N8N | Substitut Symphony |
|------------------|---------------------|
| Webhook → action | Tick handler dans `agents/<X>/skills/<event>.ps1` |
| Cron scheduling | Windows Task Scheduler → `heartbeat-tick.ps1 <agent>` |
| Sync Notion → Supabase | Skill dédié sur Doctor 11 (Interface) |
| LLM call dans pipeline | Direct via Claude / Gemini / Codex CLI ephemeral session |

## Quota & fallback chain (par Doctor)

| Doctor | 1er choix | 2e fallback | 3e last resort |
|--------|-----------|-------------|----------------|
| 13ème (L0) | Codex CLI | Gemini CLI | Claude Code |
| 12ème (L2) | Gemini CLI | Claude Code | Codex CLI |
| 11ème (L1) | Claude Code | Gemini CLI | Codex CLI |

Symphony détecte les rate-limits via code de retour CLI et bascule automatiquement.

Voir aussi : [[paniques-k1-k4-kernel]], [[mcp-doctrine-six]], [[axiomes-antifragilite-k1-k4]].