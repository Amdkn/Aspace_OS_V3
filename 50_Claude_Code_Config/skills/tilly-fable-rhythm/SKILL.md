---
name: tilly-fable-rhythm
description: Auditer la cognition d'un agent (Tilly / LD04_Cognition) contre le rythme Fable (reason-first, reads-before-edits, real-test-after-edit, plan-gate). À utiliser quand l'utilisateur mentionne Tilly, cognition, rythme Fable, audit comportemental d'agent, ou veut comparer deux modèles LLM sur leur discipline opérationnelle. Triggers : "tilly fable", "rythme fable", "audit cognition", "extract mindset", "jsonl mining", "playbook injection", "Fable vs Opus". Sortie : tableau behavioral delta + recommandations playbook A'Space.
domain: LD04_Cognition_Tilly
kernel: Kernel_OS (Doctrine)
source: Fable Mindset public manual + Tilly guide 05 canonique 2026-06-14
created: 2026-06-15
doctrine_anchors: ADR-META-001 D1/D2/D5/D6, ADR-META-002 D9-D12, Fable Mindset 12 principes
---

# 🎼 tilly-fable-rhythm

> **Mission** : auditer la **cognition** d'un agent (Tilly / LD04_Cognition) contre le **rythme Fable** (la discipline opérationnelle décrite dans le manuel `Fable_Mindset_public.md`), et produire un **playbook injectable** dans n'importe quel LLM pour qu'il adopte ce rythme.

**Pourquoi ce skill existe** (D3 nuance — Fable = 3 entités distinctes) :
- **Fable-marque** = "Fable 5" (Anthropic commercial, possiblement fictional)
- **Fable-MiniMax-M3** = backend souverain A'Space via `api.minimax.io` (live 2026-06-15)
- **Fable-Mindset** = pattern JSONL mining + playbook injection (template A'Space)

Ce skill opère sur **Fable-Mindset** (le pattern), pas sur la marque. La méthode survit au vendor.

---

## 🧠 Concepts clés

| # | Principe Fable | Source | Effet sur Tilly |
|---|----------------|--------|-----------------|
| 1 | **Reason before first action** | `Fable_Mindset_public.md` l.40-50 | Tilly énonce goal + hyp + plan avant le 1er tool call |
| 2 | **Re-evaluate after every batch** | l.52-66 | Boucle observe→decide→observe entre chaque cluster de tool calls |
| 3 | **Ground in reality first** (git status, grep, read) | l.74-84 | Tilly ouvre un fichier avant de l'éditer (D6 root cause concret) |
| 4 | **Read exact region before edit** | l.86-93 | Tilly ne patche jamais à l'aveugle — elle Lit la zone exacte qu'elle modifie |
| 5 | **Batch and parallelize independent work** | l.100-110 | Tilly regroupe les décisions récap fin de tour (D9.3 META-002) |
| 6 | **Discover capabilities before committing** | l.112-119 | Tilly vérifie outils/skills/commands dispos avant de hand-roller |
| 7 | **Run the real check after editing** (NOT ls/echo) | l.126-141 | Tilly lance le test réel, pas un proxy narratif (D5 META-001) |
| 8 | **Diagnose, then fix (never retry blind)** | l.154-160 | Tilly creuse la root cause avant retry (D6 META-001) |
| 9 | **Decompose + plan-gate + track** | l.168-176 | Tilly produit un phased plan + TodoWrite pour >5 décisions |
| 10 | **Narrate decisions and transitions** | l.180-185 | Tilly récap fin de tour (D9.3 — pas plus de 5 items) |
| 11 | **Prefer absolute paths over cd** | l.193-197 | Tilly utilise des chemins absolus (style hygiene, pas autonomie) |
| 12 | **Report outcomes faithfully** | l.200-204 | Tilly dit "done" seulement après preuve observée (D5) |

**Decision loop canonique** : `GROUND → REASON → ACT → OBSERVE → RE-EVALUATE → VERIFY → NARRATE`

---

## 🛠️ Outillage stratégique

| Outil | Rôle | Source |
|-------|------|--------|
| `Fable_Mindset_public.md` (318 lns) | Manuel d'élicitation cognitive | `ASpace_OS_V2/20_Life_OS/.../02_Templates/Fable Mindset/` |
| `DATASET.md` (108 lns) | Recette mining JSONL → profil | Idem (4,665 traces Fable 5 sur HuggingFace) |
| `PROMPTS.md` (61 lns) | Prompts copy-paste (de-bloat, filter, compare, inject, /effort, test hook) | Idem |
| `extract-mindset/SKILL.md` (199 lns) | Skill compagnon (3 scripts + template Mindset.md) | Idem |
| `05-make-any-model-think-like-fable-in-minutes.md` (Tilly guide 05) | Fiche souveraine A'Space (canonique 2026-06-14) | `ASpace_OS_V2/.../LD04_Cognition_Tilly/` |

**Calibration empirique** (DATASET.md appendix) :
- Fable 5 : 86% reasoning, 92% reason-first, **65% real-test-after-edit** (weak spot)
- Opus 4.8 baseline : 75% real-test-after-edit
- → Le playbook doit **renforcer le real-test**, pas juste copier le reste

---

## 🪐 Perspective A'Space (Domaine LD04_Cognition_Tilly)

L'audit Fable-rhythm transforme Tilly (LD04_Cognition) d'un agent "qui fait ce qu'on lui dit" en un agent "qui prouve ce qu'il a fait". La boucle `GROUND → REASON → ACT → OBSERVE → RE-EVALUATE → VERIFY → NARRATE` est l'incarnation opérationnelle de D9 (Self-Choice) — une disposition, pas une checklist rigide.

**Insight clé** (D3 nuance) : la valeur n'est pas dans le vendor Fable, elle est dans **le pattern JSONL mining** (mesure concrète du comportement) + **playbook injection** (calque les bonnes habitudes sur n'importe quel LLM). C'est pourquoi ce skill est **model-agnostic** : il marche avec Fable-MiniMax-M3 (canonique), Opus 4.8, Sonnet 4.6, ou tout autre agent respectant l'API tool-use.

