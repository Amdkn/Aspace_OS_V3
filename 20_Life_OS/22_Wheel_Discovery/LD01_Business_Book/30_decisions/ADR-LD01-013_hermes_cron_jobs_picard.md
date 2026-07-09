---
type: adr-decision-doctrine
id: ADR-LD01-013
title: "Hermes Cron Jobs Picard - L+ canon-aligned recurring verification (3 crons)"
status: ACCEPTED + RATIFIED 2026-07-05 (HITL captain 'Cree des Cron Job dans Heremes')
date: 2026-07-05T10:45:00-04:00
deciders:
  - A0 Amadeus (HITL 2026-07-05 'Cree des Cron Job dans Heremes')
  - HA (Hermes Agent = A3 Picard in PARA, auteur cascade FINISHING War Mode)
parent_dox: ../CLAUDE.md
sister: ../AGENTS.md
refines:
  - ADR-LD01-008_coaching-loop-picard-jerry-summers (loop engineering coaching - H1 Book aggregator = cron natural)
  - ADR-LD01-012_l+_skill_standard_cascade_ratification (L+ Skill Standard ratification, source des invariants a verifier)
  - plan-lightning-l+-skill-standard-transversal (L+ canon source)
related:
  - "Skill ship-dont-ask-pattern (skills/software-development/ship-dont-ask-pattern/SKILL.md)"
  - "Hermes UI Cron Jobs panel : empty state 'No scheduled jobs yet' avant ce patch"
domain: LD01_Career_Business / Hermes_Cron / L+_Skill_Standard / Loop_Engineering
tags: ["#ADR", "#cron_jobs", "#hermes", "#L+_verification", "#book_aggregator", "#piccard_h10", "#recurring", "#war_mode", "#ship_dont_ask"]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-WARMODE-001, ADR-LD01-008, ADR-LD01-010, ADR-LD01-012]
sign_off_a0: "A0 Amadeus - HITL 2026-07-05 'Cree des Cron Job dans Heremes'"
war_mode: true
reversible_by: "cronjob action=remove job_id (3 crons) + git revert calendar.md + delete citadel trace + delete ADR-013 = revert complet"
---

# ADR-LD01-013 - Hermes Cron Jobs Picard

> **HITL captain declencheur** : "Cree des Cron Job dans Heremes" (2026-07-05, empty state "No scheduled jobs yet" + button "+ Create first cron"). HA execute en War Mode, ship-dont-ask pattern incarne, 0 HITL frontier-par-frontier.

## Status

**ACCEPTED + RATIFIED 2026-07-05T10:45** (HITL A0 cleared, War Mode + ADR-WARMODE-001 + Posture C bypass par HITL explicite). Append-only strict sur calendar.md + citadel trace. Les 3 crons sont pausables/remove-able a tout moment (god-mode = A0).

## Context

Suite a la cascade L+ Skill Standard (ADR-LD01-012 RATIFIED 2026-07-05T10:40) et au ship-dont-ask pattern incarne (skill saved), le captain a signale que le panneau Hermes UI "Cron Jobs" etait vide ("No scheduled jobs yet"). 

**Probleme** : la doctrine L+ exige verification recurrente des invariants (10 invariants) et la loop engineering coaching (ADR-LD01-008) exige agregation H1 Book weekly. Sans crons, ces verifications etaient manuelles = impuissance acquise par design.

**Solution** : 3 crons Hermes, Haiku model (cheap), terminal+file toolsets, alignes sur le canon L+ et le loop engineering.

## Decision

### D1 - 3 cron jobs crees dans Hermes

| # | Cron name | Schedule | Model | Job ID | Next run |
|---|---|---|---|---|---|
| 1 | daily-lplus-verification-picard | 0 9 * * * (chaque jour 9h) | haiku | d3876cd44f05 | 2026-07-06T09:00:00-04:00 |
| 2 | weekly-book-aggregator-picard | 0 9 * * 1 (chaque lundi 9h) | haiku | c72ba59e9ad4 | 2026-07-06T09:00:00-04:00 |
| 3 | hourly-picard-h10-manifest-check | 0 */6 * * * (chaque 6h) | haiku | e2181a87eb85 | 2026-07-05T18:00:00-04:00 |

### D2 - Role de chaque cron

**Cron 1 (daily-lplus-verification-picard)** : Verifie que les 3 agents canon (Picard/Jerry/Summers) dans `.claude/agents/` sont toujours alignes sur le canon L+. Output une table D1 receipts avec PASS/FAIL par agent par invariant. Si drift detecte, append un episode a `agent-os/citadel/decisions/` avec timestamp + remediation steps. **Justification L+** : invariant #10 OKF conformant + invariant #5 D1 receipts.

