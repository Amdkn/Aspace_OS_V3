---
type: Concept
title: os-audit-SKILL.md — le skill canonique A'Space pour auditer un second brain
description: Skill canonique écrit par l'utilisateur (A+) à la racine de 02_Templates/, mirroré sur `~/.claude/skills/os-audit/SKILL.md`. Audite poisoning, bloat, confusion, clash d'un AIOS. Format-modèle pour les skills A'Space V3.
tags: [canon, skill, os-audit, second-brain, a-plus, format-canon]
generated: { by: minimax-m3, at: 2026-08-19T20:30:00Z }
verified:
  - { by: process:lecture_skill_os_audit_integral, at: 2026-08-19T20:30:00Z }
sources:
  - id: os-audit-skill-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/os-audit-SKILL.md"
    title: "OS audit SKILL.md — 5 modes de failure + 6 étapes + hard rules"
    last_modified: 2026-08
  - id: os-audit-source-of-truth
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/os-audit-SKILL.md"
    title: "Source of truth : « the executable copy lives at `~/.claude/skills/os-audit/SKILL.md` »"
    last_modified: 2026-08
okf_version: "0.2"
---

# os-audit-SKILL.md — skill canonique A'Space

## Énoncé

Le fichier `os-audit-SKILL.md` à la racine de `02_Templates/` **n'est pas un kit tiers** comme les 9 autres — c'est un **skill écrit par l'utilisateur (A+)** lui-même. Il est mirroré sur le filesystem global (`~/.claude/skills/os-audit/SKILL.md`), ce qui en fait un **artefact canonique d'A'Space**.

> **Source of truth** — this `.md` is the readable mirror of `os-audit-SKILL.md - Google Docs.pdf` in this same folder. The PDF is the canonical artifact from the source (Nate Herk, "Steal My Exact AI OS Setup (5 simple tips)"). The executable copy lives at `C:\Users\amado\.claude\skills\os-audit\SKILL.md`. When updating, edit the executable and re-export the PDF.

Cette triple présence (PDF source, MD miroir, MD exécutable) en fait un cas-modèle pour les skills A'Space.

## Périmètre

Le skill pose **4 modes de failure** qu'il audite, **2 types de context** qu'il distingue, et **6 étapes** d'audit en lecture seule.

### Les 4 modes de failure

| Mode | Symptôme | Antidote |
|---|---|---|
| **Poisoning** | Faux fait dans le contexte, agent affiché avec confiance | Vérification (web search, cross-check live DB, HITL) |
| **Bloat** | Trop de données, agent ne tire pas le signal | Segmentation expertise vs situationnel |
| **Confusion** | Fait présent non-pertinent, ou manquant et agent complète | Routing plus strict + completeness checks |
| **Clash** | Deux sources en désaccord, agent en choisit une arbitrairement | Version-stamping + source unique par claim |

### Les 2 types de context

- **Expertise context** : toujours chargé. Le rulebook. Identity, goals, policies.
- **Situational context** : juste-à-temps. Données spécifiques (ticket client, tâche précise).

L'audit trouve où les deux ont été confondus, où le rulebook est devenu stale, où le situationnel a saigné dans l'expertise.

### Les 6 étapes

1. **Routing integrity** : vérifier que chaque chemin dans les fichiers d'index existe réellement sur disque.
2. **Index truth** : comparer les compteurs des index aux mesure réelles du disque.
3. **Freshness** : classifier chaque feed de données (fresh / drifting / frozen / retired / on-demand).
4. **Memory** : chercher le bloat, la duplication, les organisation cassées.
5. **Context placement** : distinguer expertise vs situationnel pour chaque nœud de connaissance.
6. **Output** : produire un rapport `audits/audit_{YYYY-MM-DD}.md` avec sections Fix list / Routing + index / Data catchup / Durability / D1 receipts.

## Hard rules (canoniques)

1. **Read only.** Jamais de `mv`, `rm`, `Write`, `Edit` sur des fichiers source. Seules écritures autorisées : le nouveau rapport d'audit et `.gitkeep` si le dossier `audits/` n'existait pas.
2. **No D1 claims without proof.** Chaque « l'index dit 55 mais le disque en a 79 » doit venir avec un `ls | wc -l` et la sortie exacte.
3. **Wait for explicit approval before fixing.** L'utilisateur choisit quels fixes shipper.
4. **No machine-gun fixes.** Grouper en 4-6 buckets avec scope clair.
5. **Diff against the prior audit.** Si pas de rapport précédent, le dire explicitement.

Ces règles sont **canoniques** et **applicables à tout skill d'audit A'Space**.

## Trace dans V3

**Triple trace :**
1. PDF source : `os-audit-SKILL.md - Google Docs.pdf` (sibling dans `02_Templates/`).
2. MD miroir : `os-audit-SKILL.md` (lisible).
3. MD exécutable : `~/.claude/skills/os-audit/SKILL.md` (invoqué par `/os-audit`).

Le skill est **réellement invocable** dans les sessions CC. C'est l'un des rares artefacts de la racine `02_Templates/` qui est **exécuté**, pas seulement lu.

## Comparaison avec silver-platter (The Perfect Agentic OS Kit)

Les deux skills partagent :
- Frontmatter avec `name`, `description`, `when_to_use`, `argument-hint`.
- Stage-based workflow (Stage 0 à Stage 10).
- Hard rules (Plain English, audit before ask, drafts only).

Mais ils diffèrent :
- `os-audit` est **read-only** (jamais d'écriture sur le corpus, sauf le rapport).
- `silver-platter` **génère** des artefacts (HTML, OPPORTUNITIES.md, handoff prompt).

C'est la **distinction read-only / generative** parmi les skills.

## Pourquoi ce skill est canonique pour A'Space V3

A'Space V3 a explicitement besoin d'un audit :
- 180+ entrées à la racine (avant 2026-08-02 : 340).
- Multiples vagues de distillation (V2 → V3).
- Multiples agents (A0/A1/A2 + capitaines L2).

L'inadéquation entre ce qu'un agent **croit** exister (les index) et ce qui **existe vraiment** (le disque) est un risque concret que ce skill adresse.

## Concepts liés

- [[concept-perfect-agentic-silver-platter]] — l'autre skill-modèle (generative)
- [[concept-kits-utilisation-trace]] — ce skill est dans les fichiers racine, pas dans les 9 kits
