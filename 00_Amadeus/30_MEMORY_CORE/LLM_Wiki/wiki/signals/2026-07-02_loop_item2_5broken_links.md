---
source: CC-M3 loop-operator (auto-loop 2026-07-02 item 2)
date: 2026-07-02T14:47:30-04:00
type: Signal
domain: LLM_Wiki hygiene
status: OPEN
loop: meta_memoire_2026-07-02
item: 2 (wiki lint v2)
tags: [#signal #wiki_lint #broken_links #afk_loop]
related:
  - wiki/audits/audit_wiki_lint_2026-07-02.md
---

# Signal OKF — 5 liens brisés détectés wiki lint 2026-07-02

## Fait (D1 receipts)

Wiki lint PowerShell `~/.claude/bin/wiki-lint.ps1` exécuté 2026-07-02 14:47:30.
Sortie : **286 pages scannées, 0 orphelins, 78 sans frontmatter, 5 liens brisés**.

## Les 5 liens brisés — source unique `hand_offs/handoff_agent_os_fabuleux_analysis_2026-06-15.md`

- 2x pointe vers `file:///C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`
- 2x pointe vers `file:///C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_C_capsules/INDEX_capsules.md`
- 1x pointe vers `file:///C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/INDEX_runtime.md`

## Root cause (D6)

Les fichiers `_SPECS/ADR/ADR-META-001_*.md` et `ADR-META-002_*.md` ont été **renommés en `.bak_2026-06-14`** le 2026-06-14 (visible `ls _SPECS/ADR/`). Le handoff `agent_os_fabuleux_analysis_2026-06-15.md` pointe vers les paths **pré-renommage** — lien cassé depuis ~17 jours.

`INDEX_capsules.md` / `INDEX_runtime.md` dans `00_Amadeus/05_OSS_Twin/symphony/L1/` : à vérifier si ces INDEX existent réellement (ls partiel échoué dans cette itération).

## Action proposée (hors-loop, à A0)

3 options au choix d'A0 :
1. **Restore les ADRs** si l'archive `.bak_2026-06-14` est encore d'actualité → ré-éditer le handoff avec les bons chemins.
2. **Supprimer les liens morts** du handoff agent_os (édition manuelle).
3. **Marquer le handoff comme `_TRASH_<date>/`** si l'analyse est obsolète (Doctrine no-hard-delete respectée).

## Wager (ADR-LOOP-003)

- **Métrique** : `wiki_lint.broken_links_count` (cible 0 d'ici W13 — 2026-09-07)
- **Horizon** : 5 cycles de lint (1/mois × 5 mois)
- **Effort estimé** : 5 min par lien × 5 liens = 25 min

## Item 2 done-check global

- 286 pgs scannées — OK
- 0 orphelins — OK (cible done-check)
- 78 sans frontmatter — NOUVEAU : voir signal séparé si escalade
- 5 liens brisés — voir ce signal

## Notes complémentaires

- Le script `wiki_lint.py --fix` mentionné dans le contrat n'existe PAS. Seul `~/.claude/bin/wiki-lint.ps1` existe (PowerShell). À acter dans P4 wiki-lint v2 si A0 veut.
- Le contrat mentionnait `[[wikilinks]]` mais le script PowerShell ne couvre que les liens `file://...md` — pas de scan `[[wikilinks]]` à ce stade. À ajouter dans le lint v2.

## Related

- `wiki/audits/audit_wiki_lint_2026-07-02.md` — rapport complet
- `wiki/audits/audit_wiki_lint_active.md` — pointeur mis à jour
- `~/.claude/bin/wiki-lint.ps1` — script canonique
- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md.bak_2026-06-14` — cible renommée

---
**Status** : OPEN — escalade A0 au réveil.
