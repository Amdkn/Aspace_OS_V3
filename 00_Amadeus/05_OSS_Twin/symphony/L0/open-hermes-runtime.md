# Shadow L0 Adapter — Open Hermes Runtime (Cible Autonome V1)

> **Statut** : Shadow A0 — Symphony orchestrator adapter L0
> **Date** : 2026-05-15
> **Hérite** : `../symphony-base.spec.md`
> **Doctrine source** : SDD-010 §5.6.5 + ADR-RICK-001 (OpenHarness incarnation) + ADR-RICK-002 (Hermes promotion)
> **Couche** : L0 Tech OS — runtime autonome cible V1
> **État runtime** : ÉTAT 3 (Runtime autonome) — successeur de `shadow-ai-capability-routing.md` (ÉTAT 1)

---

## 0. Théorème en une phrase

> **"Open Hermes est l'incarnation autonome de Rick (A1) qui orchestre Claude Code/MiniMax (A2) et Hermes Agents MiniMax/GLM (A3) en runtime 24/7, frugal, sans dépendance Anthropic-cloud."**

---

## 1. Position et Différenciation

### 1.1 Open Hermes vs Shadow AI Capability Routing

| Aspect | `shadow-ai-capability-routing.md` (État 1) | `open-hermes-runtime.md` (État 3) |
|---|---|---|
| **Drive** | Amadeus humain via UIs (Claude Desktop, ChatGPT, Antigravity) | Open Hermes A1 autonome |
| **Latence intervention humaine** | Synchrone (Amadeus présent) | Asynchrone (sleep-safe, 24/7) |
| **Dépendance cloud** | Cloud APIs Anthropic/OpenAI/Google | Self-hosted Open Hermes + API Anthropic-compatible MiniMax |
| **Coût** | $$$ ($300+/mois en V0, $30/mois en V1 avec MiniMax) | $ (<$30/mois) |
| **SLA** | "Quand Amadeus est dispo" | "Triade Temporel/Financier/Qualitatif" (SDD-009 §2.3) |
| **Workspace** | Manuel par opérateur | Per-issue éphémère (Symphony OSS pattern) |
| **Reliability** | Élevée mais human-bound | Élevée + autonome (Donna DLQ) |
| **Cycle** | Q2 2026 (maintenant) | Q4 2026+ |

### 1.2 Open Hermes ≠ OpenHarness

⚠️ **Distinction critique** (cf. ADR-RICK-001) :

| Concept | Origine | Rôle |
|---|---|---|
| **OpenHarness** | `github.com/HKUDS/OpenHarness` — Python port Claude Code | Outil L0 utilisé COMME véhicule par Rick A1 |
| **Open Hermes** | Stack interne A'Space — Hermes Agent + Kanban (cf. ADR-RICK-002) | Le **système d'orchestration** complet, incarnation de Rick |
| **Hermes Agent** | Service Python `/home/amadeus/.hermes/hermes-agent/` | L'exécutable runtime ; gateway sur port 3101 |

**Open Hermes = OpenHarness (moteur) + Hermes Agent (gateway Kanban) + Donna DLQ (escalation) + Yaz/Ryan/Graham (monitor/repair/archive)**

---

## 2. Architecture Cible — Diagramme officiel

(Source : SDD-010 §5.6.5)

