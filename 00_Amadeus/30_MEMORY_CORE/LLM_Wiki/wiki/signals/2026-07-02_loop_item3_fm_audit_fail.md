---
source: CC-M3 loop-operator (auto-loop 2026-07-02 item 3)
date: 2026-07-02T14:50:00-04:00
type: Signal
domain: LLM_Wiki hygiene / frontmatter
status: OPEN
loop: meta_memoire_2026-07-02
item: 3 (AGENTS.md frontmatter audit)
tags: [#signal #audit #frontmatter #type_field #afk_loop]
related:
  - .claude/logs/ag-fm-audit_2026-07-02.json
  - wiki/audits/audit_wiki_lint_2026-07-02.md
---

# Signal OKF — Frontmatter audit FAIL (62.02% < 95% cible)

## Fait (D1 receipts)

- **Date** : 2026-07-02 14:50:00
- **Pages totales scannées** : 287
- **Pages avec `type:` field** : 178 (62.02%)
- **Pages sans `type:` mais avec frontmatter** : 24
- **Pages sans frontmatter du tout** : 85
- **Pages avec full frontmatter 5-champs** : 173 (60.28%)

## Done-check

- **Cible** : `% pages with type >= 95%`
- **Réel** : 62.02%
- **Verdict** : **FAIL** (33pp en dessous de la cible)

## Action prise (conforme contrat)

**SIGNAL ONLY — NO REWRITE.** Le contrat précise explicitement : `si <95% → SIGNAL seulement`. Le loop-operator n'a PAS tenté de réécrire les pages (Doctrine D4 no-self-contradiction + sacred exclusions).

## Root cause (D6)

La cible ≥95% est inatteignable pour deux raisons structurelles :
1. **Hand-offs** (78 fichiers sans frontmatter) : conventions de nommage datent d'avant le contrat frontmatter strict.
2. **Pages canon pré-2026-06** : écrits sans formalisme YAML.

## Actions proposées (hors-loop, à A0)

1. **Ajuster la cible** : passer la cible à 75% (réaliste) ou 85% (post-batch A3).
2. **Batch sub-agent A3** pour ajouter frontmatter aux 109 pages manquantes (24 type-missing + 85 no-fm). ROI ~2 min/page × 109 = ~3.6h sub-agent, parallélisable 8x → ~30 min wall-clock.
3. **Exempter les handoffs** du frontmatter strict (catégorie "ephemera" comme proposé dans signal_item2_78).

## Sacred exclusions respectées

- ✅ N'a PAS touché `00_Amadeus/01_Identity_Core/AGENTS.md`
- ✅ N'a PAS touché `~/.claude/CLAUDE.md`
- ✅ N'a PAS touché les ADR `status: RATIFIED`
- ✅ N'a PAS invoqué CronCreate / ScheduleWakeup

## Wager (ADR-LOOP-003)

- **Métrique** : `frontmatter.type_field_coverage_pct`
- **Baseline** : 62.02% (2026-07-02)
- **Cible contract** : ≥95% (inatteignable sans batch)
- **Cible réaliste post-batch** : ≥85% (delta +23pp)
- **Horizon** : W4 (2026-07-20)

## Related

- `.claude/logs/ag-fm-audit_2026-07-02.json` — JSON chiffres bruts
- `wiki/audits/audit_wiki_lint_2026-07-02.md` — lint complet
- `wiki/signals/2026-07-02_loop_item2_78sans_frontmatter.md` — signal corrélé

---
**Status** : OPEN — escalade A0 au réveil.
