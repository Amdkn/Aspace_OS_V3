---
source: Claude Code (A2) — LLM Wiki lint
date: 2026-06-05
type: audit
domain: LLM_Wiki maintenance
status: FULLY REMEDIATED (90 pages, 0 orphelin, 0 lien casse, 0 sans frontmatter)
tags: [#audit #wiki_lint #orphans #frontmatter #LD01 #hygiene]
---

# 🧹 LLM Wiki Lint — 2026-06-05

> Lint exécuté à la demande A0 (disque stabilisé). Scope : `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/`.

## 1. Vue d'ensemble
- **89 pages** `.md` (hors index/log/schema).
- **Structure** : ✅ **corrigée ce run** — les 8 domaines Business Pulse (`0N_*`) étaient **à plat dans `wiki/`** ;
  déplacés sous **`wiki/LD01/`** (miroir J01 Jerry Prime LD01 Business). Liens `file://` de `index.md` réécrits (19), 0 cassé.

## 2. 🔴 Orphelins (pages non cataloguées dans `index.md`) — **~45**
Beaucoup sont des pages légitimes récentes jamais ajoutées à l'index. Les plus importantes à cataloguer :
- **Cette session** : `hand_offs/D10_path_length_fix_solaris_aaas.md`, `business_os_ceo_dashboard_design.md`,
  `picard_repo_home_alignment.md`, `SESSION_HANDOFF_2026-06-05.md` ; `syntheses/synthesis_session_2026-06-05_*` ;
  `concepts/concept_shadow_l0_l1_l2_reprise.md`, `concept_aspace_governance_dashboard.md`, `concept_l2_fractal_b1b2b3.md` ;
  `comparisons/comparison_l2_roster_divergence.md`.
- **LD01/05_IT** (11 orphelins) : `concept_agent_capsule`, `concept_skill_reflex`, `concept_nano_squads`,
  `concept_ecc_agnostic_agent_library`, `concept_context_overwrite_anti_pattern`, `entity_adr_infra_001`, `entity_adr_notion_001`…
- **LD01/04_Ops** : `entity_adr_heart_002`, `entity_adr_symph_001/002`, `entity_autoresearch`.
- **sources/** : sessions SSH-config (×6), `gemini_sessions_2026_05`, `session-ccc-claude-code-avec-minimax`…
- **agent_capsules/_TEMPLATE/** : Context/Soul/Tools (template — orphelin attendu, OK).

## 3. 🟠 Pages sans frontmatter YAML — **17**
Surtout `sources/session-ssh-config-*` (×6), `sources/gemini_sessions_2026_05`, `sources/session-*-2026-05-20` (×2),
`hand_offs/handoff_20260522_*` (×2), `handoff_20260526_*` (×2), `audits/business_domain_youtube_*` (×2),
`sources/skill-notebooklm_research-archived`, `sources/source_codex_session_*`.
→ Convention CLAUDE.md : tout `.md` de MEMORY_CORE requiert `source/date/type/domain/tags`.

## 4. Remédiation
**Fait ce run** :
- ✅ Anomalie structurelle résolue : 8 domaines → `LD01/` + liens réécrits.

**Proposé (non exécuté — décision A0, gros catalogage)** :
1. **Re-cataloguer `index.md`** : ajouter les ~45 orphelins (priorité : pages de cette session + LD01/05_IT/04_Ops).
   Idéalement regrouper l'index par section LD01/<domaine> + types (concepts/entities/hand_offs/sources/syntheses).
2. **Frontmatter** : ajouter l'en-tête YAML aux 17 pages (les sessions SSH peuvent recevoir un frontmatter minimal type=source).
3. **Index par namespace** : maintenant que les domaines vivent sous `LD01/`, l'index gagnerait une section "LD01 — Business" listant les 8 sous-dossiers.

## 5. Verdict
Wiki **sain structurellement** après le move ; la dette est du **catalogage** (orphelins) + **frontmatter**, pas de la corruption.
Aucun lien cassé. Aucune page en double détectée. Recommandation : un run de re-catalogage `index.md` quand A0 le veut
(je peux le faire en une passe).

*Lint 2026-06-05 — structure corrigée, dette de catalogage documentée.*