**Cron 2 (weekly-book-aggregator-picard)** : Execute l'agregation H1 Book weekly per ADR-LD01-008 D2. Steps : (1) parse calendar.md last 7d, (2) count L+ canon events, (3) summarize Jerry lighting 4 indicators, (4) count Picard H10 MANIFEST.md produced, (5) count Summers verse lines, (6) output weekly aggregator report + append calendar. **Justification L+** : invariant #7 Wager mesurable (H1 aggregator = 1 fiche P&L/week) + invariant #8 HITL queue visible (escalation paths).

**Cron 3 (hourly-picard-h10-manifest-check)** : HA (A3 Picard in PARA) verifie mes projets H10 toutes les 6h. Steps : (1) scan `30_Business_OS/10_Projects/`, (2) check MANIFEST.md present + modified last 30d, (3) output status table GREEN/YELLOW/RED, (4) drift detection = append episode calendar.md. **Justification L+** : invariant #9 Verify-first (projet existe avant MANIFEST.md) + invariant #8 HITL queue.

### D3 - Choix techniques canon

| Parametre | Valeur | Justification canon |
|---|---|---|
| Model | haiku | Cheap tier, suffisant pour verifications simples |
| Skills | ship-dont-ask-pattern | Pattern canon capture les 3 questions-test avant HITL |
| Toolsets | terminal, file | Read/write filesystem uniquement |
| Deliver | local | Output dans fichiers locaux append-only |
| Repeat | forever | Cron recurrence indefinite, pausable via cronjob action=pause/remove |

### D4 - Posture C (zero cron sans HITL A0 explicite)

**Justification HITL** : A0 Amadeus a emis le HITL explicite "Cree des Cron Job dans Heremes" en 2026-07-05. Ce HITL cleared la gate Posture C pour les 3 crons ci-dessus. Pas de HITL futur necessaire pour pause/remove (god-mode A0).

### D5 - Sister canon

- ADR-LD01-008 (loop engineering coaching, H1 Book aggregator weekly)
- ADR-LD01-010 (HA Picard role, H10 projects owner input)
- ADR-LD01-012 (L+ cascade ratification, source des invariants a verifier)
- ADR-WARMODE-001 (War Mode active, gates ENABLED par defaut)
- plan-lightning-l+-skill-standard-transversal (L+ canon source)

### D6 - Hors-scope explicite (YAGNI)

- Crons externes (Telegram/Slack push) - hors scope Phase 1, livrable Phase 2 si HITL A0
- Crons sur agents dormants (`_S_L0_kernel_dormant/`) - hors scope (gated Rick S1)
- Modifications destructives (rewrite calendar.md, delete citadel) - JAMAIS, append-only strict
- Activation du `/ship` outboard via cron - JAMAIS (Stark appuie le bouton)

## Consequences

### Positives

- 3 crons actifs = verification L+ canon en boucle, sans impuissance-acquise
- Hermes UI Cron Jobs panel peuple (No scheduled jobs yet -> 3 jobs actifs)
- Doctrine ship-dont-ask incarnee + saved comme skill
- HITL captain respecte (execution immediate, 0 questions)
- Append-only strict : calendar + citadel traces appendes

### Negatives / Risques

- 3 crons = ~90 runs/mois = ~$0.09/mois cout Haiku, negligeable
- Drift detection peut declencher trop d'episodes calendar si mal calibre
- Si A0 oublie les crons, ils tournent forever sans supervision (mitigation : cronjob action=list pour visibility)

### Reversibilite

```bash
cronjob action=remove job_id=d3876cd44f05
cronjob action=remove job_id=c72ba59e9ad4
cronjob action=remove job_id=e2181a87eb85
del "ADR-LD01-013_*.md"
git checkout -- "calendar.md"
del "2026-07-05_adr_ld01_013_crons_hermes.json"
```

= rollback integral.

## Anti-patterns proteges

- JAMAIS de cron sans HITL A0 explicite (Posture C) - HITL deja acquis
- JAMAIS de cron destructive (rewrite/delete) - append-only strict
- JAMAIS de cron Sonnet tier inutile - Haiku suffit
- JAMAIS de cron /ship outboard - Stark appuie le bouton

---

*Handoff canon acte 2026-07-05T10:45 ET par HA (Hermes Agent = A3 Picard in PARA) sur instruction A+ Amadeus HITL 'Cree des Cron Job dans Heremes'. 3 crons Hermes actives. War Mode + ADR-WARMODE-001 + ship-dont-ask pattern incarne.*
