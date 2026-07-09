# A3 Curie 12 Week Plan — Discipline #2 sister canon LD01

> **Sister chain** : `a3_curie_vivid_vision_sister.md` (D1 Vivid Vision canon) → **`a3_curie_12_week_plan_sister.md` (ce fichier)** — Discipline #2 Planning canon.
> **Date** : 2026-07-05T16:56 ET (post-Vision RATIFIED + A0 GO « ok les 2 Go »).
> **Cycle** : 12WY 2026-Q3 (2026-07-05 → 2026-09-27, **WAR MODE 12 sem**).
> **Statut** : **DRAFT PROPOSED** en attente A0 ratification.

---

## §1 — Discipline #2 = Planning (Moran & Lennington canon)

Vision D1 (ADR-LD01-010 RATIFIED) lockée. Discipline #2 = transformer Vision en plan exécutable.

**Séquence canonique** : Vision → **Planning** → Process Control → Execution → Recovery.

## §2 — 12 Week Plan (Lead Measures par Triptyque)

| Sem | Triptyque | L0 Pocock | L1 gstack | L2 CEO-Bench |
|---|---|---|---|---|
| S1 | T1 People·Op·IT | 1 audit reflex / sem | 1 /autoplan draft / sem | 1 CEO-Bench runbook review / sem |
| S2 | T2 Product·Growth·Sales | 2/2 skills | 1 /plan-ceo-review | 1 CEO-Bench prep UV run |
| S3 | Duo Finance·Legal | 3/3 skills | 1 /ship gated | **1 CEO-Bench run #1 réel** (Curie W5) |
| S4 | Pass-2 T1 + DEAL | 4/4 skills | 2 /autoplan réel / sem | 2 CEO-Bench runs / sem |
| S5 | Pass-2 T2 + DEAL + AI-Act | 5/5 skills | 2 /plan-ceo-review / sem | 2 CEO-Bench runs / sem |
| S6 | Pass-2 Duo + DEAL | 6/6 skills + dry-run hook | 3 /autoplan / sem | 3 CEO-Bench runs / sem |
| S7 | Pass-2 T1 + synthèse J7 | 7/7 skills full | 3 /plan-ceo-review / sem | 3 CEO-Bench runs / sem |
| S8 | Pass-2 T2 + DEAL + Mark rot-rate | 8/8 skills + memory | 4 /autoplan / sem | 4 CEO-Bench runs / sem |
| S9 | Pass-2 Duo + DEAL | 9/9 skills + 3 prospects | 4 /plan-ceo-review / sem | 4 CEO-Bench runs / sem |
| S10 | Pass-2 T1 + Phase 2 dry-run | 10/10 skills total | 5 /autoplan / sem | 5 CEO-Bench runs / sem |
| S11 | Pass-2 T2 + Phase 2 lock-in | 11/11 + sister canon | 5 /plan-ceo-review / sem | 5 CEO-Bench runs / sem |
| S12 | Pass-2 Duo + synthèse J7 + W13 deadman | 12/12 + book canon | 5 /autoplan / sem | 5 CEO-Bench runs / sem |

**Total 12 sem** : 60+ Lead Measures saturés (4-5/sem × 12 sem).

## §3 — Weekly Rocks (5 par semaine)

| # | Rock | Owner | Output |
|---|---|---|---|
| **R1** | 1 audit reflex L0 / sem | A0 Amodei | `tools/skill_creator_reflex.py` |
| **R2** | 1 /autoplan run L1 / sem | A3 Book COO | `signals/.plans/*.plan.yaml` |
| **R3** | 1 CEO-Bench run L2 / sem | A2 Curie | `signals/.plans/*.plan.yaml` + `uv run` |
| **R4** | 1 fiche P&L hebdo / J7 | A3 Book | `LD01/30_decisions/*.weekly_p_and_l.md` |
| **R5** | 1 synthèse J7 / sem | A0 Amodei | `LD01/99_meta/calendar.md` append |

## §4 — Scorecard cadence

| Niveau | Fréquence | Output |
|---|---|---|
| **Daily** | chaque jour ouvré | `cron/output/book-loop-*.json` (1 ligne par Lead Measure) |
| **Weekly** | chaque J7 | 5 Weekly Rocks attained vs planned dans `LD01/30_decisions/*.weekly_*.md` |
| **Monthly** | W4 | Mark rot-rate audit → `LD01/99_meta/rot-rates.md` |
| **Cycle** | W13 (2026-09-27) | Synthèse J7 finale + cycle reorg → `decisions/*_12WY_cycle_reorg.json` |

## §5 — Tactics (Process Control D3, semaine prochaine)

| Tactic | Owner | Trigger |
|---|---|---|
| **Anti-drift** : même op > 3x consécutives | A0 Amodei | loop detect |
| **Quadrantic mode** : disable direct tools except sub-agent tools | A3 Book | W5+ test |
| **E-Myth SYSTEMIZE** : gatekeeper | B1 Jerry | cross-domaine check |
| **Beth veto** : burnout watch | A1 Beth | human veto |

## §6 — Sessions Hero spawned (live maintenant)

| Agent | SessionId | Status |
|---|---|---|
| a3-book-coo | `mvs_13e4c72b96d8412f87f8a7ce08faf823` | spawned ✓ |
| a2-zora-discovery | `mvs_a4b31284f8c44ac0a0f9d6db24bb9f12` | spawned ✓ |
| a1-morty-assistant | `mvs_23cd1b43b06f4bf88512237a90e9d47f` | spawned ✓ |
| a0-amodei-meta-coach | `mvs_a80dbbf6509549b892d85df00f6b21a7` | spawned ✓ |

Sous WAR MODE + A0 GO explicite, 4 sessions spawned (Beth humain exclu, AUCUN schedule). **Maintenant visibles dans la sidebar UI MiniMax Code.**

## §7 — Doctrines préservées (Planning n'écrase rien)

- ADR-WARMODE-001 + 002 : intacts
- ADR-LD01-010 RATIFIED (Vision D1)
- Append-only D4 : Planning append-only
- War Room Bypass Beth Only : Planning respecte
- 27 agents (22 canon + 5 Hero) : Planning assume
- 4 sessions Hero live : Book/Zora/Morty/Amodei

## §8 — Sister chain canon LD01

```
a0_vision_curie_sister.md (Vision A0 + Curie + Loop Engineering)
  ↓
hero_agents_canonic_creation_sister.md (5 Hero agents canon)
  ↓
a3_curie_vivid_vision_sister.md (D1 Vivid Vision RATIFIED)
  ↓
a3_curie_12_week_plan_sister.md (D2 Planning DRAFT)  ← tu es ici
  ↓
(à venir : D3 Process Control sister canon — semaine prochaine)
```

## §9 — Trace canon append-only

- `agent-os/citadel/decisions/2026-07-05_a3_curie_12_week_plan.json` (proposé)
- `LD01/30_decisions/ADR-LD01-011_12_week_plan_a3_curie.md` (DRAFT)
- `LD01/99_meta/a3_curie_12_week_plan_sister.md` (ce fichier, 9 sections)
- 4 sessions mavis spawned (live, visibles sidebar UI)

## §10 — Suite gated

Discipline #3 Process Control + Tactics sera livré S1→S2 (semaine prochaine) après ratification Planning.

Si A0 veut déjà voir les Weekly Rocks configurés en tâches individuelles (via `mavis session new a3-book-coo --prompt "..."` avec prompt R1/R2/R3/R4/R5), je peux spawner 5 sous-sessions.

Réversibilité totale : 3 fichiers à `mavis-trash` → revient à avant.