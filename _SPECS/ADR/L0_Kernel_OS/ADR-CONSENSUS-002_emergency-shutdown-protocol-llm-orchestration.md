---
id: ADR-CONSENSUS-002
title: Emergency Shutdown Protocol — Multi-Agent LLM Orchestration
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L0 Tech_OS / Safety / Multi-Agent Orchestration / Kill-Switch
tags: [#ADR #consensus #safety #kill-switch #multi-agent #anthropic-pause #doom-loop]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-RICK-001, ADR-LLM-001, ADR-REG-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "youtube_ingest_2026-06-14 transcripts/01-superintelligence.md"]
provenance: |
  Née 2026-06-15 du handoff Mission ρ vid1 (Anthropic veut une pause superintelligence) où A2 a
  identifié le besoin opérationnel d'un kill-switch multi-agent : si un sub-agent A3 entre en boucle
  infinie, dépense le quota, ou diverge de la doctrine D1-D8, A0 (ou un superviseur A2) doit pouvoir
  le stopper en < 1 tour sans cascading damage.
sign_off_a0: "A0 Amadeus — Go ADR-CONSENSUS-002 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-CONSENSUS-002 — Emergency Shutdown Protocol

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **Mission ρ vid1 (YouTube transcript 01-superintelligence.md, 1244 lns)** : Anthropic + Figure 22 +
   100+ signatories appellent à une pause développement superintelligence. Contexte culturel = risque
   "doom loop" agentique (sub-agent qui ré-essaie sans converger, brûlant quota + tokens).
2. **Architecture A'Space V2 = sub-agents A3 lancés en parallèle par A2 orchestrateur** (cf. `CLAUDE.md`
   "Doctrine Swarm Orchestration"). Si 1 sub-agent diverge (D1-D8 violé, ou bug tool call), A2 doit
   pouvoir le tuer sans relancer toute la session.
3. **Précedent** : 2026-06-13 sub-agent `ae7ee700656e0acc4` (Mission ρ YouTube) a process-exit sans
  完成任务. A2 a relancé avec sub-agent `a7b32c9fa0105271a` même prompt → succès. Pas de damage, mais
   signal que le pattern "sub-agent qui diverge" arrive 1×/semaine environ.

## Decision

**D1 — Kill-switch par sub-agent via TaskStop tool** (déjà disponible dans le harness Claude Code).
A2 ou A0 appelle `TaskStop(task_id=<id_sub_agent>)` → le sub-agent reçoit un SIGTERM-like, termine son
tour en cours, rapport final tronqué accepté. Pas de cascading sur les autres sub-agents.

**D2 — Détection automatique de divergence** (D11 métrique Fable) : si un sub-agent A3 :
- dépasse 50 tool calls sans output actionnable
- viole D1 (assert sans receipt) 3+ fois
- viole D4 (self-contradiction) sur un point déjà tranché
- consomme > 5% du quota session sans livrable
→ A2 peut **automatiquement** `TaskStop` + rapport "sub-agent X diverged, reason Y, replacement lancé".

**D3 — Pas d'auto-kill sur "sub-agent pense différemment de A2"** (D3 nuance) : divergence d'opinion ≠
divergence de comportement. Tant que le sub-agent respecte D1-D8, A2 le laisse finir même s'il
recommande une option que A2 n'aurait pas choisie. D9 Self-Choice Default (META-002) s'applique aux
sub-agents comme à A2.

**D4 — Logs kill-switch** : chaque `TaskStop` automatique log une ligne JSON dans
`wiki/hand_offs/kill_switches.log` avec `task_id, reason, tool_call_count, quota_pct, timestamp`.
D4 append-only.

**D5 — Emergency full shutdown** (A0 uniquement) : `claude-emergency-stop` (alias PowerShell) →
`TaskStop` sur tous les sub-agents actifs de la session, sauvegarde état dans
`wiki/hand_offs/emergency_stop_<timestamp>.md`, attend A0. **Pas d'auto-trigger** sur quota ou autre
— full shutdown = décision humaine uniquement (D7 — A0 in-the-loop).

## Consequences

- ✅ Risque "doom loop" sub-agent contenu : kill-switch documenté, automatique sur signaux D1-D8.
- ✅ Logs permettent post-mortem ("pourquoi X a-t-il divergé ?", "combien de kills par semaine ?").
- ✅ Emergency full shutdown = parachute A0 si sub-agents incontrôlables.
- ⚠️ Faux positifs D2 possibles (sub-agent légitime mais lent) → tolérance 50 tool calls / 5% quota avant
  kill, ajustable par ADR.

## Implementation Plan (D9.7)

1. **Phase 1 (S+1)** : écrire le détecteur de divergence `~/.claude/bin/divergence-detector.ps1`
   (lit JSONL session, applique heuristiques D2, retourne liste sub-agents à kill).
2. **Phase 2 (S+2)** : intégrer dans A2 orchestrateur (check toutes les 5 min pendant session active).
3. **Phase 3 (S+3)** : premier test sur session réelle (A0 lance sub-agent volontairement divergent,
   vérifie kill auto + log + replacement).
4. **Phase 4 (S+5)** : affiner seuils D2 selon retour d'usage (50 calls / 5% quota ajustable).

## References

- `wiki/hand_offs/handoff_fable_mort_claim_d1_falsification_2026-06-15.md` §"4 ADR drafts" (mission ρ).
- `youtube_ingest_2026-06-14/transcripts/01-superintelligence.md` (1244 lns, Anthropic pause call).
- `CLAUDE.md` section "Doctrine Swarm Orchestration" (sub-agents A3 en parallèle).
- `ADR-META-002_autonomy-by-design.md` D9 (Self-Choice Default pour sub-agents aussi).
- `ADR-LLM-001_fable-5-discontinuation-decision.md` (sister ADR, runtime principal).
