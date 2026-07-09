---
title: Loop Méta-Mémoire overnight — launch contract A0 GO 2026-07-02
date: 2026-07-02
author: A0 jumeau numérique (Fable 5, CC-M3)
layer: L0 — Tech OS / Harness & Loops
scope: P1+P2+P3 wiki-only consolidation (loop canon §10 strict subset)
sister:
  - ~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md (§10 + §10.6 prospective)
  - _SPECS/ADR/L0_Tech_OS/ADR-LOOP-001_canon-loop-verification-first.md
  - _SPECS/ADR/L0_Tech_OS/ADR-LOOP-002_queues-over-loops-hitl-rightward.md
  - _SPECS/ADR/L0_Tech_OS/ADR-LOOP-003_orient-layer-signals-wagers.md
tags: [#loop #afk #consolidation #wikipedia #geordi #memory #a0-go]
---

# Loop Méta-Mémoire — Launch Contract A0 GO 2026-07-02 (overnight)

## A0 décision (verbatim)

> *"GO /LOOP 15 — sans sandbox pour l'instant, à mon réveil on y travaillera dessus. Pour une dizaine d'itérations sur la consolidation des mémoires et index."*

## Contexte (anti-amnesia)

- A0 dort quelques heures, pas de validation possible pendant l'exécution.
- Sandbox **OFF** = override explicite ADR-LOOP-002 loi 3. Tracé ici pour D7 cost-of-escalation. A0 reste le HITL final à son réveil.
- Scope **strict** P1+P2+P3 (wiki bundle, réversible `_TRASH`). P4 (CLAUDE.md/AGENTS.md) et P6-E2/E3/E4 sont **hors-loop** (plan §10.4).
- 3 ADRs PROPOSED encadrent l'exécution (001/002/003), boucle orient-stratégie M3 corrigée par D1-D8.

## Scope AFK-safe (6 items piochables)

| # | Item | Pourquoi safe | Done-check chiffré | Tools |
|---|---|---|---|---|
| 1 | Régénération `wiki/index.md` (script canon) | Idempotent, dry-run diff | script sort code 0 + diff `git status` | `python .claude/bin/gen_wiki_index.py` |
| 2 | Wiki lint v2 (orphelins + dangling `[[wikilinks]]`) | read-only / append | 0 orphans / 0 unresolved wikilinks | `python skills/graphify-viewer/scripts/wiki_lint.py --fix` |
| 3 | AGENTS.md frontmatter audit | read-only (rapport uniquement, NO rewrite) | `% pages with `type` ≥ 95%` ; si <95% → SIGNAL seulement | Read + Grep, sortie `.claude/logs/ag-fm-audit_2026-07-02.json` |
| 4 | A3 roster revalidation (35/35 vs canon) | read-only + patch `app-*/graph.json` | `match_count == 35` | `python skills/graphify-viewer/scripts/verify_a3_roster.py` |
| 5 | MEMORY.md compaction (≤ 17.1 KB) | append-only + fusion entrées | file size ≤ 17 100 bytes | Read + Edit append-only, sortie `_TRASH_2026-07-02_*/MEMORY_pre.md` |
| 6 | Junction health check (49 junctions .claude/memory/) | read-only | 0 broken readlinks | `ls -la` 49 junctions + `readlink` |

## Scope INTERDIT (STOP immédiat §10.4)

- ❌ Edit `~/.claude/CLAUDE.md` (canon P4)
- ❌ Edit `00_Amadeus/01_Identity_Core/AGENTS.md` (canon)
- ❌ Edit un ADR `status: RATIFIED` (gate hard-stop)
- ❌ `CronCreate` / `ScheduleWakeup` (crons = HITL one-by-one, plan §10.4)
- ❌ Hard-delete (toute annulation = `_TRASH_<date>/`)

## Stop-conditions (ADR-001 + plan §10.4)

1. **2 fails consécutifs sur un même item** → STOP, write handoff blocked.
2. **Touche tente (et détectée) un canon interdit** → STOP immédiat, write `wiki/hand_offs/meta_mem_loop_blocked_<date>.md`.
3. **Cap itérations / budget** : 10 itérations × 15 min = 150 min ≈ 2,5 h. Hard-stop à 2 h sweet-spot ADR-001 (sortie propre, item non terminé).
4. **Per-iteration log** : `wiki/log.md` +1 ligne par item completed (`[YYYY-MM-DDTHH:MM-04:00] [auto-loop] item N complete | done-check=...`).

## Format TRACK enrichi (ADR-003 loi 2 — compounding)

Chaque friction/opportunité capturée → fichier `type: Signal` (OKF frontmatter `type: Signal`) déposé dans `wiki/signals/2026-07-02_loop_<item>_<ts>.md`. Pas juste log-line — c'est le mécanisme du compounding inter-loops.

## Wagers (ADR-003 loi 4)

Chaque item du scope porte un **pari d'impact** (métrique + delta attendu + horizon). Chapel (A3 SNW) ferme les verdicts en W13 sur le scorecard 12WY. Item 6 (junction health) = pari test pour la métrique 5 candidate.

## Launch prompt prêt-à-coller (CC terminal)

```text
/loop 15m "scope=P1+P2+P3 only, AFK, 10 iterations max, sweet_spot=2h, sandbox=OFF A0_GO logged_in_handoff,
excluded=CLAUDE.md|AGENTS.md|RATIFIED_ADR|CronCreate|hard-delete,
verify=item-level numeric done-check,
stop_on=fail2x|canon_rewrite_attempted|RATIFIED_edit|2h_reached,
log=1line/wikilogs/log.md per item complete,
signal=write type:Signal OKF artifact per friction to wiki/signals/2026-07-02_*,
wagers=item_has_metric+delta+horizon, chapel_verdict_W13,
hand_off=wiki/hand_offs/meta_mem_loop_<DATE>.md on STOP or COMPLETE,
contract_ref=wiki/hand_offs/loop_meta_memoire_2026-07-02.md,
plan_ref=~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md §10+10.6,
adrs=ADR-LOOP-001 (verify) + ADR-LOOP-002 (queues) + ADR-LOOP-003 (orient/signals/wagers)"
```

## À A0 au réveil

1. `Read wiki/hand_offs/meta_mem_loop_2026-07-02.md` (succès OU blocked)
2. Si success : 6 done-checks chiffrés dans le handoff → prêt pour verdict A0 avant P4/canon edits.
3. Si blocked : la garde a mordu (canon touche / fail 2x / 2h) → A0 décide repair.
4. Si nouveau SIGNAL : lire `wiki/signals/2026-07-02_*.md` pour décisions de compound-loop.

## D1 receipts (initiaux)

- A0 GO reçu : `loop_meta_memoire_2026-07-02.md` écrit (ce fichier).
- Plan §10 + §10.6 (prospective) lus et référencés.
- 3 ADR PROPOSED lus et référencés (frontmatter `status: PROPOSED`).
- Sandbox override tracé : D7 cost-of-escalation factuel, A0 GO explicite = HITL valide.
- Stop-conditions : 4 niveaux (fail 2x, canon rewrite, 2h cap, per-iter log).

## Related

- `~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` — plan source §10
- `_SPECS/ADR/L0_Tech_OS/ADR-LOOP-001_*.md` — verify-first
- `_SPECS/ADR/L0_Tech_OS/ADR-LOOP-002_*.md` — queues over loops
- `_SPECS/ADR/L0_Tech_OS/ADR-LOOP-003_*.md` — orient/signals/wagers
- `wiki/log.md` — append-only history
- `wiki/signals/` — dossier signals (à créer au 1er signal)

---

**Status** : ACTIVE (loop overnight, A0 sleeps).
**Next milestone** : handoff complete à `wiki/hand_offs/meta_mem_loop_2026-07-02.md` (auto-généré par loop-operator ou CC runtime).
**Posture** : C strict (A0 HITL = ce GO; rien d'autre sans ratification).
