---
source: CC-M3 loop-operator (auto-loop 2026-07-02 item 2)
date: 2026-07-02T14:47:30-04:00
type: Signal
domain: LLM_Wiki hygiene
status: OPEN
loop: meta_memoire_2026-07-02
item: 2 (wiki lint v2)
tags: [#signal #wiki_lint #sans_frontmatter #afk_loop]
related:
  - wiki/audits/audit_wiki_lint_2026-07-02.md
---

# Signal OKF — 78 pages wiki sans frontmatter complet (2026-07-02)

## Fait (D1 receipts)

Wiki lint 2026-07-02 : **286 pages scannées, 78 sans frontmatter complet** (27.3% du wiki).

## Distribution

Les 78 fichiers sans frontmatter complet sont TOUS dans `wiki/hand_offs/` (handoffs A'Space produits avant adoption stricte de la doctrine frontmatter 5-champs source/date/type/domain/tags).

## Action proposée (hors-loop, à A0)

- **Option A** : Batch sub-agent A3 pour ajouter frontmatter template (5 champs) sur les 78 handoffs. ROI ~5 min/handoff × 78 = 6.5h sub-agent (parallélisable 8x → ~50 min).
- **Option B** : Glossaire ADR — considérer les handoffs comme "ephemera" et exempter de la règle frontmatter stricte. Justification : ils ont déjà une date et un contexte narratif.

## Wager (ADR-LOOP-003)

- **Métrique** : `% pages with full frontmatter ≥ 95%` (cible Item 3 done-check)
- **Actuel** : 208/286 = 72.7%
- **Delta attendu** : +27.3pp si Option A exécutée
- **Horizon** : W3 (2026-07-13) — avant Item 3 audit

## Item 3 done-check en attente

L'Item 3 du contrat scope AFK vérifie "% pages with `type` ≥ 95%". La cible ne sera PAS atteinte (type field absent sur 78 handoffs). À escalader A0 — l'audit Item 3 ne va déclencher qu'un SIGNAL (conformément au contrat).

## Related

- `wiki/audits/audit_wiki_lint_2026-07-02.md`
- `wiki/hand_offs/` — 78 fichiers concernés

---
**Status** : OPEN — escalade A0 au réveil.
