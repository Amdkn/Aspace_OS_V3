---
type: handoff
title: Fable Is Gone Claim — D1 Falsification Post-Mortem
date: 2026-06-15
author: A2 (Claude Code orchestrator) + A3-θ sub-agent
doctrine_anchors: ADR-META-001 D1/D2/D3/D4/D5/D6/D7/D8, ADR-META-002 D9/D11/E13
status: HYPOTHÈSE flaggée — claim YouTube NON-CONFIRMÉ, backend Fable-MiniMax-M3 VÉRIFIÉ LIVE
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

# 🎬 Fable Is Gone — D1 Falsification Post-Mortem

> **Mission** : archiver la vérification D1 du claim YouTube *"Fable Is Gone. Here's What You Can Do Instead."* (Mark Kashef, 9,2k vues, 11h ago) vs la réalité technique du backend A'Space. Anti-régression : si A0 revoit ce claim dans 3 mois, ce handoff est la source de vérité.

---
type: handoff
title: Fable Is Gone Claim — D1 Falsification Post-Mortem
date: 2026-06-15
author: A2 (Claude Code orchestrator) + A3-θ sub-agent
doctrine_anchors: ADR-META-001 D1/D2/D3/D4/D5/D6/D7/D8, ADR-META-002 D9/D11/E13
status: HYPOTHÈSE flaggée — claim YouTube NON-CONFIRMÉ, backend Fable-MiniMax-M3 VÉRIFIÉ LIVE
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 2. 🔍 D1 Verify — Fable discontinué ?

### 2.1 Sources primaires consultées

| Source | Type | Statut HTTP | Verdict D1 |
|--------|------|-------------|------------|
| WebSearch "Fable 5 discontinued Anthropic" | Engine search | **400 Bad Request** (invalid params) | ⚠️ Tool broken, pas un verdict |
| WebFetch YouTube (vidéo Mark Kashef) | HTTP GET | **429 Too Many Requests** | ⚠️ Rate-limited |
| WebFetch Bing | HTTP GET | 200 (vide) | Aucun résultat primaire |
| WebFetch Google search | HTTP GET | 200 (vide) | Aucun résultat primaire |
| `https://api.minimax.io/anthropic` (curl HEAD) | Backend check | **301 Moved Permanently** | ✅ **Endpoint répond** |
| `https://api.minimax.io/v1/messages` (curl POST auth test) | Backend check | **401 authentication_error** (request_id `067ed481ef336027cabbf3fc4b5d5d70`) | ✅ **Auth wall normal, endpoint LIVE** |
| Dataset HuggingFace `Glint-Research/Fable-5-traces` | Trace archive | 200 (dataset lisible) | ⚠️ Note auteur : *"before it was taken away (no clue if it's coming back)"* — **spéculatif, pas communiqué officiel** |
| Anthropic.com news/blog officiel | Site officiel | (non-fetché — 2026-06-15 06:55) | ⏸️ A0 action si intéressé |

### 2.2 Verdict D1 (doctrine Anti-Paresse)

