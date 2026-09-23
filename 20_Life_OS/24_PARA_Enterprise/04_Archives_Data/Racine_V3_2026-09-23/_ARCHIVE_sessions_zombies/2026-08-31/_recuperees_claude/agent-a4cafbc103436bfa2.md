---
session: agent-a4cafbc103436bfa2
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\_ARCHIVE_2026-06-16_sessions\projects\C--Users-amado\fe190d85-1d20-4b6b-ad09-92f637cc69ab\subagents\agent-a4cafbc103436bfa2.jsonl
debut: 2026-06-10T20:18:14.967Z
fin: 2026-06-10T20:21:42.066Z
messages_utilisateur: 1
reponses_assistant: 5
titre: "You are a sub-agent (A3) creating a new Claude Code skill. Read this brief fully before acting. ## CONTEXT A'S…"
---

## >>> UTILISATEUR #1

You are a sub-agent (A3) creating a new Claude Code skill. Read this brief fully before acting.

## CONTEXT

A'Space OS V2 is a sovereign agentic OS. The user (A0 Amadeus) repeatedly does "dashboard port audits" — comparing one dashboard codebase against a reference dashboard (the AaaS "Solaris" dashboard) to identify what to port. This is a recurring pattern that warrants a dedicated skill.

Per the global `~/.claude/CLAUDE.md` "Skill Creator Reflex" doctrine:
> L'agent DOIT proposer un Skill quand il observe l'un des patterns : Répétition, Checklist longue, Documentation de workflow, Scaffold detection, Handoff manuel.

This task is creating the SCAFFOLD for the skill. The skill will be invoked LATER to perform actual audits.

## EXACT DELIVERABLE

CREATE the directory `~/.claude/skills/aaas-dashboard-port-audit/` and put 2 files inside:

### File 1: `SKILL.md`
Frontmatter + skill body. Use this exact frontmatter format:

```yaml
---
name: aaas-dashboard-port-audit
description: Audit a target dashboard against the AaaS Solaris reference and produce a structured port plan (missing views, schema divergences, runtime differences, file-by-file recommendations). Use when migrating or porting a non-Solaris dashboard to mirror the AaaS 12-view structure across 4 nav groups (CULTIVATE / NURTURE / BLOOM / ROOTS).
---
```

Body sections (markdown):
1. **When to use** — bullet list of triggers
2. **Inputs** — the args the skill takes (target dashboard path; optional source path defaults to AaaS)
3. **Reference paths** — where to find the AaaS reference (Solaris paths, view list, sidebar structure)
4. **Audit steps** — numbered procedure (read target, read source, diff, categorize, output plan)
5. **Output format** — what the audit report should contain
6. **What this skill does NOT do** — read-only, no file modifications, no SQL execution
7. **Doctrine constraints** — 4 ADR blockers, no-hard-delete, Test Key Pragma, Vite vs Next.js adaptation rules

### File 2: `references/checklist.md`
A reusable checklist that the skill can include in its audit reports. Sections:
- Pre-audit setup (read CLAUDE.md, AGENTS.md, REBUILD_WORKFLOW.md on both sides)
- Runtime diff (Vite SPA vs Next.js RSC)
- Schema diff (`omk_*` vs `solaris_*`, internal vs saas)
- View parity (12 views: Dashboard, Finance, Clients, Tasks, SOP, Legal, Growth, Marketplace, Sales, ItData, People, Settings)
- Nav group parity (4 groups: CULTIVATE / NURTURE / BLOOM / ROOTS)
- Sidebar structure parity (lucide icons, collapsible, NavView enum)
- Skeletons + empty states parity
- 4 ADR blockers status check

## STRICT CONSTRAINTS

- **DO NOT** read any source code from OMK or Solaris (this is scaffold-only, no audit yet)
- **DO NOT** create any other files outside `~/.claude/skills/aaas-dashboard-port-audit/`
- **DO NOT** modify any existing files
- **DO** use the standard Claude Code skill frontmatter format (name + description in YAML, then markdown body)
- **DO** keep total content under 400 lines across both files (this is scaffolding, not a full audit)
- **DO** use kebab-case for the directory name
- **DO** reference the AaaS doctrine (4 nav groups, 12 views) accurately
- **DO** explicitly call out the 4 ADR blockers as a precondition for any actual port

## VERIFICATION (run before reporting back)

```bash
ls -la "C:/Users/amado/.claude/skills/aaas-dashboard-port-audit/"
wc -l "C:/Users/amado/.claude/skills/aaas-dashboard-port-audit/SKILL.md"
wc -l "C:/Users/amado/.claude/skills/aaas-dashboard-port-audit/references/checklist.md"
head -10 "C:/Users/amado/.claude/skills/aaas-dashboard-port-audit/SKILL.md"
```

## REPORT BACK (concise)

- 2 files created (full paths)
- Line count per file
- Confirmation: frontmatter is valid YAML, body is under 400 lines total
- Any deviations and why

Operate from `C:/Users/amado/`.

### assistant

I'll create the skill scaffold for the AaaS dashboard port audit. Let me first verify the target directory doesn't exist, then create the two files.

### assistant

Good — target directory does not exist yet. Let me create it and write the two files.

### assistant

The skill is now registered. Now let me write the references checklist file.

### assistant

Now let me run the verification commands.

### assistant

All verification checks pass. Skill is registered and the scaffold is complete.

---

## Report

**2 files created** (absolute paths):
- `C:/Users/amado/.claude/skills/aaas-dashboard-port-audit/SKILL.md` — 157 lines
- `C:/Users/amado/.claude/skills/aaas-dashboard-port-audit/references/checklist.md` — 147 lines
- **Total: 304 lines** (under the 400-line ceiling)

**Verification:**
- Frontmatter is valid YAML (3-key: `name`, `description`); matches the exact format requested
- Skill is now auto-registered in the available skills list (confirmed in the system reminder mid-task)
- Directory uses kebab-case (`aaas-dashboard-port-audit/`)
- `references/` subdirectory created as specified
- No files created or modified outside the skill directory
- No source code from OMK or Solaris was read (scaffold-only)

**Content fidelity to brief:**
- 7 body sections in SKILL.md (When to use, Inputs, Reference paths, Audit steps, Output format, What this skill does NOT do, Doctrine constraints) — all present
- Checklist.md has all 8 requested sections (Pre-audit setup, Runtime diff, Schema diff, View parity, Nav group parity, Sidebar structure, Skeletons+empty states, ADR blockers) plus a "Report completeness" section and a "Doctrine quick-cite" table
- 12 views and 4 nav groups listed accurately
- 4 ADR blockers (ADR-RICK-001, ADR-META-001, ADR-INFRA-002, ADR-INFRA-003) named explicitly as halt conditions
- Vite vs Next.js adaptation rule called out
- No-hard-delete and Test Key Pragma honored
- Skill body explicitly states: no file modifications, no SQL execution, no commits

**No deviations from brief.**
