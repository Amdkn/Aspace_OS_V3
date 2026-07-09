# ADR-RICK-001 — OpenHarness/OpenHermes : L'Incarnation de Rick (A1)

**Date de décision :** 2026-05-11
**Date de reclassement :** 2026-05-12 (SDD-008 → ADR-RICK-001)
**Auteur :** A0 (Claude Code — Sovereign Oversight) + reclassement Architect 2026-05-12
**Statut :** RATIFIÉ — Décision d'architecture validée
**Type :** Architecture Decision Record (était SDD-008, reclassé en ADR pour respecter la typologie SPAD)
**Portée :** A1 Rick Prime + A2 Doctors + A3 Companions + Donna DLQ

## Décision

**OpenHarness (alias OpenHermes) est l'incarnation IA de Rick (A1) dans L0 Tech OS.**

Il joue trois rôles indivisibles :
1. **Souveraineté agentique** — multi-provider, autopilot loop, indépendant d'Anthropic
2. **Mécanisme Donna DLQ** — remonte les erreurs des A3 Compagnons (via Hermes) vers les A2 Doctors (Claude Code) et finalement vers A1 Rick (OpenHarness lui-même) pour traitement souverain
3. **Pont inter-providers** — Claude / OpenAI / Codex / Copilot / Moonshot / MiniMax / GLM dans un seul harnais

## Chaîne d'escalade Donna (verbatim Amadeus 2026-05-12)

```
A3 Compagnons (sur Hermes)
        │
        ▼ erreur capturée
   Donna DLQ
        │
        ▼ remontée
A2 Doctors (sur Claude Code)
        │
        ▼ si non résoluble
A1 Rick (sur OpenHarness)
        │
        ▼ arbitrage souverain
   Décision finale
```

OpenHarness n'est donc **pas un simple "agent autopilot"** — c'est le **dernier recours** avant que le système ne renvoie une erreur au Pilote Amadeus.

## Cartographie des outils IA par Couche

