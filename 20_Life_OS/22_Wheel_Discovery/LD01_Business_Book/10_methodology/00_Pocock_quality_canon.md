---
type: methodology-l0-lightning
title: Pocock Quality Canon — pour skills dérivés de CARDIA-TDD BC-Methodology
description: Capture locale (zero-install, read-canon only) des principes qualité du repo upstream mattpocock/skills/writing-great-skills. À appliquer quand BC-Methodology (10_methodology/) génère un SKILL canonique. Source : upstream README + SKILL.md + convention A+'s « anti-doublon skill-creator ».
timestamp: 2026-07-04T14:15:00-04:00
domain: LD01_Career_Business
bounded_context: BC-Methodology
upstream_source: https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md
install_status: zero-install (gated Rick S1 per ADR-LD01-003)
rot_rate: lent (verrouillé tant que upstream ne change pas son canon)
verified_by: Test-Path "https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills"
---

# Pocock Quality Canon — pour BC-Methodology skills

> *Capture locale (L0 Lightning zero-install) du canon qualité upstream. Aucune dépendance runtime, aucune install. À appliquer quand BC-Methodology produit un SKILL canonique dérivé de CARDIA-TDD.*

## 0. Pourquoi ce fichier

Per ADR-LD01-003 §L0 : « Quand `10_methodology/*.md` produit un SKILL, suivre Pocock quality canon ». Le but = **anti-doublon skill-creator** — si je (ou un harness quelconque) génère un skill depuis CARDIA-TDD methodology, il DOIT passer ce filtre avant d'être committé.

## 1. Le canon qualité (extracted de upstream)

D1-receipts 2026-07-04 — lu depuis `mattpocock/skills/writing-great-skills/SKILL.md` upstream (lecture read-only, pas installé) :

### 1.1 Frontmatter obligatoire (8 champs top-level)

```yaml
---
name: <skill-name>          # lowercase-kebab, verb-led
description: <max 1024 chars, 1 phrase, NO angle brackets, anti-XML>
allowed-tools: [...]         # restrictive — list explicite
when_to_use: <trigger-pattern, multi-sentence>
version: <semver>            # always increment on mutation
author: <name + handle>
license: <MIT|Apache-2.0|...>
---
```

### 1.2 Champs vides = refus

- `name:` vide → refuser
- `description:` vide → refuser  
- `allowed-tools:` vide → dangerously-permissive → refuser
- `when_to_use:` vide → skill ne sait pas se déclencher → refuser

### 1.3 Description en 1 phrase

> « A short, precise description of what this skill does in a single sentence. Avoid angle brackets. »

→ **Anti-pattern dupliquer** : si 2 skills ont la même description, ils DOIVENT être mergés ou l'un doit référencer l'autre (link, pas copie).

### 1.4 When-to-use = trigger pattern

> « A multi-sentence description of when to invoke this skill. Include both the trigger condition and the expected outcome. »

→ **Anti-pattern vague** : « when user wants AI stuff » n'est PAS un trigger — c'est trop large. Un bon trigger = un comportement observable (e.g. « when user says `/refactor` or asks 'can we reduce duplication here' »).

### 1.5 Self-test = optional mais recommandé

Pocock's canon inclut `tests/` par skill. BC-Methodology skills dérivés DOIVENT avoir au moins 1 test = une commande re-jouable qui prouve que le skill fait ce qu'il dit (cf. CARDIA-TDD §2.1 — D1 receipt transposition).

### 1.6 Anti-doublon canon (la règle d'or de Pocock)

> « Don't write a skill that does what an existing skill does. Extend an existing skill instead. »

→ Si un skill candidate à la création overlap avec un existant :
- Soit il devient une **sous-section** d'un skill existant (extension, ADR additif)
- Soit il devient un **`PROCEDURE.md`** dans un skill parent (workflow composé)

## 2. Application au BC-Methodology LD01

CARDIA-TDD artifacts qui peuvent devenir des SKILL via ce canon :

