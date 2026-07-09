---
source: Codex
date: 2026-05-19
type: concept
domain: Shadow_L0 / ECC / Cross-Harness Orchestration
tags: [#ECC, #ShadowL0, #Gemini, #Codex, #ClaudeCode, #MiniMax, #Symphony]
status: ACTIVE
---

# ECC Agnostic Agent Library

## Decision

ECC est retrograde de "systeme Claude Code" vers une bibliotheque agentique
agnostique. Ses composants peuvent etre lus, adaptes et executes par Gemini CLI,
Codex CLI ou Claude Code CLI route via MiniMax.

Le principe canonique est:

> Persona invariante, harnais variable.

Un agent, un skill ou une regle garde son intention. Seul l'executant change selon
la couche, le quota, le contexte et la surface d'action disponible.

## Pourquoi

A0 a deja une capacite MiniMax tres large via Claude Code CLI, alors que Claude
Desktop peut tomber en limite Anthropic. Gemini possede un contexte large et un
plan genereux. Codex est fort pour l'implementation locale et l'audit de fichiers.

Le bon systeme n'est donc pas "Claude possede ECC"; le bon systeme est:

- ECC = bibliotheque de composants agentiques;
- Gemini = pont long-contexte et continuite L1;
- Codex = executant local et mainteneur du LLM Wiki;
- Claude Code sur MiniMax = moteur Claude-style sans bruler le quota Anthropic.

## Sources locales verifiees

| Source | Preuve |
|--------|--------|
| Clone ECC | `C:\Users\amado\ECC` |
| Skill Gemini ECC | `C:\Users\amado\.gemini\skills\ecc\SKILL.md` |
| Etat d'installation Gemini | `C:\Users\amado\.gemini\ecc-install-state.json` |
| Skill Codex cree | `C:\Users\amado\.codex\skills\ecc-agnostic-orchestrator\SKILL.md` |
| Doctrine Memory Core | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md` |

Note Context7: aucune source Context7 officielle n'a ete utilisee ici, car cette
decision documente un etat local et une doctrine interne A'Space. Les claims
provider restent exclus de cette page.

## Routage Shadow

| Couche | Harnais primaire | Role |
|--------|------------------|------|
| Shadow L0 | Codex CLI | fichiers locaux, scripts, audits, LLM Wiki, meta-optimisation |
| Shadow L1 | Gemini CLI | Life OS, Baserow, Plane, synthese longue, reprise quand Claude/Codex sont occupes |
| Shadow L2 | Claude Code CLI + MiniMax | production business, boucles Claude-style, forte frequence quand Symphony sera pret |

## Format d'adaptation

Chaque composant ECC adapte doit produire une fiche minimale:

```text
source_component:
source_path:
target_harness:
target_path:
invocation:
preconditions:
safety:
validation:
residual_risk:
```

## Regles

- Ne jamais supposer qu'un skill imbrique est actif dans un harnais.
- Lire le `SKILL.md` source avant adaptation.
- Traduire les commandes propres a Claude en instructions compatibles Gemini ou Codex.
- Ne jamais copier de secrets.
- Ne pas promouvoir toute la bibliotheque ECC en bloc; faire stocktake, prioriser, adapter.
- Documenter dans le LLM Wiki quand une adaptation devient doctrine durable.

## Impact sur Symphony

Symphony ne doit pas router vers "Claude", "Gemini" ou "Codex" comme identites.
Il doit router vers une capacite:

- reasoning Claude-style;
- long-context synthesis;
- local-file implementation;
- security review;
- orchestration heartbeat;
- knowledge-base audit.

Ensuite seulement, Symphony choisit le harnais disponible qui porte cette capacite.
