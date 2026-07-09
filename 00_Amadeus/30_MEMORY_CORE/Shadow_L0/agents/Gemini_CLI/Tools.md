---
source: Shadow_L0
date: 2026-05-17
type: agent-capsule
agent: Gemini_CLI
tags: [#AgentCapsule, #GeminiCLI, #Tools]
---

# Tools

## Executor

Preferred executor: Gemini CLI
Fallback executor: Codex CLI
Codex profile: verifier/editor after synthesis
Gemini mode: large-context prompt or JSON output when useful
Claude Code mode: architecture critique after Gemini synthesis

## Allowed Tools

- Gemini CLI
- PowerShell read commands
- `rg`
- Context7 or official docs for provider/MCP/CLI config
- **Claude Code Skills** (read-only access via `~/.claude/skills/<skill-name>/`)

## Claude Code Skills Available

Gemini CLI ne peut pas invoquer directement `/skill-creator` ou les autres slash-skills (ce sont des features Claude Code). En revanche, Gemini PEUT et DOIT :

1. **Lire** le contenu de `~/.claude/skills/<skill-name>/SKILL.md` pour comprendre un workflow cristallisé.
2. **Exécuter** les `scripts/install.ps1` ou `.sh` packagés dans un skill via PowerShell ou bash direct.
3. **Proposer la création** d'un nouveau skill quand Gemini détecte un pattern répétitif (cf. [[concept_skill_reflex]]). La proposition va dans la queue `LLM_Wiki/wiki/hand_offs/skills_queue.md`. Claude Code (ou A0) invoquera `/skill-creator` ensuite.

Skills déjà disponibles à lire/exécuter :

| Skill | Path | Usage Gemini |
|---|---|---|
| `pp-cli-install` | `~/.claude/skills/pp-cli-install/` | `powershell -File scripts/install.ps1 -Service <name>` |

Lire `LLM_Wiki/wiki/concepts/concept_skill_reflex.md` pour la doctrine complète des 5 triggers obligatoires.

## Forbidden Tools

- raw secret printing
- destructive filesystem commands without explicit mission approval
- provider/MCP config edits without Docs Dogmatique source
- **Invocation directe `/skill-creator`** (réservée à Claude Code — Gemini propose, Claude exécute)

## MCP Scope

Allowed MCP servers: documented Gemini config only.

## Environment Variables

Required variable names only:

- provider variables configured outside markdown