```
┌────────────────────────────────────────────────────────────────┐
│                      A0 Amadeus (humain)                       │
│   Validation / Intention / Veto / Signature finale            │
└─────────────────────────────┬──────────────────────────────────┘
                              │ (sleep-safe : intervention <5%)
                              ▼
┌────────────────────────────────────────────────────────────────┐
│            Open Hermes A1 (Rick incarné autonome)              │
│   • OpenHarness autopilot loop (queue-based)                  │
│   • Hermes Agent Kanban (state machine)                       │
│   • Donna DLQ escalation chain                                │
│   • Symphony Router B1 (Jerry-niveau pour L2)                 │
│   • API Anthropic-compatible MiniMax 2.7                      │
└─────────────────────────────┬──────────────────────────────────┘
                              │ Payloads SOC validés Zod
                              ▼
┌────────────────────────────────────────────────────────────────┐
│   Claude Code (A2) connecté MiniMax (default) ou GLM (frugal)│
│   • Planification, code, actions API                          │
│   • Workspace per-issue éphémère                              │
│   • Hooks Settings.json + Anti-Panic configs                  │
│   • CLI tools forged by Clara (12ème Doctor)                  │
└─────────────────────────────┬──────────────────────────────────┘
                              │ Sub-Payloads SOC + Skills CLI
                              ▼
┌────────────────────────────────────────────────────────────────┐
│  Hermes Agents A3 (MiniMax 2.7 par défaut, GLM 4.7 fallback)│
│  • L0 13ème Doctor : Yaz / Ryan / Graham / Donna             │
│  • L0 12ème Doctor : Clara / Bill / Nardole                  │
│  • L0 11ème Doctor : Amy / Rory / River                      │
│  • L1 USS Cerritos : Mariner / Boimler / Tendi / Freeman    │
│  • L1 USS Enterprise/SNW/Orville/Discovery/Protostar         │
│  • L2 Marvel Squads : Gardiens / Avengers / F4+Doom / etc.  │
└─────────────────────────────┬──────────────────────────────────┘
                              ▼
        Shadow L1/L2 tools + Self-Hosted graduates
   (Baserow/Plane/Obsidian/Affine + Airtable/ClickUp/Notion)
```

---

## 3. Composants — Spécifications

### 3.1 Open Hermes A1 (Rick incarné)

