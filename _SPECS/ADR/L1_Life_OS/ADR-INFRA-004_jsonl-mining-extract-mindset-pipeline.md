---
id: ADR-INFRA-004
title: JSONL Mining × Extract-Mindset Pipeline — Traces Session → Behavioral Delta
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L1 Life_OS / Observability / Behavioral Analytics / Pipeline
tags: [#ADR #infra #observability #jsonl #mining #extract-mindset #fable-traces #huggingface]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-META-002-D11, ADR-MEMO-000, ADR-OBSERVABILITY-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Fable Mindset extract-mindset SKILL"]
provenance: |
  Née 2026-06-15 du handoff Mission σ (Fable→MiniMax distillation) où A2 a opéré le pipeline complet
  JSONL mining : download 4665 traces Fable 5 (HuggingFace Glint-Research) → extract mindset via
  3 scripts (de-bloat, filter Fable, compare Opus) → inject CLAUDE.md → mesure behavioral delta
  (88% reads-before-edits vs 80% baseline, +22 pts reason-first). Pattern à canoniser en ADR.
sign_off_a0: "A0 Amadeus — Go ADR-INFRA-004 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-INFRA-004 — JSONL Mining × Extract-Mindset Pipeline

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **Mission σ 2026-06-15** a démontré end-to-end le pipeline "extract Fable mindset from traces → inject
   into A'Space" :
   - Source : 4665 traces JSONL Fable 5 (HuggingFace `Glint-Research/Fable-5-traces`).
   - Scripts : `de-bloat.py` (filter reasoning chains), `filter-fable.py` (heuristics Fable),
     `compare-opus.py` (delta vs baseline Opus 4.8).
   - Output : `Fable_Mindset_public.md` (318 lns, 12 principes + decision loop + appendix métriques).
   - Injection : `~/.claude/skills/tilly-fable-rhythm/SKILL.md` créé 2026-06-15.
   - ROI : ~30 min/invocation économisées (audit cognition Tilly vs rythme Fable).
2. **Pattern réutilisable** : A'Space a ses propres traces JSONL (`~/.claude/projects/*/sessions/*.jsonl`,
   ~1 MB/session, déjà archivées). A2 peut miner ces traces pour identifier les patterns comportementaux
   A'Space spécifiques (D1 verify-before-assert, D2 research-first, etc.) et en extraire un
   "A'Space-Mindset" distinct de Fable-Mindset.
3. **D11 métrique empirique** (META-002 Extension 2026-06-15) demande déjà des chiffres pour toute
   claim d'autonomie. Le pipeline JSONL mining est l'**infrastructure** qui rend D11 mesurable.

## Decision

**D1 — Pipeline JSONL mining = first-class infra A'Space** : tout pattern comportemental A'Space
(doctrine, skill, agent profile) peut être :
- **Source** : traces JSONL A'Space OU dataset externe (HuggingFace Fable traces).
- **Extract** : 3 scripts canoniques (de-bloat, filter-aspace, compare-baseline).
- **Output** : SKILL.md (≤500 lignes) OU ADR (canonique) OU dataset metrics.

**D2 — Format dataset A'Space standard** : 3 fichiers par extract :
- `DATASET.md` (provenance, license, count, sample).
- `PROMPTS.md` (prompts copy-paste pour reproduire extraction).
- `SKILL.md` (skill exécutable Claude Code avec `extract-mindset` toolkit).

**D3 — Skill `/extract-mindset` companion de `/tilly-fable-rhythm`** : encapsule les 3 scripts + template
`Mindset.md` + workflow d'injection. ROI ~45 min/extract (vs ~3h manuel).

**D4 — Mesure avant/après obligatoire** : chaque extract produit un mini-tableau behavioral delta
(reads-before-edits %, reason-first %, real-test-after-edit %, latency p50). D11 metric Fable
(META-002 Extension 2026-06-15) sert de baseline.

**D5 — Append-only log extracts** : `wiki/hand_ffs/extracts/INDEX.md` liste tous les extracts faits,
avec date, source, output, ROI mesuré. D4 append-only.

## Consequences

- ✅ Pattern Fable mindset portable = pattern **général** d'extract behavior from traces.
- ✅ Infrastructure D11 (mesure comportementale) désormais outillée.
- ✅ Possibilité de dériver A'Space-Mindset spécifique depuis traces locales (vs appliquer Fable générique).
- ⚠️ Coût storage : traces JSONL A'Space s'accumulent (~1 MB/session × 30 sessions/mois = 30 MB/mois).
  Mitigation : rotation après 90 jours, archive cold sur VPS Dokploy.

## Implementation Plan (D9.7)

1. **Phase 1 (déjà fait 2026-06-15)** : skill `/tilly-fable-rhythm` créé (Mission σ livrable).
2. **Phase 2 (S+2)** : skill `/extract-mindset` generic (3 scripts + template, applicable à tout dataset).
3. **Phase 3 (S+3)** : premier extract A'Space-Mindset depuis traces locales A'Space
   (`~/.claude/projects/c--Users-amado/sessions/*.jsonl`, archive 2026-06-06 cleanup = 115 MB dispo).
4. **Phase 4 (S+5)** : comparer A'Space-Mindset à Fable-Mindset, dériver delta.

## References

- `~/.claude/skills/tilly-fable-rhythm/SKILL.md` (créé 2026-06-15, instance concrète du pattern).
- `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/extract-mindset/extract-mindset/SKILL.md` (skill compagnon, 199 lns, 3 scripts + template).
- `wiki/hand_offs/handoff_fable_to_minimax_distillation_2026-06-15.md` (Mission σ, 233 lns).
- `ADR-META-002_autonomy-by-design.md` Extension 2026-06-15 §D11 (mesure empirique Fable).
- `ADR-MEMO-000_auto-research-karpathy-loop-claude-code_DRAFT.md` (Karpathy loop ancrée).
