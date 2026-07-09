---
source: Shadow_L1
date: 2026-05-19
type: doctrine
status: DRAFT_ACTIVE
domain: Shadow_L1 / Heartbeat / Life_OS / Symphony
inherits: ../Shadow_L0/HEARTBEAT_PROTOCOL.md
anchors:
  - Shadow_L0/HEARTBEAT_PROTOCOL.md (canonical pulse doctrine)
  - LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md
  - Symphony SPEC.md (https://github.com/openai/symphony)
tags: [#Heartbeat, #ShadowL1, #LifeOS, #Baserow, #Plane, #ClaudeCode, #MiniMax, #Symphony]
---

# HEARTBEAT_PROTOCOL — Shadow L1 (Life OS Pulse)

> Hérite de `Shadow_L0/HEARTBEAT_PROTOCOL.md`. Cette doctrine ne redéfinit pas
> le tick cycle (WAKE→PROBE→DECIDE→EXECUTE→OBSERVE→LEARN→SIGNAL→SLEEP).
> Elle spécialise les **surfaces observées**, le **routage**, la **cadence**
> et les **règles d'alerte** pour la couche Life OS.
>
> Orchestrateur principal : **Claude Code CLI on MiniMax Token Plan**
> (Anthropic-compatible backbone, autonomy-friendly, request-budget tolérant).

## 1. Mission de Shadow L1

Shadow L1 = pouls **Life OS / back-office personnel** :

- Baserow Life OS (LD00-LD04, ZORA, 12WY Warp Core, Scorecard, Time Use)
- Plane work-items (quand auth débloqué)
- Scorecard 12WY (Rocks, tactiques W1-W4, lead/lag indicators)
- Calendar Tracker / Time Use
- Weekly Review (dimanche)
- Fatigue / load / priorités cognitives
- Synthèse PARA / GTD / DEAL inter-vessels

Shadow L1 **ne pense pas à la place de A0**. Il remonte les **anomalies de vigilance** :
Rocks orphelins, tactiques sans scorecard, Strategic Blocks manquants, dimanche review non préparée, surcharge cognitive.

## 2. Pourquoi Claude Code sur MiniMax orchestre L1

| Critère | Justification |
|---|---|
| Long context (200k+) | Baserow Life OS + 12WY = tables larges, synthèse multi-source |
| Reasoning Anthropic-style | Détection d'anomalies cognitives (surcharge, alignment Ren's Law) |
| MiniMax Token Plan | Request budget rend les ticks 30 min viables sans cost-anxiety |
| Anthropic policy compliance | MiniMax = backbone autonomy-friendly, harness Claude Code intact |
| Skill ecosystem | Accès direct `/airtable-enrich`, `/skill-creator`, hooks ECC |
| Fallback Gemini | Si MiniMax 429 → Gemini CLI (long context Google One AI Pro) |

**Anti-pattern explicite** : ne PAS utiliser Claude SDK direct Anthropic pour L1 (refuse unattended launches). MiniMax backbone obligatoire pour les ticks programmés.

## 3. Cadence Cible

| Tempo | Valeur | Trigger |
|---|---|---|
| Primary | `every 30m work-hours` | Task Scheduler Mon-Sun 07:00-22:00 |
| Secondary | `daily 06:30` | Préparation review hebdo si dimanche |
| Stall timeout | `20 min` | Mission cognitive ne doit pas stall > 20 min |
| Context compact | `> 75%` | Auto-suggest `/compact` (L1 charge longue) |

**Active hours** : 07:00-22:00 local (pas de tick nocturne — Life OS = rythme humain).

## 4. No-Empty-Heartbeat Rule (rappel Symphony)

Un tick L1 n'est autorisé que si AU MOINS une condition est vraie :

1. Fichier mission dans `Shadow_L1/agents/Claude_Code_CLI/memory/inbox/`
2. `tasks:` block du `HEARTBEAT.md` L1 a un check dû
3. Source active surveillée : Baserow Life OS répond `200`, Plane répond `200` (pas 403)
4. Run précédent `in-progress` / `stalled` / `needs_review`
5. Dimanche review prep dû (J-1 calendrier)

Sinon → `HEARTBEAT_OK` silencieux + exit 0.

## 5. Readiness Gates (état au 2026-05-19)

| Gate | État | Bloqueur |
|---|---|---|
| Capsule Claude_Code_CLI L1 existe | ✅ (créé par ce document) | — |
| HEARTBEAT.md L1 avec `tasks:` block | ✅ (voir `HEARTBEAT.md`) | — |
| Baserow Life OS lisible | ✅ partial | Token Baserow read-only OK, write refusé |
| Plane API joignable | ❌ | HTTP 403 (auth non résolu) |
| Scorecard 12WY peuplé | ✅ partial | LD01-LD04 + 12 Rocks + 17 tactiques W1-W4 |
| First supervised run | ⏳ pending | A0 doit valider Turn 1 manuellement |
| Scheduler enabled | ❌ disabled | Attente supervised run |

**Tant que `first supervised run = pending` → Task Scheduler DISABLED.**

## 6. Surfaces Observées (PROBE phase, L1-specific)

À chaque tick, l'orchestrateur lit (read-only sauf mention explicite) :

```yaml
surfaces:
  baserow_life_os:
    base_id: <var BASEROW_LIFE_OS_BASE_ID>
    tables_watched:
      - LD00_Life_Wheel_ZORA
      - LD01_Vision_12WY
      - LD02_Rocks
      - LD03_Tactiques_W1_W4
      - LD04_Scorecard
      - 12WY_Warp_Core
      - Time_Use_Calendar_Tracker
    auth: BASEROW_API_TOKEN (env var, never logged)
    fallback: read-only fetch via curl if MCP unavailable

  plane_workspace:
    api_base: <var PLANE_API_BASE>
    workspace: <var PLANE_WORKSPACE_SLUG>
    project: <var PLANE_PROJECT_ID>
    auth: PLANE_API_TOKEN
    status_2026_05_19: BLOCKED (403)

  obsidian_vault:
    path: 20_Life_OS/
    watched:
      - 21_Ikigai_Orville/**/*.md
      - 23_12WY_SNW/**/*.md
      - 25_GTD_Cerritos/inbox/*.md
    purpose: detect handwritten Rocks/tactics not synced to Baserow

  llm_wiki:
    path: 00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/
    watched:
      - log.md (last 24h entries)
      - syntheses/ (drift detection)
```

## 7. Anomaly Catalog (DECIDE phase, ce qui mérite alerte)

| Anomaly ID | Condition | Severity | Action |
|---|---|---|---|
| `L1-A01` | Rock active sans tactique W1-W4 | H30 | Append to `A0_inbox/anomalies-YYYY-MM-DD.md` |
| `L1-A02` | Tactique W1-W4 sans scorecard row | H30 | Same |
| `L1-A03` | Strategic Block manquant pour Rock H1 | H10 | Same + suggest block in outbox |
| `L1-A04` | Plane vide ALORS QUE Baserow contient tactiques actives | H30 | Same |
| `L1-A05` | Domaine ZORA actif (LD00) sans progression LD04 sur 14j | H90 | Append to weekly review prep |
| `L1-A06` | Surcharge : > 12 tactiques W1-W4 ouvertes simultanément | H30 | Alert A0 (cognitive load) |
| `L1-A07` | Dimanche J-1 sans review prep | H30 | Generate checklist in `outbox/sunday-review-prep.md` |
| `L1-A08` | Obsidian inbox `25_GTD_Cerritos/inbox/` > 30 fichiers | H30 | Suggest GTD processing session |
| `L1-A09` | Time Use Tracker vide depuis 7j | H30 | Alert A0 (visibility loss) |

**Règle critique** : un tick L1 émet au PLUS 1 alerte agrégée par run. Spam = trahison du contrat de vigilance.

## 8. Autonomy Scope (Trust Gating L1)

```yaml
autonomy_scope:
  - baserow-read                      # GET Baserow Life OS tables
  - obsidian-read                     # read vault files
  - llm-wiki-write                    # append concepts/syntheses if pattern detected
  - a0-inbox-write                    # write anomaly digests to A0_inbox/
  - mission-card-draft                # draft mission cards for L2 if cross-layer

requires_signoff:
  - baserow-write                     # PATCH/POST/DELETE Baserow rows
  - plane-write                       # any Plane mutation
  - obsidian-write                    # any vault modification
  - scorecard-mutation                # touching LD04 directly
  - rock-mutation                     # creating/closing Rocks

forbidden:
  - log-secret-value
  - delete-without-trash
  - write-outside-trust-zone
  - bypass-3-turn-air-lock
  - decide-on-behalf-of-a0            # L1 propose, A0 dispose
```

## 9. Fallback Chain (quota-aware, per Shadow_L0 §5)

| Failure | Fallback |
|---|---|
| MiniMax 429 (rate-limit) | → Gemini CLI (preferred 12th Doctor, long context fit L1) |
| MiniMax token plan epuise | → Gemini CLI |
| Claude Code session limit | → A0 must `/compact`, NOT a routing event |
| Both Claude+Gemini down | → Codex CLI dernier recours (mission cap = 5 turns) |
| Baserow API down | → Skip baserow surfaces, log `HEARTBEAT_PARTIAL`, alert if > 2h |
| Plane API down | → Continue (Plane already known 403, not blocking) |

Fallback CLI prepends `[FALLBACK_FROM=Claude_Code_CLI]` to outbox turn-1.md.

## 10. Output Surfaces (LEARN/SIGNAL phase)

| Output | Destination | Format |
|---|---|---|
| Anomaly digest | `A0_inbox/anomalies-YYYY-MM-DD.md` | Markdown table, max 1 per day |
| Sunday review prep | `outbox/sunday-review-prep-YYYY-MM-DD.md` | Checklist H1-H10-H30 |
| Pulse signal | `pulse.log` | `ISO_TS | signal | mission | turn | result | duration_ms` |
| Wiki concept (if pattern) | `LLM_Wiki/wiki/concepts/concept_<slug>.md` | Full frontmatter + Inbounds |
| Skill proposal | `LLM_Wiki/wiki/hand_offs/skills_queue.md` | Append-only |
| Continuation pointer | `Context.md` per mission | Turn N pointer |

## 11. Anti-Patterns L1-Specific

1. **Auto-créer des Rocks** — Rocks = décisions A0 souveraines (Ren's Law). L1 propose, jamais ne crée.
2. **Synthèse non demandée** — pas de "rapport hebdo automatique". L1 prépare une checklist, A0 fait le rapport.
3. **Cross-layer L1→L2 sans mission card** — anomalies business strictly via mission card, pas inline.
4. **Lire les vaults autres que `20_Life_OS/`** — capsule boundary respect.
5. **Modifier Baserow sans dry-run** — toute écriture passe par `airtable-write-with-dry-run` pattern.
6. **Tick nocturne 22:00-07:00** — Life OS suit le rythme humain.

## 12. Activation Procedure (when A0 says "go live")

1. Confirmer `BASEROW_API_TOKEN` set (User scope)
2. Run `heartbeat-tick-l1.ps1 --supervised --once` manually
3. A0 inspecte outbox + pulse.log
4. Si OK → enable Task Scheduler entry `ASpace-Heartbeat-L1-Claude-MiniMax`
5. Surveiller 48h en mode supervised
6. Bascule autonomous après 3 ticks utiles non-vides

## 13. Cross-refs

- `../Shadow_L0/HEARTBEAT_PROTOCOL.md` — doctrine mère
- `./SPEC.md` — spec complète L1
- `./WORKFLOW.md` — mission lifecycle L1
- `./HEARTBEAT.md` — tasks: block exécuté à chaque tick
- `./agents/Claude_Code_CLI/Heartbeat.md` — capsule personnalisation
- `LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md` — abstraction parente

## 14. Inbounds

- `./SPEC.md`
- `./WORKFLOW.md`
- `./HEARTBEAT.md`
- `./agents/Claude_Code_CLI/Heartbeat.md`
- `~/.claude/bin/heartbeat-tick-l1.ps1` (à créer)
