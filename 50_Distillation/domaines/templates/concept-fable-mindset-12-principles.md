---
type: Concept
title: Fable Mindset — 12 principes de discipline opérationnelle, mesurés
description: Manifeste de 12 principes comportementaux (think before act, verify, narrate, decay) distilllé de l'analyse de 4665 sessions Fable 5 publiques — daté sur les références Claude Code (effortLevel, alwaysThinkingEnabled), canon sur les principes.
tags: [templates, fable-mindset, discipline, verification, narration, decay, datation]
generated: { by: minimax-m3, at: 2026-08-19T19:50:00Z }
verified:
  - { by: process:lecture_fable_mindset_integral, at: 2026-08-19T19:50:00Z }
sources:
  - id: fable-mindset-public
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/Fable_Mindset_public.md"
    title: "The Fable Mindset — manifeste de 12 principes"
    last_modified: 2026-05
  - id: fable-prompts
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/PROMPTS.md"
    title: "Fable Mindset — 6 prompts copy-paste (de-bloat, analyse, playbook, wire, crank, hook)"
    last_modified: 2026-05
  - id: fable-dataset
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/DATASET.md"
    title: "Fable 5 dataset Hugging Face (4 665 traces, 69.8 MB)"
    last_modified: 2026-05
  - id: fable-scripts-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/extract-mindset/extract-mindset/scripts"
    title: "5 scripts Python : analyze_discipline, debloat_jsonl, analyze_vs_fable_dataset, extract_model_corpus"
    last_modified: 2026-05
  - id: fable-extract-mindset-skill
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/extract-mindset/extract-mindset/SKILL.md"
    title: "Fable Mindset — sous-skill extract-mindset (claude skills)"
    last_modified: 2026-05
okf_version: "0.2"
---

# Fable Mindset — 12 principes de discipline opérationnelle

## Périmètre

3 fichiers `.md` racine (Fable_Mindset_public.md, PROMPTS.md, DATASET.md) + 1 PDF (`fable-5-extreme-use-cases-guide.pdf`) + sous-dossier `extract-mindset/` (1 SKILL.md + 3 références + 5 scripts Python).

**Verdict global :** **`synthese-datee`** — daté sur les références Claude Code, canon sur les 12 principes et leur mesure.

## Les 12 principes (synthèse)

| # | Principe | Mesure Fable vs Baseline |
|---|---|---|
| 1 | Reason before the first action | 92 % vs 40 % |
| 2 | Re-evaluate after every batch of results | 87 % vs 39 % |
| 3 | Ground in reality first (git, grep, read) | non-mesuré mais « toujours » |
| 4 | Read the exact region before editing it | 88 % vs 88 % (parité) |
| 5 | Batch and parallelize independent work | mesuré en cadence d'actions |
| 6 | Discover capabilities before committing | mesuré en exploration |
| 7 | Run the real check after editing | 65 % vs 75 % (Fable est le **plus faible** ici) |
| 8 | Diagnose, then fix. Never retry blind | 3,2 % tool error rate vs 1,8 % (les deux sont bas) |
| 9 | Decompose, plan-gate, and track | non-mesuré |
| 10 | Narrate decisions and transitions | « reasons on nearly every turn » 86 % vs 39 % |
| 11 | Prefer absolute paths over `cd` | non-mesuré |
| 12 | Report outcomes faithfully | implicite dans toutes les autres mesures |

Source : `Fable_Mindset_public.md` appendix table.

## Daté sur

- La mention d'`Opus 4.8` comme baseline de comparaison — référence à un modèle qui n'est plus le modèle de référence courant.
- Les variables d'environnement : `effortLevel`, `alwaysThinkingEnabled`, `MAX_THINKING_TOKENS` — settings Claude Code spécifiques, susceptibles d'évoluer.
- La note explicite : « `MAX_THINKING_TOKENS` env var does nothing on adaptive thinking models, so do not rely on it » — daté sur le mode adaptive thinking.

## Canon sur

- La **boucle de décision compressée** : `GROUND → REASON → ACT → OBSERVE → RE-EVALUATE → VERIFY → NARRATE`.
- L'**insight clé** : « Skipping OBSERVE is how good plans produce wrong outcomes. »
- La règle 7 (run the real check) explicitée comme le **maillon le plus faible** de Fable — qui impose donc une **garantie mécanique** (PostToolUse hook), pas une intention. Citation : « Aim to exceed the source material here. The model this mindset is drawn from verifies inconsistently. You should verify every time. »
- L'appariement mindset (texte) + effort (setting) : « effort plus the reasoning rules in this file close most of the gap. The rest is intrinsic to the source model. »

## Les 6 prompts (utilisables tels quels)

Le fichier `PROMPTS.md` contient 6 prompts copy-paste, **réellement applicables** à A'Space V3 :

1. **Build the de-bloater** : crée un script Python qui strip les `tool_result` payloads d'une session JSONL.
2. **Filter to only Fable and analyze** : profil comportemental (compte messages, tool calls, cadence).
3. **Compare to the Opus 4.8 rhythm** : delta entre deux modèles, mesuré sur les mêmes critères.
4. **Point your model at the playbook** : injecter dans `CLAUDE.md` du projet.
5. **Crank the reasoning up** : `/effort max` (setting Claude Code).
6. **Wire the one guarantee (the test hook)** : ajouter un `PostToolUse` hook qui lance les tests après chaque Edit/Write.

Le prompt 6 est **directement applicable** à A'Space V3 : c'est une garantie mécanique qui résout exactement la faiblesse identifiée.

## Trace dans V3

**Aucune directe.** Pas de référence à « Fable Mindset » dans `ASpace_OS_V3/`. Mais le **principe du PostToolUse hook qui lance les tests** est très probablement applicable à plusieurs projets V3 (cf. `tools/shot.mjs` dans Coach OS qui est déjà un tel hook). À confirmer dans une vague ultérieure.

## Scripts Python disponibles (réellement utiles)

| Script | Rôle |
|---|---|
| `analyze_discipline.py` | profile comportemental d'une session |
| `analyze_discipline_win.py` | variante Windows |
| `analyze_vs_fable_dataset.py` | comparaison à la baseline Fable 5 |
| `debloat_jsonl.py` | strip les tool_result payloads |
| `extract_model_corpus.sh` | extraction bash |

Ces scripts sont **réellement applicables** pour distiller le comportement des agents V3.

## Concepts liés

- [[concept-fable-wargame-kit-8-criteria]] — la suite opérationnelle du Mindset
- [[concept-os-audit-skill-canon]] — un skill canonique V3 qui partage la philosophie « read-only + report »
