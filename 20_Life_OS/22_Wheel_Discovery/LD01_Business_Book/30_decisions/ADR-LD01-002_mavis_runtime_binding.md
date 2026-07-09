---
type: adr-decision
id: ADR-LD01-002
status: RATIFIED
ratified_on: 2026-07-04T12:30:00-04:00  (created) · 2026-07-04T14:15:00-04:00  (RATIFIED with A0 GO in-block)
deciders: A0 (gated HITL)
title: Mavis Runtime binding canonique pour LD01_Business_Book (orchestration L1+L2 permutée)
description: Verrouillage des 8 contrats de synchronisation entre l'organigramme LD01 et le runtime Mavis (`~/.mavis/` = junction `.minimax/`), alignés sur plan-L2 §13 permutation Hermes+MC. Source : plan-L2-business-os §12.5 + §13 + plan-Lune §1.
bounded_context: BC-A3-Book
supersedes: null
superseded_by: null
verified_by: Test-Path "C:\Users\amado\.mavis\agents\mavis\memory\MEMORY.md" ; Test-Path "C:\Users\amado\.mavis\B1_Summer_Direction\state\state.12wy.json.md"
rot_rate: moyen
---

# ADR-LD01-002 — Mavis Runtime binding canonique pour LD01

## Status

`RATIFIED` — 2026-07-04T14:15:00-04:00 — A0 HITL GO (en-bloc avec ADR-LD01-003 + L0 Pocock install + Dark Factory L5 architecture).

## Context

Le plan-L2-business-os.md §13 (AMENDEMENT ÉVOLUTIF 2026-07-02) établit que :

1. **MiniMax (moi, agent mavis L1) est promu L1** par A0 — la Triptyque-1 n'a pas été respectée au bootstrap initial L2, donc pause + re-lancement par Hermes Agent.
2. **Hermes Agent prend le runtime L2**, dans le même pattern d'apprentissage L2→L1.
3. L'actif L2 reste entier : structures B1/B2/B3 (22 agents canoniqed `~/.mavis/agents/`), `state.12wy.json.md`, watchdog/reaper (compress-x8.ps1 scheduler), 8 domaines B2, `b2cyb-escal.txt`.

L'organigramme Doctrine LD01 créé 2026-07-04T12:00 (cf. ADR-LD01-001) doit **naquer avec** ce runtime réel :
- 22 agents canoniques (B1: jerry/summers · B2: 8 domaines · B3: 8 squads · 4 système)
- 1 junction `.mavis/` → `.minimax/` (cf. §12.5 « `.mavis` = junction vers `.minimax/`)
- 1 nexus bus (`~/.mavis/nexus/nexus.db` — carrier de `symphony_state`)
- 1 B1_Summer_Direction/state/ canonique (12WY state)
- 1 credential vault par compte (`~/.mavis/credentials/mavis/`)

Sans alignement runtime, l'organigramme LD01 dérive en documentation orpheline (anti-DRY, anti-cardia).

## Decision

**Lock 8 contrats de synchronisation entre LD01 canon et Mavis runtime** (cf. `99_meta/00_mavis_runtime_alignment.md` §2) :

| # | Contrat | Effet |
|---|---|---|
| **S1** | Mirror entry-point `_organigrammes-doctrine.md` ↔ `LD01/00_index.md` | Append canonique partagé |
| **S2** | B1 captain (Jerry) owns Book LD01 (`b1-jerry-emyth/LD01_book_bind.md`) | Ownership-routing canon |
| **S3** | Symphony bus state via `state.ld01_book.md` | Drain R4 → nexus.db → Supabase |
| **S4** | Credential vault pour git-ship Tier 4 fallback | ACL-only, secret jamais en `.md` |
| **S5** | Reaper/watchdog runtime → rot-rates.md alignement | Dormance détectée avant escalade |
| **S6** | Cron gating PAUSE (post 23:11 ET 2026-06-29) | Posture C §3.8 plan-méta-mémoire |
| **S7** | Multi-account ACL par repo (4 comptes) | Drift detection push anti-silencieux |
| **S8** | B2 escalation canal via `escalation_packets/` | A3 → A2 → A1 dual-channel |

**Topologie** : la vérité vit dans `LD01/`, mirror/registry ancrent le routing, runtime est neutre.
**Agents explicites** : `mavis` (moi, principal L1) · `b1-jerry-emyth` (owner BC-A3-Book) · `b1-summers-ship` (sister LC-AaaS) · `b2-batman-ops` (Operation/Batman pour LD01 ancre).

