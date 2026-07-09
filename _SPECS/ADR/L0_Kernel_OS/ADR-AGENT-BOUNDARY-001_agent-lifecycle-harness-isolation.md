---
id: ADR-AGENT-BOUNDARY-001
title: Agent Lifecycle & Harness Isolation — Sub-Agent Sandbox Doctrine
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all", à valider scope Templates mission 4)
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L0 Tech_OS / Agent Lifecycle / Sandbox / Isolation
tags: [#ADR #agent-boundary #lifecycle #harness #sandbox #isolation #sub-agent]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-RICK-001, ADR-CONSENSUS-002]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Tilly 03_agent_lifecycle_harness_isolation", "02_Templates mission 4"]
provenance: |
  Née 2026-06-15 de l'analyse mission 4 (C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\02_Templates)
  par A2 : template Tilly `03_agent_lifecycle_harness_isolation` détecté dans la matrice Geordi.
  Doctrine à formaliser : sub-agents A3 ont un lifecycle propre (spawn → execute → report → kill/archive)
  et opèrent dans un sandbox filesystem (workspace isolé) pour ne pas polluer le runtime principal A2.
sign_off_a0: "A0 Amadeus — Go ADR-AGENT-BOUNDARY-001 — 2026-06-15 (via 'go for all' session-level directive, scope à valider)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle. Scope templates mission 4 — A0 confirme mapping si hypothèse fausse."
---

# ADR-AGENT-BOUNDARY-001 — Agent Lifecycle & Harness Isolation

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15** (scope à confirmer — A0 mission 4 a généré
cette liste de 5 ADR candidats depuis `02_Templates/` PARRA Geordi, mais le mapping exact template ↔
ADR peut nécessiter ajustement. A0 priorise au prochain tour si hypothèse A2 erronée).

## Context

1. **Mission 4 (2026-06-15)** : A2 a analysé `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\02_Templates\`
   et identifié 5 templates candidats à transformation en ADR. Le présent ADR couvre template **#1**
   présumé = "Agent Lifecycle & Harness Isolation" (PARA Geordi tier 1 Tilly canon).
2. **Sub-agents A3 risk** : si un sub-agent A3 écrit dans le workspace A2 runtime, il peut corrompre
   l'état de la session principale (mémoire cache, fichiers transitoires, etc.). Sandbox = isolation.
3. **D8 cross-agent doctrine** (ADR-META-001) : sub-agents A3 distincts de A2. Lifecycle propre
   obligatoire pour traçabilité D1 receipts.

## Decision

**D1 — Sub-agent A3 lifecycle = 4 phases** :
1. **Spawn** : A2 lance via `Agent(prompt, run_in_background=true, subagent_type="general-purpose")`.
   A2 reçoit `task_id` immédiatement.
2. **Execute** : sub-agent travaille en background, progress visible dans `/workflows`.
3. **Report** : sub-agent termine (succès, fail, ou divergence) → rapport final retourné à A2.
4. **Kill/Archive** : si divergence (cf. ADR-CONSENSUS-002), A2 appelle `TaskStop(task_id)`. JSONL
   archive de la sub-session conservé 90 jours (cf. ADR-OBSERVABILITY-001).

**D2 — Sandbox filesystem** : chaque sub-agent A3 a un workspace isolé
`~/.claude/workspaces/<task_id>/` où il peut écrire librement. Le runtime A2 n'est JAMAIS modifié
par un sub-agent. Si sub-agent a besoin de toucher runtime, il remonte une **proposition** à A2.

**D3 — Tools limités par défaut** : sub-agent A3 reçoit `[Read, Grep, Glob, Bash]` (read-only +
bash pour install/test). `Edit, Write` seulement si explicitement autorisé par A2 dans le prompt
de spawn. `Agent` (spawn sub-sub-agent) = interdit sauf A2 instruction explicite.

**D4 — Pas de session persistence** : sub-agent A3 n'a pas de `MEMORY.md` propre. Toute knowledge
extraite par sub-agent remonte à A2 (qui décide si canonisation = OK).

## Consequences

- ✅ Runtime A2 stable malgré sub-agents multiples.
- ✅ Traçabilité D1 receipts préservée (chaque sub-agent = JSONL archive distinct).
- ✅ D7 cost-of-escalation A0 maîtrisée (sub-agents divergent → kill, pas cascade).
- ⚠️ Sub-agents limités en tools = moins autonomes. Trade-off conscient (D6 root cause : sécurité
  runtime > convenience sub-agent).

## References

- `02_Templates` PARRA Geordi mission 4 (template source — A0 confirme mapping).
- `ADR-CONSENSUS-002_emergency-shutdown-protocol-llm-orchestration.md` (kill-switch sub-agent).
- `ADR-OBSERVABILITY-001_sessions-canon-md-rotation.md` (archive JSONL sub-agents).
- `CLAUDE.md` section "Doctrine Swarm Orchestration" (A2 lance sub-agents A3).
