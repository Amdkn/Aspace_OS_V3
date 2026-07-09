---
name: symphony-pilot
description: Symphonic orchestration of Plane tickets + 12WY rocks + A3 sub-agents on A'Space OS V2. Replaces raw /loop + CronCreate with anti-MAXIMIZER heartbeat (trio /goal + /loop + /routine bounded by 7 SOBER-002 hard-stops). Natif A'Space — NO clone of OpenAI Symphony (Elixir) or Paperclip (TS+pgsql). Phase A = dry-run local only (no cloud wire). Use when user says "pilot Symphony", "heartbeat Plane", "monitor 12WY", "dispatch A3 autonomous", "SOBER-002 dry-run", "anti-paperclip heartbeat".
status: SPEC (Phase A — no code yet)
doctrine: [ADR-META-001-D1, ADR-META-001-D7, ADR-SOBER-002-D2, ADR-SOBER-002-D3, ADR-META-005-Hook3]
phase: A (dry-run local seul, post-A1 Beth GO)
provenance: wiki/hand_offs/handoff_symphony_pilotage_paperclip_anti_maximizer_2026-06-22.md
date: 2026-06-22
---

# Skill SPEC — /symphony-pilot

> **Cycle DEAL appliqué (Dal → Rok-Tahk → Zero → Gwyn)** :
> - **Dal (Define)** : pattern = « A veut Claude Code 24/7 monitor Plane tickets + 12WY rocks + dispatch A3 sub-agents autonomes, supervisé par A0, SANS MAXIMIZER MODE »
> - **Rok-Tahk (Eliminate)** : 8 anti-patterns interdits (cf. §3)
> - **Zero (Automate)** : cette SPEC, < 800 lignes, sans code
> - **Gwyn (Liberate)** : D11 metrics (cf. §7)

---

## 1. Invocation

```
/symphony-pilot <action> [args]
```

**Pré-requis obligatoire** : `A0 GO` verbal explicite (`--a0-go=true`). Sans GO, le skill refuse d'exécuter (D7 anti-MAXIMIZER, SOBER-002 D2).

## 2. Actions disponibles

| Action | Rôle | Sortie attendue |
|---|---|---|
| `start` | Démarre heartbeat dry-run local | Heartbeat pid + log path |
| `pause` | Pause heartbeat (reversible) | `paused_at` timestamp |
| `resume` | Reprend heartbeat depuis pause | Heartbeat pid (same) |
| `status` | Affiche état dry-run + scorecard | JSON: see §6 |
| `escalate` | Force escalate A0 immédiat (SOBER-002 trigger) | Notification Telegram + handoff wiki canon |
| `audit-sober` | Test SOBER-002 7 hard-stops en dry-run | Verdict GO/NO-GO + receipts |

**Default action si omise** : `status`.

## 3. Args

