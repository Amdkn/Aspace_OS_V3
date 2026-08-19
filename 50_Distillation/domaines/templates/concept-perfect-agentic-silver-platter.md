---
type: Concept
title: The Perfect Agentic OS Kit — silver-platter, l'interview business owner en 10 stages
description: Kit de 31 fichiers dont le skill silver-platter (interview business owner en 10 stages + render Pantry → Prep → Plate HTML) est le cœur — un moule canonique pour les skills A'Space V3 (frontmatter > when_to_use > argument-hint > stages).
tags: [templates, perfect-agentic-os, silver-platter, interview, pantry-prep-plate, archetype, skill-format]
generated: { by: minimax-m3, at: 2026-08-19T20:05:00Z }
verified:
  - { by: process:lecture_perfect_agentic_os_integral, at: 2026-08-19T20:05:00Z }
sources:
  - id: silver-platter-skill
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/The Perfect Agentic OS Kit/skill_assets/SKILL.md"
    title: "Silver-platter — skill interview (10 stages, ~358 lignes)"
    last_modified: 2026-05
  - id: silver-platter-skill-assets-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/The Perfect Agentic OS Kit/skill_assets"
    title: "Dossier skill_assets (SKILL.md + 8 references + 2 scripts + 5 examples)"
    last_modified: 2026-05
  - id: silver-platter-examples-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/The Perfect Agentic OS Kit/skill_assets/examples"
    title: "5 exemples d'archetypes (devon_saas, dr_anwar_derma, dr_mehra_clinic, marco_ecommerce, sally_law)"
    last_modified: 2026-05
okf_version: "0.2"
---

# The Perfect Agentic OS Kit — silver-platter

## Périmètre

31 fichiers : `skill_assets/` (SKILL.md + 8 references + 2 scripts Python + 1 template Jinja2 + 5 exemples d'archetypes, chacun avec data_map.html + data_map.json + OPPORTUNITIES.md).

## Verdict global

**`synthese-datee`** — daté sur la dépendance communauté Skool, canon sur le format de skill silver-platter et le pipeline Pantry → Prep → Plate.

**Daté sur :** la mention systématique de la communauté `https://www.skool.com/earlyaidopters/about`, qui n'est pas le canal A'Space V3.

**Canon sur :** le **format d'un skill complet**, qui est précisément la structure qu'A'Space V3 pourrait adopter pour ses propres skills.

## Le skill silver-platter — structure-modèle

Le fichier `SKILL.md` est un **archétype de skill bien conçu**. Voici sa structure :

```yaml
---
name: silver-platter
description: [Interview a business owner about their day-to-day tools, build a tailored data map, render a Pantry → Prep → Plate HTML visualization with recipes, a 30-day build plan, and an interaction-layer Sankey, plus generate plain-English Claude Code recommendations (skills, subagents, hooks, rules, CLIs to install). Audits existing Claude Code setups in the cwd before asking questions, so users who've started building don't get re-asked. Output: a self-contained data_map.html, an OPPORTUNITIES.md, and a copy-paste prompt for the @claude-code-guide agent. Free, open-source, ships in the Business OS Demos Kit.]
when_to_use: "agentic OS, data map, silver platter, build my back of house, what should I build first in claude code, audit my repo, opportunities for AI, where do I start, how to map my data, claude code recommendations"
argument-hint: "[archetype | --audit | --resume]"
---
```

Cette structure frontmatter est **canonique** pour tout skill d'agent :
- `name` : l'invocable slash-command.
- `description` : 1 phrase qui couvre ce que fait le skill + comment l'invoquer (la description est le principal trigger de découverte).
- `when_to_use` : variantes de formulation que l'utilisateur pourrait employer.
- `argument-hint` : synopsis CLI.

C'est **exactement** le format utilisé par A'Space V3 dans `00_Amadeus/20_Harness/agentgateway/` et dans `os-audit-SKILL.md`. À formaliser en standard.

## Les 10 stages de l'interview

| Stage | Rôle |
|---|---|
| 0 | Silent audit (lit `.claude/` existant, évite de re-questionner) |
| 1 | Greet + speed toggle (walkthrough / fast track) |
| 2 | Business archetype (9 catégories : ecommerce / saas / professional_services / healthcare_clinic / wealth_advisory / content_creator / restaurant_multilocation / real_estate_brokerage / local_trades) |
| 3 | Pantry tools (questions orientées usage, pas schéma) |
| 4 | Existing automation audit |
| 5 | Data-engineering reality check (jargon glossed inline) |
| 6 | Assemble Pantry / Prep / Plate |
| 6.5 | Recipes (briefs que Claude écrira) |
| 6.6 | Setup priority (30-day build plan) |
| 6.7 | Interaction layer (où l'opérateur lit les briefs) |
| 7 | Render HTML |
| 8 | Render OPPORTUNITIES.md |
| 9 | Render handoff prompt @claude-code-guide |
| 9.5 | Branch « I don't have a developer » |
| 10 | Confirmation screen |

## Hard rules (canoniques pour tout skill)

- **Plain English.** Traduire tout jargon inline.
- **Never ask schema-shaped questions.** Les opérateurs ne pensent pas en `format`, `cadence`, `volume`. Penser en outcomes.
- **No em dashes.** Virgule, point, ou rewrite.
- **No "Great question!" / "I'd be happy to..."** en operator-facing copy.
- **Audit before you ask.** Si `.claude/` existe, lire FIRST et skip les questions sur ce qui est déjà construit.
- **Drafts only.** Jamais auto-écrire le `.claude/` de l'utilisateur. Handoff à `@claude-code-guide`.

## Le pattern Pantry → Prep → Plate (canonique)

Le kit impose une **visualisation 3-lane** pour les données d'un operator :

- **Pantry** (raw data sources) : outils que l'opérateur utilise déjà (CRM, tableurs, etc.).
- **Prep** (silver platters) : briefs hebdomadaires que Claude assemblera à partir du Pantry.
- **Plate** (output briefs) : ce que l'opérateur lit réellement.

C'est un **pattern de design** qui transpose la métaphore cuisine (pantry = garde-manger, prep = préparation, plate = assiette) sur le data engineering. C'est réutilisable.

## 9 archétypes d'operator (synthèse)

| Archetype | Particularités |
|---|---|
| ecommerce | volume haut (orders), Shopify-like |
| saas | recurring revenue, churn sensible |
| professional_services | billable hours, NDA |
| healthcare_clinic | PHI, régulé |
| wealth_advisory | relation client long terme |
| content_creator | back-catalog PDF/DOCX à convertir |
| restaurant_multilocation | multi-site |
| real_estate_brokerage | lead pipeline |
| local_trades | non-developer, branch hire_a_builder obligatoire |

## Scripts Python disponibles (réellement utiles)

| Script | Rôle |
|---|---|
| `scripts/audit_existing_folder.py` | détecte ce qui existe déjà dans `.claude/` |
| `scripts/render_data_map.py` | produit le HTML final à partir du JSON |
| `scripts/templates/data_map.html.j2` | template Jinja2 du HTML |

## Trace dans V3

**Aucune.** Mais le format du skill et le pattern Pantry → Prep → Plate sont **canoniques** et applicables à tout nouveau skill V3.

## Concepts liés

- [[concept-os-audit-skill-canon]] — un autre skill A'Space qui partage la philosophie « audit + report »
- [[concept-five-cross-cutting-patterns]] — agents-as-folders est le pattern transverse utilisé ici
