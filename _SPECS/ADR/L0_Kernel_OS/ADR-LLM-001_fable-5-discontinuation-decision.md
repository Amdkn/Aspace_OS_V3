---
id: ADR-LLM-001
title: Fable 5 Discontinuation Decision — Mythos Glasswing + Fable-MiniMax-M3 Fallback
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L0 Tech_OS / Runtime / Model Selection
tags: [#ADR #llm #fable-5 #mythos #glasswing #mini-max-m3 #model-agnostic #sovereignty]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-META-002-E13, ADR-RICK-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "fable_mort_claim_d1_falsification handoff 2026-06-15"]
provenance: |
  Née 2026-06-15 du handoff D1-falsification "Fable Is Gone" (Mission ρ, 6 transcripts YouTube Mark Kashet
  + Melvynx) où A2 a falsifié partiellement la claim littérale "Fable 5 disparu" tout en validant la fin
  d'accès public Fable 5 le 12 juin 2025 et l'évolution vers Mythos (Glasswing, US-only). Backstop = Tilly
  guide 05 (Fable = MiniMax-M3 backend, D1 verified live 2026-06-15 api.minimax.io).
sign_off_a0: "A0 Amadeus — Go ADR-LLM-001 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-LLM-001 — Fable 5 Discontinuation Decision

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **Mission ρ 2026-06-15** a ingéré 6 transcripts YouTube "Actualités IA" francophones (mission A2 antérieure :
   vision-IA + 5 vidéos post-Anthropic-pause). D1-falsification : le claim "Fable Is Gone" (Mark Kashet, vidéo
   02) est partiellement vrai — Fable 5 accès public a été désactivé le **12 juin 2025** (~1 an avant
   cette session), mais le **backend sous-jacent (MiniMax-M3 via api.minimax.io) reste live** (D1 receipt :
   `curl https://api.minimax.io/anthropic` → 301 + 401 auth wall, request_id `067ed481ef336027cabbf3fc4b5d5d70`).
2. **Mythos (successeur Fable)** : confirmé US-only via Glasswing (vidéo 05 transcript l.302). A'Space OS V2
   n'est **pas éligible** Mythos (A0 = France, Glasswing = US compliance layer).
3. **Fable-Mindset ≠ Fable-marque** : le "rythme Fable" (12 principes + decision loop + JSONL mining) est
   un **playbook model-agnostic** (Tilly guide 05 §"Make ANY Model Think Like Fable in Minutes") qui se
   distille depuis les traces Fable 5 (HuggingFace `Glint-Research/Fable-5-traces`, 4665 traces) et s'injecte
   dans n'importe quel LLM (Opus 4.8, Sonnet, Ollama, Mistral) via trinité hook + skill + `CLAUDE.md`.

## Decision

**D1 — LLM runtime principal A'Space V2 reste Fable-MiniMax-M3** (backend `https://api.minimax.io/anthropic`,
déjà opérationnel via `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN` env User scope). Pas de bascule forcée vers
Mythos (US-only incompatible), Sonnet ($ premium), ou Ollama local (overhead setup VPS non justifié à date).

**D2 — Fable-marque (Anthropic public) treated as DISCONTINUED** : ne plus présumer qu'un nouveau compte
Anthropic accède à Fable 5. Documentation onboarding A2 : pointer vers `api.minimax.io` directement.

**D3 — Fable-Mindset reste canonique** : le skill `/tilly-fable-rhythm` (créé 2026-06-15 Phase 2 autonomie) est
l'**adaptation officielle** de la doctrine Fable au contexte A'Space. ROI ~30 min/invocation (audit cognition
Tilly vs rythme Fable). D11 métrique empirique Fable (META-002 Extension 2026-06-15) reste la baseline.

**D4 — Pas de vendor lock-in** : si Fable-MiniMax-M3 devient indisponible (claim YouTube "Fable Is Gone" se
confirme côté backend), fallback immédiat vers Sonnet 4.6 (Anthropic direct) ou Ollama local Mistral 7B
(via prescription ADR-REG-001). E13 Model-Agnostic Frugality (META-002 Extension 2026-06-15 l.246-253) ancre
cette discipline.

## Consequences

- ✅ Aucun changement opérationnel immédiat — runtime A'Space V2 reste Fable-MiniMax-M3 jusqu'à preuve de panne.
- ✅ Documentation onboarding A0/agents futurs : pointer `api.minimax.io`, pas "Fable 5 Anthropic public".
- ✅ Skill `/tilly-fable-rhythm` = port officiel doctrine Fable → A'Space (model-agnostic, fonctionne avec tout LLM).
- ✅ Backup doctrinal prêt : Sonnet ou Ollama Mistral en cas de panne MiniMax-M3.
- ⚠️ Si A0 veut tester Sonnet ou Ollama en parallèle = créer ADR-OPS-002 (Glasswing compliance check) avant.

## References

- `wiki/hand_offs/handoff_fable_mort_claim_d1_falsification_2026-06-15.md` (Mission ρ, 213 lns).
- `wiki/hand_offs/handoff_fable_to_minimax_distillation_2026-06-15.md` (Mission σ, 233 lns).
- `~/.claude/skills/tilly-fable-rhythm/SKILL.md` (créé 2026-06-15, ROI ~30 min/invocation).
- `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/LD04_Cognition_Tilly/05-make-any-model-think-like-fable-in-minutes.md` (Tilly guide 05 canonique).
- `youtube_ingest_2026-06-14/transcripts/02-fin-fable-5.md` (l.232 — Fable 5 accès public désactivé 12 juin 2025).
- `CLAUDE.md` section "Runtime LLM (backend)" — déclaration MiniMax-M3 via `https://api.minimax.io/anthropic`.
