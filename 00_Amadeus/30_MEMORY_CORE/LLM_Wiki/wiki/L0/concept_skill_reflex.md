---
source: LLM_Wiki_A0
date: 2026-05-17
type: concept
domain: A0_Sovereign / Agent_Autonomy / Skills
tags: [#SkillCreator #Reflex #Agent_Autonomy #Anti_Repetition #Compounding]
---

# Concept — Skill Creator Reflex

## Definition

**Skill Creator Reflex** est le principe agentique selon lequel **les agents (Claude Code / Codex / Gemini) sont responsables de détecter les workflows répétitifs et de proposer leur cristallisation en Skills**. A0 Amadeus n'invoque jamais `/skill-creator` directement — il émet une Intention, l'agent reconnaît le pattern, propose la création.

## Pourquoi ce principe

A0 occupe le rôle **Pilote / Visionnaire** (E-Myth). Toute friction technique le repousse vers le rôle **Technicien**, ce qui :
- Casse le flow d'Intention.
- Lui fait porter une charge mentale d'inventaire d'outils (impossible à grande échelle).
- Le rend rate-limiter du système.

L'agent occupe le rôle **Manager / Technicien augmenté** : il VOIT les patterns parce qu'il EXÉCUTE les tool calls. Il a donc la responsabilité d'industrialiser ce qu'il vient de faire à la main.

## Cinq Triggers Obligatoires

| Trigger | Exemple A'Space |
|---|---|
| **Répétition session** (3+ tool calls répétés 2×) | 2 `printing-press generate` consécutifs → propose `/pp-cli-install` |
| **Checklist longue** (≥5 étapes Bash/Edit/Write) | Plan d'installation Hermes → propose `/hermes-bootstrap` |
| **Workflow documenté** (.md avec commandes shell) | Doc `02_god-mode-cli-stack.md` → propose `/pp-cli-install` |
| **Scaffold récurrent** (templates remplis) | ADR-XXX, source page, agent capsule → propose `/adr-scaffold` |
| **Handoff manuel** (brief exécutable pour autre agent) | `Shadow_L1/handoffs/Codex_CLI.md` → propose `/shadow-handoff` |
| **Exploration Context7 / Docs Dogmatiques** | MCP/provider/hook/config → Context7 ou docs officielles → si checklist récurrente, propose un skill |

## Format de proposition (court)

```
🛠️ Skill Creator Reflex : pattern détecté = [TRIGGER]
   Skill proposé : /<nom-skill>
   ROI : ~X min/invocation économisées
   Lance /skill-creator maintenant ? [oui/non/plus tard]
```

## Comportement attendu

| Si A0 répond... | Agent fait... |
|---|---|
| `oui` / `go` | Invoque `/skill-creator` immédiatement |
| `plus tard` | Ajoute à `hand_offs/skills_queue.md` |
| `non` | Pas de skill, mais log dans le wiki pourquoi (futur lint check) |

## Context7 Evidence Loop

Quand le workflow touche un provider, MCP, hook, CLI, dependency, SDK, WSL,
Hermes ou une configuration durable, l'agent doit faire une boucle de preuve:

1. Lire la source locale pertinente (`README.md`, `AGENTS.md`, `SKILL.md`, config).
2. Interroger Context7 si disponible pour obtenir la doc actuelle.
3. Si Context7 est indisponible, utiliser les docs officielles ou la source upstream locale et marquer la preuve comme fallback.
4. Si l'exploration produit une procédure 3+ étapes répétable, créer/proposer un skill.
5. Si l'exploration modifie la doctrine A'Space, mettre à jour:
   - `30_MEMORY_CORE/README.md`
   - `LLM_Wiki/wiki/log.md`
   - `LLM_Wiki/wiki/index.md` si une nouvelle page durable est créée.

Format de preuve attendu:

```text
Context7: <library/doc id>
Official docs: <URL>
Local source fallback: <path>
Validation: <command>
Residual risk: <risk>
Secret handling: no secrets printed; env var names only
```

## Anti-Patterns interdits

❌ Dire à A0 "tu peux utiliser /skill-creator pour..." (renvoie la charge).
❌ Créer un skill sans accord A0 (viole 3-Turn Air Lock).
❌ Ignorer un pattern trigger parce que "le contexte est plein" (logger dans la queue à défaut).
❌ Skill trop spécifique (`/install-vercel`) → généraliser (`/cli-install <service>`).
❌ Skill qui fait trop (`/setup-everything`) → décomposer.

## Cross-Refs

- [[concept_compounding_knowledge]] — Skills = compounding execution.
- [[concept_autonomous_research_loop]] — Skills = `train.py`-level mutation surface.
- [[concept_god_mode_cli_stack]] — Skills composent les CLIs en super-commandes.
- [[concept_e-myth]] — Anti-Technicien / Pilote vs Manager.
- [[concept_agent_capsule]] — Skills ≠ Agent Capsules (skills = verbes, capsules = identités).

## Implementation

- **Directive** : `C:\Users\amado\.claude\CLAUDE.md` (section "Skill Creator Reflex").
- **Hook detector** : `C:\Users\amado\.claude\bin\skill-reflex-detect.ps1` + `UserPromptSubmit` dans `settings.json`.
- **Codex hooks** : `C:\Users\amado\.codex\hooks\context7_*.ps1` + `skill_reflex_*.ps1` injectent la règle Context7 → Skill Reflex → Memory Core / LLM Wiki.
- **Queue** : `LLM_Wiki/wiki/hand_offs/skills_queue.md` (propositions ouvertes).
- **Inventaire** : `~/.claude/skills/` (skills locaux installés).

## Inbounds

- ADR-MCP-001 (mentionne les skills comme couche au-dessus du CLI Stack)
- Queue `hand_offs/skills_queue.md`
