---
title: SIGNAL — Pari Mindsets A'Space OS sur Real-Test % M3
date: 2026-07-03
author: A0 CC-M3 (Jumeau Numérique)
type: Signal
status: ACTIVE
horizon: W13 (2026-09-07)
tags: [wager, mindsets, audit, m3, real-test, chapel, adr-loop-003]
sister: wiki/hand_offs/audit_sessions_models_2026-07-03.md
source: CC-M3 (Jumeau Numerique)
domain: cross_layer
---

# SIGNAL — Pari Mindsets sur Real-Test % M3

> **Pourquoi un SIGNAL, pas un ADR (D5)** : on n'ouvre une ADR que sur les paris **documentés** par la mesure. Ici, le pari n'est pas encore chiffré sur assez de sessions. Le SIGNAL formalise l'engagement AVANT la fenêtre de mesure ; l'ADR viendra au W4 quand T1×8 aura livré ses 1ers artefacts sous compression.

## Le pari (verbatim, A0-emendé 2026-07-03)

> *« Transformer le pari Mindsets en wager mesurable. Métrique = real-test % de M3 sur les 20 prochaines sessions. Verdict = Chapel au scorecard W13. »*

## D1 receipts (baseline mesurée 2026-07-03)

| Métrique | M3 baseline (29 sessions, 06-06 → 07-03) | Source |
|---|---|---|
| Real-test-after-edit | **30 %** (7/23 sessions auditées) | `audit_sessions_models_2026-07-03.md` |
| Reason-before-act | 47 % / 77 % avec thinking | idem |
| Re-evaluate | 49 % / 77 % avec thinking | idem |
| Plan-gate | 75 % | idem |

## Cibles proposées (à acter en ADR au W4)

| Métrique | Baseline | Cible W13 | Levier |
|---|---|---|---|
| **Real-test % (la métrique D5 critique)** | 30 % | **≥50 %** (×1.67 lift) | Hook `posttooluse-test-after-edit` passe de log-only → hard-block sur Edit/Write API tier |
| Reason-before-act (règle B) | 47 % | ≥65 % | MindSets pulldowns explicites (Beth_Dispatch §Penser Dense) |
| Re-evaluate | 49 % | ≥60 % | MindSets Morty_Dispatch (OBSERVE + RE-EVALUATE) |
| Plan-gate | 75 % | ≥80 % | Garder (déjà canon) |

## Owner

Chapel (A3 SNW Measurement). Verdict au scorecard W13 / DEAL uplink (09/07/2026).

## Stop-condition

Si à W8 (mi-parcours) real-test reste ≤35 % → le pari échoue, ADR-META-005 passe en review, la question soulevée à S1 Rick.

## Sacred exclusions

- Pas de CronCreate (mesure manuelle au weekly review Churchill/Rutherford)
- Pas d'auto-édition des Mindsets pour gonfler la mesure (D6 : on mesure ce qui sort du runtime, pas ce qu'on a changé)

## Linkage

- `wiki/hand_offs/audit_sessions_models_2026-07-03.md` — baseline chiffrée
- `plan-strategie-cc-l1-zora-macro.md` §9 — calendrier Q3 complet
- `wiki/hand_offs/proposal_u1_supabase_symphony_state_2026-07-03.md` — l'uplink Symphony→Supabase alimente aussi Chapel (scorecard live)

## Action

Pas d'ADR avant W4. Au W4 : si T1×8 a livré ≥5 sessions M3 nouvelles (W3 final + W4 = ~10 attendues), passer le pari en ADR avec données complètes.
