---
source: buildermethods/agent-os v3.0 + correction A0 2026-06-06
date: 2026-06-06
type: entity
domain: L0 Tech_OS / build tooling / agent interface
tags: [#entity #agent_os #standards #spec_shaping #buildermethods #claude_code_interface]
related:
  - concept_agent_os_best_practices.md
  - concept_agent_os_adoption.md (superseded)
---

# Entity: Agent OS (Brian Casel / Builder Methods)

> github.com/buildermethods/agent-os | v3.0 | Interface agent CLI pour
> coding standards + spec-shaping. **Vit à `~/agent-os/` (agent-level), pas
> par projet.** Voir [[concept_agent_os_best_practices]] pour la doctrine
> A'Space.

## Ce que c'est

Système léger de **Standards** + **Spec-shaping** : *« agents qui
construisent comme TU construirais »*. 5 commandes slash + profiles
réutilisables.

## Les 5 commandes

| Commande | Rôle |
|---|---|
| `/discover-standards` | Extrait le tribal knowledge du codebase → standards concis |
| `/index-standards` | Reconstruit `standards/index.yml` (carte pour matching) |
| `/inject-standards [zone]` | Injecte **seulement** les standards pertinents (frugal) |
| `/plan-product` | Docs produit via AskUserQuestion |
| `/shape-spec` | **En plan mode** : façonne un meilleur spec avant de builder |

## Doctrine 2-part (officielle)

- **Base** = `~/agent-os/` (agent-level, one-shot, stable)
- **Project** = `<project>/agent-os/` (optionnel, par projet actif)
- Doc : `buildermethods.com/agent-os/installation`

## A'Space — statut 2026-06-06

- ✅ Base installée : `~/agent-os/` (166K, detached de .git)
- ✅ Best Practices écrites : `concept_agent_os_best_practices.md` (avec §11 Symphony Integration ajoutée 2026-06-06)
- ✅ Cleanup bad config Antigravity : `ASpace_OS_V2/.agent-os/` → `_TRASH/2026-06-06_agent-os-bad-config/` (move, no hard-delete, validé A0 2026-06-06)
- ✅ Pilote solaris-landing : full install (64K) + 13 standards discover + index.yml propre (zéro phantom, zéro "Needs description")
- ✅ Pilote Symphony : install `symphony/agent-os/` + 11 standards workflow + `pulse.log` schema 8 phases + demo tick runnable (Bash + PS1) → 8/8 phases, gate=PASS, $0.015 USD
- ✅ ADR-SYMPH-003 proposé : "Agent OS = standards injection + observability layer for Symphony ticks"
- ⏔ Roll-out multi-projets : décision en attente (recommandé: voir rapport pilote Symphony)

## Pourquoi A'Space en a besoin

- **Frugalité MiniMax** : `/inject-standards` = injection ciblée (vs tout
  relire à chaque tour)
- **Codification** : standards par repo = reproductible entre agents
  (Claude Code, Codex, Antigravity)
- **E-Myth du code** : transforme ton savoir-faire tacite en système
  reproductible

## Anti-patterns A'Space (à éviter)

Voir `concept_agent_os_best_practices.md` §8. Le plus critique :
**project-only sans base** (le piège Antigravity 2026-05-31).
