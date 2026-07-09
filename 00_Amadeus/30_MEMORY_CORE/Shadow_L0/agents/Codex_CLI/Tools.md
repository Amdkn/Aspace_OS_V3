---
source: Shadow_L0
date: 2026-05-17
type: agent-capsule
agent: Codex_CLI
tags: [#AgentCapsule, #Codex, #Tools]
---

# Tools

## Executor

Preferred executor: Codex CLI
Fallback executor: Claude Code CLI
Codex profile: `shadow_l0_safe`, `shadow_l0_exec`, `shadow_l0_yolo`
Gemini mode: read-only scout when needed
Claude Code mode: alternate implementer when Codex quota or context is constrained

## Allowed Tools

- PowerShell
- `rg`
- `git status`
- `codex exec`
- local test commands
- Context7 for provider, MCP, SDK, CLI, or configuration docs
- **Claude Code Skills scripts** (exécution directe via PowerShell/bash)

## Claude Code Skills Available

Codex CLI ne peut pas invoquer `/skill-creator` (slash-skill = feature Claude Code). En revanche, Codex DOIT :

1. **Lire** `~/.claude/skills/<skill-name>/SKILL.md` pour comprendre un workflow cristallisé avant de l'implémenter manuellement.
2. **Exécuter** les `scripts/install.ps1` / `.sh` packagés via `shadow_l0_exec` :
   ```powershell
   shadow_l0_exec "powershell -File C:\Users\amado\.claude\skills\<skill>\scripts\install.ps1 -Service <X>"
   ```
3. **Proposer la création** d'un skill quand Codex détecte un pattern répétitif (cf. [[concept_skill_reflex]]). Ajouter à `LLM_Wiki/wiki/hand_offs/skills_queue.md`. Claude Code invoquera `/skill-creator` ensuite.
4. **Étendre les références** d'un skill existant (ex: ajouter URLs OpenAPI dans `~/.claude/skills/pp-cli-install/references/known-spec-urls.md`) — c'est de la maintenance Codex naturelle.

Skills disponibles à exécuter via `shadow_l0_exec` :

| Skill | Script | Mission Codex typique |
|-------|--------|----------------------|
| `pp-cli-install` | `~/.claude/skills/pp-cli-install/scripts/install.ps1` | Batch install de CLIs Shadow L2 (Airtable, Apollo, Hostinger…) |

Doctrine complète : `LLM_Wiki/wiki/concepts/concept_skill_reflex.md` (5 triggers obligatoires, anti-patterns interdits).

## Forbidden Tools

- raw secret printing
- destructive filesystem commands without explicit mission approval
- provider/MCP config edits without Docs Dogmatique source
- **Invocation directe `/skill-creator`** (réservée à Claude Code via Skill tool)

## MCP Scope

Allowed MCP servers: Context7, repo-local MCPs when documented.

## Environment Variables

Required variable names only:

- none by default