| Couche | Entité | Outil IA |
|---|---|---|
| **Méta-A0** (hors univers Amadeus) | Le superviseur du Jumeau Numérique | **Miro Fish** ([github.com/666ghj/MiroFish](https://github.com/666ghj/MiroFish)) |
| **A0** | Jumeau Numérique Amadeus | Claude Code (Architecte Souverain) |
| **L0** | Rick (A1 — Souveraineté) | **OpenHarness / OpenHermes** ← cet ADR |
| **L1** | Beth + Morty (A1 Life OS) | À définir (TBD — peut-être Claude Code via Shadow L1 outils) |
| **L2** | Jerry + Summer (A1 Business) | À définir (TBD — peut-être OpenHarness pour la SOB Factory) |

→ Note : la cartographie L1/L2 est ouverte et fera l'objet d'ADRs futurs (`ADR-BETH-001`, `ADR-JERRY-001`).

## Références
- SDD-000 : Constitution Rick's Verse (Anti-Panic, Framework Configs)
- SDD-001 : Solarpunk Kernel Core
- SDD-002 : A1 Rick Harness (Karpathy Pattern, line_density_score)
- SDD-003 : TARDIS Protocol Orchestration (Yaz → Ryan → Graham → Donna)
- OpenHarness : [github.com/HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) — v0.1.9
- Meta-Harness : [arxiv.org/abs/2603.28052](https://arxiv.org/abs/2603.28052) — Outer-loop optimization

---

## 1. Contexte et Problématique

### 1.1 État Actuel

A'Space OS utilise actuellement :
- **Claude Code CLI** comme agent principal (bypassPermissions via settings.json)
- **Hermes Agent** (port 3101) comme service de routage
- **Paperclip AI** comme control plane heartbeat-based
- **OpenClaw** pour subagent sandboxing

### 1.2 Limites Identifiées

| Composant | Limite |
|-----------|--------|
| Claude Code CLI | Mode interactif only, pas de session resume robuste |
| Hermes Agent | Routing basique, pas de memory natif |
| Paperclip AI | Budget hard-stop, pas de multi-provider |
| OpenClaw | DM-pairing complexe, pas de streaming |

### 1.3 Solution : OpenHarness

**OpenHarness** est un port Python open-source de Claude Code qui apporte :
- **Autopilot service** — Queue-based task runner avec scan/tick loop ✅
- **Memory management** — Planifié mais non implémenté dans v0.1.9 ❌
- **Hooks system** — Planifié mais non implémenté dans v0.1.9 ❌
- **Multi-provider** — Claude, OpenAI, Codex, Copilot, Moonshot, MiniMax ✅
- **Channels** — Planifié mais non implémenté dans v0.1.9 ❌
- **Dry-run mode** — Preview sans exécution (safe testing) ✅

---

## 2. Architecture d'Intégration

### 2.1 Positionnement dans L0 Kernel

```
┌─────────────────────────────────────────────────────────────┐
│                    L0 SOLARPUNK KERNEL                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│   │   Claude    │    │ OpenHarness │    │   Hermes    │    │
│   │   Code      │    │    (oh)     │    │   Agent    │    │
│   │  (native)  │◄──►│  (parallel) │◄──►│  (routing) │    │
│   └─────────────┘    └─────────────┘    └─────────────┘    │
│         │                  │                  │            │
│         │                  │                  │            │
│         ▼                  ▼                  ▼            │
│   ┌─────────────────────────────────────────────────┐    │
│   │              A1 Rick Prime Harness                │    │
│   │  • Claude Code (primary) — bypassPermissions     │    │
│   │  • OpenHarness (backup) — autopilot loop        │    │
│   │  • Hermes (router) — message routing            │    │
│   └─────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Flux de Délégation Proposed

```
A0 (Amadeus)
    │
    ▼
Rick Prime (A1)
    │
    ├──► Claude Code CLI ──► Tâches critiques (bypassPermissions)
    │
    ├──► OpenHarness (oh) ──► Autopilot loop (queue-based task runner)
    │         │
    │         └──► Autopilot scan/tick ──► Task execution
    │         ❌ Memory scan — planifié v0.2+
    │         ❌ Hooks — planifié v0.2+
    │         ❌ Channels — planifié v0.2+
    │
    ▼
Doctors (A2) ──► Companions (A3)
```

### 2.3 Installation

```bash
# Via pipx (recommandé — isolation)
pipx install openharness-ai

# Commandes disponibles
oh          # Session interactive
ohmo        # Personal agent (Feishu/Slack/Telegram/Discord)
openh       # Alias Windows-compatible
openharness # Full name

# Version
oh --version  # 0.1.9
```

**Note:** `ohmo` (personal agent avec channels) n'est pas encore fonctionnel dans v0.1.9.

### 2.4 Configuration Provider

```bash
oh setup    # Wizard interactif — sélection provider + auth
oh provider list   # Liste des providers configurés
oh provider use <profile>  # Switch provider
```

**Providers supportés :**
| Provider | Type | Notes |
|----------|------|-------|
| Claude (Anthropic) | API key | Official |
| Claude Subscription | CLI bridge | Via ~/.claude/.credentials.json |
| OpenAI | API key | + OpenRouter, DeepSeek, Groq |
| Codex | CLI bridge | Subscription |
| Copilot | OAuth | GitHub device-flow |
| Moonshot/Kimi | API | reasoning_content support |
| MiniMax | API | Anthropic-compatible |
| GLM | API | Zhipu anthropic-compatible |

---

## 3. Modules Clés pour A'Space OS

### 3.1 Autopilot Service ✅

**Équivalent OpenHarness du pattern Karpathy AutoResearch :**

```bash
oh autopilot status         # Queue status
oh autopilot list           # List cards
oh autopilot add idea "Title" --body "Task"  # Add card
oh autopilot run-next      # Execute card end-to-end
oh autopilot journal       # Recent entries
oh autopilot install-cron  # Auto scan/tick
```

**Intégration Rick :**
- Remplacer le loop `rick.sh 001 prd` par `oh autopilot add + run-next`
- Le service maintient le loop via cron scan/tick
- Card = unité de travail (idea/issue/pr/claude)

### 3.2 Memory Management ❌ (Planifié v0.2+)

```python
# openharness/memory/manager.py
# Non implémenté dans v0.1.9
# CLAUDE.md discovery automatique — planifié
# MEMORY.md persistent session — planifié
# Context compression (auto-compact) — planifié
```

**Alternative actuelle:**
- OpenHarness scanne automatiquement les CLAUDE.md au démarrage
- LLM Wiki existant dans `30_MEMORY_CORE/LLM_Wiki/` pour la mémoire persistante

### 3.3 Hooks System ❌ (Planifié v0.2+)

**PreToolUse / PostToolUse comme governance :**
- Non implémenté dans v0.1.9
- Planifié mais pas encore développé

**Alternative actuelle A'Space :**
- Anti-Panic configs (bypassPermissions, budget, dmPolicy) dans settings.json
- DLQ routing (Donna) dans AGENTS.md
- Cross-tier communication rules dans SDD-000

### 3.4 Channels (Multi-Agent) ❌ (Planifié v0.2+)

```python
# openharness/channels/impl/
# Non implémenté dans v0.1.9
# Telegram, Discord, Slack, Feishu, DingTalk, WhatsApp, Email, QQ, Matrix
```

**Alternative actuelle A'Space :**
- Telegram MCP configuré (token manquant)
- Discord webhook dispo
- Hermes Agent (port 3101) pour routing inter-agent

---

## 4. Comparaison Framework

### 4.1 Claude Code vs OpenHarness

| Aspect | Claude Code CLI | OpenHarness |
|--------|-----------------|-------------|
| Mode interactif | ✅ | ✅ |
| Headless (-p) | ✅ | ✅ |
| Streaming | ✅ | ✅ |
| Autopilot loop | ❌ | ✅ (queue-based) |
| Memory management | Externe | ❌ (planifié v0.2+) |
| Hooks | Settings.json | ❌ (planifié v0.2+) |
| Multi-provider | ❌ | ✅ |
| Channels | ❌ | ❌ (planifié v0.2+) |
| Dry-run | `--dry-run` | `--dry-run` |
| Coûts tracking | ❌ | ✅ |

### 4.2 Sélection par Cas d'Usage

| Tâche | Outil Recommandé |
|-------|------------------|
| Tâche critique A1 | Claude Code (bypassPermissions) |
| AutoResearch loop | OpenHarness autopilot (queue-based) |
| Memory/Context | OpenHarness ❌ (planifié) / CLAUDE.md externe |
| Governance/Hooks | Claude Code (settings.json) |
| Multi-agent coordination | OpenHarness channels ❌ (planifié) |
| Subagent sandboxing | OpenClaw (existant) |
| Heartbeat autonomous | Paperclip AI (existant) |

---

## 5. Plan d'Intégration

### Phase 1 : Installation + Config (Jour 1)

```bash
# ✅ Déjà fait
pipx install openharness-ai

# Configuration provider
oh setup  # Choisir Claude comme provider principal

# Vérification
oh --dry-run -p "Test connection" --output-format json
```

### Phase 2 : Test Autopilot (Jour 1-2)

```bash
# Test du autopilot
oh autopilot status       # Statut du service
oh autopilot add idea "Test" --body "Liste les fichiers dans /srv/aspace"
oh autopilot run-next     # Exécute le card

# Test avec task simple
oh -p "Liste les fichiers dans /srv/aspace" --output-format json
```

### Phase 3 : Intégration Memory (Jour 2-3)

```bash
# ❌ Non implémenté dans v0.1.9
# oh memory scan  # Planifié pour v0.2+

# Alternative actuelle: CLAUDE.md discovery natif d'oh
# OpenHarness scanne automatiquement les CLAUDE.md au démarrage

# Pour l'instant, utiliser le LLM Wiki existant (30_MEMORY_CORE/LLM_Wiki/)
oh --dry-run -p "Analyse ce projet"
```

### Phase 4 : Hooks Governance (Jour 3-5)

```bash
# ❌ Non implémenté dans v0.1.9
# oh hooks list/enable/disable — planifié pour v0.2+

# Alternative actuelle: settings.json dans Claude Code
# + Anti-Panic configs (AGENTS.md)
```

### Phase 5 : Channels Integration (Jour 5-7)

```bash
# ❌ Non implémenté dans v0.1.9
# oh channels list/add/test/send — planifié pour v0.2+

# Alternative actuelle: Telegram MCP (déjà configuré)
# Via le MCP server Chrome DevTools ou plugin telegram
```

---

## 6. Commandes OpenHarness Utiles

### Session Management

```bash
oh                  # Session interactive
oh -p "prompt"     # Single shot
oh -c              # Continue last session
oh -r <session_id> # Resume specific session
oh --dry-run       # Preview sans exécution
```

### Output Formats

```bash
oh -p "prompt" --output-format text    # Default
oh -p "prompt" --output-format json     # Structured JSON
oh -p "prompt" --output-format stream-json  # Streaming events
```

### Provider Management

```bash
oh setup                    # Interactive setup wizard
oh provider list            # Show configured providers
oh provider use claude      # Switch to Claude
oh auth login              # Authenticate
oh auth status             # Check auth state
```

### Autopilot

```bash
oh autopilot status         # Check status
oh autopilot list           # List cards
oh autopilot add idea "Title" --body "Task description"  # Add card
oh autopilot run-next       # Run next queued card
oh autopilot journal        # View journal
oh autopilot context        # Show active repo context
oh autopilot install-cron   # Install cron for scan/tick
```

### Memory

```bash
# ❌ Non implémenté dans v0.1.9
# oh memory scan/compact/clear — planifié v0.2+

# Alternative: CLAUDE.md discovery natif + LLM Wiki externe
```

### Hooks

```bash
# ❌ Non implémenté dans v0.1.9
# oh hooks list/enable/disable/logs — planifié v0.2+

# Alternative: Claude Code settings.json + AGENTS.md Anti-Panic configs
```

### Channels

```bash
# ❌ Non implémenté dans v0.1.9
# oh channels list/add/test/send — planifié v0.2+

# Alternative actuelle: Telegram MCP (plugin chrome-devtools-mcp)
```

---

## 7. Risques et Mitigations

### 7.1 Risques Identifiés

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|-------------|
| Conflic avec Claude Code | Moyenne | Moyen | Run parallel, pas de replace |
| Memory pollution | N/A | N/A | Feature non implémenté v0.1.9 |
| Hooks trop restrictifs | N/A | N/A | Feature non implémenté v0.1.9 |
| Provider auth expiry | Faible | Haut | Monitoring + renewal |
| API 401 (clé MiniMax) | Faible | Haut | Credentials propre après bug de concaténation |

### 7.2 Mitigations

```bash
# Toujours tester en dry-run
oh --dry-run -p "task description"

# Monitoring hooks
oh hooks logs --follow

# Backup before major changes
cp -r ~/.openharness ~/.openharness.backup
```

---

## 8. Maintenance

### 8.1 Updates

```bash
pipx upgrade openharness-ai
oh --version  # Vérifier après upgrade
```

### 8.2 Logs

```bash
# Logs OpenHarness
ls ~/.openharness/logs/
cat ~/.openharness/logs/openharness.log

# Logs Autopilot
oh autopilot logs
```

### 8.3 Reset

```bash
# Reset configuration
oh setup --reset

# Clean memory
oh memory clear
rm -rf ~/.openharness/memory/*
```

---

## 9. Dépendances

| Composant | Version | Source |
|-----------|---------|--------|
| openharness-ai | 0.1.9 | pipx |
| Python | ≥3.10 | System |
| Claude API | — | ~/.claude/config |

---

## 10. Todo List

- [x] Installation OpenHarness via pipx (v0.1.9)
- [x] Configuration provider MiniMax (`oh auth login`)
- [x] Test session interactive (`oh`)
- [x] Test dry-run mode (`oh --dry-run`)
- [x] Tester autopilot (`oh autopilot add / run-next / completed ✅`)
- [ ] Configurer memory workspace — **Planifié v0.2+**
- [ ] Tester CLAUDE.md discovery — **Planifié v0.2+**
- [ ] Configurer hooks governance — **Planifié v0.2+**
- [ ] Integration Channels (Telegram etc.) — **Planifié v0.2+**
- [ ] Documentation opérateurs

**Note:** Memory, Hooks et Channels sont planifiés pour v0.2+. L'autopilot loop fonctionne correctement.

---

## Historique du document

| Date | Action | Auteur |
|------|--------|--------|
| 2026-05-11 | Création comme SDD-008_openharness-integration.md (ratifié) | A0 Claude Code |
| 2026-05-12 | Reclassement en ADR-RICK-001 — typologie corrigée par Amadeus : c'est une décision d'architecture (incarnation Rick), pas un design système | Architect (Claude Code, validation Amadeus) |

---

*ADR-RICK-001 — OpenHarness/OpenHermes : L'Incarnation de Rick — A0 Amadeus — Ratifié 2026-05-11, Reclassé 2026-05-12*
