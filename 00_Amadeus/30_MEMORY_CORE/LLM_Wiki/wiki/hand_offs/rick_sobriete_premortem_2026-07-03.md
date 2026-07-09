---
title: Rick Sobriete premortem scaffolding (F1-F15 risks)
date: 2026-07-03
author: CC-M3 loop-operator (loop v2, Fable 5)
layer: S1 - Soberte Kernel (differed Q4 2026 / Q1 2027)
status: SCAFFOLDING ONLY - no ratification, no cron, doctrine-deferred
tags: [#loop #white-gate #rick #sobriete #premortem #f1-f15 #differed]
related:
  - .claude/mindsets/Rick_Mindset.md (A1 Rick kernel)
  - .claude/mindsets/B1_Manifesto.md (B1 Manifesto, §Sobriety)
  - _SPECS/ADR/L1_Life_OS/ADR-SOBER-002_anti-paperclip.md
blast_radius: kernel pivots only (~1x/an), max scope = L0 infrastructure
source: CC-M3 loop-operator (Fable 5, A0 Jumeau Numerique twin)
type: doctrine
domain: cross_layer
---

# Rick Sobriete Premortem Scaffolding - F1-F15 Risks

> **Doctrine** : Rick = A1 Soberte kernel. Rare gate (~1x/an). NE tourne PAS en loop. Scaffold only = preparation intellectuelle SANS action. A0 + Rick valideront Q4 2026+.

## F1 - Soberte gate drift (auto-promotion Rick)

**Risque** : Rick Mindset glisse de gatekeeper sobriete vers orchestrateur actif.
**Mitigation** : F1 only = VETO/OK sur nouvelle complexite. Jamais executor.
**Source** : Rick_Mindset.md GROUND > SOBER > REASON > ACT > OBSERVE > RE-EVALUATE > VERIFY.

## F2 - Anti-paperclip trigger #5 (A1 > B1 sans A0 HITL)

**Risque** : un cron A1 declenche un side-effect B1 sans validation A0 explicite.
**Mitigation** : Sobriete gate B1_Manifesto : NO A1 > B1 cron sans A0 HITL.
**Source** : B1_Manifesto.md §Sobriety.

## F3 - Donna DLQ saturation

**Risque** : Dead Letter Queue s'accumule sans review periodique.
**Mitigation** : DLQ weekly review (A0 + Rick), purge soft via _TRASH_<date>_donna_dlq/.
**Source** : Rick_Mindset.md (Donna DLQ).

## F4 - Deep Checkpoint Law violation

**Risque** : migration/purge sans checkpoint prealable (lecons 2026-03-05 A0_Memory loss).
**Mitigation** : Checkpoint obligatoire > 100 MB. Inventaire avant Remove-Item.
**Source** : CLAUDE.md "Loi du Checkpoint Profond".

## F5 - Stop-condition bypass

**Risque** : stop-condition (2 fails, canon touch, 2h cap, RATIFIED edit) contournee.
**Mitigation** : hard-block hook ADR-META-005 Vague 3 (Q4 2026). En attendant : log-only + manual review.
**Source** : ADR-META-005_hooks-automation.md.

## F6 - A1 Rick <-> A1 Beth/Morty conflict

**Risque** : Rick VETO entre en conflit avec Beth ALIGNEMENT ou Morty EXECUTION.
**Mitigation** : precedence Rick sur complexite (kernel), Beth sur sens (life), Morty sur finition (focus). Pas de fusion.
**Source** : mindsets/Beth_Mindset.md + Morty_Mindset.md.

## F7 - Cost-of-escalation A0 explosion

**Risque** : trop d'escalades A0 (~100x cout erreur) brule la souverainete.
**Mitigation** : Phase 2 Hermes-style auto-resolution (skill creator reflex). Notification outbox only.
**Source** : ADR-META-001 D7 + ADR-META-002 D9-D12.

## F8 - M3 laziness non-mesuree

**Risque** : Real-test M3 stagne < 50% malgre Mindsets runtime.
**Mitigation** : wager Mindsets 30% > 50% (W13 verdict), si fail = S1 Rick escalation.
**Source** : 2026-07-03_wager_mindsets_real_test.md + ADR-META-007 (PROPOSED).

## F9 - D6 catalog non-maintenu

**Risque** : root causes oublies, meme erreurs repeat.
**Mitigation** : D6 catalog append-only (ADR-META-006). Entree par root cause identifie.
**Source** : ADR-META-006_d6-root-causes-catalog.md.

## F10 - L0 infrastructure fragile (no L0 in 2026)

**Risque** : L0 Doctors/Compagnons Rick Verse non spec, kernel OS sans foundation.
**Mitigation** : L0 spec differ Q4 2026 (plan §3), 2027 incarnation. Pas de shortcuts en attendant.
**Source** : plan-strategie-cc-l1-zora-macro.md §3.

## F11 - Sandbox override (D7 cost-of-escalation)

**Risque** : trop de sandbox=OFF loops, A0 HITL sature, souverainete brulee.
**Mitigation** : sandbox=OFF documente par loop avec cost-of-escalation ledger. A0 GO = HITL valide.
**Source** : ADR-LOOP-002 loi 3.

## F12 - Telegram HITL fragile (deferred)

**Risque** : Telegram channel Down, A0 Ohio GMT-4 communication gap.
**Mitigation** : HITL pocket channel = artefact differes. Terminal = current. Telegram DORMANT.
**Source** : mindsets/Telegram_HITL_Mindset.md (2026-06-25).

## F13 - Desktop Commander blast radius

**Risque** : Desktop Commander local-FS/process = higher blast radius que read-only.
**Mitigation** : config true (2026-06-25), pending CC restart. 4 gates HITL avant activation.
**Source** : mindsets/DesktopCommander_Mindset.md.

## F14 - Wager sans metric (verification impossible)

**Risque** : wager declare sans baseline mesurable, verdict W13 impossible.
**Mitigation** : wager template obligatoire (metric + delta + horizon + verdict differ). Chapel audite.
**Source** : ADR-LOOP-003_orient-layer-signals-wagers.md.

## F15 - Soberte gate auto-shutdown

**Risque** : trop de vetos Rick > agents demotivés, systeme freeze.
**Mitigation** : Rick rare (~1x/an), notification outbox only, pas de hard-block cron Q3 2026.
**Source** : Rick_Mindset.md GROUND default.

## Status

**SCAFFOLDING COMPLETE** : 15 risques identifies, mitgations sourcees. Aucune action. A0 + Rick valideront Q4 2026+.

## Sacred exclusions

- PAS de ratification Rick (A0 + Rick only, Q4 2026+)
- PAS de CronCreate (Sobriete = manuel)
- PAS d'auto-edit mindsets/Rick_Mindset.md (canon, D4 append-only)
- PAS d'activation hard-block hook (Vague 3 differ Q4)
