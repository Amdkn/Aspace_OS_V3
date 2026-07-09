---
id: ADR-META-006
title: Droid Whispering Doctrine — A0 owns model/agent selection per workstream
status: ACCEPTED
level: L0
level_name: Kernel_OS
date: 2026-06-22
author: A3 sub-agent (handoff youtube_ingest_2026-06-22)
supersedes: null
extends:
  - ADR-META-001_anti-paresse-verify-before-assert.md (D8 cross-agent)
  - ADR-META-002_self-choice-autonomy.md (D9 self-choice)
source: Luke Alvoeiro, Factory — "Multi-Agent Systems That Ship for Days" (AI Engineer channel, 2026-06-22)
---

# ADR-META-006 — Droid Whispering Doctrine

## Contexte

Luke Alvoeiro (Factory, lead core agent harness) introduit la notion de **droid whispering** : la nouvelle skill requise pour orchestrer des missions multi-jours est de savoir mentalement modéliser comment différents LLMs interagissent, où ils échouent, comment ces échecs compoundent sur une run multi-jours, et faire un choix délibéré de quel modèle sits in which seat.

**Constat Factory** : aucun modèle/provider n'est best-at-all-three (planning slow reasoning / implementation fast code fluency / validation precise instruction following). Validation peut même utiliser un **provider différent** pour adversarial bias (pas contaminé par même training data que l'implémenteur).

**Problème A'Space** : ADR-META-001 D8 (cross-agent) mandate que toute action traverse L0/L1/L2 proprement. Mais aucune doctrine ne dit **qui décide quel modèle+agent pairing pour un workstream donné**. Aujourd'hui A2 (Claude Code) choisit par défaut Sonnet 4.6 pour tout — sous-optimal pour validation (où Haiku 4.5 + adversarial prompt peut suffire, 3× coût inférieur) ou pour planning profond (où Opus 4.5 est requis).

## Décision

A0 Amadeus owns model/agent selection per workstream. Pour chaque workstream, A0 spécifie :
1. **Model tier** : Haiku 4.5 (lightweight, 3× cost savings) | Sonnet 4.6 (best coding, default) | Opus 4.5 (deepest reasoning, max context cost).
2. **Agent pairing** : A1 Gatekeeper (Beth/Morty/Rick) | A2 Orchestrator (Curie/Zora/Orville/Computer/Holo Deck/Holo Janeway) | A3 twins (35 canon).
3. **Adversarial option** : si validation, autoriser provider différent pour décorréler training data (extends Factory pattern).

**Workflow** :
- A0 émet l'intention au niveau méta (langage d'intentions, jamais B3 technicien).
- A2 orchestre : traduit l'intention en A1+A2+A3 ship + model tier.
- A3 exécute : ne choisit jamais son propre modèle (escalation à A2 si sous-optimal détecté).

**Règle D8 cross-agent** : tout changement de modèle mid-mission = justification écrite dans handoff + ack A0 via outbox E2 (jamais silencieux).

## Conséquences

**Positives** :
- Coût total mission ↓ (Haiku pour read-only validators, Sonnet pour workers, Opus pour planning).
- Adversarial validation ↑ (provider différent = moins de bias training data).
- Compounding advantage (Luke) : "as models specialize, ability to put right model in right seat becomes compounding advantage."

**Négatives** :
- Charge cognitive A0 ↑ (doit mental-model 3 model tiers × 35 A3 twins × 6 A2).
- Risque d'over-engineering si A0 spec trop granulaire (YAGNI — default Sonnet si pas d'intent clear).
- A2 doit apprendre à traduire A0 intent → model/agent pairing (formation implicite).

## Alternatives considérées

1. **A2 choisit systématiquement** : rejeté — risque de default-Sonnet-pour-tout (coût ↑, validation bias).
2. **Auto-routing par complexité de la tâche** : considéré — faisable techniquement (heuristic token count → Opus), mais Luke note que "right model" est per-role et per-domain, pas per-complexity. Rejeté pour Q3 2026.
3. **A3 choisit son modèle** : rejeté — viole ADR-META-001 D8 (cross-agent mandate), et A3 twins sont des outils, pas décideurs.

## Références

- **Source canon** : `wiki/hand_offs/youtube_ingest_2026-06-22/youtube_ingestion_handoff_2026-06-22.md` §4
- **Video** : https://youtu.be/ow1we5PzK-o?si=gjZCWKaytC21sRDo
- **ADR-META-001** : `_SPECS/ADR/L0_Kernel_OS/ADR-META-001_anti-paresse-verify-before-assert.md`
- **ADR-META-002** : `_SPECS/ADR/L0_Kernel_OS/ADR-META-002_self-choice-autonomy.md`
- **Performance rules** : `.claude/rules/performance.md` (Haiku 4.5 / Sonnet 4.6 / Opus 4.5 doctrine)
- **A0 Divinity Arsenal** : `wiki/hand_offs/handoff_a0_divinity_arsenal_2026-06-20.md`