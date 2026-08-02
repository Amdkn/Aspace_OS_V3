# ADR-LD01-011 — A3 Curie 12 Week Plan + Lead Measures Discipline #2 (DRAFT PROPOSED)

> **Statut** : **DRAFT PROPOSED** — en attente de **A0 ratification** sur les 12 Lead Measures + 5 Weekly Rocks.
> **Date draft** : 2026-07-05T16:56 ET (post-ratification Vision D1)
> **Source** : A0 GO « ok les 2 Go » à 16:56 ET
> **Cycle** : 12WY 2026-Q3 (2026-07-05 → 2026-09-27, **WAR MODE 12 sem actif**).
> **Semaine en cours** : S1 / J1 / Triptyque T1 People·Operation·IT.

---

## §1 — Discipline #2 = Planning

Vision (D1) canoniquement lockée par ADR-LD01-010 RATIFIED. Discipline #2 = **transformer Vision en plan** :
- 12 Week Plan détaillé (S1→S12)
- Lead Measures par focus (L0 Pocock / L1 gstack / L2 CEO-Bench)
- Scorecard daily / weekly / monthly
- Tactics pour Process Control (semaine prochaine)
- Weekly Rocks (4-5/sem)

**Pourquoi planning avant execution** : Moran & Lennington canon — l'exécution sans plan = gaspillage. Le plan crée un contrat avec soi-même.

## §2 — 12 Week Plan canon S1→S12

| Sem | Triptyque | Lead Measure L0 | Lead Measure L1 | Lead Measure L2 | MiroFish cadence |
|---|---|---|---|---|---|
| **S1** (2026-07-05) | T1 People·Operation·IT | 1 audit reflex / sem | 1 /autoplan draft / sem | 1 CEO-Bench runbook review / sem | 1 book-loop run toutes les 4h |
| **S2** (2026-07-12) | T2 Product·Growth·Sales | 2/2 skills Pocock-conform | 1 /plan-ceo-review trial | 1 CEO-Bench prep UV run | 1 book-loop run toutes les 4h |
| **S3** (2026-07-19) | Duo Finance·Legal | 3/3 skills Pocock-conform | 1 /ship gated run | **1 CEO-Bench run #1 réel** (Curie W5 verdict) | 1 book-loop run toutes les 4h |
| **S4** (2026-07-26) | Pass-2 T1 + DEAL libéré | 4/4 skills Pocock-conform | 2 /autoplan réel / sem | 2 CEO-Bench runs / sem | 1 book-loop run toutes les 4h |
| **S5** (2026-08-02) | Pass-2 T2 + DEAL libéré | 5/5 skills Pocock-conform | 2 /plan-ceo-review / sem | 2 CEO-Bench runs / sem | AI-Act 2026-08-02 fold-in Legal |
| **S6** (2026-08-09) | Pass-2 Duo + DEAL libéré | 6/6 skills + dry-run hook | 3 /autoplan / sem | 3 CEO-Bench runs / sem | 1 book-loop run toutes les 4h |
| **S7** (2026-08-16) | Pass-2 T1 + synthèse J7 | 7/7 skills full | 3 /plan-ceo-review / sem | 3 CEO-Bench runs / sem | Mid-cycle retrospective |
| **S8** (2026-08-23) | Pass-2 T2 + DEAL libéré | 8/8 skills + memory | 4 /autoplan / sem | 4 CEO-Bench runs / sem | Mark rot-rate audit |
| **S9** (2026-08-30) | Pass-2 Duo + DEAL libéré | 9/9 skills + 3 prospects | 4 /plan-ceo-review / sem | 4 CEO-Bench runs / sem | 1 book-loop run toutes les 4h |
| **S10** (2026-09-06) | Pass-2 T1 + DEAL libéré | 10/10 skills total | 5 /autoplan / sem | 5 CEO-Bench runs / sem | Phase 2 dry-run L5 |
| **S11** (2026-09-13) | Pass-2 T2 + DEAL libéré | 11/11 skills + sister canon | 5 /plan-ceo-review / sem | 5 CEO-Bench runs / sem | Phase 2 lock-in |
| **S12** (2026-09-20) | Pass-2 Duo + synthèse J7 finale | 12/12 skills + book canon | 5 /autoplan / sem | 5 CEO-Bench runs / sem | W13 deadman check |

**Total 12 sem = 60+ Lead Measures = 4 par sem × 12 sem (saturé)**. Scorecard quotidien via `book_loop.py` heartbeat + `/warmode` feed.

## §3 — Lead Measures par focus (détaillé)

### §3.1 — L0 Pocock (Focus #1)

| Lead Measure | Baseline (W1) | Target W12 | Mesure |
|---|---|---|---|
| Skills Pocock-conform (7 champs) | 7/7 canonic | 12/12 new + 7/7 canonic | `tools/skill_creator_reflex.py --audit` weekly |
| Hook PostToolUse L0 FIRE rate | 0/0 | ≥80% sur Edit de SKILL.md | `logs/posttooluse-skill-pocock.log` weekly grep |
| LESSONS.md entries | 0 | ≥4 entries canon | `LD01/10_methodology/00_Pocock_quality_canon.md` append |

