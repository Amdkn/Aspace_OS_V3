---
type: Backend
title: OKF v0.1 — standard de format d'un bundle mémoire
description: 4ᵉ pilier de la KB Geordi après Wiki/Graphify/Dox — définit ce qu'est un bundle valide (frontmatter, fichiers réservés, consommation permissive). C'est le format dont tous les autres concepts dérivent.
tags: [okf, format, bundle, standard, frontmatter, kb-pilier, geordi]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:30:00Z }
sources:
  - id: okf-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/OKF_INDEX.md"
    title: "OKF — Index du pilier Standard (4ᵉ pilier KB)"
    last_modified: 2026-08-01
  - id: schema-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/schema.md"
    title: "LLM Wiki — Schema (CLAUDE.md Companion)"
    last_modified: 2026-05-10
  - id: kb-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/GEORDI_KB_ROOT.md"
    title: "Geordi — Racine de la Knowledge Base (Second Brain PARA)"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# OKF v0.1 — standard de format d'un bundle mémoire

> **Erreur corrigée le 2026-08-01** : OKF a d'abord été oublié dans la liste des piliers KB
> (l'index racine Geordi ne citait que Wiki/Graphify/Dox) — c'est en fait le **4ᵉ pilier**, et le
> standard qui définit ce qu'est un bundle mémoire valide.

## 1. Définition

Un **bundle OKF** est un répertoire de fichiers `.md` muni de frontmatter YAML, conforme
au schéma OKF. Le wiki LLM_Wiki EST un bundle OKF (point de départ canonique). Graphify et
Dox **consomment** des bundles OKF.

## 2. Anatomie canonique

```
bundle = arbre de .md + frontmatter YAML
```

- Liens **bundle-relatifs** (`./concepts/concept_adr.md`), pas absolus.
- Consommation **permissive** : liens brisés et types inconnus tolérés.
- Frontmatter invalide : **warning dur**, pas repli silencieux.

## 3. Champs frontmatter (matrice de conformité)

| Champ | Requis ? | Rôle |
|---|---|---|
| `type` | **OUI** | Seul champ requis. Détermine le typage du nœud (concept, entity, hand_off…). |
| `title` | recommandé | Titre humain |
| `description` | recommandé | **Critère bloquant d'indexation** dans RESOURCES_INDEX.md |
| `tags` | recommandé | Liste YAML |
| `timestamp` | recommandé | ISO 8601 |
| `okf_version` | **RÉSERVÉ** racine | Uniquement sur `index.md` racine du bundle |
| `source`, `date`, `domain` | producteur | Conservés tels quels |
| `metadata.*` | pré-OKF | À migrer vers top-level |

## 4. Fichiers réservés

| Fichier | Frontmatter | Règle |
|---|---|---|
| `index.md` racine | OUI (seulement `okf_version`) | TOC du bundle |
| `index.md` sous-dossiers | optionnel | Générés par script, jamais édités à main |
| `log.md` | NON | ISO, **newest-first** |
| `ROT.md` | oui | Rot-rate par couche (créé 2026-08-01 dans Geordi) |

## 5. État de conformité dans Geordi au 2026-08-01

- `03_Memory_Unified/LLM_Wiki/wiki/` (cœur structuré, ~60 pages L0+concepts+entities+J01-J04) :
  `type:` à 100 %, `description:` à 0 %.
- `wiki/hand_offs/` (350) : 223/350 (64 %) ont un `type:`.
- `00_Index/` (Geordi méta) : 7/7 conformes.
- Dette principale : **60 pages cœur sans `description:`** (P1.3 du plan maître).

## 6. Loi de flux macro ↔ micro

```
MACRO (canon durable)          MICRO (mémoire de travail, rot rapide)
├── LLM Wiki (bundle OKF)      ├── ~/.claude/projects/.../memory/
├── Graphify master            ├── turn-journal.md
├── PARA Geordi                ├── AGENTS.md locaux (arbre DOX)
├── ADRs _SPECS/               └── agents ~/.claude/agents/
```

**Loi** : le micro **gradue** vers le macro (jamais l'inverse). Le macro **pointe**, ne duplique pas.

## 7. Ce que ce concept n'est pas

- ❌ Pas un outil : OKF est un standard de format, pas un logiciel.
- ❌ Pas un schéma de validation strict : la consommation est permissive.
- ❌ Pas une garantie de vérité : un bundle OKF conforme peut contenir des contre-vérités.

## Liens entrants

- `geordi-kb-quatre-piliers.md` — OKF comme 4ᵉ pilier (Wiki/Graphify/Dox)
- `wiki-schema-llm-wiki.md` — la mise en œuvre concrète d'OKF sur LLM_Wiki
