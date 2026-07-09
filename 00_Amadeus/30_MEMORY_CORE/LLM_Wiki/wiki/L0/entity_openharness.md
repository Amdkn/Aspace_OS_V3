---
source: LLM_Wiki_A0
date: 2026-05-11
type: entity
domain: Tech_OS / L0_Agentic / OpenHarness
tags: [#entity #OpenHarness #Agentic #Autopilot #Multi-Provider #L0_Kernel]
---

# Entity: OpenHarness

> github.com/HKUDS/OpenHarness | v0.1.9 | pipx install openharness-ai

**OpenHarness** est le port Python open-source de Claude Code CLI — apporte un **autopilot loop queue-based** pour les tâches automatisées.

---

## Position dans A'Space OS

```
A0 Amadeus
    │
    ▼
Rick Prime (A1) ──► Claude Code CLI (primary, bypassPermissions)
              └──► OpenHarness (backup, autopilot loop)
                          │
                          └──► Hermes Agent (routing, port 3101)
```

**Relation avec les autres agents:**
- **[[entity_rick]]**: Rick govern OpenHarness comme outil A1 parallel
- **Claude Code CLI**: primary agent (bypassPermissions) — OpenHarness est le backup

---

## Fonctionnalités par Status

### ✅ Fonctionnel (v0.1.9)

| Feature | Status | Notes |
|---------|--------|-------|
| Session interactive | ✅ | `oh` |
| Headless (-p) | ✅ | `oh -p "prompt"` |
| Dry-run mode | ✅ | `oh --dry-run` |
| Autopilot loop | ✅ | `oh autopilot add / run-next` |
| Multi-provider | ✅ | Claude, OpenAI, Codex, Moonshot, MiniMax, GLM |
| Costs tracking | ✅ | |
| Streaming | ✅ | |
| CLAUDE.md discovery | ✅ | Scan auto au démarrage |

### ❌ Planifié (v0.2+)

| Feature | Status | Notes |
|---------|--------|-------|
| Memory management | ❌ | Planifié v0.2+ |
| Hooks system | ❌ | Planifié v0.2+ (PreToolUse/PostToolUse) |
| Channels (multi-agent) | ❌ | Planifié v0.2+ (Telegram, Discord, Slack...) |

---

## Commandes Clés

```bash
oh                        # Session interactive
oh -p "prompt"            # Single shot
oh --dry-run             # Preview safe
oh autopilot status      # Queue status
oh autopilot add idea "Title" --body "Task"
oh autopilot run-next    # Execute next card
oh autopilot journal     # Recent entries
oh autopilot install-cron  # Auto scan/tick

oh provider list         # Show providers
oh provider use claude   # Switch to Claude
```

---

## Comparaison: Claude Code vs OpenHarness

| Aspect | Claude Code | OpenHarness |
|--------|------------|-------------|
| Mode interactif | ✅ | ✅ |
| Headless | ✅ | ✅ |
| Autopilot loop | ❌ | ✅ |
| Multi-provider | ❌ | ✅ |
| Memory (natif) | ❌ | ❌ (planifié) |
| Hooks (natif) | settings.json | ❌ (planifié) |
| Channels | ❌ | ❌ (planifié) |

**Règle:** Tâches critiques → Claude Code. AutoResearch loop → OpenHarness.

---

## Inbounds

- [[ADR-RICK-001_openharness-incarnation]] — Décision d'architecture : OpenHarness = incarnation IA de Rick (A1), mécanisme Donna DLQ
- [[entity_rick]] — Rick govern l'outil en parallèlle de Claude Code
- [[concept_nano_squads]] — OpenHarness autopilot = Nano Squads execution layer

---

*Last updated: 2026-05-12 (reclassement)*
*Source: ADR-RICK-001_openharness-incarnation.md (anciennement SDD-008_openharness-integration.md, reclassé 2026-05-12)*