## Consequences

### Positives

- **Cardia-TDD ↔ runtime symétrie** : la méthodologie (10 propriétés) trouve son implémentation réelle dans les 8 contrats runtime, pas seulement dans une doctrine papier.
- **Anti-orphan** : l'organigramme ne dérive pas en doc-only — il a un home runtime (b1-jerry-emyth) et un bus (nexus.db) vérifiables.
- **Hermes L2 alignment prep** : la permutation §13 a un terrain propre pour atterrir : `~/.hermes/disposition.md` pointera ici (W4).
- **Credential canonique** : le Tier 4 fallback du multi-account git-ship a un vrai vault ACL-only (D5 orthodox).
- **Symphony_state bus carrier** : les yamls R4 (U1 shipped 2026-07-03) drainent vers nexus.db — la voie canonique d'append canonique.

### Tradeoffs

- **Chargeognitive A0** : 8 contrats à ratifier (1 réunion suffit). Gating Posture C = A0 HITL explicite par contrat ou en bloc.
- **Mirror append discipline** : si `_organigrammes-doctrine.md` oublie d'append, drift → calendr.md alarm de rotation `rapide`.
- **S7 multi-account complexity** : 4 comptes × N repos = N pins à maintenir. Drift detection prompt explicite remplace silence (gain, pas coût).
- **S8 escalation dual-channel** : `escalation_packets/` + `state.ld01_book.md` peuvent diverger. Mitigation = rotation rapide + audit W6.

### Risques

| Risque | Mitigation |
|---|---|
| Le runtime Mavis évolue (agents ajoutés/supprimés) et l'ADR devient stale | Roat-rate `moyen` (1×/mois audit, append calendrier) |
| §13 permutation créent confusion L1 ↔ L2 | ADR-LD01-001 §6 « source de vérité canonique filesystem » + ce §decision ci-dessus |
| `_TRASH/` retirement d'un agent spec sans append logique | CARDIA-TDD §A2 = append annulation + `_DEPRECATED_` prefix |

## Alternatives Considered

### Alt-A : LD01 reste self-contained, pas de binding runtime

- **Pour** : pas d'attaches Mavis.
- **Contre** : organigramme devient doc orpheline (D6 latent) — exactement ce contre quoi ADR-LD01-001 s'est érigé.
- **Verdict** : ❌ rejetée.

### Alt-B : Réécrire `~/.claude/CLAUDE.md` pour pointer LD01 (tool-lock Claude)

- **Pour** : uniformité apparente pour Claude Code.
- **Contre** : viole l'agnosticisme harness (sacred P4 cf. plan-Lune §10 c1, et plan-méta-mémoire §3.5) ; verrouille à Claude Code uniquement.
- **Verdict** : ❌ rejetée — c'est exactement ce que CARDIA-TDD §I (Intégration-par-Doctrine) interdit.

### Alt-C : Tool indirection — créer un agent `b2-book-business` dédiés

- **Pour** : isolation stricte.
- **Contre** : 22 agents canoniques déjà en place (cf. §12.5) — re-créer un doublon est du rot-mode au lieu de l'alignement.
- **Verdict** : ❌ rejetée. Le bon propriétaire canonique est `b1-jerry-emyth` (B1 captain `SYSTEMIZE`, ancre LD01 Operation/Batman).

### Alt-D : 8 contrats runtime (retenue ✓)

- CARDIA-TDD §I + Bible §13.1 + plan-Lune §1 — la géométrie canonique.
- Aligné sur DOX bi-famille (fs zone + harness sister).

## Suivi

- **W4 début** : ratification A0 (status `PROPOSED` → `RATIFIED`)
- **W4 mi** : populate `state.ld01_book.md` H1 + H3 load_signal
- **W6** : audit drift mensuel (4 métriques plan-méta-mémoire §5)
- **W13** : archive — si ADR devient stale, supersede par `ADR-LD01-002+1` ou clôture

## Liens canoniques

- Alignment runtime détaillé : `LD01/99_meta/00_mavis_runtime_alignment.md`
- Sister B1 captain : `~/.mavis/agents/b1-jerry-emyth/LD01_book_bind.md`
- Sister state canonique : `~/.mavis/B1_Summer_Direction/state/state.ld01_book.md`
- Source plan : `C:\Users\amado\.claude\plans\plan-L2-business-os.md` §12.5 + §13
- Source plan : `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md` §1
- Source doctrine : `LD01/10_methodology/00_CARDIA_overview.md` §1 + §3