**Souveraineté** : la discipline Fable est un **port de comportement** (comme un port série), pas une dépendance vendor. Si Fable-marque meurt, le rythme survit.

---

## 🕹️ Protocole d'exécution D.E.A.L

| Phase | Action concrète | Output |
|-------|-----------------|--------|
| **Définir** | Identifier la session cible : `~/.claude/projects/<projet>/<session>.jsonl`. Choisir 1 session safe (pas health). Définir le scope d'audit : `tours 1..N` ou `tools_reads=1, edits=1, tests=1`. | `audit_scope.yaml` |
| **Éliminer** | Lancer `debloat_jsonl.py` (PROMPT 1 du template) → strip tool result payloads + attachment blobs. Réduire 10-100×. | `demo_session.slim.jsonl` (léger) |
| **Automatiser** | **Mission 1** : Filter `message.model == "claude-fable-5"` (PROMPT 2) → corpus Fable. Compter tool calls, order, reads-before-edits, tests-after-edits. Sortie = `fable_metrics.json`.<br>**Mission 2** : Même chose pour `claude-opus-4-8` (PROMPT 3) → `opus_metrics.json`.<br>**Mission 3** : Comparer les 2 → `delta_table.md` (Fable vs Opus, ratios, weak spots).<br>**Mission 4** : Écrire `playbook.md` injectable (PROMPT 3 suite) — inclut le weak spot real-test 65% comme fix prioritaire, pas copie aveugle. | 4 fichiers métriques + 1 playbook |
| **Libérer** | Injecter le playbook dans `~/.claude/CLAUDE.md` (PROMPT 4) ou dans une skill dédiée. Activer `/effort max` (PROMPT 5) + PostToolUse test hook (PROMPT 6). | Tilly adopte le rythme |

---

## 📋 Commandes de référence (depuis PROMPTS.md, adaptées A'Space)

```bash
# 1. Debloat une session cible
python ~/.claude/skills/tilly-fable-rhythm/scripts/debloat_jsonl.py \
  ~/.claude/projects/<projet>/<session>.jsonl \
  > demo_session.slim.jsonl

# 2. Filter Fable et métriques
python ~/.claude/skills/tilly-fable-rhythm/scripts/filter_fable.py \
  --model claude-fable-5 \
  --output fable_metrics.json

# 3. Compare Opus
python ~/.claude/skills/tilly-fable-rhythm/scripts/compare_models.py \
  --baseline claude-fable-5 \
  --target claude-opus-4-8 \
  --output delta_table.md

# 4. Génère le playbook
python ~/.claude/skills/tilly-fable-rhythm/scripts/build_playbook.py \
  --delta delta_table.md \
  --weak-spot real-test-after-edit \
  --output playbook.md
```

---

## 🎯 Triggers d'invocation

Ce skill s'invoque quand l'utilisateur dit :
- "audite Tilly contre le rythme Fable"
- "extract le mindset de cette session"
- "compare Fable vs Opus sur le behavioral delta"
- "injecte le playbook Fable dans CLAUDE.md"
- "calcule les métriques Fable de mes sessions"
- "vérifie que Tilly fait des reads-before-edits et tests-after-edits"

**Mots-clés A'Space** : `LD04_Cognition_Tilly`, `Fable-Mindset`, `JSONL mining`, `playbook injection`, `extract-mindset`, `decision loop GROUND→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY→NARRATE`.

---

## 📚 Sources canoniques (D1 receipts)

| Fichier | Lignes | Hash perceptuel | Lien |
|---------|--------|-----------------|------|
| `Fable_Mindset_public.md` | 318 | Manuel 12 principes + decision loop + appendix métriques | `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/Fable_Mindset_public.md` |
| `DATASET.md` | 108 | Recette JSONL mining 4,665 traces | `…/02_Templates/Fable Mindset/DATASET.md` |
| `PROMPTS.md` | 61 | 6 prompts copy-paste | `…/02_Templates/Fable Mindset/PROMPTS.md` |
| `extract-mindset/SKILL.md` | 199 | Skill compagnon 3 scripts | `…/02_Templates/Fable Mindset/extract-mindset/extract-mindset/SKILL.md` |
| `LD04/05-make-any-model-think-like-fable-in-minutes.md` | 47 | Fiche souveraine A'Space | `…/01_Guides/09_Life_OS/LD04_Cognition_Tilly/05-make-any-model-think-like-fable-in-minutes.md` |

---

## 🔗 Doctrine ancrage

- **ADR-META-001** D1 (verify-before-assert), D2 (research-first), D5 (proof-before-claim), D6 (root-cause concret)
- **ADR-META-002** D9 (Self-Choice Default), D9.1 (pas de AskUserQuestion si recommandation claire), D9.3 (récap 5 items max), D9.4 (coût décision &lt;&lt; coût round-trip), D12 (cohérence META-001)
- **Extension 2026-06-14 META-002** : Fable = MiniMax-M3 backend (vérifié live 2026-06-15 06:53 GMT)
- **Skill Creator Reflex Phase 2** (CLAUDE.md global) : créé en autonomie end-of-session, A0 review post-hoc

---

*Skill créé 2026-06-15 en autonomie Phase 2 — ROI estimé ~30 min/invocation économisées sur audit cognition Tilly.*
