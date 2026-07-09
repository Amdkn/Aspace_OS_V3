---
id: ADR-META-003
title: Model-Agnostic Runtime Doctrine — Harness Invariant, Model Variable
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L1 Life_OS / Meta-Cognition / Runtime Doctrine / Vendor Independence
tags: [#ADR #meta #model-agnostic #harness #runtime #sovereignty #vendor-lockin]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-META-002-E13, ADR-LLM-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "ADR-META-002 Extension 2026-06-14 E13"]
provenance: |
  Née 2026-06-15 de la Mission σ (Fable→MiniMax distillation) où A2 a recommandé en Open Question
  (META-002 l.144) la création d'un ADR-META-003 séparant proprement harness (invariant) de modèle
  (variable). Triggé par Tilly guide 05 ("Make ANY Model Think Like Fable") + D1 verify
  api.minimax.io live 2026-06-15 + risque vendor lock-in accidentel.
sign_off_a0: "A0 Amadeus — Go ADR-META-003 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-META-003 — Model-Agnostic Runtime Doctrine

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **META-002 Extension 2026-06-14 §E1-E12** + **META-002 Extension 2026-06-15 §E13** ont déjà
   établi que l'autonomie D9-D12 est **runtime-anchored, pas model-anchored**. Le présent ADR
   promeut cette insight au rang de **doctrine META tier 1** (sister à META-001, META-002).
2. **Tilly guide 05** (cf. `LD04_Cognition_Tilly/05-make-any-model-think-like-fable-in-minutes.md`)
   démontre que le rythme Fable (12 principes + decision loop) est un **playbook model-agnostic** :
   il se charge dans `~/.claude/CLAUDE.md` + skill + `MEMORY.md` (la trinité canonique) et fonctionne
   avec Opus 4.8, Sonnet, Ollama Mistral, etc.
3. **Risque vendor lock-in** : si A'Space doctrine dit "Fable-marque = source de vérité cognitive",
   alors disparition Fable-marque = effondrement doctrinal. La protection = énoncer explicitement
   que **le modèle est variable, le harness est invariant**.

## Decision

**D1 — Le harness A'Space est l'invariant de comportement** :
- `~/.claude/CLAUDE.md` (injection runtime)
- `AGENTS.md` (canon A0-A3 fractal)
- `MEMORY.md` (mémoire persistante inter-sessions)
- `~/.claude/skills/*` (skills injectables)
- `wiki/hand_offs/*` (doctrine opérationnelle, ADR, logs)

Ces 5 composants **fonctionnent identiquement** quel que soit le LLM résolu par
`ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN`/`OLLAMA_HOST`.

**D2 — Le LLM est une variable interchangeable** :
- Aujourd'hui : Fable-MiniMax-M3 (`api.minimax.io/anthropic`).
- Demain : Sonnet 4.6 direct Anthropic, ou Mistral 7B Ollama local (cf. ADR-REG-001), ou autre.
- Le harness **ne présume pas** que le LLM est stable. Si swap, D9-D12 (autonomie) restent effectifs.

**D3 — Le rythme (decision loop) survit à la marque** :
- Pattern "plan-then-act, reads-before-edits, tests-after-edits" (Fable mindset) est model-agnostic.
- 12/12 principes Fable Mindset = (P)ortable (Mission σ D1 verify).
- Skill `/tilly-fable-rhythm` ne référence pas la marque Fable, seulement le pattern.

**D4 — D1 receipts vendor-independent** : tout audit "est-ce que A'Space dépend de X vendor ?"
doit retourner 0 dépendance critique. X peut être meilleur ou moins bon, mais A'Space ne tombe pas
si X tombe. D11 métrique Fable (META-002 Extension 2026-06-15) reste la baseline de comparaison.

**D5 — E13 Model-Agnostic Frugality promu E1.13 doctrine META** : la frugalité TOKEN (coût d'escalade
A0 > coût d'une décision réversible + rollback) est un **invariant de design**, pas un quota vendor
spécifique. Si A0 bascule Sonnet ($) ou Ollama ($0), le raisonnement frugal reste valide.

## Consequences

- ✅ A'Space OS V2 n'est **pas** un projet "Fable wrapper" — c'est un projet harness-anchored qui
  exploite Fable-MiniMax-M3 quand disponible, et continue de fonctionner sans.
- ✅ Onboarding nouveaux agents/VMs : `git clone` du harness suffit, le LLM se résout par env.
- ✅ Sovereignty A0 renforcée : A0 peut rotator vendor sans ré-écrire la doctrine.
- ✅ SISTER ADR explicite : META-001 (D1-D8) + META-002 (D9-D12) + **META-003 (D13 model-agnostic)**.

## Anti-patterns prévenus

- ❌ "A'Space est cassé si Fable-marque meurt" (vendor lock-in accidentel).
- ❌ "On doit ré-écrire CLAUDE.md quand on change de LLM" (harness mal découplé).
- ❌ "Fable 5 a une feature unique X que les autres n'ont pas" (sauf si feature = propriété poids
  ET critique — alors ADR dédié pour justifier dépendance).

## References

- `ADR-META-002_autonomy-by-design.md` Extension 2026-06-14 §E13 (Model-Agnostic Frugality).
- `ADR-META-002_autonomy-by-design.md` Extension 2026-06-15 §E13 (renforcement).
- `ADR-META-001_anti-paresse-verify-before-assert.md` (sister, D1-D8 canoniques).
- `ADR-LLM-001_fable-5-discontinuation-decision.md` (runtime principal actuel).
- `ADR-REG-001_eu-mistral-self-hosting-fallback.md` (fallback UE, sister).
- `~/.claude/skills/tilly-fable-rhythm/SKILL.md` (instance model-agnostic concrète).
- `Tilly guide 05` (PARA Geordi canon, Fable = pattern model-agnostic).
