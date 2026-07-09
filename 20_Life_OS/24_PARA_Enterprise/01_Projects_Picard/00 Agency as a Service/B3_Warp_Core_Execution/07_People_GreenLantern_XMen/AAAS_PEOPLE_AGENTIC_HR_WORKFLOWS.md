---
source: A0_Amadeus + People doctrine v5 (Green Lantern) + resource_claude_dynamic_workflows_6patterns + ADR-HERMES-001
date: 2026-06-03
type: agentic_hr_workflows
domain: L2_Business / People / Project 00 Agency as a Service / Mode Solaris
status: DRAFT_V1
tags: [#people #agentic_hr #dynamic_workflows #hermes_swarm #recruiting #onboarding #ethics #tournament #adversarial]
---

# 👥 RH Agentique — les 6 patterns au service du domaine People

> Companion to `JTBD-001_AAAS_OWNER_HANDOFF_MAP.md`. Le **RH Agentique** = piloter le cycle de vie des membres
> (capsules IA **et** humains) avec les **6 dynamic-workflow patterns** (Claude Code), incarnés dans **Hermes
> Swarm Mode** (PE17). Doctrine : Green Lantern v5 (PE2 onboarding, PE6 perf, PE8 baseline, PE12 ethics, PE17 swarm).
> **L'unlock clé** : l'**adversarial verification** tue le *self-preference* — exactement le biais que PE6/PE12 combattent.

## Les 6 patterns → fonctions RH

| Pattern | Fonction RH Agentique | Brique doctrine |
|---|---|---|
| **Classify & Act** | **Intake routing** : une demande People (nouvel agent, ticket, flag éthique) → classée → routée au handler (onboarding / perf / ethics / decommission). Quarantaine avant action. | PE2 onboarding structuré |
| **Fan-out & Synthesize** | **Évaluation multi-angle** d'un candidat (humain ou capsule) : un agent par lens (skill-fit, culture, éthique, coût/affordability) en parallèle → **hire-memo cité** (source par finding). | PE4 fit, PE15 affordability |
| **Adversarial Verification** | **Perf-review & ethics-audit sans auto-complaisance** : 3 sceptiques challengent le travail/le self-report d'un agent contre une **rubrique** (= la rubrique éthique SDD-001). Tue le self-preference. | **PE6 no-bullshit · PE12 ethics audit** |
| **Generate & Filter** | **Sourcing** : sur-générer profils/role-specs/checklists d'onboarding → judge-filter (judge ≠ generator). | PE4 recrutement |
| **Tournament** | **Ranking pair-wise** (l'exemple CV = du RH !) : classer candidats/agents pour un rôle ou une promotion, agent frais par match, **rubrique par round**, traçabilité de décision. | PE6 perf, PE7 capacity |
| **Loop Until Done** | **Sweep jusqu'à clean** : auditer jusqu'à **zéro violation éthique** (PE12 Build Gate), onboarding 100% complet, ou plus aucun nouvel écart d'alignement. | PE8 baseline, PE12 gate |

## Adaptation Hermes Swarm (PE17 — le harness incarné)
Le dynamic workflow Claude Code = le **harness-natif**. En A'Space il **tourne comme une mission Hermes Workspace
Swarm Mode** (ADR-HERMES-001 : Hermes live) :
- **role-based dispatch** = Classify & Act + Fan-out
- **byte-verified review gate** = Adversarial Verification (le devil's-advocate institutionnalisé)
- **persistent tmux workers + Kanban** = le bracket Tournament + le Loop-until-done
- **proof-bearing checkpoints** = les citations / la traçabilité de décision
- **Partage** = `SKILL.md` + workflow `.js` + rubrique → un **skill Hermes** réutilisable (et/ou un `WORKFLOW.md` Symphony).

## Garde-fous (doctrine + transcript)
- **Adversarial verification obligatoire** sur toute perf-review/ethics-audit d'agent (jamais l'agent qui s'auto-note — PE6/PE12, anti-self-preference).
- **Budget token explicite** par workflow (token-consuming) → People PE15 affordability + Finance Compute (SLA).
- **Ne pas dégainer un essaim pour une tâche basique** (changer une couleur) — prompt simple. L'essaim = cas complexes (recrutement de masse, audit éthique, ranking).
- Aucune capsule `Active` sans baseline 7j (PE8) — le Loop-until-done peut *produire* cette preuve.

## Exemple stacké (RH de masse)
Recruter/sélectionner des capsules pour une squad AaaS : **Generate & Filter** (sur-générer des profils d'agents) →
**Tournament** (ranking pair-wise contre rubrique par round) → **Adversarial Verification** (3 sceptiques + audit
éthique SDD-001) → **Loop Until Done** (jusqu'à zéro flag éthique + baseline 7j atteinte). Une mission Hermes Swarm.

## Prochains pas
1. Écrire le **skill Hermes `agentic-hr-tournament`** (SKILL.md + workflow.js + rubrique éthique SDD-001) — réutilisable.
2. Brancher l'ethics-audit (PE12) en **adversarial-verification** récurrent (cron heartbeat PE18).
3. Lier au `JTBD-002 People agent-governance gate` (le gate qui passe CONDITIONAL→PASS).

## Sources
- 6 patterns : `03_Resources_Geordi/01_Guides/08_People/resource_claude_dynamic_workflows_6patterns.md`.
- Doctrine : `07_People_GreenLantern_XMen/03_GREENLANTERN_PEOPLE_PRINCIPLES.md` (PE6/PE12/PE17 + PE30). Harness : ADR-HERMES-001.