### §3.2 — L1 gstack (Focus #1)

| Lead Measure | Baseline (W1) | Target W12 | Mesure |
|---|---|---|---|
| /autoplan runs / sem | 0 | 5 runs / sem | `omk-nexus-coaching-premium/signals/.plans/*.plan.yaml` |
| /plan-ceo-review trials | 0 | 5 trials / sem | sister canon sister_picard_*.md |
| /ship runs gated outboard | 0 | 0 (canal de preuve prêt W12) | logs book_loop_cron.log |
| Sobriété Rick c1-c3 violations | 0 | 0 (audited weekly) | `omk-nexus-coaching-premium/.claude/commands/*.md` diff audit |

### §3.3 — L2 CEO-Bench (Focus #1)

| Lead Measure | Baseline (W1) | Target W12 | Mesure |
|---|---|---|---|
| CEO-Bench runs / sem | 0 | 5 runs / sem | `signals/.plans/*.plan.yaml` outputs |
| UV runs gated | 0 | 1 run réel W3 (Curie W5 verdict) | `logs/L2-ceobench-book-prep.plan.yaml` execution |
| MiroFish boundary measures | 0 | 12 / sem (1/sem × 12) | `cron/output/book-loop-*.json` boundary rows |

## §4 — Weekly Rocks (5 par semaine)

**Pattern** : 4 Weekly Rocks Hebdo = top-of-the-list execution. Chaque Rock = 1 chose concrète shippée dans la sem.

| # | Rock | Owner | Mesure |
|---|---|---|---|
| **R1** | 1 audit reflex L0 / sem | A0 Amodei | `tools/skill_creator_reflex.py` output |
| **R2** | 1 /autoplan run L1 / sem | A3 Book COO | `signals/.plans/*.plan.yaml` |
| **R3** | 1 CEO-Bench run L2 / sem | A2 Curie | `signals/.plans/*.plan.yaml` + `uv run` |
| **R4** | 1 fiche P&L hebdo / J7 | A3 Book | `LD01/30_decisions/*.weekly_p_and_l.md` |
| **R5** | 1 synthèse J7 / sem | A0 Amodei | `LD01/99_meta/calendar.md` append |

## §5 — Scorecard (cadence)

| Niveau | Fréquence | Contenu | Output |
|---|---|---|---|
| **Daily** | chaque jour ouvré | 1 ligne par Lead Measure L0/L1/L2 | `cron/output/book-loop-*.json` |
| **Weekly** | chaque J7 | 5 Weekly Rocks attained vs planned | `LD01/30_decisions/*.weekly_*.md` |
| **Monthly** | chaque J30 (W4) | Rot-rate audit Mark + rot-rates.md | `LD01/99_meta/rot-rates.md` |
| **Cycle** | chaque S12 (W13) | Synthèse J7 finale + cycle reorg | `decisions/*_12WY_cycle_reorg.json` |

## §6 — Tactics pour Process Control (D3, semaine prochaine)

| Tactic | When | Owner | Trigger |
|---|---|---|---|
| **Anti-drift** : si même op > 3x consécutives | automatic | A0 Amodei | loop detect |
| **Quadrantic mode** : disable direct tools except sub-agent tools | W5+ | A3 Book | quadrantic mode test |
| **E-Myth SYSTEMIZE** : Jerry gatekeeper | automatic | B1 Jerry | cross-domaine check |
| **Beth veto** : burnout watch | continuous | A1 Beth | human veto |

## §7 — Doctrines préservées (Planning n'écrase rien)

- ADR-WARMODE-001 + 002 : intacts
- ADR-LD01-010 RATIFIED : Vision canonique
- Append-only D4 : Planning append-only
- War Room Bypass Beth Only : Planning respecte
- 27 agents (22 canon + 5 Hero) : Planning assume l'organigramme
- 4 sessions Hero spawned : Book/Zora/Morty/Amodei

## §8 — Hors-scope

- Pas de mutation canon LD01 intouchable
- Pas de /ship outboard auto
- Pas d'installation Rick kernel lourd
- Pas de rename runtime mavis → Curie
- Pas de reset 12WY_ON_PAUSE.flag avant W13

## §9 — Anti-Ultron

(a) lecture seule sources · (b) append-only · (c) sandbox L2 strict · (d) /ship gated · (e) auto-update off · (f) /browse option · (g) EXIT 0 · (h) Book FINIT cadence · (i) War Room Bypass Beth Only

## §10 — Réversibilité totale

3 fichiers à supprimer :
- `LD01/30_decisions/ADR-LD01-011_12_week_plan_a3_curie.md` (ce fichier)
- `LD01/99_meta/a3_curie_12_week_plan_sister.md`
- `agent-os/citadel/decisions/2026-07-05_a3_curie_12_week_plan.json`

Append-only canon : rien d'autre n'est détruit.

---

**DRAFT PROPOSED. A0 ratification attendue sur §2 (12 Week Plan), §3 (Lead Measures), §4 (Weekly Rocks).**