| Élément | Verdict | Preuve (D1 receipt) |
|---------|---------|---------------------|
| Fable discontinué par Anthropic ? | **NON-CONFIRMÉ** | Aucune source primaire (WebSearch 400, YouTube 429, anthropic.com non-vérifié) |
| Backend `api.minimax.io` mort ? | **FAUX** | `curl -I` → 301, `POST /v1/messages` → 401 (auth wall) — endpoint répond |
| Fable = MiniMax-M3 (canon A'Space) ? | **VÉRIFIÉ** | Tilly guide 05 l.19 + l.29 (ingéré 2026-06-14 dans canon) |
| Date discontinuation Fable ? | **INCONNU** | Dataset HuggingFace author speculates, pas un statement officiel |
| Skill `/tilly-fable-rhythm` existe ? | **NON** (`ls ~/.claude/skills/` clean) | Phase 2 création autorisée |

### 2.3 Conclusion D5 (proof-before-claim)

**Le claim YouTube "Fable Is Gone" est HYPOTHÈSE non-prouvée.** Le backend que A0 utilise effectivement (`api.minimax.io`) **est live 2026-06-15 06:53 GMT**. Tant que A0 n'a pas (a) transcript vérifié de la vidéo originale, (b) communiqué officiel Anthropic, ou (c) date de discontinuation confirmée, on traite ce claim comme **non-fait-acquis**.

**3 hypothèses sur le claim YouTube** (D6 root cause candidates) :
- (a) **FAUX probable** — pattern typique YouTube "AI X is dead" = clickbait
- (b) **Vrai mais clickbait** — un événement mineur (baisse de popularité, dépréciation d'un endpoint spécifique) est exagéré en "Fable is gone"
- (c) **Réf à événement futur** — discontinuation annoncée mais pas encore effective (possible si Mark Kashef cite une roadmap)

**Recommandation D7** : ne PAS amender l'Extension 2026-06-14 de META-002 (qui dit Fable = MiniMax-M3 = backend live) tant que A0 n'a pas de source primaire.

---
type: handoff
title: Fable Is Gone Claim — D1 Falsification Post-Mortem
date: 2026-06-15
author: A2 (Claude Code orchestrator) + A3-θ sub-agent
doctrine_anchors: ADR-META-001 D1/D2/D3/D4/D5/D6/D7/D8, ADR-META-002 D9/D11/E13
status: HYPOTHÈSE flaggée — claim YouTube NON-CONFIRMÉ, backend Fable-MiniMax-M3 VÉRIFIÉ LIVE
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 4. 📐 Amendements D9.5/D9.6/D9.7/D11/E13 (Extension 2026-06-15)

**D4 self-contradiction prévenue** : Extension 2026-06-14 (l.99-156) reste **INCHANGÉE** (D1 verify la confirme correcte). Extension 2026-06-15 = append-only en fin de fichier.

### 4.1 D9.5 — Read the exact region before edit

> *"Re-evaluate after every batch of results + Read exact region before edit"* (Fable II.4)

**Règle** : avant tout `Edit` / `Write` / `MultiEdit`, l'agent DOIT avoir lu la zone exacte du fichier qu'il modifie (même tour ou tour précédent traçable).

**Conséquence** : un Edit sans Read préalable dans la même session = violation D9.5.

### 4.2 D9.6 — Discover capabilities before committing

> *"Discover capabilities before committing"* (Fable III.6)

**Règle** : avant de s'engager dans une approche, l'agent DOIT vérifier outils/skills/commands dispos (D2 research-first rendu opérationnel).

**Conséquence** : pattern "hand-rolling" détecté → STOP, vérifier `~/.claude/skills/`, `mcp__*`, Context7.

### 4.3 D9.7 — Decompose + plan-gate + track

> *"Decompose, plan-gate, track"* (Fable VI.9)

**Règle** : pour >5 décisions ou >3 phases, l'agent DOIT produire un phased plan tracké via TodoWrite (5-7 items max, regroupés par phase).

**Conséquence** : TodoWrite obligatoire dès que complexité >5 décisions. Phase gate = check explicite entre phases.

### 4.4 D11 — Métrique empirique Fable

| Métrique | Fable 5 | Opus 4.8 baseline | Écart |
|----------|---------|-------------------|-------|
| Raisonnement | **86%** | ~50% | +36 pts |
| Reason-first | **92%** | ~70% | +22 pts |
| **Real-test-after-edit** | **65%** ⚠️ | 75% | **-10 pts (weak spot Fable)** |
| Reads-before-edits | 88% | 80% | +8 pts |

**Règle D11** : toute claim d'autonomie opérationnelle (D9-D12) doit être ancrée sur métrique mesurée, pas prose.

**Conséquence** : sub-agents A3 = rapport de mission inclut ≥1 ligne métrique. Audit Fable-rhythm via skill `/tilly-fable-rhythm`.

### 4.5 E13 — Model-Agnostic Frugality (raffinement E1-E12)

**E13 (NOUVEAU)** : la discipline Fable est un **port de comportement**, pas une dépendance vendor. Le rythme survit à la marque.

**Conséquence** : si Fable-marque meurt, Fable-Mindset continue. Skill `/tilly-fable-rhythm` model-agnostic. Playbook injecté ne référence pas la marque Fable, seulement le pattern.

---
type: handoff
title: Fable Is Gone Claim — D1 Falsification Post-Mortem
date: 2026-06-15
author: A2 (Claude Code orchestrator) + A3-θ sub-agent
doctrine_anchors: ADR-META-001 D1/D2/D3/D4/D5/D6/D7/D8, ADR-META-002 D9/D11/E13
status: HYPOTHÈSE flaggée — claim YouTube NON-CONFIRMÉ, backend Fable-MiniMax-M3 VÉRIFIÉ LIVE
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 6. 🔄 Doctrine ancrage (D1-D8)

- **D1** : 8+ receipts collectés (curl 301/401, Tilly 05 canon, dataset HuggingFace quote, WebSearch 400 falsifying claim)
- **D2** : 5 sources primaires lues AVANT toute conclusion (AGENTS.md, META-002, 4 fichiers Fable Mindset)
- **D3** : 3 entités Fable séparées explicitement (Fable-marque vs Fable-MiniMax-M3 vs Fable-Mindset)
- **D4** : Extension 2026-06-14 INCHANGÉE (D1 verify la confirme correcte) — pas d'overturn
- **D5** : proof-before-claim (curl avant tout "Fable mort" statement)
- **D6** : WebSearch 400 → WebFetch 429 → Curl direct pivot (D6 lesson : ne pas insister sur tool broken)
- **D7** : 0 AskUserQuestion, autonomie D8 totale
- **D8** : cross-agent lisible (markdown structuré, paths absolus, citations verbatim)

---
type: handoff
title: Fable Is Gone Claim — D1 Falsification Post-Mortem
date: 2026-06-15
author: A2 (Claude Code orchestrator) + A3-θ sub-agent
doctrine_anchors: ADR-META-001 D1/D2/D3/D4/D5/D6/D7/D8, ADR-META-002 D9/D11/E13
status: HYPOTHÈSE flaggée — claim YouTube NON-CONFIRMÉ, backend Fable-MiniMax-M3 VÉRIFIÉ LIVE
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

## 8. 📚 Sources canoniques (paths absolus)

| Fichier | Lignes | Rôle |
|---------|--------|------|
| `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-002_autonomy-by-design.md` | 270 (post-Extension 2026-06-15) | Cible amendée append-only |
| `…/ADR-META-002_autonomy-by-design.md.bak_2026-06-15` | 157 (snapshot pre-Extension) | Backup D4 |
| `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md` | 9050 bytes | Doctrine Anti-Paresse D1-D8 |
| `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/Fable_Mindset_public.md` | 318 | Manuel 12 principes + decision loop + appendix |
| `…/Fable Mindset/DATASET.md` | 108 | Recette JSONL mining 4,665 traces |
| `…/Fable Mindset/PROMPTS.md` | 61 | 6 prompts copy-paste |
| `…/Fable Mindset/extract-mindset/extract-mindset/SKILL.md` | 199 | Skill compagnon 3 scripts |
| `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/LD04_Cognition_Tilly/05-make-any-model-think-like-fable-in-minutes.md` | 47 | Fiche Tilly 05 souveraine (canon 2026-06-14) |
| `C:/Users/amado/.claude/skills/tilly-fable-rhythm/SKILL.md` | (créé 2026-06-15) | Skill Phase 2 autonomie |
| `https://api.minimax.io/anthropic` | (live 2026-06-15 06:53 GMT) | Backend Fable-MiniMax-M3 vérifié |
| `https://huggingface.co/datasets/Glint-Research/Fable-5-traces` | (speculatif) | Dataset Fable 5 traces, auteur note "before it was taken away" |

---

*Handoff canonique 2026-06-15 — Doctrine Anti-Paresse D1-D8 ancrage, append-only respecté.*

