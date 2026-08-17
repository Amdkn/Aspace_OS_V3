---
type: Playbook
title: Loi du harvest — wiki evergreen depuis artefact shippé
description: Doctrine de récolte du wiki (W22 M5, 2026-07-13) : une page evergreen (concepts/, entities/) n'est créée QUE depuis un artefact shippé (handoff, wargame exécuté, projet clos). Skill canon `/harvest` (72 lignes). Anti-pattern : créer une page SANS artefact shippé = bloquer.
tags: [harvest, wiki, evergreen, sister-artifact, lint-wiki, doctrine, anti-pollution]
generated: { by: minimax-m3, at: 2026-08-17T21:35:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:35:00Z }
sources:
  - id: wiki-index-loi-harvest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md"
    title: "LLM Wiki Index — §Loi du harvest (W22 M5, 2026-07-13)"
    last_modified: 2026-07-13
  - id: wiki-schema
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/schema.md"
    title: "LLM Wiki — Schema (CLAUDE.md Companion)"
    last_modified: 2026-05-10
  - id: compounding-knowledge
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_compounding_knowledge.md"
    title: "Concept: Compounding Knowledge"
    last_modified: 2026-05-11
okf_version: "0.2"
---

# Loi du harvest — wiki evergreen depuis artefact shippé

> **Le wiki se récolte, ne s'écrit pas.** Une page evergreen (`concepts/`, `entities/`)
> n'est créée QUE depuis un artefact shippé (handoff, wargame exécuté, projet clos).
>
> Skill canon : `/harvest` (`~/.claude/skills/harvest/SKILL.md`, 72 lignes),
> sister of `/lint-wiki` + `/sessions-archive`.

## 1. Pourquoi cette doctrine existe

Le wiki A'Space OS a accumulé fin 2025 / début 2026 plusieurs centaines de pages
evergreen sans artefact source, ce qui :

- Polluait la mémory de compounding (des pages sans fondement live)
- Multipliait les contradictions intra-wiki (pas de source canonique arbitre)
- Ralentissait le lint (chaque page = orpheline candidate, transverses non-vérifiés)

D'où la canonisation datée du **2026-07-13** (W22 M5) dans le wiki lui-même.

## 2. La règle (verbe canonique)

| Action | Condition | Anti-pattern |
|---|---|---|
| Créer `concepts/<topic>.md` | Doit citer **un** sister artifact shippé (handoff, wargame exec, projet clos) | Créer une page evergreen SANS citer sister artifact = **bloquer** |
| Mettre à jour `entities/<actor>.md` | Doit citer **un** sister artifact | Idem |
| Créer `sources/<source>.md` | Doit citer **un** raw (PDF, transcript) | (sources peuvent être brutes si raw existe) |
| Créer `hand_offs/<handoff>.md` | Doit dater la session + lister 1 takeaway + 1 prochain pas | (hand_offs toujours autorisés, c'est le sas) |
| Mettre à jour `wiki/index.md` | Régénéré par `bin/gen_wiki_index.py`, **jamais édit à main** | Editer à la main = pollution |

## 3. Skill `/harvest` (extrait canon)

```yaml
triggers:
  - "récolter cette session en concept"
  - "jeter ce handoff dans le wiki"
  - "distiller cette exécution"
output:
  - Création d'une page `concepts/<slug>.md`
  - Mise à jour des `entities/` concernées
  - Append dans `wiki/log.md`
  - Catégorisation `[## YYYY-MM-DD] harvest`
preconditions:
  - Handoff ou wargame exécuté existe
  - Sister artifact lisible
artifact_obligation:
  - sister: <path/to/handoff_or_wargame.md>
  - relation: extracted-from
artifacts_touched:
  - "~/.claude/skills/harvest/SKILL.md"
```

## 4. Anti-patterns (avec exemples)

| Anti-pattern | Pourquoi c'est faux |
|---|---|
| Page `concepts/agentic_loop.md` sans sister artifact | Compounding fantôme — l'agent futur ne peut pas remonter à la source |
| Page `entities/doctor_strange.md` sans sister artifact | Induit confusion avec le membre Notion canon (Sales/Illuminati) |
| Editer `wiki/index.md` à la main | Le générateur `bin/gen_wiki_index.py` recalcule ; l'édition à la main dérive |

## 5. Exceptions nommées

- **Clés de voûte doctrinales** (`schema.md`, `index.md`, `CLAUDE.md` racine) : pilotent
  le wiki, autorisées à exister sans sister artifact.
- **Pages méta** (`Loi du harvest`, ce fichier) : auto-référentielles.

## 6. Sister canon

- **Skill source** : `~/.claude/skills/harvest/SKILL.md` (72 lignes)
- **Wargame originel** : `wiki/hand_offs/wargame_22_fable_execution_2026-07-12.md`
- **Ranking** : `wiki/hand_offs/EXECUTION-RANKING.md` (W22 M2)

## 7. Tension Constitution v1.0

Article 4 : « auto-amélioration continue comme devoir ». La **loi du harvest** n'est **pas**
une gate bloquante (Article 6). Elle se vit comme une **discipline** : un agent qui crée
une page evergreen sans sister artifact commet une erreur de curation, pas un blocage.

En pratique, `/lint-wiki` (sister skill) flagge les pages sans artefact cité, et l'agent
A0 arbitre. Le système reste non-bloquant.

## Liens entrants

- `wiki-schema-llm-wiki.md` — la procédure formelle (ingest / query / lint)
- `compounding-knowledge-wiki.md` — le compounding survit si le wiki est curé
- `geordi-kb-quatre-piliers.md` — où loge cette doctrine dans les 4 piliers
