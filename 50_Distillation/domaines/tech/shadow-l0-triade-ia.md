---
type: Concept
title: Shadow L0 manuel — triade Claude / GPT-Codex / Gemini
description: Avant l'automatisation Hermes, A0 opère L0 manuellement via 3 IA complémentaires par capability, pas par couche. Capability routing, pas model routing.
tags: [tech, shadow, capability-routing, claude, gpt, gemini]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-010-shadow-l0
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-010_meta-cloture-scope-13eme-semaine_UPDATED_shadow-L0-IA.md
    title: SDD-010 § 5.6 Shadow L0 Manuel — Triade
    last_modified: 2026-05-13
  - id: symph-002-variants
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-002_symphony-variants-per-harness.md
    title: ADR-SYMPH-002 Variants Symphony par Harness
    last_modified: 2026-05-26
okf_version: "0.2"
---

Le **Shadow L0 manuel** est la couche opératoire transitoire d'A0 avant l'automatisation Hermes. Il est composé de trois IA utilisées comme opérateurs Shadow transverses.

## Les trois opérateurs

| Opérateur | Affordance principale | Usage naturel | Limite doctrinale |
|-----------|----------------------|---------------|-------------------|
| **Claude / Claude Code** | Code, fichiers, APIs, CLI, refactor, actions profondes | L0 infra, L1 adapters, L2 scripts/API/actions | Ne devient pas l'orchestrateur global |
| **GPT / Codex** | Raisonnement, recherche, génération, documentation, découpage | PRD/ADR/DDD/TDD, SOPs, specs, QA, lead research | Ne remplace pas les Build Gates humains |
| **Gemini / Antigravity** | Navigation web, vision navigateur, Chrome, configuration SaaS | Structuration Baserow/Airtable/ClickUp/Notion, inspection UI | Ne modifie pas le Kernel sans passage par spec/validation |

## Doctrine : Capability Routing

**Les couches sont souveraines ; les modèles sont des véhicules.**

```yaml
capability_routing:
  browser_native:
    preferred: gemini_antigravity
    use_for: [inspect_web_apps, configure_baserow, configure_airtable,
              configure_clickup, apply_notion_structure]
  code_and_api_actions:
    preferred: claude_code
    use_for: [api_scripts, cli_tools, filesystem, github,
              mcp_to_cli, batch_imports]
  reasoning_and_documentation:
    preferred: gpt_codex
    use_for: [specs, sop, research, qa, issue_breakdown, lead_research]
```

**Le modèle peut traverser les couches. La spec ne traverse pas sans autorisation.**

## Variants interactifs (ADR-SYMPH-002)

| Variant | Tick auto | Émet topics | Consomme | Provider | Trust |
|---------|-----------|-------------|----------|----------|-------|
| Claude_Code_CLI | ✓ | ✓ | ✓ | MiniMax | autonomy_scope |
| Codex_CLI | ✓ | ✓ | ✓ | OpenAI | autonomy_scope |
| Gemini_CLI | ✓ | ✓ | ✓ | Google | autonomy_scope |
| Antigravity_IDE | ✗ | ✗ | ✓ | Google | sandbox |
| Claude_Desktop_App | ✗ | ✗ | ✓ | Anthropic | sandbox |
| Codex_Desktop | ✗ | ✗ | ✓ | OpenAI | sandbox |

**Règle** : seuls les variants `_CLI` ont l'autonomie de tick. Les variants `_IDE`/`_App`/`_Desktop` sont des **consoles interactives** pour A0, jamais des participants actifs au bus.

## Trajectoire d'automatisation

```
1. Shadow manuel       : Amadeus + Claude / GPT / Gemini (tester la forme)
2. Shadow assisté      : Claude Code + APIs + plugins + MCP / CLI
3. Runtime autonome    : Open Hermes A1 + Claude Code / MiniMax A2 + Hermes Agents A3
```

## Pourquoi pas de rigidité modèle → couche

L'anti-pattern observé V0 : assigner rigidement « Claude = L0, GPT = L1, Gemini = L2 ». Correction V1 : **capability routing** — mission + accès + coût + risque + interface.

L'antidote : un modèle qui traverse les couches (Claude fait du code ET de la doc, Gemini fait du search ET du browser) n'est pas une violation — c'est la doctrine. Ce qui ne traverse pas, c'est la **spec** sans autorisation.

Voir aussi : [[symphony-bus-replace-n8n]], [[caste-doctor-who]], [[paniques-k1-k4-kernel]].