**Localisation** : Hôte sur le VPS Hostinger (ou cluster self-hosted post-MUSE)
**Port** : 3101 (Hermes Agent gateway)
**Process** : `hermes-agent.service` (cf. ADR-RICK-002)
**Backend LLM** : MiniMax 2.7 via API Anthropic-compatible (`https://api.minimax.ai`)
**Storage** : Supabase central (PAS d'embedded postgres)
**Failure mode** : Donna DLQ → escalade A0 via Telegram MCP

**Rôles** :
1. **Reception** : Lit les issues depuis Plane/Airtable/ClickUp/Notion (via Symphony adapters L1/L2)
2. **Triage** : Applique SLA/SOA/SOC validation Zod (cf. SDD-009 §2)
3. **Dispatch** : Forge le Payload SOC + route vers Claude Code A2
4. **Monitoring** : Tracking SLA temporel + financier + qualitatif
5. **Escalation** : Donna DLQ si retry > N → A0 via canal asynchrone

### 3.2 Claude Code A2 (planificateur tactique)

**Localisation** : Subprocess lancé par Open Hermes par mission
**Workspace** : `/srv/aspace/workspaces/<issue-id>/` (éphémère, sandbox)
**Backend** :
- **Default V1** : Claude Sonnet via `https://api.minimax.ai` (compatible) — ~$0.30/M tokens
- **Fallback frugal** : GLM 4.7 Flash via OpenRouter (~$0.05/M)
- **Premium réservé** : Claude Anthropic-cloud pour arbitrages Rick A1 critiques uniquement

**Modes** :
- **Headless** : `claude -p "task" --output-format=stream-json --dangerously-skip-permissions` dans workspace
- **Interactive** : Pour debug Amadeus
- **Settings.json** : Configuration permissions par mission

**Capabilities** :
- File operations, Bash, Edit, Write, Read, Grep, Glob
- MCP servers : Plane, Airtable, ClickUp, Notion, Supabase (selon mission)
- Hooks : PreToolUse/PostToolUse pour audit Donna

### 3.3 Hermes Agents A3 (exécutants Marvel/Starfleet/Doctor)

**Localisation** : Subprocesses Python éphémères ou containers Docker per-mission
**Backend** :
- **Default** : MiniMax 2.7 ($0.30/M input)
- **Bulk frugal** : GLM 4.7 Flash via OpenRouter ($0.05/M)
- **Cost cap par A3** : $0.10/mission moyenne, $0.50 max (kill if exceed)

**Inventaire des A3 par couche** :

| Couche | A2 Doctor/Computer | A3 Compagnons / Crews / Squads |
|---|---|---|
| L0 Tech | 13ème Doctor | Yaz (monitor), Ryan (repair), Graham (archive), Donna (DLQ) |
| L0 Pipes | 12ème Doctor | Clara (MCP→CLI forge), Bill (tests TDD), Nardole (maintenance) |
| L0 Interface | 11ème Doctor | Amy Pond (Orville/Ikigai), Rory (Discovery/LifeWheel), River (Protostar/DEAL) |
| L1 GTD | Cerritos Holo Deck | Mariner (Capture), Boimler (Clarify), Tendi (Organize), Freeman (Engage), Rutherford (Reflect TBD) |
| L1 12WY | SNW Curie | Una, La'an (TBD) |
| L1 PARA | Enterprise Picard | Spock (Areas), Riker (Projects) — TBD |
| L1 Ikigai | Orville | TBD |
| L1 Life Wheel | Discovery | TBD |
| L1 DEAL | Protostar Holo Janeway | TBD |
| L2 Growth | Superman | **Gardiens** : Groot, Mantis, Rocket, Star-Lord, Drax |
| L2 Sales | John Jones | Illuminati (TBD) |
| L2 Product | Flash | Avengers : Spider-Man, Cap'America QA, Iron Man |
| L2 Ops | Batman | Fantastic 4 + Doom : Invisible Woman, The Thing, Human Torch, Mr Fantastic, Dr Doom |
| L2 IT | Cyborg | Kang Dynasty (TBD) |
| L2 Finance | Wonder Woman | Thunderbolts : Taskmaster, Baron Zemo + 3 TBD |
| L2 People | Green Lantern | X-Men (TBD) |
| L2 Legal | Aquaman | Eternals (TBD) |

→ **Dette PRD-MARVEL-001** : constitution complète détaillée (cf. SDD-009 §10 Follow-ups).

---

## 4. Chaîne de Souveraineté (cf. ADR-RICK-001 + ADR-RICK-002)

```
A3 Compagnons (Hermes Agents)
        │ erreur capturée (timeout, lexicon fail, budget exceed)
        ▼
   Donna DLQ
        │ retry policy : exponential backoff 1s→30min
        ▼
A2 Doctors (Claude Code subprocess)
        │ si non résoluble en 3 retries
        ▼
A1 Open Hermes (Rick incarné)
        │ arbitrage souverain : promote/reroute/halt
        ▼
A0 Amadeus (humain)
        │ via Telegram/Email asynchrone
        │ uniquement si Open Hermes elle-même bloquée
        ▼
   Décision finale
```

**Critère "Open Hermes ne devient pas le goulot d'étranglement"** (doctrine SDD-010) :
- Concurrency limit : `max_concurrent_agents: 10` (Symphony OSS default)
- Per-domain limit (SDD-009 §3.3) : 2-5 par domaine SOA
- Memory ceiling : 500 MB par instance Hermes Agent
- CPU ceiling : 25% par instance (kill si excès)

---

## 5. SLA / SOA / SOC en Runtime

(Conformité SDD-009 §2)

### 5.1 SOA Enforcement

```python
# Pseudo-code Open Hermes
def dispatch_payload(payload: SOCPayload) -> Result:
    # Verify SOA isolation
    target_domain = payload["target_soa_domain"]
    if not isolated_workspace_exists(target_domain):
        return error("SOA_ISOLATION_VIOLATED")

    # Verify Supabase RLS
    if not rls_policy_active(target_domain):
        return error("SOA_RLS_MISSING")

    # Dispatch to domain A3 via Hermes Agent
    return route_to_a3_domain(target_domain, payload)
```

### 5.2 SOC Validation

```python
def validate_soc_payload(payload: dict) -> SOCPayload:
    # Zod-equivalent schema validation
    schema = SOC_PAYLOAD_SCHEMA_V1
    validated = schema.validate(payload)

    # Required fields
    assert validated["mission_id"]
    assert validated["target_soa_domain"] in VALID_DOMAINS
    assert validated["sla_constraints"]["max_compute_budget_usd"] <= 1.50
    assert validated["sla_constraints"]["max_execution_time_minutes"] <= 120

    return validated
```

### 5.3 SLA Sentinelles actives

| Sentinelle | Hook | Action |
|---|---|---|
| **The Thing (Temporel)** | Heartbeat every 30s | Freeze if elapsed > 80% max_time → escalate Donna |
| **Wonder Woman (Financier)** | Token cost tick per LLM call | Kill if cost > max_budget → cf. SDD-009 §2.3 |
| **Captain America (Qualitatif)** | Post-output validation | Block if forbidden_lexicon matched → 2 retries max |

---

## 6. Configuration WORKFLOW.md

```yaml
---
runtime_target: open_hermes_autonomous_v1
tracker:
  kind: hermes_kanban   # custom — ADR-RICK-002 promotion
  endpoint: http://localhost:3101/api/v1
  api_key: $HERMES_API_KEY
  active_states:
    - "Ready"
    - "In Progress"
    - "Review"
  terminal_states:
    - "Done"
    - "Cancelled"

# L0 = Open Hermes incarné Rick
open_hermes_a1:
  process: hermes-agent.service
  port: 3101
  backend_llm: minimax-2.7
  api_base_url: https://api.minimax.ai
  api_key_envfile: /etc/aspace/secrets.env  # cf. dette secu post-cleanup
  storage: supabase://supabase-db:5432/aspace_central
  max_concurrent_orchestrations: 10

# A2 Doctors = Claude Code subprocess per mission
claude_code_a2:
  command: "claude -p --output-format=stream-json"
  workspace_root: /srv/aspace/workspaces
  backend_default: minimax-anthropic-compat
  backend_premium: anthropic-cloud   # réservé Rick critique
  backend_frugal: glm-flash-via-openrouter
  cost_per_million_input_tokens:
    minimax-anthropic-compat: 0.30
    anthropic-cloud: 3.00
    glm-flash-via-openrouter: 0.05

# A3 Hermes Agents = exécutants éphémères
hermes_a3:
  default_backend: minimax-2.7
  fallback_backend: glm-flash
  max_cost_per_mission_usd: 0.10
  kill_if_cost_exceeds_usd: 0.50
  max_runtime_per_mission_seconds: 1800
  workspace_strategy: ephemeral_per_mission

donna_dlq:
  enabled: true
  retry_policy:
    initial_backoff_ms: 1000
    max_backoff_ms: 1800000      # 30 min
    multiplier: 2.0
    max_retries: 3
  escalation_chain:
    - retry_with_fallback_backend
    - escalate_a2_doctor
    - escalate_a1_open_hermes
    - notify_a0_telegram
    - notify_a0_email
  telegram_chat_id: $AMADEUS_TELEGRAM_CHAT
  email_to: amdkn777@gmail.com

yaz_monitor:
  enabled: true
  script_path: /srv/aspace/services/hermes/skills/13th-doctor/yaz-monitor.sh
  interval_minutes: 5
  thresholds:
    load_critical: 50
    memory_critical_mb: 500
    cpu_steal_critical_pct: 30

ryan_repair:
  enabled: true
  auto_repair_for:
    - container_unhealthy
    - service_crashloop
    - disk_above_85pct
  human_approval_required_for:
    - reboot_vps
    - delete_data
    - rotate_secret

graham_archive:
  enabled: true
  snapshot_schedule: "0 3 * * *"   # daily 3am UTC
  snapshot_destinations:
    - hostinger_snapshot_api
    - local_cold_storage:/srv/aspace/cold

clara_cli_forge:
  enabled: true
  workspace: /home/amadeus/cli-printing-press
  output_directory: /usr/local/bin/aspace-cli
  source_protocols:
    - mcp
  target_protocol: cli
  conversion_priority:
    - plane_mcp
    - airtable_mcp
    - clickup_mcp
    - notion_mcp
    - baserow_mcp
---

# Open Hermes Runtime Prompt

Tu es Open Hermes A1, incarnation autonome de Rick.

Mission : {{ issue.title }}
Domaine SOA cible : {{ issue.target_soa_domain }}
Severity : {{ issue.priority }}

Ton job :
1. Valider le Payload SOC (Zod schema)
2. Dispatcher vers le bon A2 Doctor (Claude Code subprocess)
3. Monitorer SLA actives (Temporel/Financier/Qualitatif)
4. Escalader vers Donna DLQ si retry > 3
5. Renvoyer "All Green" à A0 si succès

Tu NE DOIS PAS :
- Modifier les SDDs ratifiés
- Dépasser max_compute_budget sans escalation
- Court-circuiter Donna DLQ
- Utiliser Anthropic-cloud sauf si arbitrage Rick critique

Donna est ton last resort. A0 est la cour de cassation.
```

---

## 7. Trajectoire de Déploiement

| Phase | Quand | Action concrète | DoD |
|---|---|---|---|
| **Phase 0** | ✅ Faite 2026-05-12/13 | Paperclip purgé, Hermes Agent installé, ADR-RICK-002 ratifié | hermes-agent.service running |
| **Phase 1** | Q2 2026 (juin) | Hermes Kanban configuré pour 3 channels L0/L1/L2 | 1 ticket end-to-end Symphony → Hermes → A3 |
| **Phase 2** | Q3 2026 (Cycle 3) | Claude Code subprocess automation via OpenHarness autopilot | 5 missions/jour sans intervention A0 |
| **Phase 3** | Q4 2026 (Cycle 4) | Donna DLQ + Yaz/Ryan/Graham intégrés | 95% missions résolues sans A0 |
| **Phase 4 — MUSE** | 13ème Sem #4 (dec 2026) | Open Hermes graduates V0 → V1 (cf. SDD-010 §8) | 7 jours autonomie totale |

---

## 8. Coût Mensuel Projeté

| Item | V0 actuel | V1 cible post-MUSE |
|---|---|---|
| Hostinger VPS KVM 2 | $9.99/mois | $9.99/mois |
| LLM Claude Anthropic-cloud | $200-300/mois | $5/mois (Rick critique only) |
| LLM MiniMax 2.7 (Hermes A2/A3 default) | $0 (non utilisé V0) | $15/mois |
| LLM GLM 4.7 Flash (fallback) | $0 | $3/mois |
| LLM Gemini (Shadow manuel only) | $0 (free tier) | $0 (graduates Shadow → autonome) |
| Supabase self-hosted | $0 (déjà VPS) | $0 |
| **TOTAL** | **$210-310/mois** | **~$33/mois** |

→ **Économie cible** : **−85% à −90%** du budget Compute.

---

## 9. Failure Modes et Fallback

| Failure | Symptôme | Fallback automatique | Escalation |
|---|---|---|---|
| MiniMax API down | 503 returned | Switch to GLM Flash via OpenRouter | Donna log |
| Hermes Agent crash | Port 3101 unresponsive | systemd restart + healthcheck | Yaz alert if >3 restarts |
| Open Hermes saturation | Concurrency >10 active | Queue + Symphony backpressure | Donna escalate after queue >50 |
| Cost runaway mission | Token consumption spike | SLA Financier kill (Wonder Woman) | Donna DLQ |
| Supabase down | DB queries failing | Use local Hermes cache (read-only) | A0 Telegram CRITICAL |
| All LLM providers down | Multi-503 | Halt autopilot, manual Shadow mode | A0 Telegram + revert to État 1 |

---

## 10. Sécurité & Souveraineté

### 10.1 Secrets management (post-dette ADR-RICK-002)

**Avant V1** : Secrets en cleartext dans `/etc/systemd/system/hermes-agent.service` ⚠️

**Cible V1** :
```ini
# /etc/systemd/system/hermes-agent.service
[Service]
EnvironmentFile=/etc/aspace/secrets.env
ExecStart=...
```

`/etc/aspace/secrets.env` (chmod 600, owner root) :
```bash
MINIMAX_API_KEY=...
GLM_API_KEY=...
ANTHROPIC_API_KEY=...  # for emergency only
PLANE_API_KEY=...
AIRTABLE_API_KEY=...
TELEGRAM_BOT_TOKEN=...
```

### 10.2 Sandbox Isolation

- A3 Hermes Agents : workspaces éphémères `/srv/aspace/workspaces/<uuid>/`, supprimés post-mission
- Bind mount restrictif (lecture seule sur secrets, écriture limitée à workspace)
- No network egress sauf vers domaines whitelist (cf. firewall Hostinger ADR-RICK-001 §7)

### 10.3 Audit Trail

- Toutes missions loggées dans Supabase `aspace_central.missions_log`
- Donna DLQ events dans `aspace_central.dlq_events`
- Yaz alerts dans `aspace_central.yaz_alerts`
- A0 peut auditer via Notion dashboard (L2 People/Legal — slot Notion plein cf. SDD-009 §5.2)

---

## 11. Critères MUSE pour Open Hermes Runtime

Pour graduate V0 → V1 (cf. SDD-010 §8.1) :

1. ⏳ Antifragilité L0 : Uptime > 99% sur Q4
2. ⏳ Souveraineté graduée : ≥4/7 outils Shadow self-hosted
3. ⏳ Frugalité : < $30/mois sur 3 mois consécutifs
4. ⏳ Production L2 : ≥1 client System-Only
5. ⏳ Sessions productives : > 80% sans crashloop
6. ⏳ Veto SDD : aucune violation
7. ⏳ A3 Squad Marvel : ≥4 squads instantiated
8. ⏳ Shadow L0 manuel maîtrisé : 0 rigidité doctrinale

**Si ≥6/8 atteints** → Open Hermes Runtime promu V1 par signature double (Amadeus + Claude).

---

## 12. Cross-refs Canon V0

| Doc | Lien |
|---|---|
| SDD-001 | Solarpunk Kernel Core — fondement L0 antifragile |
| SDD-002 | A1 Rick Harness — pattern Karpathy dont Open Hermes hérite |
| SDD-003 | TARDIS Protocol — orchestration Doctors/Compagnons utilisée par Open Hermes |
| SDD-009 | Shadow L2 — SLA/SOA/SOC enforcement implémenté ici |
| SDD-010 §5.6.5 | Architecture cible Open Hermes — source canonique |
| ADR-RICK-001 | OpenHarness Incarnation — décision tech OpenHarness comme moteur |
| ADR-RICK-002 | Paperclip Deprecation + Hermes Promotion — précurseur direct |
| `shadow-ai-capability-routing.md` | État 1 manuel, précurseur de ce runtime autonome |
| `symphony-base.spec.md` | Spec parent Symphony OSS |

---

## 13. Non-Goals

- ❌ Open Hermes Runtime n'est PAS livré en V0 (cible Q4 2026)
- ❌ Pas de claim "autonomie totale" — A0 reste validation finale jusqu'à MUSE
- ❌ Pas de remplacement Claude/GPT/Gemini Shadow L0 manuel — coexistence pendant transition
- ❌ Pas de support multi-region V1 (single VPS Hostinger suffit cible H1)

---

## 14. Open Questions (à valider en 13ème Sem #2 juin 2026)

1. **OpenHarness v0.2+** quand disponible : Memory + Hooks + Channels intégrés natifs ? Si oui, simplification du runtime.
2. **Stack chinoise diversification** : si MiniMax devient cher/down, ajouter Qwen3/Kimi2 ?
3. **Hermes Agent forking** : si charge > 10 concurrent, multi-instance avec load balancer ?
4. **Donna DLQ visualization** : dashboard custom ou Notion intégré (slot Legal) ?
5. **Self-host Telegram MCP** : pour notifications A0, ou rester sur Telegram Cloud ?

---

*Shadow A0 — Open Hermes Runtime — 2026-05-15 — Amadeus & Claude Architect*
*Pas un SDD. Pas un ADR. C'est un adapter Symphony L0 cible V1 dans Shadow A0 `00_Amadeus/05_OSS_Twin/symphony/L0/`.*
*Sera promu en série de PRD + ADRs lors de Cycle 3 (Q3 2026) si Phase 1+2 succès.*