| Arg | Type | Requis | Default | Description |
|---|---|---|---|---|
| `--plane-issue=<id>` | UUID | Non (sauf `start`/`escalate`) | None | Target Plane issue (PROJECT_ID `79df867c-06b5-4e61-b3f1-68aa886c39a3`) |
| `--12wy-rock=<id>` | UUID | Non | None | Target 12WY rock (table `fw_12wy` Supabase `hjweyhpmrxqsxfbibsnc`) |
| `--a3-subagent=<name>` | enum | Non | None | Sub-agent à dispatcher parmi **35 A3 canoniques** (cf. `handoff_a3_data_cartography_v1_2_2026-06-21.md` §3.3) |
| `--a0-go=<bool>` | bool | **OUI** | `false` | A0 GO/NO-GO explicite (D7 anti-MAXIMIZER, SOBER-002 D2) |
| `--heartbeat-interval=<sec>` | int | Non | `600` (10 min) | Intervalle heartbeat entre cycles (D6 #1 floor) |
| `--budget-tokens=<int>` | int | Non | `50000` | Token spend max / heartbeat (SOBER-002 Hard-stop 1) |
| `--max-a3-dispatch=<int>` | int | Non | `3` | Max A3 dispatches / heartbeat (SOBER-002 Hard-stop 3) |
| `--dry-run=<bool>` | bool | Non | `true` | Phase A = `true` obligatoire (Phase B flip après audit-sober GO) |
| `--notify-a0-channel=<enum>` | enum | Non | `telegram` | Canal escalation : `telegram` / `local-tts` / `wiki-handoff` |

## 4. Dépendances MCP

| MCP | Tools utilisés | Source-of-truth |
|---|---|---|
| `mcp__symphony-plane__*` | `list_issues`, `get_issue`, `update_issue`, `create_subtask` | Tickets runtime (Plane canon) |
| `mcp__supabase__*` | `apply_migration`, `execute_sql`, `list_tables` (LifeOS project) | 12WY canon (`fw_12wy`, `fw_life_wheel`) |
| `mcp__obsidian__*` | `read_note`, `append_to_note`, `create_note` | Wiki canon (`ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/`) |
| `mcp__claude-code-guide__*` | (Phase B) | CC skill lifecycle docs |

**Anti-pattern Phase A** : ne PAS utiliser `mcp__baserow__*` (MORT par décision A0), ne PAS utiliser `mcp__affine__*` (SaaS Cloud validé 2026-06-21 mais hors scope dry-run).

## 5. Garde-fous SOBER-002 (7 hard-stops → binding)

Mapping explicite entre les 7 hard-stops d'`ADR-SOBER-002 D3` et le comportement `/symphony-pilot` :

| # | Trigger SOBER-002 | Action `/symphony-pilot` |
|---|---|---|
| **1** | Siphonage données personnelles / biométriques | Skill **n'accède jamais** à colonnes PII hors `user_profiles` (table RLS-protected). Toute tentative → pause + escalate A0. |
| **2** | Manipulation algorithmes visibilité / opinion | Skill **ne touche pas** aux ranking Plane ni aux recommendations A0. Lecture seule par défaut. |
| **3** | Destruction institutions démocratiques | Skill **ne shutdown pas** de wiki pages, ADR, ou tables canoniques. Append-only strict (D4 no-amnesia). |
| **4** | Chantage géopolitique via infra critique | Skill **ne touche pas** aux DNS (Hostinger), VPS, ou config réseau. Scope = Plane/Supabase/Obsidian uniquement. |
| **5** | Valorisation financiarisée découplée prod | Skill **no metric** sur "valeur marchande". Metrics = tickets auto-traités, escalations A0, temps économisé (cf. §7). |
| **6** | Production valeur Musk-style (speed > safety) | Skill **always** : `--dry-run=true` Phase A, audit-sober GO avant Phase B, max 3 A3 dispatch / heartbeat. |
| **7** | Escalade kernel Rick (config touch) | Skill **jamais** d'édition `.claude/settings.json`, `.mcp.json`, hooks, ou config OS. Config = L0 Rick only. |

**Bonus META-001** :
- **D7 cost-of-escalation** : escalate A0 = ~100× cost. Skill **ne escalade JAMAIS** sauf 1 des 7 hard-stops OU 3× même output (boucle infinie détectée).
- **D1 verify before assert** : chaque dispatch A3 = receipt D1 obligatoire (file count, byte count, grep result).

## 6. Format `status` (sortie JSON)

```json
{
  "skill": "symphony-pilot",
  "phase": "A",
  "dry_run": true,
  "heartbeat": {
    "active": true,
    "pid": 12345,
    "started_at": "2026-06-22T10:00:00Z",
    "interval_sec": 600,
    "cycles_completed": 42,
    "last_cycle_at": "2026-06-22T16:50:00Z"
  },
  "budget": {
    "tokens_used_cycle": 12340,
    "tokens_budget_cycle": 50000,
    "a3_dispatched_cycle": 1,
    "a3_dispatched_max": 3,
    "hard_stops_triggered_total": 0
  },
  "queue": {
    "plane_issues_pending": 3,
    "12wy_rocks_pending": 5,
    "a3_dispatches_inflight": 0
  },
  "scorecard_12wy_w": {
    "W2_score": null,
    "W3_score": null,
    "a0_escalations_count": 0
  },
  "sober_audit": {
    "last_run_at": "2026-06-22T08:00:00Z",
    "verdict": "GO",
    "hard_stops_violated": 0
  }
}
```

## 7. Exemples d'invocation

### 7.1 Démarrer heartbeat dry-run

```
/symphony-pilot start \
  --plane-issue=abc-123-def \
  --12wy-rock=rock-W2-ikigai \
  --a3-subagent=protostar-zero \
  --a0-go=true \
  --heartbeat-interval=600 \
  --budget-tokens=50000 \
  --max-a3-dispatch=3 \
  --dry-run=true
```

**Effet** : heartbeat tourne localement, surveille Plane issue `abc-123-def` + 12WY rock `rock-W2-ikigai`, dispatche A3 Zero (Protostar) si nécessaire, **sans toucher au cloud**.

### 7.2 Status courant

```
/symphony-pilot status
```

→ Retourne le JSON §6.

### 7.3 Audit SOBER-002 (Phase A obligatoire avant Phase B)

```
/symphony-pilot audit-sober --a0-go=true
```

→ Teste les 7 hard-stops en dry-run, retourne verdict GO/NO-GO + receipts.

### 7.4 Escalation A0 (urgence)

```
/symphony-pilot escalate \
  --plane-issue=abc-456-ghi \
  --a0-go=true \
  --notify-a0-channel=telegram
```

→ Force escalate A0 immédiat via Telegram + handoff canon wiki.

## 8. Anti-patterns (Rok-Tahk — Eliminate)

Liste explicite des **choses à NE PAS faire** :

1. ❌ **Cloner OpenAI Symphony Elixir** — stack mismatch (A'Space = JS/TS/Supabase/Plane, pas Elixir/Phoenix).
2. ❌ **Cloner Paperclip TypeScript** — stack mismatch (A'Space = Vite/Next.js + Supabase Cloud, pas pnpm + Postgres embarqué + Vitest).
3. ❌ **Wire MCP cloud en dry-run** — Phase A = local seul. Wire cloud = Phase B post `audit-sober` GO.
4. ❌ **`CronCreate` durable SANS dry-run validé** — tout schedule persistant doit passer audit-sober GO d'abord.
5. ❌ **Production 24/7 SANS A1 Rick Sobriété activé** — Phase B requiert A1 Rick mode alerte (Q4 2026 target).
6. ❌ **MAXIMIZER MODE** — case Paperclip roadmap non livrée, A0 explicitement interdite. Aucune optimisation mono-objectif.
7. ❌ **Cloner agents externes** — utiliser les 35 A3 twins canoniques (cf. `handoff_a3_data_cartography_v1_2_2026-06-21.md`). Pas d'agent ad-hoc.
8. ❌ **Nouveau DB** — utiliser Supabase LifeOS canonique (`hjweyhpmrxqsxfbibsnc.supabase.co`). Pas de SQLite/Postgres local.
9. ❌ **Nouvelle UI** — utiliser Plane (Kamban) + Obsidian (Wiki) + Notion canoniques. Pas de dashboard custom.
10. ❌ **Hard-delete** — append-only strict (D4 no-amnesia). Retraite = `_TRASH_<date>/`.

## 9. Phase lifecycle (A → B → C)

| Phase | Scope | GO requis |
|---|---|---|
| **A (maintenant)** | Dry-run local seul, SPEC only, audit-sober test | A0 GO + A1 Beth VETO |
| **B (Q3 2026)** | Wire MCP cloud (Plane + Supabase + Obsidian), heartbeat réel, scorecard live | A0 GO + A1 Beth VETO + A1 Rick alerte |
| **C (Q4 2026)** | Production 24/7, A1 Rick Sobriété activé kernel | A0 GO + A1 Rick kernel veto |

**Transition A → B** nécessite :
- 7/7 SOBER-002 hard-stops testés `audit-sober` GO
- ≥ 1 cycle 12WY (12 semaines) de données dry-run
- 0 escalade A0 non-résolue
- A1 Rick Sobriété mode alerte (mais pas veto)

**Transition B → C** nécessite :
- Cycle 12WY complet GO
- A1 Rick kernel activé (1×/an max)
- D11 metrics dans targets (cf. §10)

## 10. D11 Liberation metrics (Gwyn)

Mesures attendues après Phase B (12 semaines) :

| Metric | Cible | Source |
|---|---|---|
| `# tickets auto-traités / jour` | ≥ 10 | Plane API `list_issues` count where `state = done` AND `assignee = "symphony-pilot"` |
| `# escalations A0 / semaine` | **0** | Telegram notifications count |
| `Temps A0 économisé / semaine` | ≥ 5h | Self-report A0 + chrono dry-run logs |
| `Scorecard 12WY W2-W3 update` | ≥ 7/10 | Table `fw_12wy` `score` column |
| `Hard-stops SOBER-002 triggered total` | **0** | Heartbeat logs |
| `A3 dispatch success rate` | ≥ 95% | A3 reply parse OK count / total dispatched |

**Avant/après ratio** : si `tickets_auto_traités ≥ 10/jour` ET `escalations_A0 = 0`, le système libère A0 (D11 pass). Sinon, retour Phase A + ajustement garde-fous.

## 11. Open follow-ups Phase A

1. ⏳ A1 Beth audit MCP drift (Baserow/Affine/Plane/Obsidian) — verdict NO-GO/GO
2. ⏳ A2 Una plan 7 jours (W2-W3 cycle 12WY) dry-run
3. ⏳ A3 Chapel D11 scorecard template + `/routine` design
4. ⏳ Test `--dry-run=true` + `audit-sober` end-to-end sur 1 cycle
5. ⏳ Handoff canon `wiki/hand_offs/symphony_pilot_phase_a_dryrun_2026-06-XX.md`

## 12. Liens canon (D1 verify)

- Brief : `wiki/hand_offs/handoff_symphony_pilotage_paperclip_anti_maximizer_2026-06-22.md`
- ADR-SOBER-002 : `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md`
- ADR-META-001 : `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`
- ADR-META-005 : `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md`
- A3 cartography v1.2 : `wiki/hand_offs/handoff_a3_data_cartography_v1_2_2026-06-21.md`
- Plane projet : PROJECT_ID `79df867c-06b5-4e61-b3f1-68aa886c39a3`
- Life-OS-2026 Supabase : `hjweyhpmrxqsxfbibsnc.supabase.co`
- OpenAI Symphony SPEC : https://github.com/openai/symphony/blob/main/SPEC.md (référence, pas clone)
- Paperclip docs : https://docs.paperclip.ing/ (référence, pas clone)
