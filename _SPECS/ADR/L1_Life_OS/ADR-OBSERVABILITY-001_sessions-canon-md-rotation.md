---
id: ADR-OBSERVABILITY-001
title: Sessions Canon + JSONL Rotation — Observability Doctrine for A'Space Traces
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L1 Life_OS / Observability / Sessions Lifecycle / Cold Storage
tags: [#ADR #observability #sessions #jsonl #rotation #cold-storage #trash-pattern]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-INFRA-004, "Doctrine no-hard-delete"]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Doctrine no-hard-delete (wiki/log.md)"]
provenance: |
  Née 2026-06-15 de la doctrine "Current Session" (alias `current`, hook SessionStart) opérationnelle
  depuis 2026-06-06, et de l'archive 30 sessions (115 MB) déplacée vers
  `~/.claude/session-data/_TRASH/2026-06-06_cleanup/` + canonique `wiki/hand_offs/sessions_archive/`.
  Pattern à formaliser : 1 session active, N archivées, JSONL mining possible, no-hard-delete respecté.
sign_off_a0: "A0 Amadeus — Go ADR-OBSERVABILITY-001 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-OBSERVABILITY-001 — Sessions Canon + JSONL Rotation

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **Doctrine "Current Session"** (active depuis 2026-06-06) :
   - 1 seule session active à la fois (alias `current` dans `~/.claude/session-aliases.json`).
   - Hook `SessionStart` exécute `~/.claude/bin/session-start-current.ps1` qui résout l'alias.
   - Reprise manuelle : `/sessions load current`.
   - Cleanup : 30 sessions (115 MB) → `~/.claude/session-data/_TRASH/2026-06-06_cleanup/`.
   - Archive canonique : `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/sessions_archive/`
     (31 fiches + INDEX + LOG) + `30_MEMORY_CORE/Memory_Core/sessions_canon.md` (synthèse A0).
2. **Doctrine no-hard-delete** (wiki/log.md, 2026-03-05 naissance) : pas de `rm -rf` destructif sur
   artefacts de travail — toujours `_TRASH/` (soft delete avec indexation pour retrieval éventuel).
3. **JSONL mining** (cf. ADR-INFRA-004) a besoin de traces pour extract A'Space-Mindset. Les sessions
   archivées en `_TRASH/` + canonique sont le **dataset brut**.
4. **Risque storage** : traces JSONL s'accumulent (~1 MB/session × 30 sessions/mois = 30 MB/mois).
   Sans politique de rotation, le disque `~/.claude/session-data/` grossit indéfiniment.

## Decision

**D1 — Cycle de vie session** :
1. **Active** : 1 seule session `current` à la fois (alias résolu par hook SessionStart).
2. **Closed** : A0 ferme manuellement (`/sessions close current`) ou après 90 jours d'inactivité.
3. **Archived** : déplacée vers `wiki/hand_offs/sessions_archive/<YYYY-MM-DD>_<topic>.md` (synthèse
   humaine) + `sessions_canon.md` (entrée canonique). JSONL brut conservé 90 jours en local.
4. **Cold** : après 90 jours, JSONL déplacé vers `~/.claude/session-data/_TRASH/<cleanup_date>/`.
5. **Trash** : jamais `rm` destructif. Index `_TRASH/INDEX.md` liste tous les fichiers cold pour
   retrieval éventuel (D6 root cause — on garde les preuves).

**D2 — Rotation automatique 1×/trimestre** (intégré au bilan 12WY) : A0 lance
`~/.claude/bin/sessions-rotate.ps1` qui :
- Identifie sessions fermées depuis > 90 jours.
- Déplace JSONL vers `_TRASH/<YYYY-MM-DD>_cleanup/`.
- Met à jour `_TRASH/INDEX.md` (append-only).
- Log dans `wiki/log.md` (1 ligne par rotation : count, MB déplacés, INDEX mis à jour).

**D3 — Synthèse humaine obligatoire avant cold** : toute session fermée de > 7 jours doit avoir
une fiche `wiki/hand_offs/sessions_archive/<date>_<topic>.md` (≥ 30 lignes) qui résume les décisions,
D1 receipts clés, et follow-ups. Pas de cold storage de JSONL "orphelin" sans synthèse.

**D4 — Cold storage sur VPS Dokploy (optionnel S+5)** : si A'Space grossit (> 500 MB sessions
archivées), mirror cold vers VPS Dokploy `/srv/aspace/sessions-cold/` (rsync quotidien, append-only).
But = backup off-site + libérer disque local.

**D5 — Observability metrics** : chaque bilan 12WY inclut un mini-tableau sessions :
- Active count, closed count, archived count, cold count, total MB.
- Top 5 sessions by tool calls (signal d'usage intense).
- D11 métrique Fable agrégée (reads-before-edits %, reason-first %, real-test-after-edit %).

## Consequences

- ✅ Disque `~/.claude/session-data/` borné (~ 100 MB steady state).
- ✅ Cold storage jamais perdu (D6 root cause : on garde les preuves).
- ✅ Synthèse humaine avant cold = knowledge canonique A'Space s'enrichit à chaque rotation.
- ✅ JSONL mining (ADR-INFRA-004) a un **dataset archivé** pour extract A'Space-Mindset.
- ⚠️ Coût humain : A0 doit rédiger les fiches archive (ou déléguer à A2 sub-agent = ADR-A0-trust).

## Implementation Plan (D9.7)

1. **Phase 1 (déjà fait 2026-06-06)** : doctrine "Current Session" + cleanup 30 sessions (115 MB).
2. **Phase 2 (S+1)** : écrire `~/.claude/bin/sessions-rotate.ps1` (≤100 lignes, idempotent, dry-run).
3. **Phase 3 (S+2)** : premier run test (rotation sessions > 90 jours si existent, sinon no-op).
4. **Phase 4 (S+5)** : intégrer rotation au checklist bilan 12WY (auto-trigger si A0 ouvre bilan).

## References

- `~/.claude/session-aliases.json` (alias `current`).
- `~/.claude/bin/session-start-current.ps1` (hook SessionStart).
- `wiki/hand_offs/sessions_archive/` (31 fiches + INDEX + LOG).
- `30_MEMORY_CORE/Memory_Core/sessions_canon.md` (synthèse canonique A0).
- `~/.claude/session-data/_TRASH/2026-06-06_cleanup/` (30 fichiers .jsonl, 115 MB, archive cold).
- `wiki/log.md` (entrée 2026-06-06 cleanup, doctrine no-hard-delete).
- `ADR-INFRA-004_jsonl-mining-extract-mindset-pipeline.md` (consommateur du cold storage).