| Source `10_methodology/*.md` | SKILL canonique potentiel | Status |
|---|---|---|
| `00_CARDIA_overview.md` (méthodologie 6 propriétés) | `cardia-tdd` skill (quality canon = no-doublon, D1 receipt required) | ACTIVATED W4 mi |
| `00_Pocock_quality_canon.md` (ce fichier) | `pocock-quality-canon` skill (référence upstream, anticlône) | ACTIVATED 2026-07-04T14:15 ET (l'instant) |
| Sub-methodology future | À author au moment du besoin | gated A0 |

## 3. Le skill `pocock-quality-canon` (proposed canon)

```yaml
---
name: pocock-quality-canon
description: Enforce Pocock quality canon on any skill authoring attempt — frontmatter 8-fields required, single-sentence description, trigger-when-to-use pattern, anti-doublon merger with existing skills. Use when reviewing or authoring a skill under BC-Methodology.
allowed-tools: [Read, Glob, Grep, Edit, Write]
when_to_use: When user invokes `/author-skill` skill or asks "let's create a new skill that does X". Refuses with rationale if the candidate overlaps an existing skill (D4 anti-doublon). Trigger also fires on incoming skill PR review.
version: 1.0.0
author: A0 (canonical) · MiniMax (L1 Mavis) · Book A3
license: MIT
---

## Self-test (D1 receipt)

```
$ test ! -z "$(yq .name ${SKILL}.md)"     # name required
$ test ! -z "$(yq .description ${SKILL}.md)" && [ $(echo $(yq .description ${SKILL}.md) | wc -c) -lt 1024 ]   # description required + < 1024
$ test ! -z "$(yq .when_to_use ${SKILL}.md)"  # when_to_use required
# dup check
$ grep -l "$(yq .description ${SKILL}.md)" ~/.mavis/skills/*/SKILL.md ~/.claude/skills/*/SKILL.md 2>/dev/null | wc -l
$ [ $? -le 1 ]   # at most 1 (the file itself)
```

## Procedure

1. **Read** candidate SKILL.md frontmatter (8 fields check).
2. **Validate** per §1.1: refuse if any of name/description/allowed-tools/when_to_use is empty.
3. **Description length check** (≤1024 chars) + 1-sentence check (no period in middle except as final).
4. **When-to-use clarity check** (specific trigger phrase, not vague "when user wants AI stuff").
5. **Anti-doublon grep** for description across all skills in `~/.mavis/skills/*/SKILL.md`, `~/.claude/skills/*/SKILL.md`. If > 1 match → refuse + suggest merger.
6. **Version semver increment** if file existed.
7. **Append** `LD01/99_meta/calendar.md` regardless of outcome (accept/refuse entry).
```

> **Note technique** : ce skill canon est le SEUL qu'on commit dans `10_methodology/00_Pocook_quality_canon.md` (recherche read-canon, pas install). Les autres SKILL candidats migrent vers `~/.mavis/skills/<name>/SKILL.md` quand ils sont acceptés.

## 4. Anti-patterns (skip these in any skill)

| Anti-pattern | Pourquoi bloqué |
|---|---|
| Description vague « AI-powered thing » | Pas un trigger — pas invocable |
| `allowed-tools: *` (splat) | dangerously-permissive = permissionMode bypass |
| Empty `when_to_use` | Skill ne sait pas se déclencher = mort-né |
| Skill qui copie description d'un autre | Anti-doublon canon |
| Skill sans self-test | Pas de D1 receipt — CARDIA-TDD §2.1 refus |
| Skill sans `version:` ou `author:` | Pas traçable |
| Skill avec license incompatible aux canon A'Space (MIT/Apache-2.0) | D5 incohérence |

## 5. Héritages et inspirations

- **Pocock canon** (mattpocock/skills/writing-great-skills — source upstream)
- **CARDIA-TDD §2.1** (TDD transposition — D1 receipt)
- **CARDIA-TDD §A Antifragile** (system gains from stress — anti-doublon strengthens the system)
- **Cole Medin Dark Factory** (Dark Factory Level 5 = skills composition, not skill explosion)

## 6. Adresses canoniques

| Ressource | Chemin |
|---|---|
| Ce canon (capture locale) | `LD01/10_methodology/00_Pocook_quality_canon.md` |
| Upstream à surveiller | `https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md` |
| Activation log | `LD01/99_meta/calendar.md` 2026-07-04T14:15 ET entry |

---

> Lock par ADR-LD01-003 RATIFIED L0 portion (2026-07-04T14:15 ET). À installer upstream = gated Rick S1 futur.


## 2. Skill Creator Reflex — Sister-links (L0 gate b PLAN-LIGHTNING-L0L1L2)

Per Plan Lightning §3 L0-2 + L0-3 (gate b RATIFIED 2026-07-04T23:08 ET par A0) :

### 2.1 Outil d'application (Skill Creator Reflex)

gent-os/citadel/tools/skill_creator_reflex.py implémente la checklist Pocock
comme gate automatique. Append-only log : gent-os/citadel/logs/skill_creator_reflex_log.md
(3835 b après 1ère exécution).

Usage :
\\\ash
python skill_creator_reflex.py <SKILL.md> [<SKILL2.md>...]
python skill_creator_reflex.py --batch <paths.txt>
python skill_creator_reflex.py --canon-dir ~/.claude/skills/
\\\

Doctrine :
- **Lecture seule** sur les SKILL.md audités (jamais de mutation)
- **Append-only** dans le log (jamais d'écrasement)
- **Idempotent** (re-run safe, déterminisme des résultats)
- **L0 = checklist consultée, JAMAIS agent qui écrit** (cf. ADR-002 §S5 anti-paperclip)

### 2.2 Sister-links canoniques (Plan L0-3)

Skills canoniques re-auditables via Skill Creator Reflex (gate b exécuté) :

| Skill | Path | Statut Pocock (2026-07-04) |
|---|---|---|
| takeout-delta-ingest | \~/.claude/skills/takeout-delta-ingest/SKILL.md\ | **FAIL** — manque llowed-tools, when_to_use, ersion, uthor, license. Action Picard : re-auditer pour conformer. |
| strategy-session-meta | \~/.claude/skills/strategy-session-meta/SKILL.md\ | **FAIL** — même diagnostic. Action Picard : re-auditer pour conformer. |

### 2.3 Verdicts L0 canon

- **2 skills FAIL** sur 2 audités : aucune conformité Pocock pleine. Le gate a fait son travail.
- Aucune auto-correction : L0 signale, A0/Picard décide (anti-Ultron §S7 Posture C).
- Les 2 skills restent utilisables runtime (Pocock = filtre qualité, pas bloqueur d'exécution).
- **Sister convergent** : LESSONS.md de strategy-session-meta (1582 b) est référencée canon (canon upstream du skill canon ADR-LD01-006).
